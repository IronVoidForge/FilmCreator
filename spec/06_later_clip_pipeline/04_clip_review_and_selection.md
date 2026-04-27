Status: 35%

# 3.4 Clip Review and Selection

## Goal

Keep review manual while making the results reproducible and easy to hand off.

## Rules

- Candidates stay in their stage-specific clip folders.
- Human-selected outputs copy into `stills/selected/`.
- Review copies also land in `06_reviews/selected/`.
- Clip state records the currently approved assets.
- Clip state also records the currently approved continuity source so the next run does not have to guess between golden, anchor, interval, or video-derived frames.
- Review may also trigger a fallback strategy when the default opening-keyframe plan is not good enough.
- The default fallback for most failed next-shot keyframes should be to retry by using the previous approved video last frame as an image-to-image camera-repositioning source.
- Review may intentionally request a previous-last-frame reframe even when the default keyframe did not fail, if the next shot needs exact continuity plus a new camera angle or zoom.
- A previous-last-frame reframe must produce a still candidate first. The next I2V clip should not run until that secondary view has been approved.
- Review should not force the whole system into direct `continuous_follow` mode unless the shot genuinely requires exact carry-forward continuity.
- Review may optionally trigger an automated identity-consistency assist when the composition works but a visible character drifts off-model from approved character-sheet refs.
- Review may optionally trigger an anatomy-repair assist when the shot is acceptable except for hands or other local anatomical issues.
- For identity consistency, the preferred automatic escalation order is:
  - conservative reference-guided image-to-image
  - region-aware reference conditioning when available
  - manual inpaint only when automated targeting is not reliable
- Video-wide hand-fix LoRAs should remain experimental and opt-in, not the primary default review remedy.

## Acceptance

- Review does not require moving files by hand across arbitrary folders.
- A teammate can open the clip folder and immediately see candidates, approved outputs, and next steps.
- A failed opening-keyframe review can redirect the next attempt into an explicit fallback strategy instead of improvising a new continuity rule.
- Review can distinguish between wrong shot design, identity drift, and local anatomy issues so the next corrective pass is targeted instead of wasteful.
- Review can approve a previous-last-frame-derived alternate-angle opener and mark it as the required first frame for the next clip.

