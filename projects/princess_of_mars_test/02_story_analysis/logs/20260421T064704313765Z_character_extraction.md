# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-21T06:47:04.313765+00:00
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

Chapter id: CH002

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

**Setting:** A cave on a narrow cliff ledge in the Arizona mountains; later, the vast expanse of space.

**Characters:**
- **The Protagonist:** An experienced fighter who becomes paralyzed by a mysterious gas in a cave, only to undergo a supernatural transformation.
- **Apache Warriors:** A group of braves who approach the cave but flee in terror from an unseen moaning sound emanating from the cave's depths.
- **The Protagonist's Former Self:** A lifeless, clothed body left behind in the cave after the protagonist's consciousness/spirit separates and manifests as a naked entity.

**Events:**
- The protagonist is paralyzed by a pungent, tenuous vapor within a cave, rendering him unable to move despite remaining mentally alert.
- A group of Apache warriors approaches the cave; they are struck with awe and terror upon seeing the protagonist, but flee in panic when they hear a low moaning sound from the back of the cave.
- The protagonist's horse wanders off down the trail, leaving him isolated.
- At midnight, after hearing more mysterious sounds and rustling from the darkness, the protagonist exerts immense mental will to break his paralysis.
- Upon breaking free, the protagonist discovers he has undergone a metamorphosis: he is standing naked while his original, clothed body lies lifeless on the cave floor.
- Fearing the unseen entity in the shadows, the protagonist escapes the cave into the Arizona night.
- While gazing at the landscape and the red star of Mars, the protagonist feels an irresistible, magnetic pull toward the planet.
- The chapter concludes with the protagonist being violently drawn through the void of space.
````

## Raw Response
````text
[[FILMCREATOR_PACKET]]

task: character_extraction

version: 1

character_index_markdown:

[[SECTION character_index_markdown]]

# Character Index - CH002

- [protagonist](#protagonist)
- [apache_warriors](#apache_warriors)
- [former_self](#former_self)

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: protagonist

canonical_character_id: CH002 Protagonist

aliases: Naked Entity, Transformed Spirit

is_fully_identified: false

manual_description_required: true

manual_description_reason: Physical appearance of the transformed state is only described as "naked"; specific facial features, build, or age are not provided.

clarification_required: true

clarification_reason: The transition from the clothed body to the naked entity implies a change in physical form that needs definition for visual continuity.

clarification_question: What are the specific physical characteristics (age, build, hair, facial features) of the protagonist's transformed naked state?

[[SECTION markdown]]

# Protagonist

**Role:** Central character undergoing supernatural metamorphosis.

**Presence:** Physically present (as a naked entity).

**Physical Description:** 
Currently described only as a naked entity that has separated from its original body. The character is an experienced fighter.

**Costume/Silhouette:** 
Naked; no clothing or equipment is mentioned for the transformed state.

**Descriptive Noun Phrases:** 
Naked man, transformed entity, survivor of metamorphosis, celestial traveler.

**Uncertainty Notes:** 
The exact physical appearance of the protagonist's new form is unknown beyond its nudity and its separation from the original clothed body.
[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: apache_warriors

canonical_character_id: CH002 Apache Warriors

aliases: Braves

is_fully_identified: true

manual_description_required: false

manual_description_reason: 

clarification_required: false

clarification_reason: 

clarification_question: 

[[SECTION markdown]]

# Apache Warriors

**Role:** Group of observers/witnesses.

**Presence:** Physically present (approaching the cave).

**Physical Description:** 
A group of Apache braves. Specific individual features are not detailed.

**Costume/Silhouette:** 
Traditional Apache warrior attire (implied by context, though specific details are absent in this text).

**Descriptive Noun Phrases:** 
Apache warriors, group of braves, terrified warriors.

**Uncertainty Notes:** 
Specific visual details regarding their clothing or equipment are not explicitly provided in the text.
[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: former_self

canonical_character_id: CH002 Former Self

aliases: Clothed Body, Lifeless Body

is_fully_identified: true

manual_description_required: false

manual_description_reason: 

clarification_required: false

clarification_reason: 

clarification_question: 

[[SECTION markdown]]

# Former Self

**Role:** The discarded physical vessel of the protagonist.

**Presence:** Physically present (lying on the cave floor).

**Physical Description:** 
A lifeless, clothed body left behind in the cave.

**Costume/Silhouette:** 
Clothed; represents the protagonist's original state prior to metamorphosis.

**Descriptive Noun Phrases:** 
Lifeless body, discarded shell, clothed corpse, former physical form.

**Uncertainty Notes:** 
The specific type of clothing or the exact appearance of the body is not detailed beyond being "clothed."
[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
