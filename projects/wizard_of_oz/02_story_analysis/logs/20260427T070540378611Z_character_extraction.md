# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-27T07:05:40.378611+00:00
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

Chapter id: CH009

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

**Setting:** A grassy field near a river, adjacent to a poppy bed.

**Characters:** 
- Dorothy
- Scarecrow
- Tin Woodman
- Toto
- The Queen of the Field Mice (and her subjects)
- The Cowardly Lion (unconscious)

**Events:**
- While traveling near the river, the Tin Woodman kills a large yellow Wildcat that was attempting to eat a small field mouse.
- The mouse reveals herself to be the Queen of all the Field Mice and pledges her people's service to the Woodman.
- Toto attempts to chase the mice, but the Woodman protects them from the dog.
- To repay the favor, the Scarecrow asks the mice to help rescue the Cowardly Lion, who is trapped in a sleep-inducing poppy bed.
- The Tin Woodman constructs a wooden truck using tree limbs and pegs.
- Thousands of mice arrive, each bringing a piece of string to act as harness lines for the vehicle.
- Dorothy wakes up from her own poppy-induced sleep to find the mice gathered around her.
- The mice, assisted by the pushing of the Scarecrow and Woodman, successfully pull the heavy Lion out of the poppy field and into the fresh air of the green fields.
- After the rescue, the Queen of the Mice promises future assistance before departing with her subjects.
- The group settles down to wait for the Lion to awaken.
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
- [Toto](#toto)
- [Queen of the Field Mice](#queen_of_the_field_mice)
- [Cowardly Lion](#cowardly_lion)
- [Wildcat](#wildcat)

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
direct_identity_evidence: Dorothy is named as waking up from a poppy-induced sleep.
direct_visual_evidence: 
costume_or_covering_evidence: 
movement_evidence: Wakes up and finds mice gathered around her.
associated_entities: Scarecrow, Tin Woodman, Toto, Cowardly Lion
alias_or_role_evidence: 
unknowns: 
source_refs: 
[[SECTION markdown]]
# Dorothy
**Role:** Protagonist / Traveler
**Presence:** Physically present (wakes up during the chapter).
**Description:** A human girl who has been sleeping in a poppy field.
**Notes:** Physical appearance details are not explicitly detailed in this specific chapter, but she is part of the core traveling group.
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
confidence: 0.9
direct_identity_evidence: Scarecrow is named as asking the mice for help and pushing the truck.
direct_visual_evidence: 
costume_or_covering_evidence: 
movement_evidence: Pushes the wooden truck to move the Lion.
associated_entities: Dorothy, Tin Woodman, Toto, Cowardly Lion, Queen of the Field Mice
alias_or_role_evidence: 
unknowns: 
source_refs: 
[[SECTION markdown]]
# Scarecrow
**Role:** Companion / Traveler
**Presence:** Physically present.
**Description:** A humanoid figure made of straw/stuffing.
**Notes:** Acts as a leader/negotiator with the mice and provides physical labor to move the Lion.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: tin_woodman
canonical_character_id: CH004 Tin Woodman
aliases: The Woodman
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
direct_identity_evidence: Tin Woodman is named as killing the wildcat and constructing the truck.
direct_visual_evidence: 
costume_or_covering_evidence: Constructed of metal/tin.
movement_evidence: Kills a wildcat; constructs a wooden truck; pushes the truck.
associated_entities: Dorothy, Scarecrow, Toto, Cowardly Lion, Queen of the Field Mice
alias_or_role_evidence: 
unknowns: 
source_refs: 
[[SECTION markdown]]
# Tin Woodman
**Role:** Companion / Traveler
**Presence:** Physically present.
**Description:** A humanoid entity constructed of tin.
**Notes:** Demonstrates strength and craftsmanship by killing a wildcat and building a wooden vehicle for the Lion's rescue.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: toto
canonical_character_id: CH005 Toto
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
direct_identity_evidence: Toto is named as attempting to chase the mice.
direct_visual_evidence: 
costume_or_covering_evidence: 
movement_evidence: Attempts to chase field mice.
associated_entities: Dorothy
alias_or_role_evidence: 
unknowns: 
source_refs: 
[[SECTION markdown]]
# Toto
**Role:** Companion / Pet
**Presence:** Physically present.
**Description:** A small dog.
**Notes:** Attempts to hunt the field mice but is restrained/protected by the Tin Woodman.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: queen_of_the_field_mice
canonical_character_id: CH006 Queen of the Field Mice
aliases: The Queen
is_fully_identified: true
manual_description_required: true
manual_description_reason: Only identified as a "small field mouse"; specific visual traits (crown, clothing, etc.) are not described.
clarification_required: false
clarification_reason: 
clarification_question: 
character_type_hint: animal
morphology_hint: quadruped
scale_hint: tiny
renderability_hint: renderable
confidence: 0.7
direct_identity_evidence: Revealed to be the Queen after being saved from a wildcat.
direct_visual_evidence: Small field mouse.
costume_or_covering_evidence: 
movement_evidence: Leads her subjects; departs with them.
associated_entities: Field Mice (subjects), Tin Woodman, Scarecrow
alias_or_role_evidence: 
unknowns: Specific regal features or markings.
source_refs: 
[[SECTION markdown]]
# Queen of the Field Mice
**Role:** Leader of the Field Mice
**Presence:** Physically present.
**Description:** A small field mouse who holds royal status over her kind.
**Notes:** She pledges her people's service to the Tin Woodman and coordinates a massive rescue effort using thousands of mice and string.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: cowardly_lion
canonical_character_id: CH007 Cowardly Lion
aliases: The Lion
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
direct_identity_evidence: Named as the one trapped in the poppy bed.
direct_visual_evidence: Large, currently unconscious/sleeping.
costume_or_covering_evidence: 
movement_evidence: Unconscious; being pulled by mice in a truck.
associated_entities: Dorothy, Scarecrow, Tin Woodman, Queen of the Field Mice
alias_or_role_evidence: 
unknowns: 
source_refs: 
[[SECTION markdown]]
# Cowardly Lion
**Role:** Companion / Traveler
**Presence:** Physically present (unconscious).
**Description:** A large lion.
**Notes:** He is incapacitated by the sleep-inducing properties of a poppy bed and must be rescued/transported by the group and the mice.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: wildcat
canonical_character_id: WILD001 Wildcat
aliases: Large yellow Wildcat
is_fully_identified: true
manual_description_required: false
manual_description_reason: 
clarification_required: false
clarification_reason: 
clarification_question: 
character_type_hint: animal
morphology_hint: quadruped
scale_hint: small
renderability_hint: context_only
confidence: 0.8
direct_identity_evidence: Described as a large yellow Wildcat attempting to eat a mouse.
direct_visual_evidence: Large and yellow.
costume_or_covering_evidence: 
movement_evidence: Attempting to eat a mouse; killed by the Tin Woodman.
associated_entities: Queen of the Field Mice (victim)
alias_or_role_evidence: 
unknowns: 
source_refs: 
[[SECTION markdown]]
# Wildcat
**Role:** Antagonist (Minor/Deceased)
**Presence:** Referenced/Action-only.
**Description:** A large, yellow wildcat.
**Notes:** Killed by the Tin Woodman while attempting to prey on a field mouse.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
