# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-20T00:01:55.694101+00:00
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

**Broad Story Summary:**
On the third day after the incubator ceremony, the narrator and Sola return home but are ordered back immediately upon seeing enemy airships approaching. The green Martians retreat into buildings. From a window, the narrator observes the arrival of twenty gray-painted enemy vessels. A volley is exchanged; the enemy fleet returns fire but is eventually driven off by accurate Martian aim. One ship crashes near the city and is looted. Warriors find a small prisoner inside, drag her to ground, and loot the vessel before setting it ablaze with a missile. The narrator descends to the street and enters the plaza. There, he sees the captured woman being dragged into a building. She turns and makes eye contact with the narrator, signaling for help, but is taken away.

**Visual Continuity Facts:**
- **Characters:** Narrator (human-like), Sola (Martian companion), Woola (hound), Green Martians (green warriors), Prisoner (slender, girlish, Earth-like features, coal black hair, light reddish copper skin).
- **Locations:** Incubator building (upper floor window), City plaza, Open valley, Building roofs.
- **Objects:** Gray-painted airships (long, low, banners, odd devices), Chariots, Mastodons, Grappling hooks, Spears, Casks of water, Solid foods/liquids, Missile (faint spurt of flame).
- **Actions:** Melting into mist (Martians), Swinging over crest (ships), Firing volley, Dragging prisoner, Setting fire, Releasing guy ropes.
````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
task: character_extraction
version: 1

[[SECTION character_index_markdown]]
# CH008 Character Index

| Asset ID | Role | Description Status |
| :--- | :--- | :--- |
| narrator | Protagonist / Observer | Human-like, present on upper floor and street. |
| sola | Martian Companion | Present with narrator, identity details sparse. |
| woola | Hound | Present with narrator, breed/size unspecified. |
| green_martians | Warriors | Group retreats into buildings, skin color noted. |
| prisoner | Captured Woman | Slender, girlish, coal black hair, light reddish copper skin. |

*Note: All characters require manual description refinement for dependable image generation.*
[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: narrator
canonical_character_id: narrator
aliases: ""
is_fully_identified: true
manual_description_required: true
manual_description_reason: "The term 'human-like' is insufficient for dependable image generation. Specific facial features, age, skin tone, and attire are missing."
clarification_required: false
clarification_reason: ""
clarification_question: ""

[[SECTION markdown]]
# Narrator (CH008)

**Role:** Protagonist / Observer  
**Presence:** Physically present on upper floor window; descends to street/plaza.  
**Description Status:** Requires refinement. Currently identified only as "human-like."  
**Uncertainty:** Specific physical traits (eyes, hair style, age) are not provided in the source material. This limits reliable render generation without manual description input.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: sola
canonical_character_id: sola
aliases: ""
is_fully_identified: true
manual_description_required: true
manual_description_reason: "Identified only as 'Martian companion.' Specific physical traits (skin color, height, features) are missing compared to the Green Martians group."
clarification_required: false
clarification_reason: ""
clarification_question: ""

[[SECTION markdown]]
# Sola (CH008)

**Role:** Martian Companion  
**Presence:** Physically present with narrator.  
**Description Status:** Requires refinement. Currently identified only as 'Martian companion.'  
**Uncertainty:** It is unclear if Sola shares the physical traits of the Green Martians or has distinct features. Specific details are missing for reliable render generation.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: woola
canonical_character_id: woola
aliases: ""
is_fully_identified: true
manual_description_required: true
manual_description_reason: "Identified only as 'hound.' Specific breed, size, fur color, and physical features are missing."
clarification_required: false
clarification_reason: ""
clarification_question: ""

[[SECTION markdown]]
# Woola (CH008)

**Role:** Hound  
**Presence:** Physically present with narrator.  
**Description Status:** Requires refinement. Currently identified only as 'hound.'  
**Uncertainty:** Specific breed, size, and fur details are not provided in the source material. This limits reliable render generation without manual description input.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: green_martians
canonical_character_id: green_martians
aliases: ""
is_fully_identified: true
manual_description_required: true
manual_description_reason: "Group identified as 'Green Martians.' Individual armor, weapon details, and specific facial features are missing for dependable render generation."
clarification_required: false
clarification_reason: ""
clarification_question: ""

[[SECTION markdown]]
# Green Martians (CH008)

**Role:** Warriors  
**Presence:** Physically present; retreat into buildings.  
**Description Status:** Requires refinement. Currently identified as 'Green Martians.'  
**Uncertainty:** While skin color is noted, individual armor styles, weapon types, and specific facial features are not detailed in the source material.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: prisoner
canonical_character_id: prisoner
aliases: ""
is_fully_identified: true
manual_description_required: true
manual_description_reason: "Description includes 'slender, girlish, Earth-like features, coal black hair, light reddish copper skin.' However, specific facial features (eyes, nose), clothing details, and exact age are missing for dependable render generation."
clarification_required: false
clarification_reason: ""
clarification_question: ""

[[SECTION markdown]]
# Prisoner (CH008)

**Role:** Captured Woman  
**Presence:** Physically present; dragged to ground/building.  
**Description Status:** Requires refinement. Currently identified as 'slender, girlish, Earth-like features, coal black hair, light reddish copper skin.'  
**Uncertainty:** Specific facial features (eyes, nose), clothing details, and exact age are not provided in the source material. This limits reliable render generation without manual description input.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
