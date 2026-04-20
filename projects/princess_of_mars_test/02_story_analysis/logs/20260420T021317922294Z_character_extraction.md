# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-20T02:13:17.922294+00:00
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

Chapter id: CH005

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

**Visual Context:** The room is furnished with silks and furs for warmth. Murals depict mountains, rivers, lakes, and gardens with rare beauty but no animal forms. Food consists of a tasteless cheese-like substance; drink is milk from a large plant (8-10 quarts/day). Martian nights are cold with sudden temperature changes due to two moons (one ~5,000 miles away, one ~14,000 miles away) and thin atmosphere.
**Story Events:** Sola leaves the chamber while the Watch Dog guards alone. The narrator examines the room's murals. Upon Sola's return, she provides food and drink. After sleeping through the cold night, the narrator decides to test the Watch Dog's loyalty by attempting an escape. The narrator successfully jumps over the dog and reaches a window sill thirty feet up. However, upon being dragged back into the room by a hand, the narrator finds themselves facing a colossal, white, ape-like creature standing over them.
````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
task: character_extraction
version: 1

[[SECTION character_index_markdown]]
# Character Index - CH005

| Asset ID | Canonical ID | Aliases | Fully Identified | Manual Description Required |
|----------|--------------|---------|------------------|------------------------------|
| sola | Sola | - | true | false |
| watch_dog | Watch Dog | - | true | true |
| narrator | Narrator | - | false | true |
| colossal_ape | Colossal White Ape | - | false | true |

**Notes:**
- Sola: Limited physical description in source material
- Watch Dog: Minimal description beyond "dog"
- Narrator: First-person perspective, no physical traits provided
- Colossal Ape: Some description but insufficient for reliable image generation
[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: sola
canonical_character_id: Sola
aliases: ""
is_fully_identified: true
manual_description_required: false
manual_description_reason: "Character has sufficient physical presence and action description in source material"
clarification_required: false
clarification_reason: ""
clarification_question: ""

[[SECTION markdown]]
# Sola - CH005

**Display Name:** Sola  
**Chapter Role:** Chamber Attendant / Food Provider  
**Physical Presence:** Referenced (leaves chamber, returns with provisions)  

**Physical Description:** Insufficient detail in source material for reliable image generation. Character is identified by name and role but lacks specific physical traits, appearance, or distinguishing features mentioned in the chapter summary.

**Costume/Silhouette:** Unknown - no costume or silhouette details provided in source material.

**Continuity-Critical Traits:** 
- Provides food and drink to narrator
- Guards chamber alongside Watch Dog (when present)
- Returns after narrator's escape attempt

**Render-Facing Prompt Notes:** Character requires manual description specification for later image generation. Focus on role-based visual cues (attendant, provider) rather than invented physical details.

**Uncertainty Notes:** Physical appearance is not described in source material. Any visual representation must be based on external knowledge or manual description specification, not chapter content.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: watch_dog
canonical_character_id: Watch Dog
aliases: ""
is_fully_identified: true
manual_description_required: true
manual_description_reason: "Source material only describes this as a 'dog' with no physical details, size, breed, or appearance features"
clarification_required: false
clarification_reason: ""
clarification_question: ""

[[SECTION markdown]]
# Watch Dog - CH005

**Display Name:** Watch Dog  
**Chapter Role:** Chamber Guardian / Loyalty Test Subject  
**Physical Presence:** Referenced (guards chamber, narrator jumps over it)  

**Physical Description:** Insufficient detail in source material for reliable image generation. Chapter only identifies this as a "dog" with no breed, size, color, or physical features mentioned.

**Costume/Silhouette:** Unknown - no costume or silhouette details provided in source material.

**Continuity-Critical Traits:** 
- Guards chamber alone when Sola leaves
- Subject of narrator's escape test (narrator jumps over it)
- Appears to be loyal but narrator tests its loyalty

**Render-Facing Prompt Notes:** Character requires manual description specification for later image generation. Focus on role-based visual cues (guardian, watch dog) rather than invented physical details. Consider size relative to narrator and chamber space.

**Uncertainty Notes:** Physical appearance is not described in source material beyond being a "dog." Any visual representation must be based on external knowledge or manual description specification, not chapter content.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: narrator
canonical_character_id: Narrator
aliases: ""
is_fully_identified: false
manual_description_required: true
manual_description_reason: "First-person perspective provides no physical description of the narrator's appearance, size, or distinguishing features"
clarification_required: true
clarification_reason: "Character may exist under another name or identity not specified in chapter; insufficient identification for reliable image generation"
clarification_question: "What is the narrator's physical appearance, age, and distinguishing features? Is this character a known entity from previous chapters?"

[[SECTION markdown]]
# Narrator - CH005

**Display Name:** The Narrator  
**Chapter Role:** First-Person Observer / Escape Attempter  
**Physical Presence:** Referenced (examines murals, tests dog's loyalty, escapes to window sill)  

**Physical Description:** Insufficient detail in source material for reliable image generation. Chapter is written from first-person perspective with no physical description of the narrator provided.

**Costume/Silhouette:** Unknown - no costume or silhouette details provided in source material.

**Continuity-Critical Traits:** 
- Examines room murals
- Tests Watch Dog's loyalty through escape attempt
- Successfully jumps over dog to window sill (30 feet up)
- Dragged back into room by hand from creature

**Render-Facing Prompt Notes:** Character requires manual description specification for later image generation. Focus on role-based visual cues (observer, escapee) rather than invented physical details. Consider perspective implications for visual representation.

**Uncertainty Notes:** Physical appearance is not described in source material. First-person narrative provides no visual information about the narrator's body, face, or distinguishing features. Any visual representation must be based on external knowledge or manual description specification, not chapter content.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: colossal_ape
canonical_character_id: Colossal White Ape
aliases: ""
is_fully_identified: false
manual_description_required: true
manual_description_reason: "Source material provides limited description ('colossal, white, ape-like') but insufficient for reliable image generation"
clarification_required: true
clarification_reason: "Character may be a known entity from previous chapters or new; identification is weak and requires clarification for reliable image generation"
clarification_question: "Is this creature a known entity from previous chapters? What are its specific physical dimensions, features, and distinguishing characteristics?"

[[SECTION markdown]]
# Colossal White Ape - CH005

**Display Name:** Colossal White Ape  
**Chapter Role:** Final Confrontation Entity / Room Guardian  
**Physical Presence:** Referenced (appears at end of chapter standing over narrator)  

**Physical Description:** Limited detail in source material for reliable image generation. Chapter describes creature as "colossal, white, ape-like" but provides no specific dimensions, facial features, or distinguishing characteristics beyond basic description.

**Costume/Silhouette:** Unknown - no costume or silhouette details provided in source material.

**Continuity-Critical Traits:** 
- Appears at end of chapter after narrator's escape attempt
- Stands over narrator when dragged back into room
- Described as "colossal" and "white" with "ape-like" features

**Render-Facing Prompt Notes:** Character requires manual description specification for later image generation. Focus on role-based visual cues (colossal guardian, white ape) rather than invented physical details. Consider scale relative to narrator and chamber space.

**Uncertainty Notes:** Physical appearance is only partially described in source material ("colossal, white, ape-like"). Specific dimensions, facial features, and distinguishing characteristics are not provided. Any visual representation must be based on external knowledge or manual description specification, not chapter content.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
