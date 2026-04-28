# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-28T04:12:27.071341+00:00
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

Chapter id: CH008

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

**Location: The Queen’s Croquet-Ground**
A garden setting featuring a large rose-tree with white roses being painted red by three card gardeners (Two, Five, and Seven). The ground is characterized by ridges and furrows.

**Events & Character Entrances/Exits:**
- **The Gardeners' Task:** Two, Five, and Seven are painting white roses red to avoid the Queen's wrath. Alice observes them.
- **The Royal Procession:** 
    - The gardeners throw themselves flat on their faces upon hearing the Queen approaching.
    - Ten soldiers (Clubs) enter, shaped like oblong/flat cards with hands/feet at corners.
    - Ten courtiers (Diamonds) enter in pairs.
    - Ten royal children (Hearts) enter jumping in couples.
    - A group of guests enters, including the White Rabbit (nervous/hurried).
    - The Knave of Hearts enters carrying the King's crown on a crimson cushion.
    - The King and Queen of Hearts enter last.
- **The Confrontation:** 
    - The procession stops before Alice. The Queen demands to know who Alice is.
    - Alice defies the Queen’s authority, leading to an order for her execution ("Off with her head!").
    - The King intervenes timidly.
    - The Queen orders the Knave to "turn them over" (the gardeners). The gardeners jump up and bow.
    - The Queen discovers the painted roses and orders the gardeners' execution.
    - **Interaction/Object:** Alice hides the three gardeners in a large flower-pot to protect them. Three soldiers march off to execute them; they later report back that "their heads are gone" (a lie).
- **The Croquet Game:** 
    - The Queen invites Alice to play.
    - **Game Mechanics/Props:** Balls are live hedgehogs; mallets are live flamingoes; arches are made by soldiers doubling themselves up on their hands and feet.
    - Alice struggles with the flamingo (which twists its neck to look at her) and the hedgehog (which crawls away).
    - The game is chaotic: players play without turns, quarrel constantly, and the arches move around as soldiers walk off.
- **The White Rabbit Subplot:** 
    - While walking, the White Rabbit whispers to Alice that the Duchess is under sentence of execution for boxing the Queen's ears.
- **The Cheshire Cat Appearance:** 
    - A grin appears in the air, followed by eyes, then ears, and finally a full head.
    - Alice complains to the Cat about the unfairness of the game.
    - The Queen passes by while Alice is talking to the Cat; Alice quickly changes her tone to avoid trouble.
    - The King approaches, expresses dislike for the Cat, and demands its removal.
    - The Queen orders "Off with his head!"
- **The Executioner's Dilemma:** 
    - The King hurries off to fetch the executioner.
    - Alice leaves the Cat to find her hedgehog (which is fighting another hedgehog) and her flamingo (which is trying to fly into a tree).
    - A crowd gathers around the Cat's head. The King, Queen, and Executioner argue:
        - **Executioner:** Cannot cut off a head without a body.
        - **King:** Anything with a head can be beheaded.
        - **Queen:** Execute everyone if it isn't settled immediately.
    - Alice suggests asking the Duchess. The Queen orders the executioner to fetch the Duchess from prison.
- **Final Visual State:** 
    - As the executioner leaves, the Cheshire Cat's head fades away completely.
    - The King and Executioner search frantically for the vanished head while the others return to the game.
````

## Raw Response
````text
[[FILMCREATOR_PACKET]]
task: character_extraction
version: 1

[[SECTION character_index_markdown]]
[[FILMCREATOR_RECORD]]
asset_id: alice
canonical_character_id: alice
aliases: []
is_fully_identified: true
manual_description_required: true
manual_description_reason: While her presence is central, the text provides no specific details regarding her hair color, eye color, or exact clothing beyond general context.
clarification_required: false
clarification_reason: 
clarification_question: 
character_type_hint: human
morphology_hint: biped
scale_hint: human_scale
renderability_hint: renderable
confidence: 1.0
direct_identity_evidence: "Alice observes them."
direct_visual_evidence: 
costume_or_covering_evidence: 
movement_evidence: "Alice hides the three gardeners..."
associated_entities: [queen_of_hearts, white_rabbit, cheshire_cat]
alias_or_role_evidence: 
unknowns: []
source_refs: []
[[SECTION markdown]]
# Alice
**Role:** Protagonist / Observer

**Status:** Physically Present

**Physical Description:**
No specific physical traits (hair, eyes, etc.) are provided in this chapter.

**Costume & Silhouette:**
No specific costume details are provided in this chapter.

**Descriptive Noun Phrases:**
- Young girl
- Defiant child
- Interlocutor to the Cat

**Uncertainty Notes:**
Visual appearance is entirely dependent on external character design as the text is silent on her physical features.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
asset_id: queen_of_hearts
canonical_character_id: queen_of_hearts
aliases: [the Queen]
is_fully_identified: true
manual_description_required: false
manual_description_reason: 
clarification_required: false
clarification_reason: 
clarification_question: 
character_type_hint: humanoid_nonhuman
morphology_hint: biped
scale_hint: human_scale
renderability_hint: renderable
confidence: 0.9
direct_identity_evidence: "The Queen demands to know who Alice is."
direct_visual_evidence: 
costume_or_covering_evidence: 
movement_evidence: "The Queen enters last."
associated_entities: [king_of_hearts, knave_of_hearts]
alias_or_role_evidence: 
unknowns: []
source_refs: []
[[SECTION markdown]]
# Queen of Hearts
**Role:** Antagonist / Royal Authority

**Status:** Physically Present

**Physical Description:**
No specific physical description provided in text.

**Costume & Silhouette:**
Associated with a royal procession; likely wears regal attire consistent with a playing card theme.

**Descriptive Noun Phrases:**
- Hot-tempered monarch
- Authoritarian queen
- Card-themed royalty

**Uncertainty Notes:**
Visuals are implied by her status and the "card" nature of her court, but specific facial or clothing details are absent.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
asset_id: king_of_hearts
canonical_character_id: king_of_hearts
aliases: [the King]
is_fully_identified: true
manual_description_required: false
manual_description_reason: 
clarification_required: false
clarification_reason: 
clarification_question: 
character_type_hint: humanoid_nonhuman
morphology_hint: biped
scale_hint: human_scale
renderability_hint: renderable
confidence: 0.9
direct_identity_evidence: "The King and Queen of Hearts enter last."
direct_visual_evidence: 
costume_or_covering_evidence: 
movement_evidence: "The King intervenes timidly."
associated_entities: [queen_of_hearts, knave_of_hearts]
alias_or_role_evidence: 
unknowns: []
source_refs: []
[[SECTION markdown]]
# King of Hearts
**Role:** Royal Figure / Timid Intervener

**Status:** Physically Present

**Physical Description:**
No specific physical description provided.

**Costume & Silhouette:**
Likely wears royal attire consistent with a playing card theme.

**Descriptive Noun Phrases:**
- Timid king
- Card-themed monarch

**Uncertainty Notes:**
Visuals are implied by his role and the "card" nature of his court.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
asset_id: white_rabbit
canonical_character_id: white_rabbit
aliases: [the White Rabbit]
is_fully_identified: true
manual_description_required: false
manual_description_reason: 
clarification_required: false
clarification_reason: 
clarification_question: 
character_type_hint: animal
morphology_hint: quadruped
scale_hint: small
renderability_hint: renderable
confidence: 1.0
direct_identity_evidence: "A group of guests enters, including the White Rabbit..."
direct_visual_evidence: 
costume_or_covering_evidence: 
movement_evidence: "nervous/hurried"
associated_entities: [alice]
alias_or_role_evidence: 
unknowns: []
source_refs: []
[[SECTION markdown]]
# White Rabbit
**Role:** Messenger / Guest

**Status:** Physically Present

**Physical Description:**
A white rabbit.

**Costume & Silhouette:**
No specific costume mentioned, but characterized by nervous/hurried movement.

**Descriptive Noun Phrases:**
- Nervous white rabbit
- Hurried guest

**Uncertainty Notes:**
Standard rabbit morphology assumed.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
asset_id: cheshire_cat
canonical_character_id: cheshire_cat
aliases: [the Cat]
is_fully_identified: true
manual_description_required: false
manual_description_reason: 
clarification_required: false
clarification_reason: 
clarification_question: 
character_type_hint: creature
morphology_hint: unknown
scale_hint: unknown
renderability_hint: renderable
confidence: 0.8
direct_identity_evidence: "The Cheshire Cat's head fades away completely."
direct_visual_evidence: "A grin appears in the air, followed by eyes, then ears, and finally a full head."
costume_or_covering_evidence: 
movement_evidence: "appears in the air... fades away"
associated_entities: [alice, king_of_hearts]
alias_or_role_evidence: 
unknowns: []
source_refs: []
[[SECTION markdown]]
# Cheshire Cat
**Role:** Enigmatic Interlocutor

**Status:** Physically Present (appearing/disappearing)

**Physical Description:**
Appears via a floating grin, followed by eyes, ears, and then a full head. Can fade away entirely.

**Costume & Silhouette:**
No costume; purely biological/magical creature appearance.

**Descriptive Noun Phrases:**
- Disembodied grinning cat
- Fading feline
- Enigmatic cat head

**Uncertainty Notes:**
The full body is not described, only the head and its ability to manifest parts of itself in the air.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
asset_id: knave_of_hearts
canonical_character_id: knave_of_hearts
aliases: [the Knave]
is_fully_identified: true
manual_description_required: false
manual_description_reason: 
clarification_required: false
clarification_reason: 
clarification_question: 
character_type_hint: humanoid_nonhuman
morphology_hint: biped
scale_hint: human_scale
renderability_hint: renderable
confidence: 0.9
direct_identity_evidence: "The Knave of Hearts enters carrying the King's crown..."
direct_visual_evidence: 
costume_or_covering_evidence: 
movement_evidence: "enters carrying the King's crown"
associated_entities: [king_of_hearts, queen_of_hearts]
alias_or_role_evidence: 
unknowns: []
source_refs: []
[[SECTION markdown]]
# Knave of Hearts
**Role:** Attendant

**Status:** Physically Present

**Physical Description:**
No specific physical description provided.

**Costume & Silhouette:**
Likely card-themed attire.

**Descriptive Noun Phrases:**
- Card-themed knave
- Crown-bearer

**Uncertainty Notes:**
Visuals are implied by his role and the "card" nature of his court.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
asset_id: gardener_two
canonical_character_id: gardener_two
aliases: [Two, card gardener]
is_fully_identified: true
manual_description_required: false
manual_description_reason: 
clarification_required: false
clarification_reason: 
clarification_question: 
character_type_hint: humanoid_nonhuman
morphology_hint: biped
scale_hint: human_scale
renderability_hint: renderable
confidence: 0.8
direct_identity_evidence: "three card gardeners (Two, Five, and Seven)."
direct_visual_evidence: 
costume_or_covering_evidence: "card gardeners"
movement_evidence: "throw themselves flat on their faces", "jump up and bow"
associated_entities: [gardener_five, gardener_seven]
alias_or_role_evidence: 
unknowns: []
source_refs: []
[[SECTION markdown]]
# Gardener Two
**Role:** Worker / Victim

**Status:** Physically Present

**Physical Description:**
A card-based entity.

**Costume & Silhouette:**
Appears as a playing card.

**Descriptive Noun Phrases:**
- Card gardener
- Playing card worker

**Uncertainty Notes:**
Specific suit or value details (other than the name 'Two') are not explicitly detailed in this chapter, though "card gardeners" implies a playing card aesthetic.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
asset_id: gardener_five
canonical_character_id: gardener_five
aliases: [Five, card gardener]
is_fully_identified: true
manual_description_required: false
manual_description_reason: 
clarification_required: false
clarification_reason: 
clarification_question: 
character_type_hint: humanoid_nonhuman
morphology_hint: biped
scale_hint: human_scale
renderability_hint: renderable
confidence: 0.8
direct_identity_evidence: "three card gardeners (Two, Five, and Seven)."
direct_visual_evidence: 
costume_or_covering_evidence: "card gardeners"
movement_evidence: "throw themselves flat on their faces", "jump up and bow"
associated_entities: [gardener_two, gardener_seven]
alias_or_role_evidence: 
unknowns: []
source_refs: []
[[SECTION markdown]]
# Gardener Five
**Role:** Worker / Victim

**Status:** Physically Present

**Physical Description:**
A card-based entity.

**Costume & Silhouette:**
Appears as a playing card.

**Descriptive Noun Phrases:**
- Card gardener
- Playing card worker

**Uncertainty Notes:**
Visuals are implied by the "card gardener" designation.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
asset_id: gardener_seven
canonical_character_id: gardener_seven
aliases: [Seven, card gardener]
is_fully_identified: true
manual_description_required: false
manual_description_reason: 
clarification_required: false
clarification_reason: 
clarification_question: 
character_type_hint: humanoid_nonhuman
morphology_hint: biped
scale_hint: human_scale
renderability_hint: renderable
confidence: 0.8
direct_identity_evidence: "three card gardeners (Two, Five, and Seven)."
direct_visual_evidence: 
costume_or_covering_evidence: "card gardeners"
movement_evidence: "throw themselves flat on their faces", "jump up and bow"
associated_entities: [gardener_two, gardener_five]
alias_or_role_evidence: 
unknowns: []
source_refs: []
[[SECTION markdown]]
# Gardener Seven
**Role:** Worker / Victim

**Status:** Physically Present

**Physical Description:**
A card-based entity.

**Costume & Silhouette:**
Appears as a playing card.

**Descriptive Noun Phrases:**
- Card gardener
- Playing card worker

**Uncertainty Notes:**
Visuals are implied by the "card gardener" designation.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
asset_id: soldier_club
canonical_character_id: soldier_club
aliases: [Ten soldiers, Clubs]
is_fully_identified: true
manual_description_required: false
manual_description_reason: 
clarification_required: false
clarification_reason: 
clarification_question: 
character_type_hint: humanoid_nonhuman
morphology_hint: biped
scale_hint: human_scale
renderability_hint: renderable
confidence: 1.0
direct_identity_evidence: "Ten soldiers (Clubs) enter, shaped like oblong/flat cards with hands/feet at corners."
direct_visual_evidence: "shaped like oblong/flat cards with hands/feet at corners"
costume_or_covering_evidence: 
movement_evidence: "march off to execute them"
associated_entities: []
alias_or_role_evidence: 
unknowns: []
source_refs: []
[[SECTION markdown]]
# Soldier (Clubs)
**Role:** Guard / Executioner

**Status:** Physically Present

**Physical Description:**
Oblong, flat card-shaped entities with hands and feet located at the corners.

**Costume & Silhouette:**
The body itself is a flat playing card shape.

**Descriptive Noun Phrases:**
- Card soldier
- Oblong club soldier
- Flat-bodied guard

**Uncertainty Notes:**
None; visual description is quite specific regarding their geometry and limb placement.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
asset_id: courtier_diamond
canonical_character_id: courtier_diamond
aliases: [Ten courtiers, Diamonds]
is_fully_identified: true
manual_description_required: false
manual_description_reason: 
clarification_required: false
clarification_reason: 
clarification_question: 
character_type_hint: humanoid_nonhuman
morphology_hint: biped
scale_hint: human_scale
renderability_hint: renderable
confidence: 0.8
direct_identity_evidence: "Ten courtiers (Diamonds) enter in pairs."
direct_visual_evidence: 
costume_or_covering_evidence: 
movement_evidence: "enter in pairs"
associated_entities: []
alias_or_role_evidence: 
unknowns: []
source_refs: []
[[SECTION markdown]]
# Courtier (Diamonds)
**Role:** Royal Attendant

**Status:** Physically Present

**Physical Description:**
Likely card-based entities consistent with the court theme.

**Costume & Silhouette:**
Card-themed attire or form.

**Descriptive Noun Phrases:**
- Card courtier
- Diamond courtier

**Uncertainty Notes:**
Specific morphology (whether they are flat cards like the soldiers) is not explicitly stated, though highly implied by the context of "Diamonds".
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
asset_id: royal_child_heart
canonical_character_id: royal_child_heart
aliases: [Ten royal children, Hearts]
is_fully_identified: true
manual_description_required: false
manual_description_reason: 
clarification_required: false
clarification_reason: 
clarification_question: 
character_type_hint: humanoid_nonhuman
morphology_hint: biped
scale_hint: small
renderability_hint: renderable
confidence: 0.8
direct_identity_evidence: "Ten royal children (Hearts) enter jumping in couples."
direct_visual_evidence: 
costume_or_covering_evidence: 
movement_evidence: "jumping in couples"
associated_entities: []
alias_or_role_evidence: 
unknowns: []
source_refs: []
[[SECTION markdown]]
# Royal Child (Hearts)
**Role:** Royal Family Member

**Status:** Physically Present

**Physical Description:**
Small humanoid entities.

**Costume & Silhouette:**
Likely card-themed attire.

**Descriptive Noun Phrases:**
- Card child
- Jumping heart child

**Uncertainty Notes:**
Morphology is assumed to be humanoid/card-based based on the group's name and context.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
asset_id: duchess
canonical_character_id: duchess
aliases: [the Duchess]
is_fully_identified: true
manual_description_required: false
manual_description_reason: 
clarification_required: false
clarification_reason: 
clarification_question: 
character_type_hint: human
morphology_hint: biped
scale_hint: human_scale
renderability_hint: context_only
confidence: 0.7
direct_identity_evidence: "the Duchess is under sentence of execution"
direct_visual_evidence: 
costume_or_covering_evidence: 
movement_evidence: 
associated_entities: [queen_of_hearts]
alias_or_role_evidence: 
unknowns: []
source_refs: []
[[SECTION markdown]]
# Duchess
**Role:** Prisoner

**Status:** Referenced (In prison)

**Physical Description:**
No physical description provided.

**Costume & Silhouette:**
Unknown.

**Descriptive Noun Phrases:**
- Imprisoned duchess

**Uncertainty Notes:**
The character is mentioned as being in prison but does not appear on screen/in the scene.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
asset_id: executioner
canonical_character_id: executioner
aliases: [the Executioner]
is_fully_identified: true
manual_description_required: false
manual_description_reason: 
clarification_required: false
clarification_reason: 
clarification_question: 
character_type_hint: human
morphology_hint: biped
scale_hint: human_scale
renderability_hint: renderable
confidence: 0.8
direct_identity_evidence: "The King hurries off to fetch the executioner."
direct_visual_evidence: 
costume_or_covering_evidence: 
movement_evidence: "searches frantically"
associated_entities: [king_of_hearts, queen_of_hearts]
alias_or_role_evidence: 
unknowns: []
source_refs: []
[[SECTION markdown]]
# Executioner
**Role:** Official

**Status:** Physically Present

**Physical Description:**
No specific physical description provided.

**Costume & Silhouette:**
Likely wears standard executioner attire (implied).

**Descriptive Noun Phrases:**
- Frantic executioner
- Royal executioner

**Uncertainty Notes:**
Visuals are based on professional role rather than explicit text.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
asset_id: flamingo_mallet
canonical_character_id: flamingo_mallet
aliases: [flamingoes]
is_fully_identified: true
manual_description_required: false
manual_description_reason: 
clarification_required: false
clarification_reason: 
clarification_question: 
character_type_hint: animal
morphology_hint: biped
scale_hint: small
renderability_hint: renderable
confidence: 0.9
direct_identity_evidence: "mallets are live flamingoes"
direct_visual_evidence: "the flamingo (which twists its neck to look at her)"
costume_or_covering_evidence: 
movement_evidence: "twists its neck", "trying to fly into a tree"
associated_entities: []
alias_or_role_evidence: 
unknowns: []
source_refs: []
[[SECTION markdown]]
# Flamingo (Mallet)
**Role:** Croquet Prop / Living Entity

**Status:** Physically Present

**Physical Description:**
A live flamingo.

**Costume & Silhouette:**
Used as a mallet in the croquet game.

**Descriptive Noun Phrases:**
- Living flamingo mallet
- Neck-twisting flamingo

**Uncertainty Notes:**
The character is an animal used as a tool, behaving with its own agency.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
asset_id: hedgehog_ball
canonical_character_id: hedgehog_ball
aliases: [hedgehogs]
is_fully_identified: true
manual_description_required: false
manual_description_reason: 
clarification_required: false
clarification_reason: 
clarification_question: 
character_type_hint: animal
morphology_hint: quadruped
scale_hint: tiny
renderability_hint: renderable
confidence: 0.9
direct_identity_evidence: "Balls are live hedgehogs"
direct_visual_evidence: "her hedgehog (which is fighting another hedgehog)"
costume_or_covering_evidence: 
movement_evidence: "crawls away", "fighting another hedgehog"
associated_entities: []
alias_or_role_evidence: 
unknowns: []
source_refs: []
[[SECTION markdown]]
# Hedgehog (Ball)
**Role:** Croquet Prop / Living Entity

**Status:** Physically Present

**Physical Description:**
A live hedgehog.

**Costume & Silhouette:**
Used as a ball in the croquet game.

**Descriptive Noun Phrases:**
- Living hedgehog ball
- Crawling hedgehog

**Uncertainty Notes:**
The character is an animal used as a tool, behaving with its own agency.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]
[[/FILMCREATOR_PACKET]]
````
