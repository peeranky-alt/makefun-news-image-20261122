#!/usr/bin/env python3
"""Copy the news-image entry PNG into the make.fun output directory.

The copy is byte-for-byte: no re-encoding, no network access, no random
values and no timestamps, so every run produces an identical file.
"""

import os
import shutil
from pathlib import Path


def entry_png() -> Path:
    """Path of the entry image sitting next to this script."""
    return Path(__file__).resolve().parent / "entry.png"


def output_dir() -> Path:
    """Output directory, overridable for local runs."""
    return Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")


def main() -> None:
    target_dir = output_dir()
    # Create the output directory up front so the copy never fails on a
    # fresh container; parents=True covers nested MAKEFUN_OUTPUT_DIR paths.
    target_dir.mkdir(parents=True, exist_ok=True)
    # copyfile moves the bytes exactly as-is: no re-encode, no metadata
    # stamp, so the output hash is stable across runs.
    shutil.copyfile(entry_png(), target_dir / "entry.png")


if __name__ == "__main__":
    main()
