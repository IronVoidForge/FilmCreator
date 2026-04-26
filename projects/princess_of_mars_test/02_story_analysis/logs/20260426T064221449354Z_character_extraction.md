# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-26T06:42:21.450354+00:00
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

Chapter id: CH008

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

**Setting:** A deserted Martian city and the surrounding valleys/hills.

**Events:**
- As the protagonist and Sola attempt to return home after an incubator ceremony, a sudden retreat by the green Martians reveals the approach of twenty large, gray-painted aerial vessels.
- The green Martian warriors engage the fleet in a highly organized and deadly skirmish from the city's buildings, targeting specific components of the ships (gunners, steering gear, etc.).
- The Martian fleet is routed; most ships retreat, but one unmanned, damaged vessel drifts erratically toward the city.
- The green Martians capture the drifting craft, strip it of all valuables (arms, silks, food, water), and then set it ablaze, sending it drifting away as a funeral pyre.
- The protagonist experiences a profound sense of melancholy and empathy for the defeated crew, feeling a strange connection to these unknown foemen.
- Upon returning to the plaza, the protagonist spots the prisoner taken from the craft: a beautiful, slender, reddish-copper skinned woman who resembles an Earthly woman in form.
- The woman makes a silent gesture toward the protagonist, seeking help; however, due to his ignorance of Martian customs, he fails to respond, leaving her to be dragged away into captivity with a look of dejection and contempt.

**Characters:**
- **The Protagonist:** An Earthman observing the conflict with growing empathy for the non-green Martians.
- **Sola:** A companion to the protagonist.
- **Green Martian Warriors:** Highly disciplined, organized combatants capable of rapid tactical retreats and precise warfare.
- **The Captive Woman:** A beautiful, slender, reddish-copper skinned female from the aerial fleet; she appears physically distinct from the green Martians.
- **Woola:** The protagonist's hound.

**Key Elements for Extraction:**
- The aerial battle between the Martian warriors and the gray vessels.
- The systematic looting and destruction of the drifting ship.
- The visual encounter/eye contact between the Protagonist and the Captive Woman in the plaza.
````

## Raw Response
````text
[[FILMCREATOR_PACKET]]

task: character_extraction

version: 1

character_index_markdown:

[[SECTION character_index_markdown]]

# Character Index - CH008

- [protagonist](#protagonist)
- [sola](#sola)
- [green_martian_warriors](#green_martian_warriors)
- [captive_woman](#captive_woman)
- [woola](#woola)

[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: protagonist
canonical_character_id: CH002 Protagonist
aliases: Earthman
is_fully_identified: true
manual_description_required: true
manual_description_reason: Physical appearance (clothing, facial features, build) is not described in this chapter.
clarification_required: false
clarification_reason: 
clarification_question: 
character_type_hint: human
morphology_hint: biped
scale_hint: human_scale
renderability_hint: renderable
confidence: 0.9
direct_identity_evidence: Identified as an Earthman observing Martian conflict.
direct_visual_evidence: None in this chapter.
costume_or_covering_evidence: None.
movement_evidence: Walking/returning with Sola and Woola.
associated_entities: Sola, Woola, Green Martian Warriors, Captive Woman
alias_or_role_evidence: Narrator/Observer.
unknowns: Physical appearance.
source_refs: Chapter 8 summary.

[[SECTION markdown]]
# Protagonist
**Role:** Observer and empathetic witness to the Martian skirmish.
**Status:** Physically present.
**Physical Description:** Identified as an Earthman; specific physical traits, clothing, or facial features are not provided in this chapter.
**Notes:** Experiences profound melancholy and empathy for the defeated aerial fleet crew.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: sola
canonical_character_id: CH003 Sola
aliases: 
is_fully_identified: true
manual_description_required: true
manual_description_reason: No physical description provided in this chapter.
clarification_required: false
clarification_reason: 
clarification_question: 
character_type_hint: humanoid_nonhuman
morphology_hint: biped
scale_hint: human_scale
renderability_hint: renderable
confidence: 0.7
direct_identity_evidence: Companion to the protagonist.
direct_visual_evidence: None in this chapter.
costume_or_covering_evidence: None.
movement_evidence: Returning home with the protagonist.
associated_entities: Protagonist, Woola
alias_or_role_evidence: 
unknowns: Physical appearance and species-specific traits.
source_refs: Chapter 8 summary.

[[SECTION markdown]]
# Sola
**Role:** Companion to the protagonist.
**Status:** Physically present.
**Physical Description:** No specific physical details provided in this chapter.
**Notes:** Traveling with the protagonist and Woola.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: green_martian_warriors
canonical_character_id: CH005 Green Martians
aliases: Martian warriors
is_fully_identified: true
manual_description_required: true
manual_description_reason: While identified as "green," specific armor, weaponry, or facial features are not detailed.
clarification_required: false
clarification_reason: 
clarification_question: 
character_type_hint: humanoid_nonhuman
morphology_hint: biped
scale_hint: human_scale
renderability_hint: renderable
confidence: 0.8
direct_identity_evidence: Identified as green Martian warriors engaging in combat.
direct_visual_evidence: Described as "green."
costume_or_covering_evidence: None specified, though they use buildings for cover.
movement_evidence: Highly organized and deadly skirmish; rapid tactical retreats.
associated_entities: Protagonist, Captive Woman
alias_or_role_evidence: 
unknowns: Specific clothing/armor and exact facial morphology.
source_refs: Chapter 8 summary.

[[SECTION markdown]]
# Green Martian Warriors
**Role:** Combatants/Antagonists in the skirmish.
**Status:** Physically present.
**Physical Description:** Described as green-skinned warriors.
**Costume/Silhouette:** Highly disciplined and organized; engage in precise warfare targeting ship components.
**Notes:** They loot and destroy the drifting vessel, treating it as a funeral pyre.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: captive_woman
canonical_character_id: CH006 Captive Woman
aliases: Prisoner
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
direct_identity_evidence: Identified as a prisoner from the aerial craft.
direct_visual_evidence: Beautiful, slender, reddish-copper skinned.
costume_or_covering_evidence: None specified.
movement_evidence: Makes a silent gesture toward the protagonist; being dragged away in dejection.
associated_entities: Protagonist, Green Martian Warriors
alias_or_role_evidence: 
unknowns: Specific clothing or attire.
source_refs: Chapter 8 summary.

[[SECTION markdown]]
# Captive Woman
**Role:** Prisoner from the defeated aerial fleet.
**Status:** Physically present.
**Physical Description:** Beautiful, slender, with reddish-copper skin. Resembles an Earthly woman in form.
**Costume/Silhouette:** Unknown.
**Notes:** She attempts to communicate a plea for help via gesture but is ignored by the protagonist.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: woola
canonical_character_id: CH004 Woola
aliases: Hound
is_fully_identified: true
manual_description_required: true
manual_description_reason: No specific physical description of the hound provided in this chapter.
clarification_required: false
clarification_reason: 
clarification_question: 
character_type_hint: animal
morphology_hint: quadruped
scale_hint: large
renderability_hint: renderable
confidence: 0.8
direct_identity_evidence: Identified as the protagonist's hound.
direct_visual_evidence: None in this chapter.
costume_or_covering_evidence: None.
movement_evidence: Traveling with the protagonist and Sola.
associated_entities: Protagonist, Sola
alias_or_role_evidence: 
unknowns: Specific breed/appearance of the hound.
source_refs: Chapter 8 summary.

[[SECTION markdown]]
# Woola
**Role:** Companion animal.
**Status:** Physically present.
**Physical Description:** A hound; specific appearance not detailed in this chapter.
**Notes:** Traveling with the protagonist and Sola.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
