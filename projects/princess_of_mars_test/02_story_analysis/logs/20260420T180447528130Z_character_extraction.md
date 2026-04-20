# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-20T18:04:47.528130+00:00
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

Chapter id: CH018

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

**Setting:**
The chapter moves from a small medical room to the open Martian plains during a military march, eventually concluding in the pitch-black, claustrophobic dungeons of the city of Warhoon.

**Characters:**
* **Protagonist:** A human survivor who has been wounded and is being held captive by the Warhoons.
* **Dak Kova:** A scarred, ferocious Warhoon warrior/jed; a former lieutenant who is ambitious, insubordinate, and murderous.
* **Bar Comas:** The young Jeddak of the Warhoon hordes, characterized by dignity and strength before his violent death.
* **The Female Healer:** An ancient, ugly Warhoon woman who treats the protagonist's wounds.
* **Warhoon Warriors/Jeddaks:** A bloodthirsty tribe known for wearing human skulls and dried hands as trophies; they are more ferocious than the Tharks.

**Key Events:**
* **Recovery and Transport:** The protagonist regains consciousness after being treated by a Warhoon female. He is strapped to a wild thoat and forced to ride with the main column of the Warhoon army.
* **The Duel for Power:** During a confrontation before the Jeddak Bar Comas, Dak Kova openly defies his leader. This escalates into a primal, animalistic duel between the two warriors. Bar Comas is killed in a brutal manner, allowing Dak Kova to seize the title of Jeddak.
* **The March to Warhoon:** The Warhoon army turns back toward their city after the delay caused by the duel. The protagonist observes the extreme violence and frequent duels inherent to Warhoon culture.
* **Imprisonment:** Upon reaching Warhoon, the protagonist is cast into a dark dungeon and chained to the floor for an indeterminate amount of time, suffering intense psychological terror in the darkness.
* **The Escape Attempt:** Driven to near-madness, the protagonist ambushes his food deliverer with his heavy chains, killing him. He recovers his senses upon finding the jailer's keys on the corpse.
* **The Eyes in the Dark:** As the protagonist prepares to use the keys, he is confronted by several pairs of gleaming eyes watching him from the darkness of the dungeon, which then retreat into the shadows.
````

## Raw Response
````text
[[FILMCREATOR_PACKET]]

task: character_extraction

version: 1

character_index_markdown:

[[SECTION character_index_markdown]]

# Character Index - Chapter 018

- [Protagonist](#protagonist)
- [Dak Kova](#dak-kova)
- [Bar Comas](#bar-comas)
- [The Female Healer](#the-female-healer)
- [Warhoon Warriors](#warhoon-warriors)

[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: protagonist
canonical_character_id: CH002 Protagonist
aliases: Human survivor
is_fully_identified: false
manual_description_required: true
manual_description_reason: Physical appearance, age, and specific clothing are not described in this chapter beyond being a wounded human.
clarification_required: true
clarification_reason: Needs physical profile for consistent rendering.
clarification_question: What is the protagonist's hair color, eye color, build, and general facial features?

[[SECTION markdown]]
# Protagonist
**Role:** Captive/Survivor

**Status:** Physically Present (Wounded)

**Physical Description:** 
A human male survivor. Currently wounded and recovering from medical treatment. He is seen being strapped to a wild thoat and later chained to a dungeon floor.

**Costume/Silhouette:** 
No specific clothing details provided; likely wearing rags or basic survival gear consistent with a captive state.

**Descriptive Noun Phrases:** 
Wounded human survivor, captive prisoner, shackled man.

**Uncertainty Notes:** 
Specific facial features and physical build are unknown.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: dak_kova
canonical_character_id: Dak Kova
aliases: Former Lieutenant, New Jeddak
is_fully_identified: true
manual_description_required: false
manual_description_reason: 
clarification_required: false
clarification_question: 
[[SECTION markdown]]
# Dak Kova
**Role:** Antagonist / Usurper

**Status:** Physically Present

**Physical Description:** 
A ferocious and scarred Warhoon warrior. Characterized by an ambitious, insubordinate, and murderous temperament.

**Costume/Silhouette:** 
Warhoon warrior attire; likely incorporates trophies such as human skulls or dried hands as per tribal custom.

**Descriptive Noun Phrases:** 
Scarred Warhoon warrior, ferocious jed, murderous usurper, ambitious warrior.

**Uncertainty Notes:** 
Specific scar patterns and exact trophy placement are not detailed.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: bar_comas
canonical_character_id: Bar Comas
aliases: Jeddak
is_fully_identified: true
manual_description_required: false
manual_description_reason: 
clarification_required: false
clarification_question: 
[[SECTION markdown]]
# Bar Comas
**Role:** Fallen Leader

**Status:** Physically Present (Deceased in chapter)

**Physical Description:** 
A Warhoon leader characterized by dignity and strength.

**Costume/Silhouette:** 
Warhoon Jeddak regalia; likely highly decorated with tribal trophies.

**Descriptive Noun Phrases:** 
Dignified Warhoon Jeddak, strong warrior leader.

**Uncertainty Notes:** 
Specific visual details of his "dignity" are implied through behavior rather than explicit physical traits.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: female_healer
canonical_character_id: The Female Healer
aliases: Ancient Warhoon woman
is_fully_identified: true
manual_description_required: false
manual_description_reason: 
clarification_required: false
clarification_question: 
[[SECTION markdown]]
# The Female Healer
**Role:** Medical Attendant (Minor)

**Status:** Physically Present

**Physical Description:** 
An ancient and ugly Warhoon woman.

**Costume/Silhouette:** 
Likely primitive or tribal healer's garb.

**Descriptive Noun Phrases:** 
Ancient ugly Warhoon, tribal healer.

**Uncertainty Notes:** 
"Ugly" is a subjective descriptor; specific facial features are not provided.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: warhoon_warriors
canonical_character_id: Warhoon Warriors
aliases: The Hordes, The Tribe
is_fully_identified: true
manual_description_required: false
manual_description_reason: 
clarification_required: false
clarification_question: 
[[SECTION markdown]]
# Warhoon Warriors
**Role:** Tribal Soldiers / Antagonists

**Status:** Physically Present (Group)

**Physical Description:** 
Bloodthirsty and ferocious warriors. More violent than the Tharks.

**Costume/Silhouette:** 
Distinctive tribal appearance featuring human skulls and dried hands worn as trophies.

**Descriptive Noun Phrases:** 
Skull-wearing warriors, trophy-clad horde, bloodthirsty Warhoon soldiers.

**Uncertainty Notes:** 
Individual variations within the group are not specified.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
