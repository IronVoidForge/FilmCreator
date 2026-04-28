# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-28T03:08:54.155839+00:00
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
* **Alice:** A young girl experiencing rapid size fluctuations; currently struggling with identity and physical control.
* **Caterpillar:** A languid, hookah-smoking insect sitting atop a mushroom; prone to sternness and contempt.
* **Pigeon:** An agitated bird living in a tree; perceives Alice as a serpent due to her elongated neck.

**Events & Scene Beats:**
1.  **The Confrontation:** Alice meets the Caterpillar on a mushroom. The Caterpillar questions Alice's identity ("Who are you?"). Alice explains her confusion regarding her frequent size changes.
2.  **The Poem Test:** To test Alice's memory, the Caterpillar commands her to recite "You are old, Father William." Alice recites it, but the Caterpillar declares it "wrong from beginning to end," creating a moment of tense silence.
3.  **Size Negotiation:** The Caterpillar asks what size Alice wants to be. Alice requests to be slightly larger than three inches. The Caterpillar (who is exactly three inches high) reacts angrily to being called small.
4.  **The Mushroom Instruction:** The Caterpillar crawls away into the grass, leaving Alice with a cryptic instruction: one side of the mushroom makes you grow taller, the other shorter.
5.  **First Transformation (Shrinking):** Alice breaks off a piece of the right-hand side of the round mushroom and eats it. She immediately experiences a violent physical reaction as she shrinks so rapidly that her chin strikes her foot.
6.  **Second Transformation (Elongation):** Desperate, Alice eats a morsel of the left-hand bit. Her head is freed, but her shoulders disappear, replaced by an immense, serpent-like neck rising above a canopy of green leaves (tree tops).
7.  **The Pigeon Encounter:** While Alice attempts to maneuver her flexible, zigzagging neck through the branches, a large Pigeon flies into her face and attacks her, screaming "Serpent!" 
8.  **Identity Dispute:** A dialogue ensues between the Pigeon and Alice. The Pigeon is convinced Alice is a serpent because of her neck; Alice insists she is a little girl. The Pigeon remains skeptical but eventually settles back into its nest.
9.  **Restoration:** Alice, still holding the mushroom pieces, nibbles alternating sides to stabilize her size. She successfully returns to her "usual" height.
10. **The Small House Discovery:** Alice discovers an open clearing containing a small house (approx. four feet high). 
11. **Final Transformation (Miniaturization):** To avoid frightening the inhabitants of the house, Alice nibbles the right-hand bit of the mushroom again, shrinking herself down to nine inches in height before approaching.
````

## Raw Response
````text
[[FILMCREATOR_PACKET]]
[SECTION character_index_markdown]
# Character Index: Chapter CH005

* [[alice_wonderland]]
* [[caterpillar_mushroom]]
* [[pigeon_bird]]
[[/SECTION]]

[[FILMCREATOR_RECORD]]
type=character
asset_id=alice_wonderland
canonical_character_id=alice
aliases=["Alice"]
is_fully_identified=true
manual_description_required=false
manual_description_reason=""
clarification_required=false
clarification_reason=""
clarification_question=""
character_type_hint=human
morphology_hint=biped
scale_hint=tiny
renderability_hint=renderable
confidence=1.0
direct_identity_evidence="Directly named as Alice; identifies herself as a little girl."
direct_visual_evidence="Described as a young girl undergoing extreme size fluctuations (from 9 inches to having an elongated neck reaching tree tops)."
costume_or_covering_evidence=""
movement_evidence="Struggles with physical control during rapid shrinking/growing; maneuvers a zigzagging neck through branches."
associated_entities=["caterpillar_mushroom", "pigeon_bird"]
alias_or_role_evidence=""
unknowns=""
source_refs=""
[SECTION markdown]
# Alice
**Role:** Protagonist

**Status:** Physically Present

**Physical Description:**
A young girl. Her size is highly unstable in this chapter, ranging from 9 inches tall to a height where her neck extends above the forest canopy. During one transformation, her neck becomes immense and serpent-like, causing her shoulders to seemingly disappear.

**Costume & Silhouette:**
Not explicitly detailed in this chapter, but her silhouette changes drastically from a standard child to an elongated, serpentine form, and finally to a miniature 9-inch figure.

**Descriptive Noun Phrases:**
* Young girl
* Rapidly fluctuating size
* Serpent-necked girl (during transformation)
* Nine-inch tall girl (at end of chapter)

**Uncertainty Notes:**
Specific clothing details are not provided in this text segment.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type=character
asset_id=caterpillar_mushroom
canonical_character_id=caterpillar
aliases=["Caterpillar"]
is_fully_identified=true
manual_description_required=false
manual_description_reason=""
clarification_required=false
clarification_reason=""
clarification_question=""
character_type_hint=creature
morphology_hint=multi_legged
scale_hint=small
renderability_hint=renderable
confidence=0.9
direct_identity_evidence="Identified as the Caterpillar."
direct_visual_evidence="An insect sitting atop a mushroom; exactly three inches high; smokes a hookah."
costume_or_covering_evidence=""
movement_evidence="Crawls away into the grass."
associated_entities=["alice_wonderland"]
alias_or_role_evidence=""
unknowns=""
source_refs=""
[SECTION markdown]
# Caterpillar
**Role:** Obstacle / Guide

**Status:** Physically Present

**Physical Description:**
A languid insect, approximately three inches in height. He is seen sitting atop a mushroom and smoking a hookah.

**Costume & Silhouette:**
An insectoid silhouette; associated with a hookah.

**Descriptive Noun Phrases:**
* Languid insect
* Hookah-smoking caterpillar
* Three-inch tall creature
* Stern, contemptuous insect

**Uncertainty Notes:**
Specific color patterns or exact species morphology are not detailed beyond being an "insect."
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type=character
asset_id=pigeon_bird
canonical_character_id=pigeon
aliases=["Pigeon"]
is_fully_identified=true
manual_description_required=false
manual_description_reason=""
clarification_required=false
clarification_reason=""
clarification_question=""
character_type_hint=animal
morphology_hint=winged
scale_hint=small
renderability_hint=renderable
confidence=1.0
direct_identity_evidence="Identified as a Pigeon."
direct_visual_evidence="A large bird living in a tree; flies into Alice's face."
costume_or_covering_evidence=""
movement_evidence="Flies; lives in a nest in a tree."
associated_entities=["alice_wonderland"]
alias_or_role_evidence=""
unknowns=""
source_refs=""
[SECTION markdown]
# Pigeon
**Role:** Agitated Encounter

**Status:** Physically Present

**Physical Description:**
A large bird. 

**Costume & Silhouette:**
Standard avian silhouette.

**Descriptive Noun Phrases:**
* Large, agitated pigeon
* Tree-dwelling bird
* Screaming bird

**Uncertainty Notes:**
Specific plumage colors or breed details are not provided.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]
[[/FILMCREATOR_PACKET]]
````
