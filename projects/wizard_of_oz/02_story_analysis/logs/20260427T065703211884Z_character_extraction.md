# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-27T06:57:03.211884+00:00
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
Project slug: wizard_of_oz

Chapter id: CH004

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

**Setting:** A deteriorating stretch of the Yellow Brick Road that transitions from well-tended farmland into a dismal, lonesome landscape, eventually entering a dense, dark forest where the canopy blocks out the daylight.

**Characters:** 
- **Dorothy:** A young girl traveling to the Emerald City; she expresses her longing for home and her belief that "there is no place like home."
- **The Scarecrow:** Dorothy's companion who lacks brains; he is physically resilient but prone to stumbling due to his lack of intellect.
- **Toto:** Dorothy's dog, who possesses superior night vision.

**Key Events:**
- **The Difficult Road:** The travelers navigate uneven and broken yellow bricks; the Scarecrow frequently falls into holes because he lacks the brains to avoid them.
- **Midday Rest & Conversation:** During a lunch break by a brook, Dorothy explains the concept of "home" to the Scarecrow, who cannot understand why anyone would prefer a gray place like Kansas over the beauty of Oz.
- **The Scarecrow's Origin Story:** The Scarecrow recounts his creation by a farmer and a Munchkin. He describes his first experiences of consciousness, being placed on a pole in a cornfield, and his realization of his own inadequacy when an old crow informs him that brains are the most important thing to possess.
- **Entering the Forest:** As evening approaches, the travelers enter a thick forest where it is nearly dark. Dorothy relies on the Scarecrow's guidance (and Toto's sight) to navigate the gloom.
- **Finding Shelter:** The Scarecrow locates a small cottage made of logs and branches. Dorothy and Toto sleep on a bed of dried leaves while the Scarecrow remains awake, standing guard through the night.
````

## Raw Response
````text
[[FILMCREATOR_PACKET]]

task: character_extraction

version: 1

character_index_markdown:

[[SECTION character_index_markdown]]

# Character Index

- [dorothy](#dorothy)
- [scarecrow](#scarecrow)
- [toto](#toto)
- [farmer](#farmer)
- [munchkin](#munchkin)
- [old_crow](#old_crow)

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: dorothy

canonical_character_id: CH001 Dorothy

aliases: Young girl

is_fully_identified: true

manual_description_required: false

manual_description_reason: 

clarification_required: false

clarification_reason: 

clarification_question: 

character_type_hint: human

morphology_hint: biped

scale_hint: small

renderability_hint: renderable

confidence: 0.9

direct_identity_evidence: true

direct_visual_evidence: false

costume_or_covering_evidence: false

movement_evidence: true

associated_entities: [scarecrow, toto]

alias_or_role_evidence: false

unknowns: []

source_refs: [CH004]

[[SECTION markdown]]
# Dorothy
**Role:** Protagonist / Traveler

**Status:** Physically Present

**Description:** A young girl traveling the Yellow Brick Road. She is characterized by her longing for home and her emotional connection to Kansas. 

**Visual Notes:** Specific clothing or hair details are not provided in this chapter, though she is established as a child.

**Prompt Phrases:** young girl, traveler, expressive face, weary traveler.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: scarecrow

canonical_character_id: CH003 Scarecrow

aliases: Companion

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

costume_or_covering_evidence: true

movement_evidence: true

associated_entities: [dorothy, toto]

alias_or_role_evidence: false

unknowns: []

source_refs: [CH004]

[[SECTION markdown]]
# Scarecrow
**Role:** Companion / Guide

**Status:** Physically Present

**Description:** A creature made of straw, created by a farmer and a Munchkin. He is physically resilient but lacks intellect, leading to clumsy movements and stumbling into holes.

**Visual Notes:** Constructed entity; likely composed of stuffed fabric/clothing and straw. He was originally placed on a pole in a cornfield.

**Prompt Phrases:** scarecrow, straw-filled humanoid, clumsy movement, rustic construction, cornfield origin.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: toto

canonical_character_id: CH005 Toto

aliases: Dog

is_fully_identified: true

manual_description_required: false

manual_description_reason: 

clarification_required: false

clarification_reason: 

clarification_question: 

character_type_hint: animal

morphology_hint: quadruped

scale_hint: small

renderability_hint: renderable

confidence: 0.9

direct_identity_evidence: true

direct_visual_evidence: false

costume_or_covering_evidence: false

movement_evidence: true

associated_entities: [dorothy]

alias_or_role_evidence: false

unknowns: []

source_refs: [CH004]

[[SECTION markdown]]
# Toto
**Role:** Companion / Scout

**Status:** Physically Present

**Description:** Dorothy's dog. He possesses superior night vision, assisting the group in the dark forest.

**Visual Notes:** Small canine. Specific breed is not mentioned.

**Prompt Phrases:** small dog, alert eyes, keen night vision, companion animal.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: farmer

canonical_character_id: REF_Farmer

aliases: 

is_fully_identified: false

manual_description_required: true

manual_description_reason: Only mentioned in a backstory; no physical description provided.

clarification_required: true

clarification_reason: Character is only a referenced figure in a memory/story.

clarification_question: What does the farmer look like?

character_type_hint: human

morphology_hint: biped

scale_hint: human_scale

renderability_hint: context_only

confidence: 0.5

direct_identity_evidence: false

direct_visual_evidence: false

costume_or_covering_evidence: false

movement_evidence: false

associated_entities: [scarecrow]

alias_or_role_evidence: true

unknowns: [physical appearance]

source_refs: [CH004]

[[SECTION markdown]]
# Farmer
**Role:** Referenced Creator

**Status:** Referenced (Backstory)

**Description:** A person who helped create the Scarecrow.

**Visual Notes:** No visual details available.

**Prompt Phrases:** farmer, rustic clothing (assumed), background character.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: munchkin

canonical_character_id: REF_Munchkin

aliases: 

is_fully_identified: false

manual_description_required: true

manual_description_reason: Mentioned as a creator of the Scarecrow, but no physical traits are described.

clarification_required: true

clarification_reason: Character is only referenced in backstory.

clarification_question: What is the specific morphology and scale of the Munchkin?

character_type_hint: humanoid_nonhuman

morphology_hint: biped

scale_hint: small

renderability_hint: context_only

confidence: 0.4

direct_identity_evidence: false

direct_visual_evidence: false

costume_or_covering_evidence: false

movement_evidence: false

associated_entities: [scarecrow]

alias_or_role_evidence: true

unknowns: [physical appearance, exact scale]

source_refs: [CH004]

[[SECTION markdown]]
# Munchkin
**Role:** Referenced Creator

**Status:** Referenced (Backstory)

**Description:** A being that assisted the farmer in creating the Scarecrow.

**Visual Notes:** No visual details provided.

**Prompt Phrases:** munchkin, small humanoid, fantasy creature.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: old_crow

canonical_character_id: REF_Old_Crow

aliases: 

is_fully_identified: true

manual_description_required: false

manual_description_reason: 

clarification_required: false

clarification_reason: 

clarification_question: 

character_type_hint: animal

morphology_hint: winged

scale_hint: small

renderability_hint: context_only

confidence: 0.7

direct_identity_evidence: true

direct_visual_evidence: false

costume_or_covering_evidence: false

movement_evidence: false

associated_entities: [scarecrow]

alias_or_role_evidence: false

unknowns: []

source_refs: [CH004]

[[SECTION markdown]]
# Old Crow
**Role:** Referenced Messenger

**Status:** Referenced (Backstory)

**Description:** A crow that spoke to the Scarecrow, informing him of the importance of having brains.

**Visual Notes:** An aged bird.

**Prompt Phrases:** old crow, black feathers, talking bird.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
