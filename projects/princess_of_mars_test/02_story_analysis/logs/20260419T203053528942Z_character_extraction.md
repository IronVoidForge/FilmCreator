# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-19T20:30:53.528942+00:00
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

# Chapter Summary: CHAPTER XVI - WE PLAN ESCAPE

## Story Events
1. **Arrival in Thark:** The expedition enters the ancient city after a 30-day journey from Korad. No enthusiastic welcome occurs, but interest is aroused by the captives (John and Dejah).
2. **Housing Assignment:** John Carter is assigned a large building near the plaza. He searches for Sola and her charges before locating Woola in his quarters.
3. **Confrontation with Dejah Thoris:** John enters Dejah's apartment to propose an escape plan. He confesses his love ("I am yours, body and soul") and commands her obedience until she is safe at her father's court. She accepts his service but warns against gratitude influencing her sentiments.
4. **Threat Revealed:** Sola reports that Sarkoja has been seen at Tal Hajus's quarters. The hordes plan to throw John and Dejah to wild calots in the arena during yearly games.
5. **Escape Plan Formulated:** John proposes a supreme effort to escape. Dejah draws a map of Barsoomian territory on the marble floor using a diamond, identifying waterways and cities. They decide to take a northern waterway route to avoid suspicion.
6. **Departure Attempt:** Sola rides one thoat; John and Dejah ride the other. John leaves Thark via back gates with his animals but is discovered by warriors leaving the city (plan compromised).
7. **Return and Discovery:** John returns to Dejah's quarters via courtyards and rooftops. He overhears a conversation between a chieftain and warriors who plan to capture him upon his return, disarm him, and chain him in vaults beneath the jeddak's quarters. Sarkoja is credited with saving Dejah for Tal Hajus.

## Visual Continuity Details
- **Map Drawing:** A diamond is used to draw lines on marble floor representing waterways (straight lines) and cities (circles). Helium is pointed out far northwest.
- **Architecture Traversal:** John moves through hollow courts within buildings, crossing doorways of magnificent scale designed for large beasts. He climbs winding runways to second-story windows.
- **Animal Behavior:** Thoats and zitidars move restlessly in paddocks; bulls emit sharp squeals or grunt low gutturals. Animals are fed bits of food at gates.
- **Lighting Conditions:** Scenes occur under the approaching gloom of sunset or moonlight flooding the room. The red sun disappears behind the horizon during Sola's search.
````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
task: character_extraction
version: 1

[[SECTION character_index_markdown]]
# Chapter 16 Character Index

| Name | Role | Status | Description Available |
| :--- | :--- | :--- | :--- |
| John Carter | Protagonist, Escape Planner | Physically Present | No physical details in chapter summary |
| Dejah Thoris | Lead Female, Map Drawer | Physically Present | No physical details in chapter summary |
| Sola | Companion, Thoat Rider | Physically Present | No physical details in chapter summary |
| Sarkoja | Antagonist, Jeddak's Associate | Referenced | No physical details in chapter summary |
| Tal Hajus | Jeddak of Thark | Referenced | No physical details in chapter summary |
| Woola | Animal Companion | Mentioned | No physical details in chapter summary |

[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: john_carter
canonical_character_id: john_carter
aliases: 
is_fully_identified: true
manual_description_required: true
manual_description_reason: Chapter summary lacks specific physical traits (height, build) or costume details for John Carter to support image generation.
clarification_required: false
clarification_reason: 
clarification_question: 

[[SECTION markdown]]
# John Carter - Chapter 16

**Display Name:** John Carter  
**Chapter Role:** Protagonist, Escape Planner  

**Presence Status:** Physically Present  
John enters Dejah's apartment to propose an escape plan. He later leaves Thark via back gates and returns to her quarters via courtyards and rooftops.

**Physical Description:**  
*Uncertain.* The provided chapter summary does not contain specific physical descriptions (e.g., hair color, eye shape, body build) or costume details for John Carter in this chapter. Visual continuity notes his movement through architecture but offers no render-facing noun phrases for appearance.

**Continuity Traits:**  
- Moves through hollow courts within buildings.
- Climbs winding runways to second-story windows.
- Leaves Thark via back gates.
- Returns via courtyards and rooftops.

**Render Notes:**  
Manual description required for later image generation due to lack of visual details in source text. Use standard Barsoomian male archetype if no other data exists, but flag for manual input.

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: dejah_thoris
canonical_character_id: dejah_thoris
aliases: 
is_fully_identified: true
manual_description_required: true
manual_description_reason: Chapter summary lacks specific physical traits (height, build) or costume details for Dejah Thoris to support image generation.
clarification_required: false
clarification_reason: 
clarification_question: 

[[SECTION markdown]]
# Dejah Thoris - Chapter 16

**Display Name:** Dejah Thoris  
**Chapter Role:** Lead Female, Map Drawer  

**Presence Status:** Physically Present  
She accepts John's service and commands obedience until she is safe at her father's court. She draws a map of Barsoomian territory on the marble floor using a diamond.

**Physical Description:**  
*Uncertain.* The provided chapter summary does not contain specific physical descriptions (e.g., hair color, eye shape, body build) or costume details for Dejah Thoris in this chapter. Visual continuity notes her drawing actions but offers no render-facing noun phrases for appearance.

**Continuity Traits:**  
- Draws map on marble floor using diamond.
- Accepts John's service and commands obedience.
- Warns against gratitude influencing sentiments.

**Render Notes:**  
Manual description required for later image generation due to lack of visual details in source text. Use standard Barsoomian female archetype if no other data exists, but flag for manual input.

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: sola
canonical_character_id: sola
aliases: 
is_fully_identified: true
manual_description_required: true
manual_description_reason: Chapter summary lacks specific physical traits (height, build) or costume details for Sola to support image generation.
clarification_required: false
clarification_reason: 
clarification_question: 

[[SECTION markdown]]
# Sola - Chapter 16

**Display Name:** Sola  
**Chapter Role:** Companion, Thoat Rider  

**Presence Status:** Physically Present  
Sola reports that Sarkoja has been seen at Tal Hajus's quarters. She rides one thoat with John and Dejah during the departure attempt.

**Physical Description:**  
*Uncertain.* The provided chapter summary does not contain specific physical descriptions (e.g., hair color, eye shape, body build) or costume details for Sola in this chapter. Visual continuity notes her riding actions but offers no render-facing noun phrases for appearance.

**Continuity Traits:**  
- Reports on Sarkoja's presence at Tal Hajus's quarters.
- Rides one thoat during departure attempt.
- Associated with John and Dejah.

**Render Notes:**  
Manual description required for later image generation due to lack of visual details in source text. Use standard Barsoomian female archetype if no other data exists, but flag for manual input.

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: sarkoja
canonical_character_id: sarkoja
aliases: 
is_fully_identified: true
manual_description_required: true
manual_description_reason: Chapter summary lacks specific physical traits (height, build) or costume details for Sarkoja to support image generation.
clarification_required: false
clarification_reason: 
clarification_question: 

[[SECTION markdown]]
# Sarkoja - Chapter 16

**Display Name:** Sarkoja  
**Chapter Role:** Antagonist, Jeddak's Associate  

**Presence Status:** Referenced  
Sarkoja has been seen at Tal Hajus's quarters. She is credited with saving Dejah for Tal Hajus.

**Physical Description:**  
*Uncertain.* The provided chapter summary does not contain specific physical descriptions (e.g., hair color, eye shape, body build) or costume details for Sarkoja in this chapter. Visual continuity notes her presence at a location but offers no render-facing noun phrases for appearance.

**Continuity Traits:**  
- Seen at Tal Hajus's quarters.
- Credited with saving Dejah for Tal Hajus.
- Threatens John and Dejah (implied by threat to throw them to wild calots).

**Render Notes:**  
Manual description required for later image generation due to lack of visual details in source text. Use standard Barsoomian antagonist archetype if no other data exists, but flag for manual input.

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: tal_hajus
canonical_character_id: tal_hajus
aliases: 
is_fully_identified: true
manual_description_required: true
manual_description_reason: Chapter summary lacks specific physical traits (height, build) or costume details for Tal Hajus to support image generation.
clarification_required: false
clarification_reason: 
clarification_question: 

[[SECTION markdown]]
# Tal Hajus - Chapter 16

**Display Name:** Tal Hajus  
**Chapter Role:** Jeddak of Thark  

**Presence Status:** Referenced  
Tal Hajus is the Jeddak whose quarters are referenced. Sarkoja saves Dejah for him.

**Physical Description:**  
*Uncertain.* The provided chapter summary does not contain specific physical descriptions (e.g., hair color, eye shape, body build) or costume details for Tal Hajus in this chapter. Visual continuity notes his quarters but offers no render-facing noun phrases for appearance.

**Continuity Traits:**  
- Owner of the Jeddak's quarters where Sarkoja is seen.
- Receives Dejah after she is saved by Sarkoja.
- Associated with the threat to John and Dejah (via calots in arena).

**Render Notes:**  
Manual description required for later image generation due to lack of visual details in source text. Use standard Barsoomian Jeddak archetype if no other data exists, but flag for manual input.

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: woola
canonical_character_id: woola
aliases: 
is_fully_identified: true
manual_description_required: true
manual_description_reason: Chapter summary lacks specific physical traits (height, build) or costume details for Woola to support image generation.
clarification_required: false
clarification_reason: 
clarification_question: 

[[SECTION markdown]]
# Woola - Chapter 16

**Display Name:** Woola  
**Chapter Role:** Animal Companion  

**Presence Status:** Mentioned  
John searches for Sola and her charges before locating Woola in his quarters.

**Physical Description:**  
*Uncertain.* The provided chapter summary does not contain specific physical descriptions (e.g., height, build) or costume details for Woola in this chapter. Visual continuity notes animal behavior but offers no render-facing noun phrases for appearance.

**Continuity Traits:**  
- Located in John's quarters during housing assignment search.
- Associated with Sola and her charges.
- Animal companion (likely a zitidar or similar based on context).

**Render Notes:**  
Manual description required for later image generation due to lack of visual details in source text. Use standard Barsoomian animal archetype if no other data exists, but flag for manual input.

[[/SECTION]]
[[/FILMCREATOR_RECORD]]
[[/FILMCREATOR_PACKET]]
````
