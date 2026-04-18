# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-18T19:23:45.571935+00:00
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

Asset id: lorquas_ptomel

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



Character breakdown path: projects/princess_of_mars_test/02_story_analysis/character_breakdowns/lorquas_ptomel.md

# Lorquas Ptomel (Chapter VIII)

## Display Name
Lorquas Ptomel

## Chapter Role
City Guardian/Leader

## Presence Status
Referenced (Remains at deserted city)

## Physical Description
*None provided in chapter summary.*

## Costume & Silhouette
*None provided in chapter summary.*

## Continuity-Critical Traits
*None provided in chapter summary.*

## Descriptive Noun Phrases
*Guardian of the city, leader.*

## Uncertainty Notes
No physical description available in chapter summary. Manual description required for image generation.

# Aliases

None



# Canonical Character ID

lorquas_ptomel



# Fully Identified

true

# Manual Description Input Required

No



# Manual Description Reason

None




Manual character description path: projects/princess_of_mars_test/01_source/character_descriptions/lorquas_ptomel_manual_description.md

(missing)
````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
task: character_shared_prompts
version: 1

[[FILMCREATOR_RECORD]]
type: character_prompt
asset_id: lorquas_ptomel

[[SECTION purpose]]
Reusable shared character-reference prompt for stable local generation of Lorquas Ptomel, City Guardian/Leader archetype. Focuses on role-based visual descriptors rather than scene-specific blocking. Prioritizes consistent face, hair, body type, costume logic, silhouette, and recurring materials across generations. Acknowledges uncertainty in physical description from chapter summary.
[[/SECTION]]

[[SECTION positive_prompt]]
Guardian of the city, leader figure with authoritative posture, protective stance, composed expression, dignified bearing, urban environment context, structured clothing, formal attire, metallic accents, stone textures, architectural elements, commanding presence, steady gaze, organized silhouette, ceremonial garments, reinforced materials, civic duty symbolism, established authority markers, mature features, confident demeanor, cityscape background, structural forms, protective gear, leadership insignia, functional costume design
[[/SECTION]]

[[SECTION negative_prompt]]
proper nouns, brand names, specific character names, scene-specific blocking, dynamic action poses, emotional extremes, casual clothing, informal attire, soft materials, organic textures, natural landscapes, rural settings, intimate spaces, personal items, decorative elements, ornate details, fantasy creatures, mythical beings, supernatural effects, magical glows, dramatic lighting, high contrast shadows, blurred faces, distorted features, inconsistent anatomy, mismatched proportions, low resolution, artifacts, noise, compression errors
[[/SECTION]]

[[SECTION inputs_markdown]]
Character ID: lorquas_ptomel
Display Name: Lorquas Ptomel
Chapter Role: City Guardian/Leader
Presence Status: Referenced (Remains at deserted city)
Descriptive Noun Phrases: Guardian of the city, leader
Manual Description Path: projects/princess_of_mars_test/01_source/character_descriptions/lorquas_ptomel_manual_description.md (missing)
Canonical Character ID: lorquas_ptomel
Fully Identified: true
Uncertainty Notes: No physical description available in chapter summary. Manual description required for image generation.
[[/SECTION]]

[[SECTION continuity_notes_markdown]]
Known Traits: Role as City Guardian/Leader, presence at deserted city, authoritative posture implied by role
Unknown Traits: Physical appearance, facial features, hair style, body type, costume details, material preferences, specific silhouette elements
Continuity Priority: Maintain consistent face, hair, body type, costume logic, silhouette, and recurring materials across all generations. Avoid scene-specific blocking that conflicts with established character identity.
Manual Description Status: Required but not available in chapter summary. External manual description path exists but is missing content.
[[/SECTION]]

[[SECTION repair_notes_markdown]]
No repairs needed at this time. Character lacks physical description from source material, which is noted as uncertainty rather than error. Future generations should incorporate any manual description once available while maintaining established role-based visual descriptors.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]
[[/FILMCREATOR_PACKET]]
````
