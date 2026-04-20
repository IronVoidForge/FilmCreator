# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-20T17:42:13.431088+00:00
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

Chapter id: CH003

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

**Setting:** A circular basin on Mars covered in yellowish, moss-like vegetation, featuring a low walled enclosure with a thick glass roof (an incubator).

**Events:**
- The protagonist wakes up on Mars and discovers the effects of low gravity, finding that even small movements result in massive leaps.
- He explores a nearby enclosure and discovers it is an incubator containing large white eggs; several grotesque, six-limbed young Martians have already hatched.
- A party of twenty Martian warriors on multi-legged mounts approaches. The leader nearly kills the protagonist with a forty-foot spear, but the protagonist escapes by performing a massive thirty-foot leap over the incubator.
- Impressed by his agility rather than angered by his presence, the Martians view him as a curiosity rather than a threat.
- The leader dismounts, approaches unarmed, and offers a metal armlet as a gesture of peace. 
- The protagonist accepts the armlet, signaling friendship. He is then hoisted onto a Martian mount and taken away with the cavalcade toward distant hills.

**Characters:**
- **The Protagonist:** An Earthman, currently naked and unarmed, possessing superior agility due to Mars' low gravity.
- **Martian Warriors:** Large (15ft tall), multi-limbed humanoids with olive/green skin and red eyes. They are highly skilled with advanced long-range rifles.
- **The Leader:** A Martian warrior who initiates peaceful contact through gestures and the offering of an armlet.
- **Martian Mounts:** Massive, eight-legged animals with slate-colored skin and no hair.

**Key Elements for Scene Extraction:**
- The physical sensation of low-gravity movement (the "ludicrous" hopping).
- The visual reveal of the hatching Martian eggs inside the glass enclosure.
- The high-tension standoff between the protagonist and the charging cavalry.
- The non-verbal peace negotiation involving the metal armlet.
````

## Raw Response
````text
[[FILMCREATOR_PACKET]]

task: character_extraction

version: 1

character_index_markdown:

[[SECTION character_index_markdown]]

# Character Index - CH003

- [Protagonist](#protagonist)
- [Martian Warriors](#martian-warriors)
- [The Leader](#the-leader)
- [Martian Mounts](#martian-mounts)

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: protagonist

canonical_character_id: CH003 Protagonist

aliases: Earthman

is_fully_identified: false

manual_description_required: true

manual_description_reason: No specific physical features (hair, eyes, build) provided beyond being an "Earthman" and currently naked.

clarification_required: true

clarification_reason: Physical appearance is entirely absent from the text.

clarification_question: What are the protagonist's hair color, eye color, ethnicity, and general body type?

[[SECTION markdown]]

# Protagonist
**Role:** Central Character / Survivor

**Status:** Physically Present

**Physical Description:** 
An Earthman. Currently naked and unarmed. Exhibits extreme agility and leaping ability due to the low Martian gravity.

**Costume/Silhouette:** 
Naked; no clothing or equipment mentioned in this chapter.

**Descriptive Noun Phrases:** 
Naked Earthman, agile survivor, low-gravity leaper.

**Uncertainty Notes:** 
Complete lack of facial features, hair, or body composition details.
[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: martian_warriors

canonical_character_id: CH003 Martian Warriors

aliases: Martians

is_fully_identified: true

manual_description_required: false

manual_description_reason: 

clarification_required: false

clarification_reason: 

clarification_question: 

[[SECTION markdown]]

# Martian Warriors
**Role:** Supporting Group / Antagonists turned Curious Observers

**Status:** Physically Present

**Physical Description:** 
Large humanoids, approximately 15 feet tall. They possess olive or green skin and red eyes. They are multi-limbed.

**Costume/Silhouette:** 
Highly skilled warriors; equipped with advanced long-range rifles.

**Descriptive Noun Phrases:** 
15ft olive-skinned humanoids, red-eyed Martians, multi-limbed warriors, large green humanoids.

**Uncertainty Notes:** 
Specific clothing/armor details are not provided beyond their weaponry.
[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: martian_leader

canonical_character_id: CH003 Martian Leader

aliases: The Leader

is_fully_identified: false

manual_description_required: true

manual_description_reason: While part of the Martian warrior group, specific distinguishing features from the rest of the warriors are not detailed.

clarification_required: true

clarification_reason: Needs distinction from standard warriors to ensure unique character design.

clarification_question: Does the leader have unique markings, different colored skin/eyes, or specific armor that distinguishes him from the other twenty warriors?

[[SECTION markdown]]

# The Leader
**Role:** Supporting Character / Diplomat

**Status:** Physically Present

**Physical Description:** 
A Martian warrior (15ft tall, olive/green skin, red eyes, multi-limbed). He carries a forty-foot spear but later approaches the protagonist unarmed to offer peace.

**Costume/Silhouette:** 
Carries a massive forty-foot spear; carries a metal armlet used as a peace offering.

**Descriptive Noun Phrases:** 
Spear-wielding Martian leader, olive-skinned diplomat, large multi-limbed commander.

**Uncertainty Notes:** 
Visual distinction from the general warrior class is not established in text.
[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: martian_mounts

canonical_character_id: CH003 Martian Mounts

aliases: Multi-legged mounts

is_fully_identified: true

manual_description_required: false

manual_description_reason: 

clarification_required: false

clarification_reason: 

clarification_question: 

[[SECTION markdown]]

# Martian Mounts
**Role:** Supporting Element / Transport

**Status:** Physically Present

**Physical Description:** 
Massive, eight-legged animals. They have slate-colored skin and no hair.

**Costume/Silhouette:** 
Large, multi-legged beasts used for cavalry.

**Descriptive Noun Phrases:** 
Slate-skinned eight-legged mounts, massive hairless Martian beasts, slate-colored quadrupeds (octopods).

**Uncertainty Notes:** 
None.
[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
