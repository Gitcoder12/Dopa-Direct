# Dopa-Direct

**A local-first Python CLI for logging distraction triggers and redirecting attention into a chosen task.**

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

Dopa-Direct records an urge or distraction, recommends a productive activity, runs a short focus-lock timer, and tracks redirects, streaks, points, and achievements in local JSON data.

## Features

- Log common or custom distraction triggers.
- Recommend productive activities using the local adaptive redirector.
- Run a timed focus session before recording success or failure.
- Track current and best streaks, redirects, points, and achievements.
- Review local trigger statistics and progress.
- Optional Attention Guardian on Windows.

## Quick Start

Python 3.10+ is recommended. The CLI uses the Python standard library; no third-party packages are required.

```bash
git clone https://github.com/Gitcoder12/Dopa-Direct.git
cd Dopa-Direct
python app.py
```

You can also start the main CLI directly:

```bash
python main.py
```

## Platform Notes

The core CLI and local JSON tracking can run across operating systems. The optional Attention Guardian uses the Windows foreground-window API and is enabled only on Windows. On Linux and macOS it safely stays disabled.

When enabled, the Guardian checks the active window title locally at the configured interval and looks for configured distraction keywords. It does not capture screenshots, record keystrokes, or send window information to a server.

## Data and Privacy

- Activity data is stored in the local JSON data file.
- The application does not require a cloud account or external analytics service.
- The Windows Guardian reads the active window title only to check configured keywords; this behavior is optional and platform-specific.

## Project Structure

```text
Dopa-Direct/
├── app.py                 # Backward-compatible launcher
├── main.py                # CLI menus and progress views
├── config.py              # Defaults and Guardian settings
├── storage.py             # Local JSON persistence
├── timer.py               # Focus timer
├── streaks.py             # Streak and point tracking
├── analytics.py           # Trigger summaries
├── achievements.py        # Achievement rules
├── adaptive_redirector.py # Local activity recommendations
├── guardian.py            # Optional Windows foreground-window monitor
└── tests/
    └── test_guardian.py   # Platform fallback regression test
```

## Run Tests

```bash
python -m unittest discover -s tests -v
```

## Scope and Limitations

Dopa-Direct is a self-tracking and focus aid, not a medical or mental-health treatment. Its trigger matching and activity recommendations are simple local heuristics. Progress scores and streaks are motivational indicators, not validated measures of attention or productivity.

## License

MIT. See [LICENSE](LICENSE).

---

## Project handbook

- [Activity log](ACTIVITY_LOG.md) · [Feature upgrade plan](FEATURE_UPGRADE_PLAN.md)
- [Company and team fit](COMPANY_FIT.md) · [README explanation draft](README_ADDENDUM_DRAFT.md)
- [README quality checklist](README_QUALITY_CHECKLIST.md)
- [Contributing](CONTRIBUTING.md) · [Agent instructions](AGENTS.md) · [Agent skills](SKILLS.md)

## Understanding the project

### In plain language

A local Python tool that helps someone notice a distraction, choose a better next task and track short focus sessions.

### Technical and research view

The user records a distraction, chooses an activity and starts a short focus session. The CLI stores session results locally so the user can review progress later.

For future work, see [FEATURE_UPGRADE_PLAN.md](FEATURE_UPGRADE_PLAN.md), [ACTIVITY_LOG.md](ACTIVITY_LOG.md), [COMPANY_FIT.md](COMPANY_FIT.md) and [CONTRIBUTING.md](CONTRIBUTING.md).
