# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-19T20:37:02.320857+00:00
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

Chapter id: CH018

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

**Story Summary:**
1.  **Awakening:** Narrator regains consciousness in a Warhoon camp room with sleeping silks/furs; ancient female and scarred jed (Dak Kova) present.
2.  **Departure:** Dak Kova plans to use narrator for "great games"; narrator strapped to wild thoat, escorted by warriors to main column.
3.  **Audience:** Reach Warhoon camp near dark; narrator taken before Jeddak Bar Comas.
4.  **Conflict & Battle:** Dak Kova insults Bar Comas and presents narrator for battle; Bar Comas kills Dak Kova in brutal hand-to-hand fight (tusks, slashing).
5.  **Ascension:** Bar Comas dies; Dak Kova becomes new Jeddak of Warhoon after three days (foot on neck of dead ruler).
6.  **Expedition Cancelled:** Injuries delay march; raid on Thark community postponed until after great games; warriors turn back to Warhoon.
7.  **Imprisonment:** Narrator cast into dungeon in Warhoon city, heavily chained to floor/walls; utter darkness, creeping things.
8.  **Escape Attempt:** Narrator kills jailer with chain to obtain keys; regains reason.
9.  **Discovery:** Six pairs of gleaming eyes approach and retreat from the darkness.

**Visual Continuity Facts:**
-   **Characters:** Green skin, tusks (single broken tusk on Dak Kova), ornaments (human skulls/hands strapped to breast).
-   **Animals:** Wild thoats (unmanageable, prone to bolting).
-   **Environment:** Small room with sleeping silks/furs; mossy floor; inky blackness of dungeon; creeping/crawling things; cold sinuous bodies.
-   **Lighting:** Dim torch light for food delivery; total darkness in dungeon; gleaming fiery eyes visible only in dark.
````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
task: character_extraction
version: 1

[[SECTION character_index_markdown]]
# Character Index: CH018

| Character | Role | Visual ID Status | Description Source |
| :--- | :--- | :--- | :--- |
| **Narrator** | Protagonist / Prisoner | Incomplete | Actions only; no physical traits. |
| **Dak Kova** | Former Jeddak / Warrior | Complete | Green skin, tusks, skull ornaments. |
| **Bar Comas** | Jeddak of Warhoon / Ruler | Incomplete | Name only; no physical traits. |

[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: narrator
canonical_character_id: narrator
aliases: 
is_fully_identified: false
manual_description_required: true
manual_description_reason: The chapter summary describes the narrator's actions and situation but provides no physical description (gender, race, age, features).
clarification_required: true
clarification_question: What is the physical appearance of the narrator?

[[SECTION markdown]]
# Narrator

## Role
Protagonist / Prisoner

## Status
Referenced (Cast into dungeon, kills jailer)

## Physical Description
Unknown

> **Note:** No physical description is provided in the chapter summary.

## Costume / Silhouette
Uncertain

## Continuity Traits
None specified.

## Descriptive Noun Phrases
"Narrator", "Prisoner", "Warhoon captive".

## Uncertainty Notes
The narrator's gender, race, and physical features are not described in the text provided. Image generation requires manual description to ensure accurate representation.

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: dak_kova
canonical_character_id: dak_kova
aliases: 
is_fully_identified: true
manual_description_required: false
manual_description_reason: 
clarification_required: false
clarification_question: 

[[SECTION markdown]]
# Dak Kova

## Role
Former Jeddak / Warrior

## Status
Present (In room, killed by Bar Comas)

## Physical Description
Green skin, single broken tusk, ornaments (human skulls/hands strapped to breast).

> **Note:** Specific visual traits are confirmed in the Visual Continuity Facts.

## Costume / Silhouette
Warhoon warrior attire with skull/hand ornaments.

## Continuity Traits
Broken tusk, green skin, skull ornaments.

## Descriptive Noun Phrases
"Dak Kova", "Scarred Jed", "Warhoon Jeddak".

## Uncertainty Notes
None specific to visual traits in the text.

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: bar_comas
canonical_character_id: bar_comas
aliases: 
is_fully_identified: false
manual_description_required: true
manual_description_reason: The chapter summary identifies Bar Comas as Jeddak but does not describe his physical appearance or ornaments.
clarification_required: true
clarification_question: Does Bar Comas share the same Warhoon physical traits (green skin, tusks) as Dak Kova, or is he distinct?

[[SECTION markdown]]
# Bar Comas

## Role
Jeddak of Warhoon / Ruler

## Status
Present (Receives narrator, kills Dak Kova, dies)

## Physical Description
Unknown

> **Note:** No physical description is provided for Bar Comas in the chapter summary.

## Costume / Silhouette
Uncertain (Likely Warhoon Jeddak attire).

## Continuity Traits
None specified.

## Descriptive Noun Phrases
"Bar Comas", "Jeddak Bar Comas", "Warhoon Ruler".

## Uncertainty Notes
The chapter summary identifies Bar Comas as Jeddak but does not describe his physical appearance or ornaments. Image generation requires clarification on whether he shares Dak Kova's traits or has a distinct appearance.

[[/SECTION]]
[[/FILMCREATOR_RECORD]]
[[/FILMCREATOR_PACKET]]
````
