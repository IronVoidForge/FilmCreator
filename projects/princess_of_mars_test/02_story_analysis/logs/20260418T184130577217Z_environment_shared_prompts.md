# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-18T18:41:30.577217+00:00
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

Asset id: window_upper_floor

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



Environment breakdown path: projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/window_upper_floor.md

# Window Upper Floor - Carter's Vantage Point

## Environment Role
Primary observation setting for John Carter's perspective during the fleet approach and battle sequence.

## Architecture and Geography
Upper floor residential or military structure with large window opening facing city plaza. Elevated position provides clear sightlines to approaching airships and rooftop activity.

## Lighting and Atmosphere Cues
Natural daylight streaming through window, sunlight reflecting off distant ship devices visible from interior. Smoke haze from burning vessel may drift into view. Interior shadows contrast with bright exterior light.

## Scale and Environmental Anchors
Human-scale interior space with large window as primary anchor point. Window frame defines composition boundaries. Distant cityscape provides depth reference. Airships appear at varying distances through glass.

## Descriptive Noun Phrases for Render Prompts
- Large observation window
- Upper floor interior
- Daylight streaming through glass
- City plaza view from above
- Distant airship silhouette
- Smoke haze in distance
- Window frame composition
- Interior shadows and exterior light contrast

````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
task: environment_shared_prompts
version: 1

[[FILMCREATOR_RECORD]]
type: environment_prompt
asset_id: window_upper_floor

[[SECTION purpose]]
Primary observation setting for character perspective during fleet approach and battle sequence. Elevated interior space with large window opening facing city plaza provides clear sightlines to approaching airships and rooftop activity. Human-scale interior anchors composition while distant cityscape establishes depth reference. Window frame defines composition boundaries with varying airship distances visible through glass.
[[/SECTION]]

[[SECTION positive_prompt]]
Large observation window, upper floor interior, daylight streaming through glass, city plaza view from above, distant airship silhouette, smoke haze in distance, window frame composition, interior shadows and exterior light contrast, elevated residential structure, natural lighting conditions, clear sightlines to approaching vessels, rooftop activity visible through glass
[[/SECTION]]

[[SECTION negative_prompt]]
Proper nouns, text overlays, distorted architecture, unnatural lighting, blurry details, incorrect scale, missing environmental anchors, darkened interior, artificial shadows, obscured window view, compressed depth, flat composition, unnatural smoke density, blocked sightlines, low ceiling height, cramped space, artificial light sources
[[/SECTION]]

[[SECTION inputs_markdown]]
- Asset ID: window_upper_floor
- Environment Role: Primary observation setting for character perspective during fleet approach and battle sequence
- Architecture Type: Upper floor residential or military structure with large window opening facing city plaza
- Scale Reference: Human-scale interior space with large window as primary anchor point
- Lighting Conditions: Natural daylight streaming through window, sunlight reflecting off distant ship devices visible from interior
- Atmospheric Elements: Smoke haze from burning vessel may drift into view, interior shadows contrast with bright exterior light
- Composition Anchors: Window frame defines composition boundaries, distant cityscape provides depth reference, airships appear at varying distances through glass
[[/SECTION]]

[[SECTION continuity_notes_markdown]]
- Window Upper Floor serves as Carter's Vantage Point for observing fleet approach and battle sequence
- Large observation window acts as primary anchor point defining composition boundaries
- Daylight streaming through glass establishes natural lighting conditions throughout scene
- Distant airship silhouette provides depth reference at varying distances through glass
- Smoke haze in distance indicates burning vessel activity from exterior environment
- Interior shadows and exterior light contrast creates visual tension between spaces
- Elevated position ensures clear sightlines to approaching airships and rooftop activity
- City plaza view from above establishes geographic context for battle sequence
[[/SECTION]]

[[SECTION repair_notes_markdown]]
- Ensure window frame composition remains visible as primary anchor point throughout renders
- Maintain natural daylight streaming through glass without artificial light sources interfering
- Verify distant airship silhouette appears at appropriate varying distances through glass
- Check smoke haze density does not obscure critical environmental anchors or sightlines
- Confirm interior shadows contrast properly with bright exterior light for visual tension
- Validate elevated position provides clear sightlines to approaching vessels and rooftop activity
- Ensure city plaza view from above establishes proper geographic context without distortion
- Monitor that human-scale interior space remains consistent across all composition variations
[[/SECTION]]
[[/FILMCREATOR_RECORD]]
[[/FILMCREATOR_PACKET]]
````
