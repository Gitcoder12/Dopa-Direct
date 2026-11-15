# Dopa-Direct — README Explanation Draft

## In plain language

A local Python tool that helps someone notice a distraction, choose a better next task and track short focus sessions.

## What happens

The user records a distraction, chooses an activity and starts a short focus session. The CLI stores session results locally so the user can review progress later.

## Technical explanation

Local-first Python CLI that records distraction triggers, recommends an activity, runs a focus timer and stores redirects/streaks/points in local JSON. The project includes an optional Windows Attention Guardian. It should not collect sensitive browsing content or claim to treat a health condition.

Document CLI commands, local JSON schema, timer implementation, recommendation logic, Windows-only components and file paths. Explain how data can be exported or erased.

## Privacy and safety

Explain exactly what is stored and what the optional guardian can access. The tool is a productivity aid, not medical treatment or diagnosis.

## Contributing

See FEATURE_UPGRADE_PLAN.md, CONTRIBUTING.md and ACTIVITY_LOG.md.
