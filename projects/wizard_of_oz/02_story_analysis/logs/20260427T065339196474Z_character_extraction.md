# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-27T06:53:39.196474+00:00
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

**Setting:** A lush, beautiful country in the Land of Oz, characterized by colorful flowers, fruit-bearing trees, and a sparkling brook.

**Characters:**
- **Dorothy:** A young girl from Kansas, newly arrived in Oz.
- **Toto:** Dorothy's small dog.
- **The Witch of the North:** A kind, elderly woman in white with star-patterned clothing; she is a "good" witch.
- **Munchkins:** A group of small people wearing blue hats with bells and blue clothing; they live in the East.

**Events:**
- Dorothy wakes up to find her house has landed in a beautiful land after the cyclone.
- She discovers that her house accidentally landed on and killed the Wicked Witch of the East, freeing the Munchkins from bondage.
- The Witch of the North arrives to greet Dorothy and explains the geography and politics of Oz, noting that only one Wicked Witch remains (the one in the West).
- The body of the Wicked Witch of the East dries up in the sun, leaving behind a pair of enchanted silver shoes, which are given to Dorothy.
- Dorothy expresses her desire to return to Kansas, but the inhabitants explain that the land is surrounded by impassable deserts.
- Through a magical slate, the Witch of the North determines that Dorothy must travel to the Emerald City to ask the Great Wizard Oz for help.
- The Witch of the North kisses Dorothy's forehead to protect her and directs her toward the Yellow Brick Road before magically disappearing.
````

## Raw Response
````text
[[FILMCREATOR_PACKET]]

task: character_extraction

version: 1

character_index_markdown:

[[SECTION character_index_markdown]]

# Character Index

- [dorothy](dorothy)
- [munchkins](munchkins)
- [toto](toto)
- [witch_of_the_east](witch_of_the_east)
- [witch_of_the_north](witch_of_the_north)

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: dorothy

canonical_character_id: CH002 Dorothy

aliases: Young girl from Kansas

is_fully_identified: true

manual_description_required: false

manual_description_reason: 

clarification_required: false

clarification_reason: 

clarification_question: 

character_type_hint: human

morphology_hint: biped

scale_hint: small

renderability_hint: renderable

confidence: 1.0

direct_identity_evidence: Dorothy is explicitly named and identified as a young girl from Kansas.

direct_visual_evidence: 

costume_or_covering_evidence: Wears enchanted silver shoes (received at end of chapter).

movement_evidence: 

associated_entities: Toto, Witch of the North, Munchkins

alias_or_role_evidence: 

unknowns: 

source_refs: 

[[SECTION markdown]]
# Dorothy
**Role:** Protagonist; a young girl from Kansas newly arrived in Oz.
**Presence:** Physically present.
**Description:** A young girl. She has recently traveled via cyclone and is now wearing enchanted silver shoes.
**Descriptive Phrases:** Young girl, traveler from Kansas, wearer of silver shoes.
[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: munchkins

canonical_character_id: CH002 Munchkins

aliases: Small people

is_fully_identified: true

manual_description_required: false

manual_description_reason: 

clarification_required: false

clarification_reason: 

clarification_question: 

character_type_hint: humanoid_nonhuman

morphology_hint: biped

scale_hint: small

renderability_hint: renderable

confidence: 1.0

direct_identity_evidence: Identified as Munchkins, a group of people living in the East.

direct_visual_evidence: Small people wearing blue hats with bells and blue clothing.

costume_or_covering_evidence: Blue hats with bells, blue clothing.

movement_evidence: 

associated_entities: Dorothy, Wicked Witch of the East

alias_or_role_evidence: 

unknowns: 

source_refs: 

[[SECTION markdown]]
# Munchkins
**Role:** Inhabitants of the East; freed from bondage by Dorothy's house.
**Presence:** Physically present.
**Description:** A group of small people.
**Costume/Silhouette:** Blue clothing, blue hats adorned with bells.
**Descriptive Phrases:** Small people in blue, bell-hatted inhabitants, Munchkins.
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

direct_identity_evidence: Toto is explicitly named as Dorothy's small dog.

direct_visual_evidence: Small dog.

costume_or_covering_evidence: 

movement_evidence: 

associated_entities: Dorothy

alias_or_role_evidence: 

unknowns: 

source_refs: 

[[SECTION markdown]]
# Toto
**Role:** Dorothy's companion.
**Presence:** Physically present.
**Description:** A small dog.
**Descriptive Phrases:** Small dog, Dorothy's pet.
[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: witch_of_the_east

canonical_character_id: CH002 Wicked Witch of the East

aliases: The Wicked Witch

is_fully_identified: true

manual_description_required: false

manual_description_reason: 

clarification_required: false

clarification_reason: 

clarification_question: 

character_type_hint: humanoid_nonhuman

morphology_hint: biped

scale_hint: human_scale

renderability_hint: context_only

confidence: 0.8

direct_identity_evidence: Identified as the Wicked Witch of the East.

direct_visual_evidence: Her body dries up in the sun.

costume_or_covering_evidence: 

movement_evidence: 

associated_entities: Munchkins, Dorothy

alias_or_role_evidence: 

unknowns: Physical appearance prior to death.

source_refs: 

[[SECTION markdown]]
# Wicked Witch of the East
**Role:** Antagonist (deceased); former ruler of the East.
**Presence:** Referenced/Deceased (body remains).
**Description:** A witch who was killed when Dorothy's house landed on her. Her body is described as having dried up in the sun.
**Descriptive Phrases:** Dried-up witch, deceased Wicked Witch.
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

confidence: 1.0

direct_identity_evidence: Identified as the Witch of the North.

direct_visual_evidence: Kind, elderly woman in white with star-patterned clothing.

costume_or_covering_evidence: White clothing with star patterns.

movement_evidence: Magically disappears.

associated_entities: Dorothy

alias_or_role_evidence: "Good" witch.

unknowns: 

source_refs: 

[[SECTION markdown]]
# Witch of the North
**Role:** Guide; a "good" witch who explains Oz to Dorothy.
**Presence:** Physically present.
**Description:** A kind, elderly woman.
**Costume/Silhouette:** White clothing featuring star patterns.
**Descriptive Phrases:** Elderly woman in white, star-patterned clothing, good witch.
[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
