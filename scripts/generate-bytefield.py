#!/usr/bin/env python3
"""Extract bytefield code blocks from markdown files and generate SVGs.

Scans all .md files under content/ for ```bytefield fenced code blocks,
generates SVGs using bytefield-svg, and saves them to assets/images/bytefield/
with MD5-hashed filenames (matching Hugo's render hook lookup).

Usage:
    python scripts/generate-bytefield.py [--clean] [--force]

Options:
    --clean   Remove orphaned SVGs that no longer match any source block
    --force   Regenerate all SVGs even if they already exist
"""

import hashlib
import os
import platform
import re
import shutil
import subprocess
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(SCRIPT_DIR)
CONTENT_DIR = os.path.join(PROJECT_ROOT, "content")
OUTPUT_DIR = os.path.join(PROJECT_ROOT, "assets", "images", "bytefield")

# Regex to find ```bytefield code blocks in markdown
BYTEFIELD_PATTERN = re.compile(
    r"```bytefield\b[^\n]*\n(.*?)```", re.DOTALL
)


def find_bytefield_blocks(content_dir):
    """Walk content directory and extract all bytefield code blocks.

    Returns a list of (filepath, block_content) tuples.
    """
    blocks = []
    for root, _dirs, files in os.walk(content_dir):
        for filename in files:
            if not filename.endswith(".md"):
                continue
            filepath = os.path.join(root, filename)
            with open(filepath, "r", encoding="utf-8") as f:
                content = f.read()
            for match in BYTEFIELD_PATTERN.finditer(content):
                blocks.append((filepath, match.group(1)))
    return blocks


def compute_hash(content):
    """Compute MD5 hash of trimmed content, matching Hugo's md5 function."""
    trimmed = content.strip()
    return hashlib.md5(trimmed.encode("utf-8")).hexdigest()


def find_bytefield_cmd():
    """Locate the bytefield-svg command, handling Windows npm globals."""
    cmd = shutil.which("bytefield-svg")
    if cmd:
        return [cmd]
    # On Windows, npm global .cmd scripts may need shell or npx fallback
    if platform.system() == "Windows":
        cmd = shutil.which("bytefield-svg.cmd")
        if cmd:
            return [cmd]
    return None


# Resolve the command once at module level
_BYTEFIELD_CMD = find_bytefield_cmd()


def generate_svg(source_code, output_path):
    """Run bytefield-svg to generate an embedded SVG."""
    if not _BYTEFIELD_CMD:
        print(
            "Error: bytefield-svg not found. Install it with: npm install -g bytefield-svg",
            file=sys.stderr,
        )
        sys.exit(1)
    try:
        result = subprocess.run(
            _BYTEFIELD_CMD + ["-e"],
            input=source_code,
            capture_output=True,
            text=True,
            timeout=30,
        )
    except subprocess.TimeoutExpired:
        print(f"Error: bytefield-svg timed out for {output_path}", file=sys.stderr)
        return False

    if result.returncode != 0:
        print(f"Error generating SVG: {result.stderr}", file=sys.stderr)
        return False

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(result.stdout)
    return True


def clean_orphans(active_hashes):
    """Remove SVGs that no longer correspond to any bytefield block."""
    if not os.path.exists(OUTPUT_DIR):
        return 0
    removed = 0
    for filename in os.listdir(OUTPUT_DIR):
        if not filename.endswith(".svg"):
            continue
        file_hash = filename[:-4]  # strip .svg
        if file_hash not in active_hashes:
            os.remove(os.path.join(OUTPUT_DIR, filename))
            print(f"  Removed orphan: {filename}")
            removed += 1
    return removed


def main():
    force = "--force" in sys.argv
    clean = "--clean" in sys.argv

    print(f"Scanning {CONTENT_DIR} for bytefield blocks...")
    blocks = find_bytefield_blocks(CONTENT_DIR)
    print(f"Found {len(blocks)} bytefield block(s)")

    if not blocks:
        if clean:
            removed = clean_orphans(set())
            print(f"Cleaned {removed} orphaned SVG(s)")
        return

    generated = 0
    skipped = 0
    errors = 0
    active_hashes = set()

    for filepath, block_content in blocks:
        block_hash = compute_hash(block_content)
        active_hashes.add(block_hash)
        svg_path = os.path.join(OUTPUT_DIR, f"{block_hash}.svg")
        rel_filepath = os.path.relpath(filepath, PROJECT_ROOT)

        if os.path.exists(svg_path) and not force:
            skipped += 1
            continue

        trimmed = block_content.strip()
        if generate_svg(trimmed, svg_path):
            generated += 1
            print(f"  Generated: {block_hash}.svg  (from {rel_filepath})")
        else:
            errors += 1
            print(f"  ERROR processing block in {rel_filepath}")

    if clean:
        removed = clean_orphans(active_hashes)
    else:
        removed = 0

    print(f"\nDone: {generated} generated, {skipped} unchanged, {errors} errors", end="")
    if clean:
        print(f", {removed} orphans removed", end="")
    print()

    if errors > 0:
        sys.exit(1)


if __name__ == "__main__":
    main()
