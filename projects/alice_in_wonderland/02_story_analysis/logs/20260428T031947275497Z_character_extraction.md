# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-28T03:19:47.275497+00:00
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

- keep one record per meaningful character mention

- prefer short facts over long prose

- if uncertain, use clarification_required instead of guessing

- if clarification is not required, still include clarification_reason and clarification_question as empty values

- still emit explicit character records; do not collapse them into index bullets only



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
[[SECTION character_index_markdown]]
[[markdown]]
# Character Index - Chapter CH003

## Present Characters
- [Alice](#alice)
- [Mouse](#mouse)
- [Lory](#lory)
- [Duck](#duck)
- [Dodo](#dodo)
- [Eaglet](#eaglet)
- [Magpie](#magpie)
- [Canary](#canary)

## Referenced Characters
- [Dinah](#dinah)

---

<a name="alice"></a>
### Alice
**Role:** Protagonist; prize-giver.
**Status:** Physically present.
**Description:** Human girl.
**Costume/Traits:** Carries a box of comfits in her pocket; possesses a thimble.
**Prompt Phrases:** young human girl, small child, holding comfits, wearing a thimble.

<a name="mouse"></a>
### Mouse
**Role:** Authority figure; storyteller.
**Status:** Physically present.
**Description:** Small mammal with a notable tail (subject of linguistic confusion).
**Costume/Traits:** Has a tail that can be "knotted."
**Prompt Phrases:** small mouse, rodent, long tail, authoritative posture.

<a name="lory"></a>
### Lory
**Role:** Sulky participant.
**Status:** Physically present.
**Description:** Bird with draggled feathers.
**Costume/Traits:** Sulky temperament.
**Prompt Phrases:** lory bird, parrot-like, wet feathers, sulking expression.

<a name="duck"></a>
### Duck
**Role:** Literal-minded participant.
**Status:** Physically present.
**Description:** Bird with draggled feathers.
**Costume/Traits:** Easily confused by language.
**Prompt Phrases:** duck, waterfowl, wet plumage.

<a name="dodo"></a>
### Dodo
**Role:** Solemn leader; race organizer.
**Status:** Physically present.
**Description:** Large bird.
**Costume/Traits:** Solemn demeanor, organizes the Caucus-race.
**Prompt Phrases:** dodo bird, large flightless bird, solemn expression, leader.

<a name="eaglet"></a>
### Eaglet
**Role:** Mocking participant.
**Status:** Physically present.
**Description:** Bird with draggled feathers.
**Costume/Traits:** Mocking attitude toward the Dodo.
**Prompt Phrases:** eaglet, small bird of prey, mocking expression.

<a name="magpie"></a>
### Magpie
**Role:** Fleeing participant.
**Status:** Physically present.
**Description:** Bird with draggled feathers.
**Costume/Traits:** Flees upon mention of Dinah.
**Prompt Phrases:** magpie, black and white bird, wet feathers.

<a name="canary"></a>
### Canary
**Role:** Fleeing participant.
**Status:** Physically present.
**Description:** Bird with draggled feathers.
**Costume/Traits:** Flees upon mention of Dinah.
**Prompt Phrases:** canary, small yellow bird, wet feathers.

<a name="dinah"></a>
### Dinah
**Role:** Mentioned pet.
**Status:** Referenced.
**Description:** Cat.
**Costume/Traits:** Known for catching mice and birds.
**Prompt Phrases:** domestic cat, predator.
[[/SECTION]]
[[/FILMCREATOR_PACKET]]

[[FILMCREATOR_RECORD]]
asset_id: alice
canonical_character_id: alice
aliases: []
is_fully_identified: true
manual_description_required: false
manual_description_reason: 
clarification_required: false
clarification_reason: 
clarification_question: 
character_type_hint: human
morphology_hint: girl
scale_hint: small_human
renderability_hint: high
confidence: 1.0
direct_identity_evidence: "Alice engages in a verbal dispute..."
direct_visual_evidence: "Alice retrieves a box of comfits from her pocket..."
costume_or_covering_evidence: "Alice is forced to surrender her thimble..."
movement_evidence: "Alice is left alone on the bank..."
associated_entities: [mouse, dinah]
alias_or_role_evidence: "Alice is designated as the prize-giver."
unknowns: []
source_refs: [CH003]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
asset_id: mouse
canonical_character_id: mouse
aliases: []
is_fully_identified: true
manual_description_required: false
manual_description_reason: 
clarification_required: false
clarification_reason: 
clarification_question: 
character_type_hint: mammal
morphology_hint: rodent
scale_hint: small
renderability_hint: high
confidence: 1.0
direct_identity_evidence: "The Mouse calls for order..."
direct_visual_evidence: "Alice becomes distracted by the physical appearance of the Mouse's tail..."
costume_or_covering_evidence: 
movement_evidence: "The Mouse growls and walks away from the group in anger."
associated_entities: [alice, dinah]
alias_or_role_evidence: "The Mouse's 'Dry' Tale"
unknowns: []
source_refs: [CH003]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
asset_id: lory
canonical_character_id: lory
aliases: []
is_fully_identified: true
manual_description_required: false
manual_description_reason: 
clarification_required: false
clarification_reason: 
clarification_question: 
character_type_hint: bird
morphology_hint: lory
scale_hint: small
renderability_hint: medium
confidence: 1.0
direct_identity_evidence: "Alice engages in a verbal dispute with the Lory..."
direct_visual_evidence: "birds with draggled feathers"
costume_or_covering_evidence: "draggled feathers"
movement_evidence: 
associated_entities: []
alias_or_role_evidence: "The Lory becomes sulky"
unknowns: []
source_refs: [CH003]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
asset_id: duck
canonical_character_id: duck
aliases: []
is_fully_identified: true
manual_description_required: false
manual_description_reason: 
clarification_required: false
clarification_reason: 
clarification_question: 
character_type_hint: bird
morphology_hint: duck
scale_hint: medium
renderability_hint: medium
confidence: 1.0
direct_identity_evidence: "The Duck interrupts..."
direct_visual_evidence: "birds with draggled feathers"
costume_or_covering_evidence: "draggled feathers"
movement_evidence: 
associated_entities: []
alias_or_role_evidence: ""
unknowns: []
source_refs: [CH003]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
asset_id: dodo
canonical_character_id: dodo
aliases: []
is_fully_identified: true
manual_description_required: false
manual_description_reason: 
clarification_required: false
clarification_reason: 
clarification_question: 
character_type_hint: bird
morphology_hint: dodo
scale_hint: large
renderability_hint: medium
confidence: 1.0
direct_identity_evidence: "the Dodo initiates a 'Caucus-race.'"
direct_visual_evidence: "birds with draggled feathers"
costume_or_covering_evidence: "draggled feathers"
movement_evidence: "The Dodo marks a circular course."
associated_entities: []
alias_or_role_evidence: "solemn leader"
unknowns: []
source_refs: [CH003]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
asset_id: eaglet
canonical_character_id: eaglet
aliases: []
is_fully_identified: true
manual_description_required: false
manual_description_reason: 
clarification_required: false
clarification_reason: 
clarification_question: 
character_type_hint: bird
morphology_hint: eaglet
scale_hint: small
renderability_hint: medium
confidence: 1.0
direct_identity_evidence: "the Eaglet mocks the Dodo's vocabulary."
direct_visual_evidence: "birds with draggled feathers"
costume_or_covering_evidence: "draggled feathers"
movement_evidence: 
associated_entities: []
alias_or_role_evidence: ""
unknowns: []
source_refs: [CH003]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
asset_id: magpie
canonical_character_id: magpie
aliases: []
is_fully_identified: true
manual_description_required: false
manual_description_reason: 
clarification_required: false
clarification_reason: 
clarification_question: 
character_type_hint: bird
morphology_hint: magpie
scale_hint: small
renderability_hint: medium
confidence: 1.0
direct_identity_evidence: "birds (Magpie, Canary) use various excuses to flee"
direct_visual_evidence: ""
costume_or_covering_evidence: ""
movement_evidence: "use various excuses to flee the area immediately."
associated_entities: []
alias_or_role_evidence: ""
unknowns: []
source_refs: [CH003]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
asset_id: canary
canonical_character_id: canary
aliases: []
is_fully_identified: true
manual_description_required: false
manual_description_reason: 
clarification_required: false
clarification_reason: 
clarification_question: 
character_type_hint: bird
morphology_hint: canary
scale_hint: small
renderability_hint: medium
confidence: 1.0
direct_identity_evidence: "birds (Magpie, Canary) use various excuses to flee"
direct_visual_evidence: ""
costume_or_covering_evidence: ""
movement_evidence: "use various excuses to flee the area immediately."
associated_entities: []
alias_or_role_evidence: ""
unknowns: []
source_refs: [CH003]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
asset_id: dinah
canonical_character_id: dinah
aliases: []
is_fully_identified: true
manual_description_required: false
manual_description_reason: 
clarification_required: false
clarification_reason: 
clarification_question: 
character_type_hint: mammal
morphology_hint: cat
scale_hint: medium
renderability_hint: low
confidence: 1.0
direct_identity_evidence: "Alice mentions her pet cat, Dinah"
direct_visual_evidence: 
costume_or_covering_evidence: 
movement_evidence: 
associated_entities: [alice]
alias_or_role_evidence: ""
unknowns: []
source_refs: [CH003]
[[/FILMCREATOR_RECORD]]
[[/FILMCREATOR_RECORD]]
````
