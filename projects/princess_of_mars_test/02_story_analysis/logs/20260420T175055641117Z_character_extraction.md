# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-20T17:50:55.641117+00:00
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

Chapter id: CH009

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
The protagonist undergoes a period of rapid adaptation, receiving Martian warrior attire and training in various weapons under the instruction of Sola and other females. He learns that Green Martian society is divided by gendered roles: women are the artisans, manufacturers, and defenders, while men focus on high-level strategy and law. Driven by curiosity regarding a beautiful Red female prisoner he witnessed being treated brutally, the protagonist pushes himself to master the Martian language. Through eavesdropping on a late-night conversation among the women in his sleeping quarters, he learns that the prisoner is destined to be taken to Thark to die in public games. A heated argument breaks out between Sola and Sarkoja; Sola expresses sympathy for the captive, which the others view as a sign of weakness and "atavism." This interaction confirms Sola's compassionate nature and motivates the protagonist to plan an eventual escape with her help.

**Characters:**
- **The Protagonist:** An Earthman learning Martian combat and language; determined to find his own kind.
- **Sola:** A Green Martian female who acts as a mentor/guardian to the protagonist; shows unexpected empathy for the Red prisoner, defying social norms.
- **Sarkoja:** An older, more hardened Green Martian woman; critical of Sola's perceived weakness.
- **The Prisoner:** A beautiful "Red" Martian woman being held for public execution.
- **The Women (Group):** Artisans and warriors who manage the domestic and manufacturing aspects of their society.

**Settings:**
- **The Plaza/Training Grounds:** Where the protagonist practices combat with the Martian youth.
- **The Sleeping Quarters:** A communal living space shared by several females, young Martians, the protagonist, Sola, and Woola the hound; the site of the pivotal overheard conversation.
````

## Raw Response
````text
[[FILMCREATOR_PACKET]]

task: character_extraction

version: 1

character_index_markdown:

[[SECTION character_index_markdown]]

# Character Index - CH009

- [Protagonist](#protagonist)
- [Sola](#sola)
- [Sarkoja](#sarkoja)
- [The Prisoner](#the-prisoner)
- [The Women (Group)](#the-women-group)

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: protagonist

canonical_character_id: CH002 Protagonist

aliases: Earthman

is_fully_identified: false

manual_description_required: true

manual_description_reason: Physical appearance and specific clothing details beyond "Martian warrior attire" are not provided.

clarification_required: true

clarification_reason: Needs physical description for consistent rendering.

clarification_question: What is the protagonist's hair color, eye color, build, and facial features?

[[SECTION markdown]]

# Protagonist
**Role:** Learner/Outsider

**Status:** Physically Present

**Physical Description:** 
An Earthman currently wearing Martian warrior attire. He is undergoing physical training in combat and weapons.

**Costume/Silhouette:** 
Martian warrior clothing (specific details unstated).

**Descriptive Noun Phrases:** 
Earthman, trainee, martial student, outsider.

**Uncertainty Notes:** 
Specific facial features and exact appearance of the "warrior attire" are unknown.

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: sola

canonical_character_id: CH005 Sola

aliases: Mentor, Guardian

is_fully_identified: false

manual_description_required: true

manual_description_reason: While identified as a Green Martian female, specific physical features (height, hair, skin tone nuances) are missing.

clarification_required: true

clarification_reason: Needs visual details to distinguish from other Green Martian females.

clarification_question: What are Sola's specific physical characteristics?

[[SECTION markdown]]

# Sola
**Role:** Mentor/Guardian

**Status:** Physically Present

**Physical Description:** 
A Green Martian female. Characterized by a compassionate and empathetic nature that deviates from her society's norms.

**Costume/Silhouette:** 
Green Martian attire (implied warrior or artisan class).

**Descriptive Noun Phrases:** 
Green Martian female, compassionate mentor, empathetic guardian.

**Uncertainty Notes:** 
Specific physical traits of the Green Martian species are not detailed in this chapter.

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: sarkoja

canonical_character_id: CH012 Sarkoja

aliases: 

is_fully_identified: false

manual_description_required: true

manual_description_reason: Described only as "older" and "hardened"; lacks specific visual markers.

clarification_required: true

clarification_reason: Needs physical description to differentiate from Sola.

clarification_question: What does Sarkoja look like? (Age markers, facial features, etc.)

[[SECTION markdown]]

# Sarkoja
**Role:** Antagonist/Social Critic

**Status:** Physically Present

**Physical Description:** 
An older, hardened Green Martian woman. She represents the strict social norms of her people and views empathy as weakness.

**Costume/Silhouette:** 
Green Martian attire.

**Descriptive Noun Phrases:** 
Hardened Green Martian, elder female, traditionalist.

**Uncertainty Notes:** 
Visual details are limited to age and temperament.

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: red_prisoner

canonical_character_id: CH015 Red Prisoner

aliases: Beautiful Red female, Captive

is_fully_identified: false

manual_description_required: true

manual_description_reason: Described only as "beautiful" and a "Red" Martian; no specific features provided.

clarification_required: true

clarification_reason: Needs specific physical description of the "Red" Martian phenotype.

clarification_question: What are the defining visual characteristics of a "Red" Martian woman?

[[SECTION markdown]]

# The Prisoner
**Role:** Victim/Catalyst

**Status:** Referenced (Witnessed previously)

**Physical Description:** 
A beautiful female from the Red Martian race.

**Costume/Silhouette:** 
Prisoner status (details unknown).

**Descriptive Noun Phrases:** 
Red Martian woman, beautiful captive, prisoner of war.

**Uncertainty Notes:** 
Specifics of "Red" Martian appearance and her current state of captivity are not detailed.

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: green_martian_women_group

canonical_character_id: CH020 Green Martian Women

aliases: The Women, Artisans, Defenders

is_fully_identified: false

manual_description_required: true

manual_description_reason: They are a collective group without individual visual identities provided.

clarification_required: false

clarification_reason: 

clarification_question: 

[[SECTION markdown]]

# The Women (Group)
**Role:** Society/Background Characters

**Status:** Physically Present (as a group)

**Physical Description:** 
Green Martian females who serve as the artisans, manufacturers, and defenders of their society.

**Costume/Silhouette:** 
Varies between artisan and warrior attire.

**Descriptive Noun Phrases:** 
Martian female collective, Green Martian artisans, Martian warriors.

**Uncertainty Notes:** 
Individual identities are not established; they function as a social unit in this chapter.

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
