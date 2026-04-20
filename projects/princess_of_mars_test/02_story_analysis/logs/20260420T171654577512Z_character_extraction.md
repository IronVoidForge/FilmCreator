# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-20T17:16:54.577512+00:00
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

Chapter id: CH007

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

- keep one record per meaningful character mention

- prefer short facts over long prose

- if uncertain, use clarification_required instead of guessing

- if clarification is not required, still include clarification_reason and clarification_question as empty values

- still emit explicit character records; do not collapse them into index bullets only



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

### Setting
The chapter takes place across several Martian locations: the bustling plaza of a green Martian community, a massive procession traveling through valleys and hills, the desolate dead sea bottom, and a remote, high-security incubator site.

### Characters
* **The Narrator:** An Earthman learning to navigate Martian gravity and telepathic communication; possesses a unique mental immunity to Martian telepathy.
* **Sola:** A Martian female who serves as the narrator's guide and foster mother to a newly hatched Martian.
* **Tars Tarkas:** A prominent Martian warrior/chief.
* **Lorquance Ptomel, Jed:** An enormous and powerful Martian chieftain.
* **The Green Martians:** A community of warriors, women, and children characterized by their telepathic abilities and a culture of extreme survivalism.

### Key Events
* **The Great Harnessing:** The narrator witnesses the massive undertaking of harnessing enormous, mastodon-like animals to highly decorated, three-wheeled chariots for a great procession.
* **The Procession to the Incubator:** A large military-style cavalcade, including hundreds of warriors and outriders, travels to a remote incubator to witness a hatching event.
* **The Demonstration of Prowess:** To impress the Chieftain Lorquas Ptomel, the narrator performs a feat of incredible leaping, jumping over the parked chariots.
* **The Hatching Ritual:** The narrator observes the chaotic and ritualistic "capture" of newly hatched Martians as they emerge from an incubator and run through a gauntlet formed by women and children.
* **Martian Child-Rearing Customs:** The narrative explains the brutal Martian system of communal child-rearing, where offspring are raised for warfare and physical perfection, with any "defective" specimens promptly culled.
* **Telepathic Training:** Back at the city, Sola begins training the narrator in the Martian language and telepathy; during this process, it is revealed that while the narrator can receive telepathic messages, his own mind remains completely shielded from Martian intrusion.
````

## Raw Response
````text
[[FILMCREATOR_PACKET]]

task: character_extraction

version: 1

character_index_markdown:

[[SECTION character_index_markdown]]

* [The Narrator](#the-narrator)
* [Sola](#sola)
* [Tars Tarkas](#tars-tarkas)
* [Lorquance Ptomel](#lorquance-ptomel)
* [The Green Martians](#the-green-martians)

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: narrator

canonical_character_id: CH007 Narrator

aliases: Earthman, Narrator, Conscious Entity

is_fully_identified: false

manual_description_required: true

manual_description_reason: Physical appearance and clothing are not described.

clarification_required: false

clarification_reason: 

clarification_question: 

[[SECTION markdown]]

# The Narrator

**Role:** Earthman learning Martian gravity, language, and telepathy.

**Presence:** Physically present.

**Physical Description:** An Earthman; possesses a unique mental immunity to Martian telepathic intrusion, though he can receive messages.

**Prompt Phrases:** human male, Earthling, telepathically shielded mind, human traveler.

**Uncertainty Notes:** Physical features and attire are unknown.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: sola

canonical_character_id: CH007 Sola

aliases: 

is_fully_identified: false

manual_description_required: true

manual_description_reason: Physical appearance and costume are not described.

clarification_required: false

clarification_reason: 

clarification_question: 

[[SECTION markdown]]

# Sola

**Role:** Martian guide and foster mother to a newly hatched Martian.

**Presence:** Physically present.

**Physical Description:** A Martian female.

**Prompt Phrases:** Martian woman, green Martian, telepathic female.

**Uncertainty Notes:** Specific physical traits or clothing are not provided.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: tars_tarkas

canonical_character_id: CH007 Tars Tarkas

aliases: 

is_fully_identified: false

manual_description_required: true

manual_description_reason: Physical appearance is not detailed in this chapter.

clarification_required: false

clarification_reason: 

clarification_question: 

[[SECTION markdown]]

# Tars Tarkas

**Role:** Prominent Martian warrior and chief.

**Presence:** Physically present/referenced.

**Physical Description:** A Martian warrior/chief.

**Prompt Phrases:** Martian warrior, Martian chief, green Martian soldier.

**Uncertainty Notes:** Specific physical details or armor are not described.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: lorquance_ptomel

canonical_character_id: CH007 Lorquance Ptomel

aliases: Jed

is_fully_identified: false

manual_description_required: true

manual_description_reason: Only size and power are mentioned; specific features are missing.

clarification_required: false

clarification_reason: 

clarification_question: 

[[SECTION markdown]]

# Lorquance Ptomel

**Role:** Enormous and powerful Martian chieftain.

**Presence:** Physically present.

**Physical Description:** An enormous, powerful Martian.

**Prompt Phrases:** massive Martian, giant chieftain, powerful Martian warrior, enormous humanoid.

**Uncertainty Notes:** Specific facial features or costume details are unknown.

[[/SECTON]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: green_martians

canonical_character_id: CH007 Green Martians

aliases: 

is_fully_identified: false

manual_description_required: true

manual_description_reason: The group is described by role and ability rather than individual physical traits.

clarification_required: false

clarification_reason: 

clarification_question: 

[[SECTION markdown]]

# The Green Martians

**Role:** A community of warriors, women, and children.

**Presence:** Physically present.

**Physical Description:** A telepathic community characterized by extreme survivalism; includes warriors, women, and children.

**Prompt Phrases:** group of green Martians, telepathic Martian community, Martian warriors and families.

**Uncertainty Notes:** Individual physical characteristics for the group members are not specified beyond their species/culture.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
