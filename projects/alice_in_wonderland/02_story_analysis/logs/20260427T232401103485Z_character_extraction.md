# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-27T23:24:01.103485+00:00
- task: character_extraction

## System Prompt
````text
You are FilmCreator's chapter analysis engine.
Return only FilmCreator packets with the requested sections and records.
Do not wrap the packet in code fences unless explicitly requested.
Do not produce JSON-only responses.
If a packet asks for markdown sections, emit the section name on its own line and wrap the body in [[SECTION ...]] ... [[/SECTION]].
Do not put another [[SECTION ...]] tag inside a section body.
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



Output format:

[[FILMCREATOR_PACKET]]

task: character_extraction

version: 1

character_index_markdown:

[[SECTION character_index_markdown]]

...index markdown...

[[/SECTION]]



[[FILMCREATOR_RECORD]]

type: character

asset_id: protagonist

canonical_character_id: CH002 Protagonist

aliases: Narrator, Conscious Entity

is_fully_identified: false

manual_description_required: true

manual_description_reason: Sparse physical detail.

clarification_required: true

clarification_reason: Needs identity clarification.

clarification_question: What is the protagonist's physical form and origin?

character_type_hint: unknown

morphology_hint: unknown

scale_hint: unknown

renderability_hint: unknown

confidence: 0.3



[[SECTION markdown]]

# Protagonist

Short, grounded character markdown.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]



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

**Location:** A riverbank; the ground is wet.
**Characters:** 
- Alice (Human girl)
- The Mouse (An authoritative figure)
- The Lory (A sulky bird)
- The Duck (Questioning and skeptical)
- The Eaglet (Young, mocking bird)
- The Dodo (Solemn leader/organizer)
- Various Birds (Magpie, Canary, etc.)
- Various Animals (Crab, Young Crab, Oyster mentioned)

**Events:**
- **The Wet Assembly:** A group of birds and animals sit on the bank, dripping wet and uncomfortable. Alice engages in a verbal argument with the Lory regarding its age.
- **The Mouse's History Lesson:** The Mouse calls for order and attempts to dry the group by reciting a "dry" history about William the Conqueror. 
    - Interaction: The Lory shivers at the story; the Duck questions the meaning of "it"; Alice reports she is still wet.
    - Conflict: The Eaglet mocks the Dodo's long words.
- **The Caucus-Race:** The Dodo proposes a "Caucus-race" to get dry. 
    - Action: The Dodo marks a circular course. The animals run in a disorganized fashion, starting and stopping at will for thirty minutes until they are dry.
    - Resolution: The Dodo declares the race over. After a period of silent contemplation (the "Shakespearean" pose), the Dodo declares that everyone has won and must receive prizes.
- **The Prize Ceremony:** 
    - Alice retrieves a box of comfits from her pocket and distributes them to the group.
    - The Mouse insists Alice needs a prize. The Dodo takes a thimble from Alice's pocket.
    - The party presents the thimble to Alice with a formal speech; Alice bows and accepts it solemnly.
- **The Tale/Tail Confusion:** The group sits in a ring to eat comfits (causing choking/noise). Alice asks the Mouse to finish his "tale" (story), but she is distracted by the physical appearance of the Mouse's "tail."
    - Conflict: The Mouse becomes angry at Alice's perceived lack of attention. Alice tries to "undo a knot" in the story, which the Mouse perceives as an insult.
    - Exit: The Mouse walks away in a huff.
- **The Dinah Reveal:** As the Mouse leaves, the Lory and Crabs discuss temperaments. Alice mentions her pet cat, Dinah, who is excellent at catching mice.
    - Reaction: This causes a panic among the birds. A Magpie and a Canary use excuses to flee the area to avoid the "mouse-eating" threat.
- **The Lonely Conclusion:** Alice is left alone on the bank, crying because she misses Dinah. She hears footsteps in the distance and looks up hopefully.
````

## Raw Response
````text

````
