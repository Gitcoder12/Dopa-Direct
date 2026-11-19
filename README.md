# 🧠 Dopa-Direct

> Break the loop. Redirect the impulse. Build instead.

Dopa-Direct is a zero-dependency, open-source Python toolkit that helps users interrupt instant-gratification habits and redirect attention toward meaningful work.

Unlike traditional productivity tools that activate after you've already decided to focus, Dopa-Direct is designed to intervene at the moment distraction appears.

Whether it's YouTube, Reddit, Instagram, endless browsing, or another attention trap, Dopa-Direct helps transform passive consumption into intentional action.

---

## Why Dopa-Direct?

Modern applications are optimized to capture attention.

Most productivity software asks:

> "What do you want to accomplish today?"

Dopa-Direct asks:

> "Where did your attention drift right now?"

The goal is not punishment.

The goal is awareness, redirection, and consistent progress.

---

## ✨ Features

### 🎯 Urge Interception

Log a distraction before it becomes a lost hour.

Supported triggers include:

* YouTube
* Reddit
* Instagram
* Twitter / X
* WhatsApp
* Custom triggers

---

### 🔒 Focus Lock

Break the dopamine loop with a cooldown session.

Features:

* Live countdown timer
* Bypass detection
* Reward points
* Streak integration

---

### 🔥 Streak Engine

Build consistency through repeated wins.

Tracks:

* Current streak
* Best streak
* Total redirects
* Reward points

---

### 📊 Analytics Dashboard

Understand where your attention goes.

Tracks:

* Most common triggers
* Redirect frequency
* Attention patterns
* Productive activity usage

---

### 🏆 Achievement Engine

Unlock permanent badges by reaching milestones.

Examples:

* 🏆 First Redirect
* 🥉 Interception Novice
* 🥈 Focus Warrior
* 🥇 Habit Breaker
* 🔥 Consistency Spark
* ⚡ Week of Fire

---

### 🧭 Attention Guardian

A lightweight background monitor designed to increase awareness when attention begins drifting.

The Guardian can identify distraction keywords and provide gentle reminders to return to intentional work.

---

### 🎯 Adaptive Redirector

Learns which productive actions work best for you.

Instead of blindly recommending random activities, the Adaptive Redirector gradually prioritizes actions that have historically helped you break distraction loops.

---

## 🕹 Example Session

```text
==================================================
     DOPA-DIRECT v5.2: THE ADAPTIVE REDIRECTOR
==================================================

[1] Log an Instant-Gratification Impulse
[2] Add Custom Productive Activity
[3] View Progress
[4] Exit Workspace

Select an action: 1

What's pulling you in right now?

[1] YouTube
[2] Instagram
[3] Reddit
[4] Twitter/X
[5] WhatsApp
[6] Custom

Select (1-6): 1

⚠ Trigger Detected: YouTube

Recommended Redirects:

[1] Work on Dopa-Direct (Chosen 21x)
[2] Read 5 Pages (Chosen 8x)
[3] Review Git Repository Status
[4] Random Activity

Select target action: 1

⚡ REDIRECT INITIALIZED

👉 Work on Dopa-Direct

🔒 FOCUS LOCK ACTIVE
⏳ Time remaining: 00:42
```

---

## 📊 Example Dashboard

```text
┌──────────────────────────────────────────────┐
│                YOUR PROGRESS                 │
├──────────────────────────────────────────────┤
│ Current Streak    : 7                        │
│ Best Streak       : 14                       │
│ Total Redirects   : 52                       │
│ Points            : 1450                     │
│ Custom Activities : 3                        │
├──────────────────────────────────────────────┤
│ TOP TRIGGERS                                 │
├──────────────────────────────────────────────┤
│ 1. YouTube - 23x                             │
│ 2. Reddit - 12x                              │
│ 3. Instagram - 8x                            │
├──────────────────────────────────────────────┤
│ UNLOCKED BADGES                              │
├──────────────────────────────────────────────┤
│ 🏆 First Redirect                            │
│ 🥉 Interception Novice                       │
│ 🔥 Consistency Spark                         │
└──────────────────────────────────────────────┘
```

---

## 🔒 Privacy First

Dopa-Direct is designed with privacy as a core principle.

### Dopa-Direct Does NOT:

* ❌ Record keystrokes
* ❌ Capture screenshots
* ❌ Read browser history
* ❌ Upload browsing data
* ❌ Send analytics to external servers
* ❌ Require a cloud account

### Dopa-Direct Does:

* ✅ Store data locally
* ✅ Use local JSON files
* ✅ Operate completely offline
* ✅ Give users full ownership of their data

---

## 🏗 Architecture

```text
dopa-direct/

├── app.py
│   Backward-compatible launcher
│
├── main.py
│   CLI menus and dashboards
│
├── config.py
│   Constants, thresholds, colors
│
├── storage.py
│   Persistent JSON storage
│
├── timer.py
│   Focus lock countdown system
│
├── streaks.py
│   Streak and point management
│
├── analytics.py
│   Trigger tracking and analysis
│
├── achievements.py
│   Achievement evaluation engine
│
├── guardian.py
│   Attention Guardian background service
│
├── adaptive_redirector.py
│   Adaptive recommendation engine
│
└── dopa_data.json
    Local application data
```

---

## 🚀 Quick Start

Clone the repository:

```bash
git clone https://github.com/Gitcoder12/Dopa-Direct.git
```

Enter the project directory:

```bash
cd Dopa-Direct
```

Run the application:

```bash
python app.py
```

Or:

```bash
python main.py
```

No external dependencies required.

---

## 🛣 Roadmap

### Completed

* [x] v1.0 — Urge Interceptor
* [x] v2.0 — Modular Architecture Refactor
* [x] v3.0 — Analytics & Streak System
* [x] v4.0 — Achievement Engine
* [x] v5.0 — Attention Guardian
* [x] v5.2 — Adaptive Redirector

### Planned

* [ ] Daily Review Reports
* [ ] Focus Score System
* [ ] Improved Adaptive Recommendations
* [ ] Cross-Platform Guardian Support
* [ ] Desktop Interface
* [ ] Community-Contributed Activity Packs

---

## 🤝 Contributing

Contributions, bug reports, feature requests, and feedback are welcome.

If you'd like to improve Dopa-Direct:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

---

## 📜 License

MIT License

---

## 👨‍💻 Author

Created by Gitcoder12.

Focused on building tools that help people:

* Control attention
* Reduce distraction
* Build better habits
* Create more than they consume

---

> Reclaim your attention.
>
> Scroll less. Build more.


---

## AI-maintained project notes (secondary — 2026-11-13)

This section supplements the maintainer-authored README above. The original text has been restored verbatim from Git-history baseline `de68e90faff9efb0d95d01215fbd6f6c4fa88831`; this addendum does not replace or certify the original claims.

- The current source tree, runtime data and tests are the implementation source of truth. Roadmap items, draft PRs and AI-generated descriptions are not shipped features by themselves.
- Preserve real and maintainer-provided data. Never silently substitute generated or placeholder data. Clearly label and isolate synthetic fixtures.
- Mark unverified sources, identifiers, metrics, benchmark results and external claims as unknown/unverified rather than guessing.
- Verify setup, execution, tests and public claims against the exact current commit before using this repository in a job, research or academic application.
- See [MODEL_AUDIT_ROUTER.md](MODEL_AUDIT_ROUTER.md) for independent model review instructions and the merge gate.

---

## Engineering Audit & Handover — 2026-11-17

**Review scope:** default branch `main`; static inspection of `main.py`, `storage.py`, `adaptive_redirector.py`, and `config.py`. Runtime tests were not executed.

### Confirmed findings
- User state is stored in a local JSON file. `save_data()` rewrites that file directly rather than using an atomic replace/backup strategy.
- If the existing data file is malformed or unreadable, `load_data()` warns and returns default state. A later save can replace the prior file, so preserve a backup before attempting recovery from a corrupted save.
- The adaptive redirector learns activity counts from successful focus sessions; this is a simple frequency-based recommender, not a validated behavioral or clinical intervention.
- The fallback activity pool is populated from `DEFAULT_ACTIVITIES`, but corrupted or manually edited state still needs schema validation.

### Next actions
1. Use atomic writes with backup/recovery and validate the persisted JSON schema before accepting it.
2. Add tests for missing, corrupted, old-version, and partially populated save files.
3. Document the limits of the recommendation/streak model and avoid making clinical or therapeutic claims.

**Verification status:** static source inspection only; CLI behavior, focus timer behavior, and tests remain unverified.

---

## Examples Used
- Redirecting an urge to browse social media into a focused task
- Using a cooldown session to interrupt repeated distraction
- Tracking which productive activities help maintain focus


---

## Comparison with Existing Open-Source Projects

Dopa-Direct is documented as a lightweight distraction-interruption toolkit that records an urge, activates a cooldown and suggests a productive redirect. These projects provide adjacent website-blocking, activity-awareness and focus-reminder approaches.

| Project | Established focus | Relationship to Dopa-Direct |
|---|---|---|
| [LeechBlock NG](https://github.com/proginosko/LeechBlockNG) | Browser extension for blocking distracting websites with configurable schedules | Stronger browser-level blocking controls; Dopa-Direct's stated distinction is the moment-of-urge workflow and explicit redirection to a chosen activity. |
| [SelfControl](https://github.com/SelfControlApp/selfcontrol) | macOS utility that blocks distracting internet access for a set period | A focused commitment/cooldown tool; Dopa-Direct aims to pair interruption with a suggested productive next action and progress tracking. |
| [ActivityWatch](https://github.com/ActivityWatch/activitywatch) | Local activity tracking and time-use awareness | Provides activity-awareness data; Dopa-Direct focuses on deliberate self-reported interception and redirect behavior rather than passive tracking alone. |

### Where Dopa-Direct is different
- **Intervene at the impulse point:** the user records the distraction trigger before it becomes an extended browsing session.
- **Redirect, not only block:** the workflow suggests a concrete productive activity and records the user's selection.
- **Lightweight local toolkit:** the README describes a zero-dependency Python tool with local progress tracking.

### Where established projects are stronger
LeechBlock and SelfControl have more direct browser/system blocking mechanisms. ActivityWatch has a mature activity-monitoring ecosystem. Dopa-Direct should not claim to technically prevent access to distracting services unless OS/browser enforcement is implemented and tested; a logged urge or countdown is not equivalent to a blocker.

### Evidence, privacy and wellbeing limitations
Keep tracking local by default, make reminders non-punitive, and provide an easy pause/disable option. Evaluate whether users actually return to their intended task rather than measuring streaks alone. Do not frame the tool as treatment for addiction or a mental-health condition. This is a workflow comparison, not a productivity-efficacy claim.
