# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-20T17:14:58.016498+00:00
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

# Character Index

- [Narrator](#narrator)
- [Sola](#sola)
- [Tars Tarkas](#tars_tarkas)
- [Lorquance Ptomel](#lorquance_ptomel)
- [Green Martians](#green_martians)

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: narrator

canonical_character_id: CH007 Narrator

aliases: Earthman

is_fully_identified: false

manual_description_required: true

manual_description_reason: Only identified as an "Earthman"; lacks specific physical features, facial details, or clothing.

clarification_required: true

clarintication_question: What are the narrator's specific physical characteristics and what is he wearing?

[[SECTION markdown]]
# Narrator
**Role:** Protagonist / Observer

**Status:** Physically Present

**Description:**
An Earthman navigating Martian gravity. He possesses a unique mental immunity to Martian telepathy, though he can receive messages. 

**Uncertainty Notes:**
Physical appearance and attire are entirely unknown.
[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: sola

canonical_character_id: CH007 Sola

aliases: []

is_fully_identified: false

manual_description_required: true

manual_description_reason: No physical description or costume details provided.

clarification_required: true

clarification_question: What does Sola look like physically?

[[SECTION markdown]]
# Sola
**Role:** Guide / Foster Mother

**Status:** Physically Present

**Description:**
A Martian female who serves as the narrator's guide and acts as a foster mother to a newly hatched Martian.

**Uncertainty Notes:**
No visual details regarding her anatomy, skin color, or clothing are available.
[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: tars_tarkas

canonical_character_id: CH007 Tars Tarkas

aliases: []

is_fully_identified: false

manual_description_required: true

manual_description_reason: No physical description provided in the text.

clarification_required: true

clarification_question: What are the visual characteristics of Tars Tarkas?

[[SECTION markdown]]
# Tars Tarkas
**Role:** Martian Warrior/Chief

**Status:** Physically Present (referenced as part of procession)

**Description:**
A prominent Martian warrior and chief.

**Uncertainty Notes:**
Physical appearance, weaponry, or armor details are missing.
[[SECTON]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: lorquance_ptomel

canonical_character_id: CH007 Lorquance Ptomel

aliases: []

is_fully_identified: false

manual_description_required: true

manual_description_reason: Described only by scale ("enormous") and status, lacking specific visual traits.

clarification_required: true

clarification_question: What are the specific physical features and attire of Lorquance Ptomel?

[[SECTION markdown]]
# Lorquance Ptomel
**Role:** Martian Chieftain

**Status:** Physically Present (referenced during procession)

**Description:**
An enormous and powerful Martian chieftain.

**Uncertainty Notes:**
While "enormous" provides a scale hint, specific facial features, skin texture, or clothing are unknown.
[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: green_martians

canonical_character_id: CH007 Green Martians

aliases: []

is_fully_identified: false

manual_description_required: true

manual_description_reason: The group is defined by behavior and ability, but lacks specific visual/costume descriptors.

clarification_required: true

clarification_question: What are the defining physical traits or characteristic clothing of the Green Martian community?

[[SECTION markdown]]
# Green Martians
**Role:** Community / Collective

**Status:** Physically Present (as a group)

**Description:**
A community of warriors, women, and children characterized by telepathic abilities and extreme survivalism. They participate in ritualistic hatching events.

**Uncertainty Notes:**
Specific visual markers for the species (beyond the name "Green") or their cultural attire are not detailed.
[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
