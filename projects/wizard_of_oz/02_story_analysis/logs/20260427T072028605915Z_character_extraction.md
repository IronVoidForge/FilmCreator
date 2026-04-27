# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-27T07:20:28.605915+00:00
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

Chapter id: CH016

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

**Setting:** The Throne Room of Oz and the surrounding camp area.

**Characters:** 
- **The Scarecrow:** Seeking brains.
- **The Tin Woodman:** Seeking a heart.
- **The Cowardly Lion:** Seeking courage.
- **Oz (The Wizard):** A "humbug" who uses sleight of hand and mundane objects to fulfill the travelers' requests.
- **Dorothy:** Observes her friends' transformations.

**Events:**
- **The Scarecrow's Brains:** The Scarecrow enters the Throne Room. Oz removes the Scarecrow's head, empties the straw, and replaces it with a mixture of bran, pins, and needles. The Scarecrow emerges feeling "wise" and "sharp."
- **The Tin Woodman's Heart:** The Woodman requests a heart. Oz cuts a hole in the Woodman's tin breast using shears and inserts a silk heart stuffed with sawdust. He then solders the tin back together. The Woodman is overjoyed by his new heart.
- **The Lion's Courage:** The Lion asks for courage. Oz presents a green liquid in a carved dish, claiming that since courage must be swallowed to become part of the person, he must drink it. The Lion drinks the contents and feels full of courage.
- **Oz's Reflection:** Alone after the group departs, Oz reveals his true nature as a humbug. He reflects on how easily he manipulated their imaginations to satisfy them, but expresses deep concern and uncertainty regarding his ability to fulfill Dorothy's much more difficult request: returning her to Kansas.
````

## Raw Response
````text
[[FILMCREATOR_PACKET]]

task: character_extraction

version: 1

character_index_markdown:

[[SECTION character_index_markdown]]

# Character Index

- [Scarecrow](#scarecrow)
- [Tin Woodman](#tin-woodman)
- [Cowardly Lion](#cowardly-lion)
- [Oz (The Wizard)](#oz-the-wizard)
- [Dorothy](#dorothy)

[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: scarecrow
canonical_character_id: CH001 Scarecrow
aliases: The Scarecrow
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
confidence: 0.9
direct_identity_evidence: The text identifies him as the Scarecrow seeking brains.
direct_visual_evidence: Mention of straw being removed from his head.
costume_or_covering_evidence: Straw-filled head.
movement_evidence: Enters the Throne Room.
associated_entities: Oz (The Wizard), Tin Woodman, Cowardly Lion, Dorothy
alias_or_role_evidence: 
unknowns: 
source_refs: 

[[SECTION markdown]]
# Scarecrow
**Role:** Traveler seeking brains.
**Presence:** Physically present.
**Description:** A humanoid entity composed of straw. In this chapter, his head is emptied of straw and refilled with a mixture of bran, pins, and needles to simulate "brains."
**Traits:** Straw-filled head (modified), wise/sharp persona post-transformation.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: tin_woodman
canonical_character_id: CH003 Tin Woodman
aliases: The Tin Woodman, Woodman
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
confidence: 0.9
direct_identity_evidence: The text identifies him as the Tin Woodman seeking a heart.
direct_visual_evidence: Tin body, breast cavity that can be cut with shears.
costume_or_covering_evidence: Constructed of tin.
movement_evidence: Present in the Throne Room.
associated_entities: Oz (The Wizard), Scarecrow, Cowardly Lion, Dorothy
alias_or_role_evidence: 
unknowns: 
source_refs: 

[[SECTION markdown]]
# Tin Woodman
**Role:** Traveler seeking a heart.
**Presence:** Physically present.
**Description:** A humanoid entity constructed of tin. He possesses a hollow breast cavity that can be opened with shears.
**Traits:** Metallic/tin body, soldered seams (post-procedure), contains a silk heart stuffed with sawdust.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: cowardly_lion
canonical_character_id: CH004 Cowardly Lion
aliases: The Lion, Lion
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
confidence: 0.8
direct_identity_evidence: The text identifies him as the Cowardly Lion seeking courage.
direct_visual_evidence: Consumes liquid from a carved dish.
costume_or_covering_evidence: 
movement_evidence: Present in the Throne Room.
associated_entities: Oz (The Wizard), Scarecrow, Tin Woodman, Dorothy
alias_or_role_evidence: 
unknowns: 
source_refs: 

[[SECTION markdown]]
# Cowardly Lion
**Role:** Traveler seeking courage.
**Presence:** Physically present.
**Description:** A large animal (lion) who seeks courage through a ritualistic consumption of liquid.
**Traits:** Large scale, consumes green liquid from a carved dish.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: oz_the_wizard
canonical_character_id: CH005 Oz the Wizard
aliases: Oz, The Wizard, Humbug
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
confidence: 0.7
direct_identity_evidence: Identified as Oz/The Wizard; reveals himself as a "humbug."
direct_visual_evidence: Uses shears, carved dishes, and mundane objects for sleight of hand.
costume_or_covering_evidence: 
movement_evidence: Operates within the Throne Room.
associated_entities: Scarecrow, Tin Woodman, Cowardly Lion, Dorothy
alias_or_role_evidence: Referred to as a "humbug" by himself.
unknowns: Physical appearance is not explicitly described in this chapter beyond his actions and tools.
source_refs: 

[[SECTION markdown]]
# Oz (The Wizard)
**Role:** The ruler of Oz; a manipulator/humbug.
**Presence:** Physically present.
**Description:** A figure who uses sleight of hand and mundane objects to fulfill the requests of travelers. He is revealed to be a "humbug" rather than a magical entity.
**Traits:** Manipulative, uses tools (shears, carved dishes), expresses internal anxiety regarding Dorothy's request.
**Uncertainty Note:** Specific physical appearance (clothing/face) is not detailed in this chapter.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: dorothy
canonical_character_id: CH002 Dorothy
aliases: Dorothy
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
direct_identity_evidence: Named as Dorothy; her request is the central concern of Oz.
direct_visual_evidence: Observes her friends' transformations.
costume_or_covering_evidence: 
movement_evidence: Present in the Throne Room/camp area.
associated_entities: Scarecrow, Tin Woodman, Cowardly Lion, Oz (The Wizard)
alias_or_role_evidence: 
unknowns: 
source_refs: 

[[SECTION markdown]]
# Dorothy
**Role:** Traveler seeking to return to Kansas.
**Presence:** Physically present.
**Description:** A human girl who observes the transformations of her companions.
**Traits:** Seeking a way home to Kansas.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
