# Wan 2.2 5B Short Cut Motion

`wan22_5b_short_cut_image_to_video_api.json` is the current primary short-cut image-to-video workflow for ordinary movie-style cuts.

This workflow family is the intended default for clips that should render as one short motion segment from one approved starting frame.

Known patch points from the current API export:

- positive prompt: node `6` -> `inputs.text`
- negative prompt: node `7` -> `inputs.text`
- starting keyframe image: node `56` -> `inputs.image`
- sampler seed: node `3` -> `inputs.seed`
- save prefix: node `58` -> `inputs.filename_prefix`

Current runtime shape:

- one approved starting frame
- one positive prompt
- one negative prompt
- one short generated video candidate
- no LongLook chunk stitching

Current default registry entry:

- `video.cut_motion.wan.i2v`
