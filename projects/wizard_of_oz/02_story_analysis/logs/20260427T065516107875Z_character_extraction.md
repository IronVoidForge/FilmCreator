# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-27T06:55:16.107875+00:00
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

Chapter id: CH003

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

**Setting:** The Munchkin Country (characterized by blue houses and round domes) and the Yellow Brick Road, specifically near a large cornfield.

**Characters:** 
- **Dorothy:** A young girl traveling to the Emerald City.
- **Toto:** Dorothy's dog.
- **Boq:** A wealthy Munchkin who hosts Dorothy.
- **The Scarecrow:** A living, straw-stuffed figure perched on a pole in a cornfield.

**Events:**
- Dorothy prepares for her journey by changing into a clean gingham dress and discovering that the silver shoes belonging to the deceased Wicked Witch of the East fit her perfectly.
- She begins walking the Yellow Brick Road toward the Emerald City, observing the prosperous Munchkin farms and receiving respectful bows from the locals.
- Dorothy is invited to a celebration at the home of Boq, a wealthy Munchkin. During the festivities, Boq mistakes her for a "friendly witch" due to her silver shoes and white-and-blue clothing. 
- After a night's rest, Dorothy continues her journey. Boq warns her that the path ahead is long and potentially dangerous.
- While resting near a cornfield, Dorothy encounters a Scarecrow that comes to life. She helps him down from his pole.
- The Scarecrow explains that he lacks brains because his head is stuffed with straw. He asks Dorothy to take him to the Emerald City so the Great Oz might grant him intelligence.
- Dorothy agrees to let him join her. The chapter ends with Dorothy and the Scarecrow walking together along the Yellow Brick Road, while Toto remains skeptical of their new companion.
````

## Raw Response
````text
[[FILMCREATOR_PACKET]]

task: character_extraction

version: 1

character_index_markdown:

[[SECTION character_index_markdown]]

# Character Index

- [dorothy](dorothy)
- [toto](toto)
- [boq](boq)
- [the_scarecrow](the_scarecrow)

[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: dorothy
canonical_character_id: Dorothy
aliases: Young girl, friendly witch
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
direct_identity_evidence: Dorothy is named as the traveler.
direct_visual_evidence: Wears a clean gingham dress and silver shoes.
costume_or_covering_evidence: White-and-blue gingham dress, silver shoes.
movement_evidence: Walking the Yellow Brick Road.
associated_entities: Toto, Boq, The Scarecrow
alias_or_role_evidence: Mistaken for a "friendly witch" by Boq.
unknowns: 
source_refs: 

[[SECTION markdown]]
# Dorothy
**Role:** Protagonist / Traveler

**Status:** Physically Present

**Physical Description:** A young girl.

**Costume & Silhouette:** Wears a white-and-blue gingham dress and silver shoes.

**Descriptive Nouns:** Young girl, traveler, gingham-clad girl.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: toto
canonical_character_id: Toto
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
direct_identity_evidence: Toto is named as Dorothy's dog.
direct_visual_evidence: Identified as a dog.
costume_or_covering_evidence: 
movement_evidence: Traveling with Dorothy, acting skeptical of the Scarecrow.
associated_entities: Dorothy
alias_or_role_evidence: 
unknowns: 
source_refs: 

[[SECTION markdown]]
# Toto
**Role:** Companion / Pet

**Status:** Physically Present

**Physical Description:** A dog.

**Costume & Silhouette:** N/A

**Descriptive Nouns:** Small dog, canine companion.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: boq
canonical_character_id: Boq
aliases: Wealthy Munchkin
is_fully_identified: true
manual_description_required: true
manual_description_reason: While identified as a "wealthy Munchkin," specific physical features (height, facial structure, etc.) are not described.
clarification_required: false
clarification_reason: 
clarification_question: 
character_type_hint: humanoid_nonhuman
morphology_hint: biped
scale_hint: small
renderability_hint: renderable
confidence: 0.7
direct_identity_evidence: Boq is named as the host.
direct_visual_evidence: Identified as a Munchkin.
costume_or_covering_evidence: 
movement_evidence: Hosting festivities.
associated_entities: Dorothy
alias_or_role_evidence: Described as a wealthy Munchkin.
unknowns: Specific facial features or exact Munchkin morphology.
source_refs: 

[[SECTION markdown]]
# Boq
**Role:** Supporting Character / Host

**Status:** Physically Present

**Physical Description:** A Munchkin; described as wealthy.

**Costume & Silhouette:** Unknown.

**Descriptive Nouns:** Wealthy Munchkin, host.

**Uncertainty Note:** Specific physical appearance and clothing are not detailed in the text.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: the_scarecrow
canonical_character_id: The Scarecrow
aliases: Straw-stuffed figure
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
direct_identity_evidence: The Scarecrow is named as the figure in the cornfield.
direct_visual_evidence: A living, straw-stuffed figure perched on a pole.
costume_or_covering_evidence: Stuffed with straw.
movement_evidence: Comes to life, climbs down from a pole, walks with Dorothy.
associated_entities: Dorothy, Toto
alias_or_role_evidence: 
unknowns: 
source_refs: 

[[SECTION markdown]]
# The Scarecrow
**Role:** Companion / Traveling Ally

**Status:** Physically Present

**Physical Description:** A living figure stuffed with straw.

**Costume & Silhouette:** Straw-stuffed humanoid; perched on a pole in a cornfield.

**Descriptive Nouns:** Straw man, living scarecrow, straw-stuffed figure.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
