# 2.3 Shared Ref Promotion and Reuse

## Goal

Define how reusable refs are approved once and reused many times.

## Rules

- Generated candidates are not automatically canonical.
- A human selects the approved character or environment ref.
- The approved file is promoted into `04_references/`.
- State files record the canonical approved path.
- Scene and clip jobs read approved refs from state instead of browsing folders manually.

## Acceptance

- One approved ref can be reused across scenes without copying it into every clip.
- The canonical approved asset is easy to find and replace if a better version is chosen later.
