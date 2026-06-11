# F-07 richer intake audit evidence

Issue Description: Intake issues omitted operational context needed to reconstruct a failure.
State: Issues recorded workflow, branch, SHA, run URL, and failed steps only.
Action: Added run attempt, triggering event, actor, and conclusion to every intake issue body.
Result: Each issue now carries a stronger self-contained audit trail.
Diff Patch: Updated the intake workflow and its contract tests.
Rationale: Operational evidence should support diagnosis without requiring immediate API access.
