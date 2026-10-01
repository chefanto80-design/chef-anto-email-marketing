# Chef Anto Email Marketing System ✉️

**The email side of the Chef Anto brand: a MailerLite setup, a list-growth plan and an AI agent that drafts every email in Chef Anto's voice.**
Part of the [Chef Anto AI Agency](https://github.com/chefanto80-design/chef-anto-agent). Built by Chef Anto (Antoanela Alexander), Miami.

## The system
| Piece | Status |
|---|---|
| Platform | MailerLite, sending domain chefanto.com (SPF/DKIM/DMARC set up) |
| Main group | "Website Signups" |
| Lead magnet | "5 Meals From What's Already In Your Fridge": five Balkan-inspired meal formulas + Chef Anto app CTA |
| Goal | 500 subscribers in 90 days |
| Growth channels | CTA in every LinkedIn post (link in first comment), QR code on pop-up tables, Instagram "FRIDGE" keyword, app opt-in |
| Email agent | [`skill/SKILL.md`](skill/SKILL.md): writes welcome sequences, newsletters, pop-up announcements, re-engagement |

### Open items (honest status)
- ⚠️ **The chefanto.com signup form is not connected yet.** Tested 2026-10-01: submitting it shows an alert, "Connect this form to MailerLite (form ID: LpK5ms) before publishing." See [chefanto-website](https://github.com/chefanto80-design/chefanto-website).
- Lead magnet not yet attached to a MailerLite automation.
- Domain warm-up not started.

## The welcome sequence
| # | Email | Delay |
|---|---|---|
| 1 | Deliver the guide + story ("Born in Romania. Rebuilt in Miami.") | Immediately |
| 2 | One fridge recipe | 1 day |
| 3 | The mission: one billion meals saved | 2 days |
| 4 | Try the Chef Anto app (3 free scans) | 2 days |
| 5 | Invite to Baba / Dream House | 3 days |

## Files
| Path | What it is |
|---|---|
| [`skill/SKILL.md`](skill/SKILL.md) | Email agent instructions (Claude skill) |
| [`demo/output.md`](demo/output.md) | Real demo: welcome email #1, verbatim |
| [`tests/check_email.py`](tests/check_email.py) | Rule checker (16 checks) |

## How to use the agent
**Claude app:** zip the `skill` folder renamed to `chef-anto-email`, upload it in Claude's Settings → Skills, then ask:
> Use chef-anto-email. Write welcome email #2 for Website Signups.

**Claude Code:** `mkdir -p ~/.claude/skills/chef-anto-email && cp skill/SKILL.md ~/.claude/skills/chef-anto-email/`

Then paste the draft into MailerLite yourself. The agent never sends.

## Real demo
Run on **2026-10-01 (UTC)** in Claude (Cowork), model `claude-opus-5-5`, by invoking the `chef-anto-email` skill.

**Input (exact):**
```
Demo order: Write welcome email #1 of the 5-email welcome sequence for the MailerLite
"Website Signups" group. It delivers the lead magnet "5 Meals From What's Already In Your
Fridge" and tells my story.
```

**Output** ([full, verbatim](demo/output.md)): subject "Your 5 fridge meals are here 🥬" + 2 alternates, preview text, story body, one button ("Download my 5 fridge meals"), sign-off, P.S., timing table.

## Test results (only tests actually run)
| # | Test | Result |
|---|---|---|
| 1 | Live run of the skill on the demo input | ✅ Full email produced, saved verbatim |
| 2 | `python3 tests/check_email.py demo/output.md`, first run | ⚠️ 15/16. The "no invented stats" check failed because of a **checker bug**: it scanned the agent's own checklist line "No invented stats or open rates" |
| 3 | Same command after scoping that check to the email body | ✅ **16/16 passed** |
| 4 | Live chefanto.com signup form (in Chrome) | ❌ **Not connected**: shows a "Connect this form to MailerLite" alert |
| 5 | Checker on a deliberately bad sample | ✅ Caught it: **5/16 passed** |

Checks cover: subject + alternates under 45 characters, no spammy caps, preview under 90, exactly one button, sign-off, P.S., send timing and group, story tagline, lead magnet named, short paragraphs, no invented stats.

**Not tested yet:** the email has not been sent, so there are no open or click rates. Nothing in MailerLite was changed.

## Run the tests
```bash
python3 tests/check_email.py demo/output.md
```

---
Chef Anto 🌿🤓❤️
