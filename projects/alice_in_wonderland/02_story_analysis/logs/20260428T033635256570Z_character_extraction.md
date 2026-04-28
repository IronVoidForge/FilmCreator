# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-28T03:36:35.256570+00:00
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
* **Alice:** A young girl experiencing rapid size fluctuations; currently struggling with identity and physical stability.
* **Caterpillar:** A languid, hookah-smoking insect sitting atop a mushroom; prone to sternness and contempt.
* **Pigeon:** An agitated, egg-laying bird living in a tree; perceives Alice as a serpent.

**Events & Scene Beats:**
1.  **The Confrontation:** Alice meets the Caterpillar on a mushroom. The Caterpillar questions her identity ("Who are you?"). Alice explains her confusion regarding her frequent size changes.
2.  **The Poem Test:** To test Alice's memory/identity, the Caterpillar commands her to recite "You are old, Father William." Alice recites it, but the Caterpillar declares it "wrong from beginning to end" due to altered words.
3.  **Size Negotiation:** The Caterpillar asks what size Alice wants to be. Alice requests to be slightly larger than three inches. The Caterpillar (who is exactly three inches high) reacts angrily to this suggestion.
4.  **The Mushroom Instruction:** The Caterpillar crawls away into the grass, leaving a vital clue: one side of the mushroom makes you grow taller, and the other makes you shorter.
5.  **First Transformation (Shrinking):** Alice attempts to test the mushroom. She nibbles a piece from the right-hand side; her chin immediately strikes her foot as she shrinks rapidly.
6.  **Second Transformation (Elongation):** Desperate, Alice swallows a morsel of the left-hand bit. Her head is freed, but her shoulders disappear, replaced by an immense, serpent-like neck rising above a sea of green leaves (the treetops).
7.  **The Pigeon Encounter:** While Alice struggles to maneuver her long, zigzagging neck among the branches, a large Pigeon flies into her face and attacks her, screaming "Serpent!"
8.  **Identity Dispute:** The Pigeon refuses to believe Alice is a little girl, insisting that any girl with such a neck must be a serpent. Alice attempts to defend herself but is eventually ignored as the Pigeon returns to its nest.
9.  **Size Stabilization:** Alice crouches among the branches, untwisting her neck. She nibbles alternating pieces of the mushroom until she successfully returns to her "usual" height.
10. **The Discovery:** Alice reaches an open clearing containing a small house (approx. four feet high). 
11. **Final Transformation:** To avoid frightening the inhabitants of the house, Alice nibbles the right-hand bit of the mushroom again, shrinking herself down to nine inches in height before approaching.

**Visual Continuity & Objects:**
* **The Mushroom:** A perfectly round object with two distinct sides (one for growing, one for shrinking).
* **Hookah:** Used by the Caterpillar.
* **Physical State:** Alice's neck can bend like a serpent; her size is highly volatile based on which piece of mushroom is consumed.
````

## Raw Response
````text
[[FILMCREATOR_PACKET]]
task: character_extraction
version: 1

[[FILMCREATOR_RECORD]]
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
scale_hint: tiny
renderability_hint: renderable
confidence: 0.9
direct_identity_evidence: "Alice explains her confusion regarding her frequent size changes."
direct_visual_evidence: "A young girl experiencing rapid size fluctuations; head freed, shoulders disappear, replaced by an immense, serpent-like neck rising above a sea of green leaves."
costume_or_covering_evidence: ""
movement_evidence: "Struggling to maneuver her long, zigzagging neck among the branches; nibbles alternating pieces of the mushroom."
associated_entities: ["caterpillar", "pigeon", "mushroom"]
alias_or_role_evidence: ""
unknowns: []
source_refs: ["CH005"]
[[SECTION character_index_markdown]]
[[markdown]]
# Alice
**Role:** Protagonist

**Status:** Physically Present

**Physical Description:**
A young girl subject to extreme and rapid size fluctuations. Her physical form is highly unstable in this chapter. At one point, her neck elongates into an immense, serpent-like structure that rises above the forest canopy, leaving her shoulders seemingly non-existent or obscured by the length of the neck. She can shrink to as small as three inches or nine inches.

**Costume & Silhouette:**
Silhouette is highly variable due to size and neck elongation (zigzagging, serpentine neck). 

**Descriptive Noun Phrases:**
* Young girl with volatile scale
* Serpentine-necked girl
* Tiny girl (nine inches)
* Elongated neck silhouette

**Uncertainty Notes:**
Specific clothing details are not provided in this chapter text.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
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
direct_identity_evidence: "The Caterpillar questions her identity."
direct_visual_evidence: "Languid, hookah-smoking insect sitting atop a mushroom; exactly three inches high; crawls away into the grass."
costume_or_covering_evidence: ""
movement_evidence: "Sitting atop a mushroom; crawls away into the grass."
associated_entities: ["alice", "mushroom", "hookah"]
alias_or_role_evidence: ""
unknowns: []
source_refs: ["CH005"]
[[SECTION character_index_markdown]]
[[markdown]]
# Caterpillar
**Role:** Supporting Character / Mentor (unconventional)

**Status:** Physically Present

**Physical Description:**
A languid insect, approximately three inches in height. 

**Costume & Silhouette:**
Uses a hookah. The silhouette is that of a large insect perched on a mushroom.

**Descriptive Noun Phrases:**
* Hookah-smoking insect
* Three-inch tall caterpillar
* Languid insect atop a mushroom

**Uncertainty Notes:**
Specific color patterns or exact species morphology (beyond "insect") are not detailed in the text.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
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
confidence: 0.8
direct_identity_evidence: "The Pigeon refuses to believe Alice is a little girl."
direct_visual_evidence: "A large Pigeon flies into her face and attacks her; lives in a tree; returns to its nest."
costume_or_covering_evidence: ""
movement_evidence: "Flies into Alice's face; returns to its nest."
associated_entities: ["alice"]
alias_or_role_evidence: ""
unknowns: []
source_refs: ["CH005"]
[[SECTION character_index_markdown]]
[[markdown]]
# Pigeon
**Role:** Antagonist (minor/misunderstanding)

**Status:** Physically Present

**Physical Description:**
A large bird.

**Costume & Silhouette:**
Standard avian silhouette.

**Descriptive Noun Phrases:**
* Agitated large pigeon
* Egg-laying bird
* Tree-dwelling pigeon

**Uncertainty Notes:**
Specific coloration or breed of the pigeon is not specified.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
asset_id: inhabitants_of_small_house
canonical_character_id: house_inhabitants
aliases: []
is_fully_identified: false
manual_description_required: true
manual_description_reason: "Characters are only referenced as 'inhabitants' and have no physical description provided."
clarification_required: true
clarification_reason: "The text mentions inhabitants but provides zero visual or character data."
clarification_question: "What species/type are the inhabitants of the four-foot-high house?"
character_type_hint: unknown
morphology_hint: unknown
scale_hint: tiny
renderability_hint: context_only
confidence: 0.5
direct_identity_evidence: ""
direct_visual_evidence: ""
costume_or_covering_evidence: ""
movement_evidence: ""
associated_entities: ["small_house"]
alias_or_role_evidence: "inhabitants"
unknowns: ["physical appearance", "species", "number of individuals"]
source_refs: ["CH005"]
[[SECTION character_index_markdown]]
[[markdown]]
# Inhabitants of the Small House
**Role:** Referenced Characters

**Status:** Referenced (Not Present)

**Physical Description:**
Unknown.

**Costume & Silhouette:**
Unknown.

**Descriptive Noun Phrases:**
* House inhabitants

**Uncertainty Notes:**
These characters are mentioned only as a reason for Alice to shrink herself. No visual information exists in the text.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]
[[/FILMCREATOR_PACKET]]
````
