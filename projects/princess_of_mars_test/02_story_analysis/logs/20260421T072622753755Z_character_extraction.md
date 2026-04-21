# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-21T07:26:22.753755+00:00
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

Chapter id: CH013

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

**Setting:** The city of Lorquas Ptomel and its surrounding plazas; the Martian night under two moons.

**Characters:**
- **John Carter:** An Earthman integrated into Thark culture, currently training in Martian warfare.
- **Tars Tarkas:** A Thark warrior leader.
- **Dejah Thoris:** A high-born red Martian princess.
- **Sola:** Dejah Thoris' companion.
- **Lorquas Ptomel:** A Thark leader/chieftain.

**Events:**
- **Thoat Training:** Following a battle with airships, the community remains in the city for safety. John Carter spends his time learning to ride and command thoats (large Martian beasts). Unlike the Tharks who use force, Carter uses a combination of authority and kindness to tame them. His success is so profound that he teaches Tars Tarkas and other warriors his methods, resulting in more docile mounts and earning him a gold anklet from Lorquas Ptomel.
- **The Departure:** After seven days, the community prepares to march toward Thark. 
- **Meeting Dejah Thoris:** Carter manages to secure a private moment with Dejah Thoris by sending Sola away on an errand. They discuss the interference of the Thark women, who have been forcing Dejah Thoris into arduous labor (mixing radium-based explosives) to keep her away from Carter.
- **Martian Warfare Insight:** Dejah Thoris explains the mechanics of Martian explosive projectiles, which detonate upon contact with sunlight.
- **Romantic Development:** Dejah Thoris reveals her respect for Carter, calling him "my chieftain," a term of great significance he does not yet fully grasp. As they walk together under the Martian moons, Carter realizes the depth of his love for her, solidified by their silent, intimate physical proximity.
````

## Raw Response
````text
[[FILMCREATOR_PACKET]]

task: character_extraction

version: 1

character_index_markdown:

[[SECTION character_index_markdown]]

# Character Index - Chapter CH013

- [john_carter](#john_carter)
- [tars_tarkas](#tars_tarkas)
- [dejah_thoris](#dejah_thoris)
- [sola](#sola)
- [lorquas_ptomel](#lorquas_ptomel)

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: john_carter

canonical_character_id: CH001 John Carter

aliases: Earthman, Chieftain (honorific)

is_fully_identified: true

manual_description_required: false

manual_description_reason: 

clarification_required: false

clarification_reason: 

clarification_question: 

[[SECTION markdown]]

# John Carter
**Role:** Protagonist, Earthman integrated into Thark culture.
**Presence:** Physically present.
**Physical Description:** An Earthman capable of taming Martian thoats through authority and kindness rather than brute force.
**Costume/Traits:** Wears a gold anklet gifted by Lorquas Ptomel.
**Prompt Phrases:** Earthman, martial training, commanding presence, gold anklet.
[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: tars_tarkas

canonical_character_id: CH003 Tars Tarkas

aliases: Thark warrior leader

is_fully_identified: true

manual_description_required: false

manual_description_reason: 

clarification_required: false

clarification_reason: 

clarification_question: 

[[SECTION markdown]]

# Tars Tarkas
**Role:** Thark warrior leader.
**Presence:** Physically present (referenced as training with Carter).
**Physical Description:** A Thark warrior; learns new methods of thoat riding from Carter.
**Prompt Phrases:** Thark warrior, Martian leader, martial trainer.
[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: dejah_thoris

canonical_character_id: CH004 Dejah Thoris

aliases: Princess, High-born red Martian

is_fully_identified: true

manual_description_required: false

manual_description_reason: 

clarification_required: false

clarification_reason: 

clarification_question: 

[[SECTION markdown]]

# Dejah Thoris
**Role:** High-born red Martian princess.
**Presence:** Physically present.
**Physical Description:** Red Martian; high-born status.
**Costume/Traits:** Involved in labor mixing radium-based explosives (contextual).
**Prompt Phrases:** Red Martian princess, high-born, noble silhouette.
[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: sola

canonical_character_id: CH005 Sola

aliases: Dejah Thoris' companion

is_fully_identified: true

manual_description_required: true

manual_description_reason: No specific physical or costume details provided in this chapter.

clarification_required: false

clarification_reason: 

clarification_question: 

[[SECTION markdown]]

# Sola
**Role:** Companion to Dejah Thoris.
**Presence:** Physically present (sent on errand).
**Physical Description:** Unknown physical details provided in this chapter.
**Prompt Phrases:** Martian companion, female attendant.
**Uncertainty Note:** Physical appearance and attire are not described in this text.
[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: lorquas_ptomel

canonical_character_id: CH006 Lorquas Ptomel

aliases: Thark chieftain

is_fully_identified: true

manual_description_required: true

manual_description_reason: No specific physical or costume details provided in this chapter.

clarification_required: false

clarification_reason: 

clarification_question: 

[[SECTION markdown]]

# Lorquas Ptomel
**Role:** Thark leader/chieftain.
**Presence:** Referenced (gifted the gold anklet).
**Physical Description:** Unknown physical details provided in this chapter.
**Prompt Phrases:** Thark chieftain, Martian leader.
**Uncertainty Note:** Physical appearance and attire are not described in this text.
[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
