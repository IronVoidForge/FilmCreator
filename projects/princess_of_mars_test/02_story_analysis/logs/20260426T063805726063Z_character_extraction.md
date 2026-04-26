# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-26T06:38:05.726063+00:00
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

Chapter id: CH005

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

**Setting:** A captive's chamber decorated with beautiful murals of Martian landscapes; a deserted city street; and the interior of a building overlooking a valley.

**Characters:**
* **The Protagonist:** An adventurous human captive attempting to test his limits and escape.
* **Sola:** A kind and sympathetic female Martian who provides food, drink, and warmth to the protagonist.
* **The Watch Dog:** A ferocious, short-legged but incredibly fast Martian beast used for protection and hunting; it acts as a constant guardian/pursuer.
* **The Colossal Creature:** A large, white, hairless, ape-like being with a shock of bristly hair that captures the protagonist.

**Events:**
* Sola leaves the protagonist under the guard of a ferocious Martian beast that blocks the room's exit.
* The protagonist observes the room's murals and learns about Martian biology (the milk-producing plant) and the planet's moons/night cycles through narration.
* Sola returns to provide food (cheese-like substance) and drink (plant-derived milk), and later covers the sleeping protagonist with furs during the cold Martian night.
* Seeking to test the watch dog's capabilities, the protagonist attempts to leave the room. The beast follows him at a distance until they reach the edge of the city.
* The beast suddenly charges the protagonist with extreme speed. The protagonist uses his jumping ability to evade the creature and leaps into a window thirty feet above the ground.
* After successfully pulling himself onto the windowsill, the protagonist is grabbed from behind by a massive, ape-like creature and dragged into a room.
````

## Raw Response
````text
[[FILMCREATOR_PACKET]]

task: character_extraction

version: 1

character_index_markdown:

[[SECTION character_index_markdown]]

# Character Index - CH005

| Asset ID | Canonical ID | Role | Status |
| :--- | :--- | :--- | :--- |
| protagonist | Protagonist | Captive / Adventurer | Physically Present |
| sola | Sola | Sympathetic Martian Caretaker | Physically Present |
| watch_dog | The Watch Dog | Guardian Beast | Physically Present |
| colossal_creature | The Colossal Creature | Captor | Physically Present |

[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: protagonist
canonical_character_id: Protagonist
aliases: Captive
is_fully_identified: true
manual_description_required: true
manual_description_reason: Physical appearance (age, hair, build) is not described in this chapter.
clarification_required: false
clarification_reason: 
clarification_question: 
character_type_hint: human
morphology_hint: biped
scale_hint: human_scale
renderability_hint: renderable
confidence: 1.0
direct_identity_evidence: Explicitly identified as a human captive.
direct_visual_evidence: Demonstrates jumping ability/agility.
costume_or_covering_evidence: None specified.
movement_evidence: High agility; capable of leaping into a window thirty feet above the ground.
associated_entities: sola, watch_dog, colossal_creature
alias_or_role_evidence: Referred to as the captive attempting to escape.
unknowns: Physical facial features and clothing details.
source_refs: Chapter 5 summary.

[[SECTION markdown]]
# Protagonist
**Role:** Adventurous human captive.
**Status:** Physically Present.

**Physical Description:**
Human male (implied). High level of physical fitness/agility; capable of a thirty-foot vertical leap to reach a windowsill. Specific facial features, hair, or clothing are not described in this chapter.

**Costume & Silhouette:**
Unknown.

**Prompting Nouns:**
Adventurous human, agile captive, jumper.

**Uncertainty Notes:**
Visual appearance is entirely unstated; requires character design sheet for consistency.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: sola
canonical_character_id: Sola
aliases: 
is_fully_identified: true
manual_description_required: true
manual_description_reason: Specific physical features (hair, eyes, skin color) are not provided.
clarification_required: false
clarification_reason: 
clarification_question: 
character_type_hint: humanoid_nonhuman
morphology_hint: biped
scale_hint: human_scale
renderability_hint: renderable
confidence: 0.9
direct_identity_evidence: Named as a female Martian.
direct_visual_evidence: None.
costume_or_covering_evidence: Provides furs to the protagonist.
movement_evidence: None.
associated_entities: protagonist
alias_or_role_evidence: Described as kind and sympathetic.
unknowns: Physical appearance, clothing style.
source_refs: Chapter 5 summary.

[[SECTION markdown]]
# Sola
**Role:** Sympathetic Martian caretaker.
**Status:** Physically Present.

**Physical Description:**
A female Martian. Characterized by kindness and sympathy through her actions (providing food, drink, and warmth). Specific morphology or appearance is not detailed.

**Costume & Silhouette:**
Unknown.

**Prompting Nouns:**
Kind Martian woman, sympathetic caretaker, humanoid alien.

**Uncertainty Notes:**
Specific Martian physiology/appearance needs definition to avoid generic human tropes.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: watch_dog
canonical_character_id: The Watch Dog
aliases: Martian beast, guardian
is_fully_identified: true
manual_description_required: false
manual_description_reason: 
clarification_required: false
clarification_reason: 
clarification_question: 
character_type_hint: creature
morphology_hint: unknown
scale_hint: small
renderability_hint: renderable
confidence: 0.7
direct_identity_evidence: Identified as a Martian beast used for protection/hunting.
direct_visual_evidence: Short-legged, incredibly fast.
costume_or_covering_evidence: None.
movement_evidence: Extremely fast; charges with sudden speed; follows at a distance.
associated_entities: protagonist, sola
alias_or_role_evidence: Acts as a constant guardian/pursuer.
unknowns: Specific limb count or head shape.
source_refs: Chapter 5 summary.

[[SECTION markdown]]
# The Watch Dog
**Role:** Ferocious Martian guardian beast.
**Status:** Physically Present.

**Physical Description:**
A ferocious Martian creature with short legs. It is characterized by extreme speed and sudden, aggressive charging capabilities.

**Costume & Silhouette:**
Short-legged, predatory silhouette.

**Prompting Nouns:**
Fast short-legged beast, predatory Martian creature, ferocious guardian animal.

**Uncertainty Notes:**
Morphology (e.g., number of legs or specific animal type) is not explicitly defined beyond "short-legged."
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: colossal_creature
canonical_character_id: The Colossal Creature
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
confidence: 1.0
direct_identity_evidence: Described as a massive, ape-like being.
direct_visual_evidence: Large, white, hairless, with a shock of bristly hair.
costume_or_covering_evidence: None.
movement_evidence: Grabs and drags the protagonist from behind.
associated_entities: protagonist
alias_or_role_evidence: Captures the protagonist.
unknowns: 
source_refs: Chapter 5 summary.

[[SECTION markdown]]
# The Colossal Creature
**Role:** Captor.
**Status:** Physically Present.

**Physical Description:**
A massive, ape-like being. It is white and hairless, except for a distinct shock of bristly hair.

**Costume & Silhouette:**
Large, heavy, ape-like silhouette; white skin.

**Prompting Nouns:**
Colossal white ape, massive hairless humanoid, bristly-haired giant.

**Uncertainty Notes:**
None.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
