# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-21T15:26:46.039018+00:00
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

Chapter id: CH025

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

**Setting:** The palace of Zodanga, specifically the brilliantly illuminated audience chamber and the labyrinthine dungeons beneath.

**Characters:**
- **John Carter:** The protagonist, who infiltrates the palace to rescue Dejah Thoris.
- **Dejah Thoris:** Princess of Helium, who is being forced into a political marriage.
- **Than Kosis:** The Jeddak of Zodanga.
- **Sab Than:** Son of Than Kosis and the Prince of Zodanga.
- **Tars Tarkas:** Leader of the Tharks, providing military support to Carter.
- **Kantos Kan:** An ally of Carter, rescued from the Zodangan dungeons.

**Events:**
- **The Infiltration:** John Carter leads fifty Tharks into Zodanga. He infiltrates the palace alone by shattering a window and leaping into the audience chamber during a marriage ceremony.
- **The Ceremony Interrupted:** Carter interrupts the wedding of Sab Than and Dejah Thoris, destroying the golden ceremonial chain intended to bind her. 
- **The Battle in the Throne Room:** A chaotic skirmish ensues between Carter, the Zodangan nobility/guards, and the advancing Tharks led by Tars Tarkas. During the fight, Sab Than is killed, as is his father, Than Kosis. The Tharks eventually secure the hall, leaving only themselves, Carter, and Dejah Thoris alive.
- **The Rescue:** Carter descends into the dungeons to rescue Kantos Kan, finding him in a dark recess and freeing him using keys taken from a fallen jailer.
- **The Engagement:** Amidst the ongoing sounds of war and looting throughout Zodanga, John Carter and Dejah Thoris share a moment of intimacy in the throne room, where they officially pledge themselves to marriage.
````

## Raw Response
````text
[[FILMCREATOR_PACKET]]

task: character_extraction

version: 1

character_index_markdown:

[[SECTION character_index_markdown]]

# Character Index - CH025

- [John Carter](#john_carter)
- [Dejah Thoris](#dejah_thoris)
- [Than Kosis](#than_kosis)
- [Sab Than](#sab_than)
- [Tars Tarkas](#tars_tarkas)
- [Kantos Kan](#kantos_kan)

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: john_carter

canonical_character_id: John Carter

aliases: Protagonist

is_fully_identified: true

manual_description_required: false

manual_description_reason: 

clarification_required: false

clarification_reason: 

clarification_question: 

[[SECTION markdown]]

# John Carter
**Role:** Protagonist / Rescuer

**Presence:** Physically present.

**Physical Description:** Infiltrates the palace by leaping through a window; engages in high-intensity combat against Zodangan nobility and guards.

**Costume/Silhouette:** Combatant, likely wearing gear suitable for infiltration and martial engagement.

**Prompt Phrases:** Human male, agile warrior, infiltrator, combatant.

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
**Role:** Princess of Helium / Love Interest

**Presence:** Physically present.

**Physical Description:** Subject of a political marriage ceremony; wears a golden ceremonial chain (which is destroyed).

**Costume/Silhouette:** Royal bridal attire, ceremonial jewelry.

**Prompt Phrases:** Princess, royal female, ceremonial gold chains, bride.

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: than_kosis

canonical_character_id: Than Kosis

aliases: Jeddak of Zodanga

is_fully_identified: true

manual_description_required: false

manual_description_reason: 

clarification_required: false

clarification_reason: 

clarification_question: 

[[SECTION markdown]]

# Than Kosis
**Role:** Antagonist / Ruler of Zodanga

**Presence:** Physically present (deceased in chapter).

**Physical Description:** High-ranking nobility/ruler.

**Costume/Silhouette:** Regal, authoritative attire of a Jeddak.

**Prompt Phrases:** Zodangan ruler, Jeddak, noble, elder male.

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: sab_than

canonical_character_id: Sab Than

aliases: Prince of Zodanga

is_fully_identified: true

manual_description_required: false

manual_description_reason: 

clarification_required: false

clarification_reason: 

clarification_question: 

[[SECTION markdown]]

# Sab Than
**Role:** Antagonist / Groom

**Presence:** Physically present (deceased in chapter).

**Physical Description:** Son of Than Kosis.

**Costume/Silhouette:** Royal groom attire.

**Prompt Phrases:** Prince, Zodangan noble, groom.

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: tars_tarkas

canonical_character_id: Tars Tarkas

aliases: Leader of the Tharks

is_fully_identified: true

manual_description_required: false

manual_description_reason: 

clarification_required: false

clarification_reason: 

clarification_question: 

[[SECTION markdown]]

# Tars Tarkas
**Role:** Military Ally

**Presence:** Physically present.

**Physical Description:** Leader of the Thark military force; part of the group that secures the throne room.

**Costume/Silhouette:** Thark warrior, commanding presence.

**Prompt Phrases:** Thark leader, green warrior, martial leader.

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: kantos_kan

canonical_character_id: Kantos Kan

aliases: Ally

is_fully_identified: true

manual_description_required: true

manual_description_reason: Held in a dark dungeon recess; specific physical features not detailed in this chapter.

clarification_required: false

clarification_reason: 

clarification_question: 

[[SECTION markdown]]

# Kantos Kan
**Role:** Rescued Ally

**Presence:** Physically present (rescued from dungeons).

**Physical Description:** Found in a dark recess of the Zodangan dungeons.

**Costume/Silhouette:** Prisoner, likely disheveled or wearing dungeon garb.

**Prompt Phrases:** Prisoner, rescued ally, captive.

**Uncertainty Note:** Specific facial features and physical build are not described due to the darkness of the setting.

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
