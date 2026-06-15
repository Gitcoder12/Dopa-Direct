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
