"""Validate volume manifest metadata and local source without printing source text."""

import argparse
from collections import Counter
import json
import re

import yaml

from extract_epub import ROOT, ensure_local_source


def validate(manifest, records, volume):
    units = manifest["units"]
    unit_ids = [u["id"] for u in units]
    source_ids = [r["id"] for r in records]
    if len(set(unit_ids)) != len(unit_ids) or len(set(source_ids)) != len(source_ids):
        raise ValueError("Duplicate unit IDs")
    expected = manifest["counts"]
    if expected != {"story": expected.get("story"), "note": expected.get("note"),
                    "total": expected.get("total")}:
        raise ValueError("Invalid manifest counts")
    actual = Counter(u["kind"] for u in units)
    record_counts = Counter(r["kind"] for r in records)
    if (actual["story"] != expected["story"] or actual["note"] != expected["note"]
            or expected["total"] != len(units) or record_counts != actual):
        raise ValueError("Wrong manifest totals")
    if manifest.get("volume") != volume:
        raise ValueError("Manifest volume differs from requested volume")
    if volume == "vol-01" and expected != {"story": 3119, "note": 20, "total": 3139}:
        raise ValueError("LN 01 audited totals changed")
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
        volume_number = int(volume.removeprefix("vol-"))
        prefix = f"YS-LN{volume_number:02d}"
        if volume == "vol-01" and unit["kind"] == "note":
            expected_id = f"{prefix}/Note/{unit['attributes']['id']}"
        elif unit["kind"] == "note":
            relative = locator["xhtml"].split("/", 1)[1]
            expected_id = f"{prefix}/Note/{relative}/p{locator['p_ordinal']:06d}"
        else:
            expected_id = f"{prefix}/{locator['xhtml'].split('/', 1)[1]}/p{locator['p_ordinal']:06d}"
        if unit["id"] != expected_id:
            raise ValueError("Unexpected ID format")
        for link in unit["links"]:
            if link.get("target_unit") is not None and link["target_unit"] not in by_id:
                raise ValueError("Unresolved note link")
    if volume == "vol-01":
        calls = [(u, link) for u in units if u["kind"] == "story" for link in u["links"]
                 if link.get("target_unit")]
        backs = [(u, link) for u in units if u["kind"] == "note" for link in u["links"]
                 if link.get("target_unit")]
        if len(calls) != 20 or len(backs) != 20:
            raise ValueError("Expected 20 note calls and backlinks")
        for note, back in backs:
            if not any(u["id"] == back["target_unit"] and link["target_unit"] == note["id"]
                       for u, link in calls):
                raise ValueError("Note call/backlink mismatch")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("volume", help="Volume key such as vol-02")
    args = parser.parse_args()
    try:
        volume = args.volume
        if not re.fullmatch(r"vol-\d{2}", volume):
            raise ValueError("Volume must use the vol-NN format")
        ensure_local_source(ROOT, volume)
        manifest = yaml.safe_load((ROOT / f"segments/{volume}/manifest.yml").read_text(encoding="utf-8"))
        with (ROOT / f"work/{volume}/source.jsonl").open(encoding="utf-8") as stream:
            records = [json.loads(line) for line in stream]
        validate(manifest, records, volume)
    except (ValueError, OSError, KeyError, TypeError, yaml.YAMLError):
        parser.exit(1, "Validation failed: check counts, IDs, locators, links and Git ignore rules.\n")
    print(f"PASS: {manifest['counts']['story']} story + {manifest['counts']['note']} notes; "
          "unique IDs; matching locators/order/SHA")
    print(f"PASS: work/{volume}/source.jsonl is ignored and not tracked by Git")


if __name__ == "__main__":
    main()
