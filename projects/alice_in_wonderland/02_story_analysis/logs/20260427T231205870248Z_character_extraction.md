# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-27T23:12:05.870248+00:00
- task: character_extraction

## System Prompt
````text
You are FilmCreator's chapter analysis engine.
Return only FilmCreator packets with the requested sections and records.
Do not wrap the packet in code fences unless explicitly requested.
Do not produce JSON-only responses.
If a packet asks for markdown sections, emit the section name on its own line and wrap the body in [[SECTION ...]] ... [[/SECTION]].
Do not put another [[SECTION ...]] tag inside a section body.
Keep the response deterministic and grounded in the supplied chapter text.
````

## User Prompt
````text
Project slug: alice_in_wonderland

Chapter id: CH002

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

**Location: The Hall / The Garden Door**
- **Visual State:** Alice is giant (over nine feet tall). Her head strikes the ceiling of the hall.
- **Event:** Alice looks down at her feet, which appear distant and small from her perspective. She contemplates sending boots to her feet via carrier.
- **Object Interaction:** Alice picks up a little golden key.
- **Action:** Alice hurries toward the garden door but finds she is too large to fit through. She sits and cries.
- **Environmental Change:** As Alice cries, a pool of salt water forms around her, roughly four inches deep, covering half the hall.

**Character Entrance: The White Rabbit**
- **Entrance:** The White Rabbit trots into the hall in a hurry. He is dressed splendidly, carrying white kid gloves and a large fan.
- **Action/Dialogue:** The Rabbit mutters about "the Duchess." Alice attempts to speak to him.
- **Reaction:** The Rabbit starts violently, drops the gloves and the fan, and scurries into the darkness.
- **Object Interaction:** Alice picks up the fan and the gloves.

**Character Internal State: Identity Crisis**
- **Action:** Alice fans herself due to the heat. She undergoes a philosophical monologue regarding her identity (questioning if she is "Mabel").
- **Action/Dialogue:** Alice attempts to recite multiplication tables and geography, but fails. She attempts to recite "How doth the little crocodile," but her voice sounds hoarse and strange.
- **Visual Reveal:** Alice realizes she has accidentally put on one of the Rabbit's white kid gloves.

**Physical Transformation: Shrinking**
- **Action/Scale Shift:** Alice stands by a table to measure herself; she is now approximately two feet high and shrinking rapidly.
- **Object Interaction:** She discovers the fan causes the shrinking and drops it to stabilize her size.
- **Action:** Alice runs back to the garden door, but finds it shut and the golden key sitting on the glass table.
- **Environmental Shift:** Alice slips and falls into the pool of tears. She is now swimming in salt water up to her chin.

**Character Interaction: The Mouse**
- **Event:** Alice hears splashing and swims toward a creature she initially thinks is a walrus or hippopotamus, but identifies as a Mouse.
- **Dialogue/Interaction:** Alice addresses the Mouse in formal English ("O Mouse"), then switches to French ("Où est ma chatte?") to test its intelligence.
- **Reaction:** The Mouse becomes agitated and offended by the mention of "cats." 
- **Conflict:** Alice tries to soothe the Mouse by mentioning her cat Dinah and a terrier dog, but these topics only make the Mouse more distressed/offended.
- **Resolution of Interaction:** The Mouse agrees to swim to the shore to tell its history once they are out of the water.

**Group Event: The Escape to Shore**
- **Environmental Change:** The pool becomes crowded with various animals (a Duck, a Dodo, a Lory, an Eaglet).
- **Action:** Alice leads the group of animals/birds swimming toward the shore to exit the pool.
````

## Raw Response
````text

````
