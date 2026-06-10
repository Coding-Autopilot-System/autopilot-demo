# F-03 immutable Action references

Issue Description: Workflows trusted mutable major-version Action tags.
State: Upstream tag movement could change executed code without a repository diff.
Action: Pinned checkout v4.2.2 and github-script v7.0.1 to verified commit SHAs.
Result: Third-party workflow code is immutable and remains human-readable through version comments.
Diff Patch: Updated CI and intake workflow Action references.
Rationale: Immutable references reduce CI supply-chain risk.
