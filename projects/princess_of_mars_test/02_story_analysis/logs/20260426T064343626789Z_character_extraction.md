# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-26T06:43:43.626789+00:00
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

**Events:**
The protagonist receives a set of warrior's arms and ornaments from a respectful yet menacing Martian, which Sola and other women remodel to fit his smaller size. He begins intensive combat training with the Martian youth in the plaza, aided by his familiarity with Earthly weaponry. Through persistent effort, he masters the Martian language, allowing him to eavesdrop on the adults in his communal sleeping quarters. During a nighttime conversation, he learns from Sarkoja that the beautiful Red female prisoner is being transported to Thark to be executed at the great games before Tal Hajus. A heated argument breaks out between Sola and the other women; Sola defends her sympathy for the captive, expressing a philosophical disdain for the endless cycle of Martian bloodshed. This interaction confirms Sola's character and the protagonist's resolve to eventually seek her help in escaping the Green Martians.

**Characters:**
- **The Protagonist:** An Earthman undergoing combat training; successfully learns the Martian language.
- **Sola:** A female Green Martian who acts as a mentor/protector; shows unexpected empathy for the Red prisoner and expresses philosophical views on the brutality of Martian life.
- **Sarkoja:** An older, more hardened female Green Martian; critical of Sola's perceived weakness.
- **The Prisoner (Red Woman):** A beautiful captive being moved toward execution in Thark.
- **Other Females/Young Martians:** Members of the communal living group who participate in training and social discourse.

**Settings:**
- **The Plaza:** The location where the protagonist practices combat with the Martian youth.
- **Communal Sleeping Quarters:** The shared domicile where the protagonist lives with Sola, several females, young Martians, and Woola the hound; the site of the pivotal overheard conversation.
````

## Raw Response
````text
[[FILMCREATOR_PACKET]]

task: character_extraction

version: 1

character_index_markdown:

[[SECTION character_index_markdown]]

# Character Index - CH009

- [Protagonist](#protagonist)
- [Sola](#sola)
- [Sarkoja](#sarkoja)
- [The Prisoner](#the-prisoner)
- [Martian Youth](#martian-youth)
- [Other Females](#other-females)

[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: protagonist
canonical_character_id: CH002 Protagonist
aliases: Earthman
is_fully_identified: false
manual_description_required: true
manual_description_reason: Physical appearance (height, build, facial features) is not described in this chapter.
clarification_required: true
clarification_reason: Specific physical traits for rendering are missing.
clarification_question: What is the protagonist's specific physical appearance and height relative to the Martians?
character_type_hint: human
morphology_hint: biped
scale_hint: human_scale
renderability_hint: renderable
confidence: 0.9
direct_identity_evidence: Identified as an Earthman undergoing training.
direct_visual_evidence: None in this chapter.
costume_or_covering_evidence: Wears remodeled warrior's arms and ornaments.
movement_evidence: Engages in intensive combat training.
associated_entities: Sola, Martian Youth, Sarkoja
alias_or_role_evidence: Referred to as the Earthman.
unknowns: Physical features, hair/eye color, exact height.
source_refs: CH009

[[SECTION markdown]]
# Protagonist
**Role:** Central character; Earthman in training.
**Presence:** Physically present.
**Description:** An Earthman undergoing intensive combat training with Martian weaponry. He is small enough that his warrior's arms and ornaments had to be remodeled by the local women. 
**Costume/Traits:** Wears Martian warrior's arms and ornaments adapted for a smaller frame.
**Uncertainty:** Specific facial features, hair, eye color, and exact physical build are unknown.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: sola
canonical_character_id: CH003 Sola
aliases: Mentor, Protector
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
direct_identity_evidence: Identified as a female Green Martian.
direct_visual_evidence: Implied presence in communal quarters and plaza.
costume_or_covering_evidence: None specified in this chapter.
movement_evidence: Participates in social discourse/arguments.
associated_entities: Protagonist, Sarkoja, Other Females
alias_or_role_evidence: Acts as a mentor/protector to the protagonist.
unknowns: Specific visual details of her Green Martian physiology are not detailed in this chapter.
source_refs: CH009

[[SECTION markdown]]
# Sola
**Role:** Female Green Martian; mentor and protector.
**Presence:** Physically present.
**Description:** A female Green Martian who shows empathy for captives and expresses philosophical disdain for the cycle of Martian bloodshed.
**Costume/Traits:** Green Martian physiology (details pending broader series description).
**Uncertainty:** Specific visual markers of her "Green" appearance are not detailed in this chapter.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: sarkoja
canonical_character_id: CH004 Sarkoja
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
direct_identity_evidence: Identified as a female Green Martian.
direct_visual_evidence: Present in communal sleeping quarters during conversation.
costume_or_covering_evidence: None specified.
movement_evidence: Engages in verbal argument/conversation.
associated_entities: Sola, Protagonist
alias_or_role_evidence: Described as an older, more hardened female Green Martian.
unknowns: Specific visual details of her age-related features or clothing.
source_refs: CH009

[[SECTION markdown]]
# Sarkoja
**Role:** Older female Green Martian; antagonist/critic to Sola.
**Presence:** Physically present.
**Description:** A hardened, older female Green Martian who is critical of Sola's empathy.
**Costume/Traits:** Hardened demeanor.
**Uncertainty:** Specific visual details of her age or appearance are not provided.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: red_prisoner
canonical_character_id: CH005 Red Prisoner
aliases: The beautiful Red female prisoner
is_fully_identified: false
manual_description_required: true
manual_description_reason: Only described as "beautiful" and "Red"; no specific morphology or facial details provided.
clarification_required: true
clarification_reason: Needs visual definition for a Red Martian.
clarification_question: What are the specific physical characteristics of the Red female prisoner?
character_type_hint: humanoid_nonhuman
morphology_hint: biped
scale_hint: human_scale
renderability_hint: context_only
confidence: 0.7
direct_identity_evidence: Identified as a captive being moved to Thark.
direct_visual_evidence: None (referenced only).
costume_or_covering_evidence: None.
movement_evidence: Being transported for execution.
associated_entities: Sola, Sarkoja
alias_or_role_evidence: Referred to as the prisoner.
unknowns: Specific facial features, exact shade of red, clothing/bindings.
source_refs: CH009

[[SECTION markdown]]
# The Prisoner (Red Woman)
**Role:** Captive being transported for execution.
**Presence:** Referenced only.
**Description:** A beautiful female Red Martian prisoner destined for the great games at Thark.
**Costume/Traits:** Described as "beautiful."
**Uncertainty:** No specific visual details provided beyond her color (Red) and beauty.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: martian_youth
canonical_character_id: CH006 Martian Youth
aliases: 
is_fully_identified: false
manual_description_required: true
manual_description_reason: Only identified as a "Martian youth" with no physical description.
clarification_required: true
clarification_reason: Needs age/size and visual details.
clarification_question: What does the Martian youth look like?
character_type_hint: humanoid_nonhuman
morphology_hint: biped
scale_hint: small
renderability_hint: renderable
confidence: 0.6
direct_identity_evidence: Identified as a youth participating in combat training.
direct_visual_evidence: None.
costume_or_covering_evidence: None.
movement_evidence: Engages in combat training with the protagonist.
associated_entities: Protagonist
alias_or_role_evidence: 
unknowns: Physical appearance, exact age/size.
source_refs: CH009

[[SECTION markdown]]
# Martian Youth
**Role:** Combat sparring partner for the protagonist.
**Presence:** Physically present.
**Description:** A young Martian participating in combat training in the plaza.
**Costume/Traits:** None specified.
**Uncertainty:** No physical description or specific visual traits provided.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: other_females
canonical_character_id: CH007 Other Females
aliases: Women, Group of females
is_fully_identified: false
manual_description_required: true
manual_description_reason: They are a collective group with no individual descriptions.
clarification_required: false
clarification_reason: 
clarification_question: 
character_type_hint: group
morphology_hint: biped
scale_hint: human_scale
renderability_hint: context_only
confidence: 0.5
direct_identity_evidence: Identified as female Green Martians in the communal quarters.
direct_visual_evidence: None (group presence).
costume_or_covering_evidence: Involved in remodeling warrior's arms.
movement_evidence: Participating in social discourse and arguments.
associated_entities: Sola, Sarkoja, Protagonist
alias_or_role_evidence: 
unknowns: Individual identities, specific appearances.
source_refs: CH009

[[SECTION markdown]]
# Other Females
**Role:** Members of the communal living group.
**Presence:** Physically present (as a group).
**Description:** A group of female Green Martians who live in the communal quarters and participate in social/philosophical debates.
**Costume/Traits:** Involved in crafting/remodeling equipment.
**Uncertainty:** No individual descriptions or specific visual details for the group members.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
