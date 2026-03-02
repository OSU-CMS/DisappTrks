#!/usr/bin/env python3
"""
Validation script for integrated_luminosity.py

This script compares every key in the old lumi dict against the new get_lumi() function
to verify they produce identical values.

Usage:
    python validate_integrated_luminosity.py
"""

import re
import sys

# Import both old and new
from DisappTrks.StandardAnalysis.IntegratedLuminosity_cff import lumi
from DisappTrks.StandardAnalysis.integrated_luminosity import get_lumi, YEAR_ERAS

# Regex to parse keys like "MET_2017" or "MET_2017BC" or "Tau_2016H"
# Format: {dataset}_{year}{eras}
KEY_PATTERN = re.compile(r"^(.+)_(\d{4})([A-Z]*)$")


def parse_key(key):
    """Parse a key like 'MET_2017BC' into (dataset, year, eras).

    Returns (dataset, year, eras) or None if parsing fails.
    eras will be None if it's a full year key like 'MET_2017'.
    """
    match = KEY_PATTERN.match(key)
    if not match:
        return None

    dataset = match.group(1)
    year = match.group(2)
    eras = match.group(3) if match.group(3) else None

    # If eras matches the full year's eras, treat it as None (full year)
    if year in YEAR_ERAS and eras == YEAR_ERAS[year]:
        eras = None

    return dataset, year, eras


def compare_values(old_val, new_val, tolerance=1e-6):
    """Compare two float values with a tolerance."""
    return abs(old_val - new_val) < tolerance


def main():
    mismatches = []
    matches = 0
    skipped = []

    print("Comparing old lumi dict against new get_lumi()...\n")

    for key in sorted(lumi.keys()):
        if isinstance(lumi[key], dict):
            # This is a prescaled trigger dict
            trigger = key
            for subkey in sorted(lumi[trigger].keys()):
                old_value = lumi[trigger][subkey]

                parsed = parse_key(subkey)
                if parsed is None:
                    skipped.append(f"{trigger}[{subkey}]")
                    continue

                dataset, year, eras = parsed

                try:
                    new_value = get_lumi(dataset, year, eras, trigger=trigger)
                except Exception as e:
                    mismatches.append({
                        "key": f"{trigger}[{subkey}]",
                        "old": old_value,
                        "new": f"ERROR: {e}",
                    })
                    continue

                if compare_values(old_value, new_value):
                    matches += 1
                else:
                    mismatches.append({
                        "key": f"{trigger}[{subkey}]",
                        "old": old_value,
                        "new": new_value,
                    })
        else:
            # Regular luminosity entry
            old_value = lumi[key]

            parsed = parse_key(key)
            if parsed is None:
                skipped.append(key)
                continue

            dataset, year, eras = parsed

            try:
                new_value = get_lumi(dataset, year, eras)
            except Exception as e:
                mismatches.append({
                    "key": key,
                    "old": old_value,
                    "new": f"ERROR: {e}",
                })
                continue

            if compare_values(old_value, new_value):
                matches += 1
            else:
                mismatches.append({
                    "key": key,
                    "old": old_value,
                    "new": new_value,
                })

    # Print results
    print(f"Matches: {matches}")
    print(f"Mismatches: {len(mismatches)}")
    print(f"Skipped (couldn't parse): {len(skipped)}")

    if skipped:
        print(f"\nSkipped keys: {skipped}")

    if mismatches:
        print("\n=== MISMATCHES ===")
        for m in mismatches:
            print(f"  {m['key']}:")
            print(f"    old: {m['old']}")
            print(f"    new: {m['new']}")
        sys.exit(1)
    else:
        print("\nAll values match!")
        sys.exit(0)


if __name__ == "__main__":
    main()
