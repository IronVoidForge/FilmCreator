# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-28T03:34:49.463355+00:00
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

**Location: The White Rabbit’s House (Interior)**
*   **Event:** The White Rabbit enters, frantic and muttering about the Duchess and his lost items (fan and white kid gloves). 
*   **Character Entrance/Interaction:** Alice observes the Rabbit; he mistakes her for his housemaid, "Mary Ann," and commands her to fetch the items. Alice complies out of fear/confusion.
*   **Setting Shift:** Alice enters a neat house with a brass plate reading "W. RABBIT." She moves upstairs to a tidy room containing a table by a window.
*   **Object Interaction:** On the table, Alice finds a fan and several pairs of tiny white kid gloves. Near a looking-glass, she finds an unlabeled bottle.
*   **Transformation 1 (Growth):** Alice drinks from the bottle. She rapidly grows until her head presses against the ceiling. She is forced into uncomfortable positions: kneeling, lying down with an elbow against the door, and eventually sticking one arm out the window and one foot up the chimney to fit.
*   **Character Interaction/Conflict:** The Rabbit arrives at the door. Because Alice's elbow blocks it, he decides to enter through the window. 
*   **Action/Sound Event:** Alice reaches out a hand toward the window; she hears a shriek and the sound of breaking glass (implied cucumber-frames).
*   **Character Reveal/Dialogue:** A new character, Pat (a laborer), is introduced via dialogue. The Rabbit and Pat discuss the "arm" filling the window.
*   **Action/Sound Event:** Alice reaches out again; two shrieks and more breaking glass are heard.
*   **Event (The Chimney):** A group of animals arrives with ladders and ropes to attack the house. They decide to send a character named Bill down the chimney. 
*   **Action/Interaction:** Alice, positioned in the chimney, delivers a sharp kick to the scrambling animal above her.
*   **Outcome:** "Bill" (a small lizard) is kicked out of the chimney and into the crowd. The Rabbit threatens to burn the house down.
*   **Transformation 2 (Shrinking):** The Rabbit throws a barrowful of pebbles through the window. As they hit the floor, they transform into little cakes. Alice eats one cake and shrinks to a manageable size.
*   **Exit:** Alice runs out of the house, passing a crowd of animals holding the injured Bill.

**Location: The Wood (Exterior)**
*   **Setting Shift:** Alice escapes into a thick wood to avoid the crowd.
*   **Character Interaction/Conflict:** An enormous puppy discovers Alice. Alice attempts to play with it using a stick to distract it, dodging behind a large thistle to avoid being trampled. 
*   **Action/Exit:** Once the puppy settles down, Alice runs away until she is out of breath.
*   **Location Subzone:** Alice rests against a buttercup in a clearing.
*   **Object Interaction/Reveal:** Alice finds a large mushroom. She climbs onto tiptoe to peer over the edge of the cap.
*   **Character Reveal:** On top of the mushroom, Alice discovers a large blue Caterpillar sitting and smoking a long hookah.
````

## Raw Response
````text
[[FILMCREATOR_PACKET]]
task: character_extraction
version: 1

[[SECTION character_index_markdown]]
[[markdown]]
# Character Index - Chapter CH004

## Alice
- [alice](#alice)

## Bill the Lizard
- [bill_the_lizard](#bill_the_lizard)

## Blue Caterpillar
- [blue_caterpillar](#blue_caterpillar)

## White Rabbit
- [white_rabbit](#white_rabbit)

## Pat (Laborer)
- [pat_laborer](#pat_laborer)

## Enormous Puppy
- [enormous_puppy](#enormous_puppy)

---

<a name="alice"></a>
### Alice
Chapter Role: Protagonist. Experiences rapid growth and shrinking; encounters the Caterpillar.
Status: Physically Present.

<a name="bill_the_lizard"></a>
### Bill the Lizard
Chapter Role: Victim of Alice's kick; part of the animal crowd.
Status: Physically Present (briefly).

<a name="blue_caterpillar"></a>
### Blue Caterpillar
Chapter Role: New encounter at the end of the chapter.
Status: Physically Present.

<a name="white_rabbit"></a>
### White Rabbit
Chapter Role: Antagonist/Instigator; owner of the house.
Status: Physically Present.

<a name="pat_laborer"></a>
### Pat (Laborer)
Chapter Role: Dialogue participant with the Rabbit.
Status: Referenced/Dialogue only.

<a name="enormous_puppy"></a>
### Enormous Puppy
Chapter Role: Obstacle in the wood.
Status: Physically Present.
[[/SECTION]]

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
confidence: 0.9
direct_identity_evidence: "Explicitly named as Alice throughout the text."
direct_visual_evidence: "Described as growing to press against a ceiling and shrinking after eating a cake."
costume_or_covering_evidence: ""
movement_evidence: "Running, climbing on tiptoe, kicking, kneeling, lying down."
associated_entities: ["white_rabbit", "blue_caterpillar"]
alias_or_role_evidence: ""
unknowns: []
source_refs: []
[[SECTION markdown]]
# Alice
**Role:** Protagonist

**Status:** Physically Present.

**Physical Description:** 
A young girl. In this chapter, she undergoes extreme scale shifts: first growing until her head presses against a ceiling (giant scale), then shrinking to a manageable size after eating a cake.

**Costume/Silhouette:** 
No specific clothing details provided in this chapter text.

**Descriptive Noun Phrases:** 
Young girl, giant-sized Alice, tiny Alice, climbing girl.

**Uncertainty Notes:** 
Specific hair color or dress details are not mentioned in this chapter.
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
confidence: 0.8
direct_identity_evidence: "Identified as the White Rabbit and via brass plate 'W. RABBIT'."
direct_visual_evidence: "Enters a house, frantic, muttering; throws pebbles."
costume_or_covering_evidence: ""
movement_evidence: "Entering through a window, throwing pebbles from a barrow."
associated_entities: ["alice", "pat_laborer"]
alias_or_role_evidence: "Brass plate reads 'W. RABBIT'."
unknowns: []
source_refs: []
[[SECTION markdown]]
# White Rabbit
**Role:** Antagonist/Instigator

**Status:** Physically Present.

**Physical Description:** 
A rabbit, likely small in scale. Characterized by frantic and muttering behavior.

**Costume/Silhouette:** 
Not explicitly described, but owns a house with a brass plate and uses a barrow for pebbles.

**Descriptive Noun Phrases:** 
Frantic white rabbit, muttering rabbit, owner of the house.

**Uncertainty Notes:** 
Specific fur texture or clothing (if any) is not detailed in this chapter.
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
confidence: 0.7
direct_identity_evidence: "Identified as a large blue Caterpillar."
direct_visual_evidence: "Large, blue, sitting on top of a mushroom, smoking a long hookah."
costume_or_covering_evidence: ""
movement_evidence: "Sitting."
associated_entities: []
alias_or_role_evidence: ""
unknowns: ["morphology_hint"]
source_refs: []
[[SECTION markdown]]
# Blue Caterpillar
**Role:** New Encounter

**Status:** Physically Present.

**Physical Description:** 
A large, blue caterpillar.

**Costume/Silhouette:** 
Sitting atop a large mushroom cap; smoking a long hookah.

**Descriptive Noun Phrases:** 
Large blue caterpillar, hookah-smoking caterpillar, mushroom-dwelling creature.

**Uncertainty Notes:** 
The exact morphology (number of legs, etc.) is not specified beyond being a "caterpillar."
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
confidence: 0.8
direct_identity_evidence: "Identified as 'Bill' and a 'small lizard'."
direct_visual_evidence: "Scrambling down a chimney, being kicked out of the chimney into a crowd."
costume_or_covering_evidence: ""
movement_evidence: "Scrambling, being kicked."
associated_entities: ["alice"]
alias_or_role_evidence: "Called 'Bill' by the group/narrator."
unknowns: []
source_refs: []
[[SECTION markdown]]
# Bill the Lizard
**Role:** Victim

**Status:** Physically Present.

**Physical Description:** 
A small lizard.

**Costume/Silhouette:** 
Small, scrambling form.

**Descriptive Noun Phrases:** 
Small lizard, scrambled Bill, injured lizard.

**Uncertainty Notes:** 
Specific color or species details are minimal beyond "lizard."
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
asset_id: pat_laborer
canonical_character_id: pat_laborer
aliases: ["Pat"]
is_fully_identified: true
manual_description_required: true
manual_description_reason: "Character is only mentioned via dialogue; no physical description or visual evidence provided."
clarification_required: false
clarification_reason: ""
clarification_question: ""
character_type_hint: humanoid_nonhuman
morphology_hint: biped
scale_hint: human_scale
renderability_hint: context_only
confidence: 0.4
direct_identity_evidence: "Named Pat and identified as a laborer in dialogue."
direct_visual_evidence: ""
costume_or_covering_evidence: ""
movement_evidence: ""
associated_entities: ["white_rabbit"]
alias_or_role_evidence: "Identified as 'Pat (a laborer)'."
unknowns: ["physical_appearance"]
source_refs: []
[[SECTION markdown]]
# Pat (Laborer)
**Role:** Dialogue Participant

**Status:** Referenced/Dialogue only.

**Physical Description:** 
No physical description provided in the text.

**Costume/Silhouette:** 
Unknown.

**Descriptive Noun Phrases:** 
Pat the laborer.

**Uncertainty Notes:** 
This character is not visually present; appearance must be inferred or created based on the role of a "laborer."
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
confidence: 0.7
direct_identity_evidence: "Identified as an enormous puppy."
direct_visual_evidence: "Discovers Alice in the wood; can be distracted by a stick."
costume_or_covering_evidence: ""
movement_evidence: "Running/moving through the wood, settling down."
associated_entities: ["alice"]
alias_or_role_evidence: ""
unknowns: []
source_refs: []
[[SECTION markdown]]
# Enormous Puppy
**Role:** Obstacle

**Status:** Physically Present.

**Physical Description:** 
An enormous puppy.

**Costume/Silhouette:** 
Large quadruped silhouette.

**Descriptive Noun Phrases:** 
Enormous puppy, large dog, distracting puppy.

**Uncertainty Notes:** 
Breed and color are not specified.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
