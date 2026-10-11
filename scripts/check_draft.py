#!/usr/bin/env python3
"""Pre-publish gate for blog drafts. Exits 1 if anything must be fixed.

Usage: python3 scripts/check_draft.py content/posts/<file>.md [more files]

Each rule is a lesson learnt since the blog pipeline was built (Jacob, 2026-10-11):

  1. Dashes: no em dashes or en dashes at all. They read as an AI tell, and the house
     style everywhere else (kern, the hub) is zero.
  2. Banned words: "honest"/"honestly" and high-frequency AI vocabulary block the post.
     Filler the style guide says to cut (actually, kind of...) only WARNS.
  3. Confidential detail: the blog shares the LESSON, never the workplace facts. No
     employer or client names, no ticket or change IDs, no internal hostnames, no
     live counts from work tools (e.g. "251 open findings"). Say "a long list of
     open findings that I manage every week", or tell an allegory that makes the point.
  4. Kern is private: never mention or link it.

Fix each finding by rewriting the sentence, not by deleting the point.
"""
import re
import sys

BANNED_WORDS = [
    # Jacob's own bans
    "honest", "honestly", "honesty",
    # high-frequency AI vocabulary (humanizer skill)
    "delve", "tapestry", "testament", "pivotal", "underscore", "underscores",
    "intricate", "intricacies", "interplay", "garner", "showcase", "showcasing",
    "vibrant", "evolving landscape", "game-changer", "game changer", "in today's",
    "let's dive", "dive into", "it's worth noting", "at the end of the day",
]

# Filler and hedging (ai/style.md "Tone Rules"). WARN only: they have normal uses too
# ("this kind of thinking"), so a person judges each one.
WARN_WORDS = ["basically", "essentially", "actually", "so to speak", "kind of", "sort of",
              "extremely", "incredibly", "really", "very"]

# Workplace names: employers, clients, auditors, colleagues' companies, internal systems.
CONFIDENTIAL_NAMES = [
    "M&S", "Marks & Spencer", "Marks and Spencer", "Namiri", "Digitax", "DigiTax",
    "PwC", "Mindera", "JayCee", "Jaycee", "Hermes", "Caine",
    "ProcessUnity", "Dynatrace", "Helix", "BEAM", "Paragon", "Bullseye",
]

CONFIDENTIAL_PATTERNS = [
    (r"\b[A-Z][A-Z0-9]{1,9}-\d{2,}\b", "ticket or issue ID"),
    (r"\bCRQ\d+|\bCHG\d+|\bINC\d+|\bRITM\d+", "change or incident number"),
    (r"\b[\w-]+\.(?:digitax\.tech|namiri\.tech|marks-and-spencer\.com|mnscorp\.net)\b", "internal hostname"),
    (r"\b\d[\d,]*\s+(?:open|fixed|closed|outstanding|unresolved)\b", "live count from a work tool"),
    (r"\b\d[\d,]*\s+(?:findings|issues|vulnerabilities|vulns|tickets|incidents|alerts|defects|bugs|CVEs)\b",
     "live count from a work tool"),
    (r"\b(?:Snyk|SonarQube|Sonar|Jira|ServiceNow)\b[^.\n]{0,60}\b\d{2,}\b", "tool named next to a number"),
    (r"\bwaiting\b[^.\n]{0,40}\b\d+\s+days\b|\b\d+\s+days\b[^.\n]{0,40}\bwaiting\b", "a specific wait from work"),
]


def body_of(text: str) -> str:
    """Drop the +++ frontmatter so titles in it are checked but dates are not."""
    m = re.match(r"\+\+\+\n(.*?)\n\+\+\+\n", text, re.S)
    if not m:
        return text
    title = re.search(r"^title\s*=\s*['\"](.*)['\"]", m.group(1), re.M)
    return (title.group(1) + "\n" if title else "") + text[m.end():]


def check(path: str) -> list[str]:
    text = body_of(open(path, encoding="utf-8").read())
    lines = text.splitlines()
    problems = []

    def where(idx: int) -> str:
        n = text.count("\n", 0, idx)
        return f"line {n + 1}: {lines[n].strip()[:90]}"

    for ch, name in (("—", "em dash"), ("–", "en dash")):
        for m in re.finditer(ch, text):
            problems.append(f"[dash] {name}, {where(m.start())}")
    for w in BANNED_WORDS:
        for m in re.finditer(r"(?<![\w-])" + re.escape(w) + r"(?![\w-])", text, re.I):
            problems.append(f"[word] '{m.group(0)}', {where(m.start())}")
    for name in CONFIDENTIAL_NAMES:
        for m in re.finditer(r"(?<!\w)" + re.escape(name) + r"(?!\w)", text):
            problems.append(f"[confidential] names '{name}', {where(m.start())}")
    for pat, why in CONFIDENTIAL_PATTERNS:
        # IDs and tool names are case-sensitive (an "airtel-4670004" URL slug is not a ticket)
        for m in re.finditer(pat, text, 0 if why in ("ticket or issue ID", "change or incident number", "tool named next to a number") else re.I):
            problems.append(f"[confidential] {why} '{m.group(0)}', {where(m.start())}")
    for m in re.finditer(r"\bkern\b", text, re.I):
        problems.append(f"[private] mentions kern, {where(m.start())}")
    warnings = []
    for w in WARN_WORDS:
        for m in re.finditer(r"(?<![\w-])" + re.escape(w) + r"(?![\w-])", text, re.I):
            warnings.append(f"[warn] '{m.group(0)}' (cut it if it adds nothing), {where(m.start())}")
    return problems, warnings


def main() -> int:
    if len(sys.argv) < 2:
        print(__doc__)
        return 2
    failed = False
    for path in sys.argv[1:]:
        problems, warnings = check(path)
        for w in warnings:
            print("  " + w)
        if problems:
            failed = True
            print(f"FAIL {path} ({len(problems)})")
            for p in problems:
                print("  " + p)
        else:
            print(f"PASS {path}")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
