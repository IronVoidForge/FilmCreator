# Princess of Mars Test Project Status

## Where We Are

This project is currently in the file-first authoring phase, before SQLite becomes the source of queryable structure.

The live pilot chapter has already proven that we can:

- read a pasted public-domain chapter from the project workspace
- analyze it into chapter summaries, character breakdowns, environment breakdowns, scene breakdowns, and beat bundles
- plan clips from those scenes
- keep the render side and the authoring side separated so LM Studio and ComfyUI can run at different times

## Implementation Order We Followed

1. Set up the project hierarchy and naming conventions.
2. Validated the clip-scoped keyframe render path.
3. Validated review and approved-keyframe promotion.
4. Validated the short-cut motion render path.
5. Built the packet-based LM Studio authoring path.
6. Proved chapter intake, scene decomposition, beat bundling, and clip planning on `A Princess of Mars`.
7. Split shared prompt generation into per-asset LM Studio calls.

## What Is Working

- Chapter analysis works on the live `princess_of_mars_test` pilot chapter.
- Scene planning works and writes canonical scene, beat, and clip files.
- Clip planning now produces canonical `CL###` clip ids.
- Packet parsing is robust against several LM Studio formatting quirks.
- LM Studio and ComfyUI are being kept as separate runtime phases.
- Unit tests are green for the current authoring code path.

## What Is Still Difficult

- Shared character prompt generation sometimes returns empty or malformed LM Studio output.
- Manual-description-required characters are the most common place where that happens.
- `inputs_markdown` is still slightly too brittle when the model emits raw path lines or partial formatting.
- The shared-prompt authoring step can still block the overall checkpoint when one asset fails.

## What We Plan To Work On Next

1. Make shared prompt generation resilient to empty LM Studio responses.
2. Make the shared-prompt parser tolerate more freeform `inputs_markdown` output.
3. Keep the chapter analysis and scene planning passes stable.
4. Build the character-to-scene mapping layer so each clip knows which approved refs to use.
5. Move to the first SQLite read-side sync after the file-first authoring flow is stable.
6. Return to `still_fix`, then short-cut motion tuning, then longer overnight scene batching.

## Current Testable Checkpoint

The current reliable checkpoint is:

- `analyze-chapter` succeeds
- `plan-scene` succeeds
- shared prompt generation is close, but not yet fully reliable for every asset

That means the authoring pipeline is useful now, but not yet complete enough to declare the full checkpoint finished.

