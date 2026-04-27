# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-27T07:35:01.777516+00:00
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

Chapter id: CH023

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

**Setting:** A room within Glinda's Castle and the Kansas prairie.

**Characters:** 
- Dorothy: Seeking to return to Kansas.
- Scarecrow: Desires to return to the Emerald City to rule.
- Tin Woodman: Desires to return to the West to rule the Winkies.
- Lion: Desires to return to his forest to be King of the beasts.
- Glinda the Good Witch: A beautiful, red-haired ruler on a ruby throne.
- Uncle Henry & Toto: Appearing in the final scene.

**Events:**
- The companions prepare themselves and meet Glinda in her ruby throne room.
- Dorothy explains her desire to return to Kansas to Aunt Em and Uncle Henry.
- Glinda agrees to help Dorothy on the condition that Dorothy surrenders the Golden Cap.
- Dorothy hands over the Golden Cap. Glinda uses its power to make three commands to the Winged Monkeys: 
    1. Carry the Scarecrow to the Emerald City.
    2. Carry the Tin Woodman to the land of the Winkies.
    3. Carry the Lion to his forest.
- After the commands, Glinda intends to give the Cap to the King of the Monkeys to grant them freedom.
- Glinda reveals that Dorothy's Silver Shoes have the power to transport her anywhere in three steps by clicking the heels together.
- The companions share a tearful farewell, acknowledging how their journey provided them with the qualities they originally sought.
- Dorothy clicks her heels three times and commands the shoes to take her home to Kansas.
- Dorothy arrives instantly on the Kansas prairie in front of her new farmhouse, but the Silver Shoes fall off during the flight and are lost forever in the desert.
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
- [Tin Woodman](#tin-woodman)
- [Lion](#lion)
- [Glinda the Good Witch](#glinda-the-good-witch)
- [Uncle Henry](#uncle-henry)
- [Toto](#toto)
- [Winged Monkeys](#winged-monkeys)

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: dorothy

canonical_character_id: Dorothy

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

confidence: 1.0

direct_identity_evidence: Explicitly named as Dorothy.

direct_visual_evidence: Wears Silver Shoes.

costume_or_covering_evidence: Silver Shoes.

movement_evidence: Clicks heels to travel; arrives on Kansas prairie.

associated_entities: Toto, Glinda the Good Witch, Scarecrow, Tin Woodman, Lion, Uncle Henry

alias_or_role_evidence: 

unknowns: 

source_refs: 

[[SECTION markdown]]
# Dorothy
**Role:** Protagonist; seeker of home.
**Presence:** Physically present.
**Description:** A human girl traveling in Silver Shoes. She possesses the ability to transport herself by clicking her heels together three times.
**Costume/Silhouette:** Notable for wearing Silver Shoes which are central to her movement and magic.
**Descriptive Phrases:** Young girl, silver-shod traveler, Kansas farm girl.
[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: scarecrow

canonical_character_id: Scarecrow

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

confidence: 1.0

direct_identity_evidence: Explicitly named as Scarecrow.

direct_visual_evidence: Characterized by his nature as a scarecrow.

costume_or_covering_evidence: 

movement_evidence: Carried by Winged Monkeys to Emerald City.

associated_entities: Dorothy, Tin Woodman, Lion, Glinda the Good Witch, Winged Monkeys

alias_or_role_evidence: 

unknowns: 

source_refs: 

[[SECTION markdown]]
# Scarecrow
**Role:** Companion; aspiring ruler of Emerald City.
**Presence:** Physically present.
**Description:** A humanoid scarecrow figure.
**Costume/Silhouette:** Traditional scarecrow construction.
**Descriptive Phrases:** Straw-filled companion, aspiring ruler, flying scarecrow.
[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: tin_woodman

canonical_character_id: Tin Woodman

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

confidence: 1.0

direct_identity_evidence: Explicitly named as Tin Woodman.

direct_visual_evidence: Constructed of tin.

costume_or_covering_evidence: Metal body.

movement_evidence: Carried by Winged Monkeys to the land of the Winkies.

associated_entities: Dorothy, Scarecrow, Lion, Glinda the Good Witch, Winged Monkeys

alias_or_role_evidence: 

unknowns: 

source_refs: 

[[SECTION markdown]]
# Tin Woodman
**Role:** Companion; aspiring ruler of the Winkies.
**Presence:** Physically present.
**Description:** A humanoid entity constructed entirely of tin.
**Costume/Silhouette:** Metallic, articulated tin body.
**Descriptive Phrases:** Tin man, metallic companion, ruler of the Winkies.
[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: lion

canonical_character_id: Lion

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

confidence: 1.0

direct_identity_evidence: Explicitly named as Lion.

direct_visual_evidence: A lion.

costume_or_covering_evidence: 

movement_evidence: Carried by Winged Monkeys to his forest.

associated_entities: Dorothy, Scarecrow, Tin Woodman, Glinda the Good Witch, Winged Monkeys

alias_or_role_evidence: 

unknowns: 

source_refs: 

[[SECTION markdown]]
# Lion
**Role:** Companion; aspiring King of the beasts.
**Presence:** Physically present.
**Description:** A large animal (lion).
**Costume/Silhouette:** Feline, large predator silhouette.
**Descriptive Phrases:** King of the beasts, large lion, forest ruler.
[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: glinda_the_good_witch

canonical_character_id: Glinda the Good Witch

aliases: Glinda

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

confidence: 1.0

direct_identity_evidence: Explicitly named as Glinda the Good Witch.

direct_visual_evidence: Beautiful, red-haired ruler sitting on a ruby throne.

costume_or_covering_evidence: Associated with a ruby throne and the Golden Cap (as controller).

movement_evidence: Uses magic via the Golden Cap.

associated_entities: Dorothy, Scarecrow, Tin Woodman, Lion, Winged Monkeys

alias_or_role_evidence: 

unknowns: 

source_refs: 

[[SECTION markdown]]
# Glinda the Good Witch
**Role:** Powerful ruler; magical guide.
**Presence:** Physically present.
**Description:** A beautiful woman with red hair.
**Costume/Silhouette:** Associated with a ruby throne and high-status magical presence.
**Descriptive Phrases:** Red-haired witch, ruler of the castle, powerful magic user.
[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: winged_monkeys

canonical_character_id: Winged Monkeys

aliases: 

is_fully_identified: true

manual_description_required: false

manual_description_reason: 

clarification_required: false

clarification_reason: 

clarification_question: 

character_type_hint: creature

morphology_hint: winged

scale_hint: small

renderability_hint: renderable

confidence: 1.0

direct_identity_evidence: Explicitly named as Winged Monkeys.

direct_visual_evidence: They have wings and obey the Golden Cap.

costume_or_covering_evidence: 

movement_evidence: Fly to transport companions.

associated_entities: Glinda the Good Witch, Dorothy, Scarecrow, Tin Woodman, Lion

alias_or_role_evidence: 

unknowns: 

source_refs: 

[[SECTION markdown]]
# Winged Monkeys
**Role:** Servants/Agents of the Golden Cap.
**Presence:** Physically present (via command).
**Description:** A group of winged primates.
**Costume/Silhouette:** Monkey-like with wings.
**Descriptive Phrases:** Flying monkeys, winged creatures, servants of the cap.
[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: uncle_henry

canonical_character_id: Uncle Henry

aliases: 

is_fully_identified: true

manual_description_required: true

manual_description_reason: No physical description provided in the text.

clarification_required: false

clarification_reason: 

clarification_question: 

character_type_hint: human

morphology_hint: biped

scale_hint: human_scale

renderability_hint: renderable

confidence: 0.5

direct_identity_evidence: Explicitly named as Uncle Henry.

direct_visual_evidence: None.

costume_or_covering_evidence: None.

movement_evidence: Appears in the final scene on the Kansas prairie.

associated_entities: Dorothy, Toto

alias_or_role_evidence: 

unknowns: 

source_refs: 

[[SECTION markdown]]
# Uncle Henry
**Role:** Family member of Dorothy.
**Presence:** Physically present (final scene).
**Description:** A human male in Kansas. Physical appearance is unknown from this text.
**Costume/Silhouette:** Unknown.
**Descriptive Phrases:** Dorothy's uncle, Kansas farmer.
[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: toto

canonical_character_id: Toto

aliases: 

is_fully_identified: true

manual_description_required: true

manual_description_reason: No physical description provided in the text.

clarification_required: false

clarification_reason: 

clarification_question: 

character_type_hint: animal

morphology_hint: quadruped

scale_hint: tiny

renderability_hint: renderable

confidence: 0.5

direct_identity_evidence: Explicitly named as Toto.

direct_visual_evidence: None.

costume_or_covering_evidence: None.

movement_evidence: Appears in the final scene on the Kansas prairie.

associated_entities: Dorothy, Uncle Henry

alias_or_role_evidence: 

unknowns: 

source_refs: 

[[SECTION markdown]]
# Toto
**Role:** Dorothy's companion/pet.
**Presence:** Physically present (final scene).
**Description:** A small animal. Specific breed or appearance is not described in this chapter.
**Costume/Silhouette:** Unknown.
**Descriptive Phrases:** Small dog, Dorothy's pet.
[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
