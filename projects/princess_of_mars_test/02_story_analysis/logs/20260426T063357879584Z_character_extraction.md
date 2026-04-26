# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-26T06:33:57.879584+00:00
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

**Setting:** A cave in the Arizona mountains; a rocky gorge under a clear starlight night.

**Characters:**
- **The Protagonist:** An experienced fighter who becomes paralyzed by a mysterious gas in a cave, undergoes a metaphysical metamorphosis, and is eventually pulled toward Mars.
- **Apache Warriors:** A group of braves who approach the cave but flee in terror from an unseen moaning sound emanating from the cave's depths.
- **The Protagonist's Dead Friend:** His body lies on a ledge near the cave entrance.

**Events:**
- The protagonist is paralyzed by a pungent, tenuous vapor within a cave, rendering him unable to move despite remaining mentally conscious.
- A group of Apache warriors approaches the cave but are struck with primal fear by a low moaning sound from the darkness behind the protagonist; they flee in panic, causing one warrior to fall from the cliff.
- The protagonist's horse wanders off down the trail, leaving him stranded and unarmed.
- At midnight, after hearing more mysterious rustling and moaning, the protagonist exerts a massive act of will to break his paralysis.
- Upon standing, he discovers a terrifying metamorphosis: he is standing naked, while his own physical body remains lying lifeless on the cave floor, still clothed and carrying his weapons.
- Fearing the unseen entity in the cave, the protagonist escapes into the Arizona night.
- While gazing at the landscape and the red star of Mars, the protagonist feels an overwhelming, magnetic pull toward the planet. He surrenders to this fascination and is suddenly transported through space into darkness.
````

## Raw Response
````text
[[FILMCREATOR_PACKET]]

task: character_extraction

version: 1

character_index_markdown:

[[SECTION character_index_markdown]]

# Character Index - CH002

- [Protagonist](#protagonist)
- [Apache Warriors](#apache-warriors)
- [Dead Friend](#dead-friend)

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: protagonist

canonical_character_id: CH002 Protagonist

aliases: Fighter, Metamorphosed Entity

is_fully_identified: false

manual_description_required: true

manual_description_reason: Physical appearance is highly unstable due to metamorphosis; the text describes a separation of consciousness from a lifeless body.

clarification_required: true

clarification_reason: The nature of the new physical form post-metamorphosis is not visually described beyond being "naked" and distinct from the original body.

clarification_question: What are the specific physical characteristics, skin texture, or non-human traits of the protagonist's new form after the metamorphosis?

character_type_hint: humanoid_nonhuman

morphology_hint: biped

scale_hint: human_scale

renderability_hint: renderable

confidence: 0.5

direct_identity_evidence: Explicitly identified as the character undergoing the experience.

direct_visual_evidence: Described as naked and standing separate from his original body.

costume_or_covering_evidence: Naked (post-metamorphosis); clothed/armed (original body).

movement_evidence: Initially paralyzed, then exerts will to stand, then escapes into the night.

associated_entities: Dead Friend, Apache Warriors, Horse (referenced)

alias_or_role_evidence: Experienced fighter.

unknowns: Specific facial features, hair, eye color, and exact post-metamorphosis anatomy.

source_refs: Chapter 2 summary.

[[SECTION markdown]]

# Protagonist
**Role:** Central character undergoing metaphysical transformation.

**Status:** Physically present (in new form).

**Physical Description:** 
An experienced fighter who undergoes a metamorphosis. Post-transformation, he is described as standing naked, while his original physical body remains lying lifeless on the cave floor. The text implies a separation of consciousness from the original biological vessel.

**Costume/Silhouette:** 
Naked (post-metamorphosis). His original form is clothed and carrying weapons.

**Descriptive Noun Phrases:** 
Metamorphosed fighter, naked wanderer, displaced consciousness, survivor of the cave gas.

**Uncertainty Notes:** 
The exact visual nature of the "new" body is unknown; it is unclear if he remains human in appearance or has become something else entirely.
[[/SECTION]]

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

character_type_hint: human

morphology_hint: biped

scale_hint: human_scale

renderability_hint: renderable

confidence: 0.8

direct_identity_evidence: Identified as Apache warriors/braves.

direct_visual_evidence: Approaching the cave, fleeing in terror.

costume_or_covering_evidence: Not specified beyond cultural context.

movement_evidence: Approach the cave, flee in panic, one falls from a cliff.

associated_entities: Protagonist (nearby)

alias_or_role_evidence: Group of braves.

unknowns: Specific facial features or individual clothing details.

source_refs: Chapter 2 summary.

[[SECTION markdown]]

# Apache Warriors
**Role:** Witness/Bystanders.

**Status:** Physically present.

**Physical Description:** 
A group of Apache warriors/braves.

**Costume/Silhouette:** 
Not explicitly detailed in text.

**Descriptive Noun Phrases:** 
Terrified braves, fleeing warriors, mountain scouts.

**Uncertainty Notes:** 
Specific visual details regarding their attire or individual features are absent from the text.
[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: dead_friend

canonical_character_id: CH002 Dead Friend

aliases: Lifeless Body

is_fully_identified: false

manual_description_required: true

manual_description_reason: No physical description provided other than being a body on a ledge.

clarification_required: true

clarification_reason: Identity and appearance are unknown.

clarification_question: What was the name and physical appearance of the protagonist's friend?

character_type_hint: human

morphology_hint: biped

scale_hint: human_scale

renderability_hint: context_only

confidence: 0.4

direct_identity_evidence: Identified as the protagonist's dead friend.

direct_visual_evidence: A body lying on a ledge near the cave entrance.

costume_or_covering_evidence: Clothed (as part of the original body/vessel).

movement_evidence: None (deceased).

associated_entities: Protagonist

alias_or_role_evidence: Dead friend.

unknowns: Name, age, appearance, specific clothing.

source_refs: Chapter 2 summary.

[[SECTION markdown]]

# Dead Friend
**Role:** Referenced corpse/Former vessel.

**Status:** Physically present (as a corpse).

**Physical Description:** 
A lifeless body lying on a ledge near the cave entrance.

**Costume/Silhouette:** 
Clothed.

**Descriptive Noun Phrases:** 
Lifeless body, fallen comrade, clothed corpse.

**Uncertainty Notes:** 
No identifying features or specific clothing descriptions are provided.
[[/SECTION]]

[[/FILMCREATOR_PACKET]]
````
