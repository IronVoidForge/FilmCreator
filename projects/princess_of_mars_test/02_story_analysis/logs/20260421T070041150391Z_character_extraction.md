# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-21T07:00:41.150391+00:00
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

**Events:**
The protagonist joins Sola in a massive procession of decorated three-wheeled chariots drawn by enormous animals. The cavalcade travels across a valley and dead sea bottom to reach a remote incubator. Upon arrival, the chieftain Lorquas Ptomel and Tars Tarkas oversee the hatching process. The protagonist performs a feat of leaping over parked chariots to impress the leaders. As the young Martians emerge from the incubator, they are captured in a ritualistic gauntlet formed by women and youths. Following the ceremony, the community returns to their territory, having completed the cycle of transporting eggs from subterranean vaults to the incubator. The protagonist spends several days in idleness before beginning intensive training with Sola.

**Characters:**
- **The Protagonist:** An Earthman who has mastered Martian walking and is learning the language and telepathy; he discovers his mind is uniquely shielded from Martian telepathic reading.
- **Sola:** A female Martian who acts as a guide and foster mother to a newly hatched Martian child.
- **Tars Tarkas:** A Martian warrior/leader involved in the coordination of the hatching.
- **Lorquas Ptomel, Jed:** The enormous chieftain overseeing the incubator operations.
- **The Young Martian:** A physically perfect, four-foot-tall male captured by Sola, who becomes a rival to the protagonist during training.

**Settings:**
- **The Plaza/City:** The starting point of the journey, filled with chariots and community activity.
- **The Dead Sea Bottom:** A level expanse traversed during the procession.
- **The Incubator:** A remote, walled enclosure where Martian eggs are hatched by solar rays after five years of incubation.
- **The Martian Territory:** An arid/semi-arid region located between forty and eighty degrees south latitude, near the crossing of Martian canals.
````

## Raw Response
````text
[[FILMCREATOR_PACKET]]

task: character_extraction

version: 1

character_index_markdown:

[[SECTION character_index_markdown]]

# Character Index - CH007

- [Protagonist](#protagonist)
- [Sola](#sola)
- [Tars Tarkas](#tars-tarkas)
- [Lorquas Ptomel, Jed](#lorquas-ptomel-jed)
- [The Young Martian](#the-young-martian)

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: protagonist

canonical_character_id: CH001 Protagonist

aliases: Earthman

is_fully_identified: false

manual_description_required: true

manual_description_reason: Physical appearance, height, and specific clothing/gear are not described in this chapter.

clarification_required: true

clarification_reason: Needs physical profile for consistent rendering.

clarification_question: What is the protagonist's physical build and what does his Earthman attire look like in a Martian context?

[[SECTION markdown]]

# Protagonist
**Role:** Central Character / Observer

**Status:** Physically Present

**Physical Description:** 
An Earthman who has mastered the gait of Martian walking. He possesses a mind that is uniquely shielded from Martian telepathic reading.

**Costume/Silhouette:** 
Unknown (not described in this chapter).

**Descriptive Noun Phrases:** 
Telepathically shielded Earthman, agile traveler.

**Uncertainty Notes:** 
No visual details provided regarding facial features, hair, or specific clothing.
[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: sola

canonical_character_id: CH002 Sola

aliases: Guide, Foster Mother

is_fully_identified: false

manual_description_required: true

manual_description_reason: While identified as a female Martian, specific physical traits (skin color, eyes, height, clothing) are absent.

clarification_required: true

clarification_reason: Requires visual definition for Martian female phenotype.

clarification_question: What is Sola's physical appearance and what does her attire consist of?

[[SECTION markdown]]

# Sola
**Role:** Guide / Mentor figure

**Status:** Physically Present

**Physical Description:** 
A female Martian.

**Costume/Silhouette:** 
Unknown (not described in this chapter).

**Descriptive Noun Phrases:** 
Martian female guide, foster mother.

**Uncertainty Notes:** 
Specific Martian physical characteristics are not detailed in the text.
[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: tars_tarkas

canonical_character_id: CH003 Tars Tarkas

aliases: Martian Leader

is_fully_identified: false

manual_description_required: true

manual_description_reason: Identified as a warrior/leader, but no specific physical description is provided in this chapter.

clarification_required: true

clarification_reason: Needs visual confirmation of his warrior physique and armor/clothing.

clarification_question: What are the distinctive physical features and attire of Tars Tarkas?

[[SECTION markdown]]

# Tars Tarkas
**Role:** Martian Warrior / Leader

**Status:** Physically Present

**Physical Description:** 
A Martian leader involved in coordinating the hatching ceremony.

**Costume/Silhouette:** 
Unknown (not described in this chapter).

**Descriptive Noun Phrases:** 
Martian warrior, commanding leader.

**Uncertainty Notes:** 
Lacks specific visual descriptors for rendering.
[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: lorquas_ptomel_jed

canonical_character_id: CH004 Lorquas Ptomel, Jed

aliases: Chieftain

is_fully_identified: false

manual_description_required: true

manual_description_reason: Described as "enormous," but lacks specific facial features or clothing details.

clarification_required: false

clarification_reason: ""

clarification_question: ""

[[SECTION markdown]]

# Lorquas Ptomel, Jed
**Role:** Chieftain

**Status:** Physically Present

**Physical Description:** 
An enormous Martian chieftain overseeing incubator operations.

**Costume/Silhouette:** 
Unknown (not described in this chapter).

**Descriptive Noun Phrases:** 
Enormous Martian chieftain, ritual overseer.

**Uncertainty Notes:** 
Scale is known (enormous), but specific visual details are missing.
[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: young_martian

canonical_character_id: CH005 Young Martian

aliases: Rival

is_fully_identified: true

manual_description_required: false

manual_description_reason: ""

clarification_required: false

clarification_reason: ""

clarification_question: ""

[[SECTION markdown]]

# The Young Martian
**Role:** Rival to the Protagonist

**Status:** Physically Present

**Physical Description:** 
A physically perfect male Martian, approximately four feet tall.

**Costume/Silhouette:** 
Not explicitly described, but part of a ritualistic gauntlet involving women and youths.

**Descriptive Noun Phrases:** 
Physically perfect young Martian, four-foot-tall male.

**Uncertainty Notes:** 
None regarding height and physical perfection.
[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
