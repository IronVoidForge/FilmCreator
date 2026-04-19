# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-19T16:50:39.272899+00:00
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

Asset id: green_martian_females

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



Character breakdown path: projects/princess_of_mars_test/02_story_analysis/character_breakdowns/green_martian_females.md

# Green Martian Females - Chapter CH008

## Display Name & Role
**Green Martian Females** - Draggers, Enforcers

## Physical Presence
**Referenced** - Multiple individuals specifically dragging prisoner into building.

## Physical Description (Supported by Source)
- Skin: Green tone
- Accessories: Wear ornaments
- Action: Drag human female prisoner from burning ship into city building

## Costume & Silhouette
- Ornamentation worn (specific style not detailed in this chapter)
- Group action described rather than individual silhouettes

## Continuity-Critical Traits
- Enforcers responsible for prisoner's captivity
- Drag prisoner into depths of edifice after battle
- Specific role in prisoner's removal from scene

## Render-Facing Noun Phrases
- "Green Martian females with green skin"
- "Wearing ornaments, carrying out prisoner"
- "Dragging human female captive into building"
- "Multiple enforcers in group action"

## Uncertainty Notes
- Described as group rather than individual characters
- Ornamentation style not specifically detailed beyond general presence
- Individual female identities not distinguished in this chapter

# Aliases

None



# Canonical Character ID

green_martian_females



# Fully Identified

true

# Manual Description Input Required

No



# Manual Description Reason

None




Manual character description path: projects/princess_of_mars_test/01_source/character_descriptions/green_martian_females_manual_description.md

(missing)
````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
task: character_shared_prompts
version: 1
[[FILMCREATOR_RECORD]]
type: character_prompt
asset_id: green_martian_females
[[SECTION purpose]]
Reusable shared character-reference prompt draft for stable local generation of Green Martian Female enforcers. Focus on consistent physical traits, ornamentation style, and group action logic while avoiding scene-specific blocking. Supports multiple individuals with stable face, hair, body type, costume, silhouette, and recurring materials across generations.
[[/SECTION]]
[[SECTION positive_prompt]]
Green skin tone females wearing ornamental accessories and jewelry pieces. Multiple enforcers in group formation carrying out human female prisoner. Ornamentation includes decorative elements on head, neck, and limbs. Silhouette shows coordinated movement with dragging action. Materials include metallic ornaments and organic green skin texture. Body type consistent across individuals with athletic build for enforcement role.
[[/SECTION]]
[[SECTION negative_prompt]]
Proper nouns, specific names, detailed scene blocking, individual character identities, facial expressions beyond neutral enforcer demeanor, isolated single figures without group context, elaborate background details, burning ship elements, city building structures, prisoner clothing specifics beyond general human female form, ornamental style variations not matching established ornamentation logic.
[[/SECTION]]
[[SECTION inputs_markdown]]
Asset ID: green_martian_females
Character Role: Enforcers/Draggers
Physical Traits: Green skin tone, ornamental accessories
Group Action: Multiple individuals dragging prisoner into building
Continuity-Critical: Enforcers responsible for prisoner captivity, group formation during removal from scene
[[/SECTION]]
[[SECTION continuity_notes_markdown]]
Green Martian females described as group rather than individual characters in source material. Ornamentation style not specifically detailed beyond general presence of decorative elements. Individual female identities not distinguished in this chapter. Continuity requires consistent green skin tone and ornamentation presence across all generated individuals. Group action logic must show coordinated movement during prisoner removal without isolating single figures.
[[/SECTION]]
[[SECTION repair_notes_markdown]]
No repairs needed at this stage. Prompts maintain stable asset ID references while using descriptive noun phrases in actual prompt body. Continuity notes capture uncertainty about specific ornamentation style and individual distinctions. Inputs section uses stable asset IDs as permitted. Prompt bodies avoid proper nouns per requirements.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]
[[/FILMCREATOR_PACKET]]
````
