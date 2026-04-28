# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-27T23:45:05.530948+00:00
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
- [Alice](#alice)
- [Fish-Footman](#fish-foottyman)
- [Frog-Footman](#frog-footman)
- [The Duchess](#the-duchess)
- [The Cook](#the-cook)
- [The Baby](#the-baby)
- [The Cheshire Cat](#the-cheshire-cat)
- [The Hatter](#the-hatter)
- [The March Hare](#the-march-hare)

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
character_type_hint: human
morphology_hint: bdipod
scale_hint: human_scale
renderability_hint: renderable
confidence: 1.0
direct_identity_evidence: true
direct_visual_evidence: false
costume_or_covering_evidence: false
movement_evidence: false
associated_entities: []
alias_or_role_evidence: false
unknowns: []
source_refs: []

[[SECTION markdown]]
# Alice
**Role:** Protagonist / Curious Girl.
**Status:** Physically present.
**Description:** A polite, curious girl attempting to navigate a nonsensical environment through logic and conversation. 
**Visual Cues:** Physical appearance is not detailed in this chapter beyond her human scale and role as an interlocutor.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: fish_footman
canonical_character_id: CH002 Fish-Footman
aliases: 
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
direct_identity_evidence: true
direct_visual_evidence: true
costume_or_covering_evidence: true
movement_evidence: false
associated_entities: [frog_footman]
alias_or_role_evidence: false
unknowns: []
source_refs: []

[[SECTION markdown]]
# Fish-Footman
**Role:** Messenger / Servant.
**Status:** Physically present.
**Description:** A creature with a fish-like face. He wears curled, powdered hair/livery. 
**Visual Cues:** Fish-face, formal/curled hair.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: frog_footman
canonical_character_id: CH003 Frog-Footman
aliases: 
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
direct_identity_evidence: true
direct_visual_evidence: true
costume_or_covering_evidence: true
movement_evidence: false
associated_entities: [fish_footman]
alias_or_role_evidence: false
unknowns: []
source_refs:s[]

[[SECTION markdown]]
# Frog-Footman
**Role:** Messenger / Servant.
**Status:** Physically present.
**Description:** A creature with large eyes like a frog and curled, powdered hair. 
**Visual Cues:** Large frog-like eyes, curled/powdered hair.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: the_duchess
canonical_character_id: CH004 The Duchess
aliases: 
is_fully_identified: true
manual_description_required: false
manual_description_reason: 
clarification_required: false
clarification_reason: 
character_type_hint: human
morphology_hint: biped
scale_hint: human_scale
renderability_hint: renderable
confidence: 0.9
direct_identity_evidence: true
direct_visual_evidence: true
costume_or_covering_evidence: false
movement_evidence: true
associated_entities: [the_cook, the_baby]
alias_or_role_evidence: false
unknowns: []
source_refs: []

[[SECTION markdown]]
# The Duchess
**Role:** Chaotic maternal figure.
**Status:** Physically present.
**Description:** A woman sitting on a three-legged stool in a peppery kitchen. She has a hoarse growl and is nursing a baby. 
**Visual Cues:** Sitting on a stool, nursing, hoarse voice.
[[/end_section]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: the_cook
canonical_character_id: CH005 The Cook
aliases: 
is_fully_identified: true
manual_description_required: false
manual_description_reason: 
clarification_required: false
clarification_reason: 
character_type_hint: human
morphology_hint: biped
scale_hint: human_scale
renderability_hint: renderable
confidence: 0.9
direct_identity_evidence: true
direct_visual_evidence: true
costume_or_covering_evidence: false
movement_evidence: true
associated_entities: [the_duchess, the_baby]
alias_or_role_evidence: false
unknowns: []
source_refs: []

[[SECTION markdown]]
# The Cook
**Role:** Chaotic kitchen worker.
**Status:** Physically present.
**Description:** A cook leaning over a fire or cauldron in a smoke-filled kitchen. She is violent, throwing objects like fire-irons and saucepans at the Duchess and baby. 
**Visual Cues:** Leaning over a cauldron/fire, active movement (throwing).
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: the_baby
canonical_character_id: CH006 The Baby
aliases: 
is_fully_identified: true
manual_description_required: false
manual_description_reason: 
clarification_required: false
clarification_reason: 
character_type_hint: humanoid_nonhuman
morphology_hint: biped
scale_hint: small
renderability_hint: renderable
confidence: 0.85
direct_identity_evidence: true
direct_visual_evidence: true
costume_or_covering_evidence: false
movement_evidence: true
associated_entities: [the_duchess, alice]
alias_or_role_evidence: false
unknowns: []
source_refs: []

[[SECTION markdown]]
# The Baby
**Role:** Chaotic infant/animal.
**Status:** Physically present / Transforms into pig.
**Description:** Initially a human infant with a turn-up nose and small eyes. As the story progresses, it takes on a starfish-like shape before transforming into a pig. 
**Visual Cues:** Humanoid infant features (turn-up nose), later becomes a pig.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILcut_record]]
type: character
asset_id: the_cheshire_cat
canonical_character_id: CH007 The Cheshire Cat
aliases: 
is_fully_identified: true
manual_description_required: false
manual_description_reason: 
clarification_required: false
clarification_reason: 
character_type_hint: animal
morphology_hint: quadruped
scale_hint: small
renderability_hint: renderable
confidence: 0.95
direct_identity_evidence: true
direct_visual_evidence: true
costume_or_covering_evidence: false
movement_evidence: true
associated_entities: []
alias_or_role_evidence: false
unknowns: []
source_refs: []

[[SECTION markdown]]
# The Cheshire Cat
**Role:** Enigmatic guide/observer.
**Status:** Physically present / Vanishing.
**Description:** A cat with long claws and many teeth. It has the ability to vanish, leaving only its grin behind. 
**Visual Cues:** Large grin, long claws, vanishing effect.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: the_hatter
canonical_character_id: CH008 The Hatter
aliases: 
is_fully_identified: false
manual_description_required: true
manual_description_reason: Only mentioned as an inhabitant of the woods.
clarification_required: false
clarification_reason: 
clarocation_question: 
character_type_hint: human
morphology_hint: biped
scale_hint: human_scale
renderability_hint: context_only
confidence: 0.5
direct_identity_evidence: false
direct_visual_evidence: false
costume_or_covering_evidence: false
movement_evidence: false
associated_entities: [the_march_hare]
alias_or_role_evidence: false
unknowns: []
source_refs: []

[[SECTION markdown]]
# The Hatter
**Role:** Mentioned inhabitant.
**Status:** Referenced.
**Description:** An inhabitant of the woods. No physical description provided in this chapter.
[[/SECTION]]
[[end_record]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: the_march_hare
canonical_character_id: CH009 The March Hare
aliases: 
is_fully_identified: false
manual_description_required: true
manual_description_reason: Only mentioned as an inhabitant of the woods.
clarification_required: false
clarification_reason: 
clarification_question: 
character_type_hint: animal
morphology_hint: quadruped
scale_hint: small
renderability_hint: context_only
confidence: 0.5
direct_identity_evidence: false
direct_visual_evidence: false
costume_or_covering_evidence: false
movement_evidence: false
associated_entities: [the_hatter]
alias_or_role_evidence: false
unknowns: []
source_refs: []

[[SECTION markdown]]
# The March Hare
**Role:** Mentioned inhabitant.
**Status:** Referenced.
**Description:** An inhabitant of the woods. No physical description provided in this chapter.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]
[[/FILMCREATOR_PACKET]]
````
