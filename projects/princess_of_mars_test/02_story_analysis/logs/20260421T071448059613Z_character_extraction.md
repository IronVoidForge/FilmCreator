# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-21T07:14:48.059613+00:00
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

Chapter id: CH010

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

**Chapter Title:** Champion and Chief
**Setting:** The city of the Tharks (Green Martians); specifically, the outskirts near low hills/ravines and the interior audience chamber of Lorquas Ptomel.

**Characters:**
*   **John Carter:** The protagonist; an Earthman who has mastered some Martian tongue and is learning the social codes of Barsoom.
*   **Woola:** A large, loyal Martian creature (white ape/hound-like) serving as Carter's guardian.
*   **Sola:** A kind and civilized green Martian woman who acts as Carter's instructress.
*   **Dejah Thoris:** The Princess of Helium; a captive red-skinned human woman.
*   **Tars Tarkas:** A Thark warrior/chieftain who oversees Carter's custody.
*   **Lorquas Ptomel:** A Thark chieftain presiding over the council.
*   **Sarkoja:** A cruel green Martian woman acting as a guard for the prisoner.

**Key Events:**
1.  **Bonding with Woola:** Early in the morning, Carter explores the city limits. He attempts to test his bond with Woola through affection rather than command. The interaction succeeds, establishing a deep, mutual understanding and loyalty between the man and the beast.
2.  **The Audience Chamber Observation:** Carter observes the trial of Dejah Thoris. He witnesses the brutality of the green Martian guards (specifically Sarkoja) and hears Dejah Thoris deliver a sophisticated plea for peace and scientific cooperation to the Thark council.
3.  **The Violent Outburst:** During a moment of tension, a young Thark warrior strikes Dejah Thoris across the face in a display of "mirthless laughter." 
4.  **Carter's Intervention:** Driven by rage, Carter intervenes and engages the warrior in single combat. Despite the size difference, Carter kills the warrior using superior technique and ferocity.
5.  **Ascension to Chieftain Status:** By killing a warrior, Carter inadvertently wins the "spoils" and honors of the deceased. He is recognized by the Tharks as a chieftain, granting him a degree of freedom and respect within their society.
6.  **The Confrontation with Tars Tarkas:** Tars Tarkas questions Carter's sudden proficiency in the language and warns him of the dangers of his "unprecedented temerity." Carter asserts his moral code, declaring that he will protect Dejah Thoris from any future insult or injury.
7.  **Departure:** Recognized as a man of valor, Carter and Dejah Thoris (accompanied by Woola) exit the chamber, with Carter assuming the responsibility of her protector under his new status as a Thark chieftain.
````

## Raw Response
````text
[[FILMCREATOR_PACKET]]

task: character_extraction

version: 1

character_index_markdown:

[[SECTION character_index_markdown]]

# Character Index - Chapter 010

- [John Carter](#john_carter)
- [Woola](#woola)
- [Sola](#sola)
- [Dejah Thoris](#dejah_thoris)
- [Tars Tarkas](#tars_tarkas)
- [Lorquas Ptomel](#lorquas_ptomel)
- [Sarkoja](#sarkoja)

[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: john_carter
canonical_character_id: CH001 John Carter
aliases: Earthman, Protagonist
is_fully_identified: true
manual_description_required: false
manual_description_reason: 
clarification_required: false
clarification_reason: 
clarification_question: 
[[SECTION markdown]]
# John Carter
**Role:** Protagonist / New Thark Chieftain
**Presence:** Physically Present
**Description:** An Earthman living on Barsoom. He possesses superior combat technique and ferocity compared to the local warriors. He is capable of single combat against larger Martian warriors and has recently gained status through martial valor.
**Prompt Phrases:** Human male, Earthling, warrior, combatant, protector.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: woola
canonical_character_id: CH003 Woola
aliases: Martian creature, white hound-like beast
is_fully_identified: true
manual_description_required: false
manual_description_reason: 
clarification_required: false
clarification_reason: 
clarification_question: 
[[SECTION markdown]]
# Woola
**Role:** Guardian / Companion
**Presence:** Physically Present
**Description:** A large, loyal Martian creature described as a white ape or hound-like beast. He shares a deep, mutual bond of affection and loyalty with John Carter.
**Prompt Phrases:** Large white Martian beast, white hound-like creature, loyal animal companion, massive white quadruped.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: sola
canonical_character_id: CH004 Sola
aliases: Instructress
is_fully_identified: true
manual_description_required: false
manual_description_reason: 
clarification_required: false
clarification_reason: 
clarification_question: 
[[SECTION markdown]]
# Sola
**Role:** Instructress
**Presence:** Physically Present (referenced/implied presence in context of Carter's social learning)
**Description:** A kind and civilized green Martian woman. She serves as an instructor to John Carter regarding Martian social codes and language.
**Prompt Phrases:** Green Martian woman, civilized green Martian, female Thark-adjacent.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: dejah_thoris
canonical_character_id: CH005 Dejah Thoris
aliases: Princess of Helium, Prisoner
is_fully_identified: true
manual_description_required: false
manual_description_reason: 
clarification_required: false
clarification_reason: 
clarification_question: 
[[SECTION markdown]]
# Dejah Thoris
**Role:** Captive Princess
**Presence:** Physically Present
**Description:** A red-skinned human woman and the Princess of Helium. She is highly sophisticated, capable of delivering complex pleas for peace and scientific cooperation. She is currently a captive of the Tharks.
**Prompt Phrases:** Red-skinned human woman, princess, elegant captive, sophisticated female.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: tars_tarkas
canonical_character_id: CH006 Tars Tarkas
aliases: Thark warrior/chieftain
is_fully_identified: true
manual_description_required: false
manual_description_reason: 
clarification_required: false
clarification_reason: 
clarification_question: 
[[SECTION markdown]]
# Tars Tarkas
**Role:** Thark Chieftain/Overseer
**Presence:** Physically Present
**Description:** A Thark warrior and chieftain who oversees John Carter's custody. He is observant of Carter's sudden proficiency in the Martian language and warns him of his temerity.
**Prompt Phrases:** Green Martian warrior, Thark chieftain, large green Martian.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: lorquas_ptomel
canonical_character_id: CH007 Lorquas Ptomel
aliases: Thark chieftain
is_fully_identified: true
manual_description_required: false
manual_description_reason: 
clarification_required: false
clarification_reason: 
clarification_question: 
[[SECTION markdown]]
# Lorquas Ptomel
**Role:** Presiding Chieftain
**Presence:** Physically Present
**Description:** A Thark chieftain who presides over the council/audience chamber during the trial of Dejah Thoris.
**Prompt Phrases:** Green Martian chieftain, presiding Thark leader.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: sarkoja
canonical_character_id: CH008 Sarkoja
aliases: Guard
is_fully_identified: true
manual_description_required: false
manual_description_reason: 
clarification_required: false
clarification_reason: 
clarification_question: 
[[SECTION markdown]]
# Sarkoja
**Role:** Guard
**Presence:** Physically Present
**Description:** A cruel green Martian woman who serves as a guard for the prisoner (Dejah Thoris).
**Prompt Phrases:** Cruel green Martian woman, female Thark guard.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
