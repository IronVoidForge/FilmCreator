# Wan LongLook Cut Motion

`wan22_longlook_cut_motion_graph.json` is the editable source graph for Wan 2.2 cut-motion work.

`wan22_longlook_cut_motion_api.json` is the API-exported workflow intended for ComfyUI `/prompt`.

This family folder now contains both forms so we can keep source editing and API execution aligned.

This workflow family is reserved for explicitly extended cuts. It is not the intended default path for ordinary approximately 5-second movie cuts.

Known patch points from the current API export:

- positive prompt: node `3` -> `inputs.text`
- negative prompt: node `4` -> `inputs.text`
- starting keyframe image: node `85` -> `inputs.image`
- first chunk samplers: nodes `35` and `36`
- chunk video outputs: nodes `78`, `90`, `104`, `131`, `145`, `146`, `147`, `148`, and `150`

Current explicit registry entry:

- `video.cut_motion.wan.longlook.extended`

The normal default has now moved to the short-cut Wan 5B workflow family.

Current extended-cut runner behavior:

- patches the same cut-motion prompt into every positive chunk prompt node
- patches the same negative prompt into every negative chunk prompt node
- injects the approved keyframe as the starting image
- patches all registered sampler seed nodes to the candidate seed
- prunes the workflow to the final preview output node so one candidate yields one routed preview video
