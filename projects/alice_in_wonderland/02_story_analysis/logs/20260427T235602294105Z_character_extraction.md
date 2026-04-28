# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-27T23:56:02.294105+00:00
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

Chapter id: CH008

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

**Setting:** The Queen’s Croquet-Ground; a garden featuring a large rose-tree with white roses being painted red by three gardeners (Two, Five, and Seven).

**Events & Character Interactions:**
*   **The Painting Incident:** Gardeners Two, Five, and Seven are painting white roses red to hide a mistake from the Queen. Alice observes them; they bow when she approaches. Two explains the situation before being interrupted by the arrival of the royal procession.
*   **The Procession:** A grand parade passes: 10 soldiers (clubs), 10 courtiers (diamonds), 10 royal children (hearts), a group of guests including the White Rabbit, the Knave of Hearts (carrying the crown), and finally the King and Queen of Hearts.
*   **The Confrontation:** The Queen questions Alice's presence/identity. Alice, feeling brave because they are "only a pack of cards," answers back to the Queen. This causes the Queen to order the gardeners' execution. 
*   **The Escape:** Alice saves the three gardeners by hiding them in a large flower-pot. The soldiers report the heads are gone (satisfying the Queen).
*   **The Croquet Game:** The game begins with live hedgehogs as balls and live flamingoes as mallets. The players play simultaneously without turns, causing chaos. Alice struggles with her flamingo (which twists to look at her) and the hedgehog (which crawls away). 
*   **The Cheshire Cat's Appearance:** A grin appears in the air, followed by the full head of the Cheshire Cat. Alice vents to the Cat about the unfairness of the game. The King arrives, finds the Cat impertinent, and calls for its removal. The Queen orders "Off with his head!"
*   **The Dispute:** While the King goes to fetch the executioner, a dispute arises between the Executioner (arguing you need a body to cut a head from), the King (arguing anything with a head can be beheaded), and the Queen (threatening mass execution). 
*   **The Duchess:** Alice suggests asking the Duchess; the Queen orders the Executioner to fetch her from prison. As the Executioner leaves, the Cat fades away entirely.

**Visual Continuity & Objects:**
*   **Gardeners/Soldiers:** They are shaped like playing cards (oblong/flat with hands/feet at corners).
*   **The Rose-Tree:** A large tree being painted red.
*   **The Procession Order:** Soldiers $\rightarrow$ Courtiers $\rightarrow$ Royal Children $\rightarrow$ Guests (White Rabbit) $\rightarrow$ Knave of Hearts $\rightarrow$ King & Queen.
*   **Croquet Equipment:** Live hedgehogs (balls), live flamingoes (mallets), and soldiers acting as arches.
*   **The Cheshire Cat:** Appears gradually (eyes, then mouth/ears, then full head) before fading away.
````

## Raw Response
````text
[[FILMCREATOR_PACKET]]

task: character_extraction

version: 1

character_index_markdown:

[[SECTION character_index_markdown]]
# Character Index
- [Alice](#alice)
- [Two](#two)
- [Five](#five)
- [Seven](#seven)
- [White Rabbit](#white-rabbit)
- [Knave of Hearts](#kneave-of-hearts)
- [King of Hearts](#king-of-hearts)
- [Queen of Hearts](#queen-of-hearts)
- [Cheshire Cat](#cheshire-cat)
- [The Duchess](#the-duchess)
[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: alice
canonical_character_id: CH002 Alice
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
direct_identity_evidence: "Alice is a central figure interacting with the Queen and the Cat."
direct_visual_evidence: "Interacts with cards and animals; described as brave/defiant."
costume_or_covering_evidence: ""
movement_evidence: ""
associated_entities: [two, five, seven, queen_of_hearts, cheshire_cat]
alias_or_role_evidence: ""
unknowns: ""
source_refs: ""

[[SECTION markdown]]
# Alice
**Role:** Protagonist / Observer.
**Status:** Physically present.
**Description:** A brave girl who stands up to the Queen of Hearts. She is capable of hiding gardeners in flower-pots and managing live animals used for croquet.
**Notes:** Her physical appearance (hair/dress) is not specified in this chapter, but she acts with a mix of curiosity and defiance.
[[/SECTION]]
[[/FILcut_record]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: gardener_two
canonical_character_id: CH003 Two
aliases: Two
is_fully_identified: true
manual_description_required: false
manual_description_reason: ""
clarification_required: false
clarification_reason: ""
clarification_question: ""
character_type_hint: humanoid_nonhuman
morphology_hint: biped
scale_hint: human_scale
renderability_hint: renderable
confidence: 0.9
direct_identity_evidence: "Identified as one of the gardeners."
direct_visual_evidence: "A playing card-shaped gardener (flat, oblong)."
costume_or_covering_evidence: "Card-like structure."
movement_evidence: ""
associated_entities: [five, seven, alice]
alias_or_role_evidence: "One of the three gardeners painting roses."
unknowns: ""
source_refs: ""

[[SECTION markdown]]
# Two (Gardener)
**Role:** Gardener.
**Status:** Physically present.
**Description:** A card-shaped gardener with hands and feet at the corners. 
**Notes:** Part of a trio of gardeners painting white roses red to hide mistakes from thes Queen.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: gardener_five
canonical_character_id: CH003 Five
aliases: Five
is_fully_identified: true
manual_description_required: false
manual_description_reason: ""
clarification_required: false
clarification_reason: ""
clarification_question: ""
character_type_hint: humanoid_nonhuman
morphology_hint: biped
scale_hint: human_scale
renderability_hint: renderable
confidence: 0.9
direct_identity_evidence: "Identified as one of the gardeners."
direct_visual_evidence: "A playing card-shaped gardener (flat, oblong)."
costume_or_covering_evidence: "Card-like structure."
movement_evidence: ""
associated_entities: [two, seven, alice]
alias_or_role_evidence: "One of the three gardeners painting roses."
unknowns: ""
source_refs: ""

[[SECTION markdown]]
# Five (Gardener)
**Role:** Gardener.
**Status:** Physically present.
**Description:** A card-shaped gardener with hands and feet at the corners. 
**Notes:** Part of a trio of gardeners painting white roses red to hide mistakes from the Queen.
[[/end_section]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: gardener_seven
canonical_character_id: CH003 Seven
aliases: Seven
is_fully_identified: true
manual_description_required: false
manual_description_reason: ""
clarification_required: false
clarification_reason: ""
character_type_hint: humanoid_nonhuman
morphology_hint: biped
scale_hint: human_scale
renderability_hint: renderable
confidence: 0.9
direct_identity_evidence: "Identified as one of the gardeners."
direct_visual_evidence: "A playing card-shaped gardener (flat, oblong)."
costume_or_covering_evidence: "Card-like structure."
movement_evidence: ""
associated_entities: [two, five, alice]
alias_or_role_evidence: "One of the three gardeners painting roses."
unknowns: ""
source_refs: ""

[[SECTION markdown]]
# Seven (Gardener)
**Role:** Gardener.
**Status:** Physically present.
**Description:** A card-shaped gardener with hands and feet at the corners. 
**Notes:** Part of a trio of gardeners painting white roses red to hide mistakes from the Queen.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMcially_record]]
type: character
asset_id: white_rabbit
canonical_character_id: CH004 White Rabbit
aliases: []
is_fully_identified: true
manual_description_required: false
manual_description_reason: ""
clarification_required: false
clarification_reason: ""
character_type_hint: animal
morphology_hint: quadruped
scale_hint: small
renderability_hint: renderable
confidence: 0.8
direct_identity_evidence: "Named as a guest in the procession."
direct_visual_evidence: ""
costume_or_covering_evidence: ""
movement_evidence: ""
associated_entities: []
alias_or_role_evidence: ""
unknowns: ""
source_refs: ""

[[SECTION markdown]]
# White Rabbit
**Role:** Guest / Procession Member.
**Status:** Physically present (referenced as guest).
**Description:** A rabbit-like creature.
**Notes:** Part of the royal procession guests.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: knave_of_hearts
canonical_character_id: CH004 Knave of Hearts
aliases: [Knave]
is_fully_identified: true
manual_description_required: false
manual_description_reason: ""
clarification_required: false
clarification_reason: ""
character_type_hint: humanoid_nonhuman
morphology_hint: biped
scale_hint: human_scale
renderability_hint: renderable
confidence: 0.9
direct_identity_evidence: "Identified as the Knave of Hearts."
direct_visual_evidence: "Carrying the crown."
costume_or_covering_evidence: ""
movement_evidence: ""
associated_entities: [queen_of_hearts, king_of_hearts]
alias_or_role_evidence: "A card-based entity carrying a crown."
unknowns: ""
source_s_refs: ""

[[SECTION markdown]]
# Knave of Hearts
**Role:** Procession Member.
**Status:** Physically present.
**Description:** A humanoid playing card figure.
**Notes:** Carries the crown during the procession.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: king_of_hearts
canonical_character_id: CH004 King of Hearts
aliases: [King]
is_fully_identified: true
manual_description_required: false
manual_description_reason: ""
clarification_required: false
clarification_reason: ""
character_type_hint: humanoid_nonhuman
morphology_hint: biped
scale_hint: human_scale
renderability_hint: renderable
confidence: 0.9
direct_identity_evidence: "Identified as the King."
direct_visual_evidence: ""
costume_or_covering_evidence: ""
movement_evidence: ""
associated_entities: [queen_of_hearts, knave_of_hearts]
alias_or_role_evidence: ""
unknowns: ""
source_refs: ""

[[SECTION markdown]]
# King of Hearts
**Role:** Royal.
**Status:** Physically present.
**Description:** A humanoid playing card figure.
**Notes:** Involved in the dispute over execution logic and the removal of the Cat.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: queen_of_hearts
canonical_character_id: CH004 Queen of Hearts
aliases: [Queen]
is_fully_identified: true
manual_description_required: false
manual_description_reason: ""
clarification_required: false
clarification_reason: ""
character_type_hint: humanoid_nonhuman
morphology_hint: biped
scale_hint: human_scale
renderability_hint: renderable
confidence: 0.9
direct_identity_evidence: "Identified as the Queen."
direct_visual_evidence: ""
costume_or_covering_evidence: ""
movement_evidence: ""
associated_entities: [king_of_hearts, knave_of_hearts]
alias_or_role_evidence: ""
unknowns: ""
source_refs: ""

[[SECTION markdown]]
# Queen of Hearts
**Role:** Royal.
**Status:** Physically present.
**Description:** A humanoid playing card figure with an authoritative presence.
**Notes:** Orders executions and reacts strongly to the gardeners' mistake and Alice's defiance.
[[/SECTION]]
[[e_record]]
[[FILMCREATOR_RECORD]]
type: character
asset_id: cheshire_cat
canonical_character_id: CH005 Cheshire Cat
aliases: [Cat]
is_fully_identified: true
manual_description_required: false
manual_description_reason: ""
clarification_required: false
clarification_reason: ""
character_type_hint: animal
morphology_hint: unknown
scale_hint: human_scale
renderability_hint: renderable
confidence: 0.85
direct_identity_evidence: "Identified as the Cheshire Cat."
direct_visual_evidence: "Appears via a grin, then head, then full form; fades away."
costume_or_covering_evidence: ""
movement_evidence: "Fades in and out of existence."
associated_entities: [alice]
alias_or_role_evidence: ""
unknowns: ""
source_refs: ""

[[SECTION markdown]]
# Cheshire Cat
**Role:** Interlocutor.
**Status:** Physically present (appearing/fading).
**Description:** A cat-like entity that manifests through a floating grin before showing its head.
**Notes:** Provides a source of conversation for Alice; can fade entirely from view.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: the_duchess
canonical_character_id: CH006 The Duchess
aliases: [Duchess]
is_fully_identified: false
manual_description_required: true
manual_description_reason: "Only mentioned as a prisoner to be fetched."
clarification_required: true
clarification_question: "What is the Duchess's physical appearance or role in the prison?"
character_type_hint: humanoid_nonhuman
morphology_hint: unknown
scale_hint: human_scale
renderability_hint: context_only
confidence: 0.5
direct_identity_evidence: ""
direct_visual_evidence: ""
costume_or_covering_evidence: ""
movement_evidence: ""
associated_entities: []
alias_or_role_evidence: "A prisoner to be fetched by the executioner."
unknowns: ""
source_refs: ""

[[SECTION markdown]]
# The Duchess
**Role:** Prisoner.
**Status:** Referenced (not physically present).
**Description:** A figure currently in prison.
**Notes:** Mentioned as a potential person to ask for advice/help.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
