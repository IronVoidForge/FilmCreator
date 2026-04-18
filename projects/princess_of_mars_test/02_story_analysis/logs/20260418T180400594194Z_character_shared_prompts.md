# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-18T18:04:00.594194+00:00
- task: character_shared_prompts

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

Asset id: narrator_observer

Task: write one reusable shared character-reference prompt draft for stable local generation.

Return exactly one Markdown packet using this outer envelope:
[[FILMCREATOR_PACKET]]
task: character_shared_prompts
version: 1

Repeat one FILMCREATOR_RECORD block for every extracted item of that type.

[[FILMCREATOR_RECORD]]
type: character_prompt
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

- prefer stable face, hair, body type, costume logic, silhouette, and recurring materials over scene-specific blocking



Character breakdown path: projects/princess_of_mars_test/02_story_analysis/character_breakdowns/narrator_observer.md

# The Narrator - Chapter VIII Observer

**Display Name:** The Narrator  
**Chapter Role:** Observer/Protagonist  
**Physical Presence:** Present (observation point from upper floor window)  

## Physical Description
*No physical description provided in source material.*

- **Face:** Unknown
- **Hair:** Unknown
- **Skin Tone:** Unknown
- **Clothing:** Unknown
- **Height:** Unknown
- **Build:** Unknown

## Costume & Silhouette
*No costume or silhouette details available.*

- **Attire:** Unknown
- **Accessories:** Unknown
- **Distinctive Features:** None documented

## Continuity-Critical Traits
- Observation point from upper floor window
- Witnesses airship fleet and combat
- Sees prisoner being dragged away
- Descends to street level after witnessing burning

## Render-Facing Prompt Notes
*Requires manual description before image generation.*

**Uncertainty Notes:**
- Physical appearance completely undocumented in chapter text
- Cannot generate reliable images without additional description
- Clarification needed for canonical identification

**Useful Descriptive Noun Phrases (for later prompts):**
- [pending clarification]
- [pending clarification]

# Aliases

[the narrator, he]



# Canonical Character ID

narrator_observer



# Fully Identified

false

# Manual Description Input Required

No



# Manual Description Reason

None




Manual character description path: projects/princess_of_mars_test/01_source/character_descriptions/narrator_observer_manual_description.md

(missing)
````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
task: character_shared_prompts
version: 1

[[FILMCREATOR_RECORD]]
type: character_prompt
asset_id: narrator_observer

[[SECTION purpose]]
Shared character-reference prompt for stable local generation of The Narrator, focusing on observation point from upper floor window. Prompts acknowledge physical appearance uncertainty while maintaining render usability through descriptive noun phrases and stable trait logic.

[[/SECTION]]

[[SECTION positive_prompt]]
person standing at upper floor window observing airship fleet and combat scene, neutral expression face, simple dark clothing silhouette, visible window frame background, atmospheric lighting from street level below, witness perspective composition, muted color palette, observation point framing, distant viewer stance, canonical narrator presence

[[/SECTION]]

[[SECTION negative_prompt]]
proper nouns, specific names, detailed physical measurements, exact height specifications, precise skin tone values, named clothing brands, scene-specific blocking, camera angles, lens types, lighting equipment, character interactions beyond observation, facial expressions beyond neutral, hair styles, body type specifics, costume details, accessories, distinctive features, scene elements unrelated to window observation

[[/SECTION]]

[[SECTION inputs_markdown]]
- Observation point from upper floor window (confirmed)
- Witnesses airship fleet and combat (confirmed)
- Sees prisoner being dragged away (confirmed)
- Descends to street level after witnessing burning (confirmed)
- Physical appearance completely undocumented in chapter text (uncertainty)
- Canonical identification requires manual description input (pending)

[[/SECTION]]

[[SECTION continuity_notes_markdown]]
Character serves as observer protagonist from upper floor window position. All prompts must maintain observation point framing and witness perspective composition. Physical traits remain undefined per source material - use placeholder descriptive language that can be filled during manual description phase. Continuity requires consistent window observation framing across all generated images.

[[/SECTION]]

[[SECTION repair_notes_markdown]]
Physical appearance documentation missing from source material requires manual intervention before reliable image generation. Prompts currently use descriptive noun phrases to maintain render usability while acknowledging uncertainty. Future iterations should incorporate canonical physical description once provided through manual character description path.

[[/SECTION]]
[[/FILMCREATOR_RECORD]]
[[/FILMCREATOR_PACKET]]
````
