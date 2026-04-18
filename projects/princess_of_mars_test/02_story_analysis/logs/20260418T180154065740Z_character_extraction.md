# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-18T18:01:54.065740+00:00
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

Chapter id: CH001

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

# Chapter Label
Chapter VIII - A Fair Captive from the Sky

# Story Summary
The procession returns home after the incubator ceremony but is ordered back immediately upon seeing a fleet of airships approaching. The narrator observes from an upper floor window as twenty gray-painted vessels sail toward the city. Green Martian warriors fire a volley from building windows, engaging the ships. The fleet returns fire and maneuvers to complete circles before retreating. One ship is disabled and drifting southeast. Warriors chase it, board with spears and grappling hooks, and loot the vessel of arms, jewels, water, and food. They empty carboys onto the dead crew and burn the ship as a funeral pyre. The narrator witnesses the burning from the roof until it drifts into the distance. Depressed by the defeat of a kindred people's forces, he descends to the street. In the plaza, he sees a prisoner being dragged into a building. He catches a glimpse of her before she enters: a slender, girlish figure with coal black hair and reddish copper skin. She looks at him with hope then dejection as she is dragged away.

# Visual Continuity Facts
- **Location:** Upper floor window (observation point), Plaza (encounter point).
- **Martian Warriors:** Green skin, erect walking, wear spears, banners, ornaments.
- **Airships:** Gray-painted, long, low, twenty total, carry strange devices on prow/stem.
- **Combat Visuals:** Figures drop at bullet explosions; banners dissolve in flame; ships swing broadside.
- **Prisoner Appearance:** Slender girlish figure, oval face, finely chiseled features, large lustrous eyes, coal black waving hair (loose coiffure), light reddish copper skin, crimson cheeks, ruby lips.
- **Attire:** Destitute of clothes, entirely naked save for highly wrought ornaments.
- **Height Comparison:** Prisoner considerably less than half as tall as green Martian warriors.
- **Movement:** Walks erect upon two legs; dragged by females into building.
- **Environment:** Deserted city buildings, open ground/plaza, valley/hills vista.
]]
````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
task: character_extraction
version: 1

[[SECTION character_index_markdown]]
# Character Index - Chapter VIII

| Display Name | Role | Physical Presence | Description Status |
|--------------|------|-------------------|--------------------|
| The Narrator | Observer/Protagonist | Present (observation point) | Manual description required |
| The Prisoner | Captive/Secondary | Referenced (encounter point) | Fully described |

**Notes:**
- Both characters lack specific names in the chapter text.
- Visual descriptions are sufficient for image generation except for the Narrator.
- Clarification questions needed for canonical identification.
[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: narrator_observer
canonical_character_id: narrator
aliases: [the narrator, he]
is_fully_identified: false
manual_description_required: true
manual_description_reason: No physical appearance details provided in chapter text (no mention of facial features, hair color, skin tone, or clothing). Cannot support dependable image generation without additional description.
clarification_required: true
clarification_reason: Character lacks specific name and stable identification beyond narrative role. May exist under another name or be too weakly identified for canonical reference.
clarification_question: What is the narrator's physical appearance (age, gender presentation, hair color, skin tone, clothing style)?

[[SECTION markdown]]
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
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: prisoner_captive
canonical_character_id: prisoner
aliases: [a prisoner, her]
is_fully_identified: false
manual_description_required: false
manual_description_reason: Detailed physical description provided in chapter text (slender girlish figure, oval face, finely chiseled features, large lustrous eyes, coal black waving hair, light reddish copper skin, crimson cheeks, ruby lips, destitute of clothes save for highly wrought ornaments). Sufficient for dependable image generation.
clarification_required: true
clarification_reason: Character lacks specific name and stable identification beyond narrative role. May exist under another name or be too weakly identified for canonical reference.
clarification_question: What is the prisoner's canonical name (if any) and background?

[[SECTION markdown]]
# The Prisoner - Chapter VIII Captive

**Display Name:** The Prisoner  
**Chapter Role:** Captive/Secondary Character  
**Physical Presence:** Referenced (encounter point in plaza)  

## Physical Description
- **Face:** Oval, finely chiseled features, large lustrous eyes
- **Hair:** Coal black, waving, loose coiffure
- **Skin Tone:** Light reddish copper
- **Cheeks:** Crimson
- **Lips:** Ruby
- **Build:** Slender, girlish figure
- **Height:** Considerably less than half as tall as green Martian warriors

## Costume & Silhouette
- **Attire:** Destitute of clothes, entirely naked save for highly wrought ornaments
- **Silhouette:** Erect walking upon two legs
- **Accessories:** Highly wrought ornaments (specific type not documented)

## Continuity-Critical Traits
- Being dragged by females into building
- Seen from upper floor window observation point
- Looks at narrator with hope then dejection
- Slender girlish figure with oval face and finely chiseled features
- Large lustrous eyes, coal black waving hair (loose coiffure)
- Light reddish copper skin, crimson cheeks, ruby lips

## Render-Facing Prompt Notes
*Physical description sufficient for image generation.*

**Uncertainty Notes:**
- Specific ornament types not documented
- Canonical name unknown
- Background and origin unclear

**Useful Descriptive Noun Phrases (for later prompts):**
- slender girlish figure with oval face and finely chiseled features
- large lustrous eyes, coal black waving hair in loose coiffure
- light reddish copper skin, crimson cheeks, ruby lips
- destitute of clothes save for highly wrought ornaments
[[/SECTION]]
[[/FILMCREATOR_RECORD]]
[[/FILMCREATOR_PACKET]]
````
