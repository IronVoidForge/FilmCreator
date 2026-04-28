# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-28T03:32:52.249957+00:00
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
- Alice (Human girl)
- Mouse (Authority figure, storyteller)
- Dodo (Leader of the Caucus-race)
- Lory (Sulky bird)
- Duck (Literal-minded bird)
- Eaglet (Mocking bird)
- Various Birds/Animals: Magpie, Canary, Old Crab, Young Crab, and others.

**Events:**
1. **The Wet Assembly:** A group of animals and birds (draggled feathers, wet fur) assemble on a bank, visibly uncomfortable and cross due to being wet. 
2. **Argument with Lory:** Alice engages in a verbal dispute with the Lory regarding its age; the Lory becomes sulky and refuses to answer.
3. **The Mouse's "Dry" Story:** The Mouse calls for order and attempts to dry everyone by reciting a historical text about William the Conqueror. 
4. **Interruption/Confusion:** The Duck interrupts the Mouse, misunderstanding the word "it." Alice reports she is still wet.
5. **The Caucus-race Proposal:** The Dodo moves to adjourn the meeting for more "energetic remedies," proposing a Caucus-race. The Eaglet mocks the Dodo's vocabulary.
6. **The Race:** The Dodo marks a circular course. The animals run in no specific order, starting and stopping at will for approximately thirty minutes until they are dry.
7. **Prize Distribution:** The Dodo declares everyone a winner. Alice is designated as the prize-giver. 
8. **Object Interaction (Comfits):** Alice retrieves a box of comfits from her pocket and distributes them to the group. Large birds struggle to taste theirs; small ones choke.
9. **Object Interaction (Thimble):** The Mouse insists Alice receives a prize. Alice produces a thimble from her pocket. The Dodo presents it back to her as an "elegant thimble" in a formal ceremony. Alice bows and accepts it.
10. **The Mouse's Tale:** The group settles into a ring. The Mouse begins a "long and sad tale." 
11. **Linguistic Misunderstanding:** Alice confuses the Mouse's "tale" (story) with its physical "tail." She attempts to help by offering to undo a "knot" she thinks she sees in the story/tail.
12. **The Mouse Exits:** Offended by Alice's perceived nonsense, the Mouse growls and walks away from the group.
13. **Crab Argument:** An Old Crab lectures a Young Crab on temper; they bicker briefly.
14. **The Dinah Reveal:** Alice mentions her cat, Dinah, and how she catches mice/birds. 
15. **Mass Exit:** The mention of the cat causes panic. Birds (Magpie, Canary) use various excuses to flee the area immediately.
16. **Alice's Solitude:** Alice is left alone on the bank, feeling lonely and crying. She hears distant footsteps and looks up expectantly.
````

## Raw Response
````text
[[FILMCREATOR_PACKET]]
[[SECTION character_index_markdown]]
# Character Index: CH003

- [Alice](#alice)
- [Mouse](#mouse)
- [Dodo](#dodo)
- [Lory](#lory)
- [Duck](#duck)
- [Eaglet](#eaglet)
- [Old Crab](#old_crab)
- [Young Crab](#young_crab)
- [Magpie](#magpie)
- [Canary](#canary)
- [Dinah](#dinah)

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
scale_hint: human_scale
renderability_hint: renderable
confidence: 1.0
direct_identity_evidence: "Explicitly named as Alice."
direct_visual_evidence: "Physically present in the scene."
costume_or_covering_evidence: "Carries a box of comfits and a thimble in her pockets."
movement_evidence: "Engages in verbal disputes, distributes prizes, bows to the Dodo, cries at the end."
associated_entities: ["mouse", "dodo", "lory", "duck", "eaglet", "dinah"]
alias_or_role_evidence: ""
unknowns: []
source_refs: "Alice is a human girl who interacts with the animals and distributes prizes."
[[SECTION markdown]]
# Alice
**Role:** Protagonist / Prize-giver

**Status:** Physically Present

**Description:**
A human girl. While specific clothing details are not provided in this chapter, she carries small items like comfits and a thimble in her pockets. She is capable of bowing formally and experiences emotional shifts from engagement to loneliness/crying.

**Prompt Phrases:**
human girl, young girl, holding a thimble, distributing comfits, crying on a riverbank.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: mouse
canonical_character_id: mouse
aliases: []
is_fully_identified: true
manual_description_required: true
manual_description_reason: "The text describes the Mouse's behavior and 'tail', but lacks specific physical descriptors like color, fur texture, or size relative to Alice beyond being an animal."
clarification_required: false
clarification_reason: ""
clarification_question: ""
character_type_hint: animal
morphology_hint: quadruped
scale_hint: small
renderability_hint: renderable
confidence: 0.9
direct_identity_evidence: "Explicitly named as the Mouse."
direct_visual_evidence: "Physically present; has a tail that Alice mistakes for having a knot."
costume_or_covering_evidence: ""
movement_evidence: "Recites stories, growls, walks away from the group."
associated_entities: ["alice", "dinah"]
alias_or_role_evidence: "Authority figure/storyteller."
unknowns: ["specific fur color", "exact size"]
source_refs: "The Mouse attempts to dry the group with a story and is offended by Alice's comment about its tail."
[[SECTION markdown]]
# Mouse
**Role:** Authority figure, Storyteller

**Status:** Physically Present

**Description:**
A small animal (mouse) with a tail. The mouse acts as an authority figure during the assembly and attempts to lead the group through recitation. It is sensitive to perceived insults regarding its "tale" vs "tail."

**Uncertainty Notes:**
Specific physical appearance (color, breed, texture) is not detailed in the text.

**Prompt Phrases:**
small mouse, animal with a long tail, authoritative small animal, wet fur.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: dodo
canonical_character_id: dodo
aliases: []
is_fully_identified: true
manual_description_required: true
manual_description_reason: "No specific visual description of the Dodo's appearance (color, size, plumage) is provided."
clarification_required: false
clarification_reason: ""
clarification_question: ""
character_type_hint: animal
morphology_hint: biped
scale_hint: unknown
renderability_hint: renderable
confidence: 0.8
direct_identity_evidence: "Explicitly named as the Dodo."
direct_visual_evidence: "Physically present; leads the Caucus-race and presents a thimble."
costume_or_covering_evidence: ""
movement_evidence: "Marks out a circular course, moves to adjourn meetings, presents prizes formally."
associated_entities: ["alice", "eaglet"]
alias_or_role_evidence: "Leader of the Caucus-race."
unknowns: ["scale relative to Alice", "visual appearance"]
source_refs: "The Dodo organizes the race and conducts a formal ceremony for Alice."
[[SECTION markdown]]
# Dodo
**Role:** Leader of the Caucus-race

**Status:** Physically Present

**Description:**
A bird (Dodo) that acts as a leader. It is capable of formal gestures, such as presenting an "elegant thimble" to Alice in a ceremony.

**Uncertainty Notes:**
Visual details regarding size and plumage are absent.

**Prompt Phrases:**
dodo bird, large flightless bird, ceremonial bird, leading a race.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: lory
canonical_character_id: lory
aliases: []
is_fully_identified: true
manual_description_required: true
manual_description_reason: "Only described as a 'sulky bird'; no visual details provided."
clarification_required: false
clarification_reason: ""
clarification_question: ""
character_type_hint: animal
morphology_hint: winged
scale_hint: small
renderability_hint: renderable
confidence: 0.7
direct_identity_evidence: "Explicitly named as the Lory."
direct_visual_evidence: "Physically present; engages in an argument with Alice."
costume_or_covering_evidence: ""
movement_evidence: "Becomes sulky and refuses to answer questions."
associated_entities: []
alias_or_role_evidence: ""
unknowns: ["color", "species-specific features"]
source_refs: "The Lory is a bird that argues with Alice about its age."
[[SECTION markdown]]
# Lory
**Role:** Sulky participant

**Status:** Physically Present

**Description:**
A bird characterized by its sulky temperament. It engages in verbal disputes with Alice.

**Uncertainty Notes:**
No physical description of color or shape is provided.

**Prompt Phrases:**
sulky bird, grumpy bird, small bird.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: duck
canonical_character_id: duck
aliases: []
is_fully_identified: true
manual_description_required: true
manual_description_reason: "No visual description provided beyond the name."
clarification_required: false
clarification_reason: ""
clarification_question: ""
character_type_hint: animal
morphology_hint: winged
scale_hint: small
renderability_hint: renderable
confidence: 0.7
direct_identity_evidence: "Explicitly named as the Duck."
direct_visual_evidence: "Physically present; interrupts the Mouse."
costume_or_covering_evidence: ""
movement_evidence: "Interrupts speech with a misunderstanding."
associated_entities: []
alias_or_role_evidence: ""
unknowns: ["color", "size"]
source_refs: "The Duck is a literal-minded bird that interrupts the Mouse's story."
[[SECTION markdown]]
# Duck
**Role:** Interrupter

**Status:** Physically Present

**Description:**
A bird (Duck) described as being literal-minded. It interrupts the Mouse during its recitation.

**Uncertainty Notes:**
Visual appearance is not specified.

**Prompt Phrases:**
duck, literal-minded bird, wet feathers.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: eaglet
canonical_character_id: eaglet
aliases: []
is_fully_identified: true
manual_description_required: true
manual_description_reason: "No visual description provided."
clarification_required: false
clarification_reason: ""
clarification_question: ""
character_type_hint: animal
morphology_hint: winged
scale_hint: tiny
renderability_hint: renderable
confidence: 0.7
direct_identity_evidence: "Explicitly named as the Eaglet."
direct_visual_evidence: "Physically present; mocks the Dodo."
costume_or_covering_evidence: ""
movement_evidence: "Mocks the Dodo's vocabulary."
associated_entities: ["dodo"]
alias_or_role_evidence: ""
unknowns: ["color", "size details"]
source_refs: "The Eaglet mocks the Dodo's use of words."
[[SECTION markdown]]
# Eaglet
**Role:** Mocking participant

**Status:** Physically Present

**Description:**
A small bird (Eaglet) that exhibits a mocking attitude toward the Dodo.

**Uncertainty Notes:**
No physical description provided.

**Prompt Phrases:**
small eaglet, mocking bird, tiny bird.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: old_crab
canonical_character_id: old_crab
aliases: []
is_fully_identified: true
manual_description_required: true
manual_description_reason: "No visual description provided."
clarification_required: false
clarification_reason: ""
clarification_question: ""
character_type_hint: animal
morphology_hint: multi_legged
scale_hint: small
renderability_hint: renderable
confidence: 0.6
direct_identity_evidence: "Explicitly named as the Old Crab."
direct_visual_evidence: "Physically present; lectures a Young Crab."
costume_or_covering_evidence: ""
movement_evidence: "Lectures/bickers with another crab."
associated_entities: ["young_crab"]
alias_or_role_evidence: ""
unknowns: ["color", "size"]
source_refs: "The Old Crab argues with the Young Crab about temper."
[[SECTION markdown]]
# Old Crab
**Role:** Lecturer/Bickerer

**Status:** Physically Present

**Description:**
A crab that engages in a lecture/argument regarding temper.

**Uncertainty Notes:**
No visual details provided.

**Prompt Phrases:**
old crab, crustacean, bickering crab.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: young_crab
canonical_character_id: young_crab
aliases: []
is_fully_identified: true
manual_description_required: true
manual_description_reason: "No visual description provided."
clarification_required: false
clarification_reason: ""
clarification_question: ""
character_type_hint: animal
morphology_hint: multi_legged
scale_hint: small
renderability_hint: renderable
confidence: 0.6
direct_identity_evidence: "Explicitly named as the Young Crab."
direct_visual_evidence: "Physically present; bickers with the Old Crab."
costume_or_covering_evidence: ""
movement_evidence: "Bickers/argues."
associated_entities: ["old_crab"]
alias_or_role_evidence: ""
unknowns: ["color", "size"]
source_refs: "The Young Crab is lectured by the Old Crab."
[[SECTION markdown]]
# Young Crab
**Role:** Bickerer

**Status:** Physically Present

**Description:**
A crab that engages in a brief argument with an older crab.

**Uncertainty Notes:**
No visual details provided.

**Prompt Phrases:**
young crab, small crustacean, bickering crab.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: magpie
canonical_character_id: magpie
aliases: []
is_fully_identified: true
manual_description_required: true
manual_description_reason: "No specific visual description provided in the text."
clarification_required: false
clarification_reason: ""
clarification_question: ""
character_type_hint: animal
morphology_hint: winged
scale_hint: small
renderability_hint: renderable
confidence: 0.7
direct_identity_evidence: "Explicitly named as the Magpie."
direct_visual_evidence: "Physically present; flees when Dinah is mentioned."
costume_or_covering_evidence: ""
movement_evidence: "Flees the area immediately."
associated_entities: ["dinah"]
alias_or_role_evidence: ""
unknowns: []
source_refs: "The Magpie is one of the birds that panics at the mention of Alice's cat."
[[SECTION markdown]]
# Magpie
**Role:** Panicked participant

**Status:** Physically Present

**Description:**
A bird (Magpie) that flees in terror upon hearing about Alice's cat.

**Uncertainty Notes:**
No specific color or plumage details are provided.

**Prompt Phrases:**
magpie, black and white bird, fleeing bird.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: canary
canonical_character_id: canary
aliases: []
is_fully_identified: true
manual_description_required: true
manual_description_reason: "No specific visual description provided in the text."
clarification_required: false
clarification_reason: ""
clarification_question: ""
character_type_hint: animal
morphology_hint: winged
scale_hint: tiny
renderability_hint: renderable
confidence: 0.7
direct_identity_evidence: "Explicitly named as the Canary."
direct_visual_evidence: "Physically present; flees when Dinah is mentioned."
costume_or_covering_evidence: ""
movement_evidence: "Flees the area immediately."
associated_entities: ["dinah"]
alias_or_role_evidence: ""
unknowns: []
source_refs: "The Canary is one of the birds that panics at the mention of Alice's cat."
[[SECTION markdown]]
# Canary
**Role:** Panicked participant

**Status:** Physically Present

**Description:**
A small bird (Canary) that flees in terror upon hearing about Alice's cat.

**Uncertainty Notes:**
No specific color or plumage details are provided beyond the name implying yellow.

**Prompt Phrases:**
canary, small yellow bird, fleeing bird.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: dinah
canonical_character_id: dinah
aliases: []
is_fully_identified: true
manual_description_required: true
manual_description_reason: "The cat is only mentioned by name; no physical description is provided."
clarification_required: false
clarification_reason: ""
clarification_question: ""
character_type_hint: animal
morphology_hint: quadruped
scale_hint: small
renderability_hint: context_only
confidence: 0.8
direct_identity_evidence: "Explicitly named as Dinah."
direct_visual_evidence: "Not visually present; only referenced by Alice."
costume_or_covering_evidence: ""
movement_evidence: ""
associated_entities: ["alice"]
alias_or_role_evidence: "Alice's cat."
unknowns: ["color", "breed", "appearance"]
source_refs: "Alice mentions Dinah catches mice and birds, causing the assembly to flee."
[[SECTION markdown]]
# Dinah
**Role:** Referenced Predator

**Status:** Referenced (Not Present)

**Description:**
Alice's cat. The mere mention of her name causes a mass exodus of the animals present.

**Uncertainty Notes:**
No physical description is provided in this chapter.

**Prompt Phrases:**
cat, predator, domestic cat.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
