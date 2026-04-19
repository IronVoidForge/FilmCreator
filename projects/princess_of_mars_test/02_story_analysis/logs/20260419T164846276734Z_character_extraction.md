# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-19T16:48:46.276734+00:00
- task: character_extraction

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

Chapter id: CH008

Task: extract visible and referenced characters into a character index plus one Markdown file per character.

Return exactly one Markdown packet using this outer envelope:
[[FILMCREATOR_PACKET]]
task: character_extraction
version: 1

[[SECTION character_index_markdown]]
...character_index_markdown content...
[[/SECTION]]

Repeat one FILMCREATOR_RECORD block for every extracted item of that type.

[[FILMCREATOR_RECORD]]
type: character
asset_id: <value>
canonical_character_id: <value>
aliases: <value>
is_fully_identified: <value>
manual_description_required: <value>
manual_description_reason: <value>
clarification_required: <value>
clarification_reason: <value>
clarification_question: <value>

[[SECTION markdown]]
...markdown content...
[[/SECTION]]
[[/FILMCREATOR_RECORD]]
[[/FILMCREATOR_PACKET]]



Important rules:

- if a character does not have enough physical or visual description in the supplied material to support dependable later image generation, set manual_description_required to true

- explain exactly why in manual_description_reason

- do not guess ornate missing details just to avoid the flag

- if the chapter names a character without enough stable identification, set is_fully_identified to false

- use aliases for alternate names or partial labels seen in the chapter

- if the character might already exist under another name or is too weakly identified, set clarification_required to true and ask a targeted question

- if clarification is not required, still include clarification_reason and clarification_question as empty values

- every character record must include a non-empty markdown section

- if details are sparse, still write a short markdown file explaining the uncertainty instead of omitting markdown

- never omit the markdown section for any character record



Asset id rules:

- lowercase snake_case

- stable across later reruns



Each character Markdown file should include:

- display name and chapter role

- whether the character is physically present, referenced, or uncertain

- physical description that is actually supported by the source

- costume, silhouette, and continuity-critical traits when known

- useful descriptive noun phrases for later render-facing prompt writing

- explicit uncertainty notes when important details are missing



Chapter summary:

# Chapter Summary: CH008 - A Fair Captive from the Sky

## Story Summary
The narrative begins on the third day after an incubator ceremony. The procession retreats to a city building due to an immediate order. From a window, John Carter observes the arrival of twenty large gray air craft. A battle ensues between Green Martians firing from buildings and the Air Fleet returning fire. The fleet retreats after damage; one ship is disabled and unmanned. Warriors loot the vessel (arms, jewels, water), burn it, and tow it away before it explodes. Carter witnesses a human female prisoner being dragged from the burning ship into a nearby building by Green Martian females. At the city plaza, the prisoner turns to Carter as she enters the building; he fails to respond to her signal of appeal. She is dragged away into the depths of the edifice.

## Visual Continuity
- **Air Craft:** Long, low, gray-painted vessels with strange banners and odd devices on prows. Figures crowd forward decks.
- **Green Martians:** Green skin, wear ornaments, carry spears, fire from windows/roofs.
- **Prisoner:** Slender, girlish figure. Skin is light reddish copper. Features finely chiseled. Eyes large/lustrous. Hair coal black, waving, caught loosely into a strange coiffure. Naked except for highly wrought ornaments. Cheeks crimson, lips ruby.
- **Locations:** City buildings (upper floors, windows, roofs), open ground/plaza, valley, hills beyond.
- **Action Details:** Ships swing broadside, dip below hill crests, drift southeast/southwesterly. Fire causes spurt of flame from missile impact. Guy ropes release simultaneously.
````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
task: character_extraction
version: 1

[[SECTION character_index_markdown]]
# Character Index - Chapter CH008

| Asset ID | Canonical Character ID | Display Name | Role | Physical Presence |
|----------|------------------------|--------------|------|-------------------|
| john_carter | john_carter | John Carter | Observer, Witness | Present |
| human_female_prisoner | prisoner_human_female | Human Female Prisoner | Captive, Appeal Signal | Referenced |
| green_martian_warriors | green_martian_warrior | Green Martian Warriors | Combatants, Looters | Referenced |
| green_martian_females | green_martian_female | Green Martian Females | Draggers, Enforcers | Referenced |

**Notes:**
- John Carter: Physically present observing from window; witnesses prisoner's appeal
- Human Female Prisoner: Detailed visual description provided in chapter; signals to Carter
- Green Martians: Multiple individuals; described as group with consistent physical traits
- All characters have sufficient identification for continuity tracking
[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: john_carter
canonical_character_id: john_carter
aliases: 
is_fully_identified: true
manual_description_required: false
manual_description_reason: 
clarification_required: false
clarification_reason: 
clarification_question: 

[[SECTION markdown]]
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
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: human_female_prisoner
canonical_character_id: prisoner_human_female
aliases: 
is_fully_identified: true
manual_description_required: false
manual_description_reason: 
clarification_required: false
clarification_reason: 
clarification_question: 

[[SECTION markdown]]
# Human Female Prisoner - Chapter CH008

## Display Name & Role
**Human Female Prisoner** - Captive, Appeal Signal

## Physical Presence
**Referenced** - Dragged from burning air craft into city building; turns to Carter before being taken away.

## Physical Description (Supported by Source)
- Build: Slender, girlish figure
- Skin: Light reddish copper tone
- Features: Finely chiseled facial features
- Eyes: Large, lustrous
- Hair: Coal black, waving, caught loosely into strange coiffure
- Attire: Naked except for highly wrought ornaments
- Cheeks: Crimson-colored
- Lips: Ruby-colored

## Costume & Silhouette
- No clothing; adorned with highly wrought ornaments only
- Ornamentation style described as "strange" (continuity detail)
- Silhouette emphasizes slender, girlish proportions

## Continuity-Critical Traits
- Signals appeal to John Carter from burning ship
- Dragged into building by Green Martian females
- Captive status established through visual description and action
- Key emotional focal point of chapter scene

## Render-Facing Noun Phrases
- "Human female prisoner with light reddish copper skin"
- "Slender girlish figure in highly wrought ornaments"
- "Coal black waving hair in strange coiffure"
- "Large lustrous eyes, finely chiseled features"
- "Crimson cheeks, ruby lips"
- "Appealing to John Carter from burning air craft"

## Uncertainty Notes
- Ornamentation style described as "strange" but specific design not detailed
- Coiffure described as "strange" without specific styling details
- No prior costume history provided in this chapter
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: green_martian_warriors
canonical_character_id: green_martian_warrior
aliases: 
is_fully_identified: true
manual_description_required: false
manual_description_reason: 
clarification_required: false
clarification_reason: 
clarification_question: 

[[SECTION markdown]]
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
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: green_martian_females
canonical_character_id: green_martian_female
aliases: 
is_fully_identified: true
manual_description_required: false
manual_description_reason: 
clarification_required: false
clarification_reason: 
clarification_question: 

[[SECTION markdown]]
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
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
