#!/usr/bin/env python3
"""Fix links with no anchor text across all content files.

Wraps bare external URLs in backticks to prevent Goldmark auto-linking,
which creates links with URL-as-anchor-text (flagged by Google Search
Console as "links with no anchor text").

Only processes URLs in markdown context (outside HTML blocks like
<div class="irc-log">). Uses a simple heuristic: skip lines that
start with HTML tags or appear to be inside an HTML block.

Applied across all 13 languages in content/*/ directories.
"""
import os
import re
import sys

LANGUAGES = ["en", "ar", "cs", "de", "es", "fr", "hi", "ko", "pt", "ru", "tr", "vi", "zh"]

# ─── BARE URL PATTERNS TO WRAP IN BACKTICKS ─────────────────────────
# These bare URLs get auto-linked by Goldmark, creating links with
# URL-as-anchor-text. Wrapping in backticks prevents auto-linking.
BARE_URL_PATTERNS = [
    # archive.org — appears in ~39 blog posts per language
    r'https?://(?:www\.)?archive\.org/?(?=["\)\s>,;]|$)',
    # Legacy i2p.net subdomains (dead sites)
    r'https?://dev\.i2p\.net\S*',
    r'https?://forum\.i2p\.net\S*',
    r'https?://syndiemedia\.i2p\.net\S*',
    # Old domains
    r'https?://(?:www\.)?geti2p\.net\S*',
    r'https?://(?:www\.)?i2p2\.de\S*',
]


def process_body(body):
    """Wrap bare URLs in backticks, skipping HTML blocks. Returns (new_body, count)."""
    count = 0
    lines = body.split('\n')
    result_lines = []
    in_html_block = False

    for line in lines:
        stripped = line.strip()

        # Track HTML block boundaries (simple heuristic)
        # Goldmark treats lines starting with block-level HTML tags as HTML blocks
        if re.match(r'<(?:div|table|pre|p\b|ul|ol|dl|details|section|article|aside|nav|header|footer|figure)\b', stripped, re.IGNORECASE):
            in_html_block = True
        if re.match(r'</(?:div|table|pre|p|ul|ol|dl|details|section|article|aside|nav|header|footer|figure)>', stripped, re.IGNORECASE):
            in_html_block = False
            result_lines.append(line)
            continue

        if in_html_block:
            result_lines.append(line)
            continue

        # Skip lines that start with HTML tags (inline HTML in markdown)
        if stripped.startswith('<') and not stripped.startswith('<!'):
            result_lines.append(line)
            continue

        # Process this line — wrap bare URLs in backticks
        new_line = line
        for pattern in BARE_URL_PATTERNS:
            # Match bare URL not already in:
            #   - backticks: `url`
            #   - markdown link URL: [text](url)
            bare_re = re.compile(
                r'(?<!`)(?<!\]\()(' + pattern + r')(?!`)'
            )
            matches = bare_re.findall(new_line)
            if matches:
                count += len(matches)
                new_line = bare_re.sub(lambda m: f'`{m.group(0)}`', new_line)

        result_lines.append(new_line)

    return '\n'.join(result_lines), count


def process_file(filepath, dry_run=False):
    """Process a single file. Returns count of changes."""
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # Split off frontmatter
    fm_match = re.match(r"^(---\s*\n.*?\n---\s*\n)(.*)", content, re.DOTALL)
    if fm_match:
        frontmatter = fm_match.group(1)
        body = fm_match.group(2)
    else:
        frontmatter = ""
        body = content

    new_body, count = process_body(body)

    if count == 0:
        return 0

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
    total_changes = 0

    for lang in LANGUAGES:
        lang_dir = os.path.join(content_dir, lang)
        if not os.path.isdir(lang_dir):
            continue

        for root, _dirs, files in os.walk(lang_dir):
            for filename in sorted(files):
                if not (filename.endswith(".md") or filename.endswith(".html")):
                    continue

                filepath = os.path.join(root, filename)
                count = process_file(filepath, dry_run)
                if count > 0:
                    total_files += 1
                    total_changes += count
                    rel_path = os.path.relpath(filepath, project_root)
                    if dry_run:
                        print(f"  {rel_path} ({count} changes)")

    action = "would modify" if dry_run else "modified"
    print(f"\nTotal: {total_files} files {action}, {total_changes} URLs wrapped")


if __name__ == "__main__":
    main()
