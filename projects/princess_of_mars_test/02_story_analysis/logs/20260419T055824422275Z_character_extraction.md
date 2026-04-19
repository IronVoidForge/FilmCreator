# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-19T05:58:24.422275+00:00
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

**Story Beat 1: The Retreat Order**
After the incubator ceremony, the procession returns to the city. Orders are given for a hasty retreat into buildings due to the approach of enemy airships. The Martians melt into doorways and vanish within three minutes.

**Visual Continuity:**
- **Setting:** Deserted city in a valley with hills beyond.
- **Entities:** Green Martian warriors, chariots, mastodons, mounted warriors.
- **Atmosphere:** Sudden scurrying to cover; deserted buildings.

**Story Beat 2: The Airship Battle and Salvage**
From a window, the narrator observes twenty gray airships approaching. Green Martians fire a volley from building windows. The ships return fire but suffer damage. Several limping craft retreat; one remains unmanned and drifting. Martians board the last ship, loot it (arms, food, water), and burn it as a funeral pyre before towing it away.

**Visual Continuity:**
- **Vessels:** Huge craft, long, low, gray-painted.
- **Action:** Banners dissolved in flame; upper works mowed through by projectiles.
- **Loot:** Arms, ammunition, silks, furs, jewels, strangely carved stone vessels, casks of water.
- **Aftermath:** Great warship soaring majestically into the air as a floating funeral pyre.

**Story Beat 3: The Captive's Arrival**
The group returns to the plaza. The narrator sees an Earthling woman being dragged into a building by Martian females. She is naked, has copper skin and black hair. She signals for help; the narrator fails to respond due to ignorance of customs. She is taken away into the building.

**Visual Continuity:**
- **Figure:** Slender, girlish figure similar to earthly women.
- **Features:** Oval face, finely chiseled features, large lustrous eyes, coal black waving hair caught loosely.
- **Skin:** Light reddish copper color with crimson glow of cheeks and ruby lips.
- **Attire:** Destitute of clothes; highly wrought ornaments only.
````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
task: character_extraction
version: 1

[[SECTION character_index_markdown]]
# Character Index - Chapter CH008

## Earthling Woman (Captive)
- **Role:** Captive brought to the plaza, referenced by narrator
- **Status:** Physically present in Story Beat 3
- **Description:** Slender girlish figure with oval face, copper skin, black hair, highly wrought ornaments only. Light reddish copper color with crimson glow of cheeks and ruby lips.

## Green Martian Warriors
- **Role:** Procession participants, defenders against airships
- **Status:** Physically present throughout chapter
- **Description:** Group entity without individual physical descriptions; green warriors in procession returning to city after incubator ceremony.

## Martian Females
- **Role:** Dragging captives into buildings
- **Status:** Physically present in Story Beat 3
- **Description:** Group entity without individual physical descriptions; female Martians involved in captive handling and ship salvage operations.

[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: earthling_woman
canonical_character_id: earthling_captive
aliases: 
is_fully_identified: true
manual_description_required: false
manual_description_reason: 
clarification_required: false
clarification_reason: 
clarification_question: 

[[SECTION markdown]]
# Earthling Woman (Captive)

## Display Name
Earthling Woman / Captive

## Chapter Role
Primary captive figure brought to the plaza after airship battle; central reference point for narrator's observations of Martian customs and treatment of prisoners.

## Physical Presence
**Present:** Yes - Physically present in Story Beat 3, dragged into building by Martian females while being observed from window.

## Physical Description (Supported by Source)
- **Figure:** Slender, girlish figure similar to earthly women
- **Face:** Oval face with finely chiseled features
- **Eyes:** Large lustrous eyes
- **Hair:** Coal black waving hair caught loosely
- **Skin:** Light reddish copper color with crimson glow of cheeks and ruby lips
- **Attire:** Destitute of clothes; highly wrought ornaments only

## Costume & Silhouette
- **Silhouette:** Slender, feminine form with loose hair arrangement
- **Ornaments:** Highly wrought decorative pieces (specific types not detailed)
- **State:** Naked/clothless except for ornamental pieces

## Continuity-Critical Traits
- Captive status established through being dragged by Martian females
- Physical description provides stable reference for character identification
- Copper skin color distinguishes from typical human appearance
- Ornamentation suggests cultural significance despite destitution

## Render-Facing Prompt Elements
"Slender girlish figure with oval face, copper skin, coal black waving hair caught loosely, large lustrous eyes, light reddish copper complexion with crimson glow of cheeks and ruby lips, destitute of clothes except highly wrought ornaments"

## Uncertainty Notes
- Specific ornament types not detailed in source material
- Exact cultural context of ornaments unclear
- Emotional state beyond physical description not specified

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: green_martian_warriors
canonical_character_id: green_martian_warrior_group
aliases: 
is_fully_identified: true
manual_description_required: true
manual_description_reason: Group entity without individual physical descriptions; requires manual description for specific individuals to support dependable image generation. Source material references warriors as collective group rather than providing individualized physical details.
clarification_required: false
clarification_reason: 
clarification_question: 

[[SECTION markdown]]
# Green Martian Warriors

## Display Name
Green Martian Warriors / Warrior Group

## Chapter Role
Procession participants returning to city after incubator ceremony; defenders firing volley from building windows against approaching airships; involved in ship salvage and burning operations.

## Physical Presence
**Present:** Yes - Physically present throughout chapter as group entity; no individual warriors specifically detailed beyond collective description.

## Physical Description (Supported by Source)
- **Group Identity:** Green Martian warriors referenced collectively
- **Individual Details:** Not provided in source material
- **Visual Continuity:** Procession returning to city, firing from windows, boarding drifting ship

## Costume & Silhouette
- **Silhouette:** Warrior group form (individual silhouettes not detailed)
- **Color Association:** Green (implied by "Green Martian" designation)
- **Equipment:** Chariots and mastodons mentioned as associated transport

## Continuity-Critical Traits
- Group entity without individualized physical descriptions
- Associated with chariots, mastodons, mounted warriors
- Involved in combat against airships and ship salvage operations
- Green color designation distinguishes from other entities

## Render-Facing Prompt Elements
"Green Martian warrior group; collective form without individualized physical details; associated with chariots and mastodons; green color designation"

## Uncertainty Notes
- **CRITICAL:** Individual physical descriptions not provided in source material
- No specific facial features, body types, or individual costume details available
- Manual description required for specific individuals to support dependable image generation
- Group references only; no individual warrior profiles established

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: martian_females
canonical_character_id: martian_female_group
aliases: 
is_fully_identified: true
manual_description_required: true
manual_description_reason: Group entity without individual physical descriptions; requires manual description for specific individuals to support dependable image generation. Source material references females as collective group rather than providing individualized physical details.
clarification_required: false
clarification_reason: 
clarification_question: 

[[SECTION markdown]]
# Martian Females

## Display Name
Martian Females / Female Warrior Group

## Chapter Role
Draggers of captives into buildings; involved in ship salvage and burning operations; participants in procession returning to city.

## Physical Presence
**Present:** Yes - Physically present in Story Beat 3 dragging Earthling woman into building; also present during ship salvage operations.

## Physical Description (Supported by Source)
- **Group Identity:** Martian females referenced collectively
- **Individual Details:** Not provided in source material
- **Visual Continuity:** Dragging captives, boarding drifting ship, burning it as funeral pyre

## Costume & Silhouette
- **Silhouette:** Female warrior group form (individual silhouettes not detailed)
- **Color Association:** Green (implied by "Martian" designation)
- **Equipment:** Associated with chariots, mastodons, mounted warriors

## Continuity-Critical Traits
- Group entity without individualized physical descriptions
- Involved in captive handling operations
- Participate in ship salvage and burning procedures
- Green color designation distinguishes from other entities

## Render-Facing Prompt Elements
"Martian female group; collective form without individualized physical details; green color designation; involved in captive handling and ship salvage operations"

## Uncertainty Notes
- **CRITICAL:** Individual physical descriptions not provided in source material
- No specific facial features, body types, or individual costume details available
- Manual description required for specific individuals to support dependable image generation
- Group references only; no individual female warrior profiles established

[[/SECTION]]
[[/FILMCREATOR_RECORD]]
[[/FILMCREATOR_PACKET]]
````
