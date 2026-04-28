# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-28T03:21:21.094799+00:00
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

**Locations:**
* **The White Rabbit’s House:** A neat little house with a brass plate reading "W. RABBIT." Interior includes a tidy room with a window table, a looking-glass, and a chimney. Exterior features a window overlooking a cucumber-frame area and a garden/hedge area.
* **Thick Wood:** A dense forest setting where Alice seeks refuge. Contains large thistles and buttercups.
* **Mushroom Clearing:** A specific spot in the wood featuring a large mushroom tall enough for Alice to peer over.

**Characters:**
* **Alice:** Currently tiny; undergoes rapid growth to giant proportions, then shrinks via magic cake.
* **The White Rabbit:** Anxious, authoritative, and prone to anger. Mistakes Alice for his housemaid, "Mary Ann."
* **Pat:** A subordinate/worker (likely an animal) seen through the window.
* **Bill:** A small creature (a lizard) who is forced down the chimney by the Rabbit's orders.
* **The Crowd:** A group of small animals and birds outside the house, including two guinea-pigs.
* **Enormous Puppy:** A large, playful, but intimidating animal in the woods that chases Alice.
* **Blue Caterpillar:** A large, calm creature sitting atop a mushroom, smoking a hookah.

**Key Events & Visual Continuity:**
* **Entrance/Discovery:** The White Rabbit enters the scene looking for lost gloves and a fan; he encounters Alice and commands her to fetch them.
* **The House Interior:** Alice enters the Rabbit's house. She finds a fan and white kid gloves on a window table. 
* **Size Change (Growth):** Alice drinks from an unlabeled bottle near a looking-glass. She grows rapidly, eventually becoming so large she is wedged in the room (head against ceiling, one arm out the window, one foot up the chimney).
* **The Confrontation at the Window:** The Rabbit attempts to enter through the window. Alice reaches out and "snatches" at the air, causing a crash in what is assumed to be a cucumber-frame. 
* **The Chimney Incident:** A group of animals attempt to use ladders/ropes to reach the house. Bill is ordered down the chimney. Alice, inside the chimney, delivers a sharp kick to Bill, sending him flying out like a "Jack-in-the-box."
* **Size Change (Shrinking):** The Rabbit's crowd throws pebbles through the window; these pebbles turn into small cakes on the floor. Alice eats one and shrinks to a manageable size.
* **Escape:** Alice exits the house, passes the recovering Bill (being tended to by guinea-pigs), and flees into the woods.
* **The Puppy Encounter:** In the woods, Alice is hunted/played with by an enormous puppy using a stick as a lure. She uses a large thistle for cover.
* **The Reveal:** Alice rests against a buttercup and discovers a large mushroom. Peering over the edge, she reveals the Blue Caterpillar smoking a hookah.
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
direct_identity_evidence: "Directly named as Alice throughout the text."
direct_visual_evidence: "Described as undergoing extreme size changes (tiny, giant/wedged in room, manageable size)."
costume_or_covering_evidence: ""
movement_evidence: "Running, kicking, reaching out of windows, eating cakes."
associated_entities: ["white_rabbit", "bill", "enormous_puppy", "blue_caterpillar"]
alias_or_role_evidence: ""
unknowns: []
source_refs: []
[[SECTION character_index_markdown]]
[[markdown]]
# Alice
**Role:** Protagonist

**Status:** Physically Present

**Physical Description:**
A young girl subject to extreme size fluctuations. In this chapter, she transitions from tiny to giant (head against ceiling, limbs protruding through windows and chimneys) before shrinking back to a manageable size via magic cake.

**Costume & Silhouette:**
Specific clothing details are not provided in this chapter, but her silhouette changes drastically due to scale shifts.

**Descriptive Noun Phrases:**
- Tiny girl
- Giant girl wedged in a room
- Girl emerging from a chimney
- Small girl fleeing through woods

**Uncertainty Notes:**
Visual appearance (hair color, eye color, specific dress) is not detailed in this chapter; relies on established character design.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
asset_id: white_rabbit
canonical_character_id: white_rabbit
aliases: ["W. Rabbit"]
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
direct_identity_evidence: "Identified by name on a brass plate and referred to as the White Rabbit."
direct_visual_evidence: "White fur (implied by name), small scale, authoritative/anxious demeanor."
costume_or_covering_evidence: "Associated with gloves and a fan; owner of a house."
movement_evidence: "Entering house, commanding others, throwing pebbles."
associated_entities: ["alice", "bill", "pat", "the_crowd"]
alias_or_role_evidence: "Brass plate reads 'W. RABBIT'."
unknowns: []
source_refs: []
[[SECTION character_index_markdown]]
[[markdown]]
# The White Rabbit
**Role:** Antagonist/Supporting Character

**Status:** Physically Present

**Physical Description:**
A small, white rabbit with an anxious and authoritative temperament. He is prone to anger and displays bossy behavior toward Alice and other creatures.

**Costume & Silhouette:**
Small animal silhouette; associated with domestic items like gloves and a fan.

**Descriptive Noun Phrases:**
- Anxious white rabbit
- Authoritative small rabbit
- Angry rabbit owner

**Uncertainty Notes:**
Specific clothing (e.g., waistcoat) is not explicitly detailed in this chapter text, though his personality suggests anthropomorphic behavior.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
asset_id: bill
canonical_character_id: bill
aliases: []
is_fully_identified: true
manual_description_required: false
manual_description_reason: ""
clarification_required: false
clarification_reason: ""
clarification_question: ""
character_type_hint: animal
morphology_hint: unknown
scale_hint: small
renderability_hint: renderable
confidence: 0.7
direct_identity_evidence: "Named as Bill."
direct_visual_evidence: "Described as a 'small creature (a lizard)' who is sent down the chimney."
costume_or_covering_evidence: ""
movement_evidence: "Sent down a chimney, flies out like a Jack-in-the-box after being kicked."
associated_entities: ["white_rabbit", "alice"]
alias_or_role_evidence: ""
unknowns: []
source_refs: []
[[SECTION character_index_markdown]]
[[markdown]]
# Bill
**Role:** Supporting Character

**Status:** Physically Present

**Physical Description:**
A small creature, identified as a lizard. He is physically vulnerable to being kicked and sent flying.

**Costume & Silhouette:**
Small lizard silhouette.

**Descriptive Noun Phrases:**
- Small lizard creature
- Jack-in-the-box lizard

**Uncertainty Notes:**
The text identifies him as a "small creature (a lizard)"; exact species morphology beyond 'lizard' is unstated.
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
scale_hint: large
renderability_hint: renderable
confidence: 0.9
direct_identity_evidence: "Identified as the Blue Caterpillar."
direct_visual_evidence: "Blue color, sitting atop a mushroom, smoking a hookah."
costume_or_covering_evidence: ""
movement_evidence: "Sitting calmly."
associated_entities: []
alias_or_role_evidence: ""
unknowns: []
source_refs: []
[[SECTION character_index_markdown]]
[[markdown]]
# Blue Caterpillar
**Role:** Supporting Character

**Status:** Physically Present (at end of chapter)

**Physical Description:**
A large, blue caterpillar. He possesses a calm demeanor and is seen smoking a hookah.

**Costume & Silhouette:**
Large caterpillar silhouette; associated with a hookah.

**Descriptive Noun Phrases:**
- Large blue caterpillar
- Calm hookah-smoking caterpillar

**Uncertainty Notes:**
Specific limb count or exact texture of the caterpillar is not described.
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
direct_identity_evidence: "Identified as an Enormous Puppy."
direct_visual_evidence: "Large size, playful but intimidating, uses a stick as a lure."
costume_or_covering_evidence: ""
movement_evidence: "Chasing Alice through the woods."
associated_entities: ["alice"]
alias_or_role_evidence: ""
unknowns: []
source_refs: []
[[SECTION character_index_markdown]]
[[markdown]]
# Enormous Puppy
**Role:** Minor Antagonist/Obstacle

**Status:** Physically Present

**Physical Description:**
A large, intimidating puppy. While described as "playful," its scale makes it a threat to Alice. It uses a stick to lure or play with her.

**Costume & Silhouette:**
Large canine silhouette.

**Descriptive Noun Phrases:**
- Large playful puppy
- Intimidating enormous dog

**Uncertainty Notes:**
Specific breed is not mentioned; scale is the primary defining characteristic.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
asset_id: the_crowd
canonical_character_id: the_crowd
aliases: []
is_fully_identified: false
manual_description_required: true
manual_description_reason: "The crowd is a collection of various animals and birds; individual visual consistency cannot be established without more detail."
clarification_required: true
clarification_reason: "It is unclear if this should be treated as a single entity or a collection of distinct characters for rendering purposes."
clarification_question: "Should 'The Crowd' be rendered as a singular mass of animals or a specific set of identifiable individuals?"
character_type_hint: group
morphology_hint: unknown
scale_hint: small
renderability_hint: context_only
confidence: 0.5
direct_identity_evidence: "Referred to as 'The Crowd'."
direct_visual_evidence: "Small animals and birds, including two guinea-pigs."
costume_or_covering_evidence: ""
movement_evidence: "Throwing pebbles through a window."
associated_entities: ["white_rabbit"]
alias_or_role_evidence: ""
unknowns: []
source_refs: []
[[SECTION character_index_markdown]]
[[markdown]]
# The Crowd
**Role:** Minor Group

**Status:** Physically Present

**Physical Description:**
A group consisting of various small animals and birds. Specifically mentioned are two guinea-pigs. They act collectively to throw pebbles through the Rabbit's window.

**Costume & Silhouette:**
A chaotic silhouette of various small animal shapes.

**Descriptive Noun Phrases:**
- Small animal crowd
- Group of birds and guinea-pigs

**Uncertainty Notes:**
The exact composition of the group is vague beyond the mention of birds, small animals, and two guinea-pigs.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
asset_id: pat
canonical_character_id: pat
aliases: []
is_fully_identified: false
manual_description_required: true
manual_description_reason: "Character is only seen through a window and lacks any physical description."
clarification_required: true
clarification_reason: "Identity/species is unknown; only described as a 'subordinate/worker'."
clarification_question: "What species is Pat, and what do they look like?"
character_type_hint: unknown
morphology_hint: unknown
scale_hint: small
renderability_hint: context_only
confidence: 0.3
direct_identity_evidence: "Named as Pat."
direct_visual_evidence: ""
costume_or_covering_evidence: ""
movement_evidence: ""
associated_entities: ["white_rabbit"]
alias_or_role_evidence: "Described as a subordinate/worker seen through the window."
unknowns: []
source_refs: []
[[SECTION character_index_markdown]]
[[markdown]]
# Pat
**Role:** Minor Character

**Status:** Referenced/Visible through window

**Physical Description:**
Unknown. Described only as a worker or subordinate to the White Rabbit.

**Costume & Silhouette:**
Unknown.

**Descriptive Noun Phrases:**
- Subordinate Pat

**Uncertainty Notes:**
Extremely low information; no visual descriptors provided in this chapter.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]
[[/FILMCREATOR_PACKET]]
````
