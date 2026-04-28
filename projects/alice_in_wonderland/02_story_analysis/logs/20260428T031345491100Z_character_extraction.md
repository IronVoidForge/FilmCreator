# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-28T03:13:45.491100+00:00
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

Chapter id: CH001

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

**Location: Riverbank**
*   **Characters:** Alice, Alice's Sister.
*   **Events:** Alice sits by the bank, feeling bored and sleepy. She contemplates making a daisy-chain.
*   **Visual State:** Hot, sleepy day.

**Location: Field / Hedge Entrance**
*   **Characters:** Alice, White Rabbit (Pink eyes, wearing a waistcoat with a pocket).
*   **Events:** 
    *   White Rabbit runs past Alice.
    *   White Rabbit speaks aloud: “Oh dear! Oh dear! I shall be late!”
    *   White Rabbit pulls a watch out of its waistcoat-pocket and checks it.
    *   Alice pursues the Rabbit.
    *   The White Rabbit enters a large rabbit-hole under a hedge.
    *   Alice follows the Rabbit into the hole.

**Location: The Rabbit-Hole / Deep Well (Transition)**
*   **Characters:** Alice.
*   **Events:** 
    *   The tunnel dips suddenly into a deep well.
    *   Alice falls slowly through the dark shaft.
    *   **Object Interaction:** Alice passes shelves/cupboards containing maps, pictures, and jars. She grabs an empty jar labeled “ORANGE MARMALADE” and places it in a cupboard to avoid dropping it on anyone below.
    *   **Internal Monologue/Action:** Alice calculates her depth (approx. 4000 miles) and muses about Latitude, Longitude, and the "Antipathies." She attempts a curtsey while falling.
    *   Alice begins to doze off, dreaming of her cat, Dinah.

**Location: Heap of Sticks and Dry Leaves**
*   **Characters:** Alice, White Rabbit (distant).
*   **Events:** 
    *   Alice lands with a "thump!" on a heap of sticks/leaves. She is unhurt.
    *   The White Rabbit is seen in the distance, hurrying down a passage.
    *   White Rabbit turns a corner, shouting: “Oh my ears and whiskers, how late it’s getting!”
    *   Alice chases the Rabbit around the corner.

**Location: Long, Low Hall**
*   **Characters:** Alice.
*   **Setting Details:** Lit by a row of hanging lamps; many doors line the walls, all locked.
*   **Events:** 
    *   Alice explores the hall, trying every door, but finds them all locked.
    *   **Object Interaction (The Table):** Alice finds a three-legged glass table. On it sits a tiny golden key.
    *   **Discovery:** Alice finds a low curtain; behind it is a small door (approx. 15 inches high).
    *   **Action:** Alice uses the golden key on the small door. It fits.
    *   **Reveal:** The door leads to a passage looking into a "lovely garden" with bright flowers and fountains.
    *   **Conflict:** Alice is too large to enter the door.

**Location: Long, Low Hall (Transformation Sequence)**
*   **Characters:** Alice.
*   **Events:** 
    *   Alice returns to the glass table.
    *   **Object Interaction (The Bottle):** A small bottle with a "DRINK ME" label has appeared on the table.
    *   **Action:** Alice inspects the bottle for poison, then drinks the contents (tasting of cherry-tart, custard, pineapple, roast turkey, toffee, and hot buttered toast).
    *   **Transformation 1:** Alice shrinks to ten inches high.
    *   **Conflict:** Alice realizes she left the golden key on top of the glass table. She is now too small to reach it. She tries to climb a table leg but it is too slippery.
    *   **Emotional State:** Alice sits down and cries.
    *   **Object Interaction (The Cake):** Alice finds a small glass box under the table containing a tiny cake marked "EAT ME" in currants.
    *   **Decision:** Alice decides to eat the cake to either grow large enough to reach the key or small enough to fit under the door.
    *   **Action:** Alice eats the cake.
    *   **Result/Uncertainty:** After eating, she initially remains the same size, then continues eating until finished. (End of Chapter).
````

## Raw Response
````text
[[FILMCREATOR_PACKET]]
task: character_extraction
version: 1

[[SECTION character_index_markdown]]
[[markdown]]
# Character Index - CH001

- [Alice](alice)
- [Alice's Sister](alices_sister)
- [White Rabbit](white_rabbit)
- [Dinah](dinah)
[[/SECTION]]
[[/FILMCREATOR_PACKET]]

[[FILMCREATOR_RECORD]]
asset_id: alice
canonical_character_id: alice
aliases: []
is_fully_identified: true
manual_description_required: true
manual_description_reason: The text provides behavioral and scale information but lacks specific details regarding hair color, eye color, or facial features necessary for consistent character design.
clarification_required: false
clarification_reason: 
clarification_question: 
character_type_hint: human
morphology_hint: biped
scale_hint: unknown
renderability_hint: renderable
confidence: 0.9
direct_identity_evidence: "Alice sits by the bank..."
direct_visual_evidence: "Alice shrinks to ten inches high."
costume_or_covering_evidence: 
movement_evidence: "Alice pursues the Rabbit.", "Alice falls slowly through the dark shaft.", "Alice attempts a curtsey while falling."
associated_entities: ["alices_sister", "white_rabbit", "dinah"]
alias_or_role_evidence: 
unknowns: "Specific facial features and hair/eye color are not mentioned in this chapter."
source_refs: []
[[SECTION markdown]]
# Alice
**Role:** Protagonist

**Status:** Physically Present (Variable Scale)

**Physical Description:**
- **Scale:** Highly variable. Starts at human scale, shrinks to ten inches high after drinking from the bottle, and changes size again after eating the cake.
- **Traits:** Capable of performing a curtsey while falling; demonstrates curiosity and emotional volatility (crying when unable to reach the key).

**Costume & Silhouette:**
- Not explicitly described in this chapter.

**Descriptive Noun Phrases:**
- Small girl, shrinking child, curious wanderer.

**Uncertainty Notes:**
- Visual appearance (hair, eyes, clothing) is not detailed in the text; requires manual definition for consistent rendering.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
asset_id: alices_sister
canonical_character_id: alices_sister
aliases: []
is_fully_identified: true
manual_description_required: true
manual_description_reason: Only mentioned as being present by the riverbank; no physical description provided.
clarification_required: false
clarification_reason: 
clarification_question: 
character_type_hint: human
morphology_hint: biped
scale_hint: human_scale
renderability_hint: context_only
confidence: 0.8
direct_identity_evidence: "Alice's Sister."
direct_visual_evidence: 
costume_or_covering_evidence: 
movement_evidence: 
associated_entities: ["alice"]
alias_or_role_evidence: 
unknowns: "Physical appearance, age, and clothing are entirely unstated."
source_refs: []
[[SECTION markdown]]
# Alice's Sister
**Role:** Supporting Character (Mentioned/Present)

**Status:** Physically Present (Initial scene)

**Physical Description:**
- **Scale:** Human scale.

**Costume & Silhouette:**
- Unknown.

**Descriptive Noun Phrases:**
- Older sister, companion by the riverbank.

**Uncertainty Notes:**
- No visual details provided in the text.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
asset_id: white_rabbit
canonical_character_id: white_rabbit
aliases: ["Rabbit"]
is_fully_identified: true
manual_description_required: false
manual_description_reason: 
clarification_required: false
clarification_reason: 
clarification_question: 
character_type_hint: animal
morphology_hint: quadruped
scale_hint: small
renderability_hint: renderable
confidence: 1.0
direct_identity_evidence: "White Rabbit runs past Alice."
direct_visual_evidence: "Pink eyes, wearing a waistcoat with a pocket.", "pulls a watch out of its waistcoat-pocket"
costume_or_covering_evidence: "wearing a waistcoat with a pocket"
movement_evidence: "runs past Alice", "hurrying down a passage"
associated_entities: ["alice"]
alias_or_role_evidence: 
unknowns: ""
source_refs: []
[[SECTION markdown]]
# White Rabbit
**Role:** Catalyst / Recurring Character

**Status:** Physically Present

**Physical Description:**
- **Eyes:** Pink.
- **Scale:** Small (rabbit-sized).

**Costume & Silhouette:**
- **Clothing:** Wearing a waistcoat with a pocket.
- **Accessories:** Carries a watch.

**Descriptive Noun Phrases:**
- Pink-eyed rabbit, waistcoat-wearing rabbit, frantic rabbit.

**Uncertainty Notes:**
- None; visual markers are specific.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
asset_id: dinah
canonical_character_id: dinah
aliases: []
is_fully_identified: true
manual_description_required: true
manual_description_reason: Character is only mentioned in a dream/thought; no physical description provided.
clarification_required: false
clarification_reason: 
clarification_question: 
character_type_hint: animal
morphology_hint: quadruped
scale_hint: small
renderability_hint: context_only
confidence: 0.7
direct_identity_evidence: "her cat, Dinah."
direct_visual_evidence: 
costume_or_covering_evidence: 
movement_evidence: 
associated_entities: ["alice"]
alias_or_role_evidence: 
unknowns: "Physical appearance (color, breed, size) is not described."
source_refs: []
[[SECTION markdown]]
# Dinah
**Role:** Referenced Character

**Status:** Referenced (Dream/Thought)

**Physical Description:**
- **Type:** Cat.

**Costume & Silhouette:**
- Unknown.

**Descriptive Noun Phrases:**
- Alice's cat.

**Uncertainty Notes:**
- No visual details provided; character is not physically present in the scene.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]
````
