# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-28T04:04:42.023727+00:00
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

Chapter id: CH004

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

**Setting: The White Rabbit's House**
*   **Location:** A neat little house with a brass plate reading "W. RABBIT."
*   **Interior Subzones:** 
    *   A tidy upstairs room containing a table by a window, a looking-glass, and a small bottle (no label).
    *   A chimney/fireplace.
    *   The doorway (blocked by Alice's size).

**Characters & Entrances/Exits**
*   **Alice:** Enters the house via the front door; exits via the door after shrinking; later enters a thick wood.
*   **White Rabbit:** Enters the house area, attempts to enter the room through the door (fails), then attempts the window.
*   **Pat:** A worker/animal outside the house; interacts with the Rabbit and Bill.
*   **Bill (a Lizard):** Appears via the chimney (after being kicked); later seen outside being held by guinea-pigs.
*   **The Crowd:** A group of small animals/birds waiting outside the house.
*   **Enormous Puppy:** Encountered by Alice in the woods; interacts with her via a stick.
*   **Blue Caterpillar:** Revealed at the end, sitting atop a large mushroom in the woods.

**Key Events & Physical Transitions**
*   **The Search:** The White Rabbit searches for lost gloves and a fan; mistakes Alice for his housemaid "Mary Ann."
*   **The Growth Spurt:** Alice finds an unlabeled bottle in the Rabbit's room, drinks it, and grows so large her head presses against the ceiling. She eventually occupies the entire room, with one arm out the window and one foot up the chimney.
*   **The Window Confrontation:** The Rabbit attempts to enter through the window; Alice reaches out a hand to snatch at him, causing a crash in what is assumed to be a cucumber-frame.
*   **The Chimney Incident:** A group of animals attempts to use ladders and ropes to reach the house/chimney. They decide Bill must go down the chimney. Alice, positioned in the chimney, delivers a sharp kick to the scrambling animal (Bill).
*   **The Siege:** The Rabbit orders a "barrowful" of pebbles to be thrown at the house. The pebbles hit Alice through the window and transform into small cakes on the floor.
*   **The Shrinking:** Alice eats one of the cake-pebbles, shrinks to a manageable size, and escapes the house.
*   **The Woods Encounter:** Alice wanders into a thick wood. She is nearly trampled by an enormous puppy but manages to distract it with a stick.
*   **The Discovery:** While resting against a buttercup, Alice discovers a large mushroom. Peering over the edge, she reveals the Blue Caterpillar smoking a hookah.

**Objects & Visual Continuity**
*   **White Kid Gloves & Fan:** The objects the Rabbit is searching for.
*   **Unlabeled Bottle:** Causes rapid growth.
*   **Pebbles/Cakes:** Small stones that transform into edible cakes upon landing.
*   **Stick:** Used by Alice to play with the puppy.
*   **Hookah:** Being used by the Caterpillar.
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
scale_hint: unknown
renderability_hint: renderable
confidence: 1.0
direct_identity_evidence: "Alice is explicitly named and acts as the protagonist."
direct_visual_evidence: "She undergoes extreme size changes (growing to fill a room, shrinking to escape)."
costume_or_covering_evidence: ""
movement_evidence: "Enters house, grows, shrinks, walks into woods, interacts with puppy/caterpillar."
associated_entities: ["white_rabbit", "bill_the_lizard", "enormous_puppy", "blue_caterpillar"]
alias_or_role_evidence: ""
unknowns: []
source_refs: []
[[SECTION character_index_markdown]]
[[SECTION markdown]]
# Alice
**Role:** Protagonist

**Status:** Physically Present

**Physical Description:**
A young girl capable of rapid, extreme size fluctuations. At one point, she grows large enough to fill a room, with her head pressing against the ceiling and limbs occupying windows and chimneys. She later shrinks to a manageable human scale.

**Costume & Silhouette:**
No specific clothing details are provided in this chapter, though her silhouette changes drastically due to her size transformations.

**Descriptive Noun Phrases:**
- Young girl
- Giantess (temporary)
- Shrinking child
- Wanderer in the woods

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
asset_id: white_rabbit
canonical_character_id: white_rabbit
aliases: ["W. RABBIT"]
is_fully_identified: true
manual_description_required: false
manual_description_reason: ""
clarification_required: false
clarification_reason: ""
clarification_question: ""
character_type_hint: animal
morphology_hint: quadruped
scale_hint: small
renderability_hint: renderable
confidence: 1.0
direct_identity_evidence: "Identified by the brass plate 'W. RABBIT' and referred to as White Rabbit."
direct_visual_evidence: "White fur/coloration implied by name; small scale relative to a house."
costume_or_covering_evidence: ""
movement_evidence: "Attempts to enter through doors and windows; searches for items."
associated_entities: ["alice", "pat"]
alias_or_role_evidence: "Mistakes Alice for his housemaid Mary Ann."
unknowns: []
source_refs: []
[[SECTION character_index_markdown]]
[[SECTION markdown]]
# White Rabbit
**Role:** Supporting Character / Catalyst

**Status:** Physically Present

**Physical Description:**
A small rabbit, presumably white in color. He is frantic and preoccupied with finding his lost gloves and fan.

**Costume & Silhouette:**
Small animal silhouette; owner of a house with a brass nameplate.

**Descriptive Noun Phrases:**
- White rabbit
- Frantic rabbit
- House owner

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
asset_id: bill_the_lizard
canonical_character_id: bill_the_lizard
aliases: ["Bill"]
is_fully_identified: true
manual_description_required: false
manual_description_reason: ""
clarification_required: false
clarification_reason: ""
clarification_question: ""
character_type_hint: animal
morphology_hint: quadruped
scale_hint: small
renderability_hint: renderable
confidence: 0.9
direct_identity_evidence: "Identified as Bill (a Lizard)."
direct_visual_evidence: "A lizard that can be kicked down a chimney and held by guinea-pigs."
costume_or_covering_evidence: ""
movement_evidence: "Scrambles down a chimney; held by other animals."
associated_entities: ["white_rabbit", "the_crowd"]
alias_or_role_evidence: ""
unknowns: []
source_refs: []
[[SECTION character_index_markdown]]
[[SECTION markdown]]
# Bill (a Lizard)
**Role:** Minor Character

**Status:** Physically Present

**Physical Description:**
A lizard.

**Costume & Silhouette:**
Small reptilian silhouette.

**Descriptive Noun Phrases:**
- Scrambling lizard
- Chimney-climbing lizard

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
asset_id: pat
canonical_character_id: pat
aliases: []
is_fully_identified: true
manual_description_required: true
manual_description_reason: "Only identified as a 'worker/animal' with no visual description of species or appearance."
clarification_required: false
clarification_reason: ""
clarification_question: ""
character_type_hint: animal
morphology_hint: unknown
scale_hint: small
renderability_hint: renderable
confidence: 0.5
direct_identity_evidence: "Named Pat."
direct_visual_evidence: ""
costume_or_covering_evidence: ""
movement_evidence: "Interacts with Rabbit and Bill outside the house."
associated_entities: ["white_rabbit", "bill_the_lizard"]
alias_or_role_evidence: "Described as a worker/animal."
unknowns: ["Species", "Appearance"]
source_refs: []
[[SECTION character_index_markdown]]
[[SECTION markdown]]
# Pat
**Role:** Minor Character

**Status:** Physically Present

**Physical Description:**
Unknown. The text identifies Pat as a worker or animal outside the White Rabbit's house, but provides no physical details.

**Costume & Silhouette:**
Unknown.

**Descriptive Noun Phrases:**
- Worker animal
- Outside observer

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
asset_id: the_crowd
canonical_character_id: the_crowd
aliases: []
is_fully_identified: true
manual_description_required: true
manual_description_reason: "Described only as a group of small animals/birds; specific species or appearance not detailed."
clarification_required: false
clarification_reason: ""
clarification_question: ""
character_type_hint: group
morphology_hint: unknown
scale_hint: small
renderability_hint: renderable
confidence: 0.7
direct_identity_evidence: "Referred to as 'The Crowd'."
direct_visual_evidence: "A group of small animals/birds waiting outside the house."
costume_or_covering_evidence: ""
movement_evidence: "Waiting outside the house; using ladders and ropes."
associated_entities: ["white_rabbit", "bill_the_lizard"]
alias_or_role_evidence: ""
unknowns: ["Specific species composition"]
source_refs: []
[[SECTION character_index_markdown]]
[[SECTION markdown]]
# The Crowd
**Role:** Background Group

**Status:** Physically Present

**Physical Description:**
A collection of various small animals and birds.

**Costume & Silhouette:**
A heterogeneous group of small animal silhouettes.

**Descriptive Noun Phrases:**
- Small animal crowd
- Gathering of birds and creatures

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
asset_id: enormous_puppy
canonical_character_id: enormous_puppy
aliases: []
is_fully_identified: true
manual_description_required: false
manual_description_reason: ""
clarification_required: false
clarification_reason: ""
clarification_question: ""
character_type_hint: animal
morphology_hint: quadruped
scale_hint: large
renderability_hint: renderable
confidence: 1.0
direct_identity_evidence: "Identified as an 'Enormous Puppy'."
direct_visual_evidence: "Described as enormous; interacts with Alice via a stick."
costume_or_covering_evidence: ""
movement_evidence: "Nearly tramples Alice in the woods."
associated_entities: ["alice"]
alias_or_role_evidence: ""
unknowns: []
source_refs: []
[[SECTION character_index_markdown]]
[[SECTION markdown]]
# Enormous Puppy
**Role:** Minor Character / Obstacle

**Status:** Physically Present

**Physical Description:**
A puppy of disproportionately large size.

**Costume & Silhouette:**
Large canine silhouette.

**Descriptive Noun Phrases:**
- Giant puppy
- Large woodland dog

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
asset_id: blue_caterpillar
canonical_character_id: blue_caterpillar
aliases: []
is_fully_identified: true
manual_description_required: false
manual_description_reason: ""
clarification_required: false
clarification_reason: ""
clarification_question: ""
character_type_hint: creature
morphology_hint: unknown
scale_hint: small
renderability_hint: renderable
confidence: 1.0
direct_identity_evidence: "Identified as the Blue Caterpillar."
direct_visual_evidence: "Blue in color; sitting atop a large mushroom; smoking a hookah."
costume_or_covering_evidence: ""
movement_evidence: "Sitting atop a mushroom."
associated_entities: ["alice"]
alias_or_role_evidence: ""
unknowns: []
source_refs: []
[[SECTION character_index_markdown]]
[[SECTION markdown]]
# Blue Caterpillar
**Role:** Supporting Character

**Status:** Physically Present (at end of chapter)

**Physical Description:**
A blue-colored caterpillar.

**Costume & Silhouette:**
Small caterpillar silhouette; seen using a hookah.

**Descriptive Noun Phrases:**
- Blue caterpillar
- Hookah-smoking caterpillar

[[/SECTION]]
[[/FILMCREATOR_RECORD]]
[[/FILMCREATOR_PACKET]]
````
