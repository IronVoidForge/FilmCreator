# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-19T05:18:14.094936+00:00
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

Asset id: disabled_ship

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



Environment breakdown path: projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/disabled_ship.md

# Disabled Ship Environment

## Environment Role
Primary recovery and looting setting for unmanned vessel.

## Architecture or Geography
Unmanned gray ship drifting south of position. Vessel boarded using spears and grappling hooks. Martians search interior removing arms, silks, jewels, food including water. Carboys emptied over dead sailors. Ship set ablaze with missile.

## Lighting and Atmosphere Cues
Ship burns as funeral pyre drifting southeast. Missile ignition creates dramatic lighting effect. Banners dissolve in flame during burning sequence. Gray color palette dominates vessel appearance.

## Scale Cues and Recurring Environmental Anchors
One ship unmanned and drifting before hitting buildings south of position. Warriors rush to intercept disabled vessel. Martians search interior removing arms, silks, jewels, food. Burning ship drifts southeast as funeral pyre. Several craft limping after fleet retreat.

## Useful Descriptive Noun Phrases
Unmanned gray ship, drifting south position, spear-grappling hook boarding, interior looting sequence, carboy-emptying sailors, missile ignition burning, funeral pyre drift, arms silks jewels food removal, dead sailor carboys, southeast drifting burn.

````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
task: environment_shared_prompts
version: 1

[[FILMCREATOR_RECORD]]
type: environment_prompt
asset_id: disabled_ship

[[SECTION purpose]]
Primary recovery and looting setting for unmanned vessel. Gray ship drifting south of position with boarding via spears and grappling hooks. Interior looting sequence where arms, silks, jewels, food including water are removed. Carboys emptied over dead sailors. Missile ignition creates burning funeral pyre drift southeast before hitting buildings south of position.
[[/SECTION]]

[[SECTION positive_prompt]]
Unmanned gray ship drifting south position, spear-grappling hook boarding, interior looting sequence, arms silks jewels food removal, carboy-emptying sailors, missile ignition burning, funeral pyre drift southeast, dead sailor carboys, banners dissolve in flame, gray color palette dominates vessel appearance, dramatic lighting effect from burning, one ship unmanned and drifting before hitting buildings south of position, warriors rush to intercept disabled vessel, burning ship drifts southeast as funeral pyre
[[/SECTION]]

[[SECTION negative_prompt]]
proper nouns, specific names, vague terms, bright colors, green blue red palette, multiple ships, stationary vessel, peaceful atmosphere, clear weather, modern technology, electronic devices, intact crew members, undamaged hull, clean interior, no fire effects, no missile ignition, no burning sequence, no funeral pyre imagery, no drifting motion, no boarding equipment
[[/SECTION]]

[[SECTION inputs_markdown]]
```markdown
## Environment Reference Data

### Asset Identification
- ID: disabled_ship
- Type: unmanned vessel environment
- Status: recovery and looting setting

### Spatial Configuration
- Location: south of position
- Motion: drifting southeast before hitting buildings
- Scale: one ship unmanned and drifting

### Visual Elements
- Primary color: gray palette dominates
- Lighting: dramatic burning effects from missile ignition
- Atmosphere: funeral pyre drift with banners dissolving in flame

### Action Anchors
- Boarding: spears and grappling hooks
- Looting sequence: arms, silks, jewels, food including water removal
- Carboy-emptying over dead sailors
- Warriors rushing to intercept disabled vessel
- Burning ship as funeral pyre drifting southeast

### Continuity Points
- Connects to fleet retreat with several craft limping after
- Precedes building impact south of position
- Links to warrior interception sequence
[[/SECTION]]

[[SECTION continuity_notes_markdown]]
This environment serves as the primary recovery and looting setting for the unmanned vessel. The gray ship drifting south of position connects to the broader fleet narrative where several craft limp after fleet retreat. The burning funeral pyre drift southeast before hitting buildings south of position creates a visual anchor that links the disabled vessel sequence to the warrior interception scene. The boarding via spears and grappling hooks establishes the action entry point, while the interior looting sequence provides environmental detail for arms, silks, jewels, food including water removal. The carboy-emptying over dead sailors adds emotional weight to the recovery setting.
[[/SECTION]]

[[SECTION repair_notes_markdown]]
Review color palette consistency - ensure gray dominates throughout without introducing bright colors that contradict the funeral pyre atmosphere. Verify missile ignition lighting effects match dramatic burning description in positive prompt. Check that drifting motion is clearly established before building impact sequence. Ensure no proper nouns appear in final prompt bodies. Confirm all environmental anchors (spear-grappling hook boarding, interior looting sequence, arms silks jewels food removal) are present and descriptive.
[[/SECTION]]

[[/FILMCREATOR_RECORD]]
[[/FILMCREATOR_PACKET]]
````
