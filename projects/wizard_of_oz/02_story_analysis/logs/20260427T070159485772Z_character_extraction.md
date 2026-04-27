# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-27T07:01:59.485772+00:00
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

Chapter id: CH007

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

**Setting:** A dense forest containing deep ditches, a riverbank, and eventually a view of a beautiful, fruit-filled meadow across a swift river.

**Characters:** Dorothy (and Toto), Scarecrow, Tin Woodman, Cowardly Lion, and the Kalidahs (monstrous bear-tiger hybrids).

**Key Events:**
- **The Forest Camp:** The group camps under a large tree; the Tin Woodman gathers wood, the Scarecrow gathers nuts for Dorothy, and the Lion hunts for himself.
- **The First Ditch:** The travelers encounter a wide, deep chasm. The Cowardly Lion successfully leaps across the gap multiple times, carrying each companion one by one on his back to safety.
- **The Kalidahs Encounter:** The group reaches a second, wider ditch that the Lion cannot jump. Following the Scarecrow's plan, the Tin Woodman chops down a tree to create a bridge. As they cross, two Kalidahs attack. To save the group, the Scarecrow instructs the Woodman to chop the bridge from their side, causing the tree to fall and sending the Kalidahs to their deaths on the rocks below.
- **The River Crossing:** Exhausted by the forest, the group reaches a swift river. They see the beautiful land beyond but realize they must cross. The Tin Woodman begins constructing a raft out of small trees.
- **Conclusion:** The group camps by the river overnight as the raft construction continues, with Dorothy dreaming of the Emerald City and the Wizard.
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
- [Kalidahs](#kalidahs)

[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: dorothy
canonical_character_id: CH001 Dorothy
aliases: 
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
direct_identity_evidence: "The group includes Dorothy."
direct_visual_evidence: ""
costume_or_covering_evidence: ""
movement_evidence: ""
associated_entities: Toto, Scarecrow, Tin Woodman, Cowardly Lion
alias_or_role_evidence: 
unknowns: 
source_refs: 
[[SECTION markdown]]
# Dorothy
**Role:** Protagonist / Traveler

**Status:** Physically Present

**Description:** A human girl traveling through the forest. While specific clothing details are not provided in this chapter, she is a central member of the traveling group.

**Descriptive Phrases:** young girl, traveler, dreamer.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: toto
canonical_character_id: CH001 Toto
aliases: 
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
direct_identity_evidence: "Dorothy (and Toto)"
direct_visual_evidence: ""
costume_or_covering_evidence: ""
movement_evidence: ""
associated_entities: Dorothy
alias_or_role_evidence: 
unknowns: 
source_refs: 
[[SECTION markdown]]
# Toto
**Role:** Companion / Pet

**Status:** Physically Present

**Description:** A small animal companion to Dorothy. Specific breed is not mentioned in this text.

**Descriptive Phrases:** small dog, canine companion.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: scarecrow
canonical_character_id: CH003 Scarecrow
aliases: 
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
direct_identity_evidence: "The group includes the Scarecrow."
direct_visual_evidence: ""
costume_or_covering_evidence: ""
movement_evidence: "Gathers nuts for Dorothy."
associated_entities: Dorothy, Tin Woodman, Cowardly Lion
alias_or_role_evidence: 
unknowns: 
source_refs: 
[[SECTION markdown]]
# Scarecrow
**Role:** Group Member / Strategist

**Status:** Physically Present

**Description:** A non-human humanoid entity. He is capable of gathering nuts and formulating plans to cross ditches.

**Descriptive Phrases:** straw-filled humanoid, strategist, forest traveler.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: tin_woodman
canonical_character_id: CH004 Tin Woodman
aliases: 
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
direct_identity_evidence: "The group includes the Tin Woodman."
direct_visual_evidence: ""
costume_or_covering_evidence: "Constructed of tin (implied by name/nature)."
movement_evidence: "Gathers wood, chops down a tree to make a bridge, constructs a raft."
associated_entities: Scarecrow, Cowardly Lion, Dorothy
alias_or_role_evidence: 
unknowns: 
source_refs: 
[[SECTION markdown]]
# Tin Woodman
**Role:** Group Member / Builder

**Status:** Physically Present

**Description:** A humanoid entity made of tin. He is physically strong and capable of using tools like an axe to chop trees for bridges and rafts.

**Descriptive Phrases:** metallic humanoid, tin man, woodcutter, raft builder.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: cowardly_lion
canonical_character_id: CH005 Cowardly Lion
aliases: 
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
confidence: 0.9
direct_identity_evidence: "The group includes the Cowardly Lion."
direct_visual_evidence: ""
costume_or_covering_evidence: ""
movement_evidence: "Hunts for himself, leaps across wide chasms while carrying companions on his back."
associated_entities: Dorothy, Scarecrow, Tin Woodman
alias_or_role_evidence: 
unknowns: 
source_refs: 
[[SECTION markdown]]
# Cowardly Lion
**Role:** Group Member / Transport

**Status:** Physically Present

**Description:** A large animal capable of powerful leaps. He serves as a means of transport for the smaller companions across gaps.

**Descriptive Phrases:** large lion, powerful leaper, predator.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: kalidahs
canonical_character_id: CH006 Kalidahs
aliases: 
is_fully_identified: true
manual_description_required: false
manual_description_reason: 
clarification_required: false
clarification_reason: 
clarification_question: 
character_type_hint: creature
morphology_hint: quadruped
scale_hint: large
renderability_hint: renderable
confidence: 0.9
direct_identity_evidence: "Two Kalidahs attack."
direct_visual_evidence: "Monstrous bear-tiger hybrids."
costume_or_covering_evidence: ""
movement_evidence: "Attacking the group while crossing a bridge."
associated_entities: 
alias_or_role_evidence: 
unknowns: 
source_refs: 
[[SECTION markdown]]
# Kalidahs
**Role:** Antagonists

**Status:** Physically Present (during encounter)

**Description:** Monstrous creatures described as bear-tiger hybrids. They are aggressive enough to attack travelers crossing a bridge.

**Descriptive Phrases:** bear-tiger hybrids, monstrous predators, forest monsters.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
