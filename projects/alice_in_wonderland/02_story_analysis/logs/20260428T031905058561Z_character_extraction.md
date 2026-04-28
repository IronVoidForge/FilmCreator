# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-28T03:19:05.058561+00:00
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
scale_hint: human_scale
renderability_hint: renderable
confidence: 1.0
direct_identity_evidence: "Alice (human girl)"
direct_visual_evidence: "Alice retrieves a box of comfits from her pocket... Alice is designated as the prize-giver."
costume_or_covering_evidence: "Carries a box of comfits and a thimble in her pocket."
movement_evidence: "Runs in the Caucus-race; distributes prizes; cries for Dinah."
associated_entities: ["mouse", "dodo", "lory", "duck", "eaglet", "dinah"]
alias_or_role_evidence: ""
unknowns: []
source_refs: []
[[SECTION character_index_markdown]]
[[SECTION markdown]]
# Alice
**Role:** Protagonist / Prize-giver

**Status:** Physically Present

**Physical Description:**
A human girl. While specific clothing details are not provided in this chapter, she carries a pocket containing comfits and a thimble.

**Descriptive Noun Phrases:**
- Human girl
- Prize-giver
- Lonely child on the riverbank

**Uncertainty Notes:**
None.
[[/SECTION]]
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
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
direct_identity_evidence: "The Mouse calls for order..."
direct_visual_evidence: "Alice becomes distracted by the physical appearance of the Mouse's tail."
costume_or_covering_evidence: ""
movement_evidence: "Walks away from the group in anger; growls."
associated_entities: ["alice", "dodo"]
alias_or_role_evidence: "Authority figure"
unknowns: []
source_refs: []
[[SECTION character_index_markdown]]
[[SECTION markdown]]
# Mouse
**Role:** Authority figure / Storyteller

**Status:** Physically Present

**Physical Description:**
A small mammal with a notable tail. The tail is described as having knots or being subject to "undoing" in Alice's metaphorical confusion.

**Descriptive Noun Phrases:**
- Small mouse
- Authoritative mouse
- Mouse with a prominent tail

**Uncertainty Notes:**
Specific fur color or pattern is not mentioned.
[[/SECTION]]
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
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
morphology_hint: biped
scale_hint: small
renderability_hint: renderable
confidence: 0.9
direct_identity_evidence: "The Dodo initiates a 'Caucus-race.'"
direct_visual_evidence: "The Dodo marks a circular course."
costume_or_covering_evidence: ""
movement_evidence: "Marks a circular course; declares the race over."
associated_entities: ["alice", "mouse"]
alias_or_role_evidence: "Solemn leader"
unknowns: []
source_refs: []
[[SECTION character_index_markdown]]
[[SECTION markdown]]
# Dodo
**Role:** Solemn Leader / Race Organizer

**Status:** Physically Present

**Physical Description:**
A bird (Dodo species). 

**Descriptive Noun Phrases:**
- Solemn dodo
- Leader of the Caucus-race
- Large-beaked bird

**Uncertainty Notes:**
Specific plumage color is not specified.
[[/SECTION]]
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
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
direct_identity_evidence: "Alice engages in a verbal dispute with the Lory..."
direct_visual_evidence: "draggled feathers"
costume_or_covering_evidence: ""
movement_evidence: "Sulky behavior."
associated_entities: []
alias_or_role_evidence: "Sulky bird"
unknowns: []
source_refs: []
[[SECTION character_index_markdown]]
[[SECTION markdown]]
# Lory
**Role:** Participant / Antagonist (minor)

**Status:** Physically Present

**Physical Description:**
A bird with draggled feathers due to being wet. Known for being sulky.

**Descriptive Noun Phrases:**
- Sulky lory
- Wet, draggled bird

**Uncertainty Notes:**
Color of feathers is unknown.
[[/SECTION]]
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
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
direct_identity_evidence: "The Duck interrupts..."
direct_visual_evidence: "draggled feathers"
costume_or_covering_evidence: ""
movement_evidence: ""
associated_entities: []
alias_or_role_evidence: "Literal-minded bird"
unknowns: []
source_refs: []
[[SECTION character_index_markdown]]
[[SECTION markdown]]
# Duck
**Role:** Participant

**Status:** Physically Present

**Physical Description:**
A bird with draggled feathers. Characterized by literal-mindedness.

**Descriptive Noun Phrases:**
- Literal-minded duck
- Wet, draggled waterfowl

**Uncertainty Notes:**
Specific color/species details are sparse beyond "Duck".
[[/SECTION]]
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
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
scale_hint: small
renderability_hint: renderable
confidence: 0.8
direct_identity_evidence: "the Eaglet mocks the Dodo's vocabulary."
direct_visual_evidence: "draggled feathers"
costume_or_covering_evidence: ""
movement_evidence: ""
associated_entities: []
alias_or_role_evidence: "Mocking bird"
unknowns: []
source_refs: []
[[SECTION character_index_markdown]]
[[SECTION markdown]]
# Eaglet
**Role:** Participant

**Status:** Physically Present

**Physical Description:**
A small bird with draggled feathers. Known for being mocking.

**Descriptive Noun Phrases:**
- Mocking eaglet
- Draggled young bird

**Uncertainty Notes:**
Color/species details are sparse.
[[/SECTION]]
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
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
scale_hint: small
renderability_hint: context_only
confidence: 0.7
direct_identity_evidence: "Alice mentions her pet cat, Dinah..."
direct_visual_evidence: ""
costume_or_covering_evidence: ""
movement_evidence: ""
associated_entities: ["alice"]
alias_or_role_evidence: ""
unknowns: []
source_refs: []
[[SECTION character_index_markdown]]
[[SECTION markdown]]
# Dinah
**Role:** Alice's Pet (Referenced)

**Status:** Referenced

**Physical Description:**
A cat. Known to catch mice and birds.

**Descriptive Noun Phrases:**
- Alice's pet cat
- Mouse-catching cat

**Uncertainty Notes:**
No visual description of Dinah is provided in this chapter; she is only mentioned by name.
[[/SECTION]]
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
asset_id: bird_group_various
canonical_character_id: bird_group_various
aliases: ["Magpie", "Canary", "Old Crab", "Young Crab"]
is_fully_identified: false
manual_description_required: true
manual_description_reason: "The group is a collection of various animals with minimal individual visual detail provided beyond being 'wet' or 'draggled'."
clarification_required: true
clarification_reason: ""
clarification_question: "Should specific birds like the Magpie and Canary be treated as distinct characters or part of this collective background group?"
character_type_hint: animal
morphology_hint: winged
scale_hint: small
renderability_hint: renderable
confidence: 0.5
direct_identity_evidence: "Various Birds/Animals: Magpie, Canary, Old Crab, Young Crab..."
direct_visual_evidence: "draggled feathers; clinging fur"
costume_or_covering_evidence: ""
movement_evidence: "flee the area immediately; running in Caucus-race."
associated_entities: []
alias_or_role_evidence: ""
unknowns: ["Specific colors", "Individual sizes"]
source_refs: []
[[SECTION character_index_markdown]]
[[SECTION markdown]]
# Various Birds and Animals
**Role:** Participants in the Caucus-race

**Status:** Physically Present

**Physical Description:**
A collection of animals including birds (Magpie, Canary) and crabs (Old Crab, Young Crab). They are all described as being wet, with draggled feathers or clinging fur.

**Descriptive Noun Phrases:**
- Draggled assembly of animals
- Wet riverbank creatures
- Small birds and crabs

**Uncertainty Notes:**
Individual visual traits (colors, specific species details) are not provided for most members of this group.
[[/SECTION]]
[[/SECTION]]
[[/FILMCREATOR_RECORD]]
[[/FILMCREATOR_PACKET]]
````
