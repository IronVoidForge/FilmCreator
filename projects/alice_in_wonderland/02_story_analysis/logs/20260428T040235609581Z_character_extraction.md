# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-28T04:02:35.610083+00:00
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

**Location:** A riverbank; a circular race-course area nearby.
**Characters:** 
- Alice (human girl)
- The Mouse (authoritative, prone to offense)
- The Lory (sulky, older bird)
- The Duck (literal-minded)
- The Dodo (solemn, leader of the Caucus-race)
- The Eaglet (skeptical/mocking bird)
- Various Birds (Magpie, Canary, etc.)
- Crabs (Old Crab and Young Crab)

**Events:**
1. **The Wet Assembly:** A group of animals and birds (draggled feathers, wet fur) assemble on a bank, visibly uncomfortable and wet. 
2. **Argument with Lory:** Alice engages in a verbal dispute with the Lory regarding its age; the Lory refuses to answer and becomes sulky.
3. **The Mouse's "Dry" History:** The Mouse calls for order. The group sits in a large ring with the Mouse in the center. The Mouse attempts to dry them by reciting a historical text about William the Conqueror. 
4. **Interruption/Confusion:** The Lory shivers at the text; the Duck interrupts, confused by the word "it"; Alice reports she is still wet.
5. **The Caucus-race Proposal:** The Dodo adjourns the meeting to propose a "Caucus-race" as a remedy for being wet. The Eaglet mocks the Dodo's vocabulary.
6. **The Race:** The Dodo marks out a circular course. The animals run in no specific order, starting and stopping at will for approximately thirty minutes until they are dry.
7. **Prize Distribution:** The Dodo declares everyone a winner. Alice is designated as the prize-giver. 
8. **Object Interaction (Comfits):** Alice retrieves a box of comfits from her pocket and distributes one to each participant. Large birds struggle to taste them; small birds choke/need patting on the back.
9. **Object Interaction (Thimble):** The Mouse insists Alice receives a prize. Alice produces a thimble. The Dodo leads the group in a formal presentation of the thimble back to Alice, which she accepts with a bow.
10. **The Mouse's Tale:** The group sits in a ring again. The Mouse begins telling a "long and sad tale." 
11. **Linguistic Misunderstanding:** Alice confuses the Mouse's "tale" (story) with its physical "tail." She interrupts the story to comment on the tail.
12. **The Conflict/Exit:** Alice attempts to help by offering to "undo a knot" in the story. The Mouse takes this as an insult and walks away from the group.
13. **Crab Argument:** As the Mouse leaves, an Old Crab scolds a Young Crab for losing its temper.
14. **The Dinah Reveal:** Alice mentions her cat, Dinah, expressing how good she is at catching birds.
15. **Mass Exit:** The mention of a cat causes panic. Birds (Magpie, Canary) use various excuses to flee the scene immediately. 
16. **Alice's Solitude:** Alice is left alone on the bank, feeling lonely and crying. She hears distant footsteps approaching.
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
direct_visual_evidence: "Alice is present and interacting with animals."
costume_or_covering_evidence: ""
movement_evidence: "Participates in the Caucus-race; bows to receive a thimble."
associated_entities: ["the_mouse", "the_lory", "the_duck", "the_dodo", "the_eaglet", "dinah"]
alias_or_role_evidence: ""
unknowns: []
source_refs: ["CH003"]
[[SECTION character_index_markdown]]
[[SECTION markdown]]
# Alice
**Role:** Protagonist; prize-giver for the Caucus-race.

**Status:** Physically present.

**Physical Description:** 
A human girl. Specific clothing or hair details are not provided in this chapter, though she is noted to be wet from the river.

**Costume & Silhouette:** 
Not explicitly detailed beyond being a "human girl."

**Descriptive Noun Phrases:** 
human girl, young girl, prize-giver.

**Uncertainty Notes:** 
Visual details regarding specific attire are absent in this chapter; relies on established series continuity for visual consistency.
[[/SECTION]]
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
asset_id: the_mouse
canonical_character_id: the_mouse
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
direct_identity_evidence: "The Mouse"
direct_visual_evidence: "Sits in the center of a ring; has a physical tail mentioned by Alice."
costume_or_covering_evidence: ""
movement_evidence: "Walks away from the group after being insulted."
associated_entities: ["alice"]
alias_or_role_evidence: ""
unknowns: []
source_refs: ["CH003"]
[[SECTION character_index_markdown]]
[[SECTION markdown]]
# The Mouse
**Role:** Authoritative figure; storyteller.

**Status:** Physically present.

**Physical Description:** 
A small animal (mouse) with a physical tail that Alice confuses for a "tale."

**Costume & Silhouette:** 
Not specified.

**Descriptive Noun Phrases:** 
small mouse, authoritative mouse, storyteller mouse.

**Uncertainty Notes:** 
Specific breed or color not mentioned.
[[/SECTION]]
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
asset_id: the_lory
canonical_character_id: the_lory
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
confidence: 0.9
direct_identity_evidence: "The Lory"
direct_visual_evidence: "An older bird; shivers at the text."
costume_or_covering_evidence: ""
movement_evidence: "Shivers; sulks during arguments."
associated_entities: []
alias_or_role_evidence: ""
unknowns: []
source_refs: ["CH003"]
[[SECTION character_index_markdown]]
[[SECTION markdown]]
# The Lory
**Role:** Sulky participant in the assembly.

**Status:** Physically present.

**Physical Description:** 
An older bird.

**Costume & Silhouette:** 
Likely has draggled/wet feathers due to the river incident.

**Descriptive Noun Phrases:** 
sulky lory, older bird, wet bird.

**Uncertainty Notes:** 
Specific color or species-specific markings are not detailed.
[[/SECTION]]
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
asset_id: the_duck
canonical_character_id: the_duck
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
confidence: 0.9
direct_identity_evidence: "The Duck"
direct_visual_evidence: "Interrupts the Mouse's recitation."
costume_or_covering_evidence: ""
movement_evidence: ""
associated_entities: []
alias_or_role_evidence: ""
unknowns: []
source_refs: ["CH003"]
[[SECTION character_index_markdown]]
[[SECTION markdown]]
# The Duck
**Role:** Literal-minded participant.

**Status:** Physically present.

**Physical Description:** 
A duck.

**Costume & Silhouette:** 
Likely has draggled/wet feathers.

**Descriptive Noun Phrases:** 
literal-minded duck, wet duck.

**Uncertainty Notes:** 
Specific color or breed not mentioned.
[[/SECTION]]
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
asset_id: the_dodo
canonical_character_id: the_dodo
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
direct_identity_evidence: "The Dodo"
direct_visual_evidence: "Leads the group in presenting a thimble; marks out the race course."
costume_or_covering_evidence: ""
movement_evidence: "Marks out a circular course; leads formal presentations."
associated_entities: ["alice"]
alias_or_role_evidence: ""
unknowns: []
source_refs: ["CH003"]
[[SECTION character_index_markdown]]
[[SECTION markdown]]
# The Dodo
**Role:** Solemn leader of the Caucus-race.

**Status:** Physically present.

**Physical Description:** 
A solemn bird (Dodo).

**Costume & Silhouette:** 
Likely has draggled/wet feathers.

**Descriptive Noun Phrases:** 
solemn dodo, race leader, formal dodo.

**Uncertainty Notes:** 
Specific visual details of the Dodo's appearance are not provided beyond its name and demeanor.
[[/SECTION]]
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
asset_id: the_eaglet
canonical_character_id: the_eaglet
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
confidence: 0.9
direct_identity_evidence: "The Eaglet"
direct_visual_evidence: "Mocks the Dodo's vocabulary."
costume_or_covering_evidence: ""
movement_evidence: ""
associated_entities: []
alias_or_role_evidence: ""
unknowns: []
source_refs: ["CH003"]
[[SECTION character_index_markdown]]
[[SECTION markdown]]
# The Eaglet
**Role:** Skeptical/mocking participant.

**Status:** Physically present.

**Physical Description:** 
A small bird (Eaglet).

**Costume & Silhouette:** 
Likely has draggled/wet feathers.

**Descriptive Noun Phrases:** 
skeptical eaglet, mocking bird.

**Uncertainty Notes:** 
Specific color or markings not mentioned.
[[/SECTION]]
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
asset_id: various_birds
canonical_character_id: various_birds
aliases: ["Magpie", "Canary"]
is_fully_identified: false
manual_description_required: true
manual_description_reason: "This is a group entity with varying species; individual visual consistency cannot be established from text alone."
clarification_required: true
clarification_reason: ""
clarification_question: "Should these birds be rendered as distinct individuals or a generic crowd of wet birds?"
character_type_hint: animal
morphology_hint: winged
scale_hint: small
renderability_hint: context_only
confidence: 0.7
direct_identity_evidence: "Various Birds (Magpie, Canary, etc.)"
direct_visual_evidence: "Flee the scene when Dinah is mentioned."
costume_or_covering_evidence: ""
movement_evidence: "Fleeing/flying away from the bank."
associated_entities: []
alias_or_role_evidence: ""
unknowns: ["Specific species counts", "Visual colors"]
source_refs: ["CH003"]
[[SECTION character_index_markdown]]
[[SECTION markdown]]
# Various Birds
**Role:** Participants in the assembly and race; flee at the mention of a cat.

**Status:** Physically present.

**Physical Description:** 
A collection of small birds, including Magpies and Canaries.

**Costume & Silhouette:** 
Draggled/wet feathers.

**Descriptive Noun Phrases:** 
panicked birds, wet birds, fleeing magpie, fleeing canary.

**Uncertainty Notes:** 
The exact composition of the group is unknown; they are treated as a collective mass that scatters.
[[/SECTION]]
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
asset_id: crabs
canonical_character_id: crabs
aliases: ["Old Crab", "Young Crab"]
is_fully_identified: false
manual_description_required: true
manual_description_reason: "Only identified by age/role; no physical description of morphology or color provided."
clarification_required: true
clarification_reason: ""
clarification_question: "Are these crabs humanoid in posture or standard crustacean-style?"
character_type_hint: animal
morphology_hint: multi_legged
scale_hint: small
renderability_hint: renderable
confidence: 0.6
direct_identity_evidence: "Old Crab and Young Crab"
direct_visual_evidence: "Engage in an argument as the Mouse leaves."
costume_or_covering_evidence: ""
movement_evidence: ""
associated_entities: []
alias_or_role_evidence: ""
unknowns: ["Color", "Size relative to birds", "Specific morphology"]
source_refs: ["CH003"]
[[SECTION character_index_markdown]]
[[SECTION markdown]]
# Crabs
**Role:** Observers/participants in the background.

**Status:** Physically present.

**Physical Description:** 
Crabs (one old, one young).

**Costume & Silhouette:** 
Not specified.

**Descriptive Noun Phrases:** 
old crab, young crab, arguing crabs.

**Uncertainty Notes:** 
No visual details provided regarding their appearance or how they interact with the environment (e.g., walking on sand vs. swimming).
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
confidence: 0.8
direct_identity_evidence: "Alice's cat, Dinah"
direct_visual_evidence: "Mentioned by Alice; causes birds to flee."
costume_or_covering_evidence: ""
movement_evidence: ""
associated_entities: ["alice"]
alias_or_role_evidence: ""
unknowns: []
source_refs: ["CH003"]
[[SECTION character_index_markdown]]
[[SECTION markdown]]
# Dinah
**Role:** Alice's cat (referenced).

**Status:** Referenced.

**Physical Description:** 
A cat capable of catching birds.

**Costume & Silhouette:** 
Not specified.

**Descriptive Noun Phrases:** 
Alice's cat, bird-catching cat.

**Uncertainty Notes:** 
The character is not physically present in the chapter; visual details are limited to her reputation as a hunter of birds.
[[/SECTION]]
[[/SECTION]]
[[/FILMCREATOR_RECORD]]
[[/FILMCREATOR_PACKET]]
````
