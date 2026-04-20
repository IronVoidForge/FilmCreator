# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-20T02:27:22.676219+00:00
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

Chapter id: CH012

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

Story: Carter is summoned by Lorquas Ptomel and accused of plotting an escape with Dejah Thoris ("red girl"). He faces a trial on return to Thark. Tars Tarkas offers him quarters in the building adjoining Sola's, explaining Thark retinue customs and distributing loot (weapons, silks, food). Carter selects a room on the third floor near Dejah Thoris's apartment to establish communication.

Visual: Audience chamber interior -> Plaza exterior -> Winding corridor -> Upper floors overlooking moss-covered court with fountains/statuary -> Back rooms receiving loads of weapons/silks/furs/cooking utensils.
````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
task: character_extraction
version: 1
[[SECTION character_index_markdown]]
# Character Index - Chapter CH012

| Asset ID | Canonical ID | Aliases | Identification | Description Status |
| :--- | :--- | :--- | :--- | :--- |
| carter | carter | | Fully Identified | Manual Description Required |
| lorquas_ptomel | lorquas_ptomel | | Fully Identified | Manual Description Required |
| dejah_thoris | dejah_thoris | "red girl" | Fully Identified | Manual Description Required |
| tars_tarkas | tars_tarkas | | Fully Identified | Manual Description Required |
| sola | sola | | Fully Identified | Manual Description Required |
[[/SECTION]]
[[FILMCREATOR_RECORD]]
type: character
asset_id: carter
canonical_character_id: carter
aliases: 
is_fully_identified: true
manual_description_required: true
manual_description_reason: Supplied material lacks physical or visual description details.
clarification_required: false
clarification_reason: 
clarification_question: 
[[SECTION markdown]]
# Carter

**Display Name:** Carter  
**Chapter Role:** Protagonist / Accused  
**Physical Presence:** Referenced / Visible (summoned, faces trial, selects room)  
**Description Status:** Uncertain in this chapter  

**Notes:**  
No physical or visual description details are provided in the supplied material for Carter. Appearance traits such as hair color, eye color, build, or facial features are not mentioned in this text. Any image generation must rely on external knowledge or manual description input.

**Continuity Traits:**  
- Accused of plotting an escape with Dejah Thoris ("red girl").
- Faces a trial upon return to Thark.
- Selects a room on the third floor near Dejah Thoris's apartment.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]
[[FILMCREATOR_RECORD]]
type: character
asset_id: lorquas_ptomel
canonical_character_id: lorquas_ptomel
aliases: 
is_fully_identified: true
manual_description_required: true
manual_description_reason: Supplied material lacks physical or visual description details.
clarification_required: false
clarification_reason: 
clarification_question: 
[[SECTION markdown]]
# Lorquas Ptomel

**Display Name:** Lorquas Ptomel  
**Chapter Role:** Summoner / Authority Figure  
**Physical Presence:** Referenced (summoned Carter)  
**Description Status:** Uncertain in this chapter  

**Notes:**  
No physical or visual description details are provided in the supplied material for Lorquas Ptomel. Appearance traits such as age, gender, clothing style, or distinguishing features are not mentioned in this text.

**Continuity Traits:**  
- Summons Carter to the audience chamber.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]
[[FILMCREATOR_RECORD]]
type: character
asset_id: dejah_thoris
canonical_character_id: dejah_thoris
aliases: "red girl"
is_fully_identified: true
manual_description_required: true
manual_description_reason: Supplied material lacks physical or visual description details.
clarification_required: false
clarification_reason: 
clarification_question: 
[[SECTION markdown]]
# Dejah Thoris

**Display Name:** Dejah Thoris  
**Chapter Role:** Accused Accomplice (Referenced)  
**Physical Presence:** Referenced (apartment mentioned, name used)  
**Description Status:** Uncertain in this chapter  

**Notes:**  
No full physical or visual description details are provided in the supplied material for Dejah Thoris. While referred to as "red girl," specific appearance traits like hair texture, eye color, or height are not detailed in this text.

**Continuity Traits:**  
- Accused of plotting an escape with Carter.
- Apartment located on upper floors overlooking moss-covered court.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]
[[FILMCREATOR_RECORD]]
type: character
asset_id: tars_tarkas
canonical_character_id: tars_tarkas
aliases: 
is_fully_identified: true
manual_description_required: true
manual_description_reason: Supplied material lacks physical or visual description details.
clarification_required: false
clarification_reason: 
clarification_question: 
[[SECTION markdown]]
# Tars Tarkas

**Display Name:** Tars Tarkas  
**Chapter Role:** Retinue Leader / Host  
**Physical Presence:** Referenced (offers quarters)  
**Description Status:** Uncertain in this chapter  

**Notes:**  
No physical or visual description details are provided in the supplied material for Tars Tarkas. Appearance traits such as species, clothing, or distinguishing features are not mentioned in this text.

**Continuity Traits:**  
- Offers Carter quarters in the building adjoining Sola's.
- Explains Thark retinue customs and distributes loot (weapons, silks, food).
[[/SECTION]]
[[/FILMCREATOR_RECORD]]
[[FILMCREATOR_RECORD]]
type: character
asset_id: sola
canonical_character_id: sola
aliases: 
is_fully_identified: true
manual_description_required: true
manual_description_reason: Supplied material lacks physical or visual description details.
clarification_required: false
clarification_reason: 
clarification_question: 
[[SECTION markdown]]
# Sola

**Display Name:** Sola  
**Chapter Role:** Building Owner (Referenced)  
**Physical Presence:** Referenced (possessive noun "Sola's")  
**Description Status:** Uncertain in this chapter  

**Notes:**  
No physical or visual description details are provided in the supplied material for Sola. The text only references the building as "adjoining Sola's," implying ownership but offering no appearance details.

**Continuity Traits:**  
- Owns the building adjoining where Carter is offered quarters.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]
[[/FILMCREATOR_PACKET]]
````
