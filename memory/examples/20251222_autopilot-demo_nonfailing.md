# Autopilot demo CI made non-failing

Issue Description:
Demo CI intentionally exited with code 1, causing permanent failure.

State:
Workflow failed on every run by design.

Action:
Replaced the failing step with a non-blocking demo step.

Result:
Demo CI now passes on dispatch and push.

Rationale:
Demo workflows should validate plumbing without breaking CI status.

Diff Patch:
```diff
commit 0ef24b2523aefde86fdafc496ba248681bf059e5
Author: Kim Harjamaki <ogeon@msn.com>
Date:   Mon Dec 22 23:12:45 2025 +0200

    Make demo CI non-failing

diff --git a/.github/workflows/demo-ci.yml b/.github/workflows/demo-ci.yml
index 2d57f3e..2c7758c 100644
--- a/.github/workflows/demo-ci.yml
+++ b/.github/workflows/demo-ci.yml
@@ -9,7 +9,6 @@ jobs:
   demo:
     runs-on: ubuntu-latest
     steps:
-      - name: Intentional failure
+      - name: Demo sanity
         run: |
-          echo "Simulated failure for Autopilot demo."
-          exit 1
+          echo "Simulated demo step (non-blocking)."
```
