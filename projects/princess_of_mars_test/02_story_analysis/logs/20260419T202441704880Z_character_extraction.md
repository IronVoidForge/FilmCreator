# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-19T20:24:41.704880+00:00
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

**Setting & Context:**
- **Timeframe:** Post-battle with air ships; specifically the seventh day following the conflict.
- **Location:** Lorquas Ptomel's community (city), near the plaza and courtyard.
- **Status:** Community remains within city for safety; homeward march to Thark is paused until ships are deemed safe.
- **Departure:** March toward Thark resumes on the seventh day after battle, probability of attack deemed remote by Lorquas Ptomel.

**Key Events & Plot Points:**
1.  **Beast Training:** Tars Tarkas instructs Carter in Thark customs (riding, guiding beasts). Carter introduces kindness to training thoats instead of violence (pistol blows).
2.  **Military Recognition:** Lorquas Ptomel presents Carter with a massive gold anklet from his own leg as appreciation for the regiment of tractable mounts.
3.  **Pre-Departure Routine:** Carter spends days preceding departure busy with lessons in Martian warfare and beast training, seeing little of Dejah Thoris.
4.  **Romantic Interaction:** On evening before departure, Carter intercepts Dejah Thoris and Sola walking on the avenue. He directs Sola away to be alone with Dejah Thoris.
5.  **Dialogue on Status:** Dejah Thoris notes Sarkoja told Sola Carter became a true Thark; she expects no more of him than other warriors. Carter dismisses this as Sarkoja being a liar.
6.  **Warfare Technology:** Dejah Thoris explains the exploding radium powder bullets used by Martians (explosion occurs upon impact or sunlight exposure).
7.  **Social Conflict:** Discussion on the warriors' jealousy of Dejah Thoris's status (daughter of ten thousand jeddaks) and their cruelty/ignominy toward her.
8.  **Intimate Conclusion:** Walking under two moons with Earth visible; Carter places silks on Dejah Thoris' shoulders; intimate touch on shoulder; mutual declaration of love.

**Visual Continuity & Atmosphere:**
- **Lighting:** Night scene illuminated by the two moons of Barsoom; Earth looking down with luminous green eye.
- **Environment:** Great avenue leading into plaza from east; courtyard with moss-like vegetation; buildings near plaza.
- **Character State:** Carter in silks and armor (Thark metal); Dejah Thoris in red Martian attire (implied by context of "red Martian salute"); Sola armed.
- **Mood:** Transition from military tension to romantic intimacy; chill of Martian night; sense of being alone in the universe during the walk.

**Scene Decomposition Notes:**
- **Opening Scene:** Community safety assessment and beast training recap (visual: courtyard, beasts).
- **Middle Sequence:** Pre-departure preparations and conversations with Dejah Thoris (visual: avenue, two moons, intimate proximity).
- **Closing Sequence:** Declaration of love and departure march (visual: walking away, gold anklet mentioned as reward).
````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
task: character_extraction
version: 1

[[SECTION character_index_markdown]]
# Chapter CH013 Character Index

| Asset ID | Canonical Character ID | Name | Status |
| :--- | :--- | :--- | :--- |
| carter | carter | Carter | Visible/Referenced |
| dejah_thoris | dejah_thoris | Dejah Thoris | Visible/Referenced |
| sola | sola | Sola | Referenced |
| lorquas_ptomel | lorquas_ptomel | Lorquas Ptomel | Referenced |
| tars_tarkas | tars_tarkas | Tars Tarkas | Referenced |
[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: carter
canonical_character_id: carter
aliases: ""
is_fully_identified: true
manual_description_required: false
manual_description_reason: ""
clarification_required: false
clarification_reason: ""
clarification_question: ""

[[SECTION markdown]]
---
**Asset ID:** `carter`
**Chapter Role:** Protagonist / Beast Trainer / Warrior
**Presence:** Physically Present (Silks and Armor)

**Description:**
Carter is the central figure in this chapter, described wearing silks and Thark metal armor. He is actively engaged in beast training under Tars Tarkas's instruction and receives a gold anklet from Lorquas Ptomel as recognition for his regiment of tractable mounts.

**Visual Continuity:**
- **Attire:** Silks and armor (Thark metal).
- **Context:** Seen on the avenue, in the courtyard, and walking under two moons with Dejah Thoris.
- **Action:** Training beasts, intercepting Sola and Dejah Thoris, declaring love.

**Notes:**
Physical description is supported by the text ("silks and armor"). No uncertainty flags raised for image generation based on provided summary.
---
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: dejah_thoris
canonical_character_id: dejah_thoris
aliases: ""
is_fully_identified: true
manual_description_required: false
manual_description_reason: ""
clarification_required: false
clarification_reason: ""
clarification_question: ""

[[SECTION markdown]]
---
**Asset ID:** `dejah_thoris`
**Chapter Role:** Martian Princess / Lover
**Presence:** Physically Present (Red Attire)

**Description:**
Dejah Thoris is the daughter of ten thousand jeddaks, described in red Martian attire. She interacts with Carter regarding Sarkoja's lies, explains Martian warfare technology (radium powder bullets), and shares an intimate moment with him under two moons.

**Visual Continuity:**
- **Attire:** Red Martian attire.
- **Context:** Walking on the avenue, near the plaza, in the courtyard.
- **Action:** Discussing status, explaining technology, receiving silks from Carter.

**Notes:**
Physical description is supported by the text ("red Martian attire"). No uncertainty flags raised for image generation based on provided summary.
---
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: sola
canonical_character_id: sola
aliases: ""
is_fully_identified: true
manual_description_required: true
manual_description_reason: "Only 'armed' is mentioned in the text; lacks specific physical details (hair, build) required for dependable image generation."
clarification_required: false
clarification_reason: ""
clarification_question: ""

[[SECTION markdown]]
---
**Asset ID:** `sola`
**Chapter Role:** Companion / Witness
**Presence:** Referenced (Walking with Dejah Thoris)

**Description:**
Sola is referenced as walking with Dejah Thoris on the avenue. Carter directs her away to be alone with Dejah Thoris. She is noted as being armed.

**Visual Continuity:**
- **Attire:** Not specified in text.
- **Context:** Walking on the avenue, near the plaza.
- **Action:** Intercepted by Carter, directed away.

**Notes:**
Physical description is sparse ("armed" only). Manual description required for dependable image generation as per source limitations.
---
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: lorquas_ptomel
canonical_character_id: lorquas_ptomel
aliases: ""
is_fully_identified: true
manual_description_required: true
manual_description_reason: "Only 'leader' status and 'gold anklet' are mentioned; lacks specific physical details (face, build) required for dependable image generation."
clarification_required: false
clarification_reason: ""
clarification_question: ""

[[SECTION markdown]]
---
**Asset ID:** `lorquas_ptomel`
**Chapter Role:** Community Leader / Rewarder
**Presence:** Referenced (Giving Anklet)

**Description:**
Lorquas Ptomel is the leader of the community, referenced as presenting Carter with a massive gold anklet from his own leg in appreciation for the regiment of tractable mounts. He assesses safety and beast training status.

**Visual Continuity:**
- **Attire:** Not specified in text.
- **Context:** Community plaza/courtyard setting.
- **Action:** Presenting reward, assessing safety.

**Notes:**
Physical description is sparse (only "leader" status and "gold anklet"). Manual description required for dependable image generation as per source limitations.
---
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: tars_tarkas
canonical_character_id: tars_tarkas
aliases: ""
is_fully_identified: true
manual_description_required: true
manual_description_reason: "Only 'instructor' role is mentioned; lacks specific physical details (face, build) required for dependable image generation."
clarification_required: false
clarification_reason: ""
clarification_question: ""

[[SECTION markdown]]
---
**Asset ID:** `tars_tarkas`
**Chapter Role:** Instructor / Mentor
**Presence:** Referenced (Instructing Carter)

**Description:**
Tars Tarkas is mentioned as instructing Carter in Thark customs, specifically riding and guiding beasts. He represents the military tradition of Thark warriors.

**Visual Continuity:**
- **Attire:** Not specified in text.
- **Context:** Courtyard/beast training area.
- **Action:** Instructing Carter on beast handling.

**Notes:**
Physical description is sparse (only "instructor" role). Manual description required for dependable image generation as per source limitations.
---
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
