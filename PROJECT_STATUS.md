# Project Status — Dopa-Direct

**Snapshot date:** 2026-11-16  
**Status type:** Initial documentation and repository-tree assessment  
**Default branch:** main  
**Review completeness:** Partial — not a code audit or release certification

## Project purpose
Local Python toolkit intended to help users notice distraction triggers and redirect attention to chosen activities.

## Current maturity (README-declared or visible scaffolding; not independently verified)
Root includes app.py/main.py, timer/guardian/redirector/analytics/storage/streaks/achievements modules and tests/. README describes a zero-dependency toolkit; runtime behavior not verified.

## Observed repository structure
app.py, main.py, adaptive_redirector.py, guardian.py, analytics.py, storage.py, streaks.py, achievements.py, timer.py, tests/ and supporting config.

## Known issues and risks to investigate
README describes a 'background monitor' and bypass detection; verify these are opt-in, local and transparent, and do not collect browsing/activity data without consent. Habit/progress examples may be illustrative, not real user metrics. Verify storage privacy and timer behavior. No tests were run.

## Recommended next actions
Run tests and CLI smoke tests; inspect what guardian monitors and how; ensure clear opt-in/stop controls and no covert monitoring; validate local storage boundaries and deletion/export; test timer accuracy, clock changes and persistence recovery.

## Verification record
| Check | Result |
|---|---|
| Default-branch top-level tree | Inspected |
| README | Inspected |
| Deep source review | Not performed |
| Tests / build / runtime | Not run |
| Security / dependency audit | Not run |
| Live deployment / API checks | Not run |
| Independent review | Not performed |

## Change log
- 2026-11-16: Added this initial status snapshot on a review branch. No application code or existing data changed.

> Update this file only after the corresponding inspection or verification has actually been performed. Distinguish observed facts, README claims, hypotheses and unrun checks.