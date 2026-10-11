"""Validate LN 01 metadata and local source without printing source text."""

import argparse
from collections import Counter
import json

import yaml

from extract_epub import ROOT, ensure_local_source


def validate(manifest, records):
    units = manifest["units"]
    unit_ids = [u["id"] for u in units]
    source_ids = [r["id"] for r in records]
    if len(set(unit_ids)) != len(unit_ids) or len(set(source_ids)) != len(source_ids):
        raise ValueError("Duplicate unit IDs")
    expected = Counter(story=3119, note=20)
    if Counter(u["kind"] for u in units) != expected or Counter(r["kind"] for r in records) != expected:
        raise ValueError("Wrong story/note counts")
    if manifest["counts"] != {"story": 3119, "note": 20, "total": 3139}:
        raise ValueError("Wrong manifest totals")
    if unit_ids != source_ids:
        raise ValueError("Manifest and source IDs/order differ")
    if len({(u['locator']['xhtml'], u['locator']['dom_path']) for u in units}) != len(units):
        raise ValueError("Duplicate locators")
    by_id = {u["id"]: u for u in units}
    for unit, record in zip(units, records):
        if record["locator"] != unit["locator"]:
            raise ValueError("Locator mismatch")
        if record["source_sha256"] != manifest["source"]["sha256"]:
            raise ValueError("Source fingerprint mismatch")
        if not record["text"].strip() or not record["xhtml"]:
            raise ValueError("Empty local source")
        locator = unit["locator"]
        expected_id = (f"YS-LN01/Note/{unit['attributes']['id']}" if unit["kind"] == "note"
                       else f"YS-LN01/{locator['xhtml'].split('/', 1)[1]}/p{locator['p_ordinal']:06d}")
        if unit["id"] != expected_id:
            raise ValueError("Unexpected ID format")
        for link in unit["links"]:
            if link["target_unit"] not in by_id:
                raise ValueError("Unresolved note link")
    calls = [(u, link) for u in units if u["kind"] == "story" for link in u["links"]]
    backs = [(u, link) for u in units if u["kind"] == "note" for link in u["links"]]
    if len(calls) != 20 or len(backs) != 20:
        raise ValueError("Expected 20 note calls and backlinks")
    for note, back in backs:
        if not any(u["id"] == back["target_unit"] and link["target_unit"] == note["id"]
                   for u, link in calls):
            raise ValueError("Note call/backlink mismatch")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("volume", choices=["vol-01"])
    parser.parse_args()
    try:
        ensure_local_source(ROOT)
        manifest = yaml.safe_load((ROOT / "segments/vol-01/manifest.yml").read_text(encoding="utf-8"))
        with (ROOT / "work/vol-01/source.jsonl").open(encoding="utf-8") as stream:
            records = [json.loads(line) for line in stream]
        validate(manifest, records)
    except (ValueError, OSError, KeyError, TypeError, yaml.YAMLError):
        parser.exit(1, "Validation failed: check counts, IDs, locators, links and Git ignore rules.\n")
    print("PASS: 3119 story + 20 notes; unique IDs; matching locators/order/SHA; 20 note links/backlinks")
    print("PASS: work/vol-01/source.jsonl is ignored and not tracked by Git")


if __name__ == "__main__":
    main()
