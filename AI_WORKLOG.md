# AI Worklog

## Assessment
- Date: 2026-11-15
- Branch: `docs/portfolio-operating-kit-2026-11-13`
- Recommendation: Improve
- Maturity: Functional local CLI prototype with persistence, focus timer, streaks, analytics, achievements, and an optional Windows foreground-window monitor.

## Purpose and implemented scope
Dopa-Direct aims to help users record distraction triggers and redirect attention toward chosen activities.

Verified source modules include:
- `main.py`: interactive trigger selection and focus workflow.
- `adaptive_redirector.py`: ranks historically selected activities and randomizes fallback suggestions.
- `timer.py`: interruptible countdown.
- `guardian.py`: Windows foreground-window title polling.
- `storage.py`, `streaks.py`, `analytics.py`, and `achievements.py`: local state and progress features.
- `tests/test_guardian.py`: one non-Windows platform test.
- `.github/workflows/tests.yml`: compile and unittest checks on Python 3.11.

## Architecture and health
The application is a local Python CLI with JSON-backed state and a daemon-thread monitor on Windows. The monitor reads foreground-window titles and may invoke the supplied persistence callback. The README's broader behavioral claims should be presented as self-management support, not clinical treatment or a validated attention intervention.

## Findings
### P1 — Guardian thread has no lifecycle control
`guardian_worker` loops indefinitely and `start_attention_guardian` returns a daemon thread without a stop event or joinable shutdown protocol. Add a stop signal and deterministic shutdown tests so the monitor can be disabled cleanly.

### P1 — Shared state may be mutated and saved concurrently
The guardian worker mutates the shared `data_ref` dictionary and calls `save_callback` while the main CLI can also update and save state. No synchronization is visible in the inspected module. Introduce a single-writer or lock strategy and test concurrent updates.

### P2 — Repeated keyword matches can repeatedly reduce focus score
A matching foreground-window title is processed on each polling cycle. There is no debounce or per-window cooldown in the inspected worker, so a continuously open window can decrement the score repeatedly. Define a clear scoring rule and test it.

### P2 — Privacy and consent behaviour needs explicit verification
The monitor reads foreground-window titles. Document exactly what is read, what is stored, how users enable/disable it, and ensure sensitive window text is not persisted. The full application startup/opt-in path was not exhaustively traced in this pass.

### P2 — Core behaviour has little regression coverage
The inspected test suite contains one platform-availability test. Timer interruption, storage recovery, adaptive ranking, streak updates, and guardian lifecycle/concurrency need focused tests.

## Checks and evidence
- Inspected README, root tree, `main.py`, `guardian.py`, `adaptive_redirector.py`, `timer.py`, `tests/test_guardian.py`, and CI workflow.
- CI workflow defines compileall and unittest discovery.
- Local tests: NOT RUN.
- Default-branch combined status query returned no status entries; no pass/fail conclusion is drawn.
- Independent model review: NOT PERFORMED.
- External links and Windows runtime behaviour: NOT exhaustively checked.

## Next actions
1. Add guardian stop-event and shutdown handling.
2. Protect shared state and persistence from concurrent writes.
3. Add debounce/cooldown semantics.
4. Document opt-in, privacy boundaries, and platform limitations.
5. Add tests for timer, storage, redirector, streaks, and guardian lifecycle.

## PR head verification
- PR #2 head CI: Dopa-Direct Tests completed successfully. This validates the configured compileall and unittest steps on the PR head; Windows-specific runtime behaviour was not exercised by the Linux runner.
