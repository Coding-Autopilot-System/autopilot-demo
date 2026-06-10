# F-02 strict YAML validation

Issue Description: CI printed YAML parsing warnings but always returned success.
State: Invalid workflow YAML could pass the portfolio CI check.
Action: Made parsing errors fatal and pinned the YAML parser dependency.
Result: CI now fails closed when workflow YAML is missing or invalid.
Diff Patch: Updated `.github/workflows/ci.yml` and added `requirements-dev.txt`.
Rationale: Validation jobs must fail on the condition they claim to validate.
