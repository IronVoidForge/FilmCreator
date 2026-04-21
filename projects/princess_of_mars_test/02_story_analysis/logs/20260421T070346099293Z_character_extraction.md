# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-21T07:03:46.099293+00:00
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

Chapter id: CH008

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

**Setting:** A deserted Martian city and its surrounding valleys/hills.

**Events:**
- As the green Martian procession prepares to return home, they are suddenly forced into hiding by the arrival of twenty large, gray-painted aerial vessels.
- A fierce battle erupts between the green Martians (utilizing high-precision ground fire from buildings) and the approaching fleet. The green warriors demonstrate highly disciplined targeting of specific ship components (guns, officers, steering gear).
- The Martian fleet is routed, with most ships retreating. One unmanned, damaged vessel drifts erratically toward the city.
- Green Martian warriors intercept the drifting craft, haul it to the ground using grappling hooks, and systematically loot it for weapons, jewels, and food/water.
- After looting, the warriors set the ship on fire, turning it into a floating funeral pyre that drifts away into the distance.
- The protagonist feels an unexpected sense of melancholy and kinship toward the defeated crew, hoping for their return to seek vengeance.
- While waiting in the city for the danger to pass, the protagonist spots the prisoner taken from the downed craft: a beautiful, slender, copper-skinned female with black hair, resembling an Earth woman in form.
- The female prisoner makes a silent sign toward the protagonist, seeking help; however, due to his ignorance of Martian customs, he fails to respond, leaving her to be dragged away in dejection.

**Characters:**
- **The Protagonist (Earthman):** Observes the battle from a window; experiences complex emotions regarding the destruction of the aerial crew.
- **Sola:** Accompanies the protagonist during the conflict.
- **Green Martian Warriors:** Highly disciplined, tactical, and ruthless combatants.
- **The Prisoner:** A beautiful, slender female with copper skin and black hair, captured from the aerial vessel; she appears more human-like than the green Martians.
- **Woola:** The protagonist's loyal hound.

**Key Themes/Motifs:** Technological warfare, biological disparity between Martian species, misunderstood communication, and the "funeral pyre" of a lost civilization.
````

## Raw Response
````text
[[FILMCREATOR_PACKET]]

task: character_extraction

version: 1

character_index_markdown:

[[SECTION character_index_markdown]]

# Character Index

- [Protagonist](#protagonist)
- [Sola](#sola)
- [Green Martian Warriors](#green-martian-warriors)
- [The Prisoner](#the-prisoner)
- [Woola](#woola)

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: protagonist

canonical_character_id: CH002 Protagonist

aliases: Earthman

is_fully_identified: false

manual_description_required: true

manual_description_reason: Physical appearance and specific clothing/gear are not described in this chapter.

clarification_required: true

clarification_reason: Identity and physical form need confirmation for visual consistency.

clarification_question: What is the protagonist's physical appearance, age, and current attire?

[[SECTION markdown]]

# Protagonist

**Role:** Observer / POV Character

**Presence:** Physically present (observing from a window).

**Physical Description:** Not described in this chapter; identified as an "Earthman."

**Costume/Silhouette:** Unknown.

**Descriptive Noun Phrases:** Earthman, observer, empathetic witness.

**Uncertainty Notes:** Visual details are entirely absent in this text segment.

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: sola

canonical_character_id: CH003 Sola

aliases: 

is_fully_identified: false

manual_description_required: true

manual_description_reason: No physical description provided in the text.

clarification_required: true

clarification_reason: Needs visual profile.

clarification_question: What does Sola look like and what is her relationship to the protagonist?

[[SECTION markdown]]

# Sola

**Role:** Companion

**Presence:** Physically present (accompanying the protagonist).

**Physical Description:** Unknown.

**Costume/Silhouette:** Unknown.

**Descriptive Noun Phrases:** Companion, witness.

**Uncertainty Notes:** Character is mentioned as being present but lacks any visual descriptors.

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: green_martian_warriors

canonical_character_id: CH004 Green Martian Warriors

aliases: Green Martians, warriors

is_fully_identified: true

manual_description_required: false

manual_description_reason: 

clarification_required: false

clarification_reason: 

clarification_question: 

[[SECTION markdown]]

# Green Martian Warriors

**Role:** Combatants / Aggressors

**Presence:** Physically present (engaging in battle and looting).

**Physical Description:** Described as "green" warriors. Highly disciplined and tactical.

**Costume/Silhouette:** Not explicitly detailed, but they utilize grappling hooks and high-precision ground fire.

**Descriptive Noun Phrases:** Green warriors, disciplined combatants, tactical Martian fighters.

**Uncertainty Notes:** Specific armor or clothing details are not provided.

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: female_prisoner

canonical_character_id: CH005 Female Prisoner

aliases: The Prisoner

is_fully_identified: true

manual_description_required: false

manual_description_reason: 

clarification_required: false

clarification_reason: 

clarification_question: 

[[SECTION markdown]]

# The Prisoner

**Role:** Captured victim / Catalyst for emotional beat

**Presence:** Physically present (captured from the downed vessel).

**Physical Description:** Beautiful, slender, copper-skinned female with black hair. Resembles an Earth woman in form.

**Costume/Silhouette:** Not described; appears as a prisoner.

**Descriptive Noun Phrases:** Copper-skinned female, slender Earth-like woman, black-haired prisoner.

**Uncertainty Notes:** None regarding her basic physical traits.

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: woola

canonical_character_id: CH006 Woola

aliases: Hound

is_fully_identified: true

manual_description_required: false

manual_description_reason: 

clarification_required: false

clarification_reason: 

clarification_question: 

[[SECTION markdown]]

# Woola

**Role:** Companion / Pet

**Presence:** Physically present.

**Physical Description:** A loyal hound.

**Costume/Silhouette:** Not described.

**Descriptive Noun Phrases:** Loyal hound, Martian dog.

**Uncertainty Notes:** Specific breed or size is not specified in this chapter.

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
