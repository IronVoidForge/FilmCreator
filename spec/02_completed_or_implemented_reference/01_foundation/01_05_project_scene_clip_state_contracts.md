# 1.5 Project Scene Clip State Contracts

## Goal

Make approvals and handoffs explicit through state files instead of relying only on folder contents.

## State Layers

- `project_state.json` owns project defaults and approved shared refs.
- `scene_state.json` owns the shot roster and scene-level selections.
- `shot_state.json` owns shot-local inputs, outputs, and approval status.
- `clip_state.json` owns clip-local inputs, outputs, and approval status inside a shot.

## Rules

- Shared approved refs must be recorded at the project level.
- Scene state must identify which shots belong to the scene.
- Shot state must identify which clips belong to the shot and the prompt packages associated with that shot.
- Clip state must identify the prompt packages, planned shot-start strategy, and approved frame chain for the clip.
- Clip state should also be able to record optional consistency-assist preferences and outcomes.
- Clip state should also be able to record dialogue bindings, key item references, and shot-level prompt bundle references when those are part of the clip.
- Clip state should distinguish between:
  - the approved still or video assets that already exist
  - the continuity source that is currently approved
  - the clip plan decision about whether the next shot actually depends on a previous frame
- Continuation stages resolve their source frame from clip state only when the clip plan or fallback strategy requires that dependency.
- Before any later approvals exist, the default approved still source is the approved golden frame or approved keyframe.
- If an approved video segment is later introduced, its last approved frame may become the next continuity source for the clip, but it should not be treated as the universal default for all later shots.
- If an optional identity-consistency or anatomy-repair assist is run, state should record:
  - what source asset it was correcting
  - what character refs were used
  - whether the corrected output replaced the prior approved still for downstream motion
- State files are the contract. Folder names are supporting structure.

## Acceptance

- The runner can resume work on a clip from state alone.
- Promotion of a golden frame or shared ref updates state in one obvious place.
- Downstream stages do not need manual path hunting for refs or continuity inputs.
- The system can tell from state and planning whether a new clip should wait on a prior video output or can generate its opening keyframe independently.
- The system can also tell whether downstream motion should use the original approved keyframe or a later corrected still.
