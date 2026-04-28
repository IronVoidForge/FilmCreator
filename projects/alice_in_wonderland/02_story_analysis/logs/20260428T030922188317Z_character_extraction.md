# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-28T03:09:22.188317+00:00
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
[[SECTION character_index_markdown]]
[[markdown]]
# Character Index - Chapter 5

## Alice
[View Profile](#alice)

## Caterpillar
[View Profile](#caterpillar)

## Pigeon
[View Profile](#pigeon)
[[/SECTION]]
[[/FILMCREATOR_PACKET]]

[[FILMCREATOR_RECORD]]
[[SECTION markdown]]
# Alice
**Role:** Protagonist / Identity-seeking child

### Status
* **Presence:** Physically Present

### Physical Description
* **Base Form:** A young girl.
* **Size Fluctuations:** 
    * Shrinks rapidly (chin strikes feet).
    * Elongates into a serpent-like form with an immense neck and no visible shoulders.
    * Shrinks to nine inches in height.
    * Shrinks to slightly larger than three inches.
* **Morphology Notes:** Highly elastic/malleable body; neck can zigzag through tree branches.

### Costume & Silhouette
* **Silhouette:** Varies wildly from a standard child to an extremely long, serpentine vertical line (neck and head only).

### Prompting Keywords
* young girl, size-shifting, elongated neck, serpent-like morphology, tiny scale (9 inches), rapid physical transformation.

### Uncertainty Notes
* Specific clothing colors or patterns are not mentioned in this chapter.
[[/SECTION]]
[[SECTION character_index_markdown]]
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
[[SECTION markdown]]
# Caterpillar
**Role:** Stern mentor / Obstacle

### Status
* **Presence:** Physically Present

### Physical Description
* **Species:** Large insect.
* **Size:** Exactly three inches high.
* **Behavioral Traits:** Languid, stern, contemptuous.

### Costume & Silhouette
* **Accessories:** Smoking a hookah.
* **Positioning:** Sitting atop a mushroom.

### Prompting Keywords
* large caterpillar, hookah-smoking insect, sitting on mushroom, three inches tall, languid posture, stern expression.

### Uncertainty Notes
* Specific color/pattern of the caterpillar's skin is not described.
[[/SECTION]]
[[SECTION character_index_markdown]]
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
[[SECTION markdown]]
# Pigeon
**Role:** Agitated witness / Accuser

### Status
* **Presence:** Physically Present

### Physical Description
* **Species:** Large bird.
* **Behavioral Traits:** Agitated, screaming, skeptical.

### Costume & Silhouette
* **Location:** Lives in a tree/nest.

### Prompting Keywords
* large pigeon, agitated bird, flying through canopy, nesting bird.

### Uncertainty Notes
* Specific breed or color of the pigeon is not specified.
[[/SECTION]]
[[SECTION character_index_markdown]]
[[/SECTION]]
[[/FILMCREATOR_RECORD]]
````
