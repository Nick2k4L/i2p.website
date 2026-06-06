#!/usr/bin/env python3
"""Update file hashes in claude_segment_cache.json for already-translated files.

This prevents the CI translation pipeline from re-translating files that were
translated outside the normal CI flow (e.g. bulk translations done manually).

It computes SHA256 hashes of the English source files and stores them in the
segment cache, matching the format used by translate_claude_realtime.py.

Usage:
    python3 scripts/translate/update_hashes.py --dry-run
    python3 scripts/translate/update_hashes.py
"""
import hashlib
import json
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
CONTENT_DIR = SCRIPT_DIR.parent.parent / "content"
SEGMENT_CACHE_FILE = SCRIPT_DIR / "claude_segment_cache.json"
TARGET_LANGUAGES = ["zh", "es", "ko", "ru", "cs", "de", "fr", "tr", "vi", "hi", "ar", "pt"]


def calculate_file_hash(file_path: Path) -> str:
    """Calculate SHA256 hash of file content (matches translate_claude_realtime.py)."""
    content = file_path.read_text(encoding="utf-8")
    return hashlib.sha256(content.encode("utf-8")).hexdigest()


def split_front_matter(text: str):
    """Split markdown into frontmatter and body."""
    if not text.startswith("---"):
        return None, text
    lines = text.splitlines()
    for idx in range(1, len(lines)):
        if lines[idx].strip() == "---":
            return "\n".join(lines[:idx + 1]), "\n".join(lines[idx + 1:])
    return None, text


def find_translated_en_files():
    """Find all English source files that have at least one non-English translation.

    A file is considered translated if the non-English version's body differs
    from the English source (meaning it was actually translated, not just copied).
    """
    en_dir = CONTENT_DIR / "en"
    translated_files = set()

    for en_file in sorted(en_dir.rglob("*")):
        if en_file.suffix not in (".md", ".html") or not en_file.is_file():
            continue

        rel = en_file.relative_to(en_dir)
        rel_str = str(rel).replace("\\", "/")

        en_content = en_file.read_text(encoding="utf-8")
        _, en_body = split_front_matter(en_content)
        en_body_stripped = en_body.strip()

        if not en_body_stripped:
            continue

        # Check if at least one language has a translated version
        for lang in TARGET_LANGUAGES:
            lang_file = CONTENT_DIR / lang / rel
            if not lang_file.exists():
                continue

            lang_content = lang_file.read_text(encoding="utf-8")
            _, lang_body = split_front_matter(lang_content)

            if lang_body.strip() != en_body_stripped:
                # This language has a translated version
                translated_files.add(en_file)
                break

    return sorted(translated_files)


def main():
    dry_run = "--dry-run" in sys.argv

    # Load existing segment cache
    if SEGMENT_CACHE_FILE.exists():
        cache = json.loads(SEGMENT_CACHE_FILE.read_text(encoding="utf-8"))
    else:
        cache = {"version": 2, "files": {}}

    if "files" not in cache:
        cache["files"] = {}

    print("Scanning for translated English source files...")
    translated_files = find_translated_en_files()
    print(f"Found {len(translated_files)} English files with translations")

    # Check which ones are missing from or outdated in the cache
    updated = 0
    added = 0
    unchanged = 0

    for en_file in translated_files:
        rel = en_file.relative_to(CONTENT_DIR)
        cache_key = str(rel).replace("\\", "/")  # e.g. "en/blog/2020-01-01-post.md"
        current_hash = calculate_file_hash(en_file)

        existing = cache["files"].get(cache_key)
        if existing and existing.get("file_hash") == current_hash:
            unchanged += 1
            continue

        if dry_run:
            status = "UPDATE" if existing else "ADD"
            print(f"  [{status}] {cache_key}")
        else:
            if cache_key not in cache["files"]:
                cache["files"][cache_key] = {"segments": {}}
                added += 1
            else:
                updated += 1
            cache["files"][cache_key]["file_hash"] = current_hash

    if dry_run:
        total_changes = len(translated_files) - unchanged
        print(f"\nDry run: would update {total_changes} entries ({unchanged} already up to date)")
    else:
        # Save cache
        SEGMENT_CACHE_FILE.write_text(
            json.dumps(cache, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8"
        )
        print(f"\nDone: {added} added, {updated} updated, {unchanged} unchanged")
        print(f"Saved to {SEGMENT_CACHE_FILE}")


if __name__ == "__main__":
    main()
