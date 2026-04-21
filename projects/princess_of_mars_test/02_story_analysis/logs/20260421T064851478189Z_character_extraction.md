# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-21T06:48:51.478688+00:00
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

**Setting:** A circular basin on Mars covered in yellowish, moss-like vegetation, featuring quartz-bearing rock outcroppings and a low, walled glass enclosure (an incubator).

**Events:**
- The protagonist wakes up on Mars and discovers the effects of low gravity, finding that even simple movements result in massive leaps.
- He explores a nearby glass-roofed enclosure and observes several hundred large white eggs; some have hatched into grotesque, six-limbed young creatures.
- A party of twenty Martian warriors on eight-legged mounts approaches. The leader nearly kills the protagonist with a forty-foot spear, but the protagonist narrowly escapes by performing a massive thirty-foot leap over the incubator.
- The Martians, astonished by his agility rather than angered by his presence near their young, decide to capture him as a curiosity.
- The leader of the party dismounts, approaches unarmed, and offers a metal armlet as a gesture of peace. 
- The protagonist accepts the armlet, signaling friendship. He is then hoisted onto a Martian mount and taken away by the cavalcade toward distant hills.

**Characters:**
- **The Protagonist:** An Earthman, currently naked and unarmed, possessing superhuman agility due to the Martian gravity.
- **Martian Warriors:** Fifteen-foot-tall humanoids with four arms (two right, two left), red eyes, and white tusks. They are highly skilled with long-range radium rifles.
- **The Leader:** A prominent warrior who initiates peaceful contact through gesture and a gift of an armlet.
- **Martian Mounts:** Ten-foot-tall, eight-legged, slate-colored animals with glossy skin and no hair.

**Key Technology/Biology:**
- **Incubator:** A glass-roofed structure used for hatching Martian eggs.
- **Martian Rifles:** Highly advanced weapons made of white metal and wood, capable of firing radium projectiles at extreme ranges (up to 200+ miles).
- **Martian Anatomy:** Multi-limbed, large-boned, and possessing antenna-like ears and independent eyes.
````

## Raw Response
````text
[[FILMCREATOR_PACKET]]

task: character_extraction

version: 1

character_index_markdown:

[[SECTION character_index_markdown]]

# Character Index - CH003

- [protagonist](#protagonist)
- [martian_warrior_leader](#martian_warrior_leader)
- [martian_warriors](#martian_warriors)
- [martian_mounts](#martian_mounts)

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: protagonist

canonical_character_id: CH003 Protagonist

aliases: Earthman

is_fully_identified: false

manual_description_required: true

manual_description_reason: No physical description (hair, eyes, build, ethnicity) provided beyond being an "Earthman."

clarification_required: true

clarification_reason: Physical appearance is entirely absent from the text.

clarification_question: What are the protagonist's specific physical features (age, hair color, eye color, body type)?

[[SECTION markdown]]

# Protagonist
**Role:** Main Character / Survivor

**Status:** Physically Present

**Physical Description:** 
An Earthman currently appearing naked and unarmed. He exhibits superhuman agility and leaping ability due to the low Martian gravity.

**Costume/Silhouette:** 
Naked; no clothing or equipment mentioned in this chapter.

**Prompting Phrases:** 
Naked human male, agile movement, high-leaping silhouette, Earthman.

**Uncertainty Notes:** 
Complete lack of facial features, hair, or body type details.
[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: martian_warrior_leader

canonical_character_id: CH003 Martian Leader

aliases: The Leader

is_fully_identified: true

manual_description_required: false

manual_description_reason: 

clarification_required: false

clarification_reason: 

clarification_question: 

[[SECTION markdown]]

# Martian Warrior Leader
**Role:** Diplomatic/Aggressive Contact

**Status:** Physically Present

**Physical Description:** 
A fifteen-foot-tall humanoid with four arms (two right, two left), red eyes, white tusks, and antenna-like ears. Possesses independent eyes.

**Costume/Silhouette:** 
Part of a warrior party; carries a forty-foot spear. Later approaches unarmed to offer a metal armlet.

**Prompting Phrases:** 
15-foot tall humanoid, four arms, red eyes, white tusks, antenna ears, Martian warrior.

**Uncertainty Notes:** 
Specific clothing/armor details are not described, only the presence of a spear and an armlet.
[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: martian_warriors

canonical_character_id: CH003 Martian Warriors

aliases: Party of twenty, Martian warriors

is_fully_identified: true

manual_description_required: false

manual_description_reason: 

clarification_required: false

clarification_reason: 

clarification_question: 

[[SECTION markdown]]

# Martian Warriors
**Role:** Antagonists / Captors

**Status:** Physically Present (Group)

**Physical Description:** 
A group of twenty fifteen-foot-tall humanoids. They feature four arms, red eyes, white tusks, and antenna-like ears with independent eyes.

**Costume/Silhouette:** 
Equipped with long-range radium rifles made of white metal and wood.

**Prompting Phrases:** 
Group of giant humanoids, four arms, red eyes, white tusks, carrying radium rifles, white metal and wood weapons.

**Uncertainty Notes:** 
Specific armor or clothing textures are not specified.
[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: martian_mounts

canonical_character_id: CH003 Martian Mounts

aliases: Eight-legged mounts

is_fully_identified: true

manual_description_required: false

manual_description_reason: 

clarification_required: false

clarification_reason: 

clarification_question: 

[[SECTION markdown]]

# Martian Mounts
**Role:** Transport / Beasts

**Status:** Physically Present

**Physical Description:** 
Ten-foot-tall, eight-legged animals with slate-colored, glossy skin and no hair.

**Costume/Silhouette:** 
Large, multi-legged beasts used for riding by the Martian warriors.

**Prompting Phrases:** 
Ten-foot tall eight-legged beast, slate-colored skin, glossy texture, hairless animal, Martian mount.

**Uncertainty Notes:** 
None.
[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
