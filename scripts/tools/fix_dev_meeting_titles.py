#!/usr/bin/env python3
"""Fix generic 'I2P dev meeting' blog post titles by adding the date.

Finds blog posts with the generic title "I2P dev meeting" (no date) and
updates them to "I2P dev meeting, Month Day, Year" using the frontmatter
date field. Applied across all 13 languages.
"""
import os
import re
import sys
from datetime import datetime

LANGUAGES = ["en", "ar", "cs", "de", "es", "fr", "hi", "ko", "pt", "ru", "tr", "vi", "zh"]


def fix_title_in_file(filepath, dry_run=False):
    """Fix a generic dev meeting title by adding the date. Returns True if modified."""
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    fm_match = re.match(r"^---\n(.*?)\n---", content, re.DOTALL)
    if not fm_match:
        return False

    frontmatter = fm_match.group(1)

    # Check if title is generic "I2P dev meeting" (exact, case-insensitive)
    title_match = re.search(r'^title:\s*["\']?(I2P dev meeting)["\']?\s*$', frontmatter, re.MULTILINE | re.IGNORECASE)
    if not title_match:
        return False

    # Extract the date
    date_match = re.search(r'^date:\s*(\d{4}-\d{2}-\d{2})', frontmatter, re.MULTILINE)
    if not date_match:
        return False

    date_str = date_match.group(1)
    date_obj = datetime.strptime(date_str, "%Y-%m-%d")
    formatted_date = date_obj.strftime("%B %d, %Y")
    # Remove leading zero from day (e.g., "July 01, 2003" -> "July 1, 2003")
    formatted_date = re.sub(r' 0(\d),', r' \1,', formatted_date)

    new_title = f'title: "I2P dev meeting, {formatted_date}"'

    # Add slug to preserve original URL (title change would alter the slug)
    has_slug = re.search(r'^slug:', frontmatter, re.MULTILINE)

    # Replace the title line
    new_frontmatter = re.sub(
        r'^title:\s*["\']?I2P dev meeting["\']?\s*$',
        new_title,
        frontmatter,
        count=1,
        flags=re.MULTILINE | re.IGNORECASE,
    )

    # Add slug field after title if not already present
    if not has_slug:
        new_frontmatter = re.sub(
            r'^(title:.*\n)',
            r'\1slug: "i2p-dev-meeting"\n',
            new_frontmatter,
            count=1,
            flags=re.MULTILINE,
        )

    new_content = content.replace(fm_match.group(1), new_frontmatter, 1)

    if not dry_run:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(new_content)

    return True


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

    total_modified = 0

    for lang in LANGUAGES:
        blog_dir = os.path.join(content_dir, lang, "blog")
        if not os.path.isdir(blog_dir):
            continue

        for filename in sorted(os.listdir(blog_dir)):
            if not filename.endswith(".md"):
                continue

            filepath = os.path.join(blog_dir, filename)
            if fix_title_in_file(filepath, dry_run):
                total_modified += 1
                rel_path = os.path.relpath(filepath, project_root)
                if dry_run:
                    print(f"  {rel_path}")

    action = "would modify" if dry_run else "modified"
    print(f"\nTotal: {total_modified} files {action}")


if __name__ == "__main__":
    main()
