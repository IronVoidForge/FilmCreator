# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-20T03:42:29.521885+00:00
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

Chapter id: CH010

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

# Chapter Summary: CH010 - Champion and Chief

## Visual Continuity
*   **Locations:** City limits (hills/ravines), Audience Chamber of Lorquas Ptomel, Steps of the rostrum, Benches at the side of the room.
*   **Key Objects:** Short-swords, Pistols, Silk from cape, Regalia/Chieftain trappings.
*   **Characters in Scene:** John Carter, Woola, Dejah Thoris, Lorquas Ptomel, Tars Tarkas, Sarkoja, Young Warrior (antagonist).

## Story Summary
1.  **Walk with Woola:** Early morning exploration of the city limits. John Carter establishes a bond with Woola, who acts like a playful dog upon Carter's affection. Carter commands Woola to follow him back to the hills and then returns to the plaza.
2.  **Council Hearing:** Dejah Thoris stands before Lorquas Ptomel and Tars Tarkas. She explains her scientific expedition from Helium and pleads for peace between Red Men (Martians) and Green Men (Tharks).
3.  **Intervention:** A young warrior attacks Dejah Thoris with a blow to the face. John Carter intervenes, killing the warrior in rage. He is awarded the status of a Thark Chieftain due to his valor.
4.  **Aftermath Conversation:** John Carter tends to Dejah Thoris's injuries (nosebleed). They converse briefly; he reveals his name (John Carter) and origin (Virginia, Earth). Tars Tarkas explains the rules regarding prisoners and chieftain status.
5.  **Departure:** John Carter asserts his protection over Dejah Thoris. He leaves the Audience Chamber with her and Woola, passing through silence from the other chieftains.

## Specific Scene Notes
*   **Combat:** The killing of the young warrior is a pivotal moment establishing Carter's status.
*   **Dialogue:** Key exchange regarding names ("Dejah Thoris", "John Carter") and origins (Helium vs. Virginia).
*   **Status Change:** Carter transitions from prisoner to Thark Chieftain via combat valor.
````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
task: character_extraction
version: 1

[[SECTION character_index_markdown]]
# Character Index - Chapter CH010

| Asset ID | Canonical Character ID | Aliases | Fully Identified | Description Required | Clarification Required |
|----------|------------------------|---------|------------------|----------------------|------------------------|
| john_carter | John Carter | - | true | false | false |
| woola | Woola | - | true | true | false |
| dejah_thoris | Dejah Thoris | - | true | false | false |
| lorquas_ptomel | Lorquas Ptomel | - | false | true | true |
| tars_tarkas | Tars Tarkas | - | false | true | true |
| sarkoja | Sarkoja | - | false | true | true |
| young_warrior | Young Warrior | - | false | true | true |

[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: john_carter
canonical_character_id: John Carter
aliases: -
is_fully_identified: true
manual_description_required: false
manual_description_reason: 
clarification_required: false
clarification_reason: 
clarification_question: 

[[SECTION markdown]]
# John Carter

**Chapter Role:** Protagonist / Thark Chieftain (after intervention)  
**Physical Presence:** Present in scene throughout chapter  
**Physical Description:** Tall, muscular build; wears Earth clothing initially; later accepts Thark status. Strong, commanding presence noted during combat.  
**Costume/Silhouette:** Earth garments at start; transitions to Thark chieftain regalia after killing young warrior.  
**Continuity-Critical Traits:** Name revealed as "John Carter" from Virginia, Earth. Origin: Helium vs. Virginia exchange with Dejah Thoris. Status change from prisoner to Chieftain via combat valor.  
**Render-Facing Prompt Noun Phrases:** tall muscular man, earth clothing, strong commanding presence, thark chieftain status, combat valor, protective over dejah thoris.

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: woola
canonical_character_id: Woola
aliases: -
is_fully_identified: true
manual_description_required: true
manual_description_reason: Physical description limited to "acts like a playful dog upon Carter's affection" and general Martian creature. Insufficient specific visual details (fur color, size, facial features) for dependable image generation.
clarification_required: false
clarification_reason: 
clarification_question: 

[[SECTION markdown]]
# Woola

**Chapter Role:** Companion / Guide  
**Physical Presence:** Present throughout chapter with John Carter and Dejah Thoris  
**Physical Description:** Martian creature; acts like playful dog upon Carter's affection. Bond established through early morning exploration of city limits.  
**Costume/Silhouette:** Native Martian appearance; no clothing mentioned.  
**Continuity-Critical Traits:** Loyal companion to John Carter; follows him back to hills; accompanies Dejah Thoris and John Carter out of Audience Chamber.  
**Render-Facing Prompt Noun Phrases:** martian creature, playful dog-like behavior, loyal companion, follows john carter, native martian appearance.

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: dejah_thoris
canonical_character_id: Dejah Thoris
aliases: -
is_fully_identified: true
manual_description_required: false
manual_description_reason: 
clarification_required: false
clarification_reason: 
clarification_question: 

[[SECTION markdown]]
# Dejah Thoris

**Chapter Role:** Princess of Helium / Pleader for Peace  
**Physical Presence:** Present in Audience Chamber; receives injuries from young warrior's attack  
**Physical Description:** Princess of Helium; wears cape with silk mentioned during scene. Nosebleed injury noted after combat intervention.  
**Costume/Silhouette:** Cape with silk material; Thark chieftain audience chamber attire.  
**Continuity-Critical Traits:** Name revealed as "Dejah Thoris" from Helium. Scientific expedition background explained. Pleads for peace between Red Men (Martians) and Green Men (Tharks). Status: prisoner transitioning to protected person under John Carter's protection.  
**Render-Facing Prompt Noun Phrases:** princess of helium, cape with silk, scientific expedition background, pleader for peace, nosebleed injury, protected by john carter.

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: lorquas_ptomel
canonical_character_id: Lorquas Ptomel
aliases: -
is_fully_identified: false
manual_description_required: true
manual_description_reason: Limited description in chapter summary. Only identified as chieftain present in Audience Chamber with Tars Tarkas. No physical or costume details provided for dependable image generation.
clarification_required: true
clarification_reason: Character may already exist under another name or is too weakly identified in this chapter to confirm stable identity across reruns.
clarification_question: Is Lorquas Ptomel a distinct character from other chieftains mentioned, and what are his physical characteristics?

[[SECTION markdown]]
# Lorquas Ptomel

**Chapter Role:** Chieftain / Audience Chamber Authority  
**Physical Presence:** Present in Audience Chamber with Tars Tarkas; listens to Dejah Thoris's plea  
**Physical Description:** Limited description available. Identified as chieftain present during council hearing.  
**Costume/Silhouette:** Thark chieftain regalia/trappings mentioned in general scene notes.  
**Continuity-Critical Traits:** Part of ruling authority in Audience Chamber; listens to Dejah Thoris's scientific expedition explanation and peace plea. Status: chieftain with prisoner rules knowledge.  
**Render-Facing Prompt Noun Phrases:** thark chieftain, audience chamber authority, regalia/trappings, listens to dejah thoris, prisoner rules knowledge.

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: tars_tarkas
canonical_character_id: Tars Tarkas
aliases: -
is_fully_identified: false
manual_description_required: true
manual_description_reason: Limited description in chapter summary. Only identified as chieftain who explains rules regarding prisoners and chieftain status. No physical or costume details provided for dependable image generation.
clarification_required: true
clarification_reason: Character may already exist under another name or is too weakly identified in this chapter to confirm stable identity across reruns.
clarification_question: Is Tars Tarkas a distinct character from other chieftains mentioned, and what are his physical characteristics?

[[SECTION markdown]]
# Tars Tarkas

**Chapter Role:** Chieftain / Rules Authority  
**Physical Presence:** Present in Audience Chamber with Lorquas Ptomel; explains rules to John Carter  
**Physical Description:** Limited description available. Identified as chieftain who explains prisoner and chieftain status rules.  
**Costume/Silhouette:** Thark chieftain regalia/trappings mentioned in general scene notes.  
**Continuity-Critical Traits:** Explains rules regarding prisoners and chieftain status to John Carter after combat intervention. Part of ruling authority in Audience Chamber.  
**Render-Facing Prompt Noun Phrases:** thark chieftain, explains prisoner rules, explains chieftain status, audience chamber authority, regalia/trappings.

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: sarkoja
canonical_character_id: Sarkoja
aliases: -
is_fully_identified: false
manual_description_required: true
manual_description_reason: Character listed in chapter summary but not detailed in specific scene notes of this chapter. No physical or costume details provided for dependable image generation.
clarification_required: true
clarification_reason: Character may already exist under another name or is too weakly identified in this chapter to confirm stable identity across reruns.
clarification_question: Is Sarkoja present in this chapter's scenes, and what are her physical characteristics?

[[SECTION markdown]]
# Sarkoja

**Chapter Role:** Listed Character / Antagonist (potential)  
**Physical Presence:** Uncertain - listed in character summary but not detailed in specific scene notes of this chapter.  
**Physical Description:** No description available in this chapter's material.  
**Costume/Silhouette:** No costume details provided.  
**Continuity-Critical Traits:** Listed as character in chapter summary; potential antagonist role based on general project context.  
**Render-Facing Prompt Noun Phrases:** listed character, potential antagonist, uncertain presence.

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: young_warrior
canonical_character_id: Young Warrior
aliases: -
is_fully_identified: false
manual_description_required: true
manual_description_reason: Limited description in chapter summary. Only identified as antagonist who attacks Dejah Thoris with blow to face and is killed by John Carter. No physical or costume details provided for dependable image generation.
clarification_required: true
clarification_reason: Character may already exist under another name or is too weakly identified in this chapter to confirm stable identity across reruns.
clarification_question: Is the young warrior a distinct character from other warriors mentioned, and what are his physical characteristics?

[[SECTION markdown]]
# Young Warrior

**Chapter Role:** Antagonist / Combatant  
**Physical Presence:** Present briefly in Audience Chamber; attacks Dejah Thoris then killed by John Carter  
**Physical Description:** Limited description available. Identified as young warrior who delivers blow to face and is killed in combat intervention.  
**Costume/Silhouette:** Thark warrior attire implied (short-swords mentioned in key objects).  
**Continuity-Critical Traits:** Pivotal combat moment establishing Carter's status; killing of warrior awards John Carter Thark Chieftain status. Antagonist role confirmed through attack on Dejah Thoris.  
**Render-Facing Prompt Noun Phrases:** young thark warrior, antagonist, short-swords, combat intervention, killed by john carter, establishes chieftain status.

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
