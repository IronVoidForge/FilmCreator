# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-27T23:41:21.394835+00:00
- task: character_extraction

## System Prompt
````text
You are FilmCreator's chapter analysis engine.
Return only FilmCreator packets with the requested sections and records.
Do not wrap the packet in code fences unless explicitly requested.
Do not produce JSON-only responses.
If a packet asks for markdown sections, emit the section name on its own line and wrap the body in [[SECTION ...]] ... [[/SECTION]].
Do not put another [[SECTION ...]] tag inside a section body.
Keep the response deterministic and grounded in the supplied chapter text.
````

## User Prompt
````text
Project slug: alice_in_wonderland

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

- keep one record per meaningful character mention

- prefer short facts over long prose

- if uncertain, use clarification_required instead of guessing

- if clarification is not required, still include clarification_reason and clarification_question as empty values

- still emit explicit character records; do not collapse them into index bullets only



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

**Setting:** A mushroom in a forest setting; later, the treetops (viewed from a high vantage point).

**Characters:**
* **Alice:** A young girl experiencing fluctuating physical sizes.
* **The Caterpillar:** A languid, stern creature smoking a hookah.
* **The Pigeon:** A frantic bird mistaking Alice for a serpent.

**Events/Sequence:**
1. **The Dialogue of Identity:** The Caterpillar questions Alice's identity. Alice explains her confusion caused by frequent size changes. The Caterpillar dismisses her concerns about metamorphosis (chrysalis/butterfly) as trivial.
2. **The Poem:** To test her, the Caterpillar has Alice recite "You are old, Father William." Alice recites a version of the poem; the Caterpillar critiques it for being inaccurate.
3. **Size Discussion:** The Caterpillar asks what size Alice wants to be. She expresses a desire to be slightly larger than three inches (the Caterpillar's height). 
4. **The Departure:** The Caterpillar leaves, revealing that one side of the mushroom makes one grow taller and the other shorter. It disappears into the grass.
5. **The First Transformation:** Alice breaks off a piece of the mushroom edge and eats it. She shrinks rapidly until her chin hits her foot. 
6. **The Second Transformation:** To fix this, she eats a morsel from the other side. Her neck grows immensely long (like a serpent), while her body stays high above the trees.
7. **The Pigeon Encounter:** A large Pigeon flies into Alice's face, mistaking her long neck for a serpent. The Pigeon describes its struggle with "serpents" while hatching eggs. Alice defends her identity as a "little girl."
8. **Restoring Size:** Alice nibbles on the mushroom pieces alternately to regulate her size until she returns to her usual height.
9. **The Discovery:** Alice finds an open space containing a small house (four feet high). To avoid frightening the inhabitants, she eats more of the mushroom to shrink herself down to nine inches.

**Visual/Continuity States:**
* **Initial State:** Alice and Caterpillar at the mushroom.
* **Shrunken State:** Alice is three inches tall; her chin hits her foot after eating a piece of the mushroom.
* **Elongated State:** Alice has an immense neck, looking like a serpent among tree leaves.
* **Final State:** Alice returns to normal size, then shrinks to nine inches before approaching the house.
````

## Raw Response
````text
[[FILMCREATOR_PACKET]]

task: character_extraction

version: 1

character_index_markdown:

[[SECTION character_index_markdown]]

# Character Index
* [Alice](#alice)
* [The Caterpillar](#the-caterpillar)
* [The Pigeon](#the-pigeon)

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: alice

canonical_character_id: CH001 Alice

aliases: 

is_fully_identified: true

manual_description_required: false

manual_description_reason: 

clarification_required: false

clariction_reason: 

clarification_question: 

character_type_hint: human (young girl)

morphology_hint: variable size; can be three inches tall, have an immensely long neck, or nine inches tall.

scale_hint: fluctuates between microscopic and human-sized.

renderability_hint: high complexity due to morphing body proportions.

confidence: 0.9

direct_identity_evidence: Alice is a young girl experiencing size changes.

direct_visual_evidence: Shrinks to three inches; neck grows long like a serpent; shrinks to nine inches.

costume_or_covering_evidence: 

movement_evidence: Moves through forest/treetops; eats mushroom pieces to regulate size.

associated_entities: The Caterpillar, The Pigeon

alias_or_role_evidence: Protagonist

unknowns: exact hair color or clothing details not specified in text.

source_refs: CH005

[[SECTION markdown]]

# Alice
**Role:** Protagonist

**Presence:** Physically present throughout the chapter.

**Physical Description:** A young girl whose size fluctuates wildly due to eating mushroom pieces. She can be as small as three inches (where her chin hits her foot) or have an elongated, serpent-like neck while remaining high above the trees.

**Costume & Silhouette:** Variable silhouette; at times extremely small/compact, at other times elongated with a long neck.

**Descriptive Noun Phrases:** Small girl, size-shifting protagonist, long-necked girl, miniature explorer.

**Uncertainty Notes:** Specific clothing colors or hair textures are not detailed in this chapter.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: caterpillar

canonical_character_id: CH003 The Caterpillar

aliases: 

is_fully_identified: true

manual_description_required: false

manual_description_reason: 

clarification_required: false

clarification_reason: 

clarification_question: 

character_type_hint: insectoid/creature

morphology_hint: languid, stern creature.

scale_hint: approximately three inches tall (comparable to Alice's initial size).

renderability_hint: smoking a hookah; sitting on a mushroom.

confidence: 0.85

direct_identity_evidence: The Caterpillar is a distinct entity questioning Alice.

direct_visual_evidence: Sitting on a mushroom, smoking a hookah.

costume_or_covering_evidence: 

movement_evidence: Languid demeanor; disappears into the grass.

associated_entities: Alice

alias_or_role_evidence: The interrogator/mentor figure.

unknowns: exact species or number of legs/limbs.

source_refs: CH005

[[SECTION markdown]]

# The Caterpillar
**Role:** Supporting Character / Interrogator

**Presence:** Physically present (initial encounter), then disappears into the grass.

**Physical Description:** A languid, stern creature roughly three inches in height. He is seen smoking a hookah.

**Costume & Silhouette:** Sitting on a mushroom; smoke-emitting silhouette.

**Descriptive Noun Phrases:** Stern insectoid, hookah-smoking creature, three-inch philosopher.

**Uncertainty Notes:** Specific anatomical details (legs vs. body) are not explicitly described beyond being "languid" and "stern."

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: pigeon

canonical_character_id: CH004 The Pigeon

aliases: 

is_fully_identified: true

manual_description_required: false

manual_description_reason: 

clarification_required: false

clarification_reason: 

clarification_question: 

character_type_hint: bird

morphology_hint: large bird.

scale_hint: large enough to fly into Alice's face/neck.

renderability_hint: flying, frantic movement.

confidence: 0.8

direct_identity_evidence: A large pigeon that encounters the elongated Alice.

direct_visual_evidence: Flies into Alice's face; mistaken for a serpent-handler.

costume_or_covering_evidence: Feathers/avian.

movement_evidence: Flying, frantic.

associated_entities: Alice

alias_or_role_evidence: 

unknowns: specific breed or color of feathers.

source_refs: CH005

[[SECTION markdown]]

# The Pigeon
**Role:** Encountered Character

**Presence:** Physically present (briefly).

**Physical Description:** A large bird.

**Costume & Silhouette:** Avian silhouette; frantic flier.

**Descriptive Noun Phrases:** Large bird, frantic pigeon, egg-hatcher.

**Uncertainty Notes:** Specific plumage colors are not mentioned.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
