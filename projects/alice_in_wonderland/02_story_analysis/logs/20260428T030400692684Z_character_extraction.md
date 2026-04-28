# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-28T03:04:00.692684+00:00
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

**Location:** A riverbank; a circular race-course marked out on the ground.
**Characters:** 
- Alice (human girl)
- Mouse (authoritative, prone to offense)
- Dodo (solemn, leader of the Caucus-race)
- Lory (sulky, older than Alice)
- Duck (literal-minded)
- Eaglet (skeptical, mocking)
- Various Birds/Animals: Magpie, Canary, Old Crab, Young Crab, and others.

**Events:**
1. **The Wet Gathering:** A group of animals (birds with draggled feathers, wet fur) assembles on the bank. They are uncomfortable and cross due to being wet. 
2. **Argument with Lory:** Alice engages in a long argument with the Lory regarding its age; the Lory refuses to answer and becomes sulky.
3. **The Mouse's "Dry" Story:** The Mouse calls for order and attempts to dry everyone by reciting a historical text about William the Conqueror. 
4. **Interruption/Confusion:** The Duck interrupts the Mouse, misunderstanding the word "it." The Eaglet mocks the Dodo’s vocabulary. Alice reports she is still wet.
5. **The Caucus-Race:** The Dodo adjourns the meeting to propose a "Caucus-race." He marks out a circular course. The animals run in no specific order, starting and stopping whenever they please for thirty minutes until they are dry.
6. **Prize Distribution:** The Dodo declares everyone a winner. Alice is designated as the prize-giver. 
7. **Object Interaction (Comfits):** Alice retrieves a box of comfits from her pocket and distributes them to the group. There is chaos/choking among the small animals and complaints from large birds.
8. **Object Interaction (Thimble):** The Mouse insists Alice receives a prize. Alice produces a thimble. The Dodo leads the group in a formal presentation, returning the thimble to Alice as an "elegant" gift. Alice bows and accepts it solemnly.
9. **The Mouse's Tale:** The animals sit in a ring. The Mouse begins telling a "long and sad tale." 
10. **Misunderstanding/Conflict:** Alice confuses the Mouse's "tale" (story) with its physical "tail." She attempts to help by trying to "undo a knot," which the Mouse perceives as an insult. The Mouse exits, walking away angrily.
11. **The Crab Argument:** As the Mouse leaves, an Old Crab scolds a Young Crab for losing her temper.
12. **The Dinah Reveal:** Alice mentions her cat, Dinah, and how she catches mice/birds. 
13. **Mass Exit:** The mention of a cat causes panic. Birds (Magpie, Canary) use various excuses to flee the area immediately.
14. **Alice's Solitude:** Alice is left alone on the bank, crying due to loneliness and the absence of Dinah. She hears footsteps in the distance.
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
direct_visual_evidence: "Identified as a human girl; interacts with animals."
costume_or_covering_evidence: ""
movement_evidence: "Bows to the Dodo; walks on the riverbank; cries."
associated_entities: ["mouse", "dodo", "lory", "duck", "eaglet", "dinah"]
alias_or_role_evidence: "Designated as the prize-giver for the Caucus-race."
unknowns: []
source_refs: ["CH003"]
[[SECTION character_index_markdown]]
[[SECTION markdown]]
# Alice
**Role:** Protagonist; Prize-giver.

**Status:** Physically Present.

**Physical Description:** 
A human girl. Specific facial features or hair color are not detailed in this chapter, though she is capable of bowing and expressing complex emotions like loneliness and sadness.

**Costume & Silhouette:** 
Not explicitly described in this chapter, though she carries a box of comfits and a thimble in her pockets.

**Descriptive Noun Phrases:** 
human girl, prize-giver, lonely child.

**Uncertainty Notes:** 
Visual specifics (hair/eye color) are not provided in the text; rely on established character design from previous chapters if available.
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
scale_hint: tiny
renderability_hint: renderable
confidence: 0.9
direct_identity_evidence: "The Mouse"
direct_visual_evidence: "Has a tail (referenced via the 'tale/tail' pun); small enough to be threatened by Alice's attempt to undo a knot."
costume_or_covering_evidence: ""
movement_evidence: "Walks away angrily; sits in a ring with other animals."
associated_entities: ["alice", "dodo"]
alias_or_role_evidence: "Attempts to dry the group by reciting history."
unknowns: []
source_refs: ["CH003"]
[[SECTION character_index_markdown]]
[[SECTION markdown]]
# Mouse
**Role:** Authoritative figure; Storyteller.

**Status:** Physically Present.

**Physical Description:** 
A small mouse. Possesses a tail (subject of a pun).

**Costume & Silhouette:** 
Small, rodent-like silhouette.

**Descriptive Noun Phrases:** 
small mouse, authoritative mouse, storyteller mouse.

**Uncertainty Notes:** 
Specific fur color or markings are not mentioned.
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
direct_identity_evidence: "Dodo"
direct_visual_evidence: "Leads the group in a formal presentation; marks out a circular course."
costume_or_covering_evidence: ""
movement_evidence: "Marks out a race course; leads the presentation of the thimble."
associated_entities: ["alice", "eaglet"]
alias_or_role_evidence: "Leader of the Caucus-race."
unknowns: []
source_refs: ["CH003"]
[[SECTION character_index_markdown]]
[[SECTION markdown]]
# Dodo
**Role:** Leader of the Caucus-race.

**Status:** Physically Present.

**Physical Description:** 
A bird (Dodo). Solemn demeanor.

**Costume & Silhouette:** 
Bird silhouette; likely large enough to be a leader but small enough to participate in the gathering on the bank.

**Descriptive Noun Phrases:** 
solemn dodo, race leader, formal dodo.

**Uncertainty Notes:** 
Specific plumage colors or patterns are not described.
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
direct_identity_evidence: "Lory"
direct_visual_evidence: "Engages in an argument with Alice; described as sulky."
costume_or_covering_evidence: ""
movement_evidence: "Part of the wet gathering on the bank."
associated_entities: ["alice"]
alias_or_role_evidence: ""
unknowns: []
source_refs: ["CH003"]
[[SECTION character_index_markdown]]
[[SECTION markdown]]
# Lory
**Role:** Argumentative participant.

**Status:** Physically Present.

**Physical Description:** 
A bird (Lory). Described as being older than Alice.

**Costume & Silhouette:** 
Bird silhouette; feathers are likely draggled/wet at the start of the chapter.

**Descriptive Noun Phrases:** 
sulky lory, old lory.

**Uncertainty Notes:** 
Color and specific species-accurate markings are not provided.
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
direct_identity_evidence: "Duck"
direct_visual_evidence: "Interrupts the Mouse."
costume_or_covering_evidence: ""
movement_evidence: "Part of the wet gathering."
associated_entities: ["mouse"]
alias_or_role_evidence: "Literal-minded interrupter."
unknowns: []
source_refs: ["CH003"]
[[SECTION character_index_markdown]]
[[SECTION markdown]]
# Duck
**Role:** Interrupter.

**Status:** Physically Present.

**Physical Description:** 
A bird (Duck). Literal-minded personality.

**Costume & Silhouette:** 
Waterfowl silhouette; feathers likely wet/draggled.

**Descriptive Noun Phrases:** 
literal-minded duck, wet duck.

**Uncertainty Notes:** 
Specific breed or color not specified.
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
scale_hint: tiny
renderability_hint: renderable
confidence: 0.8
direct_identity_evidence: "Eaglet"
direct_visual_evidence: "Mocks the Dodo."
costume_or_covering_evidence: ""
movement_evidence: "Part of the wet gathering."
associated_entities: ["dodo"]
alias_or_role_evidence: "Skeptical/mocking participant."
unknowns: []
source_refs: ["CH003"]
[[SECTION character_index_markdown]]
[[SECTION markdown]]
# Eaglet
**Role:** Skeptical mocker.

**Status:** Physically Present.

**Physical Description:** 
A young eagle (Eaglet).

**Costume & Silhouette:** 
Small bird silhouette; feathers likely wet/draggled.

**Descriptive Noun Phrases:** 
skeptical eaglet, mocking eaglet.

**Uncertainty Notes:** 
Specific plumage details are absent.
[[/SECTION]]
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
asset_id: old_crab
canonical_character_id: old_crab
aliases: []
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
direct_identity_evidence: "Old Crab"
direct_visual_evidence: "Scolds the Young Crab."
costume_or_covering_evidence: ""
movement_evidence: "Present on the bank during the Mouse's exit."
associated_entities: ["young_crab"]
alias_or_role_evidence: ""
unknowns: []
source_refs: ["CH003"]
[[SECTION character_index_markdown]]
[[SECTION markdown]]
# Old Crab
**Role:** Scolding elder.

**Status:** Physically Present.

**Physical Description:** 
A crab.

**Costume & Silhouette:** 
Crustacean silhouette; multi-legged.

**Descriptive Noun Phrases:** 
old crab, scolding crab.

**Uncertainty Notes:** 
Color and shell texture are not described.
[[/SECTION]]
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
asset_id: young_crab
canonical_character_id: young_crab
aliases: []
is_fully_identified: true
manual_description_required: false
manual_description_reason: ""
clarification_required: false
clarification_reason: ""
clarification_question: ""
character_type_hint: animal
morphology_hint: multi_legged
scale_hint: tiny
renderability_hint: renderable
confidence: 0.8
direct_identity_evidence: "Young Crab"
direct_visual_evidence: "Gets scolded by the Old Crab."
costume_or_covering_evidence: ""
movement_evidence: "Present on the bank."
associated_entities: ["old_crab"]
alias_or_role_evidence: ""
unknowns: []
source_refs: ["CH003"]
[[SECTION character_index_markdown]]
[[SECTION markdown]]
# Young Crab
**Role:** Temperamental participant.

**Status:** Physically Present.

**Physical Description:** 
A crab.

**Costume & Silhouette:** 
Small crustacean silhouette; multi-legged.

**Descriptive Noun Phrases:** 
young crab, temperamental crab.

**Uncertainty Notes:** 
Color and shell texture are not described.
[[/SECTION]]
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
asset_id: dinah
canonical_character_id: dinah
aliases: ["Dinah"]
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
confidence: 0.9
direct_identity_evidence: "Alice's cat, Dinah"
direct_visual_evidence: "None (referenced only)."
costume_or_covering_evidence: ""
movement_evidence: ""
associated_entities: ["alice"]
alias_or_role_evidence: "Mentioned as a hunter of mice and birds."
unknowns: []
source_refs: ["CH003"]
[[SECTION character_index_markdown]]
[[SECTION markdown]]
# Dinah
**Role:** Referenced pet.

**Status:** Referenced.

**Physical Description:** 
A cat.

**Costume & Silhouette:** 
Feline silhouette.

**Descriptive Noun Phrases:** 
Alice's cat, predatory cat.

**Uncertainty Notes:** 
Not physically present in the chapter; visual details (color/pattern) are not provided.
[[/SECTION]]
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
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
direct_identity_evidence: "Magpie"
direct_visual_evidence: "Flees the area when Dinah is mentioned."
costume_or_covering_evidence: ""
movement_evidence: "Flees/flies away."
associated_entities: []
alias_or_role_evidence: ""
unknowns: []
source_refs: ["CH003"]
[[SECTION character_index_markdown]]
[[SECTION markdown]]
# Magpie
**Role:** Panicked bystander.

**Status:** Physically Present.

**Physical Description:** 
A magpie bird.

**Costume & Silhouette:** 
Bird silhouette; likely wet/draggled at the start.

**Descriptive Noun Phrases:** 
panicked magpie, fleeing magpie.

**Uncertainty Notes:** 
Specific plumage details are not provided.
[[/SECTION]]
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
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
direct_identity_evidence: "Canary"
direct_visual_evidence: "Flees the area when Dinah is mentioned."
costume_or_covering_evidence: ""
movement_evidence: "Flees/flies away."
associated_entities: []
alias_or_role_evidence: ""
unknowns: []
source_refs: ["CH003"]
[[SECTION character_index_markdown]]
[[SECTION markdown]]
# Canary
**Role:** Panicked bystander.

**Status:** Physically Present.

**Physical Description:** 
A canary bird.

**Costume & Silhouette:** 
Small bird silhouette; likely wet/draggled at the start.

**Descriptive Noun Phrases:** 
panicked canary, fleeing canary.

**Uncertainty Notes:** 
Specific color (e.g., yellow) is implied by species but not explicitly stated in text.
[[/SECTION]]
[[/SECTION]]
[[/FILMCREATOR_RECORD]]
[[/FILMCREATOR_PACKET]]
````
