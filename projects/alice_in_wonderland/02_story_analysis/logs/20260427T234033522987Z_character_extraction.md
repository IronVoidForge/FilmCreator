# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-27T23:40:33.522987+00:00
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
- [alice](#alice)
- [the_caterpillar](#the_caterpillar)
- [the_pigeon](#the_pigeon)

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: alice

canonical_character_id: CH001 Alice

aliases: None

is_fully_identified: true

manual_description_required: false

manual_description_reason: ""

clarification_required: false

clarification_reason: ""

clarification_question: ""

character_type_hint: human

morphology_hint: biped

scale_hint: tiny / human_scale

renderability_hint: renderable

confidence: 0.9

direct_identity_evidence: "Alice is a young girl experiencing size changes."
direct_visual_evidence: "She shrinks to the size of three inches and later has an immensely long neck."
costume_or_covering_evidence: ""
movement_evidence: "She eats mushroom pieces to regulate her size."
associated_entities: the_caterpillar, the_pigeon
alias_or_role_evidence: ""
unknowns: ""
source_refs: ""

[[SECTION markdown]]
# Alice
**Role:** Protagonist / Young Girl

**Status:** Physically Present (Variable Scale)

**Physical Description:** 
A young girl whose size fluctuates wildly due to eating mushroom pieces. At one point, she is so small her chin hits her feet; at another, her neck becomes immensely long like a serpent. She eventually shrinks herself down to nine inches to visit a small house.

**Visual Cues for Rendering:**
- **Shrunken State:** Extremely small scale (three inches), proportions compressed.
- **Elongated State:** An unnaturally long, serpentine neck while the body remains at a higher altitude.
- **Final State:** Nine inches tall.

**Uncertainty Notes:** Specific hair color or clothing details are not provided in this chapter to define her permanent look.
[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: the_caterpillar

canonical_character_id: CH003 The Caterpillar

aliases: None

is_fully_identified: true

manual_description_required: false

manual_description_reason: ""

clarification_required: false

clarification_reason: ""

clarification_question: ""

character_type_hint: humanoid_nonhuman

morphology_hint: unknown

scale_hint: small

renderability_hint: renderable

confidence: 0.8

direct_identity_evidence: "A creature smoking a hookah on a mushroom."
direct_visual_evidence: "Languid, stern creature; roughly three inches in height."
costume_or_covering_evidence: ""
movement_evidence: "He disappears into the grass after leaving Alice."
associated_entities: alice
alias_or_role_evidence: ""
unknowns: "Specific insectoid vs. humanoid anatomy is not detailed."
source_refs: ""

[[SECTION markdown]]
# The Caterpillar
**Role:** Supporting Character / Mentor-like Figure

**Status:** Physically Present (Initially)

**Physical Description:** 
A languid and stern creature, approximately three inches tall. He sits upon a mushroom while smoking a hookah.

**Visual Cues for Rendering:**
- **Form:** Likely an insectoid or larval-type entity with humanoid-like presence/behavior.
- **Action:** Smoking a hookah; dismissive of Alice's concerns regarding metamorphosis.

**Uncertainty Notes:** The exact anatomical blend between a caterpillar and a humanoid is not specified.
[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILcitator_RECORD]]

type: character

asset_id: the_pigeon

canonical_character_id: CH004 The Pigeon

aliases: None

is_fully_identified: true

manual_description_required: false

manual_description_reason: ""

clarification_required: false

clarification_reason: ""

clarification_question: ""

character_type_hint: animal

morphology_hint: winged

scale_hint: large (relative to Alice)

renderability_hint: renderable

confidence: 0.8

direct_identity_evidence: "A large bird that mistakes a long neck for a serpent."
direct_visual_evidence: "A large bird flying into Alice's face."
costume_or_covering_evidence: ""
movement_evidence: "Flies through the treetops/air."
associated_entities: alice
alias_or_role_evidence: ""
unknowns: ""
source_refs: ""

[[SECTION markdown]]
# The Pigeon
**Role:** Encountered Entity

**Status:** Physically Present (Briefly)

**Physical Description:** 
A large bird that flies through the treetops.

**Visual Cues for Rendering:**
- **Scale:** Large enough to mistake Alice's elongated neck for a serpent during flight.
- **Behavior:** Frantic; struggles with "serpents" while hatching eggs.

**Uncertainty Notes:** Specific breed or color of the pigeon is not mentioned.
[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
