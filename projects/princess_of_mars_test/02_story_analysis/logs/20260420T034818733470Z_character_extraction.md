# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-20T03:48:18.733470+00:00
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

Chapter id: CH013

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

**Visual Continuity Facts:**
- **Setting:** Lorquas Ptomel city courtyard, plaza vicinity, great avenue leading into the plaza from the east.
- **Lighting:** Day transitioning to night; two moons of Barsoom visible in the sky; Earth appearing as a luminous green eye overhead.
- **Characters:** John Carter (wearing silks and metal armor), Dejah Thoris (red Martian attire, bare shoulders during conversation), Sola (armed), Woola (accompanying excursions).
- **Beasts:** Thoats (great beasts, dangerous but tractable when trained by kindness).
- **Props:** Pistol, gold anklet, radium powder bullets.

**Story Summary:**
1.  **Training & Community Reaction:** John Carter demonstrates his ability to ride thoats using kindness rather than violence. The community marvels at his "bewitched" beasts. Lorquas Ptomel gifts him a gold anklet for enhancing military precision and celerity.
2.  **Preparation for March:** On the seventh day post-battle with air ships, preparations resume for the march toward Thark. John Carter has been busy with Tars Tarkas's lessons in Martian warfare.
3.  **Dejah Thoris & Sola:** Before departure, Dejah Thoris and Sola walk the streets near the plaza. They are warned against venturing far due to white apes. Woola accompanies them for safety.
4.  **Romantic Exchange:** John Carter intercepts them before departure. He takes responsibility for Dejah Thoris's safekeeping. They exchange greetings (red Martian salute).
5.  **Warfare Discussion:** Dejah Thoris explains the mechanics of exploding radium powder bullets used in daylight battles versus non-exploding ones at night. She reveals the warriors' jealousy toward her status as a jeddak daughter and their hatred for their own fates.
6.  **Mutual Affection:** John Carter expresses his desire to protect her from their treatment. They discuss Earth customs (nursing enemies) vs. Martian customs (dead enemies). A moment of physical intimacy occurs (arm on shoulder), confirming mutual love before the march begins.

**Key Dialogue:** "A warrior may change his metal, but not his heart", "I loved Dejah Thoris".
````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
task: character_extraction
version: 1

[[SECTION character_index_markdown]]
# Character Index - Chapter CH013

| Asset ID | Display Name | Role | Physical Presence | Description Status |
|----------|--------------|------|-------------------|-------------------|
| john_carter | John Carter | Protagonist, warrior | Present (wearing silks and metal armor) | Partially identified |
| dejah_thoris | Dejah Thoris | Jeddak daughter, love interest | Referenced (red Martian attire, bare shoulders) | Partially identified |
| sola | Sola | Warrior companion | Referenced (armed) | Uncertain description |
| woola | Woola | Companion/excursion partner | Referenced (accompanying excursions) | Uncertain description |

**Notes:** All characters have limited physical description in this chapter context. Manual descriptions recommended for consistent image generation across reruns.
[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: john_carter
canonical_character_id: john_carter
aliases: 
is_fully_identified: false
manual_description_required: true
manual_description_reason: Insufficient stable physical description for dependable image generation; only "wearing silks and metal armor" noted in chapter summary
clarification_required: false
clarification_reason: Character is well-established in Barsoom series context but lacks detailed visual continuity data from this specific chapter
clarification_question: 

[[SECTION markdown]]
# John Carter - Chapter CH013

**Display Name:** John Carter  
**Chapter Role:** Protagonist, warrior demonstrating thoat riding and preparing for march toward Thark  
**Physical Presence:** Present (wearing silks and metal armor)  
**Physical Description:** Silks and metal armor noted; no detailed facial features, height, or build information provided in chapter summary  
**Costume/Silhouette:** Metal armor over silks; specific design details unknown  
**Continuity-Critical Traits:** Demonstrates ability to ride thoats using kindness rather than violence; recipient of gold anklet from Lorquas Ptomel for enhancing military precision and celerity  
**Uncertainty Notes:** Limited visual description in this chapter context. For consistent image generation across reruns, manual description required. Physical presence confirmed but detailed appearance not fully documented.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: dejah_thoris
canonical_character_id: dejah_thoris
aliases: 
is_fully_identified: false
manual_description_required: true
manual_description_reason: Only "red Martian attire, bare shoulders during conversation" noted; insufficient for dependable image generation without detailed visual continuity data
clarification_required: false
clarification_reason: Character is well-established in Barsoom series context but lacks detailed visual continuity data from this specific chapter
clarification_question: 

[[SECTION markdown]]
# Dejah Thoris - Chapter CH013

**Display Name:** Dejah Thoris  
**Chapter Role:** Jeddak daughter, love interest explaining radium powder bullet mechanics and warrior customs  
**Physical Presence:** Referenced (red Martian attire, bare shoulders during conversation)  
**Physical Description:** Red Martian attire with bare shoulders noted during conversation; no detailed facial features or build information provided in chapter summary  
**Costume/Silhouette:** Red Martian attire; specific design details beyond color unknown  
**Continuity-Critical Traits:** Explains exploding radium powder bullets used in daylight battles versus non-exploding ones at night; reveals warriors' jealousy toward her status as jeddak daughter and their hatred for their own fates; exchanges red Martian salute with John Carter; expresses mutual affection through physical intimacy (arm on shoulder)  
**Uncertainty Notes:** Limited visual description in this chapter context. For consistent image generation across reruns, manual description required. Physical presence confirmed but detailed appearance not fully documented.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: sola
canonical_character_id: sola
aliases: 
is_fully_identified: false
manual_description_required: true
manual_description_reason: Only "armed" noted in chapter summary; insufficient physical description for dependable image generation without detailed visual continuity data
clarification_required: true
clarification_reason: Character name provided but lacks stable identification details; may exist under alternate names or be too weakly identified for consistent rendering
clarification_question: What are Sola's physical features, height, build, and facial characteristics?

[[SECTION markdown]]
# Sola - Chapter CH013

**Display Name:** Sola  
**Chapter Role:** Warrior companion accompanying Dejah Thoris before departure  
**Physical Presence:** Referenced (armed)  
**Physical Description:** Armed status noted; no detailed physical features, height, build, or facial information provided in chapter summary  
**Costume/Silhouette:** Specific costume details unknown beyond being armed warrior  
**Continuity-Critical Traits:** Walks streets near plaza with Dejah Thoris before departure; warned against venturing far due to white apes; accompanies them for safety with Woola  
**Uncertainty Notes:** Limited visual description in this chapter context. For consistent image generation across reruns, manual description required. Physical presence confirmed but detailed appearance not fully documented. Clarification recommended for stable identification.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: woola
canonical_character_id: woola
aliases: 
is_fully_identified: false
manual_description_required: true
manual_description_reason: Only "accompanying excursions" noted in chapter summary; insufficient physical description for dependable image generation without detailed visual continuity data
clarification_required: true
clarification_reason: Character name provided but lacks stable identification details; may exist under alternate names or be too weakly identified for consistent rendering
clarification_question: What are Woola's physical features, height, build, and facial characteristics?

[[SECTION markdown]]
# Woola - Chapter CH013

**Display Name:** Woola  
**Chapter Role:** Companion/excursion partner accompanying Dejah Thoris and Sola before departure  
**Physical Presence:** Referenced (accompanying excursions)  
**Physical Description:** Accompanying excursions noted; no detailed physical features, height, build, or facial information provided in chapter summary  
**Costume/Silhouette:** Specific costume details unknown beyond accompanying role  
**Continuity-Critical Traits:** Warned against venturing far due to white apes; accompanies Dejah Thoris and Sola for safety before departure; intercepts them before departure with John Carter  
**Uncertainty Notes:** Limited visual description in this chapter context. For consistent image generation across reruns, manual description required. Physical presence confirmed but detailed appearance not fully documented. Clarification recommended for stable identification.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
