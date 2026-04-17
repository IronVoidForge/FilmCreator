# Video Workflow Home

These are the local video-workflow families we are organizing for future orchestrator support.

- `cut_motion_wan_5b_short_i2v/wan22_5b_short_cut_image_to_video_api.json`
  - Wan 2.2 5B short-cut image-to-video API export for normal movie-style cuts
  - synced from `C:\Users\setho\Downloads\Video-wan2_2_5B_TextOrImage.json`
  - currently wired as the default `video.cut_motion.wan.i2v` workflow
- `cut_motion_wan_longlook/wan22_longlook_cut_motion_graph.json`
  - Wan 2.2 LongLook source graph for extended-cut motion generation
  - synced from `workflows/stills/current_workflows/LongLook - Wan2.2.json`
- `cut_motion_wan_longlook/wan22_longlook_cut_motion_api.json`
  - Wan 2.2 LongLook API export intended for ComfyUI `/prompt`
  - synced from `workflows/stills/current_workflows/LongLook - Wan2.2 API.json`
  - available for patch-point mapping and extended-cut runner integration
- `transition_wan_14b_fun_inpaint/wan22_14b_fun_inpaint_transition_api.json`
  - Wan 2.2 14B fun inpaint API export for later guided transition or target-end-frame work
  - synced from `C:\Users\setho\Downloads\VIDEO_wan2_2_14B_fun_inpaint.json`
  - preserved for later integration, not the default short-cut path

Current intent:

- normal movie-style cuts should use a standard Wan single-image-to-video workflow family
- LongLook is reserved for explicitly extended cuts rather than the default path for ordinary approximately 5-second cuts
- a longer cut around 10 seconds may be represented as multiple planned short motion segments before we reach for LongLook

Video workflows should only be added to the orchestrator registry after:

- they have an API-exported JSON intended for ComfyUI `/prompt`
- their patch points for prompt text, input image, save prefix, and run controls are known
- their output contract is documented for the relevant stage family
