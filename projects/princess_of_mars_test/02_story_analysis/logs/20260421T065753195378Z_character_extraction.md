# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-21T06:57:53.195378+00:00
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

Chapter id: CH006

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

**Setting:** An interior chamber within a Martian building, overlooking a plaza.

**Characters:**
* **The Protagonist:** An Earthman fighting for survival.
* **The Watch-thing:** A loyal, multi-legged, beast-like creature that serves as the protagonist's guardian.
* **The Ape-men:** Two massive, ten-to-fifteen-foot tall creatures with four limbs and gorilla-like features.
* **Tars Tarkas:** A Martian warrior who respects physical prowess.
* **Sola:** A Martian woman who shows compassion and solicitude toward the protagonist.
* **Martian Warriors:** A group of warriors following Tars Tarkas.

**Events:**
* **The Ambush:** The protagonist is pinned by one massive ape-man while its mate approaches with a stone cudgel to kill him.
* **The Battle of the Beasts:** The protagonist's watch-thing intervenes, engaging the second ape-man in a ferocious struggle. As the watch-thing begins to succumb to the ape-man's strength, the protagonist seizes the fallen cudgel and kills the first ape-man by crushing its skull.
* **The Second Duel:** The mate of the slain ape-man returns in a rage. Despite the overwhelming physical disadvantage, the protagonist decides to stay and fight to honor his dying guardian. Using earthly combat tactics—striking the creature's chin and stomach—the protagonist manages to incapacitate and kill the second monster.
* **The Arrival of the Martians:** Tars Tarkas, Sola, and a group of warriors arrive, having witnessed the fight. They applaud the protagonist's bravery, viewing his combat skills as a source of high regard.
* **Conflict over the Beast:** The Martian warriors attempt to execute the wounded watch-thing. The protagonist intervenes by striking a warrior's arm, preventing the shot. 
* **Resolution:** Tars Tarkas allows the protagonist to keep his beast. The protagonist realizes he has found two allies on Mars: Sola, who provides emotional care, and his loyal beast, who provides protection.
````

## Raw Response
````text
[[FILMCREATOR_PACKET]]

task: character_extraction

version: 1

character_index_markdown:

[[SECTION character_index_markdown]]

# Character Index - CH006

- [protagonist](#protagonist)
- [watch_thing](#watch_thing)
- [ape_man_1](#ape_man_1)
- [ape_man_2](#ape_man_2)
- [tars_tarkas](#tars_tarkas)
- [sola](#sola)
- [martian_warriors](#martian_warriors)

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: protagonist

canonical_character_id: CH001 Protagonist

aliases: Earthman

is_fully_identified: false

manual_description_required: true

manual_description_reason: Physical appearance, clothing, and specific build are not described in this chapter.

clarification_required: true

clarification_reason: Needs physical profile for visual consistency.

clarification_question: What is the protagonist's height, hair color, facial features, and current attire?

[[SECTION markdown]]

# Protagonist
**Role:** Main Character / Survivor

**Presence:** Physically Present

**Physical Description:** 
An Earthman fighting for survival. No specific physical traits or clothing are provided in this chapter beyond his ability to wield a stone cudgel and use earthly combat tactics (striking chin/stomach).

**Uncertainty Notes:** 
Visual identity is entirely unknown; requires character design sheet.
[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: watch_thing

canonical_character_id: CH003 Watch-thing

aliases: Guardian, Beast

is_fully_identified: false

manual_description_required: true

manual_description_reason: General morphology is provided (multi-legged), but specific textures, colors, and scale are missing.

clarification_required: true

clarification_reason: Needs specific biological details for rendering.

clarification_question: What color is the creature's skin/fur, how many legs does it have exactly, and what is its approximate size?

[[SECTION markdown]]

# Watch-thing
**Role:** Protagonist's Guardian / Companion

**Presence:** Physically Present

**Physical Description:** 
A loyal, multi-legged, beast-like creature. Engages in ferocious combat with large ape-men.

**Uncertainty Notes:** 
Specific species morphology and color palette are undefined.
[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: ape_man_1

canonical_character_id: CH004 Ape-men

aliases: First Ape-man

is_fully_identified: true

manual_description_required: false

manual_description_reason: 

clarification_required: false

clarification_reason: 

clarification_question: 

[[SECTION markdown]]

# Ape-man 1
**Role:** Antagonist / Combatant

**Presence:** Physically Present (Deceased)

**Physical Description:** 
A massive, ten-to-fifteen-foot tall creature with four limbs and gorilla-like features.

**Useful Phrases:** 
Massive primate-like humanoid, ten-foot tall ape-man, heavy-set gorilla features.
[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: ape_man_2

canonical_character_id: CH004 Ape-men

aliases: Second Ape-man, Mate of the first

is_fully_identified: true

manual_description_required: false

manual_description_reason: 

clarification_required: false

clarification_reason: 

clarification_question: 

[[SECTION markdown]]

# Ape-man 2
**Role:** Antagonist / Combatant

**Presence:** Physically Present (Deceased)

**Physical Description:** 
A massive, ten-to-fifteen-foot tall creature with four limbs and gorilla-like features. Carried a stone cudgel.

**Useful Phrases:** 
Giant ape-man, heavy primate silhouette, wielding stone cudgel.
[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: tars_tarkas

canonical_character_id: CH005 Tars Tarkas

aliases: Martian Warrior

is_fully_identified: false

manual_description_required: true

manual_description_reason: While identified as a warrior, specific physical appearance (Martian biology) is not detailed in this chapter.

clarification_required: true

clarification_reason: Needs biological/visual description for Martian species.

clarification_question: What does Tars Tarkas look like? (Skin color, eyes, height, etc.)

[[SECTION markdown]]

# Tars Tarkas
**Role:** Martian Warrior / Ally

**Presence:** Physically Present

**Physical Description:** 
A Martian warrior who possesses physical prowess and commands respect.

**Uncertainty Notes:** 
Specific Martian physiological traits are not described in this text.
[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: sola

canonical_character_id: CH006 Sola

aliases: Martian Woman

is_fully_identified: false

manual_description_required: true

manual_description_reason: No physical description provided.

clarification_required: true

clarification_reason: Needs visual profile for character design.

clarification_question: What is Sola's appearance and clothing?

[[SECTION markdown]]

# Sola
**Role:** Martian Ally / Caretaker

**Presence:** Physically Present

**Physical Description:** 
A Martian woman characterized by compassion and solicitude toward the protagonist.

**Uncertainty Notes:** 
Visual identity (Martian features) is not established in this chapter.
[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: martian_warriors

canonical_character_id: CH007 Martian Warriors

aliases: Group of warriors

is_fully_identified: false

manual_description_required: true

manual_description_reason: They are a collective group with no individual descriptions.

clarification_required: false

clarification_reason: 

clarification_question: 

[[SECTION markdown]]

# Martian Warriors
**Role:** Supporting Group / Antagonists (briefly)

**Presence:** Physically Present

**Physical Description:** 
A group of warriors following Tars Tarkas. They are capable of combat and attempt to execute the watch-thing.

**Uncertainty Notes:** 
Individual appearances and armor/clothing details are unknown.
[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
