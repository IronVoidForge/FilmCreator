# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-20T03:55:22.206072+00:00
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

Chapter id: CH016

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

**Arrival at Thark:** Journey complete (20 days). Arrival at city (30 days after advent on Barsoom). Entry into plaza receives formal greetings; interest aroused by captives.
**Quarters Assigned:** John Carter assigned a large building near the plaza, architecture grander than Korad. Warriors occupy buildings based on chieftain retinues or scattered sections.
**Reconciliation Attempt:** John Carter visits Dejah Thoris's room. Confesses love ("I am yours"). She accepts his service but remains guarded regarding her heart.
**Threat Revealed:** Sola reports Sarkoja plans to throw them to calots in arena games.
**Escape Plan Formulated:** Decide to escape that night. Map drawn on marble floor by Dejah Thoris showing waterways and cities. Route chosen: northern waterway to avoid suspicion.
**Execution Begins:** John Carter saddles two thoats, leaves city alone at night via southern boundary.
**Discovery of Plan:** Warriors discover plan (hear him leaving). Plan compromised.
**Return to Quarters:** John Carter hides animals in courtyard of a building, returns to Dejah Thoris's quarters via rooftops/courts.
**Climax:** Overhears chieftain ordering warriors to capture John Carter when he returns. Chieftain confirms Sarkoja has secured Dejah Thoris ("safe in the arms of Tal Hajus").
````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
task: character_extraction
version: 1

[[SECTION character_index_markdown]]
# Chapter 016 Character Index

| Character | Role in Chapter | Identification Status |
|-----------|-----------------|----------------------|
| John Carter | Protagonist; assigned quarters, visits Dejah Thoris, escapes, returns | Fully identified |
| Dejah Thoris | Love interest; receives greetings, maps route, overhears chieftain | Fully identified |
| Sola | Reporter of Sarkoja's plan | Fully identified |
| Sarkoja | Antagonist; plans to throw captives to calots, secures Dejah Thoris | Fully identified |
| Chieftain | Orders warriors to capture John Carter, confirms Sarkoja's action | Title-based (uncertain name) |
| Tal Hajus | Associated with Dejah Thoris's safety ("safe in the arms of") | Fully identified |

[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: john_carter
canonical_character_id: john_carter
aliases: 
is_fully_identified: true
manual_description_required: true
manual_description_reason: No physical description provided in chapter summary; only actions and dialogue context available.
clarification_required: false
clarification_reason: 
clarification_question: 

[[SECTION markdown]]
# John Carter - Chapter 016

**Display Name:** John Carter  
**Chapter Role:** Protagonist; assigned quarters, visits Dejah Thoris, escapes, returns  
**Physical Presence:** Physically present throughout chapter (assigned building, courtyard, rooftops)  
**Physical Description:** Not provided in source material. Actions indicate male figure capable of saddling thoats and navigating city architecture.  
**Costume/Silhouette:** No specific costume details available. Silhouette inferred from ability to move through grand buildings and navigate waterways via map.  
**Continuity-Critical Traits:** Central figure in escape plan; known by warriors and chieftain; associated with Dejah Thoris's quarters.  
**Uncertainty Notes:** Physical appearance, height, build, and specific attire are unknown. No visual markers provided for later image generation.  

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: dejah_thoris
canonical_character_id: dejah_thoris
aliases: 
is_fully_identified: true
manual_description_required: true
manual_description_reason: No physical description provided in chapter summary; only actions and dialogue context available.
clarification_required: false
clarification_reason: 
clarification_question: 

[[SECTION markdown]]
# Dejah Thoris - Chapter 016

**Display Name:** Dejah Thoris  
**Chapter Role:** Love interest; receives greetings, maps route, overhears chieftain  
**Physical Presence:** Physically present in assigned quarters; referenced in escape plan and chieftain's confirmation.  
**Physical Description:** Not provided in source material. Actions indicate female figure capable of navigating city architecture and drawing maps on marble floor.  
**Costume/Silhouette:** No specific costume details available. Silhouette inferred from ability to move through grand buildings and navigate waterways via map.  
**Continuity-Critical Traits:** Central figure in escape plan; known by John Carter, Sola, Sarkoja, and chieftain; associated with quarters near plaza.  
**Uncertainty Notes:** Physical appearance, height, build, and specific attire are unknown. No visual markers provided for later image generation.  

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: sola
canonical_character_id: sola
aliases: 
is_fully_identified: true
manual_description_required: true
manual_description_reason: No physical description provided in chapter summary; only reporting action available.
clarification_required: false
clarification_reason: 
clarification_question: 

[[SECTION markdown]]
# Sola - Chapter 016

**Display Name:** Sola  
**Chapter Role:** Reporter of Sarkoja's plan  
**Physical Presence:** Referenced in threat revelation; physical presence uncertain (may be observer or messenger).  
**Physical Description:** Not provided in source material. Actions indicate ability to report information about Sarkoja's plans.  
**Costume/Silhouette:** No specific costume details available. Silhouette inferred from role as informant within city context.  
**Continuity-Critical Traits:** Associated with threat intelligence regarding calots and arena games; linked to Sarkoja's actions.  
**Uncertainty Notes:** Physical appearance, height, build, and specific attire are unknown. Role may be observer or messenger; visual markers not provided for later image generation.  

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: sarkoja
canonical_character_id: sarkoja
aliases: 
is_fully_identified: true
manual_description_required: true
manual_description_reason: No physical description provided in chapter summary; only antagonist role available.
clarification_required: false
clarification_reason: 
clarification_question: 

[[SECTION markdown]]
# Sarkoja - Chapter 016

**Display Name:** Sarkoja  
**Chapter Role:** Antagonist; plans to throw captives to calots, secures Dejah Thoris  
**Physical Presence:** Referenced in threat revelation and chieftain's confirmation; physical presence uncertain (may be observer or active participant).  
**Physical Description:** Not provided in source material. Actions indicate ability to orchestrate threats involving calots and arena games.  
**Costume/Silhouette:** No specific costume details available. Silhouette inferred from role as antagonist within city context.  
**Continuity-Critical Traits:** Associated with threat intelligence regarding calots and arena games; linked to Dejah Thoris's safety ("safe in the arms of Tal Hajus").  
**Uncertainty Notes:** Physical appearance, height, build, and specific attire are unknown. Role may be observer or active participant; visual markers not provided for later image generation.  

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: chieftain
canonical_character_id: thak
aliases: 
is_fully_identified: false
manual_description_required: true
manual_description_reason: No physical description provided; role is defined by title only.
clarification_required: true
clarification_reason: Title used instead of specific name; need to confirm if character has a proper name (e.g., Thak).
clarification_question: Does this chieftain have a specific name (e.g., Thak) or is this a generic role?

[[SECTION markdown]]
# Chieftain - Chapter 016

**Display Name:** Chieftain  
**Chapter Role:** Orders warriors to capture John Carter, confirms Sarkoja's action  
**Physical Presence:** Referenced in orders and confirmations; physical presence uncertain (may be observer or active participant).  
**Physical Description:** Not provided in source material. Actions indicate authority over warriors and knowledge of city affairs.  
**Costume/Silhouette:** No specific costume details available. Silhouette inferred from role as leader within city context.  
**Continuity-Critical Traits:** Associated with warrior commands; linked to Sarkoja's actions regarding Dejah Thoris's safety ("safe in the arms of Tal Hajus").  
**Uncertainty Notes:** Physical appearance, height, build, and specific attire are unknown. Title-based identification requires clarification on proper name (e.g., Thak); visual markers not provided for later image generation.  

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: tal_hajus
canonical_character_id: tal_hajus
aliases: 
is_fully_identified: true
manual_description_required: true
manual_description_reason: No physical description provided; only mentioned in context of being "safe in the arms of".
clarification_required: false
clarification_reason: 
clarification_question: 

[[SECTION markdown]]
# Tal Hajus - Chapter 016

**Display Name:** Tal Hajus  
**Chapter Role:** Associated with Dejah Thoris's safety ("safe in the arms of")  
**Physical Presence:** Referenced in chieftain's confirmation; physical presence uncertain (may be observer or active participant).  
**Physical Description:** Not provided in source material. Actions indicate association with Dejah Thoris's safety context.  
**Costume/Silhouette:** No specific costume details available. Silhouette inferred from role as entity associated with Dejah Thoris's safety.  
**Continuity-Critical Traits:** Linked to Dejah Thoris's safety ("safe in the arms of Tal Hajus"); associated with Sarkoja's actions.  
**Uncertainty Notes:** Physical appearance, height, build, and specific attire are unknown. Role may be observer or active participant; visual markers not provided for later image generation.  

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
