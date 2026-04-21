# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-21T07:23:44.291478+00:00
- task: character_extraction

## System Prompt
````text
You are FilmCreator's chapter analysis engine.
Return only FilmCreator packets with the requested sections and records.
Do not wrap the packet in code fences unless explicitly requested.
Do not produce JSON-only responses.
If a packet asks for markdown sections, emit the section name on its own line and wrap the body in [[SECTION ...]] ... [[/SECTION]].
Keep the response deterministic and grounded in the supplied chapter text.
````

## User Prompt
````text
Project slug: princess_of_mars_test

Chapter id: CH012

Task: extract visible and referenced characters into a character index plus one Markdown file per character.

Packet contract:
- task: character_extraction
- version: 1
- first line: [[FILMCREATOR_PACKET]]
- last line: [[/FILMCREATOR_PACKET]]
- required sections: character_index_markdown
- record type character: fields=asset_id, canonical_character_id, aliases, is_fully_identified, manual_description_required, manual_description_reason, clarification_required, clarification_reason, clarification_question sections=markdown



Output format:

[[FILMCREATOR_PACKET]]

task: character_extraction

version: 1

character_index_markdown:

[[SECTION character_index_markdown]]

...index markdown...

[[/SECTION]]



[[FILMCREATOR_RECORD]]

type: character

asset_id: protagonist

canonical_character_id: CH002 Protagonist

aliases: Narrator, Conscious Entity

is_fully_identified: false

manual_description_required: true

manual_description_reason: Sparse physical detail.

clarification_required: true

clarification_reason: Needs identity clarification.

clarification_question: What is the protagonist's physical form and origin?



[[SECTION markdown]]

# Protagonist

Short, grounded character markdown.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]



Important rules:

- if a character does not have enough physical or visual description in the supplied material to support dependable later image generation, set manual_description_required to true

- explain exactly why in manual_description_reason

- do not guess ornate missing details just to avoid the flag

- if the chapter names a character without enough stable identification, set is_fully_identified to false

- use aliases for alternate names or partial labels seen in the chapter

- if the character might already exist under another name or is too weakly identified, set clarification_required to true and ask a targeted question

- if clarification is not required, still include clarification_reason and clarification_question as empty values

- emit one explicit character record per meaningful character mention

- every character record must have a FILMCREATOR_RECORD wrapper with type character

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

**Summary:**
John Carter is summoned to an audience with Lorquas Ptomel, a Thark leader. Ptomel issues a stern warning: while Carter has earned respect through combat, he remains an alien prisoner. He is accused of plotting escape with Dejah Thoris (the "red girl") and warns that if Carter attempts to flee with her, he will be killed. Ptomel emphasizes the importance of delivering Dejah Thoris safely to Tal Hajus, a brutal and powerful leader. 

Carter realizes that Sarkoja, a high-ranking female Thark, has been spying on him and reporting his intentions to undermine him. This encounter intensifies Carter's resolve to escape, driven by fear of what the predatory Tal Hajus might do to Dejah Thoris.

Following the meeting, Tars Tarkas assists Carter in establishing quarters. Following Thark custom, Carter is granted the spoils of the two chieftains he defeated, including weapons, silks, and furs. He moves into a third-floor apartment in a large building, strategically choosing a room close to Dejah Thoris's quarters to facilitate potential communication. Carter also takes responsibility for the retinues (women and youths) belonging to the fallen chieftains, organizing them within his new living quarters while reflecting on the cold, communal, and loveless social structures of the green Martians.

**Characters:**
* **John Carter:** The protagonist; a Thark chieftain by prowess but a prisoner by status; determined to rescue Dejah Thoris.
* **Lorquas Ptomel:** A Thark leader; stern, just by Martian standards, and wary of Carter's influence.
* **Tars Tarkas:** A respected Thark warrior who treats Carter with professional courtesy and assists him with logistics.
* **Sarkoja (Mentioned):** A powerful female Thark and informant who is actively working against Carter.
* **Tal Hajus (Mentioned):** A feared, brutal leader to whom Dejah Thoris is being delivered.
* **Dejah Thoris (Mentioned):** The captive red Jeddak princess; the primary motivation for Carter's escape plans.

**Settings:**
* **The Audience Chamber:** Where Carter meets Lorquas Ptomel.
* **The Plaza/Thark City:** A complex of buildings and streets featuring overgrown courts, fountains, and statuary from a lost era of Martian civilization.
* **Carter’s New Quarters:** A third-floor apartment in a large building overlooking an enormous central court filled with animals and vegetation.
````

## Raw Response
````text
[[FILMCREATOR_PACKET]]

task: character_extraction

version: 1

character_index_markdown:

[[SECTION character_index_markdown]]

# Character Index

- [John Carter](#john_carter)
- [Lorquas Ptomel](#lorquas_ptomel)
- [Tars Tarkas](#tars_tarkas)
- [Sarkoja](#sarkoja)
- [Tal Hajus](#tal_hajus)
- [Dejah Thoris](#dejah_thoris)

[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: john_carter
canonical_character_id: CH001 John Carter
aliases: Carter
is_fully_identified: true
manual_description_required: false
manual_description_reason: 
clarification_required: false
clarification_reason: 
clarification_question: 
[[SECTION markdown]]
# John Carter
**Role:** Protagonist; Thark chieftain by prowess, prisoner by status.
**Presence:** Physically present.
**Physical Description:** Human male (implied Earthling). Currently holds the spoils of two defeated chieftains including weapons, silks, and furs.
**Costume/Silhouette:** Wearing spoils of war (silks and furs).
**Prompt Phrases:** human male, warrior, survivor, wearing Martian silks and furs.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: lorquas_ptomel
canonical_character_id: CH012 Lorquas Ptomel
aliases: Ptomel
is_fully_identified: false
manual_description_required: true
manual_description_reason: No specific physical description provided beyond being a Thark leader.
clarification_required: false
clarification_reason: 
clarification_question: 
[[SECTION markdown]]
# Lorquas Ptomel
**Role:** Thark leader; stern authority figure.
**Presence:** Physically present.
**Physical Description:** Green Martian (Thark). Stern demeanor.
**Costume/Silhouette:** Thark warrior attire (implied).
**Prompt Phrases:** green Martian, Thark leader, stern expression, authoritative.
**Uncertainty Notes:** Specific facial features and exact armor/clothing details are not described in this chapter.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: tars_tarkas
canonical_character_id: CH012 Tars Tarkas
aliases: 
is_fully_identified: true
manual_description_required: false
manual_description_reason: 
clarification_required: false
clarification_reason: 
clarification_question: 
[[SECTION markdown]]
# Tars Tarkas
**Role:** Respected Thark warrior; ally/logistics assistant to Carter.
**Presence:** Physically present.
**Physical Description:** Green Martian (Thark) warrior.
**Costume/Silhouette:** Warrior attire.
**Prompt Phrases:** green Martian, Thark warrior, professional demeanor.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: sarkoja
canonical_character_id: CH012 Sarkoja
aliases: 
is_fully_identified: false
manual_description_required: true
manual_description_reason: Described as a high-ranking female Thark, but lacks specific visual details.
clarification_required: false
clarification_reason: 
clarification_question: 
[[SECTION markdown]]
# Sarkoja
**Role:** High-ranking female Thark; spy and antagonist.
**Presence:** Referenced (not present in scene).
**Physical Description:** Female Green Martian (Thark).
**Costume/Silhouette:** High-ranking Thark attire (implied).
**Prompt Phrases:** female green Martian, Thark noble, spy, calculating expression.
**Uncertainty Notes:** Specific physical features and clothing are not detailed in this text.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: tal_hajus
canonical_character_id: CH012 Tal Hajus
aliases: 
is_fully_identified: false
manual_description_required: true
manual_description_reason: Mentioned only as a brutal leader; no physical description provided.
clarification_required: false
clarification_reason: 
clarification_question: 
[[SECTION markdown]]
# Tal Hajus
**Role:** Feared, brutal Thark leader.
**Presence:** Referenced (not present in scene).
**Physical Description:** Green Martian (Thark).
**Costume/Silhouette:** Unknown.
**Prompt Phrases:** green Martian, brutal warrior, feared leader.
**Uncertainty Notes:** Character is only a looming threat in dialogue; no visual data available.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: dejah_thoris
canonical_character_id: CH012 Dejah Thoris
aliases: The red girl
is_fully_identified: true
manual_description_required: false
manual_description_reason: 
clarification_required: false
clarification_reason: 
clarification_question: 
[[SECTION markdown]]
# Dejah Thoris
**Role:** Captive Jeddak princess; Carter's motivation.
**Presence:** Referenced (not present in scene).
**Physical Description:** Red-skinned female (Jeddak/humanoid Martian).
**Costume/Silhouette:** Princess attire (implied).
**Prompt Phrases:** red-skinned female, Martian princess, captive, elegant.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
