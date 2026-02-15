#!/usr/bin/env python3
"""Add Hugo aliases to content files to fix broken internal links.

Adds redirect aliases to target content files so old/moved paths
redirect to the correct pages. Applied across all 13 languages.

Hugo alias behavior with defaultContentLanguageInSubdir = true:
- Absolute aliases (leading /) are used as-is for the redirect path
- So we must include the language prefix: /en/docs/protocol/i2cp
- Each language's content file gets its own language-prefixed aliases
"""
import os
import re
import sys

LANGUAGES = ["en", "ar", "cs", "de", "es", "fr", "hi", "ko", "pt", "ru", "tr", "vi", "zh"]

# Alias paths WITHOUT language prefix — the script prepends /{lang}/ for each language.
# Both trailing-slash and non-trailing-slash variants are generated.
ALIAS_PATHS = [
    # --- Original aliases (from broken internal links) ---
    ("docs/specs/i2cp.md", ["docs/protocol/i2cp", "docs/api/i2cp"]),
    ("docs/specs/i2np.md", ["docs/protocol/i2np"]),
    ("docs/legacy/ntcp.md", ["docs/transport/ntcp", "docs/ntcp"]),
    ("docs/legacy/ssu.md", [
        "docs/transport/ssu",
        "docs/transports/ssu",
    ]),
    ("docs/legacy/bob.md", ["docs/api/bob"]),
    ("docs/legacy/sam.md", ["docs/api/sam"]),
    ("docs/legacy/samv2.md", ["docs/api/samv2"]),
    ("docs/applications/git-bundle.md", ["docs/applications/git"]),
    ("docs/overview/performance.md", [
        "about/performance/future",
        "about/performance/history",
    ]),
    # --- docs/develop/* → docs/development/* (renamed section) ---
    ("docs/development/applications.md", ["docs/develop/applications"]),
    ("docs/development/dev-guidelines.md", ["docs/develop/dev-guidelines"]),
    ("docs/development/licenses.md", ["docs/develop/licenses"]),
    ("docs/development/new-translators.md", ["docs/develop/new-translators"]),
    ("docs/development/release-signing-key.md", ["docs/develop/release-signing-key"]),
    ("docs/development/new-developers.md", ["docs/develop/new-developers"]),
    ("docs/development/overview.md", ["docs/develop/overview"]),
    # --- docs/legacy/* → current locations ---
    ("docs/specs/tunnel-message.md", ["docs/legacy/tunnel-message"]),
    ("docs/historical/naming.md", ["docs/legacy/naming"]),
    ("docs/historical/netdb.md", ["docs/legacy/netdb"]),
    # --- docs/specs/* and docs/overview/* old paths ---
    ("docs/specs/tunnel-implementation.md", ["docs/specs/implementation"]),
    ("docs/overview/naming.md", ["docs/specs/naming", "docs/naming"]),
    # --- docs/specs/* old slug names ---
    ("docs/specs/red25519.md", ["docs/specs/red25519-signature-scheme"]),
    ("docs/specs/b32encrypted.md", ["docs/specs/b32-for-encrypted-leasesets"]),
    ("docs/specs/udp-announces.md", ["docs/specs/udp-bittorrent-announces"]),
    # --- docs/historical/* old paths ---
    ("docs/legacy/old-tunnel-implementation.md", ["docs/historical/tunnel-alt"]),
    ("docs/historical/ntcp-discussion.md", ["docs/discussions/ntcp"]),
    ("docs/historical/tunnel.md", ["docs/discussions/tunnel"]),
    # --- docs/guides renamed pages ---
    ("docs/guides/macos-install.md", ["docs/guides/installing-i2p-on-macos-the-long-way"]),
    # --- get-involved ---
    ("get-involved/roadmap.md", ["get-involved/todo"]),
    # --- Proposals with old/shortened slugs ---
    ("proposals/111-ntcp-2.md", ["proposals/111-ntcp2"]),
    ("proposals/119-bidirectional-tunnels.md", ["proposals/119"]),
    ("proposals/142-new-crypto-template.md", ["proposals/142-ecies-template"]),
    ("proposals/143-build-message-options.md", ["proposals/143"]),
    ("proposals/144-ecies-x25519-aead-ratchet.md", ["proposals/144-ecies-x25519"]),
    ("proposals/145-ecies.md", ["proposals/145-ecies-ecdh-aes"]),
    ("proposals/152-ecies-tunnels.md", ["proposals/152-ecies-config", "proposals/152"]),
    ("proposals/153-chacha20-layer-encryption.md", ["proposals/153-chacha20-layer", "proposals/153"]),
    ("proposals/154-ecies-lookups.md", ["proposals/154-ratchet"]),
    ("proposals/156-ecies-routers.md", ["proposals/156"]),
    ("proposals/157-new-tbm.md", ["proposals/157"]),
    ("proposals/163-datagram2.md", ["proposals/163-datagram2-datagram3"]),
    ("proposals/168-tunnel-bandwidth.md", ["proposals/168"]),
    # --- spec/proposals/* → proposals/* (wrong parent path) ---
    ("proposals/126-ipv6-peer-testing.md", ["spec/proposals/126-ipv6-peer-testing"]),
    ("proposals/158-ipv6-transport-enhancements.md", ["spec/proposals/158"]),
]

# Bare-path aliases for URLs without a language prefix (e.g., www.i2p.net/docs/...).
# These are added to the ENGLISH file only (no /{lang}/ prefix) so Hugo creates
# a redirect from the bare path to the English version.
BARE_ALIASES = [
    ("docs/specs/common-structures.md", ["docs/specs/common-structures"]),
    ("docs/api/samv3.md", ["docs/api/samv3"]),
    ("docs/api/streaming.md", ["docs/api/streaming"]),
    ("docs/specs/ecies.md", ["docs/specs/ecies"]),
    ("docs/specs/ecies-hybrid.md", ["docs/specs/ecies-hybrid"]),
    ("docs/specs/ecies-routers.md", ["docs/specs/ecies-routers"]),
    ("proposals/134-gost.md", ["proposals/134-gost"]),
    ("proposals/169-pq-crypto.md", ["proposals/169-pq-crypto"]),
]


def add_aliases_to_file(filepath, new_aliases, dry_run=False):
    """Add aliases to a file's frontmatter. Returns list of actually added aliases."""
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    fm_match = re.match(r"^---\s*\n(.*?)\n---", content, re.DOTALL)
    if not fm_match:
        return []

    frontmatter = fm_match.group(1)

    # Parse existing aliases
    existing_aliases = []
    alias_match = re.search(r"^aliases:\s*\n((?:\s+-\s+.*\n)*)", frontmatter, re.MULTILINE)
    if alias_match:
        for line in alias_match.group(1).strip().split("\n"):
            line = line.strip()
            if line.startswith("- "):
                val = line[2:].strip().strip("'\"")
                existing_aliases.append(val)

    # Also handle single-line aliases format: aliases: ["/path/"]
    if not alias_match:
        alias_match_inline = re.search(r'^aliases:\s*\[([^\]]*)\]', frontmatter, re.MULTILINE)
        if alias_match_inline:
            for item in alias_match_inline.group(1).split(","):
                val = item.strip().strip("'\"")
                if val:
                    existing_aliases.append(val)

    # Remove any old incorrect aliases (relative ones without leading /)
    # that were added by a previous run of this script
    old_relative_paths = set()
    for _, paths in ALIAS_PATHS:
        for p in paths:
            old_relative_paths.add(p)
            old_relative_paths.add(p + "/")
    cleaned_aliases = [a for a in existing_aliases if a not in old_relative_paths]

    # Determine which new aliases are truly new
    to_add = [a for a in new_aliases if a not in cleaned_aliases]
    changed = len(cleaned_aliases) != len(existing_aliases)

    if not to_add and not changed:
        return []

    all_aliases = cleaned_aliases + to_add

    # Build new aliases block
    aliases_yaml = "aliases:\n"
    for alias in all_aliases:
        aliases_yaml += f'  - "{alias}"\n'

    # Replace or insert aliases in frontmatter
    if re.search(r"^aliases:", frontmatter, re.MULTILINE):
        # Replace existing aliases block
        new_frontmatter = re.sub(
            r"^aliases:\s*(?:\n(?:\s+-\s+.*\n)*|\s*\[.*?\]\s*\n)",
            aliases_yaml,
            frontmatter,
            count=1,
            flags=re.MULTILINE,
        )
    else:
        # Insert after slug line if it exists, otherwise after title
        if re.search(r"^slug:", frontmatter, re.MULTILINE):
            new_frontmatter = re.sub(
                r"^(slug:.*\n)",
                r"\1" + aliases_yaml,
                frontmatter,
                count=1,
                flags=re.MULTILINE,
            )
        else:
            new_frontmatter = re.sub(
                r"^(title:.*\n)",
                r"\1" + aliases_yaml,
                frontmatter,
                count=1,
                flags=re.MULTILINE,
            )

    new_content = content.replace(fm_match.group(1), new_frontmatter, 1)

    if not dry_run:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(new_content)

    return to_add if to_add else (["(fixed)"] if changed else [])


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

    for target_file, alias_paths in ALIAS_PATHS:
        for lang in LANGUAGES:
            filepath = os.path.join(content_dir, lang, target_file)
            if not os.path.isfile(filepath):
                continue

            # Build language-prefixed absolute aliases
            aliases = []
            for path in alias_paths:
                aliases.append(f"/{lang}/{path}")
                aliases.append(f"/{lang}/{path}/")

            added = add_aliases_to_file(filepath, aliases, dry_run)
            if added:
                total_modified += 1
                rel_path = os.path.relpath(filepath, project_root)
                if dry_run:
                    print(f"  {rel_path}")
                    for a in added:
                        print(f"    + {a}")

    # Process bare-path aliases (English only, no language prefix)
    for target_file, alias_paths in BARE_ALIASES:
        filepath = os.path.join(content_dir, "en", target_file)
        if not os.path.isfile(filepath):
            continue

        aliases = []
        for path in alias_paths:
            aliases.append(f"/{path}")
            aliases.append(f"/{path}/")

        added = add_aliases_to_file(filepath, aliases, dry_run)
        if added:
            total_modified += 1
            rel_path = os.path.relpath(filepath, project_root)
            if dry_run:
                print(f"  {rel_path}")
                for a in added:
                    print(f"    + {a}")

    action = "would modify" if dry_run else "modified"
    print(f"\nTotal: {total_modified} files {action}")


if __name__ == "__main__":
    main()
