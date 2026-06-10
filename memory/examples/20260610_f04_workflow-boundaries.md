# F-04 least-privilege workflow boundaries

Issue Description: CI and Demo CI relied on repository-default token permissions and had no execution timeout.
State: Jobs could inherit broader permissions and run without a repository-defined time bound.
Action: Declared read-only contents permission and five-minute job timeouts.
Result: Routine workflows now have explicit least privilege and bounded execution.
Diff Patch: Updated `.github/workflows/ci.yml` and `.github/workflows/demo-ci.yml`.
Rationale: Security boundaries should be visible and enforced in source control.
