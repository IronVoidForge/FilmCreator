# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-20T00:59:59.642130+00:00
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

Chapter id: CH009

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

Visual Continuity Facts:
- Warrior presents full accouterments and arms at the building doorway.
- Women remodel armor trappings to fit narrator's proportions in sleeping quarters.
- Narrator practices weapons on the plaza with young Martians under Sola's instruction.
- Nighttime conversations occur in sleeping quarters among females, Woola, and the narrator.
- Narrator observes guards treating the prisoner harshly during transport to audience chamber.

Broad Story Summary:
- Narrator learns Martian language rapidly due to familiarity with earthly concepts.
- Sola expresses concern regarding narrator's interaction with the prisoner, hinting at jealousy or protective feelings.
- Women explain Martian society: women produce all goods/weapons and train in defense; men handle strategy and laws.
- Discussions reveal plans for the prisoner's death/exhibition at Thark games before Tal Hajus.
- Narrator realizes Sola hates cruelty and decides to ask her for help escaping later.
````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
task: character_extraction
version: 1

[[SECTION character_index_markdown]]
| Character Name | Role in Chapter | Identification Status |
| :--- | :--- | :--- |
| Narrator (Warrior) | Protagonist, Weapons Practitioner | Partially Identified (Text uses "Warrior"/"Narrator") |
| Sola | Female Martian, Instructor | Fully Identified |
| Woola | Companion, Sleeping Quarters Resident | Fully Identified |
| Prisoner | Captive, Subject of Discussion | Not Identified |
| Tal Hajus | Future Event Reference / Leader | Fully Identified |
[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: narrator_warrior
canonical_character_id: narrator_warrior
aliases: warrior
is_fully_identified: false
manual_description_required: true
manual_description_reason: Summary mentions 'full accouterments' and 'armor trappings' but lacks specific physical descriptors like height, hair color, or facial features.
clarification_required: false
clarification_question: 
[[SECTION markdown]]
# Narrator (Warrior)

**Chapter Role:** Protagonist, Weapons Practitioner, Armor Wearer
**Physical Presence:** Present in building doorway, sleeping quarters, plaza
**Description:** The text identifies this character as the "Narrator" and "Warrior". They are described wearing full accouterments and armor trappings.
**Uncertainty:** The provided material does not specify a canonical name (e.g., John Carter) or detailed physical traits (height, build, hair). Only the presence of weapons and armor is confirmed.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: sola
canonical_character_id: sola
aliases: 
is_fully_identified: true
manual_description_required: true
manual_description_reason: Summary identifies her as a female Martian but provides no physical description.
clarification_required: false
clarification_question: 
[[SECTION markdown]]
# Sola

**Chapter Role:** Female Martian, Weapons Instructor, Friend/Relative
**Physical Presence:** Present in sleeping quarters, plaza
**Description:** A female Martian who instructs the narrator on weapons practice and expresses concern regarding the narrator's interaction with the prisoner.
**Uncertainty:** No specific physical appearance (hair, eyes, height) is detailed in the provided text.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id:_woola
canonical_character_id: woola
aliases: 
is_fully_identified: true
manual_description_required: true
manual_description_reason: Summary mentions name but no physical description.
clarification_required: false
clarification_question: 
[[SECTION markdown]]
# Woola

**Chapter Role:** Companion, Sleeping Quarters Resident
**Physical Presence:** Present in sleeping quarters
**Description:** Mentioned alongside females and the narrator during nighttime conversations in the sleeping quarters.
**Uncertainty:** No specific physical appearance is detailed in the provided text.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: prisoner
canonical_character_id: prisoner
aliases: 
is_fully_identified: false
manual_description_required: true
manual_description_reason: Referred to only as 'the prisoner' with no physical details.
clarification_required: true
clarification_question: What is the specific name or identity of the prisoner mentioned in the sleeping quarters?
[[SECTION markdown]]
# Prisoner

**Chapter Role:** Captive, Subject of Discussion
**Physical Presence:** Referenced in doorway, sleeping quarters, transport
**Description:** The character is referred to as "the prisoner" or "captive". They are treated harshly by guards during transport.
**Uncertainty:** No name or physical description is provided in the supplied material. Identification status is weak due to lack of proper noun.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: tal_hajus
canonical_character_id: tal_hajus
aliases: 
is_fully_identified: true
manual_description_required: true
manual_description_reason: Mentioned only as a name in the context of future events.
clarification_required: false
clarification_question: 
[[SECTION markdown]]
# Tal Hajus

**Chapter Role:** Future Event Reference / Leader
**Physical Presence:** Referenced in conversation regarding games/audience chamber
**Description:** A name mentioned in the context of plans for the prisoner's death/exhibition at Thark games.
**Uncertainty:** No physical description is provided in the supplied text; only the name is visible.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
