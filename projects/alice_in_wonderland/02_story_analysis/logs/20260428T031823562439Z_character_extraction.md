# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-28T03:18:23.562439+00:00
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

Chapter id: CH003

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

**Location:** A riverbank; wet, muddy terrain.
**Characters:** 
- Alice (human girl)
- Mouse (authority figure)
- Lory (sulky bird)
- Duck (literal-minded bird)
- Dodo (solemn leader)
- Eaglet (mocking bird)
- Various Birds/Animals: Magpie, Canary, Old Crab, Young Crab, and others.

**Events:**
1. **The Wet Assembly:** A group of animals (birds with draggled feathers, mammals with clinging fur) are gathered on the bank, all dripping wet and uncomfortable. 
2. **Argument with Lory:** Alice engages in a verbal dispute with the Lory regarding its age; the Lory becomes sulky and refuses to answer.
3. **The Mouse's "Dry" Tale:** The Mouse calls for order and attempts to dry everyone by reciting a historical text about William the Conqueror. 
4. **Linguistic Conflict:** The Duck interrupts, misunderstanding the word "it" in the history lesson; the Eaglet mocks the Dodo's vocabulary. Alice reports she is still wet.
5. **The Caucus-Race:** To solve the dryness issue, the Dodo initiates a "Caucus-race." 
    - *Action:* The Dodo marks a circular course. Animals run in no specific order, starting and stopping at will for approximately thirty minutes.
    - *Result:* Once everyone is dry, the Dodo declares the race over.
6. **Prize Distribution:** 
    - The Dodo deliberates on winners, eventually declaring "Everybody has won."
    - Alice is designated as the prize-giver.
    - Alice retrieves a box of comfits from her pocket and distributes one to each participant.
    - As a prize for herself, Alice is forced to surrender her thimble to the group; the animals present it back to her with a formal speech and cheers.
7. **The Comfit Chaos:** The animals eat the comfits, resulting in large birds complaining of lack of taste and small birds choking/requiring patting on the back.
8. **The Mouse's Tale & Misunderstanding:** 
    - The group settles into a ring for the Mouse to tell his history.
    - Alice becomes distracted by the physical appearance of the Mouse's tail, confusing "tale" (story) with "tail" (appendage).
    - Alice attempts to be helpful by offering to "undo a knot" in the story, which the Mouse perceives as an insult.
9. **The Mouse's Exit:** The Mouse growls and walks away from the group in anger.
10. **The Dinah Reveal:** 
    - While discussing the Mouse's departure, Alice mentions her pet cat, Dinah, and how she catches mice/birds.
    - *Reaction:* A "remarkable sensation" occurs; birds (Magpie, Canary) use various excuses to flee the area immediately.
11. **Alice's Solitude:** Alice is left alone on the bank, feeling lonely and crying for Dinah. 
12. **Ending Beat:** Alice hears distant pattering footsteps, looking up hopefully for a returning Mouse.
````

## Raw Response
````text
[[FILMCREATOR_PACKET]]
[SECTION character_index_markdown]
[[SECTION markdown]]
# Character Index - Chapter CH003

## Present Characters
- [Alice](alice)
- [Mouse](mouse)
- [Lory](lory)
- [Duck](duck)
- [Dodo](dodo)
- [Eaglet](eaglet)
- [Magpie](magpie)
- [Canary](canary)

## Referenced Characters
- [Dinah](dinah)

## Group Entities
- [Crabs](crabs)
[[/SECTION]]
[[/character_index_markdown]]

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
scale_hint: human_scale
renderability_hint: renderable
confidence: 1.0
direct_identity_evidence: "Explicitly named as Alice."
direct_visual_evidence: "Identified as a girl."
costume_or_covering_evidence: "Carries comfits in her pocket; possesses a thimble."
movement_evidence: "Participates in the Caucus-race; distributes prizes."
associated_entities: ["mouse", "dodo", "lory", "duck", "eaglet", "dinah"]
alias_or_role_evidence: ""
unknowns: []
source_refs: []
[[SECTION markdown]]
# Alice
**Role:** Protagonist; prize-giver.

**Status:** Physically present.

**Physical Description:** A human girl. 

**Costume/Traits:** Carries a pocket containing comfits and a thimble.

**Descriptive Phrases:** young human girl, prize-giver, participant in caucus-race.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: mouse
canonical_character_id: mouse
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
direct_identity_evidence: "Explicitly named as Mouse."
direct_visual_evidence: "Has a tail that Alice observes; walks away in anger."
costume_or_covering_evidence: ""
movement_evidence: "Walks away from the group; growls."
associated_entities: ["alice"]
alias_or_role_evidence: ""
unknowns: []
source_refs: []
[[SECTION markdown]]
# Mouse
**Role:** Authority figure; storyteller.

**Status:** Physically present.

**Physical Description:** A small mammal with a notable tail.

**Costume/Traits:** Has a tail that can be confused with a "tale".

**Descriptive Phrases:** small mouse, authority figure, storyteller, angry mouse.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: lory
canonical_character_id: lory
aliases: []
is_fully_identified: true
manual_description_required: false
manual_description_reason: ""
clarification_required: false
clarification_reason: ""
clarification_question: ""
character_type_hint: animal
morphology_hint: winged
scale_hint: small
renderability_hint: renderable
confidence: 0.8
direct_identity_evidence: "Explicitly named as Lory."
direct_visual_evidence: "A bird with draggled feathers (implied by the group description)."
costume_or_covering_evidence: ""
movement_evidence: "Sulky behavior; verbal dispute."
associated_entities: []
alias_or_role_evidence: ""
unknowns: []
source_refs: []
[[SECTION markdown]]
# Lory
**Role:** Sulky participant.

**Status:** Physically present.

**Physical Description:** A bird.

**Costume/Traits:** Draggled feathers (as part of the wet assembly).

**Descriptive Phrases:** sulky bird, draggled lory.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: duck
canonical_character_id: duck
aliases: []
is_fully_identified: true
manual_description_required: false
manual_description_reason: ""
clarification_required: false
clarification_reason: ""
clarification_question: ""
character_type_hint: animal
morphology_hint: winged
scale_hint: small
renderability_hint: renderable
confidence: 0.8
direct_identity_evidence: "Explicitly named as Duck."
direct_visual_evidence: "A bird with draggled feathers."
costume_or_covering_evidence: ""
movement_evidence: "Interrupts the Mouse's tale."
associated_entities: []
alias_or_role_evidence: ""
unknowns: []
source_refs: []
[[SECTION markdown]]
# Duck
**Role:** Literal-minded participant.

**Status:** Physically present.

**Physical Description:** A bird.

**Costume/Traits:** Draggled feathers.

**Descriptive Phrases:** literal-minded duck, draggled bird.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: dodo
canonical_character_id: dodo
aliases: []
is_fully_identified: true
manual_description_required: false
manual_description_reason: ""
clarification_required: false
clarification_reason: ""
clarification_question: ""
character_type_hint: animal
morphology_hint: winged
scale_hint: small
renderability_hint: renderable
confidence: 0.8
direct_identity_evidence: "Explicitly named as Dodo."
direct_visual_evidence: "A bird with draggled feathers; marks a circular course."
costume_or_covering_evidence: ""
movement_evidence: "Initiates the Caucus-race; deliberates on winners."
associated_entities: []
alias_or_role_evidence: ""
unknowns: []
source_refs: []
[[SECTION markdown]]
# Dodo
**Role:** Solemn leader of the assembly.

**Status:** Physically present.

**Physical Description:** A bird.

**Costume/Traits:** Draggled feathers.

**Descriptive Phrases:** solemn dodo, leader of the caucus-race.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: eaglet
canonical_character_id: eaglet
aliases: []
is_fully_identified: true
manual_description_required: false
manual_description_reason: ""
clarification_required: false
clarification_reason: ""
clarification_question: ""
character_type_hint: animal
morphology_hint: winged
scale_hint: tiny
renderability_hint: renderable
confidence: 0.8
direct_identity_evidence: "Explicitly named as Eaglet."
direct_visual_evidence: "A bird with draggled feathers."
costume_or_covering_evidence: ""
movement_evidence: "Mocks the Dodo's vocabulary."
associated_entities: []
alias_or_role_evidence: ""
unknowns: []
source_refs: []
[[SECTION markdown]]
# Eaglet
**Role:** Mocking participant.

**Status:** Physically present.

**Physical Description:** A bird.

**Costume/Traits:** Draggled feathers.

**Descriptive Phrases:** mocking eaglet, small bird.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: magpie
canonical_character_id: magpie
aliases: []
is_fully_identified: true
manual_description_required: false
manual_description_reason: ""
clarification_required: false
clarification_reason: ""
clarification_question: ""
character_type_hint: animal
morphology_hint: winged
scale_hint: small
renderability_hint: renderable
confidence: 0.7
direct_identity_evidence: "Explicitly named as Magpie."
direct_visual_evidence: "A bird that flees when Dinah is mentioned."
costume_or_covering_evidence: ""
movement_evidence: "Flees the area immediately."
associated_entities: []
alias_or_role_evidence: ""
unknowns: []
source_refs: []
[[SECTION markdown]]
# Magpie
**Role:** Fleeing participant.

**Status:** Physically present.

**Physical Description:** A bird.

**Costume/Traits: ** Draggled feathers (implied).

**Descriptive Phrases:** fleeing magpie, small bird.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: canary
canonical_character_id: canary
aliases: []
is_fully_identified: true
manual_description_required: false
manual_description_reason: ""
clarification_required: false
clarification_reason: ""
clarification_question: ""
character_type_hint: animal
morphology_hint: winged
scale_hint: tiny
renderability_hint: renderable
confidence: 0.7
direct_identity_evidence: "Explicitly named as Canary."
direct_visual_evidence: "A bird that flees when Dinah is mentioned."
costume_or_covering_evidence: ""
movement_evidence: "Flees the area immediately."
associated_entities: []
alias_or_role_evidence: ""
unknowns: []
source_refs: []
[[SECTION markdown]]
# Canary
**Role:** Fleeing participant.

**Status:** Physically present.

**Physical Description:** A bird.

**Costume/Traits: ** Draggled feathers (implied).

**Descriptive Phrases:** fleeing canary, small bird.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: crabs
canonical_character_id: crabs
aliases: ["Old Crab", "Young Crab"]
is_fully_identified: true
manual_description_required: false
manual_description_reason: ""
clarification_required: false
clarification_reason: ""
clarification_question: ""
character_type_hint: animal
morphology_hint: multi_legged
scale_hint: small
renderability_hint: renderable
confidence: 0.8
direct_identity_evidence: "Explicitly named as Old Crab and Young Crab."
direct_visual_evidence: "Crabs present at the assembly."
costume_or_covering_evidence: ""
movement_evidence: ""
associated_entities: []
alias_or_role_evidence: ""
unknowns: []
source_refs: []
[[SECTION markdown]]
# Crabs
**Role:** Participants in the wet assembly.

**Status:** Physically present.

**Physical Description:** Crustaceans; includes an "Old Crab" and a "Young Crab".

**Costume/Traits: ** Wet/clinging (implied by group description).

**Descriptive Phrases:** old crab, young crab, small crustaceans.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: dinah
canonical_character_id: dinah
aliases: []
is_fully_identified: true
manual_description_required: false
manual_description_reason: ""
clarification_required: false
clarification_reason: ""
clarification_question: ""
character_type_hint: animal
morphology_hint: quadruped
scale_hint: unknown
renderability_hint: context_only
confidence: 0.5
direct_identity_evidence: "Explicitly named as Dinah; identified as Alice's pet cat."
direct_visual_evidence: "None (referenced only)."
costume_or_covering_evidence: ""
movement_evidence: ""
associated_entities: ["alice"]
alias_or_role_evidence: ""
unknowns: []
source_refs: []
[[SECTION markdown]]
# Dinah
**Role:** Referenced pet.

**Status:** Referenced (not physically present).

**Physical Description:** A cat.

**Costume/Traits: ** Known for catching mice and birds.

**Descriptive Phrases:** Alice's pet cat, mouse-catching cat.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]
[[/FILMCREATOR_PACKET]]
````
