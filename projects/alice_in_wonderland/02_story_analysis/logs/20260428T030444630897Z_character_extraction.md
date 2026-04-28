# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-28T03:04:44.630897+00:00
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
[[SECTION character_index_markdown]]
[[markdown]]
# Character Index - Chapter 003

## Alice
- [Alice](alice)

## Animals & Birds
- [Mouse](mouse)
- [Dodo](dodo)
- [Lory](lory)
- [Duck](duck)
- [Eaglet](eaglet)
- [Magpie](magpie)
- [Canary](canary)
- [Old Crab](old_crab)
- [Young Crab](young_crab)

## Referenced Characters
- [Dinah](dinah)
[[/SECTION]]
[[/FILMCREATOR_PACKET]]

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
morphology_hint: girl
scale_hint: human
renderability_hint: high
confidence: 1.0
direct_identity_evidence: "Directly named as Alice."
direct_visual_evidence: "Physically present throughout the chapter."
costume_or_covering_evidence: "Not explicitly described in this chapter, but carries a box of comfits and a thimble."
movement_evidence: "Engages in argument, bows to receive a gift, cries on the riverbank."
associated_entities: ["mouse", "dodo", "lory", "dinah"]
alias_or_role_evidence: ""
unknowns: []
source_refs: "Alice engages in an argument with the Lory; Alice is designated as the prize-giver; Alice produces a thimble; Alice mentions her cat, Dinah."
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
morphology_hint: rodent
scale_hint: small
renderability_hint: high
confidence: 1.0
direct_identity_evidence: "Directly named as Mouse."
direct_visual_evidence: "Physically present; recites a story; has a tail mentioned in a pun."
costume_or_covering_evidence: ""
movement_evidence: "Walks away angrily after being insulted."
associated_entities: ["alice", "dodo"]
alias_or_role_evidence: "Attempts to dry the group by reciting history; tells a 'long and sad tale'."
unknowns: []
source_refs: "The Mouse calls for order... attempts to dry everyone by reciting a historical text... The Mouse begins telling a 'long and sad tale'."
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
morphology_hint: bird-like/dodo
scale_hint: medium
renderability_hint: high
confidence: 1.0
direct_identity_evidence: "Directly named as Dodo."
direct_visual_evidence: "Physically present; leads the Caucus-race and the presentation of the thimble."
costume_or_covering_evidence: ""
movement_evidence: "Marks out a circular course; leads the group in formal presentation."
associated_entities: ["alice", "mouse"]
alias_or_role_evidence: "Leader of the Caucus-race; solemn character."
unknowns: []
source_refs: "Dodo (solemn, leader of the Caucus-race)... The Dodo declares everyone a winner... The Dodo leads the group in a formal presentation."
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
morphology_hint: bird
scale_hint: medium
renderability_hint: high
confidence: 1.0
direct_identity_evidence: "Directly named as Lory."
direct_visual_evidence: "Physically present; engages in argument with Alice."
costume_or_covering_evidence: ""
movement_evidence: "Part of the wet gathering on the bank."
associated_entities: ["alice"]
alias_or_role_evidence: "Sulky, older than Alice."
unknowns: []
source_refs: "Alice engages in a long argument with the Lory regarding its age; the Lory refuses to answer and becomes sulky."
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
morphology_hint: waterfowl
scale_hint: medium
renderability_hint: high
confidence: 1.0
direct_identity_evidence: "Directly named as Duck."
direct_visual_evidence: "Physically present; interrupts the Mouse."
costume_or_covering_evidence: ""
movement_evidence: "Part of the wet gathering."
associated_entities: ["mouse"]
alias_or_role_evidence: "Literal-minded."
unknowns: []
source_refs: "The Duck interrupts the Mouse, misunderstanding the word 'it'."
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
morphology_hint: bird/eaglet
scale_hint: small
renderability_hint: high
confidence: 1.0
direct_identity_evidence: "Directly named as Eaglet."
direct_visual_evidence: "Physically present; mocks the Dodo."
costume_or_covering_evidence: ""
movement_evidence: "Part of the wet gathering."
associated_entities: ["dodo"]
alias_or_role_evidence: "Skeptical, mocking."
unknowns: []
source_refs: "The Eaglet mocks the Dodo’s vocabulary."
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
morphology_hint: bird/magpie
scale_hint: small
renderability_hint: high
confidence: 1.0
direct_identity_evidence: "Directly named as Magpie."
direct_visual_evidence: "Physically present; flees the area."
costume_or_covering_evidence: ""
movement_evidence: "Flees the area when Alice mentions Dinah."
associated_entities: ["alice"]
alias_or_role_evidence: ""
unknowns: []
source_refs: "Birds (Magpie, Canary) use various excuses to flee the area immediately [after mention of Dinah]."
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
morphology_hint: bird/canary
scale_hint: small
renderability_hint: high
confidence: 1.0
direct_identity_evidence: "Directly named as Canary."
direct_visual_evidence: "Physically present; flees the area."
costume_or_covering_evidence: ""
movement_evidence: "Flees the area when Alice mentions Dinah."
associated_entities: ["alice"]
alias_or_role_evidence: ""
unknowns: []
source_refs: "Birds (Magpie, Canary) use various excuses to flee the area immediately [after mention of Dinah]."
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
morphology_hint: crab
scale_hint: small
renderability_hint: high
confidence: 1.0
direct_identity_evidence: "Directly named as Old Crab."
direct_visual_evidence: "Physically present; scolds Young Crab."
costume_or_covering_evidence: ""
movement_evidence: "Part of the gathering on the bank."
associated_entities: ["young_crab"]
alias_or_role_evidence: ""
unknowns: []
source_refs: "An Old Crab scolds a Young Crab for losing her temper."
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
morphology_hint: crab
scale_hint: small
renderability_hint: high
confidence: 1.0
direct_identity_evidence: "Directly named as Young Crab."
direct_visual_evidence: "Physically present; loses temper."
costume_or_covering_evidence: ""
movement_evidence: "Part of the gathering on the bank."
associated_entities: ["old_crab"]
alias_or_role_evidence: ""
unknowns: []
source_refs: "An Old Crab scolds a Young Crab for losing her temper."
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
morphology_hint: cat
scale_hint: medium
renderability_hint: low
confidence: 1.0
direct_identity_evidence: "Directly named as Dinah."
direct_visual_evidence: "Not physically present; only referenced by Alice."
costume_or_covering_evidence: ""
movement_evidence: ""
associated_entities: ["alice"]
alias_or_role_evidence: "Alice's cat who catches mice and birds."
unknowns: []
source_refs: "Alice mentions her cat, Dinah, and how she catches mice/birds."
[[/FILMCREATOR_RECORD]]
[[/FILMCREATOR_RECORD]]
````
