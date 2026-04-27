# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-27T07:07:31.814586+00:00
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

Chapter id: CH010

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

**Summary:**
After being rescued from a field of deadly poppies by mice, the Cowardly Lion rejoins Dorothy and her companions. The group travels along the yellow brick road through a landscape dominated by green-painted houses and people dressed in emerald attire. They stop at a farmhouse for supper, where a local man informs them of the Great Oz's elusive nature; he explains that the Wizard is a shapeshifter who rarely allows anyone to see his true form. The travelers discuss their specific quests (brains, heart, courage, and returning home) before continuing to the Emerald City. Upon arrival, they encounter the Guardian of the Gates at a massive emerald-studded gate. To prevent them from being blinded by the city's intense green brilliance, the Guardian forces the entire group—including Toto—to wear green-lensed spectacles that are locked onto their heads with a key he holds. The chapter ends as the Guardian leads them into the streets of the Emerald City.

**Characters:**
* **Dorothy:** The leader of the group, seeking to return to Kansas.
* **Scarecrow:** Seeking brains from Oz.
* **Tin Woodman:** Seeking a heart from Oz.
* **Cowardly Lion:** Seeking courage from Oz; recently recovered from poppy sleep.
* **Toto:** Dorothy's dog.
* **Farmer/Woman & Family:** Residents of a green farmhouse who provide food and information about Oz.
* **Guardian of the Gates:** A small, green-skinned man who manages entry to the Emerald City and enforces the use of protective spectacles.

**Settings:**
* **The Yellow Brick Road/Green Countryside:** A beautiful landscape featuring green fences and houses.
* **The Farmhouse:** A residence where the group rests for the night.
* **The Emerald City Gates:** A high, thick green wall with an emerald-studded gate.
* **The Streets of the Emerald City:** The brilliant, glowing interior of the city reached after passing through the gates.
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
- [Farmer/Woman & Family](#farmer_woman_family)
- [Guardian of the Gates](#guardian_of_the_gates)

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
direct_identity_evidence: Dorothy is identified as the leader seeking to return home.
direct_visual_evidence: 
costume_or_covering_evidence: 
movement_evidence: 
associated_entities: Scarecrow, Tin Woodman, Cowardly Lion, Toto
alias_or_role_evidence: 
unknowns: 
source_refs: 
[[SECTION markdown]]
# Dorothy
**Role:** Group leader seeking to return home to Kansas.
**Presence:** Physically present.
**Description:** A human girl traveling with a group of companions.
**Notes:** Part of the core traveling party.
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
direct_identity_evidence: Scarecrow is seeking brains from Oz.
direct_visual_evidence: 
costume_or_covering_evidence: 
movement_evidence: 
associated_entities: Dorothy, Tin Woodman, Cowardly Lion
alias_or_role_evidence: 
unknowns: 
source_refs: 
[[SECTION markdown]]
# Scarecrow
**Role:** Companion seeking brains.
**Presence:** Physically present.
**Description:** A humanoid non-human entity.
**Notes:** Part of the core traveling party.
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
direct_identity_evidence: Tin Woodman is seeking a heart from Oz.
direct_visual_evidence: 
costume_or_covering_evidence: 
movement_evidence: 
associated_entities: Dorothy, Scarecrow, Cowardly Lion
alias_or_role_evidence: 
unknowns: 
source_refs: 
[[SECTION markdown]]
# Tin Woodman
**Role:** Companion seeking a heart.
**Presence:** Physically present.
**Description:** A humanoid non-human entity.
**Notes:** Part of the core traveling party.
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
direct_identity_evidence: Cowardly Lion is seeking courage; recently rescued from poppies.
direct_visual_evidence: 
costume_or_covering_evidence: 
movement_evidence: 
associated_entities: Dorothy, Scarecrow, Tin Woodman
alias_or_role_evidence: 
unknowns: 
source_refs: 
[[SECTION markdown]]
# Cowardly Lion
**Role:** Companion seeking courage.
**Presence:** Physically present (recently recovered from poppy sleep).
**Description:** A large animal/creature.
**Notes:** Part of the core traveling party.
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
confidence: 0.9
direct_identity_evidence: Toto is Dorothy's dog.
direct_visual_evidence: 
costume_or_covering_evidence: Wears green-lensed spectacles (locked on).
movement_evidence: 
associated_entities: Dorothy
alias_or_role_evidence: 
unknowns: 
source_refs: 
[[SECTION markdown]]
# Toto
**Role:** Dorothy's dog.
**Presence:** Physically present.
**Description:** A small quadruped animal.
**Costume:** Wears green-lensed spectacles.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: farmer_woman_family
canonical_character_id: CH007 Farmer/Woman & Family
aliases: Local residents
is_fully_identified: false
manual_description_required: true
manual_description_reason: Only mentioned as a group; specific physical traits for individuals are not provided.
clarification_required: true
clarification_reason: Need individual descriptions if they are to be rendered specifically.
clarification_question: What do the individual members of this family look like?
character_type_hint: human
morphology_hint: biped
scale_hint: human_scale
renderability_hint: renderable
confidence: 0.5
direct_identity_evidence: Residents of a green farmhouse who provide food and information.
direct_visual_evidence: 
costume_or_covering_evidence: Dressed in emerald attire (implied by landscape description).
movement_evidence: 
associated_entities: 
alias_or_role_evidence: 
unknowns: 
source_refs: 
[[SECTION markdown]]
# Farmer/Woman & Family
**Role:** Local residents providing food and information.
**Presence:** Physically present (at the farmhouse).
**Description:** A group of humans living in a green-painted landscape.
**Costume:** Likely dressed in emerald attire to match the surroundings.
**Uncertainty Note:** Specific physical features for individual family members are unknown.
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
confidence: 0.9
direct_identity_evidence: Guardian of the Gates at the Emerald City entrance.
direct_visual_evidence: Small, green-skinned man.
costume_or_covering_evidence: Holds a key used to lock spectacles on heads.
movement_evidence: Leads the group into the streets.
associated_entities: Dorothy, Scarecrow, Tin Woodman, Cowardly Lion, Toto
alias_or_role_evidence: 
unknowns: 
source_refs: 
[[SECTION markdown]]
# Guardian of the Gates
**Role:** Gatekeeper of the Emerald City.
**Presence:** Physically present.
**Description:** A small man with green skin.
**Costume/Traits:** Carries a key used to secure protective green-lensed spectacles onto travelers' heads.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
