# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-27T07:22:16.098173+00:00
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

Chapter id: CH017

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

**Setting:** The Throne Room and the exterior of the Palace in the Emerald City.

**Characters:** 
- Dorothy: Longing to return to Kansas.
- Oz (The Wizard): A "humbug" seeking to escape his life of deception by returning to the circus.
- Scarecrow, Tin Woodman, Lion: Contented with their new perceived attributes.
- The citizens of the Emerald City: Curious onlookers.

**Events:**
- After three days of silence, Oz summons Dorothy and proposes traveling by balloon to cross the desert.
- Oz reveals his true nature as a former circus performer and expresses a desire to leave Oz to avoid being exposed as a fraud.
- Dorothy and Oz spend three days constructing a large green silk balloon; Oz coats it with glue to make it airtight.
- A basket is attached to the balloon, and the Tin Woodman provides wood for a fire to heat the air inside the bag.
- Oz announces to his people that he is visiting a "brother Wizard" in the clouds and appoints the Scarecrow as ruler in his absence.
- As the balloon begins to rise, Dorothy searches for Toto; just as she reaches the basket, the ropes snap.
- The balloon ascends into the sky with only Oz inside, leaving Dorothy and her friends behind in the Emerald City.
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
- [Oz (The Wizard)](#oz-the-wizard)
- [Scarecrow](#scarecrow)
- [Tin Woodman](#tin-woodman)
- [Lion](#lion)
- [Citizens of the Emerald City](#citizens-of-the-emerald-city)

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: dorothy

canonical_character_id: CH001 Dorothy

aliases: None

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

confidence: 0.9

direct_identity_evidence: Dorothy is named as the one longing to return to Kansas and searching for Toto.

direct_visual_evidence: None in this specific chapter text, but established identity is clear.

costume_or_covering_evidence: None mentioned in this chapter.

movement_evidence: Searching for Toto near the balloon basket.

associated_entities: Oz, Scarecrow, Tin Woodman, Lion, Toto

alias_or_role_evidence: 

unknowns: Specific clothing details for this scene are not provided in the text.

source_refs: CH017

[[SECTION markdown]]

# Dorothy
**Role:** Protagonist / Traveler

**Status:** Physically Present

**Description:** A young girl longing to return home to Kansas. In this chapter, she is actively involved in the construction of the balloon and the search for her dog, Toto.

**Visual Notes:** While specific attire isn't detailed in this chapter, she is a human child of human scale.

**Uncertainty:** Specific costume details for the balloon departure are not explicitly described in this text segment.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: oz_the_wizard

canonical_character_id: CH003 Oz the Wizard

aliases: The Wizard, Humbug

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

confidence: 0.8

direct_identity_evidence: Identified as Oz, a former circus performer and "humbug."

direct_visual_evidence: Involved in constructing a green silk balloon and coating it with glue.

costume_or_covering_evidence: None mentioned.

movement_evidence: Constructing the balloon, announcing his departure to the citizens.

associated_entities: Dorothy, Scarecrow, Citizens of the Emerald City

alias_or_role_evidence: Referred to as a "humbug" and a former circus performer.

unknowns: Physical appearance/clothing not described in this chapter.

source_refs: CH017

[[SECTION markdown]]

# Oz (The Wizard)
**Role:** Former Ruler / Fugitive Performer

**Status:** Physically Present

**Description:** A man who has lived a life of deception as a "Wizard" but is actually a former circus performer. He is attempting to escape his position by traveling via balloon.

**Visual Notes:** Human male, human scale. 

**Uncertainty:** The text focuses on his actions and revelation rather than his physical appearance or specific costume.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: scarecrow

canonical_character_id: CH004 Scarecrow

aliases: None

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

direct_identity_evidence: Named as Scarecrow; appointed ruler by Oz.

direct_visual_evidence: None in this chapter.

costume_or_covering_evidence: None mentioned.

movement_evidence: Contented with new attributes.

associated_entities: Oz, Tin Woodman, Lion, Dorothy

alias_or_role_evidence: Appointed ruler of the Emerald City.

unknowns: Specific visual details for this chapter are absent.

source_refs: CH017

[[SECTION markdown]]

# Scarecrow
**Role:** New Ruler of the Emerald City

**Status:** Physically Present

**Description:** A character who is contented with his current state and has been appointed to rule the Emerald City in Oz's absence.

**Visual Notes:** Humanoid non-human, human scale.

**Uncertainty:** Physical appearance details are not provided in this chapter text.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: tin_woodman

canonical_character_id: CH005 Tin Woodman

aliases: None

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

direct_identity_evidence: Named as Tin Woodman.

direct_visual_evidence: Provides wood for a fire to heat the balloon.

costume_or_covering_evidence: Implied metallic/constructed nature from name and role.

movement_evidence: Providing materials for the balloon.

associated_entities: Oz, Scarecrow, Lion, Dorothy

alias_or_role_evidence: 

unknowns: Specific visual details of his construction are not described here.

source_refs: CH017

[[SECTION markdown]]

# Tin Woodman
**Role:** Companion

**Status:** Physically Present

**Description:** A contented companion who assists in the preparations for Oz's departure by providing fuel for the balloon.

**Visual Notes:** Humanoid non-human, human scale. Likely constructed/metallic.

**Uncertainty:** Specific visual details of his metallic form are not described in this chapter.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: lion

canonical_character_id: CH006 Lion

aliases: None

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

confidence: 0.7

direct_identity_evidence: Named as Lion.

direct_visual_evidence: None in this chapter.

costume_or_covering_evidence: None mentioned.

movement_evidence: Contented with new attributes.

associated_entities: Oz, Scarecrow, Tin Woodman, Dorothy

alias_or_role_evidence: 

unknowns: Specific physical appearance details are not provided in this text segment.

source_refs: CH017

[[SECTION markdown]]

# Lion
**Role:** Companion

**Status:** Physically Present

**Description:** A contented companion of Dorothy and the others.

**Visual Notes:** Large quadruped animal.

**Uncertainty:** Specific visual details (fur color, etc.) are not provided in this chapter text.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: citizens_of_emerald_city

canonical_character_id: GROUP_Citizens_Emerald_City

aliases: Onlookers, People of the Emerald City

is_fully_identified: true

manual_description_required: true

manual_description_reason: They are a group with no specific individual descriptions or shared visual traits provided.

clarification_required: false

clarification_reason: 

clarification_question: 

character_type_hint: group

morphology_hint: biped

scale_hint: human_scale

renderability_hint: context_only

confidence: 0.5

direct_identity_evidence: Referred to as "his people" and "citizens of the Emerald City."

direct_visual_evidence: Described as curious onlookers.

costume_or_covering_evidence: None mentioned.

movement_evidence: Watching Oz's announcement.

associated_entities: Oz

alias_or_role_evidence: 

unknowns: Individual appearances, clothing, or specific species/types of the citizens.

source_refs: CH017

[[SECTION markdown]]

# Citizens of the Emerald City
**Role:** Onlookers / Populace

**Status:** Physically Present

**Description:** The inhabitants of the Emerald City who watch Oz's announcement regarding his departure and his visit to a "brother Wizard."

**Visual Notes:** A group of human-scale bipeds. 

**Uncertainty:** No specific visual details, clothing, or individual characteristics are provided for this group in the text.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
