#!/usr/bin/env python3
"""Wrap www.i2p.net URLs in backticks to prevent Goldmark auto-linking.

Goldmark's linkify extension auto-links bare URLs starting with http://,
https://, or www. Wrapping in backticks renders them as inline code,
preventing clickable links from being generated.

Applied across all 13 languages in content/*/blog/ directories.
"""
import os
import re
import sys

LANGUAGES = ["en", "ar", "cs", "de", "es", "fr", "hi", "ko", "pt", "ru", "tr", "vi", "zh"]

# Match www.i2p.net URLs with or without scheme, not already in backticks
URL_PATTERN = re.compile(r'(?<!`)(?:https?://)?www\.i2p\.net\S*')


def delink_file(filepath, dry_run=False):
    """Wrap www.i2p.net URLs in backticks. Returns count of replacements."""
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # Split off frontmatter to avoid modifying it
    fm_match = re.match(r"^(---\s*\n.*?\n---\n)(.*)", content, re.DOTALL)
    if fm_match:
        frontmatter = fm_match.group(1)
        body = fm_match.group(2)
    else:
        frontmatter = ""
        body = content

    matches = URL_PATTERN.findall(body)
    count = len(matches)
    if count == 0:
        return 0

    new_body = URL_PATTERN.sub(lambda m: f"`{m.group(0)}`", body)

    if not dry_run:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(frontmatter + new_body)

    return count


def main():
    dry_run = "--dry-run" in sys.argv

    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.join(script_dir, "..", "..")
    content_dir = os.path.join(project_root, "content")

    if not os.path.isdir(content_dir):
        print(f"Error: content directory not found at {content_dir}")
        sys.exit(1)

    if dry_run:
        print("=== DRY RUN - no files will be modified ===\n")

    total_files = 0
    total_replacements = 0

    for lang in LANGUAGES:
        blog_dir = os.path.join(content_dir, lang, "blog")
        if not os.path.isdir(blog_dir):
            continue

        for filename in sorted(os.listdir(blog_dir)):
            if not filename.endswith(".md"):
                continue

            filepath = os.path.join(blog_dir, filename)
            count = delink_file(filepath, dry_run)
            if count > 0:
                total_files += 1
                total_replacements += count
                rel_path = os.path.relpath(filepath, project_root)
                if dry_run:
                    print(f"  {rel_path} ({count} URLs)")

    action = "would modify" if dry_run else "modified"
    print(f"\nTotal: {total_files} files {action}, {total_replacements} URLs delinked")


if __name__ == "__main__":
    main()
