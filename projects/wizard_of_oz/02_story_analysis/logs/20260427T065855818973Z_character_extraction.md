# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-27T06:58:55.818973+00:00
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

**Setting:** A forest near a small cottage and a spring of clear water; later, the Yellow Brick Road.

**Characters:** 
- Dorothy: A young girl traveling to find Oz.
- Toto: Dorothy's dog.
- Scarecrow: A companion seeking brains.
- Tin Woodman: A man made entirely of tin who has been rusted immobile for a year.

**Events:**
- After waking in the forest, Dorothy and the Scarecrow search for water and food.
- They hear groaning and discover the Tin Woodman, who is frozen in place due to rusted joints.
- Dorothy uses an oil-can from the Woodman's cottage to lubricate his neck, arms, and legs, restoring his mobility.
- The Tin Woodman joins the group, expressing a desire to ask Oz for a heart.
- As they travel, the Woodman uses his axe to clear thick branches blocking the road.
- The Woodman recounts his tragic backstory: once a human wood-chopper, he was systematically dismantled by the Wicked Witch of the East via an enchanted axe. He was rebuilt piece-by-piece with tin, but in the process, he lost his heart and his ability to love.
- A philosophical debate arises between the Scarecrow (who values brains) and the Woodman (who values a heart), leaving Dorothy conflicted as she worries about their dwindling food supplies.
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
- [Toto](#toto)
- [Scarecrow](#scarecrow)
- [Tin Woodman](#tin_woodman)
- [Wicked Witch of the East](#wicked_witch_of_the_east)

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: dorothy

canonical_character_id: CH001 Dorothy

aliases: Young girl

is_fully_identified: true

manual_description_required: true

manual_description_reason: No specific physical features (hair color, eye color, clothing details) are provided in this chapter.

clarification_required: false

clarification_reason: 

clarification_question: 

character_type_hint: human

morphology_hint: biped

scale_hint: human_scale

renderability_hint: renderable

confidence: 1.0

direct_identity_evidence: Named as Dorothy; described as a young girl.

direct_visual_evidence: None provided in text.

costume_or_covering_evidence: None provided in text.

movement_evidence: Searching for water and food; traveling.

associated_entities: Toto, Scarecrow, Tin Woodman

alias_or_role_evidence: 

unknowns: Physical appearance details.

source_refs: CH005

[[SECTION markdown]]

# Dorothy
**Role:** Protagonist / Traveler

**Status:** Physically Present

**Description:** A young girl traveling toward the Land of Oz. While her presence is central to the narrative, specific visual details regarding her hair, eyes, or clothing are not detailed in this chapter.

**Descriptive Noun Phrases:** Young girl, traveler, companion.

**Uncertainty Notes:** Physical appearance (coloration/clothing) is unknown based on this text alone.
[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: toto

canonical_character_id: CH001 Toto

aliases: Dog

is_fully_identified: true

manual_description_required: true

manual_description_reason: Breed and physical appearance not specified.

clarification_required: false

clarification_reason: 

clarification_question: 

character_type_hint: animal

morphology_hint: quadruped

scale_hint: small

renderability_hint: renderable

confidence: 1.0

direct_identity_evidence: Named as Toto; identified as Dorothy's dog.

direct_visual_evidence: None provided in text.

costume_or_covering_evidence: None.

movement_evidence: Traveling with Dorothy.

associated_entities: Dorothy

alias_or_role_evidence: 

unknowns: Breed, color, size.

source_refs: CH005

[[SECTION markdown]]

# Toto
**Role:** Companion / Pet

**Status:** Physically Present

**Description:** Dorothy's dog.

**Descriptive Noun Phrases:** Small dog, canine companion.

**Uncertainty Notes:** Specific breed and coat color are not mentioned.
[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: scarecrow

canonical_character_id: CH003 Scarecrow

aliases: Companion

is_fully_identified: true

manual_description_required: true

manual_description_reason: No specific visual details regarding construction materials or facial features are provided.

clarification_required: false

clarification_reason: 

clarification_question: 

character_type_hint: humanoid_nonhuman

morphology_hint: biped

scale_hint: human_scale

renderability_hint: renderable

confidence: 0.9

direct_identity_evidence: Named as Scarecrow; described as seeking brains.

direct_visual_evidence: None provided in text.

costume_or_covering_evidence: None.

movement_evidence: Searching for water/food; traveling with Dorothy.

associated_entities: Dorothy, Tin Woodman

alias_or_role_evidence: 

unknowns: Material composition (straw vs other), facial features.

source_refs: CH005

[[SECTION markdown]]

# Scarecrow
**Role:** Companion / Seeker of Brains

**Status:** Physically Present

**Description:** A companion to Dorothy who is motivated by a desire for brains.

**Descriptive Noun Phrases:** Brain-seeking companion, humanoid entity.

**Uncertainty Notes:** Specific visual construction (e.g., straw, burlap) is implied by name but not explicitly described in this chapter's text.
[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: tin_woodman

canonical_character_id: CH004 Tin Woodman

aliases: Man made of tin, wood-chopper (formerly)

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

direct_identity_evidence: Named as Tin Woodman; described as a man made entirely of tin.

direct_visual_evidence: Rusted immobile; has joints (neck, arms, legs); uses an axe; carries/uses an oil-can.

costume_or_covering_evidence: Constructed of tin.

movement_evidence: Initially rusted immobile; restored to mobility via oil; clears branches with an axe.

associated_entities: Dorothy, Scarecrow

alias_or_role_evidence: Formerly a human wood-chopper.

unknowns: Facial features, specific tin texture/patina details beyond "rusted."

source_refs: CH005

[[SECTION markdown]]

# Tin Woodman
**Role:** Companion / Seeker of a Heart

**Status:** Physically Present

**Description:** A man constructed entirely of tin. He was once a human wood-chopper who was dismantled and rebuilt with tin parts. He was found rusted immobile in a cottage before being lubricated with an oil-can.

**Costume/Silhouette:** Entirely metallic (tin) body; carries an axe.

**Descriptive Noun Phrases:** Tin man, rusted metal humanoid, axe-wielding construct.

**Uncertainty Notes:** Specific facial features or the exact degree of rust/patina are not detailed.
[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: wicked_witch_of_the_east

canonical_character_id: UNK Wicked Witch of the East

aliases: The Wicked Witch

is_fully_identified: false

manual_description_required: true

manual_description_reason: Character is only mentioned in backstory; no physical description provided.

clarification_required: true

clarification_reason: Only referenced as an antagonist in a backstory.

clarification_question: What is the visual appearance of the Wicked Witch of the East?

character_type_hint: humanoid_nonhuman

morphology_hint: biped

scale_hint: human_scale

renderability_hint: context_only

confidence: 0.5

direct_identity_evidence: Named as Wicked Witch of the East.

direct_visual_evidence: None.

costume_or_covering_evidence: None.

movement_evidence: None.

associated_entities: Tin Woodman (antagonist)

alias_or_role_evidence: 

unknowns: Physical appearance, magical nature.

source_refs: CH005

[[SECTION markdown]]

# Wicked Witch of the East
**Role:** Antagonist (Referenced)

**Status:** Referenced (Backstory)

**Description:** An antagonist who used an enchanted axe to systematically dismantle a human wood-chopper, leading to his transformation into the Tin Woodman.

**Descriptive Noun Phrases:** Enchanted antagonist, witch.

**Uncertainty Notes:** No physical description or visual details are provided in this chapter.
[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
