# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-26T06:35:21.749894+00:00
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

**Setting:** A circular basin on Mars covered in yellowish, moss-like vegetation, featuring quartz-bearing rock outcroppings and a low, walled glass enclosure (an incubator).

**Events:**
- The protagonist wakes up on Mars and discovers the effects of low gravity, finding that even simple movements result in massive leaps.
- He explores a nearby glass-roofed enclosure and observes several hundred large white eggs; some have hatched into grotesque, six-limbed creatures with independent eyes and antennae.
- A party of twenty Martian warriors on eight-legged mounts approaches. The leader nearly kills the protagonist with a forty-foot spear, but the protagonist escapes by performing a massive thirty-foot leap over the incubator.
- Impressed by his agility rather than threatened by him, the Martians view him as a curiosity rather than an enemy.
- The leader of the party dismounts, approaches unarmed, and offers a metal armlet as a gesture of peace. 
- The protagonist accepts the armlet, signaling friendship. He is then hoisted onto a Martian mount and taken away by the cavalcade toward distant hills.

**Characters:**
- **The Protagonist:** An Earthman, currently naked and unarmed, possessing superhuman agility due to the Martian gravity.
- **Martian Warriors:** Fifteen-foot-tall humanoids with four arms (two right, two left), olive-green skin, and blood-red eyes. They are highly skilled with long spears and advanced radium-projectile rifles.
- **The Leader:** A prominent Martian warrior who initiates peaceful contact through gesture and a gift of an armlet.

**Key Elements/Technology:**
- **Martian Mounts:** Massive, eight-legged animals with slate-colored skin and no hair.
- **Martian Rifles:** Highly advanced weapons made of white metal and hard wood, capable of extreme long-range accuracy (up to 200+ miles).
- **The Incubator:** A glass-roofed structure used for hatching Martian lifeforms.
````

## Raw Response
````text
[[FILMCREATOR_PACKET]]

task: character_extraction

version: 1

character_index_markdown:

[[SECTION character_index_markdown]]

# Character Index - CH003

- [Protagonist](#protagonist)
- [Martian Warriors](#martian-warriors)
- [The Leader](#the-leader)
- [Grotesque Creatures](#grotesque-creatures)
- [Martian Mounts](#martian-mounts)

[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: protagonist
canonical_character_id: CH003 Protagonist
aliases: Earthman
is_fully_identified: false
manual_description_required: true
manual_description_reason: Physical appearance (face, hair, build) is not described; only state of dress (naked) and physical capability are noted.
clarification_required: true
clarification_reason: Specific facial features and body type are missing for consistent rendering.
clarification_question: What is the protagonist's hair color, eye color, ethnicity/build, and approximate age?
character_type_hint: human
morphology_hint: biped
scale_hint: human_scale
renderability_hint: renderable
confidence: 0.9
direct_identity_evidence: "An Earthman"
direct_visual_evidence: "naked and unarmed"
costume_or_covering_evidence: none
movement_evidence: "massive thirty-foot leap", "superhuman agility due to the Martian gravity"
associated_entities: Martian Warriors, The Leader, Martian Mounts
alias_or_role_evidence: "The protagonist"
unknowns: facial features, hair, eye color, body type
source_refs: CH003

[[SECTION markdown]]
# Protagonist
**Role:** Central character / Explorer.
**Status:** Physically present.
**Physical Description:** An Earthman described as naked and unarmed during the encounter. Possesses superhuman agility and leaping ability due to low Martian gravity.
**Costume/Silhouette:** Naked; no clothing or equipment mentioned in this chapter.
**Prompt Phrases:** human male, naked, agile, leaping, Earthling.
**Uncertainty Notes:** No facial features, hair color, or specific body morphology provided.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: martian_warriors
canonical_character_id: CH003 Martian Warriors
aliases: Martians
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
confidence: 0.95
direct_identity_evidence: "Martian warriors"
direct_visual_evidence: "Fifteen-foot-tall humanoids with four arms (two right, two left), olive-green skin, and blood-red eyes."
costume_or_covering_evidence: armed with long spears and radium-projectile rifles.
movement_evidence: riding eight-legged mounts.
associated_entities: The Leader, Martian Mounts
alias_or_role_evidence: "A party of twenty Martian warriors"
unknowns: 
source_refs: CH003

[[SECTION markdown]]
# Martian Warriors
**Role:** Encountered group / Potential antagonists turned curious observers.
**Status:** Physically present.
**Physical Description:** Fifteen-foot-tall humanoids with olive-green skin and blood-red eyes. They possess four arms (two on the right, two on the left).
**Costume/Silhouette:** Equipped with long spears and advanced white metal/hard wood radium-projectile rifles.
**Prompt Phrases:** 15-foot tall humanoid, four arms, olive-green skin, red eyes, Martian warrior, wielding spear.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: martian_leader
canonical_character_id: CH003 Martian Leader
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
direct_identity_evidence: "The leader of the party"
direct_visual_evidence: "dismounts, approaches unarmed, and offers a metal armlet"
costume_or_covering_evidence: carries/offers a metal armlet.
movement_evidence: dismounts from mount.
associated_entities: Martian Warriors, Protagonist, Martian Mounts
alias_or_role_evidence: "The leader of the party"
unknowns: specific facial features beyond species traits.
source_refs: CH003

[[SECTION markdown]]
# The Leader
**Role:** Diplomat / Leader of the Martian party.
**Status:** Physically present.
**Physical Description:** A member of the Martian warrior race (15ft tall, four arms, olive-green skin, red eyes).
**Costume/Silhouette:** Approaches unarmed; carries a metal armlet as a peace offering.
**Prompt Phrases:** large four-armed humanoid, olive-green skin, red eyes, holding metal armlet, peaceful gesture.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: grotesque_creatures
canonical_character_id: CH003 Grotesque Creatures
aliases: Hatched creatures
is_fully_identified: true
manual_description_required: false
manual_description_reason: 
clarification_required: false
clarification_reason: 
clarification_question: 
character_type_hint: creature
morphology_hint: multi_legged
scale_hint: small
renderability_hint: renderable
confidence: 0.85
direct_identity_evidence: "grotesque, six-limbed creatures"
direct_visual_evidence: "six-limbed creatures with independent eyes and antennae"
costume_or_covering_evidence: none
movement_evidence: hatched from eggs in the incubator.
associated_entities: The Incubator
alias_or_role_evidence: "hatched into grotesque, six-limbed creatures"
unknowns: exact size/scale relative to human.
source_refs: CH003

[[SECTION markdown]]
# Grotesque Creatures
**Role:** Background lifeforms / Hatchlings.
**Status:** Physically present (in incubator).
**Physical Description:** Six-limbed creatures featuring independent eyes and antennae. Described as "grotesque."
**Costume/Silhouette:** Small, emerging from large white eggs.
**Prompt Phrases:** six-limbed creature, independent eyes, antennae, grotesque alien lifeform, small creature.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: martian_mounts
canonical_character_id: CH003 Martian Mounts
aliases: 
is_fully_identified: true
manual_description_required: false
manual_description_reason: 
clarification_required: false
clarification_reason: 
clarification_question: 
character_type_hint: animal
morphology_hint: multi_legged
scale_hint: large
renderability_hint: renderable
confidence: 0.95
direct_identity_evidence: "Martian mounts"
direct_visual_evidence: "eight-legged animals with slate-colored skin and no hair."
costume_or_covering_evidence: none
movement_evidence: carrying warriors; being ridden by the protagonist at the end.
associated_entities: Martian Warriors, The Leader, Protagonist
alias_or_role_evidence: "Martian mounts"
unknowns: 
source_refs: CH003

[[SECTION markdown]]
# Martian Mounts
**Role:** Transport/Beasts of burden.
**Status:** Physically present.
**Physical Description:** Massive, eight-legged animals with slate-colored skin and no hair.
**Costume/Silhouette:** Large quadrupedal (octopedal) beasts.
**Prompt Phrases:** massive eight-legged animal, slate-colored skin, hairless, alien mount, large beast.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
