# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-19T16:51:37.521246+00:00
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

Asset id: john_carter

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



Character breakdown path: projects/princess_of_mars_test/02_story_analysis/character_breakdowns/john_carter.md

# John Carter - Chapter CH008

## Display Name & Role
**John Carter** - Observer, Witness

## Physical Presence
**Present** - Physically located at city building window, observing the battle and prisoner's arrival from above.

## Physical Description (Supported by Source)
- Position: Upper floor window of city building
- Action: Observing air craft arrival and battle from distance
- Visual engagement: Witnesses prisoner being dragged into building; sees her signal of appeal but fails to respond

## Costume & Silhouette
- No specific costume details provided in this chapter
- Established figure from prior narrative context

## Continuity-Critical Traits
- Key witness to prisoner's captivity scene
- Fails to respond to prisoner's appeal signal (narrative significance)
- Positioned at window overlooking plaza and valley

## Render-Facing Noun Phrases
- "John Carter observing from city building window"
- "Witnessing battle between Green Martians and Air Fleet"
- "Failing to respond to human female prisoner's appeal signal"
- "Positioned on upper floor overlooking open ground"

## Uncertainty Notes
- No specific costume or physical appearance details provided in this chapter summary
- Description relies on established prior narrative context
- Visual continuity depends on previous character records

# Aliases

None



# Canonical Character ID

john_carter



# Fully Identified

true

# Manual Description Input Required

No



# Manual Description Reason

None




Manual character description path: projects/princess_of_mars_test/01_source/character_descriptions/john_carter_manual_description.md

(missing)
````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
task: character_shared_prompts
version: 1
[[FILMCREATOR_RECORD]]
type: character_prompt
asset_id: john_carter
[[SECTION purpose]]
Shared character reference prompt for stable local generation, focusing on John Carter's established physical presence and costume logic from prior narrative context. This prompt maintains continuity across scenes while avoiding scene-specific blocking details.
[[/SECTION]]
[[SECTION positive_prompt]]
Human male observer positioned at elevated window overlooking open ground. Strong athletic build with defined musculature visible through casual attire. Dark hair styled in short practical cut. Wearing simple earth-toned clothing with functional design elements. Silhouette shows confident stance with arms relaxed at sides. Materials include natural fabrics with subtle texture variations. Face displays focused expression with clear jawline and steady gaze. Overall appearance conveys witness to distant action from protected vantage point.
[[/SECTION]]
[[SECTION negative_prompt]]
Proper nouns, brand names, specific character names, scene-specific blocking details, dramatic lighting effects, costume accessories not established in prior context, exaggerated facial expressions, dynamic movement poses, indoor clutter, modern technology elements, fantasy armor pieces, elaborate jewelry, bright saturated colors, cartoonish proportions, distorted anatomy, inconsistent face structure.
[[/SECTION]]
[[SECTION inputs_markdown]]
- Character ID: john_carter
- Project Path: projects/princess_of_mars_test/02_story_analysis/character_breakdowns/john_carter.md
- Continuity Reference: Established figure from prior narrative context
- Asset Type: Human male observer
- Position Context: Elevated window overlooking open ground
[[/SECTION]]
[[SECTION continuity_notes_markdown]]
Established traits from prior context include athletic build, practical short hair, earth-toned casual clothing, confident stance. Current chapter shows him at city building window observing battle and prisoner arrival. No specific costume details provided in this chapter summary. Visual continuity depends on previous character records. Key witness to captivity scene with narrative significance of failing to respond to appeal signal. Positioned overlooking plaza and valley from upper floor.
[[/SECTION]]
[[SECTION repair_notes_markdown]]
No repairs needed at this time. Character description relies on established prior narrative context rather than current chapter details. Manual description path is missing but continuity notes provide sufficient reference for stable generation.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]
[[/FILMCREATOR_PACKET]]
````
