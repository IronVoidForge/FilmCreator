# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-28T03:28:47.044272+00:00
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
*   **Events:** Alice sits by the bank, bored, looking at her sister's book (no pictures/conversations). 
*   **Visual State:** Hot, sleepy day.

**Location: Field / Hedge**
*   **Characters:** Alice, White Rabbit.
*   **Events:** A White Rabbit with pink eyes runs past Alice. The Rabbit speaks ("Oh dear! Oh dear! I shall be late!") and checks a watch from its waistcoat-pocket. 
*   **Action:** Alice chases the Rabbit and watches it disappear down a large rabbit-hole under a hedge.

**Location: The Rabbit-Hole / Deep Well**
*   **Characters:** Alice (falling).
*   **Events:** Alice plunges down the hole. The descent is slow, like falling through a deep well. 
*   **Environment/Objects:** The walls are lined with cupboards, bookshelves, maps, and pictures on pegs. 
*   **Interaction:** Alice grabs an empty jar labeled "ORANGE MARMALADE" from a shelf; she places it into a cupboard to avoid dropping it on anyone below.
*   **Internal State:** Alice muses about the depth (4,000 miles), latitude/longitude, and the "Antipathies." She attempts a curtsey while falling.

**Location: Bottom of the Hole (Heap of sticks/leaves)**
*   **Characters:** Alice, White Rabbit (distant).
*   **Events:** Alice lands with a "thump!" on a heap of sticks and dry leaves. She is unhurt. 
*   **Action:** The White Rabbit is seen hurrying down a long passage; Alice chases it.
*   **Transition:** The Rabbit turns a corner, shouting about the time, and disappears.

**Location: Long, Low Hall**
*   **Characters:** Alice.
*   **Environment/Objects:** A hall lit by a row of hanging lamps. Numerous doors line the walls, but all are locked. 
*   **Object Interaction:** Alice finds a three-legged solid glass table in the middle of the hall. On it sits a tiny golden key.
*   **Discovery:** Alice finds a low curtain; behind it is a small door (15 inches high). The golden key fits this lock.
*   **Reveal:** Through the small door, Alice sees a beautiful garden with bright flowers and fountains, but she is too large to enter.

**Location: Long, Low Hall (Second Pass)**
*   **Characters:** Alice.
*   **Object Interaction:** Alice returns to the glass table. A small bottle labeled "DRINK ME" has appeared on it. 
*   **Action:** Alice checks for a "poison" label. Finding none, she drinks the liquid (tastes of cherry-tart, custard, pineapple, roast turkey, toffee, and hot buttered toast).
*   **Transformation 1:** Alice shrinks to ten inches high.
*   **Conflict:** Alice realizes she left the golden key on top of the glass table. She tries to climb a table leg, but it is too slippery.
*   **Emotional State:** Alice cries, then scolds herself.
*   **Object Interaction:** Alice finds a small glass box under the table containing a tiny cake marked "EAT ME" in currants.
*   **Action:** Alice eats the cake to attempt to change her size again.
*   **Transformation 2 (Incomplete):** After eating, she initially remains the same size, then continues eating the rest of the cake.
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
manual_description_required: true
manual_description_reason: While her actions and size changes are documented, her specific facial features, hair color/style, and exact clothing details are not explicitly described in this chapter text.
clarification_required: false
clarification_reason: 
clarification_question: 
character_type_hint: human
morphology_hint: biped
scale_hint: unknown
renderability_hint: renderable
confidence: 0.9
direct_identity_evidence: "Alice sits by the bank... Alice chases the Rabbit... Alice plunges down the hole."
direct_visual_evidence: "Alice shrinks to ten inches high... she is too large to enter [the small door]."
costume_or_covering_evidence: 
movement_evidence: "Alice plunges down the hole... attempts a curtsey while falling... tries to climb a table leg."
associated_entities: ["alice_s_sister", "white_rabbit"]
alias_or_role_evidence: 
unknowns: ["facial features", "hair color/style", "specific clothing details"]
source_refs: []

[[SECTION character_index_markdown]]
[[SECTION markdown]]
# Alice
**Role:** Protagonist

**Status:** Physically Present

**Physical Description:**
- A young girl.
- Subject to significant scale changes: starts at human scale, shrinks to ten inches high after drinking from the "DRINK ME" bottle.
- Note: Specific hair and clothing details are not provided in this chapter.

**Costume & Silhouette:**
- Silhouette changes drastically due to size transformations (human scale vs. 10-inch scale).

**Descriptive Noun Phrases:**
- Young girl
- Shrinking child
- Curious explorer

**Uncertainty Notes:**
- Exact appearance (hair, eyes, dress) is not described in the text; requires external design direction or character sheet.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
asset_id: alice_s_sister
canonical_character_id: alice_s_sister
aliases: []
is_fully_identified: true
manual_description_required: true
manual_description_reason: The character is only mentioned as being present with Alice; no physical description of her appearance is provided.
clarification_required: false
clarification_reason: 
clarification_question: 
character_type_hint: human
morphology_hint: biped
scale_hint: human_scale
renderability_hint: context_only
confidence: 0.8
direct_identity_evidence: "Alice's Sister... looking at her sister's book"
direct_visual_evidence: 
costume_or_covering_evidence: 
movement_evidence: 
associated_entities: ["alice"]
alias_or_role_evidence: 
unknowns: ["physical appearance", "age", "clothing"]
source_refs: []

[[SECTION character_index_markdown]]
[[SECTION markdown]]
# Alice's Sister
**Role:** Supporting Character (Referenced/Present at start)

**Status:** Physically Present (Initial scene only)

**Physical Description:**
- No physical description provided in the text.

**Costume & Silhouette:**
- Unknown.

**Descriptive Noun Phrases:**
- Alice's sister
- Reader

**Uncertainty Notes:**
- Character is a background presence with zero visual descriptors; likely intended as a non-visual anchor for the opening scene.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
asset_id: white_rabbit
canonical_character_id: white_rabbit
aliases: ["White Rabbit"]
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
direct_identity_evidence: "A White Rabbit with pink eyes runs past Alice."
direct_visual_evidence: "White Rabbit with pink eyes... checks a watch from its waistcoat-pocket."
costume_or_covering_evidence: "waistcoat-pocket"
movement_evidence: "runs past Alice... hurrying down a long passage"
associated_entities: ["alice"]
alias_or_role_evidence: 
unknowns: []
source_refs: []

[[SECTION character_index_markdown]]
[[SECTION markdown]]
# White Rabbit
**Role:** Catalyst / Recurring Character

**Status:** Physically Present

**Physical Description:**
- A white rabbit.
- Features pink eyes.

**Costume & Silhouette:**
- Wears a waistcoat (implied by the presence of a waistcoat-pocket).
- Carries/uses a watch.

**Descriptive Noun Phrases:**
- White rabbit with pink eyes
- Rabbit in a waistcoat
- Hurrying rabbit

**Uncertainty Notes:**
- None; visual markers are specific.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
