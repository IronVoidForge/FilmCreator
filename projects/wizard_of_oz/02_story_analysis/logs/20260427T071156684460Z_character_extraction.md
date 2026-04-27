# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-27T07:11:56.684460+00:00
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

Chapter id: CH012

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

**Setting:** The rugged, untilled lands of the West, moving toward the Wicked Witch's castle.

**Characters:**
* **Dorothy & Toto:** Traveling toward the West; Dorothy discovers her green clothes have turned white.
* **The Scarecrow & Tin Woodman:** Act as protectors for the group during various attacks.
* **The Cowardly Lion:** Provides intimidation against the Witch's slaves but is eventually captured.
* **The Wicked Witch of the West:** A one-eyed, powerful antagonist who uses magic and minions to stop the travelers.
* **The Winged Monkeys:** Magical creatures summoned by the Golden Cap to capture the group.
* **The Winkies:** The Witch's yellow-clad slaves.

**Key Events:**
* **Departure from Emerald City:** The group heads West after receiving directions from the Guardian of the Gates.
* **The Witch's Failed Attacks:** The Witch sends a pack of wolves (defeated by the Tin Woodman), a flock of crows (defeated by the Scarecrow), and a swarm of black bees (neutralized by the Scarecrow using straw to protect Dorothy and the Lion) to destroy the travelers.
* **The Golden Cap:** In desperation, the Witch uses the last charge of the Golden Cap to summon the Winged Monkeys.
* **Capture of the Companions:** The Monkeys drop the Tin Woodman on sharp rocks, strip the Scarecrow of his straw, and bind the Lion to take him to the castle. They leave Dorothy unharmed due to the mark of the Good Witch on her forehead.
* **Imprisonment:** Dorothy is forced into domestic servitude in the Witch's kitchen, while the Lion is imprisoned in the courtyard and starved. Dorothy secretly feeds the Lion at night.
* **The Theft of the Silver Shoe:** The Witch uses invisible magic to trip Dorothy, allowing her to steal one of the Silver Shoes.
* **The Death of the Witch:** Enraged by the theft, Dorothy throws a bucket of water at the Witch. Because the Witch has a mortal vulnerability to water, she melts into a shapeless mass on the kitchen floor.
* **Resolution:** Dorothy retrieves her shoe and rushes to free the Lion and her other friends.
````

## Raw Response
````text
[[FILMCREATOR_PACKET]]

task: character_extraction

version: 1

character_index_markdown:

[[SECTION character_index_markdown]]

# Character Index

- [Dorothy](#dorothy)
- [Toto](#toto)
- [Scarecrow](#scarecrow)
- [Tin Woodman](#tin_woodman)
- [Cowardly Lion](#cowardly_lion)
- [Wicked Witch of the West](#wicked_witch_of_the_west)
- [Winged Monkeys](#winged_monkeys)
- [Winkies](#winkies)

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: dorothy

canonical_character_id: CH001 Dorothy

aliases: None

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

confidence: 1.0

direct_identity_evidence: Named as Dorothy; traveling with companions.

direct_visual_evidence: Green clothes have turned white.

costume_or_covering_evidence: White clothing (formerly green).

movement_evidence: Traveling, walking, throwing a bucket of water.

associated_entities: Toto, Scarecrow, Tin Woodman, Cowardly Lion, Wicked Witch of the West

alias_or_role_evidence: 

unknowns: 

source_refs: 

[[SECTION markdown]]

# Dorothy
**Role:** Protagonist / Traveler

**Status:** Physically Present

**Physical Description:** A human girl. Her clothing, which was previously green, has turned white during the journey.

**Costume/Silhouette:** White dress/clothing.

**Descriptive Phrases:** Young girl in white, traveler of the West.
[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: toto

canonical_character_id: CH003 Toto

aliases: None

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

confidence: 1.0

direct_identity_evidence: Named as Toto; traveling with Dorothy.

direct_visual_evidence: 

costume_or_covering_evidence: 

movement_evidence: Traveling with the group.

associated_entities: Dorothy

alias_or_role_evidence: 

unknowns: Specific breed/color not mentioned in this chapter.

source_refs: 

[[SECTION markdown]]

# Toto
**Role:** Companion / Pet

**Status:** Physically Present

**Physical Description:** A small animal companion to Dorothy.

**Costume/Silhouette:** Small quadruped.

**Descriptive Phrases:** Small dog, Dorothy's companion.
[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: scarecrow

canonical_character_id: CH004 Scarecrow

aliases: None

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

confidence: 1.0

direct_identity_evidence: Named as Scarecrow; part of the group.

direct_visual_evidence: Made of straw (implied by being stripped of it).

costume_or_covering_evidence: Straw-filled body.

movement_evidence: Defeating crows and bees; captured by monkeys.

associated_entities: Dorothy, Tin Woodman, Cowardly Lion, Wicked Witch of the West

alias_or_role_evidence: 

unknowns: Specific clothing/face details not provided.

source_refs: 

[[SECTION markdown]]

# Scarecrow
**Role:** Protector / Companion

**Status:** Physically Present

**Physical Description:** A humanoid entity composed of straw.

**Costume/Silhouette:** Straw-filled form; stripped of straw by monkeys during capture.

**Descriptive Phrases:** Straw man, protector, humanoid straw construct.
[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: tin_woodman

canonical_character_id: CH005 Tin Woodman

aliases: None

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

confidence: 1.0

direct_identity_evidence: Named as Tin Woodman; part of the group.

direct_visual_evidence: Made of tin (implied by name/type).

costume_or_covering_evidence: Metal body.

movement_evidence: Defeating wolves; dropped on rocks by monkeys.

associated_entities: Dorothy, Scarecrow, Cowardly Lion, Wicked Witch of the West

alias_or_role_evidence: 

unknowns: Specific articulation or facial features.

source_refs: 

[[SECTION markdown]]

# Tin Woodman
**Role:** Protector / Companion

**Status:** Physically Present

**Physical Description:** A humanoid entity made of tin.

**Costume/Silhouette:** Metallic, bipedal silhouette.

**Descriptive Phrases:** Tin man, metal protector, articulated metal humanoid.
[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: cowardly_lion

canonical_character_id: CH006 Cowardly Lion

aliases: None

is_fully_identified: true

manual_description_required: false

manual_description_reason: 

clarification_required: false

clarification_reason: 

clarification_question: 

character_type_hint: animal

morphology_hint: quadruped

scale_hint: large

renderability_hint: renderable

confidence: 1.0

direct_identity_evidence: Named as Cowardly Lion; part of the group.

direct_visual_evidence: A lion.

costume_or_covering_evidence: 

movement_evidence: Intimidating slaves; captured and bound by monkeys; imprisoned in courtyard.

associated_entities: Dorothy, Scarecrow, Tin Woodman, Wicked Witch of the West

alias_or_role_evidence: 

unknowns: 

source_refs: 

[[SECTION markdown]]

# Cowardly Lion
**Role:** Protector / Companion

**Status:** Physically Present

**Physical Description:** A large lion.

**Costume/Silhouette:** Large quadruped, feline silhouette.

**Descriptive Phrases:** Large lion, intimidating beast, imprisoned lion.
[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: wicked_witch_of_the_west

canonical_character_id: CH007 Wicked Witch of the West

aliases: The Witch

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

confidence: 1.0

direct_identity_evidence: Named as Wicked Witch of the West.

direct_visual_evidence: One eye (one-eyed).

costume_or_covering_evidence: Uses invisible magic.

movement_evidence: Trips Dorothy; melts into a shapeless mass when hit with water.

associated_entities: Winged Monkeys, Winkies, Dorothy

alias_or_role_evidence: 

unknowns: Specific clothing color or facial features beyond the single eye.

source_refs: 

[[SECTION markdown]]

# Wicked Witch of the West
**Role:** Antagonist

**Status:** Physically Present

**Physical Description:** A powerful, one-eyed woman/entity.

**Costume/Silhouette:** Uses invisible magic; melts into a shapeless mass upon contact with water.

**Descriptive Phrases:** One-eyed witch, powerful antagonist, melting sorceress.
[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: winged_monkeys

canonical_character_id: CH008 Winged Monkeys

aliases: None

is_fully_identified: true

manual_description_required: false

manual_description_reason: 

clarification_required: false

clarification_reason: 

clarification_question: 

character_type_hint: creature

morphology_hint: biped (implied by monkey/flight)

scale_hint: human_scale

renderability_hint: renderable

confidence: 0.9

direct_identity_evidence: Named as Winged Monkeys; summoned by Golden Cap.

direct_visual_evidence: They have wings.

costume_or_covering_evidence: 

movement_evidence: Flying to capture the group; dropping the Tin Woodman; stripping the Scarecrow; binding the Lion.

associated_entities: Wicked Witch of the West, Dorothy, Scarecrow, Tin Woodman, Cowardly Lion

alias_or_role_evidence: 

unknowns: Specific wing type or monkey species.

source_refs: 

[[SECTION markdown]]

# Winged Monkeys
**Role:** Minions / Captors

**Status:** Physically Present

**Physical Description:** Magical winged creatures (monkeys).

**Costume/Silhouette:** Flying primates.

**Descriptive Phrases:** Winged monkeys, magical flying minions, primate with wings.
[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: winkies

canonical_character_id: CH009 Winkies

aliases: The Witch's slaves

is_fully_identified: true

manual_description_required: false

manual_description_reason: 

clarification_required: false

clarification_reason: 

clarification_question: 

character_type_hint: humanoid

morphology_hint: biped

scale_hint: human_scale

renderability_hint: renderable

confidence: 1.0

direct_identity_evidence: Identified as the Witch's slaves.

direct_visual_evidence: Wearing yellow clothing.

costume_or_covering_evidence: Yellow-clad.

movement_evidence: Acting as slaves/minions.

associated_entities: Wicked Witch of the West

alias_or_role_evidence: 

unknowns: Individual identities or specific facial features.

source_refs: 

[[SECTION markdown]]

# Winkies
**Role:** Minions / Slaves

**Status:** Physically Present (referenced as slaves)

**Physical Description:** Humanoid slaves to the Witch.

**Costume/Silhouette:** Yellow clothing.

**Descriptive Phrases:** Yellow-clad slaves, Witch's minions.
[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
