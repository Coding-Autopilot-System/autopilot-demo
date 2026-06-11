# F-05 workflow contract tests

Issue Description: No automated tests protected workflow behavior and security invariants.
State: Regressions in YAML validity, Action pinning, permissions, timeouts, or demo failure behavior depended on review alone.
Action: Added standard-library workflow contract tests and executed them from CI.
Result: Core demo and security invariants now fail visibly in pull requests.
Diff Patch: Added `tests/test_workflows.py` and updated `.github/workflows/ci.yml`.
Rationale: Workflow code needs executable contracts like application code.
