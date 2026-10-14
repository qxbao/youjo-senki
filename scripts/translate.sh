#!/usr/bin/env bash
set -euo pipefail
umask 077

ROOT=$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." && pwd -P)
CONFIG="$ROOT/config/translation-pipeline.yml"
STATE="$ROOT/work/run-state"
SESSION="$STATE/herdr-session.json"
CHECKPOINT="$STATE/translation-coordinator.yml"
DRY_RUN=false
PYTHON=python3
[[ ! -x "$ROOT/.venv/bin/python" ]] || PYTHON="$ROOT/.venv/bin/python"

usage() {
  printf '%s\n' 'Usage: scripts/translate.sh {up|status|down|resume|logs|doctor} [--dry-run]' \
    '--dry-run is supported only for up/down; it performs no filesystem or Herdr mutations.'
}
fail() { printf 'ERROR: %s\n' "$*" >&2; exit 1; }
[[ $# -ge 1 && $# -le 2 ]] || { usage >&2; exit 2; }
ACTION=$1
case "$ACTION" in up|status|down|resume|logs|doctor) ;; *) usage >&2; exit 2 ;; esac
if [[ $# == 2 ]]; then
  [[ $2 == --dry-run && ( $ACTION == up || $ACTION == down ) ]] || { usage >&2; exit 2; }
  DRY_RUN=true
fi
cd -- "$ROOT"

require_session() {
  [[ -f "$SESSION" && ! -L "$SESSION" ]] || fail 'Missing safe session file. Run scripts/translate.sh up inside Herdr; down will not discover or close other panes.'
  jq -e --arg root "$ROOT" '
    .schema_version == 1 and .managed_by == "youjo-translation-pipeline" and
    .project_root == $root and (.workspace_id | type == "string") and
    (.tab_id | type == "string") and (.owned_panes | type == "array") and
    (.owned_panes | length > 0) and
    all(.owned_panes[]; (.pane_id | type == "string") and
      (.terminal_id | type == "string") and
      (.role == "coordinator" or .role == "translator" or .role == "reviewer" or
       .role == "polisher" or .role == "semantic_regression" or .role == "recovery")) and
    ([.owned_panes[].pane_id] | length == (unique | length)) and
    ([.owned_panes[] | select(.role == "coordinator")] | length == 1)
  ' "$SESSION" >/dev/null || fail 'Session schema/owner/IDs invalid. Inspect work/run-state/herdr-session.json; do not adopt IDs by hand.'
}

load_config() {
  CFG=$("$PYTHON" - "$CONFIG" "$ROOT" <<'PY'
import json, pathlib, sys
import yaml
p, root = pathlib.Path(sys.argv[1]), pathlib.Path(sys.argv[2])
try:
    c = yaml.safe_load(p.read_text())
    assert isinstance(c, dict) and c.get('schema_version') == 1, 'schema_version must be 1'
    assert c.get('project') == 'youjo-senki-vi', 'project must be youjo-senki-vi'
    expected = {'local_config': 'project.local.yml', 'manifests': 'segments/vol-*/manifest.yml',
        'handoffs': 'handoffs/', 'translations': 'translations/', 'polish_candidates': 'polish-candidates/', 'state_dir': 'work/run-state',
        'session': 'work/run-state/herdr-session.json',
        'checkpoint': 'work/run-state/translation-coordinator.yml',
        'pending': 'work/run-state/pending-terms.yml'}
    assert c['paths'] == expected, 'paths must match the repository-relative pipeline paths'
    assert c['scope']['volumes'] == 'all_available_in_source_dir' and c['scope']['include'] == ['story'], 'scope must include story across available volumes'
    assert c['batch']['min_source_words'] == 600 and c['batch']['max_source_words'] == 900, 'batch target must be 600–900'
    assert c['batch']['sequential_workers'] is False, 'independent worker streams must be enabled'
    concurrency = c['batch']['concurrency']
    assert concurrency['max_parallel_workers'] == 2 and concurrency['require_disjoint_allowlists'] is True, 'worker concurrency must be capped at two with disjoint allowlists'
    assert concurrency['canonical_translation_writer'] == 'one_at_a_time' and concurrency['candidate_root'] == 'polish-candidates/', 'canonical writer/candidate isolation invalid'
    assert c['stages'] == ['translator_luna', 'terminology_review_argon', 'prose_polish_gemini', 'semantic_regression_luna'], 'stages must preserve translation, terminology, polish, semantic-check order'
    assert c['review']['every_batch'] is True, 'terminology review is required for every batch before polishing'
    assert set(c['review']['risk_flags']) == {'meaning', 'new_pending_terms', 'emphasis', 'validator_warning'}, 'review risk_flags invalid'
    assert c['gemini']['enabled'] is True and c['gemini']['writes_only'] == 'polish-candidates/', 'Gemini must write isolated polish candidates only'
    assert c['gemini']['preserve_locked_choices'] is True, 'Gemini must preserve locked choices'
    assert c['gemini']['candidate_pattern'] == 'polish-candidates/vol-*/ch-*-b*.gemini.jsonl', 'Gemini must use the isolated polish-candidates tree'
    assert set(c['acceptance']['reject_on']) == {'critical', 'locked_choice_violation'}, 'acceptance must reject critical and locked-choice regressions'
    assert c['acceptance']['coordinator_only'] is True, 'only coordinator may promote candidates'
    assert c['acceptance']['require_semantic_receipt'] is True, 'promotion requires a semantic receipt'
    assert c['pending_terms']['automatic_canon_promotion'] is False, 'automatic canon promotion must be disabled'
    assert c['checkpoint']['after_each_batch'] is True and c['checkpoint']['compact_after_batches'] == 4, 'checkpoint/compact cadence invalid'
    assert c['checkpoint']['compact_on_context_warning'] is True and c['checkpoint']['summary_max_words'] == 500, 'context/summary policy invalid'
    required = {'validator_failure', 'diff_check_failure', 'unresolved_serious_error', 'out_of_scope_git_change', 'agent_or_herdr_failure', 'plot_affecting_canon_decision', 'preparation_required'}
    assert required <= set(c['hard_stops']), 'missing hard-stop policy'
    r = c['runtime']
    for role in ('codex', 'semantic_regression'):
        a = r[role]
        expected = {'launcher_alias': 'codex-personal', 'via': 'ai-isolator',
            'model': 'gpt-6-luna', 'effort': 'medium', 'sandbox': 'danger-full-access',
            'approval_policy': 'never'}
        assert isinstance(a, dict), f'runtime.{role} must be a mapping'
        assert set(a) == set(expected) | {'source_rc'}, f'runtime.{role} fields invalid'
        for key, value in expected.items():
            assert a[key] == value, f'runtime.{role}.{key} must be {value}'
        assert a['source_rc'] in ('~/.zshrc', '/home/$USER/.zshrc'), f'runtime.{role}.source_rc must be ~/.zshrc or /home/$USER/.zshrc'
    for role, model in (('coordinator', 'gemini-4-argon-medium'), ('reviewer', 'gemini-4-argon-medium'), ('gemini', 'gemini-3.8-flash-medium')):
        a = r[role]
        expected = {'launcher_alias': 'agy', 'via': 'agy', 'model': model, 'effort': 'medium',
            'mode': 'auto', 'approval_policy': 'never'}
        assert isinstance(a, dict), f'runtime.{role} must be a mapping'
        extra = {'source_rc'}
        if role in ('coordinator', 'reviewer'):
            extra.add('effort_flag')
        assert set(a) == set(expected) | extra, f'runtime.{role} fields invalid'
        for key, value in expected.items():
            assert a[key] == value, f'runtime.{role}.{key} must be {value}'
        if role in ('coordinator', 'reviewer'):
            assert a.get('effort_flag') == 'omit_model_variant_encodes_medium', f'runtime.{role}.effort_flag must omit unsupported --effort for this model variant'
        assert a['source_rc'] in ('~/.zshrc', '/home/$USER/.zshrc'), f'runtime.{role}.source_rc must be ~/.zshrc or /home/$USER/.zshrc'
    assert r['herdr_required_env'] is True and r['preserve_tab_and_cwd'] is True and r['reuse_current_workspace'] is True and r['focus'] is False, 'Herdr topology policy invalid'
    assert 1 <= r['ready_timeout_seconds'] <= 60 and 1000 <= r['shutdown_timeout_ms'] <= 60000, 'runtime timeout outside supported limits'
    for k in ('validator', 'extraction', 'batch_planner', 'polished_promotion'):
        tool = pathlib.Path(c['tools'][k])
        assert not tool.is_absolute() and '..' not in tool.parts and (root / tool).is_file(), f'missing/unsafe tools.{k}'
    for name in ('shared', 'coordinator', 'translator', 'reviewer', 'recovery', 'gemini-polisher', 'semantic-regression-checker'):
        assert (root / 'agents' / f'{name}.md').is_file(), f'missing agents/{name}.md'
    local = yaml.safe_load((root / c['paths']['local_config']).read_text())
    assert isinstance(local, dict) and isinstance(local.get('source_dir'), str), 'project.local.yml requires source_dir'
    src = pathlib.Path(local['source_dir']).expanduser()
    if not src.is_absolute(): src = root / src
    src = src.resolve()
    assert src.is_dir(), 'source_dir does not exist; set project.local.yml:source_dir to the existing source directory'
    assert any(x.is_file() and x.suffix.lower() == '.epub' for x in src.iterdir()), 'source_dir contains no EPUB; select the directory containing the existing books'
    print(json.dumps(c))
except (AssertionError, KeyError, TypeError, ValueError, OSError, yaml.YAMLError) as e:
    print(f'Config error: {e}. Run: ${{EDITOR:-vi}} config/translation-pipeline.yml; or ${{EDITOR:-vi}} project.local.yml; then scripts/translate.sh doctor.', file=sys.stderr)
    if not (root / 'project.local.yml').is_file():
        print('Local config missing. Run: cp project.local.example.yml project.local.yml; then edit source_dir in project.local.yml.', file=sys.stderr)
    sys.exit(1)
PY
  )
}

runtime_shell() {
  local role=$1 mode=$2 rc code launcher model effort effort_flag mode_value
  rc=$(jq -r --arg role "$role" '.runtime[$role].source_rc' <<<"$CFG")
  case "$rc" in
    '~/.zshrc') code='export DISABLE_AUTO_UPDATE=true; source "$HOME/.zshrc" || exit 1;' ;;
    '/home/$USER/.zshrc') code='export DISABLE_AUTO_UPDATE=true; source "/home/$USER/.zshrc" || exit 1;' ;;
    *) fail "Unsupported runtime.$role.source_rc" ;;
  esac
  if [[ $(jq -r --arg role "$role" '.runtime[$role].via' <<<"$CFG") == agy ]]; then
    code+=' command -v agy >/dev/null || exit 1;'
    case "$mode" in
      help) code+=' agy --help' ;;
      models) code+=' agy models' ;;
      launch)
        launcher=$(jq -r --arg role "$role" '.runtime[$role].launcher_alias' <<<"$CFG")
        model=$(jq -r --arg role "$role" '.runtime[$role].model' <<<"$CFG")
        effort=$(jq -r --arg role "$role" '.runtime[$role].effort' <<<"$CFG")
        effort_flag=$(jq -r --arg role "$role" '.runtime[$role].effort_flag // empty' <<<"$CFG")
        mode_value=$(jq -r --arg role "$role" '.runtime[$role].mode' <<<"$CFG")
        if [[ $effort_flag == omit_model_variant_encodes_medium ]]; then
          code+=" $launcher --model $model --mode $mode_value --dangerously-skip-permissions"
        else
          code+=" $launcher --model $model --effort $effort --mode $mode_value --dangerously-skip-permissions"
        fi
        ;;
      probe) ;;
      *) fail "Unsupported agy probe mode: $mode" ;;
    esac
  else
    code+=' a=$(alias codex-personal 2>/dev/null) || exit 1; [[ $a == *ai-isolator* && $a == *"run codex"* && $a == *"--name personal"* ]] || exit 1;'
    if [[ $mode == launch ]]; then
      code+=" eval \"$(jq -r --arg role "$role" '.runtime[$role] | "\(.launcher_alias) --model \(.model) --config model_reasoning_effort=\(.effort) --sandbox \(.sandbox) --ask-for-approval \(.approval_policy)"' <<<"$CFG")\""
    fi
  fi
  printf '%s\n' "$code"
}

doctor() {
  local errors=0 cmd status help_text role model models flag config_ready=false
  for cmd in git herdr jq zsh flock "$PYTHON"; do
    if ! command -v "$cmd" >/dev/null 2>&1; then
      printf 'ERROR: missing %s. Install it via the system package manager; rerun scripts/translate.sh doctor.\n' "$cmd" >&2
      errors=$((errors + 1))
    fi
  done
  (( errors == 0 )) || return 1
  if ! "$PYTHON" -c 'import yaml' >/dev/null 2>&1; then
    printf 'ERROR: PyYAML missing. Run: uv sync; then scripts/translate.sh doctor\n' >&2
    errors=$((errors + 1))
  elif load_config; then config_ready=true
  else errors=$((errors + 1)); fi
  if ! git rev-parse --show-toplevel >/dev/null 2>&1; then
    printf 'ERROR: project is not a Git checkout. Run this script from the project checkout.\n' >&2
    errors=$((errors + 1))
  elif [[ $(git rev-parse --show-toplevel) != "$ROOT" ]]; then
    printf 'ERROR: script root differs from Git root. Move the pipeline files to the repository root.\n' >&2
    errors=$((errors + 1))
  else
    if [[ -n $(git status --porcelain) ]]; then
      printf 'ERROR: Git has changes outside a running batch. Run git status --short; preserve/review those changes before up/resume.\n' >&2
      errors=$((errors + 1))
    fi
    if ! git check-ignore -q work/run-state/herdr-session.json || [[ -n $(git ls-files -- work/run-state) ]]; then
      printf 'ERROR: run-state is not safely ignored/untracked. Add /work/run-state/ to .gitignore; if already tracked, review git rm --cached for those exact paths.\n' >&2
      errors=$((errors + 1))
    fi
  fi
  if [[ ${HERDR_ENV:-} != 1 ]]; then
    printf 'ERROR: HERDR_ENV must be 1. Open this checkout in a Herdr-managed pane and run scripts/translate.sh doctor there.\n' >&2
    errors=$((errors + 1))
  elif ! status=$(herdr status 2>&1); then
    printf 'ERROR: Herdr is inaccessible. Run herdr status in the intended session; repair that session manually, then rerun doctor. No server will be started here.\n' >&2
    errors=$((errors + 1))
  elif [[ $status != *'endpoint_compatible: yes'* || $status != *'private_protocol_compatible: yes'* ]]; then
    printf 'ERROR: Herdr client/server incompatible. Inspect herdr status and resolve the version mismatch manually.\n' >&2
    errors=$((errors + 1))
  else
    help_text=$(herdr --help 2>&1)
    [[ $help_text == *'herdr agent'* ]] || { printf 'ERROR: missing Herdr agent CLI. Update the client manually.\n' >&2; errors=$((errors + 1)); }
    help_text=$(herdr agent 2>&1 || true)
    [[ $help_text == *'herdr agent prompt'* && $help_text == *'herdr agent rename'* ]] || { printf 'ERROR: unsupported Herdr agent syntax. Inspect herdr agent.\n' >&2; errors=$((errors + 1)); }
    help_text=$(herdr pane 2>&1 || true)
    [[ $help_text == *'herdr pane split'* && $help_text == *'herdr pane process-info'* ]] || { printf 'ERROR: unsupported Herdr pane syntax. Inspect herdr pane.\n' >&2; errors=$((errors + 1)); }
    herdr --skill >/dev/null || { printf 'ERROR: herdr --skill failed. Inspect herdr status.\n' >&2; errors=$((errors + 1)); }
  fi
  if $config_ready; then
    for role in codex semantic_regression; do
      if ! DISABLE_AUTO_UPDATE=true zsh -ic "$(runtime_shell "$role" probe)" >/dev/null 2>&1; then
        printf 'ERROR: runtime.%s codex-personal alias through ai-isolator missing. Inspect source_rc in config/translation-pipeline.yml and define the alias there.\n' "$role" >&2
        errors=$((errors + 1))
      fi
    done
    for role in coordinator reviewer gemini; do
      if ! help_text=$(DISABLE_AUTO_UPDATE=true zsh -ic "$(runtime_shell "$role" help)" 2>&1); then
        printf 'ERROR: runtime.%s agy unavailable. Inspect source_rc and agy --help in that shell.\n' "$role" >&2
        errors=$((errors + 1))
        continue
      fi
      for flag in --model --effort --mode --dangerously-skip-permissions; do
        if [[ $help_text != *"$flag"* ]]; then
          printf 'ERROR: runtime.%s agy lacks %s. Inspect agy --help; update the configured CLI manually.\n' "$role" "$flag" >&2
          errors=$((errors + 1))
        fi
      done
      model=$(jq -r --arg role "$role" '.runtime[$role].model' <<<"$CFG")
      if ! models=$(DISABLE_AUTO_UPDATE=true zsh -ic "$(runtime_shell "$role" models)" 2>&1); then
        printf 'ERROR: runtime.%s cannot list agy models. Run agy models in the configured shell.\n' "$role" >&2
        errors=$((errors + 1))
      elif [[ ! $models =~ (^|[^[:alnum:]_-])$model([^[:alnum:]_-]|$) ]]; then
        printf 'ERROR: runtime.%s model %s unavailable in agy models. Select an available explicit model ID in config/translation-pipeline.yml.\n' "$role" "$model" >&2
        errors=$((errors + 1))
      fi
    done
  fi
  printf 'NOTE: source-preparation adapters cover LN 01–14 via TOC/NCX; missing manifests/packages require preparation. No book was opened.\n'
  (( errors == 0 )) || return 1
  printf 'OK: config, Git, tools, source directory and Herdr are ready.\n'
}

need_herdr() {
  [[ ${HERDR_ENV:-} == 1 ]] || fail 'Run inside Herdr (HERDR_ENV=1).'
  herdr status >/dev/null || fail 'Herdr inaccessible; no alternate orchestration backend.'
}

lock_state() {
  [[ ! -L "$ROOT/work" && ! -L "$STATE" ]] || fail 'Refusing symlinked run-state directory.'
  mkdir -p -- "$STATE"
  exec 9>"$STATE/translation.lock"
  flock -n 9 || fail 'Another translate.sh operation holds the session lock.'
}

save_state() {
  local tmp
  tmp=$(mktemp "$STATE/session.XXXXXX")
  jq . <<<"$DATA" >"$tmp"
  mv -- "$tmp" "$SESSION"
}

event() {
  # Store only control metadata, never prompts, screen contents, paths or environment.
  [[ ! -L "$STATE/events.jsonl" ]] || fail 'Refusing symlinked event log.'
  jq -cn --arg action "$1" --arg at "$(date -u +%FT%TZ)" '{at:$at,event:$action}' >>"$STATE/events.jsonl"
}

pane_record() {
  local id=$1 expected=$2 live
  if ! live=$(herdr pane get "$id" 2>/dev/null); then
    printf 'missing\n'; return
  fi
  jq -e --arg root "$ROOT" --arg terminal "$expected" \
    --arg ws "$(jq -r .workspace_id "$SESSION")" --arg tab "$(jq -r .tab_id "$SESSION")" '
    .result.pane.terminal_id == $terminal and .result.pane.cwd == $root and
    .result.pane.workspace_id == $ws and .result.pane.tab_id == $tab and
    (.result.pane.foreground_cwd == null or .result.pane.foreground_cwd == $root)
  ' <<<"$live" >/dev/null || fail "Pane ownership/cwd mismatch: $id. Inspect herdr pane get $id; no pane will be closed."
  printf '%s\n' "$live"
}

verify_owned() {
  local record id terminal live expected actual state process
  while IFS= read -r record; do
    id=$(jq -r .pane_id <<<"$record")
    [[ $id != "${HERDR_PANE_ID:-}" ]] || fail "Refusing to stop the calling pane $id. Run down from another managed pane."
    terminal=$(jq -r .terminal_id <<<"$record")
    live=$(pane_record "$id" "$terminal")
    [[ $live != missing ]] || continue
    expected=$(jq -r '.agent_session_id // ""' <<<"$record")
    actual=$(jq -r '.result.pane.agent_session.value // ""' <<<"$live")
    if [[ -n $(jq -r '.result.pane.agent // ""' <<<"$live") ]]; then
      [[ -n $expected && $actual == "$expected" ]] || fail "Agent occupant changed in $id. Read the screen and reconcile ownership manually."
      if [[ ${1:-identity} == settled ]]; then
        state=$(jq -r .result.pane.agent_status <<<"$live")
        [[ $state == idle || $state == done ]] || fail "Owned agent $id is $state; checkpoint/stop protocol not settled. Read it first."
      fi
    else
      process=$(herdr pane process-info --pane "$id")
      jq -e '.result.process_info.foreground_process_group_id == .result.process_info.shell_pid' <<<"$process" >/dev/null || fail "Unrecognized foreground process in $id; refusing to close it."
    fi
  done < <(jq -c '.owned_panes[]' "$SESSION")
}

launch_coordinator() {
  local pane=$1 mode=$2 name=$3 live status ready=0 limit i prompt launch expected_agent expected_model process command_line banner
  launch=$("$PYTHON" -c 'import shlex, sys; print("zsh -ic " + shlex.quote(sys.argv[1]))' "$(runtime_shell coordinator launch)")
  expected_agent=$(jq -r '.runtime.coordinator.via' <<<"$CFG")
  expected_model=$(jq -r '.runtime.coordinator.model' <<<"$CFG")
  herdr pane run "$pane" "$launch"
  limit=$(jq -r .runtime.ready_timeout_seconds <<<"$CFG")
  for ((i=0; i<limit; i++)); do
    live=$(herdr pane get "$pane")
    status=$(jq -r '.result.pane.agent_status // "unknown"' <<<"$live")
    if [[ $status == blocked ]]; then
      herdr agent read "$pane" --source visible --lines 50
      fail "Coordinator startup blocked in $pane; inspect before any further input."
    fi
    if [[ $(jq -r '.result.pane.agent // ""' <<<"$live") == "$expected_agent" && ( $status == idle || $status == done ) ]]; then ready=1; break; fi
    sleep 1
  done
  (( ready == 1 )) || { herdr pane read "$pane" --source visible --lines 50; fail 'Coordinator did not become ready; command may have been received. Do not resend automatically.'; }
  process=$(herdr pane process-info --pane "$pane")
  command_line=$(jq -r '[.result.process_info.foreground_processes[]?.cmdline] | join(" ")' <<<"$process")
  [[ $command_line == *"--model $expected_model"* ]] || fail "Coordinator model preflight failed in $pane; expected $expected_model in process argv. No task was sent."
  if [[ $(jq -r '.runtime.coordinator.effort_flag // ""' <<<"$CFG") == omit_model_variant_encodes_medium && $command_line == *'--effort'* ]]; then
    fail "Coordinator runtime must omit --effort for $expected_model. No task was sent."
  fi
  banner=$(herdr pane read "$pane" --source recent-unwrapped --lines 60)
  [[ $banner == *'Gemini 4 Argon (Medium)'* ]] || fail "Coordinator model banner did not confirm Gemini 4 Argon Medium in $pane. No task was sent."
  herdr agent rename "$pane" "$name" >/dev/null
  live=$(herdr agent get "$pane")
  # Agent CLIs may expose their session ID only after the first submitted turn.
  DATA=$(jq '.prompt_delivery="dispatching"' <<<"$DATA")
  save_state
  prompt='Read agents/shared.md, agents/coordinator.md and config/translation-pipeline.yml. Start the continuous coordinator loop from manifests/handoffs/Git/checkpoint. Obey role write boundaries; no direct translation. Register every owned worker pane in work/run-state/herdr-session.json immediately. Never repeat uncertain prompt delivery. Create checkpoint before any worker task.'
  if [[ $mode == recovery ]]; then
    prompt='Read agents/shared.md, agents/recovery.md, agents/coordinator.md and config/translation-pipeline.yml. Recover solely from checkpoint/Git/handoff/Herdr ownership; no old conversation history. ACK checkpoint_generation and then run the continuous coordinator loop. Register every owned worker pane in work/run-state/herdr-session.json immediately.'
  fi
  if ! herdr agent prompt "$pane" "$prompt" >/dev/null; then
    herdr agent read "$pane" --source visible --lines 50 || true
    fail 'Prompt submission uncertain; session retained. Inspect the agent before retrying.'
  fi
  DATA=$(jq '.prompt_delivery="submitted" | .state="running"' <<<"$DATA")
  save_state
  for ((i=0; i<limit; i++)); do
    live=$(herdr agent get "$pane")
    local sid
    sid=$(jq -r '.result.agent.agent_session.value // empty' <<<"$live")
    if [[ -n $sid ]]; then
      DATA=$(jq --arg pane "$pane" --arg sid "$sid" '.owned_panes |= map(if .pane_id==$pane then .agent_session_id=$sid else . end)' <<<"$DATA")
      save_state
      break
    fi
    if [[ $(jq -r '.result.agent.agent_status' <<<"$live") == blocked ]]; then
      herdr agent read "$pane" --source visible --lines 50
      fail 'Coordinator blocked after submission; no duplicate prompt will be sent.'
    fi
    sleep 1
  done
  [[ -n ${sid:-} ]] || fail 'Submitted prompt has no session identity yet. Inspect the owned pane; do not redispatch.'
  event coordinator_dispatched
  printf 'Coordinator dispatched in owned pane %s. Use status/logs; do not rerun the same prompt.\n' "$pane"
}

up() {
  local mode=$1 current pane terminal tab workspace name live owned process
  doctor || fail 'Preflight failed; see doctor remedies above.'
  if [[ -f "$SESSION" ]]; then
    require_session
    verify_owned
    owned=$(jq -c '.owned_panes[] | select(.role=="coordinator")' "$SESSION")
    pane=$(jq -r .pane_id <<<"$owned")
    live=$(pane_record "$pane" "$(jq -r .terminal_id <<<"$owned")")
    if [[ $live != missing && -n $(jq -r '.result.pane.agent // ""' <<<"$live") ]]; then
      [[ $(jq -r '.prompt_delivery // ""' "$SESSION") == submitted ]] || fail 'Previous prompt delivery is uncertain. Inspect the saved pane; do not redispatch.'
      if [[ $(jq -r .result.pane.agent_status <<<"$live") == blocked ]]; then
        herdr agent read "$pane" --source visible --lines 50
        fail 'Existing coordinator blocked; inspect its question/error before recovery.'
      fi
      if [[ $mode == recovery && $(jq -r .result.pane.agent_status <<<"$live") != working ]]; then
        [[ -f "$CHECKPOINT" ]] || fail 'resume requires a checkpoint.'
        lock_state
        DATA=$(jq '.prompt_delivery="dispatching"' "$SESSION")
        save_state
        if ! herdr agent prompt "$pane" 'Read agents/shared.md and agents/recovery.md. Reconcile checkpoint/Git/handoffs and pane identities; ACK the recovered generation, then continue coordinator.md. Do not rely on old conversation history or repeat an uncertain worker prompt.' >/dev/null; then
          herdr agent read "$pane" --source visible --lines 50 || true
          fail 'Recovery prompt delivery uncertain; inspect before resubmitting.'
        fi
        DATA=$(jq '.prompt_delivery="submitted" | .state="running"' <<<"$DATA")
        save_state
        event recovery_dispatched
        printf 'Recovery dispatched to owned coordinator %s.\n' "$pane"
        return
      fi
      printf 'Existing coordinator retained in %s; no duplicate launch or prompt.\n' "$pane"
      return
    fi
    if [[ $mode == recovery ]]; then
      [[ -f "$CHECKPOINT" ]] || fail 'resume requires a checkpoint. Inspect local run-state and Git; do not invent a completed batch.'
      "$PYTHON" - "$CHECKPOINT" <<'PY'
import sys, yaml
c = yaml.safe_load(open(sys.argv[1]))
if not isinstance(c, dict) or c.get('active_translation_editor') or c.get('active_worker'):
    raise SystemExit('Checkpoint invalid or live lease unresolved; inspect worker identity before recovery.')
PY
    fi
  elif [[ $mode == recovery ]]; then
    fail 'resume requires herdr-session.json; use up for a new owned session after reconciling checkpoint/Git.'
  fi
  if $DRY_RUN; then
    printf 'DRY-RUN: validate current workspace; create one sibling project pane if needed; launch codex-personal coordinator. No files/panes/agents changed.\n'
    return
  fi
  lock_state
  # Reload after acquiring lock; concurrent invocation must never duplicate a pane.
  if [[ -f "$SESSION" ]]; then
    require_session
    [[ $(jq -r '.state' "$SESSION") == stopped || $mode == recovery ]] || fail 'Session exists; use status/resume after inspecting ownership.'
    if [[ $mode == recovery ]]; then verify_owned settled; fi
  fi
  current=$(herdr pane current --current)
  tab=$(jq -er .result.pane.tab_id <<<"$current")
  workspace=$(jq -er .result.pane.workspace_id <<<"$current")
  if [[ $mode == recovery && -f "$SESSION" ]]; then
    [[ $workspace == "$(jq -r .workspace_id "$SESSION")" && $tab == "$(jq -r .tab_id "$SESSION")" ]] || fail 'Run resume from the saved workspace/tab to restore a missing coordinator. No pane was created in another tab.'
  fi
  if [[ -n ${owned:-} && ${live:-missing} != missing ]]; then
    process=$(herdr pane process-info --pane "$pane")
    jq -e '.result.process_info.foreground_process_group_id == .result.process_info.shell_pid' <<<"$process" >/dev/null || fail 'Recovery pane is not a foreground shell.'
    DATA=$(jq '.prompt_delivery="not_sent" | .state="starting"' "$SESSION")
    name=$(jq -r .coordinator_name <<<"$DATA")
  else
    # Register creation result immediately; never adopt or close the caller's pane.
    local direction=down layout
    layout=$(herdr pane layout --current)
    if jq -e '.result.layout.area.width > (2 * .result.layout.area.height)' <<<"$layout" >/dev/null; then direction=right; fi
    live=$(herdr pane split --current --direction "$direction" --cwd "$ROOT" --env DISABLE_AUTO_UPDATE=true --no-focus)
    pane=$(jq -er .result.pane.pane_id <<<"$live")
    terminal=$(jq -er .result.pane.terminal_id <<<"$live")
    name="ys-coord-$(date +%s)"
    DATA=$(jq -cn --arg root "$ROOT" --arg pane "$pane" --arg terminal "$terminal" --arg tab "$tab" --arg ws "$workspace" --arg name "$name" \
      '{schema_version:1,managed_by:"youjo-translation-pipeline",project_root:$root,workspace_id:$ws,tab_id:$tab,coordinator_name:$name,state:"starting",prompt_delivery:"not_sent",owned_panes:[{role:"coordinator",pane_id:$pane,terminal_id:$terminal,agent_session_id:null}]}')
    if [[ $mode == recovery && -f "$SESSION" ]]; then
      DATA=$(jq --argjson new "$DATA" '.owned_panes = ([.owned_panes[] | select(.role!="coordinator")] + $new.owned_panes) | .state="starting" | .prompt_delivery="not_sent" | .coordinator_name=$new.coordinator_name | .workspace_id=$new.workspace_id | .tab_id=$new.tab_id' "$SESSION")
    fi
  fi
  save_state
  event coordinator_pane_registered
  launch_coordinator "$pane" "$mode" "$name"
}

down() {
  require_session # Includes dry-run: no session means no shutdown authority.
  need_herdr
  load_config
  verify_owned
  if [[ $(jq -r .state "$SESSION") == stopped ]]; then printf 'Already stopped.\n'; return; fi
  if $DRY_RUN; then
    printf 'DRY-RUN: request checkpoint ACK, verify every saved identity, close only saved owned panes. No files/panes/agents changed.\n'
    jq -r '.owned_panes[] | "owned: \(.role) \(.pane_id)"' "$SESSION"
    return
  fi
  lock_state
  require_session
  verify_owned
  local pane token timeout record id live
  pane=$(jq -r '.owned_panes[] | select(.role=="coordinator") | .pane_id' "$SESSION")
  live=$(herdr agent get "$pane") || fail 'Coordinator missing; cannot obtain a fresh checkpoint ACK. Resume/reconcile before down.'
  if [[ $(jq -r .result.agent.agent_status <<<"$live") == blocked ]]; then
    herdr agent read "$pane" --source visible --lines 50
    fail 'Coordinator blocked; no shutdown prompt sent and no pane closed.'
  fi
  token=$("$PYTHON" -c 'import uuid; print(uuid.uuid4())')
  DATA=$(jq --arg token "$token" '.shutdown_request=$token | .state="checkpoint_requested"' "$SESSION")
  save_state
  timeout=$(jq -r .runtime.shutdown_timeout_ms <<<"$CFG")
  # One submission only; a timeout never triggers a second prompt or teardown.
  if ! herdr agent prompt "$pane" "Shutdown request $token. Stop dispatching now. Finish/cancel workers at a safe boundary, release translation lease, and atomically write checkpoint with shutdown.request_id=$token and shutdown.acknowledged=true. ACK only when all workers are idle/exited. Do not start another batch." --wait --timeout "$timeout" >/dev/null; then
    herdr agent read "$pane" --source visible --lines 50 || true
    fail 'Checkpoint request did not settle; no pane closed. Inspect checkpoint and agent before retrying.'
  fi
  "$PYTHON" - "$CHECKPOINT" "$token" <<'PY'
import sys, yaml
try:
    c = yaml.safe_load(open(sys.argv[1]))
    assert isinstance(c, dict) and c['shutdown']['request_id'] == sys.argv[2]
    assert c['shutdown']['acknowledged'] is True
    assert not c.get('active_translation_editor') and not c.get('active_worker')
except (OSError, KeyError, TypeError, AssertionError, yaml.YAMLError):
    raise SystemExit('No fresh checkpoint ACK/lease release. No pane may be closed; inspect run-state and coordinator.')
PY
  verify_owned settled
  # Workers first, coordinator last. Workspace/server and foreign panes are never closed.
  while IFS= read -r record; do
    id=$(jq -r .pane_id <<<"$record")
    live=$(pane_record "$id" "$(jq -r .terminal_id <<<"$record")")
    if [[ $live != missing ]]; then herdr pane close "$id" >/dev/null; fi
  done < <(jq -c '.owned_panes | sort_by(.role == "coordinator")[]' "$SESSION")
  DATA=$(jq '.state="stopped" | .owned_panes |= map(. + {closed:true})' "$SESSION")
  save_state
  event session_stopped
  printf 'Checkpoint acknowledged; only saved owned panes stopped.\n'
}

case "$ACTION" in
  doctor) doctor ;;
  up) up start ;;
  resume) up recovery ;;
  down) down ;;
  status)
    require_session; need_herdr
    jq '{state,prompt_delivery,workspace_id,tab_id,owned_panes}' "$SESSION"
    verify_owned
    while IFS= read -r id; do herdr pane get "$id" || true; done < <(jq -r '.owned_panes[].pane_id' "$SESSION")
    ;;
  logs)
    require_session
    [[ ! -f "$STATE/events.jsonl" ]] || tail -n 100 -- "$STATE/events.jsonl"
    printf 'Session state: %s\n' "$(jq -r .state "$SESSION")"
    # Screen text may contain source; logs intentionally expose only control events.
    ;;
esac
