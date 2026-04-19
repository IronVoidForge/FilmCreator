# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-19T19:57:29.750207+00:00
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

Chapter id: CH003

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

# Chapter Summary: CH003 - My Advent on Mars

## Narrative Arc
### Scene 1: Awakening and Exploration
The protagonist wakes in a deep, circular basin of yellowish moss. Realizing they are on Mars without questioning sanity or wakefulness, they explore the immediate area. They discover a low, walled enclosure (4 feet high) with a solid glass roof containing hundreds of large eggs (2.5 feet diameter). Several eggs have hatched into grotesque creatures with six limbs and independent eye movement.

### Scene 2: First Contact and Threat
A group of adult Martians approaches silently on soundless moss. The leader, mounted on a ten-foot-tall beast, nearly spears the protagonist. A rifle swing causes a metallic clatter against a spear butt, alerting the protagonist. The protagonist escapes by leaping 30 feet into the air, landing safely on the opposite side of the enclosure.

### Scene 3: Negotiation and Departure
The Martian leader dismounts unarmed and approaches with peace overtures (throwing down weapons). The protagonist responds with a bow and hand-over-heart gesture. They exchange an enormous metal armlet as a token of friendship. The protagonist rides behind one of the Martians on their mount, departing toward the range of hills in the distance.

## Visual Continuity Facts
### Martian Physiology
- **Height:** Adult warriors approx. 15 feet tall; Mounts tower 10 feet at shoulder.
- **Skin:** Dark slate color, smooth and glossy (Mounts); Light yellowish-green (Young Martians), deepening to olive green in adults.
- **Eyes:** Iris blood red (Albinos), dark pupil, very white eyeball.
- **Teeth:** Snow-white china-like teeth; lower tusks curve upward to sharp points ending near human eye level.
- **Limbs:** Two legs and two arms plus intermediary pair usable as arms or legs. Ears are small cup-shaped antennae protruding not more than an inch.

### Technology & Weapons
- **Rifles:** White metal stock with wood (intensely hard growth unknown to Earth). Barrel alloy of aluminum and steel tempered to hardness exceeding familiar steel. Effective radius 300 miles theoretical, 200 miles practical with wireless finders.
- **Spears:** Forty feet long, tipped with gleaming metal.
- **Mounts:** Four legs on either side, broad flat tail held straight out behind while running. Gaping mouth splitting head from snout to neck. Feet heavily padded and nailless.

### Environment Details
- **Vegetation:** Yellowish mosslike vegetation covering practically entire surface except frozen polar areas and cultivated districts.
- **Rock:** Slight outcroppings of quartz-bearing rock glistening in sunlight.
- **Enclosure:** Low walled structure (4 feet height), roof of solid glass (4 or 5 inches thickness).
````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
task: character_extraction
version: 1

[[SECTION character_index_markdown]]
| Character Name | Role | Visual Status | Identification Status |
| :--- | :--- | :--- | :--- |
| Protagonist (Unnamed) | Main Character / Traveler | Unidentified / No Visuals | False |
| Martian Leader (Unnamed) | Antagonist / First Contact | Identified as Adult Martian | False |
[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: protagonist
canonical_character_id: protagonist
aliases: main_character, traveler
is_fully_identified: false
manual_description_required: true
manual_description_reason: No physical description provided in chapter summary.
clarification_required: true
clarification_reason: Character is unnamed and lacks specific visual details for image generation.
clarification_question: What is the protagonist's name and physical appearance?

[[SECTION markdown]]
# protagonist_chapter_003.md

## Display Name
Protagonist (Unnamed)

## Chapter Role
Main Character / Traveler

## Physical Presence
Present in Scene 1, 2, and 3. Wakes in basin, explores enclosure, exchanges armlet, departs on mount.

## Physical Description
*   **Status:** Unknown. No physical description provided in the chapter summary.
*   **Note:** Image generation requires manual description input.

## Continuity Traits
*   **Action:** Wakes in yellowish moss basin, explores enclosure, exchanges armlet, departs on mount.
*   **Gear:** None specified (except exchanging metal armlet).
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: martian_leader
canonical_character_id: martian_leader
aliases: leader, warrior
is_fully_identified: false
manual_description_required: false
manual_description_reason: Martian physiology details provided in Visual Continuity Facts.
clarification_required: true
clarification_reason: Character is unnamed.
clarification_question: What is the Martian Leader's name?

[[SECTION markdown]]
# martian_leader_chapter_003.md

## Display Name
Martian Leader (Unnamed)

## Chapter Role
Antagonist / First Contact / Negotiator

## Physical Presence
Present in Scene 1, 2, and 3. Mounted on beast in Scenes 1 & 2. Dismounted unarmed in Scene 3.

## Physical Description
*   **Species:** Adult Martian.
*   **Height:** Approx. 15 feet tall (per Visual Continuity Facts).
*   **Skin:** Dark slate color, smooth and glossy.
*   **Eyes:** Iris blood red, dark pupil, very white eyeball.
*   **Teeth:** Snow-white china-like teeth; lower tusks curve upward to sharp points ending near human eye level.
*   **Limbs:** Two legs and two arms plus intermediary pair usable as arms or legs. Ears are small cup-shaped antennae protruding not more than an inch.

## Continuity Traits
*   **Mount:** Ten-foot-tall beast (Four legs, broad flat tail held straight out behind while running, gaping mouth splitting head from snout to neck).
*   **Action:** Approaches silently on soundless moss, nearly spears protagonist, dismounts unarmed, exchanges armlet.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]
````
