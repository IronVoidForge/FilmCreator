# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-19T16:50:50.932282+00:00
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

Asset id: green_martian_warriors

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



Character breakdown path: projects/princess_of_mars_test/02_story_analysis/character_breakdowns/green_martian_warriors.md

# Green Martian Warriors - Chapter CH008

## Display Name & Role
**Green Martian Warriors** - Combatants, Looters

## Physical Presence
**Referenced** - Multiple individuals firing from buildings and looting disabled air craft.

## Physical Description (Supported by Source)
- Skin: Green tone
- Accessories: Wear ornaments
- Weapons: Carry spears
- Positioning: Fire from windows and roofs of city buildings

## Costume & Silhouette
- Ornamentation worn (specific style not detailed in this chapter)
- Group action described rather than individual silhouettes

## Continuity-Critical Traits
- Combatants in battle between Green Martians and Air Fleet
- Loot disabled air craft for arms, jewels, water
- Fire from buildings causes spurt of flame on missile impact
- Release guy ropes simultaneously during retreat

## Render-Facing Noun Phrases
- "Green Martian warriors with green skin"
- "Wearing ornaments, carrying spears"
- "Firing from city building windows and roofs"
- "Looting disabled air craft vessel"
- "Multiple combatants in group action"

## Uncertainty Notes
- Described as group rather than individual characters
- Ornamentation style not specifically detailed beyond general presence
- Individual warrior identities not distinguished in this chapter

# Aliases

None



# Canonical Character ID

green_martian_warriors



# Fully Identified

true

# Manual Description Input Required

No



# Manual Description Reason

None




Manual character description path: projects/princess_of_mars_test/01_source/character_descriptions/green_martian_warriors_manual_description.md

(missing)
````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
task: character_shared_prompts
version: 1

[[FILMCREATOR_RECORD]]
type: character_prompt
asset_id: green_martian_warriors

[[SECTION purpose]]
Create reusable shared character-reference prompt for stable local generation focusing on Green Martian Warriors combatants with consistent visual traits across multiple individuals. Prioritize skin tone, ornamentation style, weapon presence, and positioning logic over scene-specific blocking to maintain continuity during group action sequences.
[[/SECTION]]

[[SECTION positive_prompt]]
Green skin tone humanoid figures wearing decorative ornaments and carrying long spears positioned firing from elevated building windows and rooftops. Multiple combatants in coordinated group formation with ornamental accessories visible on upper body. Standing posture with weapon held ready for combat engagement. Elevated position relative to ground level with architectural background elements. Consistent green dermal coloring across all individuals with ornamentation patterns maintained uniformly.
[[/SECTION]]

[[SECTION negative_prompt]]
Proper nouns, specific brand names, individual character identities, detailed facial features beyond skin tone, hair styling variations, scene-specific blocking details, ground-level positioning, isolated single combatant, inconsistent skin coloring, missing weapon presence, architectural background elements removed, ornamental accessories absent, varied ornamentation styles, detailed costume patterns beyond general ornamentation.
[[/SECTION]]

[[SECTION inputs_markdown]]
- Skin: Green tone consistent across all individuals
- Accessories: Ornamentation worn on upper body (style not specified)
- Weapons: Long spears carried and held ready
- Positioning: Elevated building windows and rooftops
- Group Action: Multiple combatants in coordinated formation
- Continuity Traits: Combat between Green Martians and Air Fleet, looting disabled air craft vessel, firing from buildings causes flame spurt on missile impact, releasing guy ropes during retreat
[[/SECTION]]

[[SECTION continuity_notes_markdown]]
Green Martian Warriors function as group combatants rather than individual characters. Visual consistency maintained through green skin tone and ornamentation presence across multiple individuals. Weapon presence (spears) and elevated positioning from buildings are key continuity markers. Group action sequences prioritize formation over individual silhouettes. Ornamentation style remains general without specific pattern details to allow flexibility in generation while maintaining character identity.
[[/SECTION]]

[[SECTION repair_notes_markdown]]
Monitor for inconsistent skin tone variations across generated individuals. Ensure ornamentation presence is maintained even when detailed patterns are unspecified. Verify weapon presence and elevated positioning remain consistent during group action sequences. Check that proper nouns and specific brand references are absent from all prompt variations. Maintain general ornamentation style without over-specifying pattern details to preserve generation flexibility.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]
[[/FILMCREATOR_PACKET]]
````
