#!/usr/bin/env python3
"""Translate untranslated proposal files using Together API (OpenAI-compatible).

Scans all non-English proposal files, compares body content to English source,
and translates any that are still in English.

Usage:
    python3 scripts/translate/translate_proposals.py --api-key <TOGETHER_API_KEY>
    python3 scripts/translate/translate_proposals.py --api-key <TOGETHER_API_KEY> --dry-run
    python3 scripts/translate/translate_proposals.py --api-key <TOGETHER_API_KEY> --lang es de fr
"""
from __future__ import annotations

import argparse
import json
import os
import sys
import time
from pathlib import Path
from typing import List, Optional, Dict
from concurrent.futures import ThreadPoolExecutor, as_completed

try:
    from openai import OpenAI
except ImportError:
    print("Error: openai package not installed. Run: pip install openai", file=sys.stderr)
    sys.exit(1)

CONTENT_DIR = Path(__file__).resolve().parent.parent.parent / "content"
TARGET_LANGUAGES = ["zh", "es", "ko", "ru", "cs", "de", "fr", "tr", "vi", "hi", "ar", "pt"]

SYSTEM_PROMPT = """You are a professional technical translator with deep familiarity with internet privacy technologies, I2P (The Invisible Internet Project), and network terminology.

Your task is to translate text segments into the target language while preserving precise meaning, tone, and context.

CRITICAL RULES:
1. Do NOT translate or modify: code blocks, commands, configuration examples, URLs, file paths, variable names, JSON/YAML structures, Markdown syntax
2. Keep I2P technical terms in English: router, tunnel, leaseSet, netDb, floodfill, NTCP2, SSU, SAMv3, I2PTunnel, I2CP, I2NP, eepsite, garlic encryption
3. Preserve ALL Markdown formatting exactly (headings, lists, links, inline code with backticks)
4. Translate idioms and expressions naturally - prefer meaning over literal translation
5. For technical terms without perfect equivalents, keep English term + add localized explanation in parentheses (only once per document)
6. Sound human, fluent, and professional - as if written by a bilingual technical writer
7. NEVER invent content - if unclear, return the original text unchanged
8. Preserve all HTML tags and attributes exactly as they are

Context: These are official I2P technical proposal documents for a developer audience. Maintain consistency with standard I2P terminology."""

LANG_NAMES = {
    "en": "English", "es": "Spanish", "de": "German", "ko": "Korean",
    "fr": "French", "it": "Italian", "pt": "Portuguese", "ru": "Russian",
    "ja": "Japanese", "zh": "Chinese", "cs": "Czech", "tr": "Turkish",
    "vi": "Vietnamese", "hi": "Hindi", "ar": "Arabic"
}


def split_front_matter(text: str):
    """Split markdown into frontmatter lines and body."""
    if not text.startswith("---"):
        return None, text

    lines = text.splitlines()
    end_index = None
    for idx in range(1, len(lines)):
        if lines[idx].strip() == "---":
            end_index = idx
            break

    if end_index is None:
        return None, text

    fm_text = "\n".join(lines[:end_index + 1])
    body = "\n".join(lines[end_index + 1:])
    return fm_text, body


def get_untranslated_proposals() -> Dict[str, List[str]]:
    """Find all non-English proposals with body identical to English source.

    Returns dict mapping proposal filename -> list of languages needing translation.
    """
    en_dir = CONTENT_DIR / "en" / "proposals"
    if not en_dir.exists():
        print(f"Error: English proposals directory not found: {en_dir}", file=sys.stderr)
        sys.exit(1)

    en_proposals = {}
    for f in sorted(en_dir.glob("*.md")):
        content = f.read_text(encoding="utf-8")
        _, body = split_front_matter(content)
        en_proposals[f.name] = body.strip()

    untranslated = {}
    for lang in TARGET_LANGUAGES:
        lang_dir = CONTENT_DIR / lang / "proposals"
        if not lang_dir.exists():
            continue

        for f in sorted(lang_dir.glob("*.md")):
            if f.name not in en_proposals:
                continue

            content = f.read_text(encoding="utf-8")
            _, body = split_front_matter(content)

            if body.strip() == en_proposals[f.name]:
                if f.name not in untranslated:
                    untranslated[f.name] = []
                untranslated[f.name].append(lang)

    return untranslated


def translate_text(client: OpenAI, model: str, text: str, target_lang: str) -> str:
    """Translate text using Together API."""
    target_lang_name = LANG_NAMES.get(target_lang, target_lang)

    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": f"Translate the following I2P technical proposal from English to {target_lang_name}. Preserve all Markdown formatting, code blocks, URLs, and technical terms exactly. Provide ONLY the translation, nothing else:\n\n{text}"}
        ],
        temperature=0.2,
        top_p=0.9,
        max_tokens=16000
    )

    return response.choices[0].message.content.strip()


def translate_proposal(client: OpenAI, model: str, proposal_name: str, lang: str, dry_run: bool = False) -> bool:
    """Translate a single proposal file for a given language."""
    en_path = CONTENT_DIR / "en" / "proposals" / proposal_name
    target_path = CONTENT_DIR / lang / "proposals" / proposal_name

    en_content = en_path.read_text(encoding="utf-8")
    target_content = target_path.read_text(encoding="utf-8")

    # Get the existing translated frontmatter (title may already be translated)
    target_fm, _ = split_front_matter(target_content)
    _, en_body = split_front_matter(en_content)

    en_body = en_body.strip()
    if not en_body:
        print(f"  [SKIP] {proposal_name} ({lang}) - empty body")
        return True

    if dry_run:
        print(f"  [DRY RUN] Would translate {proposal_name} -> {lang}")
        return True

    try:
        translated_body = translate_text(client, model, en_body, lang)

        # Reconstruct: keep existing frontmatter + translated body
        output = f"{target_fm}\n{translated_body}\n"
        target_path.write_text(output, encoding="utf-8")
        return True

    except Exception as exc:
        print(f"  [ERROR] {proposal_name} ({lang}): {exc}", file=sys.stderr)
        return False


def main() -> int:
    parser = argparse.ArgumentParser(description="Translate untranslated I2P proposals using Together API")
    parser.add_argument("--api-key", required=True, help="Together API key")
    parser.add_argument("--model", default="Qwen/Qwen3-235B-A22B-Instruct-2507-tput", help="Model to use")
    parser.add_argument("--lang", nargs="*", help="Specific languages to translate (default: all)")
    parser.add_argument("--dry-run", action="store_true", help="Preview without writing files")
    parser.add_argument("--max-parallel", type=int, default=4, help="Max parallel API calls")
    args = parser.parse_args()

    client = OpenAI(
        api_key=args.api_key,
        base_url="https://api.together.xyz/v1"
    )

    print("Scanning for untranslated proposals...")
    untranslated = get_untranslated_proposals()

    if args.lang:
        for name in list(untranslated.keys()):
            untranslated[name] = [l for l in untranslated[name] if l in args.lang]
            if not untranslated[name]:
                del untranslated[name]

    total_jobs = sum(len(langs) for langs in untranslated.values())
    if total_jobs == 0:
        print("No untranslated proposals found!")
        return 0

    print(f"Found {total_jobs} translations needed across {len(untranslated)} proposals")
    print(f"Model: {args.model}")
    print(f"Parallel: {args.max_parallel}")
    print()

    successful = 0
    failed = 0
    completed = 0

    jobs = []
    for proposal_name, langs in sorted(untranslated.items()):
        for lang in sorted(langs):
            jobs.append((proposal_name, lang))

    with ThreadPoolExecutor(max_workers=args.max_parallel) as executor:
        futures = {}
        for proposal_name, lang in jobs:
            future = executor.submit(
                translate_proposal, client, args.model, proposal_name, lang, args.dry_run
            )
            futures[future] = (proposal_name, lang)

        for future in as_completed(futures):
            proposal_name, lang = futures[future]
            completed += 1
            try:
                if future.result():
                    successful += 1
                    print(f"  [{completed}/{total_jobs}] {proposal_name} -> {lang} OK")
                else:
                    failed += 1
                    print(f"  [{completed}/{total_jobs}] {proposal_name} -> {lang} FAILED")
            except Exception as exc:
                failed += 1
                print(f"  [{completed}/{total_jobs}] {proposal_name} -> {lang} ERROR: {exc}")

    print(f"\nDone: {successful} successful, {failed} failed out of {total_jobs} total")
    return 0 if failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
