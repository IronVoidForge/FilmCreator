# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-26T07:11:41.741864+00:00
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



Entity taxonomy rules:

- identify what the entity itself appears to be, not what it wears or rides

- do not confuse nearby/associated things with the entity

- if source says a person rides a mount, classify the person separately from the mount

- if source says a character wears foreign/alien/exotic clothing, do not change their species/type

- character_type_hint: human, humanoid_nonhuman, animal, creature, group, object, machine, abstract, unknown

- morphology_hint: biped, quadruped, multi_legged, serpentine, winged, constructed, amorphous, unknown

- scale_hint: tiny, small, human_scale, large, giant, unknown

- renderability_hint: renderable, context_only, alias_or_role, unknown

- confidence: 0.0 to 1.0 for each type/morphology/renderability hint

- if uncertain, use unknown and explain the missing evidence in the markdown section



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
morphology_hint: biped
scale_hint: human_scale
renderability_hint: renderable
confidence: 0.9
direct_identity_evidence: true
direct_visual_evidence: true
costume_or_covering_evidence: true
movement_evidence: true
associated_entities: mummified_woman, dejah_thoris, little_boy, hideous_creature
alias_or_role_evidence: true
unknowns: 
source_refs: 
[[SECTION markdown]]
# John Carter
**Role:** Protagonist.

**Status:** Physically present.

**Description:** A man who has aged twenty years since his return to Earth. He is wealthy and resides in a study overlooking the Hudson River. He experiences profound longing for Mars.

**Costume/Traits:** Initially found in an Arizona cave wearing strange, crumbling garments. Later seen as a mature man in a terrestrial study.

**Prompt Phrases:** Mature human male, weathered features, contemplative expression, wealthy Earth dweller, longing gaze.
[[/SECTION]]
[[/FILMCREATOR_RECORD]

[[FILMCREATOR_RECORD]]
type: character
asset_id: mummified_woman
canonical_character_id: Mummified Woman
aliases: Old woman
is_fully_identified: true
manual_description_required: false
manual_description_reason: 
clarification_required: false
clarification_reason: 
clarification_question: 
character_type_hint: humanoid_nonhuman
morphology_hint: biped
scale_hint: human_scale
renderability_hint: renderable
confidence: 0.8
direct_identity_evidence: true
direct_visual_evidence: true
costume_or_covering_evidence: false
movement_evidence: false
associated_entities: john_carter
alias_or_role_evidence: true
unknowns: 
source_refs: 
[[SECTION markdown]]
# Mummified Woman
**Role:** Deceased figure found in the cave.

**Status:** Physically present (as a corpse).

**Description:** A mummified remains of an old woman found tending a charcoal burner with green powder.

**Costume/Traits:** Mummified, desiccated skin, part of a scene involving hanging human skeletons.

**Prompt Phrases:** Mummified female corpse, ancient desiccated skin, skeletal remains, cave dweller mummy.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: dejah_thoris
canonical_character_id: Dejah Thoris
aliases: Lost love
is_fully_identified: false
manual_description_required: true
manual_description_reason: Only mentioned as a memory/longing; no physical description provided in this chapter.
clarification_required: true
clarification_reason: Physical appearance is not described in the text.
clarification_question: What are the specific physical characteristics of Dejah Thoris?
character_type_hint: humanoid_nonhuman
morphology_hint: biped
scale_hint: human_scale
renderability_hint: context_only
confidence: 0.5
direct_identity_evidence: true
direct_visual_evidence: false
costume_or_covering_evidence: false
movement_evidence: false
associated_entities: john_carter
alias_or_role_evidence: true
unknowns: physical appearance
source_refs: 
[[SECTION markdown]]
# Dejah Thoris
**Role:** Carter's lost love on Mars.

**Status:** Referenced (in memory/vision).

**Description:** A figure of intense longing for the protagonist, believed to be waiting for him on Mars.

**Costume/Traits:** Unknown.

**Prompt Phrases:** Martian woman, object of affection, distant memory.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: little_boy
canonical_character_id: Little Boy
aliases: Child
is_fully_identified: false
manual_description_required: true
manual_description_reason: Appears only in a vision/feeling; no physical details provided.
clarification_required: true
clarification_reason: Visual identity is purely speculative/visionary.
clarification_question: What does the child in the vision look like?
character_type_hint: human
morphology_hint: biped
scale_hint: small
renderability_hint: context_only
confidence: 0.4
direct_identity_evidence: false
direct_visual_evidence: false
costume_or_covering_evidence: false
movement_evidence: false
associated_entities: dejah_thoris, john_carter
alias_or_role_evidence: true
unknowns: physical appearance
source_refs: 
[[SECTION markdown]]
# Little Boy
**Role:** Visionary figure.

**Status:** Uncertain (Vision/Imagined).

**Description:** A child sensed by Carter in a profound feeling or vision, potentially his offspring with Dejah Thoris.

**Costume/Traits:** Unknown.

**Prompt Phrases:** Young child, visionary figure, ethereal presence.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: hideous_creature
canonical_character_id: Hideous Creature
aliases: 
is_fully_identified: false
manual_description_required: true
manual_description_reason: Described only by the adjective "hideous" in a vision.
clarification_required: true
clarification_reason: No morphological or visual details provided beyond being "hideous".
clarification_question: What is the specific morphology and appearance of the hideous creature?
character_type_hint: creature
morphology_hint: unknown
scale_hint: unknown
renderability_hint: context_only
confidence: 0.2
direct_identity_evidence: false
direct_visual_evidence: false
costume_or_covering_evidence: false
movement_evidence: false
associated_entities: little_boy
alias_or_role_evidence: true
unknowns: morphology, scale, appearance
source_refs: 
[[SECTION markdown]]
# Hideous Creature
**Role:** Visionary figure.

**Status:** Uncertain (Vision/Imagined).

**Description:** A creature seen in Carter's vision alongside the child.

**Costume/Traits:** Described as "hideous".

**Prompt Phrases:** Monstrous entity, frightening creature, shadowy vision.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
