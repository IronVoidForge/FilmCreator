# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-26T07:12:42.474401+00:00
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

Chapter id: CH028

Task: extract visible and referenced characters into a character index plus one Markdown file per character.

Packet contract:
- task: character_extraction
- version: 1
- first line: [[FILMCREATOR_PACKET]]
- last line: [[/FILMCREATOR_PACKET]]
- required sections: character_index_markdown
- record type character: fields=asset_id, canonical_character_id, aliases, is_fully_identified, manual_description_required, manual_description_reason, clarification_required, clarification_reason, clarification_question, character_type_hint, morphology_hint, scale_hint, renderability_hint, confidence, direct_identity_evidence, direct_visual_evidence, costume_or_covering_evidence, movement_evidence, associated_entities, alias_or_role_evidence, unknowns, source_refs sections=markdown



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

character_type_hint: unknown

morphology_hint: unknown

scale_hint: unknown

renderability_hint: unknown

confidence: 0.3



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

**Setting:** An Arizona cave (Earth) and a study overlooking the Hudson River (Earth).

**Characters:**
- **John Carter:** The protagonist, now living on Earth.
- **The Mummified Woman:** A deceased figure found in the cave.
- **Dejah Thoris (Mentioned):** Carter's lost love on Mars.
- **A Little Boy and a "Hideous Creature" (Visionary/Imagined):** Seen by Carter in a vision of his potential future or reunion.

**Events:**
- John Carter awakens in a dark cave in Arizona, clothed in strange garments that crumble upon movement.
- He discovers the mummified remains of an old woman tending a charcoal burner with green powder, surrounded by hanging human skeletons.
- Upon exiting the cave, Carter realizes he is back on Earth, looking out over the Arizona landscape.
- A temporal jump occurs: Carter reflects on the twenty years that have passed since his return to Earth. He has become wealthy from an untouched mine but remains consumed by longing for Mars and Dejah Thoris.
- In his study by the Hudson, Carter experiences a vision or profound feeling while looking at Mars through his window, sensing that Dejah Thoris and a child are waiting for him across space.
````

## Raw Response
````text
[[FILMCREATOR_PACKET]]

task: character_extraction

version: 1

character_index_markdown:

[[SECTION character_index_markdown]]

# Character Index - CH028

- [john_carter](#john_carter)
- [mummified_woman](#mummified_woman)
- [dejah_thoris](#dejah_thoris)
- [little_boy](#little_boy)
- [hideous_creature](#hideous_creature)

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

character_type_hint: human

morphology_hint: adult male

scale_hint: human scale

renderability_hint: high

confidence: 1.0

direct_identity_evidence: Explicitly named as John Carter.

direct_visual_evidence: Present in cave and study.

costume_or_covering_evidence: Wears strange garments that crumble; later seen in a study by the Hudson.

movement_evidence: Awakens, moves through cave, exits, reflects on 20 years.

associated_entities: Dejah Thoris, Mummified Woman

alias_or_role_evidence: Protagonist

unknowns: 

source_refs: Chapter 28 summary

[[SECTION markdown]]

# John Carter
**Role:** Protagonist

**Status:** Physically Present

**Physical Description:** Adult male. Has lived on Earth for twenty years since his return.

**Costume/Silhouette:** Initially wears strange, crumbling garments in the cave; later depicted as a wealthy man in a study overlooking the Hudson River.

**Prompting Phrases:** Wealthy man, contemplative, looking through window at Mars, survivor of Mars.

**Uncertainty Notes:** Specific facial features not detailed in this chapter.
[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: mummified_woman

canonical_character_id: The Mummified Woman

aliases: Old woman

is_fully_identified: true

manual_description_required: false

manual_description_reason: 

clarification_required: false

clarification_reason: 

clarification_question: 

character_type_hint: human (deceased)

morphology_hint: mummified female

scale_hint: human scale

renderability_hint: medium

confidence: 0.9

direct_identity_evidence: Described as a mummified old woman.

direct_visual_evidence: Found in the Arizona cave.

costume_or_covering_evidence: Not specified beyond being mummified.

movement_evidence: None (deceased).

associated_entities: John Carter

alias_or_role_evidence: Tending a charcoal burner with green powder.

unknowns: 

source_refs: Chapter 28 summary

[[SECTION markdown]]

# The Mummified Woman
**Role:** Deceased figure found in cave

**Status:** Physically Present (as remains)

**Physical Description:** An old, mummified woman.

**Costume/Silhouette:** Mummified remains.

**Prompting Phrases:** Mummified corpse, ancient remains, skeletal, desert cave dweller.

**Uncertainty Notes:** Exact state of preservation or clothing is unknown.
[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: dejah_thoris

canonical_character_id: Dejah Thoris

aliases: Lost love

is_fully_identified: true

manual_description_required: false

manual_description_reason: 

clarification_required: false

clarification_reason: 

clarification_question: 

character_type_hint: alien (Martian)

morphology_hint: female

scale_hint: human scale

renderability_hint: low

confidence: 0.8

direct_identity_evidence: Named as Dejah Thoris.

direct_visual_evidence: None (referenced/visionary).

costume_or_covering_evidence: None.

movement_evidence: None.

associated_entities: John Carter

alias_or_role_evidence: Carter's lost love on Mars.

unknowns: Current physical appearance or status.

source_refs: Chapter 28 summary

[[SECTION markdown]]

# Dejah Thoris
**Role:** Lost Love

**Status:** Referenced / Visionary

**Physical Description:** Martian female (implied).

**Costume/Silhouette:** Unknown.

**Prompting Phrases:** Martian princess, distant love, vision of Mars.

**Uncertainty Notes:** Character is not physically present in the current timeline; only exists in Carter's memory and visions.
[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: little_boy

canonical_character_id: The Little Boy

aliases: Child

is_fully_identified: false

manual_description_required: true

manual_description_reason: Appears only in a vision/feeling.

clarification_required: true

clarification_reason: Nature of the child (real or hallucination) is unconfirmed.

clarification_question: Is the child a real person from Carter's future or a purely symbolic vision?

character_type_hint: human/child

morphology_hint: small child

scale_hint: child scale

renderability_hint: medium

confidence: 0.5

direct_identity_evidence: Seen in vision.

direct_visual_evidence: None (visionary).

costume_or_covering_evidence: Unknown.

movement_evidence: Part of a vision/feeling.

associated_entities: Dejah Thoris, John Carter

alias_or_role_evidence: A child waiting for Carter.

unknowns: Identity and reality.

source_refs: Chapter 28 summary

[[SECTION markdown]]

# The Little Boy
**Role:** Visionary figure

**Status:** Referenced / Visionary

**Physical Description:** A young boy.

**Costume/Silhouette:** Unknown.

**Prompting Phrases:** Young child, visionary child, waiting across space.

**Uncertainty Notes:** It is unclear if this child is a literal person or a manifestation of Carter's longing.
[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: hideous_creature

canonical_character_id: The Hideous Creature

aliases: Creature

is_fully_identified: false

manual_description_required: true

manual_description_reason: Vague description in a vision.

clarification_required: true

clarification_reason: Visual details are not provided beyond "hideous".

clarification_question: What are the specific physical characteristics of this creature?

character_type_hint: unknown

morphology_hint: hideous

scale_hint: unknown

renderability_hint: medium

confidence: 0.4

direct_identity_evidence: Mentioned in vision.

direct_visual_evidence: None (visionary).

costume_or_covering_evidence: Unknown.

movement_evidence: Part of a vision/feeling.

associated_entities: Little Boy, John Carter

alias_or_role_evidence: Seen in a vision alongside the child.

unknowns: Appearance, species, size.

source_refs: Chapter 28 summary

[[SECTION markdown]]

# The Hideous Creature
**Role:** Visionary entity

**Status:** Referenced / Visionary

**Physical Description:** Described only as "hideous".

**Costume/Silhouette:** Unknown.

**Prompting Phrases:** Monstrous, hideous creature, unsettling vision.

**Uncertainty Notes:** Extremely low detail; appearance is entirely undefined in the text.
[[/SECTION]]

[[/FILMCREATOR_PACKET]]
````
