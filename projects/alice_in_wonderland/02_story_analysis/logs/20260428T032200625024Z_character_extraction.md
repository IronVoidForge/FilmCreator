# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-28T03:22:00.625024+00:00
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
direct_identity_evidence: "Alice is the protagonist and central figure throughout the chapter."
direct_visual_evidence: "Described as undergoing rapid growth to giant proportions (head against ceiling, arm out window) and shrinking via magic cake."
costume_or_covering_evidence: ""
movement_evidence: "Grows rapidly, shrinks, kicks Bill down a chimney, flees into the woods, hides behind a thistle."
associated_entities: ["white_rabbit", "bill", "enormous_puppy", "blue_caterpillar"]
alias_or_role_evidence: ""
unknowns: []
source_refs: []
[[SECTION character_index_markdown]]
[[SECTION markdown]]
# Alice
**Role:** Protagonist

**Status:** Physically Present

**Physical Description:**
Alice's size is highly unstable in this chapter. She begins as a tiny figure, grows to a giant scale where her head touches the ceiling and limbs extend through windows/chimneys, and eventually shrinks back down after eating a pebble-cake. 

**Costume & Silhouette:**
No specific clothing details are provided in this chapter text, though she is a human girl.

**Descriptive Noun Phrases:**
* Tiny girl
* Giant Alice (wedged in room)
* Shrinking Alice

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
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
confidence: 0.9
direct_identity_evidence: "Identified by the brass plate 'W. RABBIT' on his house and referred to as The White Rabbit."
direct_visual_evidence: "Anxious, authoritative, prone to anger; owns a house with a window table, looking-glass, and chimney."
costume_or_covering_evidence: ""
movement_evidence: "Enters the scene looking for gloves/fan; commands Alice; attempts to enter through a window."
associated_entities: ["alice", "bill", "pat"]
alias_or_role_evidence: "Mistakes Alice for his housemaid, Mary Ann."
unknowns: []
source_refs: []
[[SECTION character_index_markdown]]
[[SECTION markdown]]
# The White Rabbit
**Role:** Antagonist/Authority Figure

**Status:** Physically Present

**Physical Description:**
An anxious and authoritative rabbit. He is prone to anger and displays a sense of ownership over his tidy house.

**Costume & Silhouette:**
Not explicitly described, but he possesses white kid gloves and a fan.

**Descriptive Noun Phrases:**
* Anxious White Rabbit
* Authoritative Rabbit
* W. Rabbit (via brass plate)

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: bill
canonical_character_id: bill
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
confidence: 0.7
direct_identity_evidence: "Named as Bill during the chimney incident."
direct_visual_evidence: "A small creature (identified in summary as a lizard) who is sent down a chimney and kicked out like a 'Jack-in-the-box'."
costume_or_covering_evidence: ""
movement_evidence: "Forced down a chimney; flies out of the chimney after being kicked."
associated_entities: ["white_rabbit", "alice"]
alias_or_role_evidence: ""
unknowns: ["Exact morphology is described as a lizard in summary, but text implies a small creature."]
source_refs: []
[[SECTION character_index_markdown]]
[[SECTION markdown]]
# Bill
**Role:** Subordinate/Victim

**Status:** Physically Present

**Physical Description:**
A small creature (likely a lizard). He is small enough to be sent down a chimney.

**Costume & Silhouette:**
Not described.

**Descriptive Noun Phrases:**
* Small lizard-like creature
* Jack-in-the-box Bill

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
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
direct_visual_evidence: "A large, calm creature sitting atop a mushroom, smoking a hookah."
costume_or_covering_evidence: ""
movement_evidence: "Sitting calmly on a mushroom."
associated_entities: []
alias_or_role_evidence: ""
unknowns: ["Exact morphology (legs/segments) is not detailed."]
source_refs: []
[[SECTION character_index_markdown]]
[[SECTION markdown]]
# Blue Caterpillar
**Role:** Mysterious Figure

**Status:** Physically Present (Revealed at end)

**Physical Description:**
A large, calm blue creature. 

**Costume & Silhouette:**
Seen smoking a hookah while perched on a mushroom.

**Descriptive Noun Phrases:**
* Large Blue Caterpillar
* Hookah-smoking caterpillar

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
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
confidence: 0.9
direct_identity_evidence: "Identified as an Enormous Puppy."
direct_visual_evidence: "A large, playful but intimidating animal that chases Alice in the woods using a stick as a lure."
costume_or_covering_evidence: ""
movement_evidence: "Chases Alice through the woods; uses a stick to play/lure her."
associated_entities: ["alice"]
alias_or_role_evidence: ""
unknowns: []
source_refs: []
[[SECTION character_index_markdown]]
[[SECTION markdown]]
# Enormous Puppy
**Role:** Pursuer

**Status:** Physically Present

**Physical Description:**
A large, intimidating puppy. 

**Costume & Silhouette:**
Not described.

**Descriptive Noun Phrases:**
* Large playful puppy
* Intimidating enormous dog

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: the_crowd
canonical_character_id: the_crowd
aliases: ["the crowd"]
is_fully_identified: false
manual_description_required: true
manual_description_reason: "The group is a collection of various small animals and birds; individual visual traits are not specified beyond 'two guinea-pigs'."
clarification_required: true
clarification_question: "Should the crowd be rendered as a single mass or as distinct, identifiable animal characters?"
character_type_hint: group
morphology_hint: unknown
scale_hint: small
renderability_hint: context_only
confidence: 0.5
direct_identity_evidence: "Referred to as 'The Crowd' outside the house."
direct_visual_evidence: "A group of small animals and birds; includes two guinea-pigs."
costume_or_covering_evidence: ""
movement_evidence: "Throws pebbles through the window."
associated_entities: ["white_rabbit"]
alias_or_role_evidence: ""
unknowns: ["Specific species of most members", "exact number of individuals"]
source_refs: []
[[SECTION character_index_markdown]]
[[SECTION markdown]]
# The Crowd
**Role:** Collective Obstacle/Participants

**Status:** Physically Present

**Physical Description:**
A collection of various small animals and birds. Two guinea-pigs are explicitly mentioned as being part of the group or tending to Bill.

**Costume & Silhouette:**
N/A

**Descriptive Noun Phrases:**
* Small animal crowd
* Group of birds and guinea-pigs

**Uncertainty Note:**
The exact composition of this group is vague; it functions more as a collective entity than a set of distinct characters.

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: pat
canonical_character_id: pat
aliases: []
is_fully_identified: false
manual_description_required: true
manual_description_reason: "Only mentioned as a subordinate/worker seen through a window; no physical description provided."
clarification_required: true
clarification_question: "Is Pat a specific animal character or just a background worker?"
character_type_hint: unknown
morphology_hint: unknown
scale_hint: small
renderability_hint: context_only
confidence: 0.3
direct_identity_evidence: "Named as Pat."
direct_visual_evidence: "Seen through the window of the White Rabbit's house."
costume_or_covering_evidence: ""
movement_evidence: ""
associated_entities: ["white_rabbit"]
alias_or_role_evidence: "Subordinate/worker."
unknowns: ["Species", "Appearance"]
source_refs: []
[[SECTION character_index_markdown]]
[[SECTION markdown]]
# Pat
**Role:** Subordinate

**Status:** Referenced/Visible through window

**Physical Description:**
Unknown. Described only as a subordinate or worker seen through the window of the Rabbit's house.

**Costume & Silhouette:**
Unknown.

**Descriptive Noun Phrases:**
* Worker Pat (unidentified)

**Uncertainty Note:**
Extremely low visual information available.

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
