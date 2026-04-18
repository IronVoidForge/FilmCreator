# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-18T20:59:53.673957+00:00
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

Asset id: open_ground_hill

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



Environment breakdown path: projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/open_ground_hill.md

**Role:** Primary setting / Retreat location

**Architecture/Geography:** Open ground with hill crests forming natural elevation markers. Gray air ships swing slowly over hill ridges, banners and odd devices visible on prows.

**Lighting/Atmosphere:** Daylight conditions with slow-moving aerial vessels creating atmospheric tension. Smoke from burning banners adds visual texture during battle sequences.

**Scale:** Large-scale environment accommodating twenty air ships in formation. Hill crests provide reference points for fleet positioning and movement patterns.

**Anchors:** Hill crests, air ship prows, banner displays, ground-level observation points.

**Descriptive Phrases:** Gray air ships over hill crests, strange banners on prows, open ground retreat zone, aerial vessel formation, hill ridge elevation markers.

````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
task: environment_shared_prompts
version: 1

[[FILMCREATOR_RECORD]]
type: environment_prompt
asset_id: open_ground_hill

[[SECTION purpose]]
Primary setting / Retreat location for large-scale aerial fleet operations. Open ground with hill crests forming natural elevation markers and atmospheric tension zones. Stable architecture accommodating twenty air ships in formation with recurring environmental anchors at ground level and ridge positions.
[[/SECTION]]

[[SECTION positive_prompt]]
open ground retreat zone, gray air ships over hill crests, strange banners on prows, aerial vessel formation, hill ridge elevation markers, daylight conditions, smoke from burning banners, ground-level observation points, large-scale environment, natural elevation markers, atmospheric tension zones, fleet positioning reference points, banner displays on prows, open terrain with hill crests
[[/SECTION]]

[[SECTION negative_prompt]]
proper nouns, specific brand names, character faces, indoor settings, night scenes, static composition, small scale, crowded spaces, artificial lighting, enclosed areas, detailed machinery, close-up shots, text overlays, logos, signatures, watermarks, copyrighted elements
[[/SECTION]]

[[SECTION inputs_markdown]]
Project: princess_of_mars_test
Asset: open_ground_hill
Role: Primary setting / Retreat location
Architecture: Open ground with hill crests forming natural elevation markers. Gray air ships swing slowly over hill ridges, banners and odd devices visible on prows.
Lighting: Daylight conditions with slow-moving aerial vessels creating atmospheric tension. Smoke from burning banners adds visual texture during battle sequences.
Scale: Large-scale environment accommodating twenty air ships in formation. Hill crests provide reference points for fleet positioning and movement patterns.
Anchors: Hill crests, air ship prows, banner displays, ground-level observation points.
[[/SECTION]]

[[SECTION continuity_notes_markdown]]
Hill crest positions remain consistent across shots as elevation markers. Air ship formation maintains twenty vessel count during battle sequences. Banner smoke texture appears during active engagement phases. Ground observation points serve as stable reference anchors for camera positioning. Ridge elevation markers provide consistent scale references throughout environment shots. Fleet movement patterns follow hill ridge contours for natural flow.
[[/SECTION]]

[[SECTION repair_notes_markdown]]
Ensure air ship count stays at twenty vessels maximum in formation shots. Verify banner smoke appears only during battle sequences, not peaceful moments. Hill crest positions must remain stable as elevation markers across all camera angles. Ground observation points need clear visibility for camera reference anchoring. Ridge elevation markers should provide consistent scale without visual clutter. Avoid proper nouns in final prompt bodies to maintain reusable shared environment-reference functionality.
[[/SECTION]]

[[/FILMCREATOR_RECORD]]
[[/FILMCREATOR_PACKET]]
````
