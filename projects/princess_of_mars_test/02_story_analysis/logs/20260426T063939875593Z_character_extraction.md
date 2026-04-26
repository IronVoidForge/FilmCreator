# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-26T06:39:39.875593+00:00
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

Chapter id: CH006

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

**Setting:** An interior chamber within a Martian building, overlooking a plaza.

**Characters:**
* **The Protagonist (Earthman):** A survivor who uses Earthly combat tactics to defend himself.
* **The Watch-thing:** A loyal, multi-legged, beast-like creature that acts as the protagonist's guardian.
* **The Bull Apes:** Two massive, ten-to-fifteen-foot tall, ape-like creatures with four arms and immense strength.
* **Tars Tarkas:** A Martian warrior who observes and respects the protagonist's combat skills.
* **Sola:** A Martian woman who shows uncharacteristic compassion and solicitude toward the protagonist.
* **Martian Warriors:** A group of warriors who value physical bravery above all else.

**Events:**
* **The Ambush:** The protagonist is pinned by one massive bull ape while its mate approaches with a stone cudgel to kill him.
* **The Battle of the Beasts:** The protagonist's watch-thing intervenes, engaging the first ape in a ferocious struggle. As the watch-thing begins to succumb to the ape's strength, the protagonist seizes the fallen cudgel and crushes the ape's skull.
* **The Second Duel:** The second bull ape, enraged by its mate's death, charges the protagonist. Despite the overwhelming physical disadvantage, the protagonist uses a combination of throwing the cudgel and tactical hand-to-hand strikes to incapacitate and kill the creature.
* **Martian Observation:** Tars Tarkas, Sola, and a group of warriors arrive, having witnessed the fight. They applaud the protagonist's prowess, viewing his combat as a demonstration of high social value.
* **Conflict over the Beast:** The Martians attempt to execute the wounded watch-thing. The protagonist intervenes physically to stop a warrior from shooting the creature. 
* **Resolution:** Tars Tarkas allows the protagonist to keep his beast. The protagonist realizes he has formed two distinct types of bonds: a compassionate connection with Sola and a loyal, primal bond with his watch-thing.
````

## Raw Response
````text
[[FILMCREATOR_PACKET]]

task: character_extraction

version: 1

character_index_markdown:

[[SECTION character_index_markdown]]

# Character Index - CH006

| Asset ID | Canonical ID | Role/Description | Status |
| :--- | :--- | :--- | :--- |
| protagonist | CH002 Protagonist | Earthman survivor; combatant | Physically Present |
| watch_thing | CH005 Watch-thing | Multi-legged guardian beast | Physically Present |
| bull_ape_1 | CH007 Bull Ape | Massive, four-armed ape creature | Deceased (Physically Present) |
| bull_ape_2 | CH007 Bull Ape | Massive, four-armed ape creature | Deceased (Physically Present) |
| tars_tarkas | CH003 Tars Tarkas | Martian warrior; observer | Physically Present |
| sola | CH004 Sola | Compassionate Martian woman | Physically Present |
| martian_warriors | CH008 Martian Warriors | Group of combat-focused Martians | Physically Present |

[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: protagonist
canonical_character_id: CH002 Protagonist
aliases: Earthman
is_fully_identified: true
manual_description_required: true
manual_description_reason: Physical appearance (clothing, facial features, hair) is not described in this chapter.
clarification_required: false
clarification_reason: 
clarification_question: 
character_type_hint: human
morphology_hint: biped
scale_hint: human_scale
renderability_hint: renderable
confidence: 0.9
direct_identity_evidence: Explicitly identified as the protagonist/Earthman.
direct_visual_evidence: Engages in hand-to-hand combat and uses a stone cudgel.
costume_or_covering_evidence: None provided in text.
movement_evidence: Uses Earthly combat tactics, throwing weapons, and tactical strikes.
associated_entities: watch_thing, sola, tars_tarkas
alias_or_role_evidence: Referred to as the survivor/Earthman.
unknowns: Physical appearance, clothing, specific gear.
source_refs: CH006

[[SECTION markdown]]
# Protagonist
**Role:** Survivor and combatant.
**Status:** Physically Present.
**Description:** An Earthman who utilizes tactical hand-to-hand combat and improvised weaponry (a stone cudgel) to defend himself against much larger creatures. 
**Visual Notes:** Physical appearance is currently unknown; requires definition for clothing and facial features. Combat style is disciplined/tactical rather than purely primal.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: watch_thing
canonical_character_id: CH005 Watch-thing
aliases: The Beast, Guardian
is_fully_identified: true
manual_description_required: false
manual_description_reason: 
clarification_required: false
clarification_reason: 
clarification_question: 
character_type_hint: creature
morphology_hint: multi_legged
scale_hint: large
renderability_hint: renderable
confidence: 0.8
direct_identity_evidence: Identified as the protagonist's loyal guardian.
direct_visual_evidence: Multi-legged, beast-like appearance; engages in ferocious struggle with a bull ape.
costume_or_covering_evidence: None.
movement_evidence: Fights ferociously; wounded during combat.
associated_entities: protagonist
alias_or_role_evidence: Described as a loyal, multi-legged beast.
unknowns: Specific number of legs, skin texture/color.
source_refs: CH006

[[SECTION markdown]]
# Watch-thing
**Role:** Protagonist's loyal guardian.
**Status:** Physically Present (Wounded).
**Description:** A large, multi-legged creature that acts as a protector for the protagonist. 
**Visual Notes:** Beast-like morphology; multi-legged; engages in high-intensity combat.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: bull_ape
canonical_character_id: CH007 Bull Ape
aliases: Massive ape, mate
is_fully_identified: true
manual_description_required: false
manual_description_reason: 
clarification_required: false
clarification_reason: 
clarification_question: 
character_type_hint: creature
morphology_hint: quadruped
scale_hint: large
renderability_hint: renderable
confidence: 0.9
direct_identity_evidence: Identified as Bull Apes.
direct_visual_evidence: Ten-to-fifteen feet tall, four arms, massive strength, ape-like.
costume_or_covering_evidence: None.
movement_evidence: Charges the protagonist; pins him down.
associated_entities: protagonist
alias_or_role_evidence: Described as massive, ten-to-fifteen-foot tall creatures.
unknowns: Specific fur color or facial features.
source_refs: CH006

[[SECTION markdown]]
# Bull Ape
**Role:** Antagonist/Combatant.
**Status:** Physically Present (Deceased).
**Description:** Massive, ape-like creatures standing 10-15 feet tall. They possess four arms and immense physical strength.
**Visual Notes:** Large scale; four-armed morphology; heavy/powerful silhouette.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: tars_tarkas
canonical_character_id: CH003 Tars Tarkas
aliases: 
is_fully_identified: true
manual_description_required: true
manual_description_reason: Physical appearance of the Martian warrior is not detailed in this chapter.
clarification_required: false
clarification_reason: 
clarification_question: 
character_type_hint: humanoid_nonhuman
morphology_hint: biped
scale_hint: human_scale
renderability_hint: renderable
confidence: 0.7
direct_identity_evidence: Named character; Martian warrior.
direct_visual_evidence: Observes the fight; applauds the protagonist.
costume_or_covering_evidence: None mentioned.
movement_evidence: Arrives at the scene with Sola and warriors.
associated_entities: sola, martian_warriors, protagonist
alias_or_role_evidence: Identified as a Martian warrior who respects combat prowess.
unknowns: Physical appearance, clothing, specific Martian features.
source_refs: CH006

[[SECTION markdown]]
# Tars Tarkas
**Role:** Martian warrior and observer.
**Status:** Physically Present.
**Description:** A Martian warrior who values physical bravery and combat skill. He shows respect for the protagonist's ability to kill the bull apes.
**Visual Notes:** Physical appearance (Martian features/clothing) is not provided in this text.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: sola
canonical_character_id: CH004 Sola
aliases: 
is_fully_identified: true
manual_description_required: true
manual_description_reason: Physical appearance of the Martian woman is not detailed in this chapter.
clarification_required: false
clarification_reason: 
clarification_question: 
character_type_hint: humanoid_nonhuman
morphology_hint: biped
scale_hint: human_scale
renderability_hint: renderable
confidence: 0.7
direct_identity_evidence: Named character; Martian woman.
direct_visual_evidence: Shows compassion and solicitude toward the protagonist.
costume_or_covering_evidence: None mentioned.
movement_evidence: Arrives at the scene with Tars Tarkas.
associated_entities: protagonist, tars_tarkas
alias_or_role_evidence: Described as a Martian woman showing compassion.
unknowns: Physical appearance, clothing, specific Martian features.
source_refs: CH006

[[SECTION markdown]]
# Sola
**Role:** Compassionate Martian woman.
**Status:** Physically Present.
**Description:** A Martian woman who exhibits uncharacteristic compassion and solicitude toward the protagonist.
**Visual Notes:** Physical appearance (Martian features/clothing) is not provided in this text.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: martian_warriors
canonical_character_id: CH008 Martian Warriors
aliases: 
is_fully_identified: true
manual_description_required: true
manual_description_reason: Individual descriptions are not provided; they are a collective group.
clarification_required: false
clarification_reason: 
clarification_question: 
character_type_hint: group
morphology_hint: biped
scale_hint: human_scale
renderability_hint: context_only
confidence: 0.6
direct_identity_evidence: Identified as a group of warriors.
direct_visual_evidence: They applaud the protagonist; one attempts to shoot the watch-thing.
costume_or_covering_evidence: None mentioned.
movement_evidence: Arrive at the scene; attempt to execute the wounded beast.
associated_entities: tars_tarkas, sola
alias_or_role_evidence: Described as warriors who value physical bravery.
unknowns: Individual appearances, specific armor/weapons.
source_refs: CH006

[[SECTION markdown]]
# Martian Warriors
**Role:** Group of combat-focused Martians.
**Status:** Physically Present.
**Description:** A group of Martian warriors who prize physical bravery and combat prowess. They initially attempt to execute the protagonist's wounded beast.
**Visual Notes:** Collective group; likely armed (one attempts to shoot). Specific visual details are absent.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
