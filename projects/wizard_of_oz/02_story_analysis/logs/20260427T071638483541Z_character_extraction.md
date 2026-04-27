# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-27T07:16:38.483541+00:00
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

Chapter id: CH014

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

**Setting:** The vast, scarlet fields of buttercups and yellow daisies between the Wicked Witch's castle and the Emerald City; later, the air above the landscape during flight.

**Characters:** 
- **Dorothy:** Uses the Golden Cap to summon help.
- **Scarecrow, Tin Woodman, Cowardly Lion, Toto:** Dorothy's companions, who become lost and discouraged in the fields.
- **Queen of the Mice:** Provides directions and explains the power of the Golden Cap.
- **The Winged Monkeys (including the Monkey King):** Magical creatures bound to obey the wearer of the Golden Cap.

**Events:**
- **Lost in the Fields:** After being carried away from the Wicked Witch's castle by Winged Monkeys, the travelers become lost in a massive field of flowers because they cannot maintain their direction without a road.
- **The Mice's Advice:** Desperate and exhausted, Dorothy uses her whistle to summon the Queen of the Mice. The Queen informs them that they have been walking in the wrong direction and suggests using the Golden Cap to command the Winged Monkeys for transport.
- **Summoning the Monkeys:** Dorothy reads the magic words inside the Golden Cap and performs a ritual involving standing on different feet. This summons the band of Winged Monkeys, who arrive to obey her command to fly them to the Emerald City.
- **The Legend of the Golden Cap:** During the flight, the Monkey King tells Dorothy the history of his people. He explains how they were once free until a prank played by his grandfather on the groom-to-be, Quelala, angered the sorceress Gayelette. As punishment, the monkeys were bound to obey the wearer of the Golden Cap three times.
- **Arrival:** The Winged Monkeys fly the group rapidly across the land, arriving at the gates of the Emerald City, successfully ending their period of being lost.
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
- [Scarecrow](#scarecrow)
- [Tin Woodman](#tin_woodman)
- [Cowardly Lion](#cowardly_lion)
- [Toto](#toto)
- [Queen of the Mice](#queen_of_the_mice)
- [Winged Monkeys](#winged_monkeys)
- [Monkey King](#monkey_king)

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
confidence: 1.0
direct_identity_evidence: Named as Dorothy and uses the Golden Cap.
direct_visual_evidence: Present in chapter.
costume_or_covering_evidence: 
movement_evidence: Uses whistle to summon mice, performs ritual with feet.
associated_entities: Scarecrow, Tin Woodman, Cowardly Lion, Toto, Winged Monkeys, Queen of the Mice
alias_or_role_evidence: 
unknowns: 
source_refs: 

[[SECTION markdown]]
# Dorothy
**Role:** Protagonist; traveler seeking the Emerald City.
**Status:** Physically present.
**Description:** A human girl capable of using magical artifacts like the Golden Cap and a whistle to summon creatures.
**Traits:** Determined, resourceful.
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
confidence: 1.0
direct_identity_evidence: Named as Scarecrow.
direct_visual_evidence: Present in chapter.
costume_or_covering_evidence: 
movement_evidence: Walking through fields, becomes lost/discouraged.
associated_entities: Dorothy, Tin Woodman, Cowardly Lion, Toto
alias_or_role_evidence: 
unknowns: 
source_refs: 

[[SECTION markdown]]
# Scarecrow
**Role:** Companion to Dorothy.
**Status:** Physically present.
**Description:** A humanoid scarecrow figure.
**Traits:** Becomes lost and discouraged in the flower fields.
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
confidence: 1.0
direct_identity_evidence: Named as Tin Woodman.
direct_visual_evidence: Present in chapter.
costume_or_covering_evidence: Constructed of tin.
movement_evidence: Walking through fields.
associated_entities: Dorothy, Scarecrow, Cowardly Lion, Toto
alias_or_role_evidence: 
unknowns: 
source_refs: 

[[SECTION markdown]]
# Tin Woodman
**Role:** Companion to Dorothy.
**Status:** Physically present.
**Description:** A humanoid figure constructed of tin.
**Traits:** Becomes lost and discouraged in the flower fields.
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
scale_hint: human_scale
renderability_hint: renderable
confidence: 1.0
direct_identity_evidence: Named as Cowardly Lion.
direct_visual_evidence: Present in chapter.
costume_or_covering_evidence: 
movement_evidence: Walking through fields.
associated_entities: Dorothy, Scarecrow, Tin Woodman, Toto
alias_or_role_evidence: 
unknowns: 
source_refs: 

[[SECTION markdown]]
# Cowardly Lion
**Role:** Companion to Dorothy.
**Status:** Physically present.
**Description:** A large quadruped lion.
**Traits:** Becomes lost and discouraged in the flower fields.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: toto
canonical_character_id: CH006 Toto
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
confidence: 1.0
direct_identity_evidence: Named as Toto.
direct_visual_evidence: Present in chapter.
costume_or_covering_evidence: 
movement_evidence: Traveling with the group.
associated_entities: Dorothy, Scarecrow, Tin Woodman, Cowardly Lion
alias_or_role_evidence: 
unknowns: 
source_refs: 

[[SECTION markdown]]
# Toto
**Role:** Companion to Dorothy.
**Status:** Physically present.
**Description:** A small quadruped animal (dog).
**Traits:** Traveling with the group through the fields.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: queen_of_the_mice
canonical_character_id: CH007 Queen of the Mice
aliases: 
is_fully_identified: true
manual_description_required: true
manual_description_reason: No physical description provided beyond being a mouse/queen.
clarification_required: false
clarification_reason: 
clarification_question: 
character_type_hint: animal
morphology_hint: quadruped
scale_hint: tiny
renderability_hint: renderable
confidence: 0.8
direct_identity_evidence: Named as Queen of the Mice.
direct_visual_evidence: Present in chapter (summoned by Dorothy).
costume_or_covering_evidence: 
movement_evidence: Provides directions to travelers.
associated_entities: Dorothy
alias_or_role_evidence: 
unknowns: 
source_refs: 

[[SECTION markdown]]
# Queen of the Mice
**Role:** Guide/Informant.
**Status:** Physically present.
**Description:** A tiny mouse-like creature with authority over mice.
**Uncertainty:** Specific visual details (clothing, appearance) are not provided in text.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: winged_monkeys
canonical_character_id: CH008 Winged Monkeys
aliases: 
is_fully_identified: true
manual_description_required: false
manual_description_reason: 
clarification_required: false
clarification_reason: 
clarification_question: 
character_type_hint: creature
morphology_hint: biped_winged
scale_hint: human_scale
renderability_hint: renderable
confidence: 0.9
direct_identity_evidence: Named as Winged Monkeys; bound to the Golden Cap.
direct_visual_evidence: Present in chapter (summoned and flying).
costume_or_covering_evidence: 
movement_evidence: Flying across the land.
associated_entities: Monkey King, Dorothy
alias_or_role_evidence: 
unknowns: 
source_refs: 

[[SECTION markdown]]
# Winged Monkeys
**Role:** Magical servants/transportation.
**Status:** Physically present.
**Description:** A band of magical creatures with wings.
**Traits:** Bound to obey the wearer of the Golden Cap; capable of rapid flight.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: monkey_king
canonical_character_id: CH009 Monkey King
aliases: 
is_fully_identified: true
manual_description_required: true
manual_description_reason: Only identified by role/title; no physical description provided.
clarification_required: false
clarification_reason: 
clarification_question: 
character_type_hint: creature
morphology_hint: biped_winged
scale_hint: human_scale
renderability_hint: renderable
confidence: 0.7
direct_identity_evidence: Identified as the Monkey King during flight.
direct_visual_evidence: Present in chapter (speaking to Dorothy).
costume_or_covering_evidence: 
movement_evidence: Flying with the group.
associated_entities: Winged Monkeys, Dorothy
alias_or_role_evidence: 
unknowns: 
source_refs: 

[[SECTION markdown]]
# Monkey King
**Role:** Leader of the Winged Monkeys; storyteller.
**Status:** Physically present.
**Description:** A winged monkey leader who knows the history of his people.
**Uncertainty:** Physical appearance and specific distinguishing features are not described in this chapter.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
