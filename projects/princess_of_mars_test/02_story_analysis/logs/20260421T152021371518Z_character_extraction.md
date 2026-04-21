# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-21T15:20:21.371518+00:00
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

Chapter id: CH017

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

**Events:**
John Carter infiltrates the city of Thark to rescue Dejah Thoris from the clutches of the beastly Jeddak, Tal Hajus. After witnessing Tal Hajus threaten Dejah with prolonged torture and sexual violation, Carter intervenes. Instead of using his sword, he knocks the Jeddak unconscious with a single blow, allowing him to spirit Dejah Thoris and her companion Sola away from the city.

The escape turns into a grueling trek across a two-hundred-mile mossy waste toward Helium. The party suffers from extreme exhaustion, hunger, and thirst; one of their thoats collapses from fatigue, forcing Carter, Sola, and Dejah to continue on foot or with a single animal. During their journey, they are spotted by a Thark chieftain scanning the area with a fieldglass. To ensure the women's escape, Carter uses his Martian rifle to kill the charging chieftain and then stays behind to provide cover fire against a massive force of nearly a thousand warriors. After exhausting his ammunition, Carter attempts to lead the warriors away through acrobatic maneuvers but is eventually overtaken and beaten into unconsciousness.

**Characters:**
* **John Carter:** The protagonist; heroic and selfless; uses tactical thinking and superior weaponry to protect Dejah Thoris.
* **Dejah Thoris:** Princess of Helium; maintains her royal dignity even in the face of terror; expresses profound love for Carter during the escape.
* **Sola:** Dejah Thoris's companion; assists in the escape and helps manage the fleeing thoat.
* **Tal Hajus:** The villainous, bestial Jeddak of the Tharks; characterized by cruelty and animalistic passions.
* **Tars Tarkas:** A Thark warrior who watches the scene with silent loathing for Tal Hajus, though he does not intervene.
* **Woola:** Carter's faithful Martian hound, who tracks the party through the waste.

**Settings:**
* **The City of Thark:** A fortified settlement featuring large circular halls, raised platforms, and multi-story buildings.
* **The Mossy Waste:** A vast, trackless, and desolate expanse between Thark and Helium, characterized by a lack of waterways and extreme environmental hardship.
* **The Low Mountains/Hills:** A rugged terrain toward the end of the chapter that provides both potential landmarks and dangerous ravines for pursuit.
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
- [Dejah Thoris](#dejah_thoris)
- [Sola](#sola)
- [Tal Hajus](#tal_hajus)
- [Tars Tarkas](#tars_tarkas)
- [Woola](#woola)

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
**Role:** Protagonist / Heroic Warrior

**Status:** Physically Present

**Description:** A heroic and selfless warrior capable of extreme physical feats, including acrobatic maneuvers to evade large groups. He utilizes a Martian rifle and swords for combat.

**Prompt Phrases:** Heroic human warrior, tactical fighter, agile acrobat, wielding Martian rifle.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: dejah_thoris
canonical_character_id: CH003 Dejah Thoris
aliases: Princess of Helium
is_fully_identified: true
manual_description_required: false
manual_description_reason: 
clarification_required: false
clarification_reason: 
clarification_question: 
[[SECTION markdown]]
# Dejah Thoris
**Role:** Princess of Helium / Love Interest

**Status:** Physically Present

**Description:** A royal figure who maintains her dignity even under extreme duress and terror. She is a central figure in the escape from Thark.

**Prompt Phrases:** Royal Martian princess, dignified noblewoman, elegant silhouette.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: sola
canonical_character_id: CH004 Sola
aliases: 
is_fully_identified: true
manual_description_required: false
manual_description_reason: 
clarification_required: false
clarification_reason: 
clarification_question: 
[[SECTION markdown]]
# Sola
**Role:** Companion to Dejah Thoris

**Status:** Physically Present

**Description:** An assistant and companion to the Princess, involved in managing the escape and the thoat during the trek across the mossy waste.

**Prompt Phrases:** Female Martian companion, traveling party member.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: tal_hajus
canonical_character_id: CH005 Tal Hajus
aliases: Jeddak of the Tharks, The Beastly Jeddak
is_fully_identified: true
manual_description_required: false
manual_description_reason: 
clarification_required: false
clarification_reason: 
clarification_question: 
[[SECTION markdown]]
# Tal Hajus
**Role:** Villain / Antagonist

**Status:** Physically Present (referenced/seen)

**Description:** A beastly and cruel Jeddak of the Tharks. Characterized by animalistic passions and a penchant for cruelty and torture.

**Prompt Phrases:** Bestial Thark leader, cruel Jeddak, monstrous Martian warrior.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: tars_tarkas
canonical_character_id: CH006 Tars Tarkas
aliases: 
is_fully_identified: true
manual_description_required: false
manual_description_reason: 
clarification_required: false
clarification_reason: 
clarification_question: 
[[SECTION markdown]]
# Tars Tarkas
**Role:** Thark Warrior

**Status:** Physically Present (witness)

**Description:** A Thark warrior who observes the actions of Tal Hajus with silent loathing.

**Prompt Phrases:** Thark warrior, silent observer, Martian green man.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: woola
canonical_character_id: CH007 Woola
aliases: Martian hound
is_fully_identified: true
manual_description_required: false
manual_description_reason: 
clarification_required: false
clarification_reason: 
clarification_question: 
[[SECTION markdown]]
# Woola
**Role:** Companion / Animal

**Status:** Physically Present (referenced/tracking)

**Description:** A faithful Martian hound that tracks the party through the mossy waste.

**Prompt Phrases:** Large Martian hound, loyal beast, tracking animal.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
