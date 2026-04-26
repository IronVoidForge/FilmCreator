# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-26T06:56:48.363263+00:00
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

Chapter id: CH018

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
The chapter moves from a small room within a Warhoon camp to the open Martian plains during a military march, and finally to a pitch-black, subterranean dungeon within the city of Warhoon.

**Characters:**
* **Protagonist:** A human captive who survives severe injuries through mysterious medical treatments but suffers extreme psychological trauma due to isolation and darkness.
* **Dak Kova:** A scarred, ferocious Warhoon warrior/jed; an insubordinate lieutenant who eventually murders his leader to become the new Jeddak.
* **Bar Comas:** The young, dignified Jeddak of the Warhoons who is killed in a primal duel with Dak Kova.
* **The Female Healer:** An ancient, ugly Warhoon woman who treats the protagonist's wounds.
* **Warhoon Warriors/Jailer:** A bloodthirsty horde characterized by their use of human skulls and hands as ornamentation; includes the silent jailer killed by the protagonist.

**Key Events:**
* **Recovery and Transport:** The protagonist regains consciousness, healed by a Warhoon female, and is strapped to a wild thoat to be transported to the main Warhoon column.
* **The Duel of the Jeddaks:** Dak Kova openly defies Bar Comas, leading to a savage, animalistic hand-to-hand combat between the two leaders. Dak Kova kills Bar Comas with a tusk thrust and seizes power.
* **The March to Warhoon:** The Warhoon horde, numbering ten thousand, retreats toward their city after the duel delays their raid on the Tharks.
* **Imprisonment:** The protagonist is cast into a dark dungeon in Warhoon, where he endures weeks or months of sensory deprivation and terror from unseen creatures.
* **The Escape Attempt:** Driven to near-madness, the protagonist ambushes his food deliverer with a heavy chain, killing him. He recovers his senses upon finding the jailer's keys but is immediately confronted by the glowing eyes of unseen entities in the darkness.
````

## Raw Response
````text
[[FILMCREATOR_PACKET]]

task: character_extraction

version: 1

character_index_markdown:

[[SECTION character_index_markdown]]

# Character Index - Chapter 018

- [Protagonist](#protagonist)
- [Dak Kova](#dak-kova)
- [Bar Comas](#bar-comas)
- [The Female Healer](#the-female-healer)
- [Warhoon Warriors/Jailer](#warhoon-warriors-jailer)

[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: protagonist
canonical_character_id: CH002 Protagonist
aliases: Captive, Human
is_fully_identified: true
manual_description_required: true
manual_description_reason: Physical appearance is not described beyond being human and suffering injuries/trauma.
clarification_required: false
clarification_reason: 
clarification_question: 
character_type_hint: human
morphology_hint: biped
scale_hint: human_scale
renderability_hint: renderable
confidence: 1.0
direct_identity_evidence: Explicitly identified as a human captive.
direct_visual_evidence: None (internal perspective).
costume_or_covering_evidence: Strapped to a thoat; later in a dungeon.
movement_evidence: Surviving injuries, ambushing jailer with a chain.
associated_entities: Dak Kova, Bar Comas, The Female Healer, Warhoon Warriors/Jailer
alias_or_role_evidence: Referred to as the captive and survivor of medical treatments.
unknowns: Facial features, hair color, specific build.
source_refs: Chapter 018

[[SECTION markdown]]
# Protagonist
**Role:** Human captive / Survivor
**Presence:** Physically present (POV)

**Physical Description:**
A human male suffering from severe physical injuries and extreme psychological trauma. He is capable of sudden, desperate violence (killing a jailer with a chain).

**Costume/Silhouette:**
Likely disheveled or wounded; strapped to a mount during transport; later confined in darkness.

**Notes:**
Visuals should focus on the state of injury and the psychological toll of sensory deprivation. Specific facial features are unstated.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: dak_kova
canonical_character_id: CH018 Dak Kova
aliases: Lieutenant, New Jeddak
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
direct_identity_evidence: Named as Dak Kova; identified as a Warhoon warrior/jed.
direct_visual_evidence: Described as scarred and ferocious.
costume_or_covering_evidence: Warrior attire (implied).
movement_evidence: Engages in primal, animalistic hand-to-hand combat; kills Bar Comas with a tusk thrust.
associated_entities: Bar Comas, Warhoon Warriors
alias_or_role_evidence: Insubordinate lieutenant who becomes Jeddak.
unknowns: Specific facial structure beyond scarring.
source_refs: Chapter 018

[[SECTION markdown]]
# Dak Kova
**Role:** Antagonist / Usurper
**Presence:** Physically present

**Physical Description:**
A ferocious and scarred Warhoon warrior. He possesses a primal, animalistic combat style.

**Costume/Silhouette:**
Warhoon warrior gear; likely carries or utilizes tusks as weapons.

**Notes:**
Characterized by ferocity and sudden, violent ascension to power. The scarring is a key visual identifier.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: bar_comas
canonical_character_id: CH018 Bar Comas
aliases: Jeddak
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
direct_identity_evidence: Named as Bar Comas; identified as the Jeddak of the Warhoons.
direct_visual_evidence: Dignified presence.
costume_or_covering_evidence: Likely wears leadership regalia/armor.
movement_evidence: Engages in a primal duel with Dak Kova.
associated_entities: Dak Kova, Warhoon Warriors
alias_or_role_evidence: The young leader of the Warhoon horde.
unknowns: Specific physical features beyond "dignified."
source_refs: Chapter 018

[[SECTION markdown]]
# Bar Comas
**Role:** Fallen Leader
**Presence:** Physically present (deceased)

**Physical Description:**
A young and dignified Warhoon leader.

**Costume/Silhouette:**
Likely more ornate or formal than a standard warrior, reflecting his status as Jeddak.

**Notes:**
His death marks the shift in Warhoon leadership from dignity to Dak Kova's primal rule.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: female_healer
canonical_character_id: CH018 Female Healer
aliases: Ancient Woman
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
direct_identity_evidence: Identified as a Warhoon female healer.
direct_visual_evidence: Ancient and ugly.
costume_or_covering_evidence: None specified.
movement_evidence: Treats the protagonist's wounds.
associated_entities: Protagonist
alias_or_role_evidence: Healer for the captive.
unknowns: Specific clothing or exact age details.
source_refs: Chapter 018

[[SECTION markdown]]
# The Female Healer
**Role:** Supporting Character
**Presence:** Physically present

**Physical Description:**
An ancient, ugly Warhoon woman.

**Costume/Silhouette:**
Unspecified; likely practical or tribal healer attire.

**Notes:**
Provides the medical intervention that allows the protagonist to survive his initial injuries.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: warhoon_warriors_jailer
canonical_character_id: CH018 Warhoon Horde
aliases: Jailer, Bloodthirsty Horde
is_fully_identified: false
manual_description_required: true
manual_description_reason: The group is a collective; individual jailers lack specific physical descriptions beyond being "silent" or "bloodthirsty."
clarification_required: false
clarification_reason: 
clarification_question: 
character_type_hint: humanoid_nonhuman
morphology_hint: biped
scale_hint: large
renderability_hint: renderable
confidence: 0.7
direct_identity_evidence: Identified as Warhoon warriors and a jailer.
direct_visual_evidence: Use human skulls and hands as ornamentation.
costume_or_covering_evidence: Ornamented with human remains (skulls/hands).
movement_evidence: Marching in a column of ten thousand; delivering food to the dungeon.
associated_entities: Protagonist, Dak Kova, Bar Comas
alias_or_role_evidence: The horde and the specific jailer killed by the protagonist.
unknowns: Individual facial features or specific armor types.
source_refs: Chapter 018

[[SECTION markdown]]
# Warhoon Warriors / Jailer
**Role:** Antagonists / Background Horde
**Presence:** Physically present (Horde) and Referenced (Jailer)

**Physical Description:**
A bloodthirsty, massive horde of ten thousand. They are characterized by a macabre aesthetic, using human skulls and hands as ornamentation on their person/gear.

**Costume/Silhouette:**
Tribal/warrior attire heavily decorated with human remains.

**Notes:**
The collective "horde" should feel overwhelming in scale. The individual jailer is a specific target for the protagonist's desperation.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
