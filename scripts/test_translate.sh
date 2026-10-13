#!/usr/bin/env bash
set -euo pipefail

# Only mocks control Herdr; fixtures contain no book text or real credentials.
ROOT=$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." && pwd -P)
TMP=$(mktemp -d)
cleanup() { rm -r -- "$TMP"; }
trap cleanup EXIT
FIXTURE="$TMP/project"
MOCKBIN="$TMP/bin"
mkdir -p "$FIXTURE" "$MOCKBIN"
cp -R "$ROOT/agents" "$ROOT/config" "$ROOT/scripts" "$ROOT/tools" "$FIXTURE/"
cp "$ROOT/.gitignore" "$FIXTURE/"
if [[ -x "$ROOT/.venv/bin/python" ]]; then ln -s "$ROOT/.venv" "$FIXTURE/.venv"; fi
export TRANSLATE_TEST_CALLS="$TMP/calls"
export TRANSLATE_TEST_ROOT="$FIXTURE"
export HERDR_ENV=1 HERDR_PANE_ID=w-test:p-caller
export PATH="$MOCKBIN:$PATH"
: >"$TRANSLATE_TEST_CALLS"

cat >"$MOCKBIN/herdr" <<'SH'
#!/usr/bin/env bash
set -euo pipefail
printf '%s\n' "$*" >>"$TRANSLATE_TEST_CALLS"
case "$*" in
  status) printf 'endpoint_compatible: yes\nprivate_protocol_compatible: yes\n' ;;
  --help) printf 'herdr agent\n' ;;
  agent) printf 'herdr agent prompt\nherdr agent rename\n' ;;
  pane) printf 'herdr pane split\nherdr pane process-info\n' ;;
  --skill) printf 'mock skill\n' ;;
  'pane get w-test:p-owned')
    jq -n --arg root "$TRANSLATE_TEST_ROOT" '{result:{pane:{pane_id:"w-test:p-owned",workspace_id:"w-test",tab_id:"w-test:t1",terminal_id:"terminal-owned",cwd:$root,foreground_cwd:$root,agent:"codex",agent_status:"idle",agent_session:{value:"session-owned"}}}}' ;;
  'agent get w-test:p-owned')
    [[ ${TRANSLATE_TEST_ALLOW_SHUTDOWN:-} == 1 || ${TRANSLATE_TEST_LIFECYCLE:-} == 1 ]] || exit 97
    printf '{"result":{"agent":{"agent_status":"idle","agent_session":{"value":"session-owned"}}}}\n' ;;
  'agent prompt w-test:p-owned '*)
    [[ ${TRANSLATE_TEST_ALLOW_SHUTDOWN:-} == 1 || ${TRANSLATE_TEST_LIFECYCLE:-} == 1 ]] || exit 97
    if [[ ${TRANSLATE_TEST_LIFECYCLE:-} == 1 && $4 == 'Shutdown request '* ]]; then
      request=${4#Shutdown request }; request=${request%%.*}
      printf 'active_translation_editor: null\nactive_worker: null\nshutdown:\n  request_id: %s\n  acknowledged: true\n' "$request" >"$TRANSLATE_TEST_ROOT/work/run-state/translation-coordinator.yml"
    fi
    printf '{"result":{"type":"agent_prompted"}}\n' ;;
  'pane current --current')
    [[ ${TRANSLATE_TEST_LIFECYCLE:-} == 1 ]] || exit 97
    printf '{"result":{"pane":{"pane_id":"w-test:p-caller","tab_id":"w-test:t1","workspace_id":"w-test"}}}\n' ;;
  'pane layout --current')
    [[ ${TRANSLATE_TEST_LIFECYCLE:-} == 1 ]] || exit 97
    printf '{"result":{"layout":{"area":{"width":120,"height":40}}}}\n' ;;
  'pane split --current '*)
    [[ ${TRANSLATE_TEST_LIFECYCLE:-} == 1 ]] || exit 97
    printf '{"result":{"pane":{"pane_id":"w-test:p-owned","terminal_id":"terminal-owned"}}}\n' ;;
  'pane run w-test:p-owned '*)
    [[ ${TRANSLATE_TEST_LIFECYCLE:-} == 1 && $4 == *'source "/home/$USER/.zshrc" || exit 1;'* && $4 == *codex-personal* && $4 == *'gpt-6-luna'* && $4 == *'model_reasoning_effort=medium'* && $4 == *'--ask-for-approval never'* ]] || exit 97 ;;
  'agent rename w-test:p-owned '*|'pane close w-test:p-owned')
    [[ ${TRANSLATE_TEST_LIFECYCLE:-} == 1 ]] || exit 97 ;;
  *) printf 'Forbidden/unexpected mock Herdr call: %s\n' "$*" >&2; exit 97 ;;
esac
SH
cat >"$MOCKBIN/zsh" <<'SH'
#!/usr/bin/env bash
printf 'zsh %s\n' "$*" >>"$TRANSLATE_TEST_CALLS"
[[ $1 == -ic && ( $2 == *'source "/home/$USER/.zshrc" || exit 1;'* || $2 == *'source "$HOME/.zshrc" || exit 1;'* ) ]] || exit 97
exit 0
SH
cat >"$MOCKBIN/orca" <<'SH'
#!/usr/bin/env bash
printf 'forbidden-backend\n' >>"$TRANSLATE_TEST_CALLS"
exit 98
SH
chmod +x "$MOCKBIN/"*
mkdir -p "$FIXTURE/source-fixture"
: >"$FIXTURE/source-fixture/synthetic.epub"
printf 'source_dir: source-fixture\n' >"$FIXTURE/project.local.yml"
git -C "$FIXTURE" init -q
git -C "$FIXTURE" -c user.name=Test -c user.email=test@example.invalid add .
git -C "$FIXTURE" -c user.name=Test -c user.email=test@example.invalid commit -qm fixture

SCRIPT="$FIXTURE/scripts/translate.sh"
reject() {
  if bash "$SCRIPT" "$@" >"$TMP/out" 2>&1; then
    printf 'FAIL: accepted invalid operation: %s\n' "$*" >&2; exit 1
  fi
}
reject
reject bogus
reject status --dry-run
reject up --unknown
reject down extra extra
[[ ! -s "$TRANSLATE_TEST_CALLS" ]] || { printf 'FAIL: argument validation called Herdr\n'; exit 1; }
reject down
reject down --dry-run
rg -q 'Missing safe session file' "$TMP/out"
[[ ! -s "$TRANSLATE_TEST_CALLS" ]] || { printf 'FAIL: missing session down called Herdr\n'; exit 1; }

# The current Codex reviewer config must pass without a runtime.claude section.
bash "$SCRIPT" doctor >"$TMP/doctor-out" 2>&1
rg -q '^OK:' "$TMP/doctor-out"
rg -q 'source "/home/\$USER/\.zshrc"' "$TRANSLATE_TEST_CALLS"
CONFIG_PYTHON=python3
[[ ! -x "$FIXTURE/.venv/bin/python" ]] || CONFIG_PYTHON="$FIXTURE/.venv/bin/python"
cp "$FIXTURE/config/translation-pipeline.yml" "$TMP/original-config.yml"
update_runtime() {
  "$CONFIG_PYTHON" - "$FIXTURE/config/translation-pipeline.yml" "$1" "$2" "$3" <<'PY'
import pathlib, sys, yaml
p = pathlib.Path(sys.argv[1])
c = yaml.safe_load(p.read_text())
c['runtime'][sys.argv[2]][sys.argv[3]] = sys.argv[4]
p.write_text(yaml.safe_dump(c, sort_keys=False))
PY
}
for role in codex reviewer; do
  update_runtime "$role" model unsupported-model
  reject doctor
  rg -q "runtime.$role.model must be" "$TMP/out"
  cp "$TMP/original-config.yml" "$FIXTURE/config/translation-pipeline.yml"
  update_runtime "$role" approval_policy on-request
  reject doctor
  rg -q "runtime.$role.approval_policy must be never" "$TMP/out"
  cp "$TMP/original-config.yml" "$FIXTURE/config/translation-pipeline.yml"
  update_runtime "$role" source_rc '/tmp/untrusted.rc'
  reject doctor
  rg -q "runtime.$role.source_rc must be" "$TMP/out"
  cp "$TMP/original-config.yml" "$FIXTURE/config/translation-pipeline.yml"
done
# Retain support for the original rc spelling, and actually use it in probes.
update_runtime codex source_rc '~/.zshrc'
update_runtime reviewer source_rc '~/.zshrc'
git -C "$FIXTURE" add config/translation-pipeline.yml
git -C "$FIXTURE" -c user.name=Test -c user.email=test@example.invalid commit -qm legacy-rc
bash "$SCRIPT" doctor >"$TMP/legacy-doctor-out" 2>&1
rg -q '^OK:' "$TMP/legacy-doctor-out"
rg -q 'source "\$HOME/\.zshrc"' "$TRANSLATE_TEST_CALLS"
cp "$TMP/original-config.yml" "$FIXTURE/config/translation-pipeline.yml"
git -C "$FIXTURE" add config/translation-pipeline.yml
git -C "$FIXTURE" -c user.name=Test -c user.email=test@example.invalid commit -qm host-rc

bash "$SCRIPT" up --dry-run >"$TMP/up-out" 2>&1
[[ ! -e "$FIXTURE/work/run-state" ]] || { printf 'FAIL: dry up created run-state\n'; exit 1; }
rg -q 'DRY-RUN' "$TMP/up-out"

mkdir -p "$FIXTURE/work/run-state"
jq -n --arg root "$FIXTURE" '{schema_version:1,managed_by:"youjo-translation-pipeline",project_root:$root,workspace_id:"w-test",tab_id:"w-test:t1",coordinator_name:"test-coordinator",state:"running",prompt_delivery:"submitted",owned_panes:[{role:"coordinator",pane_id:"w-test:p-owned",terminal_id:"terminal-owned",agent_session_id:"session-owned"}]}' >"$FIXTURE/work/run-state/herdr-session.json"
BEFORE=$(sha256sum "$FIXTURE/work/run-state/herdr-session.json")
bash "$SCRIPT" down --dry-run >"$TMP/down-out" 2>&1
[[ $(sha256sum "$FIXTURE/work/run-state/herdr-session.json") == "$BEFORE" ]] || { printf 'FAIL: dry down edited session\n'; exit 1; }
rg -q 'DRY-RUN' "$TMP/down-out"
if rg -q '^(pane (split|close|run|send)|agent (prompt|start|send|rename)|workspace (create|close))|forbidden-backend' "$TRANSLATE_TEST_CALLS"; then
  printf 'FAIL: dry-run mutated Herdr or called forbidden backend\n'; exit 1
fi

# Wrong terminal identity cannot authorize teardown, even in dry-run.
jq '.owned_panes[0].terminal_id="foreign-terminal"' "$FIXTURE/work/run-state/herdr-session.json" >"$TMP/bad-session"
mv "$TMP/bad-session" "$FIXTURE/work/run-state/herdr-session.json"
reject down --dry-run
rg -q 'ownership/cwd mismatch' "$TMP/out"

# A delivered shutdown request without a fresh checkpoint ACK must not close panes.
jq '.owned_panes[0].terminal_id="terminal-owned"' "$FIXTURE/work/run-state/herdr-session.json" >"$TMP/good-session"
mv "$TMP/good-session" "$FIXTURE/work/run-state/herdr-session.json"
export TRANSLATE_TEST_ALLOW_SHUTDOWN=1
reject down
rg -q 'No fresh checkpoint ACK' "$TMP/out"
if rg -q '^pane close|forbidden-backend' "$TRANSLATE_TEST_CALLS"; then
  printf 'FAIL: missing checkpoint ACK closed a pane or used forbidden backend\n'; exit 1
fi

# Exercise the real lifecycle control flow with the fake CLI, never the real server.
mv "$FIXTURE/work/run-state" "$TMP/previous-state"
export TRANSLATE_TEST_LIFECYCLE=1
bash "$SCRIPT" up >"$TMP/lifecycle-up" 2>&1
jq -e '.state=="running" and .prompt_delivery=="submitted" and .owned_panes[0].agent_session_id=="session-owned"' "$FIXTURE/work/run-state/herdr-session.json" >/dev/null
# up is idempotent: retaining the coordinator must not mutate session or dispatch.
CALLS_BEFORE=$(rg -c '^agent prompt' "$TRANSLATE_TEST_CALLS")
bash "$SCRIPT" up >"$TMP/lifecycle-retain" 2>&1
[[ $(rg -c '^agent prompt' "$TRANSLATE_TEST_CALLS") == "$CALLS_BEFORE" ]]
bash "$SCRIPT" down >"$TMP/lifecycle-down" 2>&1
jq -e '.state=="stopped" and .owned_panes[0].closed==true' "$FIXTURE/work/run-state/herdr-session.json" >/dev/null
rg -q '^pane close w-test:p-owned$' "$TRANSLATE_TEST_CALLS"
if rg -q '^pane close w-test:p-caller|forbidden-backend' "$TRANSLATE_TEST_CALLS"; then
  printf 'FAIL: foreign pane or forbidden backend used\n'; exit 1
fi
printf 'PASS: current/legacy Codex rc, role model/permissions/rc validation, invalid args, missing-session down, dry-run immutability, ownership mismatch, shutdown without ACK, mocked up/down lifecycle, no forbidden backend.\n'
