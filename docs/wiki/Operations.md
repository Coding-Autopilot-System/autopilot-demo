# Operations

## Run the demo

```bash
gh workflow run demo-ci.yml -R Coding-Autopilot-System/autopilot-demo
gh issue list -R Coding-Autopilot-System/autopilot-demo --label autofix --label queued
gh pr list -R Coding-Autopilot-System/autopilot-demo
```

## Demo runbook

1. Trigger `.github/workflows/demo-ci.yml` with `simulate_failure=true` to produce a known
   failure signal. Regular pushes and default dispatches stay green.
2. Confirm `.github/workflows/autopilot-create-issue.yml` creates an `autofix + queued` issue.
3. Watch `autopilot-core` pick up the issue and open a PR back into this repo.
4. Use this repo's issue, branch, and PR history as the audit trail for the demo.

## CI workflows

| Workflow | Purpose |
|---|---|
| `ci.yml` | Portfolio CI — YAML validation (always passes) |
| `demo-ci.yml` | Demo trigger — simulates CI activity to test the intake flow |
| `autopilot-create-issue.yml` | Intake — creates the `autofix + queued` issue on workflow failure |
| `codeql.yml` | CodeQL static analysis |
| `pr-lint.yml` | PR metadata/title linting |
| `stale.yml` | Stale issue/PR sweep |
| `pages.yml` | Publishes docs to GitHub Pages |

There is no coverage-percentage gate in this repo — `ci.yml` validates workflow YAML only, by
design (this repo has no application code to test).

## Local verification

```bash
python -m unittest discover -s tests -v
```

Run this before triggering the demo if CI fails at the validation step, per the README's
troubleshooting guidance.

## Reset and troubleshooting

1. Close the completed intake issue and merge or close its repair pull request before the next
   demonstration.
2. Re-run with `simulate_failure=true`; intake reopens the matching issue when the same commit
   is demonstrated again.
3. If no issue appears, inspect
   `gh run list -R Coding-Autopilot-System/autopilot-demo --workflow autopilot-create-issue.yml`
   and confirm the failed run was named `Demo CI`.
4. If the issue remains queued, verify the `autopilot-core` operator is running and can read
   issues and create branches and pull requests in this repository.

<!-- docs-verified: ec62179aa2c20bc731542de4ac3fec9cc94a831d 2026-07-08 -->
