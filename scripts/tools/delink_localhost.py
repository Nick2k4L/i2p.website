#!/usr/bin/env python3
"""Convert 127.0.0.1 and localhost links to plain text (backticks/code).

Google Search Console reports these as broken external links because
crawlers can't reach the local I2P router console. Converting them to
inline code prevents clickable links from being generated.

Handles:
  - Markdown links: [text](http://127.0.0.1:7657/path) → `http://127.0.0.1:7657/path`
  - HTML links: <a href="http://127.0.0.1:7657/path">text</a> → <code>http://127.0.0.1:7657/path</code>
  - Bare URLs are wrapped in backticks to prevent Goldmark auto-linking.

Applied across all 13 languages in content/*/ directories.
"""
import os
import re
import sys

LANGUAGES = ["en", "ar", "cs", "de", "es", "fr", "hi", "ko", "pt", "ru", "tr", "vi", "zh"]

# Match markdown links with 127.0.0.1 or localhost URLs
MD_LINK_PATTERN = re.compile(
    r'\[([^\]]*)\]\((https?://(?:127\.0\.0\.1|localhost)[^\)]*)\)'
)

# Match HTML <a> links with 127.0.0.1 or localhost URLs
HTML_LINK_PATTERN = re.compile(
    r'<a\s+href="(https?://(?:127\.0\.0\.1|localhost)[^"]*)"[^>]*>(.*?)</a>',
    re.IGNORECASE,
)

# Match bare 127.0.0.1 or localhost URLs not already in backticks or code tags
# (after markdown/HTML links have been replaced)
BARE_URL_PATTERN = re.compile(
    r'(?<!`)(?<!<code>)https?://(?:127\.0\.0\.1|localhost):\d+\S*(?!`|</code>)'
)


def delink_file(filepath, dry_run=False):
    """Convert localhost links to plain text. Returns count of replacements."""
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # Split off frontmatter
    fm_match = re.match(r"^(---\s*\n.*?\n---\n)(.*)", content, re.DOTALL)
    if fm_match:
        frontmatter = fm_match.group(1)
        body = fm_match.group(2)
    else:
        frontmatter = ""
        body = content

    count = 0

    # 1. Replace markdown links: [text](http://127.0.0.1:7657/path) → `http://127.0.0.1:7657/path`
    md_matches = MD_LINK_PATTERN.findall(body)
    count += len(md_matches)
    body = MD_LINK_PATTERN.sub(lambda m: f'`{m.group(2)}`', body)

    # 2. Replace HTML <a> links: <a href="url">text</a> → <code>url</code>
    html_matches = HTML_LINK_PATTERN.findall(body)
    count += len(html_matches)
    body = HTML_LINK_PATTERN.sub(lambda m: f'<code>{m.group(1)}</code>', body)

    # 3. Wrap remaining bare URLs in backticks
    bare_matches = BARE_URL_PATTERN.findall(body)
    count += len(bare_matches)
    body = BARE_URL_PATTERN.sub(lambda m: f'`{m.group(0)}`', body)

    if count == 0:
        return 0

    if not dry_run:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(frontmatter + body)

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
        lang_dir = os.path.join(content_dir, lang)
        if not os.path.isdir(lang_dir):
            continue

        for root, _dirs, files in os.walk(lang_dir):
            for filename in sorted(files):
                if not filename.endswith(".md"):
                    continue

                filepath = os.path.join(root, filename)
                count = delink_file(filepath, dry_run)
                if count > 0:
                    total_files += 1
                    total_replacements += count
                    rel_path = os.path.relpath(filepath, project_root)
                    if dry_run:
                        print(f"  {rel_path} ({count} links)")

    action = "would modify" if dry_run else "modified"
    print(f"\nTotal: {total_files} files {action}, {total_replacements} links delinked")


if __name__ == "__main__":
    main()
