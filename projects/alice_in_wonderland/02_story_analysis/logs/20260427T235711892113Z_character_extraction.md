# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-27T23:57:11.892113+00:00
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
- [Knave of Hearts](#knave-of-hearts)
- [King of Hearts](#king-of-hearts)
- [Queen of Hearts](#queen-of-hearts)
- [Cheshire Cat](#cheshire-cat)
- [The Duchess](#the-duchess)
- [Executioner](#executioner)

[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: alice
canonical_character_id: CH001 Alice
aliases: 
is_fully_identified: true
manual_description_required: false
manual_description_reason: 
clarification_required: false
clarification_reason: 
clarification_question: 
character_type_hint: human-like entity
morphology_hint: human
scale_hint: human-sized
renderability_hint: high
confidence: 0.9
direct_identity_evidence: true
direct_visual_evidence: true
costume_or_covering_evidence: false
movement_evidence: true
associated_entities: Two, Five, Seven, Queen of Hearts, Cheshire Cat
alias_or_role_evidence: protagonist
unknowns: 
source_refs: CH008
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: gardener_two
canonical_character_id: CH008 Gardener Two
aliases: Two
is_fully_identified: true
manual_description_required: false
manual_description_reason: 
clarification_required: false
clarification_reason: 
clarification_question: 
character_type_hint: card-person
morphology_hint: flat, oblong shape with hands/feet at corners
scale_hint: human-sized (relative to Alice)
renderability_hint: medium
confidence: 0.8
direct_identity_evidence: true
direct_visual_evidence: true
costume_or_covering_evidence: card-like structure
movement_evidence: true
associated_entities: Five, Seven, Alice
alias_or_role_evidence: gardener
unknowns: 
source_refs: CH008
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: gardener_five
canonical_character_id: CH008 Gardener Five
aliases: Five
is_fully_identified: true
manual_description_required: false
manual_description_reason: 
clarification_required: false
clarification_reason: 
clarification_question: 
character_type_hint: card-person
morphology_hint: flat, oblong shape with hands/feet at corners
scale_hint: human-sized (relative to Alice)
renderability_hint: medium
confidence: 0.8
direct_identity_evidence: true
direct_visual_evidence: true
costume_or_covering_evidence: card-like structure
movement_evidence: true
associated_entities: Two, Seven, Alice
alias_or_role_evidence: gardener
unknowns: 
source_refs: CH008
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: gardener_seven
canonical_character_id: CH008 Gardener Seven
aliases: Seven
is_fully_identified: true
manual_description_required: false
manual_description_reason: 
clarification_required: false
clarification_reason: 
clarification_question: 
character_type_hint: card-person
morphology_hint: flat, oblong shape with hands/feet at corners
scale_hint: human-sized (relative to Alice)
renderability_hint: medium
confidence: 0.8
direct_identity_evidence: true
direct_visual_evidence: true
coststant_or_covering_evidence: card-like structure
movement_evidence: true
associated_entities: Two, Five, Alice
alias_or_role_evidence: gardener
unknowns: 
source_refs: CH008
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: white_rabbit
canonical_character_id: CH008 White Rabbit
aliases: 
is_fully_identified: true
manual_description_required: false
manual_description_reason: 
clarification_required: false
clarification_reason: 
clarification_question: 
character_type_hint: animal-person
morphology_hint: rabbit
scale_hint: small/human-sized
renderability_hint: high
confidence: 0.7
direct_identity_evidence: true
direct_visual_evidence: false
costume_or_covering_evidence: false
movement_evidence: false
associated_entities: 
alias_or_role_evidence: guest in procession
unknowns: 
source_refs: CH008
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: knave_of_hearts
canonical_character_id: CH008 Knave of Hearts
aliases: 
is_fully_identified: true
manual_description_required: false
manual_description_reason: 
clarification_required: false
clarification_reason: 
clarification_question: 
character_type_hint: card-person
morphology_hint: flat, oblong shape with hands/feet at corners
scale_hint: human-sized
renderability_hint: medium
confidence: 0.8
direct_identity_evidence: true
direct_visual_evidence: false
costume_or_covering_evidence: carrying the crown
movement_evidence: false
associated_entities: King of Hearts, Queen of Hearts
alias_or_role_evidence: royal guest/bearer
unknowns: 
source_refs: CH008
[[/FIL_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: king_of_hearts
canonical_character_id: CH001 King of Hearts
aliases: 
is_fully_identified: true
manual_description_required: false
manual_description_reason: 
clarification_required: false
clarification_reason: 
clarification_question: 
character_type_hint: card-person
morphology_hint: flat, oblong shape with hands/feet at corners
scale_hint: human-sized
renderability_hint: medium
confidence: 0.8
direct_identity_evidence: true
direct_visual_evidence: false
costume_or_covering_evidence: crown
movement_evidence: false
associated_entities: Queen of Hearts, Knave of Hearts, Executioner
alias_or_role_evidence: king
unknowns: 
source_refs: CH008
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: queen_of_hearts
canonical_character_id: CH001 Queen of Hearts
aliases: 
is_fully_identified: true
manual_description_required: false
manual_description_reason: 
clarification_required: false
clarification_reason: 
clarification_question: 
character_type_hint: card-person
morphology_hint: flat, oblong shape with hands/feet at corners
scale_hint: human-sized
renderability_hint: medium
confidence: 0.8
direct_identity_evidence: true
direct_visual_evidence: false
costume_or_covering_evidence: crown
movement_evidence: false
associated_entities: King of Hearts, Alice, Executioner
alias_or_role_evidence: queen
unknowns: 
source_refs: CH008
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: cheshire_cat
canonical_character_id: CH001 Cheshire Cat
aliases: 
is_fully_identified: true
manual_description_required: false
manual_description_reason: 
clarification_required: false
clarification_reason: 
clarification_question: 
character_type_hint: feline-entity
morphology_hint: cat head/grin appearing in air
scale_hint: variable/floating
renderability_hint: high
confidence: 0.9
direct_identity_evidence: true
direct_visual_evidence: true
costume_or_covering_evidence: false
movement_evidence: fades in and out
associated_entities: Alice, King of Hearts
alias_or_role_evidence: impertinent guest
unknowns: 
source_refs: CH008
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: the_duchess
canonical_character_id: CH008 The Duchess
aliases: 
is_fully_identified: false
manual_description_required: true
manual_description_reason: Only mentioned as a prisoner.
clarification_required: false
clarification_reason: 
clarification_question: What is her physical description?
character_type_hint: unknown
morphology_hint: unknown
scale_hint: human-sized
renderability_hint: low (referenced)
confidence: 0.5
direct_identity_evidence: false
direct_visual_evidence: false
costume_or_covering_evidence: false
movement_evidence: false
associated_entities: Queen of Hearts
alias_or_role_evidence: prisoner/subject
unknowns: 
source_refs: CH008
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: executioner
canonical_character_id: CH008 Executioner
aliases: 
is_fully_identified: true
manual_description_required: false
manual_description_reason: 
clarification_required: false
clarification_reason: 
clarification_question: 
character_type_hint: card-person
morphology_hint: flat, oblong shape with hands/feet at corners
scale_hint: human-sized
renderability_hint: medium
confidence: 0.8
direct_identity_evidence: true
direct_visual_evidence: false
costume_or_covering_evidence: likely carries execution tools
movement_evidence: false
associated_entities: Queen of Hearts, King of Hearts
alias_or_role_evidence: executioner
unknowns: 
source_refs: CH008
[[/FILMCREATOR_RECORD]]

[[SECTION markdown]]
# Alice
**Role:** Protagonist / Observer.  
**Status:** Physically present.  
**Description:** A human-sized girl who is brave enough to answer the Queen and clever enough to hide gardeners in a pot.  
**Notes:** She views the royal court as "only a pack of cards."

# Two
**Role:** Gardener / Card Soldier.  
**Status:** Physically present.  
**Description:** A card-shaped entity (flat, oblong with hands/feet at corners) tasked with painting roses red.  
**Notes:** Bows to Alice; part of the gardening crew.

# Five
**Role:** Gardener / Card Soldier.  
**satus:** Physically present.  
**Description:** A card-shaped entity (flat, oblong with hands/feet at corners).  
**Notes:** Part of the gardening crew.

# Seven
**Role:** Gardener / Card Soldier.  
**Status:** Physically的に present.  
**Description:** A card-shaped entity (flat, oblong with hands/feet at corners).  
**Notes:** Part of the gardening crew.

# White Rabbit
**Role:** Guest in Procession.  
**Status:** Physically present (referenced as part of a group).  
**Description:** An animal-like figure within the royal procession.  
**Notes:** Moves with the court.

# Knave of Hearts
**Role:** Royal Bearer / Guest.  
**Status:** Physically present.  
**Description:** A card-shaped entity carrying the crown.  
**Notes:** Part of the grand parade.

# King of Hearts
**Role:** Ruler / Player.  
**Status:** Physically present.  
**Description:** A card-shaped entity; part of the royal family.  
**Notes:** Argues with the Executioner and the Queen about the logistics of beheading.

# Queen of Hearts
**Role:** Ruler / Antagonist.  
**Status:** Physically present.  
**Description:** A card-shaped entity; authoritative and volatile.  
**Notes:** Orders executions and plays croquet with live animals.

# Cheshire Cat
**Role:** Impertinent Guest / Entity.  
**Status:** Physically present (appears/fades).  
**Description:** A floating head/grin that appears in the air, then fades away entirely.  
**Notes:** Provides a sounding board for Alice's frustrations.

# The Duchess
**Role:** Prisoner (Referenced).  
**Status:** Referenced only.  
**Description:** Unknown physical form; currently in prison.  
**Notes:** Mentioned as a potential person to ask about the situation.

# Executioner
**Role:** Royal Official / Executioner.  
**Status:** Physically present.  
**Description:** A card-shaped entity tasked with carrying out orders.  
**Notes:** Argues the practicalities of beheading heads without bodies.

[[/SECTION]]

[[/FILMCREATOR_PACKET]]
````
