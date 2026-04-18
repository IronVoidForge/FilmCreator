# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-18T17:22:02.410860+00:00
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

# Upper Floor Window View

## Environment Role
Primary observation point for narrator's initial perspective.

## Architecture and Geography
Elevated window frame overlooking valley terrain and distant hills. Glass panes provide framed view of landscape beyond immediate city walls.

## Lighting and Atmosphere Cues
Natural daylight filtering through window glass. Soft shadows cast by interior architecture. Distant haze over valley floor suggesting Martian atmospheric conditions.

## Scale Cues and Environmental Anchors
Window frame establishes human scale against vast landscape. Interior room boundaries define intimate space contrasting with exterior openness.

## Descriptive Noun Phrases
- "framed valley view"
- "distant hill silhouette"
- "interior window frame"
- "Martian atmospheric haze"
- "elevated observation vantage"

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
Primary observation point for narrator's initial perspective, establishing elevated window frame overlooking valley terrain and distant hills with natural daylight filtering through glass panes. Soft shadows cast by interior architecture contrast with exterior openness. Martian atmospheric haze over valley floor suggests environmental conditions. Window frame establishes human scale against vast landscape. Interior room boundaries define intimate space contrasting with exterior openness.
[[/SECTION]]

[[SECTION positive_prompt]]
elevated observation vantage, framed valley view, distant hill silhouette, interior window frame, Martian atmospheric haze, natural daylight filtering through glass panes, soft shadows cast by interior architecture, human scale against vast landscape, intimate interior room boundaries, elevated window overlooking terrain, glass panes providing framed view of landscape beyond immediate city walls
[[/SECTION]]

[[SECTION negative_prompt]]
proper nouns, brand names, specific character references, indoor artificial lighting, night time conditions, heavy fog obscuring distant hills, close-up interior only without exterior view, distorted perspective, unrealistic scale proportions, modern urban skyline elements, clear weather without atmospheric haze, low angle shots from ground level
[[/SECTION]]

[[SECTION inputs_markdown]]
projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/upper_floor_window.md
[[/SECTION]]

[[SECTION continuity_notes_markdown]]
Maintain consistent elevated perspective across all frames. Window frame boundaries should remain stable in composition. Atmospheric haze density should not vary significantly between shots. Interior room scale must stay human-sized relative to exterior landscape. Lighting temperature should reflect natural daylight conditions throughout sequence.
[[/SECTION]]

[[SECTION repair_notes_markdown]]
If generation shows ground-level perspective, reframe to elevated vantage point. If interior dominates without exterior view, ensure glass panes provide framed landscape beyond city walls. If atmospheric haze is missing, add Martian atmospheric conditions over valley floor. If lighting appears artificial, adjust to natural daylight filtering through window glass.
[[/SECTION]]

[[/FILMCREATOR_RECORD]]
[[/FILMCREATOR_PACKET]]
````
