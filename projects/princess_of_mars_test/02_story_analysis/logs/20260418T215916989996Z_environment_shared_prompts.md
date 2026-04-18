# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-18T21:59:16.989996+00:00
- task: environment_shared_prompts

## System Prompt
````text
You are FilmCreator's local authoring analyst.
Work like a careful local planning assistant for chapter analysis and shot-prep authoring.
Return exactly one FILMCREATOR packet in Markdown.
Do not return JSON.
Do not use markdown fences.
Do not add commentary before or after the packet.
Preserve uncertainty instead of inventing hidden facts.
Prefer short, concrete section bodies over long prose.
Follow the requested headings and record fields exactly.
When asked to write Markdown file contents, place the complete file body inside the requested SECTION tags.
When asked to extract render-facing facts, focus on visible, continuity-relevant details.
If information is missing, say so briefly instead of guessing.
````

## User Prompt
````text
Project slug: princess_of_mars_test

Asset id: martian_valley_hills

Task: write one reusable shared environment-reference prompt draft for stable local generation.

Return exactly one Markdown packet using this outer envelope:
[[FILMCREATOR_PACKET]]
task: environment_shared_prompts
version: 1

Repeat one FILMCREATOR_RECORD block for every extracted item of that type.

[[FILMCREATOR_RECORD]]
type: environment_prompt
asset_id: <value>

[[SECTION purpose]]
...purpose content...
[[/SECTION]]

[[SECTION positive_prompt]]
...positive_prompt content...
[[/SECTION]]

[[SECTION negative_prompt]]
...negative_prompt content...
[[/SECTION]]

[[SECTION inputs_markdown]]
...inputs_markdown content...
[[/SECTION]]

[[SECTION continuity_notes_markdown]]
...continuity_notes_markdown content...
[[/SECTION]]

[[SECTION repair_notes_markdown]]
...repair_notes_markdown content...
[[/SECTION]]
[[/FILMCREATOR_RECORD]]
[[/FILMCREATOR_PACKET]]



Rules:

- purpose and inputs may use stable asset ids

- final positive and negative prompt bodies should avoid proper nouns and use descriptive noun phrases

- keep prompts concrete and visible

- emphasize stable architecture, geography, scale, atmosphere, and recurring environmental anchors



Environment breakdown path: projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/martian_valley_hills.md

Role: Secondary setting for ship movement and burning.
Architecture: Open plain, hills with crests.
Lighting: Sunlight gleaming on ships, dim vistas of distance.
Atmosphere: Vast, open, awe-inspiring.
Scale: Ship drifting fifty feet above ground, rising higher into air.
Anchors: Hill crest, valley floor, distant horizon.

````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
task: environment_shared_prompts
version: 1

[[FILMCREATOR_RECORD]]
type: environment_prompt
asset_id: martian_valley_hills

[[SECTION purpose]]
Generate stable environment reference for ship movement sequences. Establish open plain with hills as secondary setting for burning and drifting action. Maintain vast atmospheric scale with visible anchors for spatial continuity during camera movement through valley terrain.
[[/SECTION]]

[[SECTION positive_prompt]]
Open plain landscape with rolling hills featuring distinct crests, sunlight reflecting off metallic ship surfaces, dim atmospheric distance vistas, vast open sky, awe-inspiring environmental scale, ship drifting fifty feet above ground level, rising higher into air, hill crest anchor point, valley floor reference, distant horizon marker, natural lighting conditions, expansive geography
[[/SECTION]]

[[SECTION negative_prompt]]
proper nouns, specific location names, enclosed spaces, dark shadows obscuring visibility, cramped architecture, artificial lighting sources, close-up restricted views, limited atmospheric depth, ground contact with ship, confined terrain, obstructed horizons, weather effects reducing clarity, restricted camera movement, small scale environments, detailed interior structures
[[/SECTION]]

[[SECTION inputs_markdown]]
```markdown
## Environment Reference: martian_valley_hills

### Primary Function
Secondary setting for ship movement and burning sequences. Open plain with hills serves as backdrop for drifting action at elevated altitude.

### Spatial Anchors
- Hill crest: Primary visual anchor point for camera orientation
- Valley floor: Ground reference for scale perception
- Distant horizon: Atmospheric depth marker for environment boundaries

### Lighting Conditions
Sunlight gleaming on ship surfaces creates metallic reflections. Dim atmospheric distance vistas establish spatial separation between foreground and background elements.

### Scale Parameters
Ship maintains fifty feet above ground level during initial drifting phase, rising higher into air as sequence progresses. Open plain architecture supports expansive camera movement without obstruction.

### Atmospheric Qualities
Vast open environment with awe-inspiring scale. Natural lighting conditions maintain visibility while preserving atmospheric depth through dim distance vistas.
```
[[/SECTION]]

[[SECTION continuity_notes_markdown]]
```markdown
## Continuity Guidelines for martian_valley_hills

### Camera Movement
Maintain elevated perspective during ship drifting sequences. Hill crest anchor provides consistent orientation reference throughout camera sweeps across valley terrain.

### Environmental Anchors
- Keep hill crest visible in at least 70% of frames during primary movement sequences
- Valley floor should appear as distant reference point maintaining scale perception
- Distant horizon must remain unobstructed for atmospheric depth continuity

### Lighting Consistency
Sunlight reflection on ship surfaces should maintain consistent intensity across sequence. Dim distance vistas preserve spatial separation between foreground ship and background landscape elements.

### Scale Maintenance
Ship altitude progression from fifty feet above ground to higher elevation should be visually clear through environmental reference points. Open plain architecture supports continuous camera movement without visual interruption.
```
[[/SECTION]]

[[SECTION repair_notes_markdown]]
```markdown
## Repair Notes for martian_valley_hills

### Common Issues Observed
- Ship contact with ground level during drifting sequences breaks elevated perspective continuity
- Hill crest anchor point becomes obscured in wide camera sweeps, losing spatial orientation reference
- Distance vistas too bright, reducing atmospheric depth perception between foreground and background
- Lighting intensity fluctuates inconsistently across sequence frames, disrupting visual cohesion

### Recommended Fixes
- Maintain fifty feet minimum altitude during all ship movement phases to preserve elevated perspective
- Ensure hill crest remains visible through camera framing adjustments during wide shots
- Adjust distance vista brightness to maintain dim atmospheric quality for depth perception
- Standardize lighting intensity across all sequence frames for consistent visual appearance

### Prevention Measures
- Establish clear altitude markers in environment reference documentation
- Create checklist for hill crest visibility during camera movement planning
- Implement lighting consistency verification before sequence completion
```
[[/SECTION]]
[[/FILMCREATOR_RECORD]]
[[/FILMCREATOR_PACKET]]
````
