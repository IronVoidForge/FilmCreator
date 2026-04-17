# Wan 2.2 14B Fun Inpaint Transition

`wan22_14b_fun_inpaint_transition_api.json` is a future transition-oriented workflow export.

It is not the primary default for normal short cuts because it requires both:

- a `start_image`
- an `end_image`

That makes it a better fit for later guided transitions, target-end-frame shots, or special bridge beats rather than ordinary “approved keyframe to short cut motion” generation.

Notable structure in this export:

- two UNET loaders
- high-noise and low-noise LoRAs
- a start image and end image pair
- inpaint-to-video generation

This file is kept in the repo for later integration work, but it is not wired in as the default `cut_motion` path.
