#!/usr/bin/env python3
"""
Resplits WebGL.zip back into 100 parts after modification.
Run this from the root of your cloned silksong repo.

Usage:
    python resplit.py

Output:
    StreamingAssets/aa/WebGL.zip.part1 through .part100
"""

import os
import math

PARTS_DIR = os.path.join("StreamingAssets", "aa")
INPUT_FILE = os.path.join(PARTS_DIR, "WebGL.zip")
TOTAL_PARTS = 100
BASE_NAME = "WebGL.zip.part"

def resplit():
    if not os.path.exists(INPUT_FILE):
        print(f"ERROR: {INPUT_FILE} not found.")
        return

    file_size = os.path.getsize(INPUT_FILE)
    part_size = math.ceil(file_size / TOTAL_PARTS)

    print(f"File size: {file_size / (1024*1024):.1f} MB")
    print(f"Part size: {part_size / (1024*1024):.1f} MB each")
    print(f"Splitting into {TOTAL_PARTS} parts...")

    with open(INPUT_FILE, "rb") as f:
        for i in range(1, TOTAL_PARTS + 1):
            part_path = os.path.join(PARTS_DIR, f"{BASE_NAME}{i}")
            data = f.read(part_size)
            if not data:
                break
            with open(part_path, "wb") as part:
                part.write(data)
            mb = (i * part_size) / (1024 * 1024)
            print(f"  [{i:>3}/{TOTAL_PARTS}] wrote {part_path}", end="\r")

    print(f"\nDone! {TOTAL_PARTS} parts written to {PARTS_DIR}")
    print("\nNext steps:")
    print("  1. git add StreamingAssets/aa/WebGL.zip.part*")
    print("  2. git commit -m 'Remove watermarks from title texture'")
    print("  3. git push")

if __name__ == "__main__":
    resplit()