# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-18T18:04:54.478701+00:00
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

Asset id: upper_floor_window

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



Environment breakdown path: projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/upper_floor_window.md

# Upper Floor Window Environment

## Environment Role
Primary observation setting for narrator's vantage point during fleet engagement sequence.

## Architecture and Geography
Upper floor interior space with window opening to exterior cityscape. Elevated position above street level, providing panoramic view of approaching airships and distant valley terrain.

## Lighting and Atmosphere Cues
Interior lighting suggests daytime conditions with natural light filtering through window frame. Exterior view shows clear visibility of gray-painted vessels against sky backdrop. Atmospheric tension conveyed through narrator's elevated perspective during combat sequence.

## Scale Cues and Environmental Anchors
Window frame serves as primary architectural anchor. Elevated position allows observation of: twenty airships at distance, green Martian warriors on building facades, burning ship drifting southeast across valley floor. Interior space provides intimate contrast to expansive exterior battlefield view.

## Descriptive Noun Phrases for Render-Facing Prompts
- elevated interior observation point
- window frame architectural anchor
- panoramic cityscape vista
- daylight natural illumination
- interior-exterior visual boundary
- narrator's vantage position
- upper floor residential space
- clear sky visibility conditions

````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
task: environment_shared_prompts
version: 1

[[FILMCREATOR_RECORD]]
type: environment_prompt
asset_id: upper_floor_window

[[SECTION purpose]]
Primary observation setting for narrator's vantage point during fleet engagement sequence. Elevated interior space with window opening to exterior cityscape, providing panoramic view of approaching airships and distant valley terrain. Daytime conditions with natural light filtering through window frame. Atmospheric tension conveyed through elevated perspective during combat sequence.
[[/SECTION]]

[[SECTION positive_prompt]]
elevated interior observation point, window frame architectural anchor, panoramic cityscape vista, daylight natural illumination, interior-exterior visual boundary, narrator's vantage position, upper floor residential space, clear sky visibility conditions, gray-painted vessels against sky backdrop, green warriors on building facades, burning ship drifting across valley floor
[[/SECTION]]

[[SECTION negative_prompt]]
proper nouns, brand names, specific character names, interior darkness, night conditions, cloudy sky, street level view, close-up perspective, blurry details, distorted proportions, artificial lighting, indoor shadows, obscured visibility, low resolution, pixelation, color bleeding, inconsistent scale
[[/SECTION]]

[[SECTION inputs_markdown]]
projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/upper_floor_window.md
[[/SECTION]]

[[SECTION continuity_notes_markdown]]
Window frame serves as primary architectural anchor. Elevated position allows observation of: twenty airships at distance, green warriors on building facades, burning ship drifting southeast across valley floor. Interior space provides intimate contrast to expansive exterior battlefield view. Daylight natural illumination maintains consistent time period. Clear sky visibility conditions establish atmospheric baseline for combat sequence.
[[/SECTION]]

[[SECTION repair_notes_markdown]]
Maintain window frame as stable architectural anchor across all shots. Preserve elevated interior-exterior visual boundary consistency. Ensure daylight natural illumination remains constant throughout engagement sequence. Verify clear sky visibility conditions match established atmospheric tension. Keep scale cues consistent between interior observation point and exterior battlefield elements.
[[/SECTION]]

[[/FILMCREATOR_RECORD]]
[[/FILMCREATOR_PACKET]]
````
