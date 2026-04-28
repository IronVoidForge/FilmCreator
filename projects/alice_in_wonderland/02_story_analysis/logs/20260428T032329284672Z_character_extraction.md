# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-28T03:23:29.284672+00:00
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

**Location: Mushroom Clearing / Forest Canopy / Small House Clearing**

**Characters:**
* **Alice:** A young girl experiencing rapid size fluctuations and identity crises.
* **Caterpillar:** A languid, hookah-smoking insect sitting atop a mushroom; prone to irritability and philosophical questioning.
* **Pigeon:** A frantic, nesting bird that mistakes Alice for a serpent.

**Events & Scene Breakdown:**
1.  **The Confrontation on the Mushroom:** Alice encounters the Caterpillar sitting on a large mushroom. The Caterpillar smokes a hookah and interrogates Alice regarding her identity ("Who are you?"). 
2.  **The Recitation:** After a tense exchange about Alice's changing size, the Caterpillar demands she recite "You are old, Father William." Alice performs the poem, but the Caterpillar critiques her for getting the words wrong.
3.  **Size Negotiation:** The Caterpillar asks Alice what size she wants to be. Alice requests to be slightly larger than three inches. The Caterpillar becomes angry at this request (noting it is exactly three inches high) before returning to his hookah.
4.  **The Departure & Instruction:** The Caterpillar gets off the mushroom and crawls away into the grass. Before disappearing, he reveals a crucial mechanic: one side of the mushroom makes you grow taller, and the other side makes you grow shorter.
5.  **First Transformation (Shrinking):** Alice attempts to test the mushroom. She breaks off a piece from the right-hand side and eats it. Immediately, she experiences a violent physical sensation as her chin strikes her foot; she begins shrinking rapidly.
6.  **Second Transformation (Elongation):** To counteract the shrinking, Alice hurriedly eats a morsel from the left-hand side. Her head is freed, but her shoulders disappear, replaced by an immense, serpent-like neck that rises above the forest canopy (the "green leaves").
7.  **The Pigeon Encounter:** While Alice struggles to maneuver her long, flexible neck through the branches, a large Pigeon flies into her face and attacks her, screaming "Serpent!" 
8.  **Identity Argument:** A dialogue ensues between the panicked Pigeon and the indignant Alice. The Pigeon insists she is a serpent because of her neck; Alice insists she is a little girl. The Pigeon remains unconvinced but eventually settles back into its nest.
9.  **Restoring Normalcy:** Alice, crouching among the trees to untangle her neck, nibbles alternating pieces of the mushroom until she successfully returns to her usual height.
10. **Discovery of the House:** Having regained her size, Alice discovers an open clearing containing a small house (approx. four feet high). 
11. **Final Transformation (Miniaturization):** To avoid frightening the inhabitants of the house, Alice nibbles on the right-hand bit of the mushroom again, successfully shrinking herself down to nine inches in height before approaching.
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
manual_description_required: false
manual_description_reason: ""
clarification_required: false
clarification_reason: ""
clarification_question: ""
character_type_hint: human
morphology_hint: biped
scale_hint: unknown
renderability_hint: renderable
confidence: 1.0
direct_identity_evidence: "Alice is explicitly named and described as a young girl."
direct_visual_evidence: "Described undergoing rapid size fluctuations, including having an immense serpent-like neck and shrinking to nine inches."
costume_or_covering_evidence: ""
movement_evidence: "Shrinking, growing, maneuvering a long neck through branches, crouching."
associated_entities: ["caterpillar", "pigeon"]
alias_or_role_evidence: ""
unknowns: []
source_refs: []
[[SECTION character_index_markdown]]
[[SECTION markdown]]
# Alice
**Role:** Protagonist

**Status:** Physically Present

**Physical Description:**
A young girl. In this chapter, she undergoes extreme morphological changes due to consuming mushroom pieces:
- Rapidly shrinks (down to 3 inches and later 9 inches).
- Experiences extreme elongation where her shoulders disappear and are replaced by an immense, serpent-like neck that rises above the forest canopy.
- Returns to a normal human height through controlled consumption of the mushroom.

**Costume & Silhouette:**
Subject to rapid scale changes; silhouette shifts from standard child to extremely long/serpentine to miniature.

**Descriptive Noun Phrases:**
Young girl, shrinking child, elongated neck, serpent-like girl, miniature girl.
[[/SECTION]]
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: caterpillar
canonical_character_id: caterpillar
aliases: []
is_fully_identified: true
manual_description_required: false
manual_description_reason: ""
clarification_required: false
clarification_reason: ""
clarification_question: ""
character_type_hint: creature
morphology_hint: multi_legged
scale_hint: small
renderability_hint: renderable
confidence: 0.9
direct_identity_evidence: "Identified as the Caterpillar."
direct_visual_evidence: "An insect sitting atop a large mushroom, smoking a hookah."
costume_or_covering_evidence: ""
movement_evidence: "Sits on a mushroom, then crawls away into the grass."
associated_entities: ["alice"]
alias_or_role_evidence: ""
unknowns: []
source_refs: []
[[SECTION character_index_markdown]]
[[SECTION markdown]]
# Caterpillar
**Role:** Philosophical Interrogator

**Status:** Physically Present

**Physical Description:**
A languid insect. He is seen sitting atop a large mushroom.

**Costume & Silhouette:**
Smoking a hookah.

**Descriptive Noun Phrases:**
Languid insect, hookah-smoking caterpillar, mushroom-dwelling creature.
[[/SECTION]]
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: pigeon
canonical_character_id: pigeon
aliases: []
is_fully_identified: true
manual_description_required: false
manual_description_reason: ""
clarification_required: false
clarification_reason: ""
clarification_question: ""
character_type_hint: animal
morphology_hint: winged
scale_hint: small
renderability_hint: renderable
confidence: 1.0
direct_identity_evidence: "Identified as a Pigeon."
direct_visual_evidence: "A large bird that flies into Alice's face and screams 'Serpent!'"
costume_or_covering_evidence: ""
movement_evidence: "Flies, nests, attacks."
associated_entities: ["alice"]
alias_or_role_evidence: ""
unknowns: []
source_refs: []
[[SECTION character_index_markdown]]
[[SECTION markdown]]
# Pigeon
**Role:** Panicked Antagonist/Witness

**Status:** Physically Present

**Physical Description:**
A large bird.

**Costume & Silhouette:**
Nesting in trees.

**Descriptive Noun Phrases:**
Large pigeon, frantic nesting bird, screaming bird.
[[/SECTION]]
[[/SECTION]]
[[/FILMCREATOR_RECORD]]
[[/FILMCREATOR_PACKET]]
````
