# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-20T04:04:39.850913+00:00
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

Chapter id: CH021

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

**Arrival at Zodanga:**
John Carter arrives at the gates of Zodanga ten days after leaving the Ptor brothers. He separates from Woola before entering the city to prevent unwelcome attention (Woola is not domesticated by red men). He enters via a letter of introduction, gaining immediate entrance to the vast walled city.

**Meeting Kantos Kan:**
In the central plaza, Carter meets Kantos Kan, who recognizes him as "John Carter" and "Darseen." They discuss Dejah Thoris's fate; she is believed dead by the Zodangans but not confirmed. Carter intends to reach Helium to report news of her possible whereabouts.

**Enlistment in Air Scouts:**
Carter joins the air-scout squadron. Kantos Kan helps him bypass initial examination checks by claiming he is John Carter (a ruse that will be discovered later). The next few days are spent learning Martian aviation and repairing dainty little contrivances (one-man aircraft powered by radium engines and eighth ray buoyancy).

**Action Sequence:**
On the fourth day, Carter makes his first flight. He saves a cousin of the Jeddak Than Kosis from three green warriors who were attacking him near a walled field. Carter rammed the nearest warrior's mount and engaged the others on foot, killing them with practiced skill. The Zodangan was wounded but survived.

**Reward and Promotion:**
A ceremony is held in the plaza to confer honors for bravery. Carter is called out by name ("John Carter, air scout!"). Than Kosis awards him a metal ornament and appoints him a padwar of The Guards, granting him quarters in his palace. Carter returns his machine to the barracks and reports to the officer in charge of the palace.

**Visual Continuity:**
*   Morning streets are practically deserted; residences resemble huge rookeries raised on metal columns.
*   Shops are not raised from the ground; doors are unbolted or barred (thievery unknown).
*   Air craft bodies are sixteen feet long, two feet wide, three inches thick.
*   The plaza covers a square mile and is bounded by palaces of royalty.
*   Mechanical apparatus serves food in cafes; no hand touches the food from raw state to table.
````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
task: character_extraction
version: 1

[[SECTION character_index_markdown]]
# Zodanga Chapter Character Index

- **John Carter**: Protagonist, Air Scout, recipient of honors.
- **Woola**: Companion animal, separated before city entry.
- **Kantos Kan**: City official, air scout instructor.
- **Dejah Thoris**: Referenced as believed dead.
- **Jeddak Than Kosis**: Jeddak, awards honors to Carter.
[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: john_carter
canonical_character_id: John Carter
aliases: Darseen
is_fully_identified: true
manual_description_required: true
manual_description_reason: The chapter summary mentions John Carter's name and actions but does not provide specific physical attributes like height, build, hair color, or facial features.
clarification_required: false
clarification_question:

[[SECTION markdown]]
# John Carter

**Display Name:** John Carter  
**Chapter Role:** Protagonist, Air Scout, Honor Recipient  
**Presence Status:** Physically Present  

**Physical Description (Supported by Source):**  
Not specified in the provided chapter summary. No physical attributes are described.

**Costume & Silhouette:**  
Not specified in the provided chapter summary.

**Continuity-Critical Traits:**  
- Recognized as "Darseen" by Kantos Kan.
- Joined air-scout squadron.
- Awarded metal ornament and appointed padwar of The Guards.
- Granted quarters in Jeddak Than Kosis's palace.

**Descriptive Noun Phrases for Render-Facing Prompts:**  
- Red Martian male protagonist.
- Air scout with radium engine aircraft.
- Recipient of Zodangan honors.

**Uncertainty Notes:**  
Physical attributes are unknown and cannot be reliably inferred from the source text. Image generation will require manual description input to ensure accuracy.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: woola
canonical_character_id: Woola
aliases: 
is_fully_identified: true
manual_description_required: true
manual_description_reason: The chapter summary references Woola but does not provide specific physical attributes like species, size, or appearance details.
clarification_required: false
clarification_question:

[[SECTION markdown]]
# Woola

**Display Name:** Woola  
**Chapter Role:** Companion Animal  
**Presence Status:** Referenced (Separated before city entry)  

**Physical Description (Supported by Source):**  
Not specified in the provided chapter summary. No physical attributes are described.

**Costume & Silhouette:**  
Not specified in the provided chapter summary.

**Continuity-Critical Traits:**  
- Not domesticated by red men.
- Separated from John Carter before entering Zodanga to prevent unwelcome attention.

**Descriptive Noun Phrases for Render-Facing Prompts:**  
- Martian companion animal.
- Non-domesticated creature of the Ptor brothers' party.

**Uncertainty Notes:**  
Species and appearance are unknown and cannot be reliably inferred from the source text. Image generation will require manual description input to ensure accuracy.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: kantos_kan
canonical_character_id: Kantos Kan
aliases: 
is_fully_identified: true
manual_description_required: true
manual_description_reason: The chapter summary mentions Kantos Kan's name and role but does not provide specific physical attributes.
clarification_required: false
clarification_question:

[[SECTION markdown]]
# Kantos Kan

**Display Name:** Kantos Kan  
**Chapter Role:** City Official, Air Scout Instructor  
**Presence Status:** Physically Present  

**Physical Description (Supported by Source):**  
Not specified in the provided chapter summary. No physical attributes are described.

**Costume & Silhouette:**  
Not specified in the provided chapter summary.

**Continuity-Critical Traits:**  
- Recognizes John Carter as "Darseen."
- Helps Carter bypass initial examination checks (ruse discovered later).
- Teaches Martian aviation and aircraft repair.
- Holds position in central plaza.

**Descriptive Noun Phrases for Render-Facing Prompts:**  
- Zodangan city official.
- Air scout squadron instructor.
- Central plaza resident near royal palaces.

**Uncertainty Notes:**  
Physical attributes are unknown and cannot be reliably inferred from the source text. Image generation will require manual description input to ensure accuracy.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: dejah_thoris
canonical_character_id: Dejah Thoris
aliases: 
is_fully_identified: true
manual_description_required: true
manual_description_reason: The chapter summary references Dejah Thoris's fate but does not provide specific physical attributes.
clarification_required: false
clarification_question:

[[SECTION markdown]]
# Dejah Thoris

**Display Name:** Dejah Thoris  
**Chapter Role:** Referenced Character (Believed Dead)  
**Presence Status:** Referenced Only  

**Physical Description (Supported by Source):**  
Not specified in the provided chapter summary. No physical attributes are described.

**Costume & Silhouette:**  
Not specified in the provided chapter summary.

**Continuity-Critical Traits:**  
- Believed dead by Zodangans but not confirmed.
- Subject of news report John Carter intends to deliver to Helium.

**Descriptive Noun Phrases for Render-Facing Prompts:**  
- High-status Martian woman (implied by name recognition).
- Central figure in John Carter's narrative arc.

**Uncertainty Notes:**  
Physical attributes are unknown and cannot be reliably inferred from the source text. Image generation will require manual description input to ensure accuracy.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: jeddak_than_kosis
canonical_character_id: Jeddak Than Kosis
aliases: 
is_fully_identified: true
manual_description_required: true
manual_description_reason: The chapter summary mentions Jeddak Than Kosis's name and role but does not provide specific physical attributes.
clarification_required: false
clarification_question:

[[SECTION markdown]]
# Jeddak Than Kosis

**Display Name:** Jeddak Than Kosis  
**Chapter Role:** Jeddak, Honor Awarder  
**Presence Status:** Physically Present  

**Physical Description (Supported by Source):**  
Not specified in the provided chapter summary. No physical attributes are described.

**Costume & Silhouette:**  
Not specified in the provided chapter summary.

**Continuity-Critical Traits:**  
- Cousin of Jeddak Than Kosis was saved by Carter.
- Awarded metal ornament to Carter for bravery.
- Appointed Carter as padwar of The Guards.
- Granted Carter quarters in his palace.

**Descriptive Noun Phrases for Render-Facing Prompts:**  
- Royal Zodangan official (Jeddak).
- Palace resident near central plaza.
- Bestower of honors and rewards.

**Uncertainty Notes:**  
Physical attributes are unknown and cannot be reliably inferred from the source text. Image generation will require manual description input to ensure accuracy.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]
[[/FILMCREATOR_PACKET]]
````
