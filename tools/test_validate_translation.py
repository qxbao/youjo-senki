"""Minimal source-free checks for validate_translation."""

from validate_translation import validate


HANDOFF = {"source_sha256": "a" * 64, "glossary_version": "sha256:" + "b" * 64}
SOURCE = [{"id": "segment-001", "text": "Synthetic source text for validator checks.", "xhtml": "<p/>"}]


def row(segment_id="segment-001", source_sha256=HANDOFF["source_sha256"]):
    return {
        "segment_id": segment_id,
        "translation": "Văn bản giả để kiểm tra.",
        "status": "draft",
        "translator": "test-agent",
        "glossary_version": HANDOFF["glossary_version"],
        "source_sha256": source_sha256,
        "notes": [],
    }


def main():
    missing_id = validate(HANDOFF, SOURCE, [row(segment_id="wrong-segment")])
    bad_sha = validate(HANDOFF, SOURCE, [row(source_sha256="c" * 64)])
    assert any("IDs must match" in error for error in missing_id)
    assert any("source_sha256 does not match" in error for error in bad_sha)
    print("PASS: missing/incorrect segment ID and incorrect SHA are rejected")


if __name__ == "__main__":
    main()
