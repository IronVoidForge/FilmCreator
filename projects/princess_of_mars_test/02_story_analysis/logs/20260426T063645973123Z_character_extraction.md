# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-26T06:36:45.973123+00:00
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

Chapter id: CH004

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

**Setting:**
An enormous, ancient city situated on a low table land near the edge of a dried-up Martian sea. The city features grand, white marble buildings inlaid with gold and jewels, though they appear built for a much smaller, extinct race. A large central plaza serves as the hub for the current inhabitants—a community of Green Martians.

**Characters:**
* **The Narrator (Protagonist):** A human captive attempting to navigate Martian customs through observation and physical prowess.
* **Tars Tarkas:** A high-ranking Green Martian, vice-chieftain of the community, and a skilled statesman/warrior who acts as the narrator's escort.
* **The Chieftain:** The ruler of the local Martian community, characterized by heavy metal ornamentation and a violent temperament.
* **Sola:** A young female Martian (approx. 8 feet tall) with light olive-green skin, belonging to Tars Tarkas's retinue; she provides the narrator with food/shelter.
* **The Martian People:** A race of large, tusked creatures. They are characterized by extreme violence, a lack of empathy for suffering, and a culture where death is often viewed as entertainment.

**Key Events:**
* **Arrival at the City:** The narrator and Tars Tarkas arrive at the deserted, ancient city, which is now occupied by hundreds of Green Martians.
* **Cultural Observations:** The narrator observes Martian biology (differences between sexes/ages) and their grim social customs, including a "voluntary pilgrimage" to the river Iss and a high mortality rate due to constant warfare and dangerous sports.
* **The Audience Chamber:** The party enters a magnificent marble hall to meet the Chieftain. The narrator notes that the furniture is scaled for humans, suggesting the Martians are squatters in an older civilization's ruins.
* **The Confrontation:** After struggling to walk, the narrator accidentally strikes a Martian warrior who was mocking him. Instead of being killed, the narrator is met with laughter and applause, earning respect through his display of aggression.
* **The "Sak" Demonstration:** To prove his worth/ability, the narrator performs a massive leap (sakk) of 150 feet, impressing the crowd.
* **Request for Sustenance:** The narrator refuses to perform further jumps, instead signaling his hunger and thirst.
* **Provisioning:** Sola leads the narrator to a decorated sleeping chamber where he is given rest and encounters a small, ten-legged Martian creature resembling a pony with frog-like features.
````

## Raw Response
````text
[[FILMCREATOR_PACKET]]

task: character_extraction

version: 1

character_index_markdown:

[[SECTION character_index_markdown]]

# Character Index - CH004

| Asset ID | Canonical ID | Role | Status |
| :--- | :--- | :--- | :--- |
| protagonist | Protagonist | Narrator / Human Captive | Physically Present |
| tars_tarkas | Tars Tarkas | Vice-chieftain / Escort | Physically Present |
| chieftain | The Chieftain | Local Ruler | Physically Present |
| sola | Sola | Martian Retinue Member | Physically Present |
| martian_people | Martian People | Local Inhabitants | Physically Present |

[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: protagonist
canonical_character_id: Protagonist
aliases: Narrator, Human Captive
is_fully_identified: true
manual_description_required: true
manual_description_reason: Physical appearance (facial features, hair, build) is not described in this chapter.
clarification_required: false
clarification_reason: 
clarification_question: 
character_type_hint: human
morphology_hint: biped
scale_hint: human_scale
renderability_hint: renderable
confidence: 0.9
direct_identity_evidence: Narrator identifies as a human captive.
direct_visual_evidence: Performs a 150-foot leap (sakk).
costume_or_covering_evidence: None specified.
movement_evidence: Struggles to walk in the Martian environment; performs massive leaps.
associated_entities: Tars Tarkas, Sola, The Chieftain
alias_or_role_evidence: Narrator/Captive.
unknowns: Physical facial features and clothing.
source_refs: CH004

[[SECTION markdown]]
# Protagonist
**Role:** Human captive and narrator.
**Status:** Physically present.
**Description:** A human male capable of extreme physical feats (a 150-foot leap). He is currently navigating a Martian city as a captive/guest.
**Visual Notes:** Physical appearance is currently unknown; requires specific character design for hair, face, and clothing.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: tars_tarkas
canonical_character_id: Tars Tarkas
aliases: Vice-chieftain
is_fully_identified: true
manual_description_required: true
manual_description_reason: While identified as a Green Martian, specific facial details or exact proportions are not provided.
clarification_required: false
clarification_reason: 
clarification_question: 
character_type_hint: humanoid_nonhuman
morphology_hint: biped
scale_hint: large
renderability_hint: renderable
confidence: 0.8
direct_identity_evidence: Named as Tars Tarkas, vice-chieftain.
direct_visual_evidence: Identified as a Green Martian.
costume_or_covering_evidence: None specified.
movement_evidence: Acts as an escort for the protagonist.
associated_entities: Protagonist, Sola, The Chieftain
alias_or_role_evidence: Vice-chieftain of the community.
unknowns: Specific facial features or exact scale relative to humans beyond "large".
source_refs: CH004

[[SECTION markdown]]
# Tars Tarkas
**Role:** High-ranking Green Martian, vice-chieftain, and escort.
**Status:** Physically present.
**Description:** A powerful Green Martian statesman and warrior. 
**Visual Notes:** Large humanoid non-human; green skin; tusked (per species description).
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: chieftain
canonical_character_id: The Chieftain
aliases: Ruler
is_fully_identified: true
manual_description_required: true
manual_description_reason: Specific facial features or exact morphology are not detailed.
clarification_required: false
clarification_reason: 
clarification_question: 
character_type_hint: humanoid_nonhuman
morphology_hint: biped
scale_hint: large
renderability_hint: renderable
confidence: 0.7
direct_identity_evidence: Identified as the ruler of the local community.
direct_visual_evidence: Wears heavy metal ornamentation.
costume_or_covering_evidence: Heavy metal ornamentation.
movement_evidence: Holds audience in a marble hall.
associated_entities: Tars Tarkas, Protagonist
alias_or_role_evidence: Ruler of the local Martian community.
unknowns: Specific facial features.
source_refs: CH004

[[SECTION markdown]]
# The Chieftain
**Role:** Local ruler/leader.
**Status:** Physically present.
**Description:** A violent-tempered Green Martian leader.
**Visual Notes:** Large humanoid; green skin; tusked; wears heavy metal ornamentation.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: sola
canonical_character_id: Sola
aliases: 
is_fully_identified: true
manual_description_required: false
manual_description_reason: 
clarification_required: false
clarification_reason: 
clarification_question: 
character_type_hint: humanoid_nonhuman
morphology_hint: biped
scale_hint: large
renderability_hint: renderable
confidence: 0.9
direct_identity_evidence: Named as Sola.
direct_visual_evidence: Approx 8 feet tall, light olive-green skin.
costume_or_covering_evidence: None specified.
movement_evidence: Leads the protagonist to a sleeping chamber.
associated_entities: Tars Tarkas, Protagonist
alias_or_role_evidence: Member of Tars Tarkas's retinue.
unknowns: 
source_refs: CH004

[[SECTION markdown]]
# Sola
**Role:** Martian retinue member; provider of food/shelter.
**Status:** Physically present.
**Description:** A young female Green Martian.
**Visual Notes:** Approximately 8 feet tall; light olive-green skin; tusked (per species description).
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: martian_people
canonical_character_id: Martian People
aliases: Green Martians
is_fully_identified: true
manual_description_required: false
manual_description_reason: 
clarification_required: false
clarification_reason: 
clarification_question: 
character_type_hint: group
morphology_hint: biped
scale_hint: large
renderability_hint: renderable
confidence: 0.8
direct_identity_evidence: Identified as the inhabitants of the city.
direct_visual_evidence: Large, tusked creatures; green skin.
costume_or_covering_evidence: None specified.
movement_evidence: Engage in warfare and dangerous sports; laugh/applaud at violence.
associated_entities: Tars Tarkas, The Chieftain
alias_or_role_evidence: Local inhabitants of the ancient city.
unknowns: 
source_refs: CH004

[[SECTION markdown]]
# Martian People
**Role:** The local population/inhabitants.
**Status:** Physically present (as a group).
**Description:** A violent, large-scale race of Green Martians with a culture centered around combat and entertainment through death.
**Visual Notes:** Large scale; green skin; prominent tusks; bipedal.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
