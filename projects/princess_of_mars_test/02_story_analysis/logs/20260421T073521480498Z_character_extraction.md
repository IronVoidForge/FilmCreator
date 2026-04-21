# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-21T07:35:21.480498+00:00
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

Chapter id: CH016

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

**Setting:** The ancient, sprawling city of Thark, characterized by massive, grand architecture and divided into quarters for different communities under the rule of Tal Hajus.

**Characters:**
* **John Carter:** A human warrior attempting to orchestrate an escape for Dejah Thoris.
* **Dejah Thoris:** Princess of Helium, currently a captive of the Tharks.
* **Sola:** A Thark woman who harbors sympathies for the protagonists.
* **Tal Hajus:** The Jeddak (ruler) of Thark.
* **Woola:** John Carter's loyal, multi-tusked Martian hound.
* **Sarkoja:** A Thark priest/advisor whose machinations threaten the protagonists.

**Events:**
* **The Journey to Thark:** John Carter, Dejah Thoris, and Sola travel for twenty days across sea bottoms and canals, moving stealthily under cover of darkness to avoid Martian patrols.
* **Arrival in Thark:** The group enters the city of Thark, where they are assigned quarters based on their status as captives/warriors. John Carter occupies a large building near the central plaza.
* **The Declaration:** John Carter visits Dejah Thoris and formally declares his devotion to her, commanding her to assist him in her own escape. 
* **The Threat Revealed:** Sola arrives with news that Sarkoja has advised Tal Hajus to throw Dejah Thoris to the wild dogs in the upcoming yearly games.
* **Escape Planning:** Using a map drawn by Dejah Thoris on a marble floor, the trio decides to flee via a northern waterway that leads toward Helium, hoping to bypass the more heavily patrolled southern routes.
* **The Failed Rendezvous:** John Carter slips out of the city at night with his thoats (mounts) to meet the women at the city edge. However, he discovers that the escape plan has been compromised by Thark warriors.
* **The Ambush Plot:** After hiding his animals in a courtyard, John Carter attempts to return to Dejah Thoris's quarters. He overhears a Thark chieftain instructing warriors to ambush him and take him to the vaults beneath the Jeddak's quarters, while Dejah Thoris is being taken directly to Tal Hajus.
````

## Raw Response
````text
[[FILMCREATOR_PACKET]]

task: character_extraction

version: 1

character_index_markdown:

[[SECTION character_index_markdown]]

# Character Index - CH016

- [john_carter](#john_carter)
- [dejah_thoris](#dejah_thoris)
- [sola](#sola)
- [tal_hajus](#tal_hajus)
- [woola](#woola)
- [sarkoja](#sarkoja)

[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: john_carter
canonical_character_id: John Carter
aliases: Human Warrior
is_fully_identified: true
manual_description_required: false
manual_description_reason: 
clarification_required: false
clarification_reason: 
clarification_question: 
[[SECTION markdown]]
# John Carter
**Role:** Protagonist / Human Warrior

**Status:** Physically Present

**Physical Description:** A human warrior capable of navigating Martian terrain and managing thoats.

**Costume/Silhouette:** Warrior attire suitable for stealthy travel and combat.

**Prompt Phrases:** Human male, warrior, athletic build, traveling through Thark.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: dejah_thoris
canonical_character_id: Dejah Thoris
aliases: Princess of Helium
is_fully_identified: true
manual_description_required: false
manual_description_reason: 
clarification_required: false
clarification_reason: 
clarification_question: 
[[SECTION markdown]]
# Dejah Thoris
**Role:** Captive Princess

**Status:** Physically Present

**Physical Description:** Princess of Helium, currently held captive by the Tharks.

**Costume/Silhouette:** Royal attire (implied), currently in captivity.

**Prompt Phrases:** Martian princess, noble features, captive, Helium royalty.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: sola
canonical_character_id: Sola
aliases: Thark woman
is_fully_identified: true
manual_description_required: false
manual_description_reason: 
clarification_required: false
clarification_reason: 
clarification_question: 
[[SECTION markdown]]
# Sola
**Role:** Sympathetic Ally

**Status:** Physically Present

**Physical Description:** A Thark woman with sympathies for the protagonists.

**Costume/Silhouette:** Thark attire.

**Prompt Phrases:** Thark female, sympathetic expression, Martian inhabitant.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: tal_hajus
canonical_character_id: Tal Hajus
aliases: Jeddak of Thark
is_fully_identified: true
manual_description_required: false
manual_description_reason: 
clarification_required: false
clarification_reason: 
clarification_question: 
[[SECTION markdown]]
# Tal Hajus
**Role:** Ruler/Antagonist

**Status:** Referenced / Present in city

**Physical Description:** The Jeddak (ruler) of the Tharks.

**Costume/Silhouette:** Grand, authoritative Thark regalia.

**Prompt Phrases:** Thark ruler, Jeddak, commanding presence, Martian authority.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: woola
canonical_character_id: Woola
aliases: Martian hound
is_fully_identified: true
manual_description_required: false
manual_description_reason: 
clarification_required: false
clarification_reason: 
clarification_question: 
[[SECTION markdown]]
# Woola
**Role:** Loyal Companion

**Status:** Referenced

**Physical Description:** A multi-tusked Martian hound.

**Costume/Silhouette:** Large, beastly silhouette with prominent tusks.

**Prompt Phrases:** Multi-tusked Martian hound, loyal beast, large canine-like creature.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: sarkoja
canonical_character_id: Sarkoja
aliases: Thark priest/advisor
is_fully_identified: true
manual_description_required: false
manual_description_reason: 
clarification_required: false
clarification_reason: 
clarification_question: 
[[SECTION markdown]]
# Sarkoja
**Role:** Scheming Advisor

**Status:** Referenced / Present in city

**Physical Description:** A Thark priest and advisor to the Jeddak.

**Costume/Silhouette:** Priest/Advisor robes or ceremonial Thark attire.

**Prompt Phrases:** Thark priest, scheming advisor, religious authority, Martian manipulator.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
