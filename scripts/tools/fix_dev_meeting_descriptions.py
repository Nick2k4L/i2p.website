#!/usr/bin/env python3
"""Fix duplicate meta descriptions on dev meeting blog posts.

Replaces generic descriptions like "I2P development meeting covering project
updates and technical discussions" with unique date-specific descriptions like
"I2P development meeting log for November 20, 2002." across all 13 languages.
"""
import glob
import os
import re
import sys

LANGUAGES = ["en", "ar", "cs", "de", "es", "fr", "hi", "ko", "pt", "ru", "tr", "vi", "zh"]
CONTENT_DIR = "content"

# Month names per language
MONTHS = {
    "en": ["January", "February", "March", "April", "May", "June",
           "July", "August", "September", "October", "November", "December"],
    "ar": ["\u064a\u0646\u0627\u064a\u0631", "\u0641\u0628\u0631\u0627\u064a\u0631", "\u0645\u0627\u0631\u0633", "\u0623\u0628\u0631\u064a\u0644", "\u0645\u0627\u064a\u0648", "\u064a\u0648\u0646\u064a\u0648",
           "\u064a\u0648\u0644\u064a\u0648", "\u0623\u063a\u0633\u0637\u0633", "\u0633\u0628\u062a\u0645\u0628\u0631", "\u0623\u0643\u062a\u0648\u0628\u0631", "\u0646\u0648\u0641\u0645\u0628\u0631", "\u062f\u064a\u0633\u0645\u0628\u0631"],
    "cs": ["ledna", "února", "března", "dubna", "května", "června",
           "července", "srpna", "září", "října", "listopadu", "prosince"],
    "de": ["Januar", "Februar", "März", "April", "Mai", "Juni",
           "Juli", "August", "September", "Oktober", "November", "Dezember"],
    "es": ["enero", "febrero", "marzo", "abril", "mayo", "junio",
           "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"],
    "fr": ["janvier", "février", "mars", "avril", "mai", "juin",
           "juillet", "août", "septembre", "octobre", "novembre", "décembre"],
    "hi": ["\u091c\u0928\u0935\u0930\u0940", "\u092b\u0930\u0935\u0930\u0940", "\u092e\u093e\u0930\u094d\u091a", "\u0905\u092a\u094d\u0930\u0948\u0932", "\u092e\u0908", "\u091c\u0942\u0928",
           "\u091c\u0941\u0932\u093e\u0908", "\u0905\u0917\u0938\u094d\u0924", "\u0938\u093f\u0924\u0902\u092c\u0930", "\u0905\u0915\u094d\u091f\u0942\u092c\u0930", "\u0928\u0935\u0902\u092c\u0930", "\u0926\u093f\u0938\u0902\u092c\u0930"],
    "ko": ["1\uc6d4", "2\uc6d4", "3\uc6d4", "4\uc6d4", "5\uc6d4", "6\uc6d4",
           "7\uc6d4", "8\uc6d4", "9\uc6d4", "10\uc6d4", "11\uc6d4", "12\uc6d4"],
    "pt": ["janeiro", "fevereiro", "março", "abril", "maio", "junho",
           "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"],
    "ru": ["\u044f\u043d\u0432\u0430\u0440\u044f", "\u0444\u0435\u0432\u0440\u0430\u043b\u044f", "\u043c\u0430\u0440\u0442\u0430", "\u0430\u043f\u0440\u0435\u043b\u044f", "\u043c\u0430\u044f", "\u0438\u044e\u043d\u044f",
           "\u0438\u044e\u043b\u044f", "\u0430\u0432\u0433\u0443\u0441\u0442\u0430", "\u0441\u0435\u043d\u0442\u044f\u0431\u0440\u044f", "\u043e\u043a\u0442\u044f\u0431\u0440\u044f", "\u043d\u043e\u044f\u0431\u0440\u044f", "\u0434\u0435\u043a\u0430\u0431\u0440\u044f"],
    "tr": ["Ocak", "\u015eubat", "Mart", "Nisan", "May\u0131s", "Haziran",
           "Temmuz", "A\u011fustos", "Eyl\u00fcl", "Ekim", "Kas\u0131m", "Aral\u0131k"],
    "vi": ["1", "2", "3", "4", "5", "6",
           "7", "8", "9", "10", "11", "12"],
    "zh": ["1", "2", "3", "4", "5", "6",
           "7", "8", "9", "10", "11", "12"],
}


def format_date(lang, year, month, day):
    """Format a date according to the language's convention."""
    month_name = MONTHS[lang][month - 1]

    if lang == "en":
        return f"{month_name} {day}, {year}"
    elif lang == "ar":
        return f"{day} {month_name} {year}"
    elif lang == "cs":
        return f"{day}. {month_name} {year}"
    elif lang == "de":
        return f"{day}. {month_name} {year}"
    elif lang == "es":
        return f"{day} de {month_name} de {year}"
    elif lang == "fr":
        return f"{day} {month_name} {year}"
    elif lang == "hi":
        return f"{day} {month_name} {year}"
    elif lang == "ko":
        return f"{year}\ub144 {month_name} {day}\uc77c"
    elif lang == "pt":
        return f"{day} de {month_name} de {year}"
    elif lang == "ru":
        return f"{day} {month_name} {year}"
    elif lang == "tr":
        return f"{day} {month_name} {year}"
    elif lang == "vi":
        return f"{day} th\u00e1ng {month_name} n\u0103m {year}"
    elif lang == "zh":
        return f"{year}\u5e74{month_name}\u6708{day}\u65e5"
    return f"{month_name} {day}, {year}"


def make_description(lang, year, month, day):
    """Build the date-specific description for the given language."""
    date_str = format_date(lang, year, month, day)

    templates = {
        "en": "I2P development meeting log for {date}.",
        "ar": "\u0633\u062c\u0644 \u0627\u062c\u062a\u0645\u0627\u0639 \u062a\u0637\u0648\u064a\u0631 I2P \u0644\u064a\u0648\u0645 {date}.",
        "cs": "Z\u00e1pis z v\u00fdvoj\u00e1\u0159sk\u00e9 sch\u016fzky I2P ze dne {date}.",
        "de": "Protokoll der I2P-Entwicklungsbesprechung vom {date}.",
        "es": "Registro de la reuni\u00f3n de desarrollo de I2P del {date}.",
        "fr": "Journal de la r\u00e9union de d\u00e9veloppement I2P du {date}.",
        "hi": "{date} \u0915\u0940 I2P \u0935\u093f\u0915\u093e\u0938 \u092c\u0948\u0920\u0915 \u0915\u093e \u0932\u0949\u0917\u0964",
        "ko": "{date}\uc790 I2P \uac1c\ubc1c \ud68c\uc758\ub85d.",
        "pt": "Registro da reuni\u00e3o de desenvolvimento do I2P de {date}.",
        "ru": "\u041f\u0440\u043e\u0442\u043e\u043a\u043e\u043b \u0432\u0441\u0442\u0440\u0435\u0447\u0438 \u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u0447\u0438\u043a\u043e\u0432 I2P \u043e\u0442 {date} \u0433\u043e\u0434\u0430.",
        "tr": "{date} tarihli I2P geli\u015ftirme toplant\u0131s\u0131 tutana\u011f\u0131.",
        "vi": "Bi\u00ean b\u1ea3n cu\u1ed9c h\u1ecdp ph\u00e1t tri\u1ec3n c\u1ee7a I2P ng\u00e0y {date}.",
        "zh": "{date}\u7684 I2P \u5f00\u53d1\u4f1a\u8bae\u8bb0\u5f55\u3002",
    }

    return templates[lang].format(date=date_str)


def extract_frontmatter(filepath):
    """Extract description and date from a file's frontmatter."""
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    fm_match = re.match(r"^---\n(.*?)\n---", content, re.DOTALL)
    if not fm_match:
        return None, None, None

    frontmatter = fm_match.group(1)

    desc_match = re.search(r'^description:\s*["\']?(.*?)["\']?\s*$', frontmatter, re.MULTILINE)
    if not desc_match:
        return None, None, None

    date_match = re.search(r'^date:\s*(\d{4})-(\d{2})-(\d{2})', frontmatter, re.MULTILINE)
    if not date_match:
        return None, None, None

    desc = desc_match.group(1).strip()
    date_tuple = (int(date_match.group(1)), int(date_match.group(2)), int(date_match.group(3)))
    return desc, date_tuple, desc_match.group(0)


def find_duplicate_descriptions(files):
    """Find descriptions that appear 2+ times (these are the generics to fix)."""
    desc_counts = {}
    for filepath in files:
        desc, _, _ = extract_frontmatter(filepath)
        if desc:
            desc_counts[desc] = desc_counts.get(desc, 0) + 1
    return {d for d, count in desc_counts.items() if count >= 2}


def process_file(filepath, lang, duplicate_descs, dry_run=False):
    """Process a single dev meeting file. Returns (old_desc, new_desc) or None."""
    desc, date_tuple, old_line = extract_frontmatter(filepath)
    if not desc or not date_tuple or not old_line:
        return None

    if desc not in duplicate_descs:
        return None

    year, month, day = date_tuple
    new_desc = make_description(lang, year, month, day)

    if not dry_run:
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
        new_line = f'description: "{new_desc}"'
        new_content = content.replace(old_line, new_line, 1)
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(new_content)

    return (desc, new_desc)


def main():
    dry_run = "--dry-run" in sys.argv

    # Find the content directory
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.join(script_dir, "..", "..")
    content_dir = os.path.join(project_root, CONTENT_DIR)

    if not os.path.isdir(content_dir):
        print(f"Error: content directory not found at {content_dir}")
        sys.exit(1)

    if dry_run:
        print("=== DRY RUN - no files will be modified ===\n")

    total_changed = 0

    for lang in LANGUAGES:
        lang_dir = os.path.join(content_dir, lang, "blog")
        if not os.path.isdir(lang_dir):
            continue

        files = sorted(glob.glob(os.path.join(lang_dir, "*i2p-dev-meeting*.md")))

        # Find descriptions that appear 2+ times in this language
        duplicate_descs = find_duplicate_descriptions(files)
        lang_changed = 0

        for filepath in files:
            result = process_file(filepath, lang, duplicate_descs, dry_run)
            if result:
                old_desc, new_desc = result
                lang_changed += 1
                if dry_run:
                    basename = os.path.basename(filepath)
                    print(f"  [{lang}] {basename}")
                    print(f"    OLD: {old_desc}")
                    print(f"    NEW: {new_desc}")

        if lang_changed > 0:
            total_changed += lang_changed
            action = "would change" if dry_run else "changed"
            print(f"[{lang}] {action} {lang_changed} files")

    print(f"\nTotal: {total_changed} files {'would be changed' if dry_run else 'changed'}")


if __name__ == "__main__":
    main()
