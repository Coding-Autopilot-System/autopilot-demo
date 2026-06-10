# Enterprise Hardening Verification

**Date:** 2026-06-10
**Branch:** `hardening/enterprise-audit-20260610`
**Result:** passed with manual GitHub administration gaps

## Finding Status

| ID | Result | Evidence |
|---|---|---|
| F-01 | passed | `simulate_failure` is explicit and defaults to false |
| F-02 | passed | invalid YAML now fails CI; dependency is pinned |
| F-03 | passed | third-party Actions use verified 40-character commit SHAs |
| F-04 | passed | routine jobs declare read-only permissions and five-minute timeouts |
| F-05 | passed | seven workflow contract tests run in CI; bytecode is ignored |
| F-06 | passed | intake updates are serialized by head SHA and time-bounded |
| F-07 | passed | issues record attempt, event, actor, and conclusion |
| F-08 | passed after one reverted attempt | matching closed issues reopen; runbook covers prerequisites, reset, and troubleshooting |

## Verification Commands

- `python -m unittest discover -s tests -v`: 7 passed
- strict PyYAML parse of `.github/workflows/*.yml`: 3 validated
- PowerShell parser check of `scripts/record-fix.ps1`: passed
- `git diff --check origin/main...HEAD`: passed
- clean worktree after tests: passed

## Manual Gaps

- Protect `main` and require the `CI` status check.
- Configure the organization Actions allow-list and immutable pinning policy.
- Run the live failure-to-issue-to-repair journey after this branch is merged because `workflow_dispatch` uses the default-branch workflow definition.
- Install `actionlint` in the workstation bootstrap and add it to CI; it was not available for this verification.
