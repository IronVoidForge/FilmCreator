# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-20T17:06:04.959913+00:00
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

**Setting:** A chamber within a Martian building, near a window overlooking a plaza.

**Characters:**
* **The Narrator:** An Earthman who uses both primitive weapons and Earthly boxing tactics to survive.
* **The Watch-thing:** The narrator's loyal, multi-legged, monstrous pet/guardian.
* **The Ape-creatures:** Two massive (10-15ft tall), four-armed, gorilla-like beings with high physical strength.
* **Tars Tarkas:** A Martian warrior who observes the narrator's combat.
* **Sola:** A Martian woman who shows compassion and concern for the narrator.
* **Martian Warriors:** A group of onlookers who value physical prowess and witness the fight.

**Events:**
1. **The Initial Capture:** The narrator is pinned to the ground by one of the massive, ape-like creatures while its mate approaches with a stone cudgel to kill him.
2. **The First Battle:** The narrator's "watch-thing" attacks the second ape to save the narrator. A brutal struggle ensues between the two beasts; the watch-thing is severely wounded and nearly choked to death by the ape's immense strength.
3. **The Narrator's Intervention:** Driven by loyalty to his pet, the narrator uses a fallen cudgel to crush the skull of the first ape. 
4. **The Second Battle:** The mate of the deceased ape returns in a rage. The narrator initially considers fleeing but chooses to stay and defend his wounded beast. Using Earthly boxing techniques—specifically punches to the chin and stomach—the narrator manages to knock the creature off balance and finish it with the cudgel.
5. **The Arrival of Allies:** Tars Tarkas, Sola, and a group of warriors arrive, having witnessed the fight. They are impressed by the narrator's combat skill, though their reaction is rooted more in admiration of his strength than true friendship.
6. **An Act of Compassion:** A Martian warrior attempts to execute the wounded watch-thing with a pistol. The narrator intervenes, physically stopping the warrior's arm and preventing the shot. This act of mercy confuses the Martians but solidifies the narrator's bond with both Sola and his loyal beast.
````

## Raw Response
````text
[[FILMCREATOR_PACKET]]

task: character_extraction

version: 1

character_index_markdown:

[[SECTION character_index_markdown]]

# Character Index

* [The Narrator](#the-narrator)
* [The Watch-thing](#the-watch-thing)
* [Ape-creatures](#ape-creatures)
* [Tars Tarkas](#tars-tarkas)
* [Sola](#sola)
* [Martian Warriors](#martian-warriors)

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: narrator

canonical_character_id: CH006 Narrator

aliases: Earthman

is_fully_identified: false

manual_description_required: true

manual_description_reason: No specific physical features, facial details, or clothing descriptions are provided beyond his origin as an Earthman.

clarification_required: true

clarification_reason: Physical appearance and attire are unknown.

clarification_question: What is the narrator's physical build, facial features, and what is he wearing?

[[SECTION markdown]]

# The Narrator

**Role:** Protagonist / Combatant

**Presence:** Physically present.

**Description:** An Earthman capable of using both primitive weapons (cudgel) and Earthly boxing techniques (punches to the chin and stomach). 

**Uncertainty Notes:** Physical appearance, height, and clothing are entirely unstated in this chapter.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: watch_thing

canonical_character_id: CH006 Watch-thing

aliases: pet, guardian

is_fully_identified: true

manual_description_required: false

manual_description_reason: ""

clarification_required: false

clarification_reason: ""

clarification_question: ""

[[SECTION markdown]]

# The Watch-thing

**Role:** Loyal Pet / Guardian

**Presence:** Physically present.

**Description:** A multi-legged, monstrous creature. 

**Continuity Notes:** Severely wounded during the struggle with the ape-creature; nearly choked to death.

**Prompt Phrases:** Multi-legged monster, alien pet, wounded beast.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: ape_creature

canonical_character_id: CH006 Ape-creature

aliases: gorilla-like beings

is_fully_identified: true

manual_description_required: false

manual_description_reason: ""

clarification_required: false

clarification_reason: ""

clarification_question: ""

[[SECTION markdown]]

# Ape-creatures

**Role:** Antagonists / Aggressors

**Presence:** Physically present.

**Description:** Massive, 10-15ft tall beings with four arms and a gorilla-like appearance. They possess immense physical strength and use stone cudgels.

**Prompt Phrases:** 15ft tall ape-man, four-armed gorilla creature, massive primate humanoid.

[[/

]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: tars_tarkas

canonical_character_id: CH006 Tars Tarkas

aliases: Martian warrior

is_fully_identified: false

manual_description_required: true

manual_description_reason: Identified only by role; no physical description or costume details provided.

clarification_required: true

clarification_reason: Needs visual identification for rendering.

clarification_question: What does Tars Tarkas look like physically, and what is his Martian attire?

[[SECTION markdown]]

# Tars Tarkas

**Role:** Observer / Ally

**Presence:** Physically present.

**Description:** A Martian warrior who observes the narrator's combat prowess.

**Uncertainty Notes:** Physical appearance and specific gear are unknown.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: sola

canonical_character_id: CH006 Sola

aliases: Martian woman

is_fully_identified: false

manual_description_required: true

manual_description_reason: No physical description or clothing details provided.

clarification_required: true

clarification_reason: Needs visual identification for rendering.

clarification_question: What are Sola's physical features and what is she wearing?

[[SECTION markdown]]

# Sola

**Role:** Ally / Compassionate Observer

**Presence:** Physically present.

**Description:** A Martian woman who exhibits compassion and concern for the narrator.

**Uncertainty Notes:** Physical appearance and costume are unstated.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: martian_warriors

canonical_character_id: CH006 Martian Warriors

aliases: onlookers

is_fully_identified: false

manual_description_required: true

manual_description_reason: No specific physical or uniform details provided for the group.

clarification_required: true

clarification_reason: Visuals for the group/uniforms are missing.

clarification_question: What is the standard appearance or armor of the Martian warriors?

[[SECTION markdown]]

# Martian Warriors

**Role:** Onlookers / Witnesses

**Presence:** Physically present (group).

**Description:** A group of Martians who witness the fight and value physical prowess. One warrior attempts to execute the wounded watch-thing with a pistol.

**Uncertainty Notes:** Specifics on their numbers, armor, or weaponry (beyond the pistol) are not detailed.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
