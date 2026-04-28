# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-28T04:05:58.209735+00:00
- task: character_extraction

## System Prompt
````text
You are FilmCreator's chapter analysis engine.
Return only FilmCreator packets with the requested sections and records.
Do not wrap the packet in code fences unless explicitly requested.
Do not produce JSON-only responses.
If a packet asks for markdown sections, emit the section name on its own line and wrap the body in [[SECTION ...]] ... [[/SECTION]].
Do not put another [[SECTION ...]] tag inside a section body.
Copy every FILMCREATOR structural tag literally.
Do not rename, translate, partially rewrite, or decorate any PACKET, RECORD, or SECTION tag.
The only valid closing tags are [[/FILMCREATOR_PACKET]], [[/FILMCREATOR_RECORD]], and [[/SECTION]].
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



Literal tag rules:

- begin with [[FILMCREATOR_PACKET]] on its own line

- end with [[/FILMCREATOR_PACKET]] on its own line

- wrap each character item in [[FILMCREATOR_RECORD]] ... [[/FILMCREATOR_RECORD]]

- use [[SECTION character_index_markdown]] and [[SECTION markdown]] exactly as written

- do not invent alternate closing tags such as [[/FIL_RECORD]], [[end_section]], or misspelled FILMCREATOR tags

- do not echo this instruction block back as an example packet; return the actual packet only



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

**Location: Mushroom Clearing / Forest Canopy**

**Characters:**
* **Alice:** A young girl experiencing rapid physical instability (size changes, neck elongation).
* **Caterpillar:** A languid, hookah-smoking insect sitting atop a mushroom.
* **Pigeon:** A frantic, nesting bird that mistakes Alice for a serpent.

**Events & Scene Beats:**
1.  **The Confrontation:** Alice and the Caterpillar engage in a philosophical argument regarding identity and size. The Caterpillar smokes a hookah and asks "Who are you?"
2.  **The Recitation:** To prove her memory is failing, Alice recites "You are old, Father William." The Caterpillar critiques her performance as being "wrong from beginning to end."
3.  **Size Negotiation:** The Caterpillar asks what size Alice wants to be. She requests to be slightly larger than three inches. The Caterpillar (who is exactly three inches high) reacts angrily to this suggestion.
4.  **The Departure:** The Caterpillar gets off the mushroom and crawls into the grass, providing a crucial instruction: one side of the mushroom makes you grow taller, the other shorter. He identifies the mushroom as the source before disappearing.
5.  **First Transformation (Shrinking):** Alice breaks off a piece of the right-hand side of the round mushroom and eats it. She immediately experiences a violent physical reaction where her chin strikes her foot, indicating she is shrinking rapidly.
6.  **Second Transformation (Elongation):** To counteract the shrinking, Alice eats a morsel from the left-hand side. Her head is freed, but her shoulders disappear, replaced by an immense, serpent-like neck rising above a sea of green leaves (the treetops).
7.  **The Pigeon Encounter:** While Alice attempts to navigate her long, flexible neck through the branches, a large Pigeon flies into her face and attacks her, screaming "Serpent!" 
8.  **The Argument:** A dialogue ensues where the Pigeon insists Alice is a serpent because of her neck; Alice insists she is a little girl. The Pigeon expresses exhaustion from guarding eggs against serpents.
9.  **Stabilization:** Alice crouches among the trees, untwisting her neck. She nibbles alternating pieces of the mushroom to regulate her height until she returns to her "usual" size.
10. **Discovery & Final Transformation:** Alice discovers a small house (four feet high) in an open clearing. To avoid frightening the inhabitants, she nibbles the right-hand bit of the mushroom again to shrink herself down to nine inches tall before approaching.

**Visual Continuity/Objects:**
* **The Mushroom:** A large, perfectly round object used as a platform and a tool for size manipulation.
* **Hookah:** Used by the Caterpillar.
* **Mushroom Fragments:** Alice holds pieces of both sides in her hands.
* **Physical State Shift:** Alice transitions from normal $\rightarrow$ tiny (chin to foot) $\rightarrow$ long-necked/serpent-like $\rightarrow$ normal $\rightarrow$ nine inches tall.
````

## Raw Response
````text
[[FILMCREATOR_PACKET]]
task: character_extraction
version: 1

[[FILMCREATOR_RECORD]]
type: character
asset_id: alice
canonical_character_id: alice
aliases: []
is_fully_identified: true
manual_description_required: true
manual_description_reason: While her general identity is known, the chapter describes extreme and rapid morphological shifts (neck elongation to serpent-like proportions, shrinking to nine inches) that require specific artistic direction for continuity.
clarification_required: false
clarification_reason: 
clarification_question: 
character_type_hint: human
morphology_hint: biped
scale_hint: unknown
renderability_hint: renderable
confidence: 0.9
direct_identity_evidence: "Alice and the Caterpillar engage in a philosophical argument..."
direct_visual_evidence: "Alice... recites 'You are old, Father William.'", "her chin strikes her foot", "her shoulders disappear, replaced by an immense, serpent-like neck"
costume_or_covering_evidence: 
movement_evidence: "crouches among the trees, untwisting her neck"
associated_entities: [caterpillar, pigeon]
alias_or_role_evidence: 
unknowns: []
source_refs: []
[[SECTION character_index_markdown]]
[[SECTION markdown]]
# Alice
**Role:** Protagonist

**Status:** Physically Present (undergoing rapid size/shape transformations)

**Physical Description:**
A young girl. In this chapter, she undergoes extreme physical instability:
- **Normal State:** Standard human child proportions.
- **Shrunken State:** Rapidly shrinking until her chin strikes her feet.
- **Elongated State:** A "serpent-like" morphology where her shoulders disappear and an immense, flexible neck rises above the treetops.
- **Miniature State:** Shrinks down to nine inches tall to enter a small house.

**Costume & Silhouette:**
Varies significantly due to scale; silhouette shifts from bipedal human to a long, serpentine vertical line during elongation.

**Descriptive Noun Phrases:**
- Young girl with an immense serpent-like neck
- Shrinking child
- Nine-inch tall girl
- Flexible, elongated neck rising above leaves

**Uncertainty Notes:**
Specific clothing details are not provided in this chapter; visual design must establish a consistent outfit that can accommodate extreme stretching and shrinking.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: caterpillar
canonical_character_id: caterpillar
aliases: []
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
direct_identity_evidence: "The Caterpillar asks what size Alice wants to be."
direct_visual_evidence: "Caterpillar, a languid, hookah-smoking insect sitting atop a mushroom.", "He is exactly three inches high"
costume_or_covering_evidence: 
movement_evidence: "gets off the mushroom and crawls into the grass"
associated_entities: [alice]
alias_or_role_evidence: 
unknowns: []
source_refs: []
[[SECTION character_index_markdown]]
[[SECTION markdown]]
# Caterpillar
**Role:** Philosophical guide/antagonist

**Status:** Physically Present

**Physical Description:**
A languid insect, approximately three inches in height. He is capable of crawling through grass.

**Costume & Silhouette:**
Sitting atop a large round mushroom; uses a hookah.

**Descriptive Noun Phrases:**
- Three-inch tall insect
- Hookah-smoking caterpillar
- Languid insect on a mushroom

**Uncertainty Notes:**
Specific species or color patterns are not detailed beyond "insect."
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: pigeon
canonical_character_id: pigeon
aliases: []
is_fully_identified: true
manual_description_required: false
manual_description_reason: 
clarification_required: false
clarification_reason: 
clarification_question: 
character_type_hint: animal
morphology_hint: winged
scale_hint: large
renderability_hint: renderable
confidence: 0.9
direct_identity_evidence: "The Pigeon expresses exhaustion from guarding eggs against serpents."
direct_visual_evidence: "a large Pigeon flies into her face and attacks her"
costume_or_covering_evidence: 
movement_evidence: "flies into her face", "screaming 'Serpent!'"
associated_entities: []
alias_or_role_evidence: 
unknowns: []
source_refs: []
[[SECTION character_index_markdown]]
[[SECTION markdown]]
# Pigeon
**Role:** Accidental antagonist/obstacle

**Status:** Physically Present

**Physical Description:**
A large bird.

**Costume & Silhouette:**
Flying through forest canopy/treetops.

**Descriptive Noun Phrases:**
- Large, frantic pigeon
- Nesting bird
- Screaming pigeon

**Uncertainty Notes:**
Specific breed or color is not mentioned; "large" relative to Alice's shifting scale.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]
[[/FILMCREATOR_PACKET]]
````
