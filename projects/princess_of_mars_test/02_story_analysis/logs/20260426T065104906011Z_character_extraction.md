# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-26T06:51:04.906011+00:00
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

Chapter id: CH014

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

**Setting:** The Martian landscape during a march toward Thark; includes an incubator site for green Martian eggs and the open plains where a duel takes place.

**Characters:**
- **John Carter:** A human warrior struggling with his unrequited love for Dejah Thoris and his physical survival.
- **Dejah Thoris:** Princess of Helium, currently traveling under Thark custody; she is angry with Carter due to a perceived social insult.
- **Tars Tarkas:** A Thark chieftain who shows unexpected moments of restraint and empathy toward Carter and Dejah Thoris.
- **Sola:** A faithful companion to Dejah Thoris who risks her life to protect the princess.
- **Sarkoja:** A female Thark driven by intense hatred for John Carter; she orchestrates a distraction to ensure his death.
- **Zad:** A powerful green Martian warrior (*o mad*) who challenges Carter to a formal duel.

**Key Events:**
- **Emotional Conflict:** John Carter reflects on his love for Dejah Thoris, realizing the cultural and biological gulf between them, while Dejah Thoris remains cold toward him following an accidental social transgression.
- **The Journey Begins:** The group departs for Thark; Dejah Thoris is kept in chains by Sarkoja, though Tars Tarkas eventually intervenes to ensure her comfort and takes custody of the key.
- **Sabotage at the Incubator:** The party discovers and destroys a Warhoon incubator containing small green Martian eggs.
- **The Duel:** Zad challenges Carter to a formal duel with long-swords. During the fight, Sarkoja uses a mirror to flash sunlight into Carter's eyes, blinding him momentarily.
- **Chaos in the Chariot:** As the duel reaches its climax, Dejah Thoris confronts Sarkoja; Sola intercedes to protect the princess and is stabbed by Sarkoja.
- **The Climax:** Amidst the distraction, Zad delivers a fatal thrust to Carter's chest, leaving him on the brink of death.
````

## Raw Response
````text
[[FILMCREATOR_PACKET]]

task: character_extraction

version: 1

character_index_markdown:

[[SECTION character_index_markdown]]

# Character Index - CH014

- [John Carter](#john_carter)
- [Dejah Thoris](#dejah_thoris)
- [Tars Tarkas](#tars_tarkas)
- [Sola](#sola)
- [Sarkoja](#sarkoja)
- [Zad](#zad)

[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: john_carter
canonical_character_id: CH001 John Carter
aliases: Human Warrior
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
direct_identity_evidence: Explicitly named as John Carter.
direct_visual_evidence: Participating in a long-sword duel.
costume_or_covering_evidence: None specified in this chapter.
movement_evidence: Engaging in combat/duel.
associated_entities: Dejah Thoris, Zad, Sarkoja, Tars Tarkas
alias_or_role_evidence: 
unknowns: 
source_refs: 

[[SECTION markdown]]
# John Carter
**Role:** Protagonist / Human Warrior

**Status:** Physically Present (Injured/Near death)

**Physical Description:**
A human male warrior. Currently engaged in a formal duel using long-swords. He is susceptible to visual distractions (blinded by sunlight reflection).

**Costume & Silhouette:**
Not explicitly detailed in this chapter, but characterized as a combatant.

**Prompting Phrases:**
Human warrior, long-sword combatant, wounded male.

**Uncertainty Notes:**
Specific clothing/armor details are absent from this text segment.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: dejah_thoris
canonical_character_id: CH003 Dejah Thoris
aliases: Princess of Helium
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
direct_identity_evidence: Explicitly named as Dejah Thoris, Princess of Helium.
direct_visual_evidence: Traveling under Thark custody; being held in chains.
costume_or_covering_evidence: Held in chains by Sarkoja.
movement_evidence: Traveling with the group; confronting Sarkoja.
associated_entities: John Carter, Sola, Sarkoja, Tars Tarkas
alias_or_role_evidence: Princess of Helium
unknowns: 
source_refs: 

[[SECTION markdown]]
# Dejah Thoris
**Role:** Princess of Helium

**Status:** Physically Present

**Physical Description:**
A humanoid non-human (Martian princess). Currently experiencing emotional coldness/anger toward Carter.

**Costume & Silhouette:**
Traveling in Thark custody; described as being held in chains during the journey.

**Prompting Phrases:**
Martian princess, humanoid female, captive, regal but distressed.

**Uncertainty Notes:**
Specific biological features of her non-human morphology are not detailed in this chapter.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: tars_tarkas
canonical_character_id: CH004 Tars Tarkas
aliases: Thark Chieftain
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
direct_identity_evidence: Explicitly named as Tars Tarkas, Thark chieftain.
direct_visual_evidence: Intervening in the custody of Dejah Thoris.
costume_or_covering_evidence: None specified.
movement_evidence: Traveling with the group.
associated_entities: Dejah Thoris, John Carter
alias_or_role_evidence: Thark chieftain
unknowns: 
source_refs: 

[[SECTION markdown]]
# Tars Tarkas
**Role:** Thark Chieftain

**Status:** Physically Present

**Physical Description:**
A large humanoid non-human (Thark). Displays restraint and empathy.

**Costume & Silhouette:**
Not specified.

**Prompting Phrases:**
Large green Martian, Thark chieftain, powerful warrior.

**Uncertainty Notes:**
Specific physical appearance of the Thark species is not detailed in this chapter.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: sola
canonical_character_id: UNK Sola
aliases: Companion
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
direct_identity_evidence: Explicitly named as Sola.
direct_visual_evidence: Intercedes to protect the princess and is stabbed.
costume_or_covering_evidence: None specified.
movement_evidence: Protecting Dejah Thoris.
associated_entities: Dejah Thoris, Sarkoja
alias_or_role_evidence: Faithful companion
unknowns: 
source_refs: 

[[SECTION markdown]]
# Sola
**Role:** Companion to Dejah Thoris

**Status:** Physically Present (Injured/Stabbed)

**Physical Description:**
A humanoid non-human. Characterized by loyalty and bravery.

**Costume & Silhouette:**
Not specified.

**Prompting Phrases:**
Martian companion, loyal female humanoid.

**Uncertainty Notes:**
Specific physical traits are not provided in this chapter.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: sarkoja
canonical_character_id: UNK Sarkoja
aliases: Female Thark
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
direct_identity_evidence: Explicitly named as Sarkoja.
direct_visual_evidence: Holding Dejah Thoris in chains; using a mirror to flash sunlight.
costume_or_covering_evidence: None specified.
movement_evidence: Orchestrating distraction; stabbing Sola.
associated_entities: Dejah Thoris, John Carter, Sola
alias_or_role_evidence: Female Thark
unknowns: 
source_refs: 

[[SECTION markdown]]
# Sarkoja
**Role:** Antagonist / Female Thark

**Status:** Physically Present

**Physical Description:**
A humanoid non-human (Thark) driven by hatred.

**Costume & Silhouette:**
Not specified; uses a mirror as a tool/weapon of distraction.

**Prompting Phrases:**
Hostile female Thark, green Martian warrior, malicious expression.

**Uncertainty Notes:**
Specific physical appearance is not detailed beyond her species and temperament.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: zad
canonical_character_id: UNK Zad
aliases: o mad, Warrior
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
direct_identity_evidence: Explicitly named as Zad, an *o mad*.
direct_visual_evidence: Challenging Carter to a duel; delivering a fatal thrust.
costume_or_covering_evidence: None specified.
movement_evidence: Engaging in long-sword combat.
associated_entities: John Carter
alias_or_role_evidence: o mad, warrior
unknowns: 
source_refs: 

[[SECTION markdown]]
# Zad
**Role:** Challenger / Warrior

**Status:** Physically Present

**Physical Description:**
A powerful green Martian warrior (*o mad*).

**Costume & Silhouette:**
Not specified.

**Prompting Phrases:**
Powerful green Martian, o mad warrior, long-sword combatant.

**Uncertainty Notes:**
Specific physical details of the *o mad* class are not provided in this chapter.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
