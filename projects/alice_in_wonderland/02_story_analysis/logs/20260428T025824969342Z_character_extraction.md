# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-28T02:58:24.969843+00:00
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
- **Characters:** Alice, Alice's Sister.
- **Events:** Alice sits by the bank, bored, looking at a book with no pictures/conversations. 
- **Visual State:** Hot, sleepy day.

**Location: Field / Hedge**
- **Characters:** Alice, White Rabbit (Pink eyes, wearing a waistcoat with a pocket).
- **Events:** 
    - The White Rabbit runs past Alice, muttering "Oh dear! Oh dear! I shall be late!"
    - The White Rabbit pulls a watch out of its waistcoat pocket and checks it.
    - Alice, driven by curiosity, chases the Rabbit.
    - The White Rabbit enters a large rabbit-hole under a hedge.
    - Alice follows the Rabbit into the hole.

**Location: The Rabbit-Hole / Deep Well (Transition)**
- **Characters:** Alice.
- **Events:** 
    - The tunnel dips suddenly into a deep well/shaft.
    - Alice falls slowly through the darkness.
    - **Object Interaction:** Alice passes cupboards and bookshelves filled with maps and pictures. She grabs an empty jar labeled "ORANGE MARMALADE" from a shelf and places it into a cupboard to avoid dropping it on anyone below.
    - **Dialogue/Internal Monologue:** Alice muses about the depth of the fall, her school lessons (latitude/longitude), and her cat Dinah.
    - **Visual State:** Dark, descending through a vertical shaft lined with domestic objects.

**Location: Heap of Sticks and Dry Leaves**
- **Characters:** Alice, White Rabbit (distant).
- **Events:** 
    - Alice lands with a "thump" on a heap of sticks/leaves; she is unhurt.
    - The White Rabbit is seen in the distance hurrying down a long passage, muttering about his ears and whiskers.
    - Alice chases after him.

**Location: Long, Low Hall**
- **Characters:** Alice.
- **Setting Details:** Lit by a row of lamps hanging from the roof; many doors line the walls, all locked.
- **Events:** 
    - Alice explores the hall, trying every door, but finds them all locked.
    - **Object Interaction (The Table):** Alice finds a three-legged glass table. On it sits a tiny golden key.
    - **Discovery:** Alice finds a low curtain; behind it is a small door (approx. 15 inches high).
    - **Action:** Alice uses the golden key on the small door; it fits.
    - **Reveal:** Through the small door, Alice sees a beautiful garden with bright flowers and fountains.
    - **Constraint:** Alice realizes she is too large to fit through the door.

**Location: Long, Low Hall (Continued)**
- **Characters:** Alice.
- **Events:** 
    - **Object Interaction (The Bottle):** Alice returns to the glass table. A small bottle labeled "DRINK ME" has appeared (not previously there).
    - **Action:** Alice inspects the label for "poison," finds none, and drinks the liquid.
    - **Sensory Detail:** The drink tastes of cherry-tart, custard, pineapple, roast turkey, toffee, and hot buttered toast.
    - **Transformation 1:** Alice shrinks to ten inches high.
    - **Conflict:** Alice realizes she left the golden key on top of the glass table. She tries to climb the slippery glass leg but fails.
    - **Emotional State:** Alice sits down and cries.
    - **Object Interaction (The Cake):** Alice finds a small glass box under the table containing a tiny cake marked "EAT ME" in currants.
    - **Action:** Alice eats the cake to attempt to change her size again.
    - **Transformation 2 (Unresolved):** After eating, she initially remains the same size, then continues eating the rest of the cake.
````

## Raw Response
````text
[[FILMCREATOR_PACKET]]
[[SECTION character_index_markdown]]
# Character Index

- [Alice](#alice)
- [Alice's Sister](#alices-sister)
- [White Rabbit](#white-rabbit)
- [Dinah](#dinah)
[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: alice
canonical_character_id: alice
aliases: []
is_fully_identified: true
manual_description_required: true
manual_description_reason: While her size changes are documented, her specific facial features, hair color/style, and exact clothing (beyond the implication of a child) are not described in this chapter.
clarification_required: false
clarification_reason: 
clarification_question: 
character_type_hint: human
morphology_hint: biped
scale_hint: unknown
renderability_hint: renderable
confidence: 1.0
direct_identity_evidence: "Alice sits by the bank... Alice, driven by curiosity, chases the Rabbit."
direct_visual_evidence: "Alice shrinks to ten inches high... Alice eats the cake..."
costume_or_covering_evidence: 
movement_evidence: "Alice falls slowly through the darkness... Alice tries to climb the slippery glass leg..."
associated_entities: ["alices_sister", "white_rabbit", "dinah"]
alias_or_role_evidence: 
unknowns: []
source_refs: []
[[SECTION markdown]]
# Alice
**Role:** Protagonist

**Status:** Physically Present

**Physical Description:**
A young girl. Her physical scale is highly variable, ranging from human-scale to ten inches high during the chapter. Specific hair color and facial features are not provided in the text.

**Costume & Silhouette:**
Not explicitly described, though she is a child capable of interacting with domestic objects like cupboards and bookshelves.

**Descriptive Noun Phrases:**
- Young girl
- Shrinking child
- Curious explorer

**Uncertainty Notes:**
Specific visual design (hair, eye color, dress) must be established via external art direction as the text focuses on her scale and actions rather than her appearance.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: alices_sister
canonical_character_id: alices_sister
aliases: []
is_fully_identified: true
manual_description_required: true
manual_description_reason: Only mentioned as being present by the riverbank; no physical description is provided.
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
unknowns: []
source_refs: []
[[SECTION markdown]]
# Alice's Sister
**Role:** Supporting Character (Mentioned/Present at start)

**Status:** Physically Present (Initial scene)

**Physical Description:**
No physical description provided in the text.

**Costume & Silhouette:**
Unknown.

**Descriptive Noun Phrases:**
- Alice's sister
- Woman by the riverbank

**Uncertainty Notes:**
Character is a background presence with no visual identifiers provided in this chapter.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
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
direct_identity_evidence: "The White Rabbit runs past Alice... The White Rabbit pulls a watch out of its waistcoat pocket..."
direct_visual_evidence: "Pink eyes, wearing a waistcoat with a pocket."
costume_or_covering_evidence: "wearing a waistcoat with a pocket"
movement_evidence: "runs past Alice... hurrying down a long passage"
associated_entities: ["alice"]
alias_or_role_evidence: "The White Rabbit"
unknowns: []
source_refs: []
[[SECTION markdown]]
# White Rabbit
**Role:** Catalyst / Recurring Character

**Status:** Physically Present

**Physical Description:**
A rabbit with pink eyes. 

**Costume & Silhouette:**
Wears a waistcoat that contains a pocket for a watch.

**Descriptive Noun Phrases:**
- White rabbit with pink eyes
- Rabbit in a waistcoat
- Hurrying rabbit

**Uncertainty Notes:**
None. Visual details are specific.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: dinah
canonical_character_id: dinah
aliases: []
is_fully_identified: true
manual_description_required: true
manual_description_reason: The character is only mentioned in Alice's thoughts; no physical description of the cat is provided.
clarification_required: false
clarification_reason: 
clarification_question: 
character_type_hint: animal
morphology_hint: quadruped
scale_hint: small
renderability_hint: context_only
confidence: 0.7
direct_identity_evidence: "her cat Dinah."
direct_visual_evidence: 
costume_or_covering_evidence: 
movement_evidence: 
associated_entities: ["alice"]
alias_or_role_evidence: 
unknowns: []
source_refs: []
[[SECTION markdown]]
# Dinah
**Role:** Referenced Character

**Status:** Referenced (Not physically present)

**Physical Description:**
A cat. No specific color, breed, or markings are mentioned in the text.

**Costume & Silhouette:**
N/A

**Descriptive Noun Phrases:**
- Alice's cat
- Dinah the cat

**Uncertainty Notes:**
Visual appearance is entirely unknown based on this chapter alone.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]
[[/FILMCREATOR_PACKET]]
````
