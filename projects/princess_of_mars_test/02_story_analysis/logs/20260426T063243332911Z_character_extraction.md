# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-26T06:32:43.333418+00:00
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

Chapter id: CH001

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
The Arizona hills and mountains; specifically a remote gold-bearing quartz vein, a high plateau filled with Apache tepees, and a large, ancient cave located on a narrow trail between a cliff and a ravine.

**Characters:**
* **John Carter (Captain Jack Carter):** A former Confederate cavalry officer and seasoned fighter. He is characterized by an instinctive sense of duty that often overrides his survival instinct.
* **Captain James K. Powell:** A mining engineer and fellow Confederate officer; Carter's friend and partner in prospecting.
* **Apache Warriors:** A large group (approximately five hundred) encountered during a pursuit.

**Events:**
* **The Discovery:** Carter and Powell discover a massive gold vein in Arizona in 1865. They decide that Powell will return to civilization to secure machinery while Carter holds the claim.
* **The Pursuit:** After Powell departs, Carter observes suspicious movement in the valley. Suspecting an Apache ambush, he pursues the trail, discovering tracks of galloping ponies.
* **The Skirmish:** Carter discovers a large Apache camp on a plateau. He launches a sudden, violent charge with his revolvers, causing the warriors to scatter in confusion.
* **Finding Powell:** Amidst the chaos, Carter finds Powell dead, riddled with arrows. Carter retrieves the body to prevent mutilation and flees the plateau under heavy fire.
* **The Escape and the Cave:** While fleeing, Carter's horse takes a wrong turn, leading him away from the pursuit and toward a high cliff. He discovers a large, ancient cave at the end of a trail.
* **The End of the Journey:** After confirming Powell is dead, Carter enters the cave to explore. Overcome by extreme fatigue and a mysterious drowsiness, he collapses on the cave floor, marking the beginning of his ten-year disappearance.
````

## Raw Response
````text
[[FILMCREATOR_PACKET]]

task: character_extraction

version: 1

character_index_markdown:

[[SECTION character_index_markdown]]

# Character Index - CH001

- [john_carter](#john_carter)
- [james_k_powell](#james_k_powell)
- [apache_warriors](#apache_warriors)

[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: john_carter
canonical_character_id: CH002 John Carter
aliases: Captain Jack Carter
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
direct_identity_evidence: true
direct_visual_evidence: false
costume_or_covering_evidence: false
movement_evidence: true
associated_entities: james_k_powell, apache_warriors
alias_or_role_evidence: true
unknowns: 
source_refs: 
[[SECTION markdown]]
# John Carter
**Role:** Protagonist; former Confederate cavalry officer.
**Presence:** Physically present.
**Description:** A seasoned fighter with an instinctive sense of duty. Characterized by his combat proficiency with revolvers and riding ability.
**Notes:** Physical appearance (facial features, hair, specific clothing) is not detailed in this chapter beyond his military background/status.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: james_k_powell
canonical_character_id: CH003 James K. Powell
aliases: Captain Powell
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
direct_identity_evidence: true
direct_visual_evidence: false
costume_or_covering_evidence: false
movement_evidence: false
associated_entities: john_carter
alias_or_role_evidence: true
unknowns: 
source_refs: 
[[SECTION markdown]]
# James K. Powell
**Role:** Supporting character; mining engineer and Confederate officer.
**Presence:** Physically present (deceased).
**Description:** A friend and partner to John Carter. Found dead, riddled with arrows.
**Notes:** Specific visual details of his person are not provided beyond his role and cause of death.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: apache_warriors
canonical_character_id: CH004 Apache Warriors
aliases: Apache
is_fully_identified: false
manual_description_required: true
manual_description_reason: Group entity; specific individual features or distinct uniform/costume details are not provided.
clarification_required: false
clarification_reason: 
clarification_question: 
character_type_hint: humanoid_nonhuman
morphology_hint: biped
scale_hint: human_scale
renderability_hint: renderable
confidence: 0.8
direct_identity_evidence: true
direct_visual_evidence: false
costume_or_covering_evidence: false
movement_evidence: true
associated_entities: 
alias_or_role_evidence: true
unknowns: 
source_refs: 
[[SECTION markdown]]
# Apache Warriors
**Role:** Antagonists/Group.
**Presence:** Physically present (large group).
**Description:** A large group of approximately five hundred warriors encountered in the Arizona hills. They utilize ponies and arrows.
**Notes:** Specific visual descriptions of their attire, weaponry (beyond arrows), or physical appearance are absent.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
