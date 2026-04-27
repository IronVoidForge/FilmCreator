# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-27T06:49:16.960411+00:00
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

Chapter id: CH002

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

**Setting:** A lush, beautiful country filled with colorful flowers, fruit-bearing trees, and a sparkling brook; specifically, the land of the Munchkins in the East.

**Characters:**
- **Dorothy:** A young girl from Kansas, confused by her sudden arrival in Oz.
- **Toto:** Dorothy's small dog.
- **The Witch of the North:** A kind, elderly woman in white with star-patterned clothing; a "good" witch who provides guidance.
- **Munchkins:** A group of small people wearing blue hats and outfits; they are grateful to Dorothy for liberating them.

**Events:**
- Dorothy wakes up in the Land of Oz after her house lands safely following a cyclone.
- She discovers that her house has landed on and killed the Wicked Witch of the East, whose feet (wearing silver shoes) are visible under the house.
- The Munchkins and the Witch of the North arrive to greet Dorothy, mistakenly treating her as a "noble Sorceress" for killing the wicked ruler.
- The Witch of the East's body dries up in the sun, leaving only the enchanted silver shoes, which the Witch of the North gives to Dorothy.
- Dorothy expresses her desire to return to Kansas, but is informed that the land is surrounded by impassable deserts and ruled by other witches.
- Through a magical slate, the Witch of the North determines that Dorothy must travel to the Emerald City to ask the Great Wizard Oz for help.
- The Witch of the North kisses Dorothy's forehead to protect her and directs her toward the Yellow Brick Road.
- The Witch of the North disappears magically, leaving Dorothy to begin her journey.
````

## Raw Response
````text
[[FILMCREATOR_PACKET]]

task: character_extraction

version: 1

character_index_markdown:

[[SECTION character_index_markdown]]

# Character Index

- [dorothy](#dorothy)
- [toto](#toto)
- [witch_of_the_north](#witch_of_the_north)
- [munchkins](#munchkins)
- [wicked_witch_of_the_east](#wicked_witch_of_the_east)

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: dorothy

canonical_character_id: CH002 Dorothy

aliases: Young girl from Kansas, Noble Sorceress

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

direct_identity_evidence: Dorothy is explicitly named and identified as a young girl from Kansas.

direct_visual_evidence: Present in the scene, interacting with Munchkins and the Witch of the North.

costume_or_covering_evidence: None specified in this chapter beyond being a "young girl".

movement_evidence: Wakes up, expresses desire to return home, interacts with others.

associated_entities: toto, witch_of_the_north, munchkins

alias_or_role_evidence: Mistakenly called "noble Sorceress" by Munchkins.

unknowns: 

source_refs: 

[[SECTION markdown]]

# Dorothy
**Role:** Protagonist; a young girl from Kansas who has arrived in Oz via cyclone.
**Status:** Physically present.

### Physical Description
A young human girl. While specific clothing details are not provided in this chapter, she is identified as being from Kansas.

### Notes for Rendering
- **Keywords:** Young girl, Kansas origin, confused expression, traveler.
- **Uncertainty:** Specific hair color, eye color, and outfit details are not mentioned in this text; these will need to be established based on broader franchise continuity or design preference.

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: toto

canonical_character_id: CH002 Toto

aliases: Small dog

is_fully_identified: true

manual_description_required: false

manual_description_reason: 

clarification_required: false

clarification_reason: 

clarification_question: 

character_type_hint: animal

morphology_hint: quadruped

scale_hint: tiny

renderability_hint: renderable

confidence: 1.0

direct_identity_evidence: Named as Dorothy's dog.

direct_visual_evidence: Identified as a small dog.

costume_or_covering_evidence: None.

movement_evidence: Present with Dorothy.

associated_entities: dorothy

alias_or_role_evidence: 

unknowns: 

source_refs: 

[[SECTION markdown]]

# Toto
**Role:** Dorothy's companion.
**Status:** Physically present.

### Physical Description
A small dog.

### Notes for Rendering
- **Keywords:** Small dog, canine, companion.
- **Uncertainty:** Breed and color are not specified in this chapter.

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: witch_of_the_north

canonical_character_id: CH002 Witch of the North

aliases: Good Witch

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

direct_identity_evidence: Explicitly named as the Witch of the North.

direct_visual_evidence: Described as a kind, elderly woman in white with star-patterned clothing.

costume_or_covering_evidence: White clothing with star patterns.

movement_evidence: Arrives to greet Dorothy, kisses Dorothy's forehead, disappears magically.

associated_entities: dorothy, munchkins

alias_or_role_evidence: Referred to as a "good" witch.

unknowns: 

source_refs: 

[[SECTION markdown]]

# Witch of the North
**Role:** Guide and benevolent magical entity.
**Status:** Physically present.

### Physical Description
An elderly woman.

### Costume & Silhouette
White clothing featuring star patterns.

### Notes for Rendering
- **Keywords:** Elderly woman, kind expression, white star-patterned robes, magical presence.
- **Uncertainty:** Specific facial features or hair color are not detailed beyond "elderly".

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: munchkins

canonical_character_id: CH002 Munchkins

aliases: Group of small people

is_fully_identified: true

manual_description_required: false

manual_description_reason: 

clarification_required: false

clarification_reason: 

clarification_question: 

character_type_hint: group

morphology_hint: biped

scale_hint: small

renderability_hint: renderable

confidence: 0.8

direct_identity_evidence: Identified as the Munchkins.

direct_visual_evidence: Described as a group of small people wearing blue hats and outfits.

costume_or_covering_evidence: Blue hats and blue outfits.

movement_evidence: Arrive to greet Dorothy; treat her as a sorceress.

associated_entities: witch_of_the_north, dorothy

alias_or_role_evidence: 

unknowns: 

source_refs: 

[[SECTION markdown]]

# Munchkins
**Role:** Inhabitants of the land; grateful subjects.
**Status:** Physically present (as a group).

### Physical Description
A group of small-statured people.

### Costume & Silhouette
Blue outfits and blue hats.

### Notes for Rendering
- **Keywords:** Small people, blue clothing, blue hats, celebratory/grateful mood.
- **Uncertainty:** Specific facial features or exact shades of blue are not defined.

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: wicked_witch_of_the_east

canonical_character_id: CH002 Wicked Witch of the East

aliases: The Wicked Ruler

is_fully_identified: false

manual_description_required: true

manual_description_reason: Only remains (feet/shoes) are visible; no physical description of the body or face is provided.

clarification_required: true

clarification_reason: Character is deceased and only partially visible via remains.

clarification_question: Should the character be rendered as a corpse, or only as the visible feet/shoes under the house?

character_type_hint: humanoid_nonhuman

morphology_hint: biped

scale_hint: human_scale

renderability_hint: context_only

confidence: 0.5

direct_identity_evidence: Identified as the Wicked Witch of the East.

direct_visual_evidence: Only feet wearing silver shoes are visible under the house before drying up.

costume_or_covering_evidence: Silver shoes.

movement_evidence: None (deceased).

associated_entities: 

alias_or_role_evidence: Referred to as the "wicked ruler".

unknowns: Physical appearance of the body/face.

source_refs: 

[[SECTION markdown]]

# Wicked Witch of the East
**Role:** Deceased antagonist/ruler.
**Status:** Referenced (deceased); partially visible via remains.

### Physical Description
Unknown. The character is deceased, having been crushed by a house.

### Costume & Silhouette
Silver shoes (enchanted).

### Notes for Rendering
- **Keywords:** Silver shoes, feet under house, dried remains.
- **Uncertainty:** The body is described as "drying up" in the sun, leaving only the shoes. Visual representation should likely focus on the silver shoes and the aftermath of the house landing rather than a full character model.

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
