# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-18T18:05:05.676739+00:00
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

Asset id: valley_hills_vista

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



Environment breakdown path: projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/valley_hills_vista.md

# Valley Hills Vista Environment

## Environment Role
Background landscape setting providing distant terrain context for fleet engagement sequence.

## Architecture and Geography
Distant valley floor with hills forming natural landscape backdrop. Open terrain visible from upper floor window and plaza positions. Natural topography provides expansive view of burning ship drifting southeast across valley floor before retreating into distance.

## Lighting and Atmosphere Cues
Daylight conditions with clear visibility across valley terrain. Atmospheric depth conveyed through distant ship movement across valley floor. Landscape vista provides scale reference for fleet engagement sequence, showing burning ship's journey from combat zone to distant horizon.

## Scale Cues and Environmental Anchors
Valley floor serves as primary horizontal anchor for distant ship movement. Hills form natural landscape boundaries providing vertical context. Distant position allows observation of burning ship's complete journey across valley terrain before disappearing into distance. Interior observation points (upper floor window, plaza) frame vista through architectural openings.

## Descriptive Noun Phrases for Render-Facing Prompts
- distant valley floor terrain
- hills natural landscape boundaries
- expansive view conditions
- daylight clear visibility
- burning ship journey path
- horizon distance reference
- landscape backdrop environment
- interior-exterior vista framing

````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
task: environment_shared_prompts
version: 1
[[FILMCREATOR_RECORD]]
type: environment_prompt
asset_id: valley_hills_vista
[[SECTION purpose]]
Background landscape setting providing distant terrain context for fleet engagement sequence with open valley floor and hills forming natural boundaries visible from interior observation points. Daylight conditions with clear visibility across expansive vista showing burning ship journey path from combat zone to distant horizon.
[[/SECTION]]
[[SECTION positive_prompt]]
distant valley floor terrain, hills natural landscape boundaries, expansive view conditions, daylight clear visibility, burning ship journey path, horizon distance reference, landscape backdrop environment, interior-exterior vista framing through architectural openings
[[/SECTION]]
[[SECTION negative_prompt]]
proper nouns, specific brand names, indoor clutter, foggy or overcast weather, close-up details obscuring vista, artificial lighting, night conditions, crowded scenes, text overlays, distorted perspective, excessive shadows blocking horizon view
[[/SECTION]]
[[SECTION inputs_markdown]]
- Environment Role: Background landscape setting providing distant terrain context for fleet engagement sequence
- Architecture and Geography: Distant valley floor with hills forming natural landscape backdrop. Open terrain visible from upper floor window and plaza positions. Natural topography provides expansive view of burning ship drifting southeast across valley floor before retreating into distance.
- Lighting and Atmosphere Cues: Daylight conditions with clear visibility across valley terrain. Atmospheric depth conveyed through distant ship movement across valley floor. Landscape vista provides scale reference for fleet engagement sequence, showing burning ship's journey from combat zone to distant horizon.
- Scale Cues and Environmental Anchors: Valley floor serves as primary horizontal anchor for distant ship movement. Hills form natural landscape boundaries providing vertical context. Distant position allows observation of burning ship's complete journey across valley terrain before disappearing into distance. Interior observation points (upper floor window, plaza) frame vista through architectural openings.
[[/SECTION]]
[[SECTION continuity_notes_markdown]]
- Valley floor serves as primary horizontal anchor for distant ship movement
- Hills form natural landscape boundaries providing vertical context
- Distant position allows observation of burning ship's complete journey across valley terrain before disappearing into distance
- Interior observation points (upper floor window, plaza) frame vista through architectural openings
- Daylight conditions maintain clear visibility across expansive vista
- Burning ship journey path visible from combat zone to distant horizon
[[/SECTION]]
[[SECTION repair_notes_markdown]]
- Ensure vista framing remains consistent with interior-exterior perspective
- Maintain daylight clarity without fog or overcast interference
- Preserve horizontal valley floor anchor for ship movement continuity
- Keep hills as vertical landscape boundaries without distortion
- Verify burning ship journey path visibility from upper observation points
- Check horizon distance reference maintains scale accuracy for fleet engagement sequence
[[/SECTION]]
[[/FILMCREATOR_RECORD]]
[[/FILMCREATOR_PACKET]]
````
