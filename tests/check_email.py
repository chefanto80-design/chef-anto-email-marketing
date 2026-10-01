"""Rule checks for a Chef Anto email draft (skill: chef-anto-email).

Usage: python3 tests/check_email.py demo/output.md
"""
import re
import sys

text = open(sys.argv[1], encoding="utf-8").read()
lower = text.lower()
checks = []


def check(name, ok, detail=""):
    checks.append((name, ok, detail))


def field(label):
    m = re.search(r"\*\*" + re.escape(label) + r":\*\*\s*(.+)", text)
    return m.group(1).strip() if m else ""


subjects = [field("Subject"), field("Alternate 1"), field("Alternate 2")]
for i, s in enumerate(subjects):
    name = "Subject" if i == 0 else f"Alternate {i}"
    check(f"{name} present and under 45 characters", 0 < len(s) < 45, f"{len(s)} chars")
    check(f"{name}: no spammy caps or FREE!!!", "FREE" not in s and "!!" not in s)
preview = field("Preview text")
check("Preview text under 90 characters", 0 < len(preview) < 90, f"{len(preview)} chars")
buttons = re.findall(r"^\[ .+ \]$", text, re.M)
check("Exactly one CTA button", len(buttons) == 1, f"{len(buttons)} found")
check("Sign-off", "Chef Anto 🌿🤓❤️" in text)
check("P.S. present", "**P.S.**" in text)
check("Send timing and group given", "**send:**" in lower and "**group:**" in lower)
check("Story tagline used", "born in romania. rebuilt in miami." in lower)
check("Lead magnet named", "5 fridge meals" in lower or "5 meals from what's already in your fridge" in lower)
body = text.split("---")[1] if text.count("---") >= 2 else text
paras = [p for p in body.split("\n\n") if p.strip()]
longest = max(len(p.split()) for p in paras)
check("Phone-friendly: no paragraph over 60 words", longest <= 60, f"longest {longest} words")
check("No invented stats in the email (no % or 'open rate')", "%" not in body and "open rate" not in body.lower())
check("Draft-only statement", "draft only" in lower)

passed = sum(ok for _, ok, _ in checks)
for name, ok, detail in checks:
    print(f"{'PASS' if ok else 'FAIL'}  {name}" + (f"  ({detail})" if detail else ""))
print(f"\n{passed}/{len(checks)} checks passed")
sys.exit(0 if passed == len(checks) else 1)
