# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-27T23:46:04.031982+00:00
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

Chapter id: CH006

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

**Setting:** A house with a door (leading to a smoke-filled kitchen) and the surrounding woods. The kitchen is filled with pepper-laden air. Later, an outdoor area where the baby transforms into a pig, and finally, the path toward the March Hare's house (which has ear-shaped chimneys and fur-thatched roofing).

**Characters:**
* **Alice:** A curious, polite girl trying to maintain logic in a nonsensical environment.
* **Fish-Footman:** Has a fish-like face; wears curled, powdered hair/livery. He delivers the Queen's invitation.
* **Frog-Footman:** Has large eyes like a frog and curled, powdered hair.
* **The Duchess:** Sitting on a three-legged stool in the kitchen; has a hoarse growl and is nursing a baby.
* **The Cook:** Leaning over a fire/caustron; throws objects (fire-irons, saucepans) at the Duchess and baby.
* **The Baby:** A creature that starts as a human infant but possesses a turn-up nose and small eyes; eventually transforms into a pig.
* **The Cheshire Cat:** A cat with long claws and many teeth; it can vanish/reappear, leaving only its grin behind.
* **The Hatter & The March Hare:** Mentioned as inhabitants of the woods.

**Key Events:**
1. **The Invitation:** Alice watches from the wood as a Fish-Footman delivers a large letter to a Frog-Footman, announcing an invitation from the Queen to play croquet for the Duchess.
2. **The Interaction at the Door:** The Frog-Footman sits on the ground; Alice approaches him. He explains that knocking is useless because they are on the same side of the door and the noise inside is too loud. A large plate skims out of the house, nearly hitting the Footman before shattering against a tree.
3. **The Kitchen Chaos:** Alice enters the smoke-filled kitchen. The Duchess sits on a stool nursing a baby while the Cook stirs a cauldron of peppery soup. The Duchess and the baby sneeze frequently.
4. **The Cat's Grin:** Alice asks about the grinning cat (the Cheshire Cat) sitting on the hearth. The Duchess dismisses her knowledge.
5. **The Violent Kitchen Scene:** The Cook throws items at the Duchess and baby. The Duchess remains unfazed. Alice tries to discuss the earth's rotation, but the Duchess tells the Cook to "chop off her head!"
6. **The Baby’s Transformation:** The Duchess flings the baby to Alice as she leaves for croquet. Alice realizes the baby is shaped like a starfish and has a snout-like nose. As they walk outside, the baby grunts violently and transforms into a pig before trotting into the wood.
7. **Meeting the Cheshire Cat:** Alice encounters the Cat in the woods. The Cat explains that everyone is mad (using its own logic of growling vs. purring). The Cat tells Alice she will see him at the croquet game before vanishing, leaving only its grin.
8. **Approaching the March Hare's House:** Alice walks toward a house with ear-shaped chimneys and fur-thatched roof. She nibbles mushroom to adjust her size and approaches timidly.
````

## Raw Response
````text
[[FILMCREATOR_PACKET]]

task: character_extraction

version: 1

character_index_markdown:

[[SECTION character_index_markdown]]

# Character Index
* [Alice](#alice)
* [Fish-Footman](#fish-footty-footman)
* [Frog-Footman](#frog-footman)
* [The Duchess](#the-duchess)
* [The Cook](#the-cook)
* [The Baby](#the-baby)
* [The Cheshire Cat](#the-cheshire-cat)
* [The Hatter](#the-hatter)
* [The March Hare](#the-march-hare)

[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: alice
canonical_character_id: CH002 Alice
aliases: 
is_fully_identified: true
manual_description_required: false
manual_description_reason: ""
clarification_required: false
clarification_reason: ""
clarification_question: ""
character_type_hint: human girl
morphology_hint: human
scale_hint: human-sized
renderability_hint: high
confidence: 0.9
direct_identity_evidence: true
direct_visual_evidence: true
costume_or_covering_evidence: false
movement_evidence: true
associated_entities: The Duchess, The Cook, The Baby, The Cheshire Cat
alias_or_role_evidence: protagonist
unknowns: ""
source_refs: ""

[[SECTION markdown]]
# Alice
**Role:** Protagonist / Curious Girl
**Status:** Physically Present
**Description:** A curious and polite girl attempting to maintain logic in a nonsly nonsensical environment. 
**Notes:** She interacts with various entities, from the Footmen to the Duchess and the Cheshire Cat.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: fish_footman
canonical_character_id: CH006 Fish-Footman
aliases: 
is_fully_identified: true
manual_description_required: false
manual_description_reason: ""
clarification_required: false
clarification_reason: ""
clarification_question: ""
character_type_hint: hybrid
morphology_hint: fish-headed human
scale_hint: human-sized
renderability_hint: high
confidence: 0.85
direct_identity_evidence: true
direct_visual_evidence: true
costume_or_covering_evidence: true
movement_evidence: true
associated_entities: Frog-Footman, The Queen
alias_or_role_evidence: messenger
unknowns: ""
source_refs: ""

[[SECTION markdown]]
# Fish-Footman
**Role:** Messenger / Servant
**Status:** Physically Present
**Description:** A creature with a fish-like face wearing curled, powdered hair/livery. 
**Notes:** Delivers the Queen's invitation to the Frog-Footman.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: frog_footman
canonical_character_id: CH006 Frog-Footman
aliases: 
is_fully_identified: true
manual_description_required: false
manual_description_reason: ""
clarification_required: false
clarification_reason: ""
clarification_question: ""
character_type_hint: hybrid
morphology_hint: frog-eyed human
scale_hint: human-sized
renderability_hint: high
confidence: 0.85
direct_identity_evidence: true
direct_visual_evidence: true
costmist_or_covering_evidence: true
movement_evidence: true
associated_entities: Fish-Footman, The Queen
alias_or_role_evidence: recipient of invitation
unknowns: ""
source_refs: ""

[[SECTION markdown]]
# Frog-Footman
**Role:** Recipient / Servant
**Status:** Physically Present
**Description:** A creature with large eyes like a frog and curled, powdered hair. 
**Notes:** Sits on the ground to receive an invitation from the Queen.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: the_duchess
canonical_character_id: CH006 The Duchess
aliases: 
is_fully_identified: true
manual_description_required: false
manual_description_reason: ""
clarification_required: false
clarification_reason: ""
clarification_question: ""
character_type_hint: human-like
morphology_hint: human
scale_hint: human-sized
renderability_hint: high
confidence: 0.9
direct_identity_evidence: true
direct_visual_evidence: true
costume_or_covering_evidence: true
movement_evidence: true
associated_entities: The Cook, The Baby, Alice
alias_or_role_evidence: noble/mother figure
unknowns: ""
source_refs: ""

[[SECTION markdown]]
# The Duchess
**Role:** Chaotic Mother Figure
**Status:** Physically Present
**Description:** Sits on a three-legged stool in a smoke-filled kitchen; possesses a hoarse growl. 
**Notes:** She is nursing a baby and remains unfazed by the violent cooking environment.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: the_cook
canonical_character_id: CH006 The Cook
aliases: 
is_fully_identified: true
manual_description_required: false
manual_description_reason: ""
clarification_required: false
clarification_reason: ""
clarification_question: ""
character_type_hint: human
morphology_hint: human
scale_hint: human-sized
renderability_hint: high
confidence: 0.9
direct_identity_evidence: true
direct_visual_evidence: true
costume_or_covering_evidence: false
movement_evidence: true
associated_entities: The Duchess, The Baby
alias_or_role_evidence: kitchen worker
unknowns: ""
source_refs: ""

[[SECTION markdown]]
# The Cook
**Role:** Chaotic Kitchen Worker
**Status:** Physically Present
**Description:** Leaning over a fire/cauldron in a peppery-filled kitchen. 
**Notes:** Throws objects like fire-irons and saucepans at the Duchess and baby.
[[/end_section]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: the_baby
canonical_character_id: CH006 The Baby
aliases: 
is_fully_identified: true
manual_description_required: false
manual_description_reason: ""
clarification_required: false
clarification_reason: ""
clarification_question: ""
character_type_hint: hybrid (human to pig)
morphology_hint: human infant with turn-up nose and small eyes, later a pig
scale_hint: infant/small animal
renderability_hint: high
confidence: 0.95
direct_identity_evidence: true
direct_visual_evidence: true
costume_or_covering_evidence: false
movement_evidence: true
associated_entities: The Duchess, Alice
alias_or_role_evidence: infant/animal
unknowns: ""
source_srefs: ""

[[SECTION markdown]]
# The Baby
**Role:** Transforming Infant
**Status:** Physically Present (Transforms)
**Description:** Initially a human infant with a turn-up nose and small eyes; later transforms into a pig. 
**Notes:** Eventually trots off into the woods as a pig after being handed to Alice.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: the_cheshire_cat
canonical_character_id: CH006 The Cheshire Cat
aliases: 
is_fully_identified: true
manual_description_required: false
manual_description_reason: ""
clarification_required: false
clarification_reason: ""
clarification_question: ""
character_type_hint: feline-like entity
morphology_hint: cat with long claws and many teeth
scale_hint: cat-sized
renderability_hint: high
confidence: 0.95
direct_identity_evidence: true
direct_visual_evidence: true
costume_or_covering_evidence: false
movement_evidence: true
associated_entities: Alice
alias_or_role_evidence: guide/philosopher
unknowns: ""
source_refs: ""

[[SECTION markdown]]
# The Cheshire Cat
**Role:** Philosophical Guide
**Status:** Physically Present (Vanishing)
**Description:** A cat with long claws and many teeth; capable of vanishing to leave only a grin. 
**Notes:** Explains the concept of madness to Alice before disappearing.
[[/SECTION]]
[[e_section]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: the_hatter
canonical_character_id: CH006 The Hatter
aliases: 
is_fully_identified: false
manual_description_required: true
manual_description_reason: Mentioned but not present.
clarification_required: false
clarification_reason: ""
clarification_question: ""
character_type_hint: human
morphology_hint: unknown
scale_hint: human-sized
renderability_hint: medium
confidence: 0.5
direct_identity_evidence: false
direct_visual_evidence: false
costume_or_covering_evidence: false
movement_evidence: false
associated_entities: The March Hare
alias_or_role_evidence: inhabitant of the woods
unknowns: "Physical appearance"
source_refs: ""

[[SECTION markdown]]
# The Hatter
**Role:** Inhabitant (Referenced)
**Status:** Referenced
**Description:** An inhabitant of the woods. 
**Notes:** Mentioned as a resident of the area.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: the_march_hare
canonical_character_id: CH006 The March Hare
aliases: 
is_fully_identified: false
manual_description_required: true
manualdescription_reason: Mentioned but not present.
clarification_required: false
clarification_reason: ""
clarification_question: ""
character_type_hint: animal-like human
morphology_hint: unknown
scale_hint: small/human-sized
renderability_hint: medium
confidence: 0.5
direct_identity_evidence: false
direct_visual_evidence: false
costume_or_covering_evidence: false
movement_evidence: false
associated_entities: The Hatter
alias_or_role_evidence: inhabitant of the woods
unknowns: "Physical appearance"
source_refs: ""

[[SECTION markdown]]
# The March Hare
**Role:** Inhabitant (Referenced)
**Status:** Referenced
**Description:** An inhabitant of the woods. 
**Notes:** Associated with a house featuring ear-shaped chimneys and fur-thatched roofing.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
