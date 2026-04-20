# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-20T01:34:50.745553+00:00
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

Chapter id: CH022

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

### Story Arc
Carter witnesses Dejah Thoris promising herself to Sab Than before Than Kosis. He abandons his post to confront her in her apartments. After killing her four guards, he reveals himself as John Carter. Dejah Thoris explains she thought him dead and that Barsoomian custom binds her promise to Sab Than despite her true feelings for Carter. Realizing the promise is final by custom, Carter escapes the palace via a balcony and glass wall to avoid detection of his unauthorized presence.

### Visual Continuity
*   Apartment walls hung with tapestries hiding windows/doors.
*   Passage behind tapestries connecting chambers.
*   Antechamber containing four guards accompanying Dejah Thoris.
*   Spiral runway leading to lower floors.
*   Balcony overlooking a broad avenue of Zodanga.
*   Glass wall (20 feet high, polished glass) separating building from avenue.
````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
task: character_extraction
version: 1

[[SECTION character_index_markdown]]
# Character Index - Chapter CH022

| Character | Role | Status |
| :--- | :--- | :--- |
| Carter (John Carter) | Protagonist, Witness, Escaper | Present/Referenced |
| Dejah Thoris | Promisee, Victim of Custom | Present/Referenced |
| Sab Than | Promise Recipient | Referenced |
| Than Kosis | Promise Recipient | Referenced |
[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: carter
canonical_character_id: john_carter
aliases: carter
is_fully_identified: true
manual_description_required: true
manual_description_reason: Source material (story summary) lacks specific physical traits (hair, eyes, skin tone, height) required for dependable image generation.
clarification_required: false
clarification_reason: 
clarification_question: 

[[SECTION markdown]]
# Carter (John Carter)

**Chapter Role:** Protagonist, Witness, Escaper  
**Physical Presence:** Present/Referenced  

**Physical Description:**  
*   **Uncertain:** Specific physical traits are not described in the provided text.  
*   **Note:** Image generation requires manual description of hair color, eye color, skin tone, and height to ensure consistency with established visual continuity.  

**Costume & Silhouette:**  
*   **Uncertain:** Attire details are not specified in the summary.  
*   **Continuity Critical:** Needs definition for later render-facing prompts (e.g., Barsoomian armor style).  

**Descriptive Noun Phrases:**  
*   "Heroic figure"  
*   "Barsoomian warrior"  
*   "John Carter"  

**Uncertainty Notes:**  
*   Physical appearance details are missing from the source text and must be defined manually for reliable image generation.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: dejah_thoris
canonical_character_id: dejah_thoris
aliases: 
is_fully_identified: true
manual_description_required: true
manual_description_reason: Source material (story summary) lacks specific physical traits (hair, eyes, skin tone, height) required for dependable image generation.
clarification_required: false
clarification_reason: 
clarification_question: 

[[SECTION markdown]]
# Dejah Thoris

**Chapter Role:** Promisee, Victim of Custom  
**Physical Presence:** Present/Referenced  

**Physical Description:**  
*   **Uncertain:** Specific physical traits are not described in the provided text.  
*   **Note:** Image generation requires manual description of hair color, eye color, skin tone, and height to ensure consistency with established visual continuity.  

**Costume & Silhouette:**  
*   **Uncertain:** Attire details are not specified in the summary.  
*   **Continuity Critical:** Needs definition for later render-facing prompts (e.g., Zodanga palace attire).  

**Descriptive Noun Phrases:**  
*   "Noblewoman"  
*   "Barsoomian princess"  
*   "Dejah Thoris"  

**Uncertainty Notes:**  
*   Physical appearance details are missing from the source text and must be defined manually for reliable image generation.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: sab_than
canonical_character_id: sab_than
aliases: 
is_fully_identified: true
manual_description_required: true
manual_description_reason: Source material (story summary) lacks specific physical traits (hair, eyes, skin tone, height) required for dependable image generation.
clarification_required: false
clarification_reason: 
clarification_question: 

[[SECTION markdown]]
# Sab Than

**Chapter Role:** Promise Recipient  
**Physical Presence:** Referenced  

**Physical Description:**  
*   **Uncertain:** Specific physical traits are not described in the provided text.  
*   **Note:** Image generation requires manual description of hair color, eye color, skin tone, and height to ensure consistency with established visual continuity.  

**Costume & Silhouette:**  
*   **Uncertain:** Attire details are not specified in the summary.  
*   **Continuity Critical:** Needs definition for later render-facing prompts (e.g., Zodanga attire).  

**Descriptive Noun Phrases:**  
*   "Warrior"  
*   "Sab Than"  

**Uncertainty Notes:**  
*   Physical appearance details are missing from the source text and must be defined manually for reliable image generation.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: than_kosis
canonical_character_id: than_kosis
aliases: 
is_fully_identified: true
manual_description_required: true
manual_description_reason: Source material (story summary) lacks specific physical traits (hair, eyes, skin tone, height) required for dependable image generation.
clarification_required: false
clarification_reason: 
clarification_question: 

[[SECTION markdown]]
# Than Kosis

**Chapter Role:** Promise Recipient  
**Physical Presence:** Referenced  

**Physical Description:**  
*   **Uncertain:** Specific physical traits are not described in the provided text.  
*   **Note:** Image generation requires manual description of hair color, eye color, skin tone, and height to ensure consistency with established visual continuity.  

**Costume & Silhouette:**  
*   **Uncertain:** Attire details are not specified in the summary.  
*   **Continuity Critical:** Needs definition for later render-facing prompts (e.g., Zodanga attire).  

**Descriptive Noun Phrases:**  
*   "Warrior"  
*   "Than Kosis"  

**Uncertainty Notes:**  
*   Physical appearance details are missing from the source text and must be defined manually for reliable image generation.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]
[[/FILMCREATOR_PACKET]]
````
