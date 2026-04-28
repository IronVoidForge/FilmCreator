# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-28T03:07:10.641650+00:00
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

**Location: The White Rabbit's House (Interior)**
*   **Event:** The White Rabbit enters the scene, frantic and muttering about "The Duchess" and lost items (fan and white kid gloves). 
*   **Character Entrance/Interaction:** The Rabbit mistakes Alice for his housemaid, "Mary Ann," and commands her to fetch the items. Alice, frightened, complies and runs toward the Rabbit's residence.
*   **Location Shift:** Alice enters a neat little house with a brass plate reading "W. RABBIT." She moves upstairs to a tidy room containing a table by a window.
*   **Object Interaction:** On the table, Alice finds a fan and several pairs of tiny white kid gloves. Nearby, she discovers an unlabeled bottle.
*   **Transformation 1 (Growth):** Alice drinks from the bottle. She rapidly grows until her head presses against the ceiling. She continues to grow until she is forced into an uncomfortable position: kneeling, then lying down with one elbow against the door and one arm curled around her head, eventually placing one arm out the window and one foot up the chimney.
*   **External Conflict (The Siege):** The White Rabbit arrives at the door. Because Alice's elbow blocks it, he attempts to enter through the window. 
*   **Action/Interaction:** Alice reaches out a hand and makes a "snatch" in the air near the window. This results in a shriek and the sound of breaking glass (a cucumber-frame).
*   **Character Reveal/Dialogue:** A new character, Pat (an animal), is introduced via dialogue. The Rabbit and Pat discuss the "arm" filling the window. 
*   **Action/Interaction:** Alice makes a second "snatch" in the air, causing more shrieks and broken glass.
*   **The Siege Escalates:** A crowd of small animals arrives with ladders and ropes. They attempt to reach the window/roof. There is a loud crash involving a loose slate.
*   **Action/Interaction (The Kick):** The Rabbit orders "Bill" to go down the chimney. Alice, positioned in the chimney, delivers a sharp kick to the scrambling creature above her.
*   **Result:** Bill is ejected from the chimney. A chorus of voices reacts to his "sky-rocket" exit.
*   **Conflict Escalation:** The Rabbit threatens to burn the house down. Alice shouts back a threat involving her cat, Dinah.
*   **Object Interaction/Transformation 2 (Shrinking):** The Rabbit begins throwing pebbles through the window. As they hit the floor, the pebbles transform into little cakes. Alice eats one cake and rapidly shrinks.
*   **Exit:** Once small enough, Alice exits through the door.

**Location: Outside / Thick Wood**
*   **Character Interaction/Visual State:** Alice emerges to find a crowd of animals. She sees Bill (a lizard) being held up by two guinea-pigs. Fearing the crowd, Alice flees into a thick wood.
*   **Character Entrance/Interaction:** An enormous puppy appears, looking down at Alice. 
*   **Action/Interaction:** Alice uses a stick to play with the puppy to distract it. The puppy performs "charges" and tumbles over itself. Alice uses this distraction to escape into the woods.
*   **Location Shift:** Alice rests against a large buttercup. She observes her surroundings looking for something to eat or drink to restore her size.
*   **Character Reveal/Visual Discovery:** Alice finds a large mushroom. She climbs onto tiptoe and peeks over the edge of the cap.
*   **Reveal:** On top of the mushroom, she discovers a large blue caterpillar sitting with arms folded, smoking a long hookah.
````

## Raw Response
````text
[[FILMCREATOR_PACKET]]
[[SECTION character_index_markdown]]
# Character Index - Chapter 4

- [Alice](#alice)
- [White Rabbit](#white_rabbit)
- [Mary Ann](#mary_ann)
- [The Duchess](#the_duchess)
- [Pat](#pat)
- [Bill](#bill)
- [Dinah](#dinah)
- [Guinea-pigs](#guinea_pigs)
- [Puppy](#puppy)
- [Blue Caterpillar](#blue_caterpillar)

[[/SECTION]]

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
direct_identity_evidence: "Directly named as Alice throughout the text."
direct_visual_evidence: "Described growing to press against a ceiling and shrinking after eating a cake; interacts with objects like fans, gloves, and mushrooms."
costume_or_covering_evidence: ""
movement_evidence: "Runs, climbs on tiptoe, kicks Bill, flees into woods, plays with a puppy using a stick."
associated_entities: ["white_rabbit", "bill", "dinah", "puppy", "blue_caterpillar"]
alias_or_role_evidence: ""
unknowns: []
source_refs: []
[[SECTION markdown]]
# Alice
**Role:** Protagonist

**Status:** Physically Present

**Physical Description:**
A young girl whose size fluctuates dramatically throughout the chapter. She grows large enough to fill a room (head against ceiling, arm out window, foot in chimney) and later shrinks after eating a cake.

**Costume & Silhouette:**
Not explicitly detailed in this chapter, though her silhouette changes from human-scale to giant-scale to tiny-scale.

**Descriptive Noun Phrases:**
- Growing girl
- Shrinking child
- Girl in a white rabbit's house
- Small girl fleeing animals

**Uncertainty Notes:**
Specific clothing details are not provided in this chapter text.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
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
confidence: 0.9
direct_identity_evidence: "Named as White Rabbit and identified by the brass plate 'W. RABBIT'."
direct_visual_evidence: "Described as frantic, muttering, and throwing pebbles."
costume_or_covering_evidence: ""
movement_evidence: "Enters frantically, attempts to enter a window, throws pebbles."
associated_entities: ["alice", "pat", "bill"]
alias_or_role_evidence: "Brass plate reads 'W. RABBIT'."
unknowns: []
source_refs: []
[[SECTION markdown]]
# White Rabbit
**Role:** Antagonist/Instigator

**Status:** Physically Present

**Physical Description:**
A rabbit, likely small in scale relative to a human house. He is characterized by his frantic and muttering behavior.

**Costume & Silhouette:**
Not explicitly described, but he acts with the agency of a character (muttering about lost items).

**Descriptive Noun Phrases:**
- Frantic white rabbit
- Muttering rabbit
- Rabbit in a waistcoat (implied by behavior/setting)

**Uncertainty Notes:**
Specific visual details like eye color or exact fur texture are absent.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: mary_ann
canonical_character_id: mary_ann
aliases: []
is_fully_identified: false
manual_description_required: true
manual_description_reason: "Character is only mentioned as a name the Rabbit uses to mistake Alice for someone else; no physical description exists."
clarification_required: true
clarification_reason: "Is Mary Ann a distinct character or just a mistaken identity for Alice?"
clarification_question: "Does Mary Ann have a unique visual design, or is she purely a narrative device for the Rabbit's mistake?"
character_type_hint: human
morphology_hint: biped
scale_hint: human_scale
renderability_hint: context_only
confidence: 0.5
direct_identity_evidence: ""
direct_visual_evidence: ""
costume_or_covering_evidence: ""
movement_evidence: ""
associated_entities: ["white_rabbit"]
alias_or_role_evidence: "The Rabbit mistakes Alice for his housemaid, Mary Ann."
unknowns: ["physical appearance", "actual existence"]
source_refs: []
[[SECTION markdown]]
# Mary Ann
**Role:** Referenced (Mistaken Identity)

**Status:** Referenced

**Physical Description:**
No physical description provided. She is the name the White Rabbit uses when addressing Alice.

**Costume & Silhouette:**
Unknown.

**Descriptive Noun Phrases:**
- The housemaid
- Mistaken identity

**Uncertainty Notes:**
It is unclear if Mary Ann is a real person in this world or simply a name the Rabbit calls Alice.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: the_duchess
canonical_character_id: the_duchess
aliases: []
is_fully_identified: false
manual_description_required: true
manual_description_reason: "Character is only mentioned in dialogue; no physical description provided."
clarification_required: true
clarification_reason: "Is she a human, animal, or something else?"
clarification_question: "What is the Duchess's species and appearance?"
character_type_hint: unknown
morphology_hint: unknown
scale_hint: unknown
renderability_hint: context_only
confidence: 0.1
direct_identity_evidence: ""
direct_visual_evidence: ""
costume_or_covering_evidence: ""
movement_evidence: ""
associated_entities: ["white_rabbit"]
alias_or_role_evidence: "Mentioned by the White Rabbit."
unknowns: ["species", "appearance", "scale"]
source_refs: []
[[SECTION markdown]]
# The Duchess
**Role:** Referenced

**Status:** Referenced

**Physical Description:**
No physical description provided.

**Costume & Silhouette:**
Unknown.

**Descriptive Noun Phrases:**
- The Duchess (referenced)

**Uncertainty Notes:**
Extremely low information; character exists only as a name in the Rabbit's mutterings.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: pat
canonical_character_id: pat
aliases: []
is_fully_identified: false
manual_description_required: true
manual_description_reason: "Character is introduced via dialogue but lacks any physical description."
clarification_required: true
clarification_reason: "What kind of animal is Pat?"
clarification_question: "What is Pat's species and appearance?"
character_type_hint: animal
morphology_hint: unknown
scale_hint: unknown
renderability_hint: context_only
confidence: 0.3
direct_identity_evidence: ""
direct_visual_evidence: ""
costume_or_covering_evidence: ""
movement_evidence: ""
associated_entities: ["white_rabbit"]
alias_or_role_evidence: "Discusses the 'arm' in the window with the Rabbit."
unknowns: ["species", "appearance", "scale"]
source_refs: []
[[SECTION markdown]]
# Pat
**Role:** Supporting Character

**Status:** Physically Present (Auditory/Dialogue)

**Physical Description:**
No physical description provided.

**Costume & Silhouette:**
Unknown.

**Descriptive Noun Phrases:**
- Pat the animal

**Uncertainty Notes:**
The text identifies Pat as an "animal" but provides no visual details for rendering.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: bill
canonical_character_id: bill
aliases: []
is_fully_identified: true
manual_description_required: true
manual_description_reason: "While identified as a lizard, specific visual details (color, size, pattern) are missing."
clarification_required: false
clarification_reason: ""
clarification_question: ""
character_type_hint: animal
morphology_hint: quadruped
scale_hint: small
renderability_hint: renderable
confidence: 0.7
direct_identity_evidence: "Identified as 'Bill (a lizard)' in the summary."
direct_visual_evidence: "Scrambles down a chimney, is ejected like a sky-rocket, held up by guinea-pigs."
costume_or_covering_evidence: ""
movement_evidence: "Scrambling, being ejected from a chimney, being held up by others."
associated_entities: ["white_rabbit", "guinea_pigs"]
alias_or_role_evidence: ""
unknowns: ["color", "pattern", "exact size"]
source_refs: []
[[SECTION markdown]]
# Bill
**Role:** Supporting Character

**Status:** Physically Present

**Physical Description:**
A lizard. He is small enough to be held up by guinea-pigs and can scramble down a chimney.

**Costume & Silhouette:**
Lizard silhouette.

**Descriptive Noun Phrases:**
- Bill the lizard
- Scrambling lizard
- Sky-rocketing lizard

**Uncertainty Notes:**
Specific colors or markings for the lizard are not mentioned.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: dinah
canonical_character_id: dinah
aliases: []
is_fully_identified: false
manual_description_required: true
manual_description_reason: "Only mentioned as Alice's cat; no physical description provided."
clarification_required: false
clarification_reason: ""
clarification_question: ""
character_type_hint: animal
morphology_hint: quadruped
scale_hint: small
renderability_hint: context_only
confidence: 0.5
direct_identity_evidence: "Alice refers to 'her cat, Dinah'."
direct_visual_evidence: ""
costume_or_covering_evidence: ""
movement_evidence: ""
associated_entities: ["alice"]
alias_or_role_evidence: ""
unknowns: ["appearance", "color"]
source_refs: []
[[SECTION markdown]]
# Dinah
**Role:** Referenced

**Status:** Referenced

**Physical Description:**
A cat.

**Costume & Silhouette:**
Feline silhouette.

**Descriptive Noun Phrases:**
- Alice's cat, Dinah

**Uncertainty Notes:**
No visual details provided regarding breed or color.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: guinea_pigs
canonical_character_id: guinea_pigs
aliases: []
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
direct_identity_evidence: "Identified as 'two guinea-pigs'."
direct_visual_evidence: "Holding up Bill the lizard."
costume_or_covering_evidence: ""
movement_evidence: "Holding/lifting an animal."
associated_entities: ["bill"]
alias_or_role_evidence: ""
unknowns: []
source_refs: []
[[SECTION markdown]]
# Guinea-pigs
**Role:** Background Characters

**Status:** Physically Present

**Physical Description:**
Small rodents (guinea-pigs).

**Costume & Silhouette:**
Rodent silhouette.

**Descriptive Noun Phrases:**
- Two guinea-pigs
- Small rodent crowd

**Uncertainty Notes:**
None.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: puppy
canonical_character_id: puppy
aliases: []
is_fully_identified: true
manual_description_required: true
manual_description_reason: "Described as 'enormous' but lacks specific breed, color, or texture details."
clarification_required: false
clarification_reason: ""
clarification_question: ""
character_type_hint: animal
morphology_hint: quadruped
scale_hint: large
renderability_hint: renderable
confidence: 0.8
direct_identity_evidence: "Identified as an 'enormous puppy'."
direct_visual_evidence: "Looking down at Alice, performing charges, and tumbling over itself."
costume_or_covering_evidence: ""
movement_evidence: "Charging, tumbling, looking down."
associated_entities: ["alice"]
alias_or_role_evidence: ""
unknowns: ["color", "breed", "fur texture"]
source_refs: []
[[SECTION markdown]]
# Puppy
**Role:** Obstacle/Distraction

**Status:** Physically Present

**Physical Description:**
An enormous puppy. It is large enough to loom over Alice and perform heavy movements like charging and tumbling.

**Costume & Silhouette:**
Large canine silhouette.

**Descriptive Noun Phrases:**
- Enormous puppy
- Charging puppy
- Tumbling puppy

**Uncertainty Notes:**
The specific breed or color of the puppy is not stated.
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
direct_identity_evidence: "Identified as 'a large blue caterpillar'."
direct_visual_evidence: "Sitting with arms folded, smoking a long hookah on top of a mushroom."
costume_or_covering_evidence: ""
movement_evidence: "Sitting."
associated_entities: []
alias_or_role_evidence: ""
unknowns: []
source_refs: []
[[SECTION markdown]]
# Blue Caterpillar
**Role:** Encountered Character

**Status:** Physically Present

**Physical Description:**
A large, blue caterpillar. It has arms that can be folded.

**Costume & Silhouette:**
Caterpillar silhouette; smoking a long hookah.

**Descriptive Noun Phrases:**
- Large blue caterpillar
- Hookah-smoking caterpillar
- Sitting caterpillar

**Uncertainty Notes:**
The exact morphology (number of legs/segments) is not specified beyond being a "large caterpillar."
[[/SECTION]]
[[/FILMCREATOR_RECORD]]
[[/FILMCREATOR_PACKET]]
````
