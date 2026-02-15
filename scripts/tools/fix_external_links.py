#!/usr/bin/env python3
"""Fix broken external links across all content files.

Two operations:
1. URL replacements — update broken URLs to new working locations
2. Delinks — convert links to dead/internal-only sites to plain text

Applied across all 13 languages in content/*/ directories.
"""
import os
import re
import sys

LANGUAGES = ["en", "ar", "cs", "de", "es", "fr", "hi", "ko", "pt", "ru", "tr", "vi", "zh"]

# ─── URL REPLACEMENTS ────────────────────────────────────────────────
# (old_url_pattern, replacement_url)
# These fix the URL but keep the link clickable.
URL_REPLACEMENTS = [
    # docs.i2p-projekt.de: remove /javadoc/ from path
    (r'http://docs\.i2p-projekt\.de/javadoc/', 'http://docs.i2p-projekt.de/'),
    # json.org → canonical URL
    (r'https?://(?:www\.)?json\.org/?(?=["\)\s>,;]|$)', 'https://www.json.org/json-en.html'),
    # gnunet.org/links/ → /en/
    (r'https://www\.gnunet\.org/links/?', 'https://www.gnunet.org/en/'),
    # altonen.github.io → eepnet.github.io
    (r'https://altonen\.github\.io/emissary/?', 'https://eepnet.github.io/emissary/'),
]

# ─── DELINK PATTERNS ─────────────────────────────────────────────────
# URLs matching these patterns get converted to plain text.
# Order matters — more specific patterns should come first.
DELINK_URL_PATTERNS = [
    # Broken transifex URLs (old project paths)
    r'https?://www\.transifex\.com/(?:projects/p|otf)/I2P\S*',
    # Dead sites
    r'https?://www\.lvh\.io\S*',
    r'https?://reseed\.i2p\.rocks\S*',
    r'https?://reseed-fr\.i2pd\.xyz\S*',
    # All .i2p domains (only reachable inside I2P network)
    # Lookahead ensures .i2p is the TLD, not part of a longer domain like .i2p-projekt.de
    r'https?://\S+\.i2p(?=[/:\s"\)>,;]|$)(?:/\S*)?',
]


def process_body(body):
    """Apply URL replacements and delinks to body text. Returns (new_body, count)."""
    count = 0

    # ── Phase 1: URL replacements ──
    for pattern, replacement in URL_REPLACEMENTS:
        regex = re.compile(pattern)
        matches = regex.findall(body)
        if matches:
            count += len(matches)
            body = regex.sub(replacement, body)

    # ── Phase 2: Delink markdown links [text](url) ──
    def delink_md(m):
        link_text = m.group(1)
        return link_text
    # Match markdown links where URL matches any delink pattern
    md_pattern = re.compile(
        r'\[([^\]]*)\]\((' + '|'.join(f'(?:{p})' for p in DELINK_URL_PATTERNS) + r')\)'
    )
    md_matches = md_pattern.findall(body)
    count += len(md_matches)
    body = md_pattern.sub(delink_md, body)

    # ── Phase 3: Delink HTML <a> links ──
    def delink_html(m):
        inner_text = m.group(2)
        return inner_text
    html_pattern = re.compile(
        r'<a\s+href="(' + '|'.join(f'(?:{p})' for p in DELINK_URL_PATTERNS) + r')"[^>]*>(.*?)</a>',
        re.IGNORECASE,
    )
    html_matches = html_pattern.findall(body)
    count += len(html_matches)
    body = html_pattern.sub(delink_html, body)

    # ── Phase 4: Wrap bare delink URLs in backticks ──
    def wrap_bare(m):
        url = m.group(0)
        return f'`{url}`'
    # Only match if not already in backticks
    bare_pattern = re.compile(
        r'(?<!`)(?:' + '|'.join(f'(?:{p})' for p in DELINK_URL_PATTERNS) + r')(?!`)'
    )
    bare_matches = bare_pattern.findall(body)
    count += len(bare_matches)
    body = bare_pattern.sub(wrap_bare, body)

    return body, count


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
    print(f"\nTotal: {total_files} files {action}, {total_changes} links fixed")


if __name__ == "__main__":
    main()
