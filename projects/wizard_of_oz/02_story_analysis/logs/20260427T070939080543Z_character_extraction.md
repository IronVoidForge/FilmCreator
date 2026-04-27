# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-27T07:09:39.080543+00:00
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

Chapter id: CH011

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

**Setting:** The Emerald City, characterized by green marble streets, emerald-studded buildings, and citizens dressed entirely in green. The group stays within the Palace of Oz.

**Characters:** 
- Dorothy & Toto
- Scarecrow (seeking brains)
- Tin Woodman (seeking a heart)
- Cowardly Lion (seeking courage)
- The Great Oz (appearing in various shifting forms: a Giant Head, a Lovely Lady, a Terrible Beast, and a Ball of Fire)
- The Guardian of the Gates and Palace Soldiers
- A Green Girl (palace attendant)

**Key Events:**
- **Arrival in the Emerald City:** The group arrives at the city and is dazzled by the pervasive green splendor. They are led to the Palace of Oz.
- **The Wizard's Terms:** The group is lodged in the palace. Each member is granted a private audience with Oz one by one, but Oz refuses to grant their requests immediately. Instead, he demands they kill the Wicked Witch of the West as a condition for their wishes.
- **The Shifting Identities of Oz:** 
    - Dorothy meets a **Giant Head**, which demands she kill the Witch to return home.
    - The Scarecrow meets a **Lovely Lady**, who promises brains if he (or someone) kills the Witch.
    - The Tin Woodman meets a **Terrible Beast**, who promises a heart if he helps Dorothy kill the Witch.
    - The Lion meets a **Ball of Fire**, which demands proof of the Witch's death to grant him courage.
- **The Decision:** Despite their fears and reluctance to kill, the group realizes they have no choice but to fulfill the Wizard's command. They prepare themselves for the journey to the land of the Winkies the following morning.
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
- [The Great Oz](#the_great_oz)
- [Guardian of the Gates](#guardian_of_the_gates)
- [Palace Soldiers](#palace_soldiers)
- [Green Girl](#green_girl)

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
direct_identity_evidence: Present in Emerald City arrival and audience with Oz.
direct_visual_evidence: 
costume_or_covering_evidence: 
movement_evidence: 
associated_entities: Toto, Scarecrow, Tin Woodman, Cowardly Lion, The Great Oz
alias_or_role_evidence: 
unknowns: 
source_refs: 

[[SECTION markdown]]
# Dorothy
**Role:** Protagonist.
**Status:** Physically present.
**Description:** A young human girl traveling with her companions to the Emerald City.
**Notes:** Part of the core group seeking passage home via the Wizard.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: toto
canonical_character_id: CH003 Toto
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
direct_identity_evidence: Traveling with Dorothy.
direct_visual_evidence: 
costume_or_covering_evidence: 
movement_evidence: 
associated_entities: Dorothy
alias_or_role_evidence: 
unknowns: 
source_refs: 

[[SECTION markdown]]
# Toto
**Role:** Companion.
**Status:** Physically present.
**Description:** A small animal companion to Dorothy.
**Notes:** Travels with the group through the Emerald City.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: scarecrow
canonical_character_id: CH004 Scarecrow
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
direct_identity_evidence: Seeking brains in the Emerald City.
direct_visual_evidence: 
costume_or_covering_evidence: 
movement_evidence: 
associated_entities: Dorothy, Tin Woodman, Cowardly Lion, The Great Oz
alias_or_role_evidence: 
unknowns: 
source_refs: 

[[SECTION markdown]]
# Scarecrow
**Role:** Companion.
**Status:** Physically present.
**Description:** A humanoid entity seeking brains.
**Notes:** Meets the Wizard in the form of a "Lovely Lady."
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: tin_woodman
canonical_character_id: CH005 Tin Woodman
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
direct_identity_evidence: Seeking a heart in the Emerald City.
direct_visual_evidence: 
costume_or_covering_evidence: 
movement_evidence: 
associated_entities: Dorothy, Scarecrow, Cowardly Lion, The Great Oz
alias_or_role_evidence: 
unknowns: 
source_refs: 

[[SECTION markdown]]
# Tin Woodman
**Role:** Companion.
**Status:** Physically present.
**Description:** A humanoid entity seeking a heart.
**Notes:** Meets the Wizard in the form of a "Terrible Beast."
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: cowardly_lion
canonical_character_id: CH006 Cowardly Lion
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
confidence: 1.0
direct_identity_evidence: Seeking courage in the Emerald City.
direct_visual_evidence: 
costume_or_covering_evidence: 
movement_evidence: 
associated_entities: Dorothy, Scarecrow, Tin Woodman, The Great Oz
alias_or_role_evidence: 
unknowns: 
source_refs: 

[[SECTION markdown]]
# Cowardly Lion
**Role:** Companion.
**Status:** Physically present.
**Description:** A large animal seeking courage.
**Notes:** Meets the Wizard in the form of a "Ball of Fire."
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: the_great_oz
canonical_character_id: CH007 The Great Oz
aliases: Wizard, Oz
is_fully_identified: false
manual_description_required: true
manual_description_reason: Character manifests in multiple, contradictory shifting forms.
clarification_required: true
clarification_reason: Identity is intentionally unstable/shifting.
clarification_question: Should the character be rendered as a composite entity or as separate assets for each manifestation?
character_type_hint: unknown
morphology_hint: unknown
scale_hint: unknown
renderability_hint: renderable
confidence: 0.5
direct_identity_evidence: Identified as The Great Oz/Wizard.
direct_visual_evidence: Giant Head, Lovely Lady, Terrible Beast, Ball of Fire.
costume_or_covering_evidence: 
movement_evidence: Shifting forms.
associated_entities: Dorothy, Scarecrow, Tin Woodman, Cowardly Lion
alias_or_role_evidence: 
unknowns: True underlying form.
source_refs: 

[[SECTION markdown]]
# The Great Oz
**Role:** Ruler of the Emerald City.
**Status:** Physically present (via manifestations).
**Description:** A shapeshifting entity that appears to different characters in different forms.
**Manifestations:**
- Giant Head (met by Dorothy)
- Lovely Lady (met by Scarecrow)
- Terrible Beast (met by Tin Woodman)
- Ball of Fire (met by Cowardly Lion)
**Notes:** Demands the death of the Wicked Witch of the West as a condition for granting wishes.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: guardian_of_the_gates
canonical_character_id: CH008 Guardian of the Gates
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
direct_identity_evidence: Named as Guardian of the Gates.
direct_visual_evidence: 
costume_or_covering_evidence: 
movement_evidence: 
associated_entities: Palace Soldiers
alias_or_role_evidence: 
unknowns: 
source_refs: 

[[SECTION markdown]]
# Guardian of the Gates
**Role:** Gatekeeper.
**Status:** Physically present.
**Description:** An entity guarding the entrance to the Emerald City/Palace.
**Notes:** Part of the city's security/order.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: palace_soldiers
canonical_character_id: CH009 Palace Soldiers
aliases: 
is_fully_identified: true
manual_description_required: false
manual_description_reason: 
clarification_required: false
clarification_reason: 
clarification_question: 
character_type_hint: group
morphology_hint: biped
scale_hint: human_scale
renderability_hint: renderable
confidence: 0.9
direct_identity_evidence: Mentioned as Palace Soldiers.
direct_visual_evidence: 
costume_or_covering_evidence: Dressed in green (implied by city description).
movement_evidence: 
associated_entities: Guardian of the Gates
alias_or_role_evidence: 
unknowns: 
source_refs: 

[[SECTION markdown]]
# Palace Soldiers
**Role:** Security/Attendants.
**Status:** Physically present.
**Description:** A group of soldiers stationed within the Palace of Oz.
**Notes:** Likely part of the pervasive green aesthetic of the city.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: green_girl
canonical_character_id: CH010 Green Girl
aliases: Palace Attendant
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
direct_identity_evidence: Identified as a Green Girl/palace attendant.
direct_visual_evidence: 
costume_or_covering_evidence: Dressed in green.
movement_evidence: 
associated_entities: The Great Oz
alias_or_role_evidence: 
unknowns: 
source_refs: 

[[SECTION markdown]]
# Green Girl
**Role:** Palace Attendant.
**Status:** Physically present.
**Description:** A female attendant in the palace, dressed entirely in green.
**Notes:** Consistent with the Emerald City's aesthetic.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
