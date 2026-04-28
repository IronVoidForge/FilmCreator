# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-27T23:44:08.613203+00:00
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
- [Fish-Footman](#fish-footmaun)
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
morphology_hint: bdip
scale_hint: human_scale
renderability_hint: renderable
confidence: 1.0
direct_identity_evidence: true
direct_visual_evidence: true
costume_or_covering_evidence: false
movement_evidence: true
associated_entities: [the_baby, the_duchess, the_cook, the_cheshire_cat]
alias_or_role_evidence: true
unknowns: []
source_refs: []

[[SECTION markdown]]
# Alice
**Role:** Protagonist / Curious Girl

**Status:** Physically Present.

**Description:** A curious and polite girl attempting to maintain logic in a nonsensical environment. She is of human scale and moves through the woods and houses.

**Notes:** Her physical appearance (hair color, dress) is not specified in this chapter, but she is established as a human-scale child/young lady.
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
movement_evidence: true
associated_entities: [frog_footman]
alias_or_role_evidence: true
unknowns: []
source_refs: []

[[SECTION markdown]]
# Fish-Footman
**Role:** Messenger / Inhabitant of the woods.

**Status:** Physically Present.

**Description:** A creature with a fish-like face. He wears curled, powdered hair/lipecy. 

**Notes:** His identity is tied to his hybrid aquatic/humanoid appearance.
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
movement_evidence: true
associated_entities: [fish_footman, alice]
alias_or_role_evidence: true
unknowns: []
source_refs: []

[[SECTION markdown]]
# Frog-Footman
**Role:** Messenger / Inhabitant of the woods.

**Status:** Physically Present.

**Description:** A creature with large eyes like a frog and curled, powdered hair. 

**Notes:** He sits on the ground near a door to interact with Alice.
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
costume_or_covering_evidence: true
movement_evidence: true
associated_entities: [the_cook, the_baby]
alias_or_role_evidence: true
unknowns: []
source_refs: []

[[SECTION markdown]]
# The Duchess
**Role:** Chaotic Mother / Hostess.

**Status:** Physically Present.

**Description:** A woman sitting on a three-legged stool in a kitchen, nursing a baby. She has a hoarse growl and is prone to sneezing due to the pepper.

**Notes:** She remains unfazed by the violent cooking environment around her.
[[end_section]]
[[/SECTION]]
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
alias_or_role_evidence: true
unknowns: []
source_refs: []

[[SECTION markdown]]
# The Cook
**Role:** Chaotic Kitchen Worker.

**Status:** Physically Present.

**Description:** A person leaning over a fire or cauldron in a smoke-filled kitchen. She is violent, throwing fire-irons and saucepans at the Duchess and baby.

**Notes:** Her actions are characterized by chaos and aggression.
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
scale_hint: tiny
renderability_hint: renderable
confidence: 0.85
direct_identity_evidence: true
direct_visual_evidence: true
costume_or_covering_evidence: false
movement_evidence: true
associated_entities: [the_duchess, alice]
alias_or_role_evidence: true
unknowns: []
source_refs: []

[[SECTION markdown]]
# The Baby
**Role:** Chaotic Infant.

**Status:** Physically Present / Transforms into a pig.

**Description:** Initially appears as a human infant with a turn-up nose and small eyes. As it grows/changes, it takes on a starfish shape before transforming into a pig.

**Notes:** The transformation from baby to pig is a key visual shift in the chapter.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: the_cheshire_cat
canonical_character_id: CH007 The Cheshire Cat
aliases: 
is_fully_identified: true
manual_description_required: false
manualdescription_reason: 
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
associated_entities: [alice]
alias_or_role_evidence: true
unknowns: []
source_refs: []

[[SECTION markdown]]
# The Cheshire Cat
**Role:** Enigmatic Guide / Inhabitant of the woods.

**Status:** Physically Present (can vanish/reappear).

**Description:** A cat with long claws and many teeth. It has the ability to vanish, leaving only its grin behind.

**Notes:** Its presence is marked by its wide, toothy grin.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: the_hatter
canonical_character_id: CH008 The Hatter
aliases: 
is_fully_identified: false
manual_description_required: true
manual_description_reason: Only mentioned as an inhabitant.
clarification_required: false
clarification_reason: 
clarification_question: 
character_type_hint: unknown
morphology_hint: unknown
scale_hint: human_scale
renderability_hint: context_only
confidence: 0.4
direct_identity_evidence: false
direct_visual_evidence: false
costume_or_covering_evidence: false
movement_evidence: false
associated_entities: [the_march_hare]
alias_or_role_evidence: true
unknowns: []
source_refs: []

[[SECTION markdown]]
# The Hatter
**Role:** Mentioned Inhabitant.

**Status:** Referenced.

**Description:** A character mentioned as living in the woods. No physical description is provided in this chapter.

**Notes:** Likely a human-scale figure, but visual details are currently unknown.
[[/SECTION]]
[[end_section]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: the_march_hare
canonical_character_id: CH009 The March Hare
aliases: 
is_fully_identified: false
manual_description_required: true
manual_description_reason: Only mentioned as an inhabitant.
clarification_required: false
clarification_reason: 
clarification_question: 
character_type_hint: unknown
morphology_hint: unknown
scale_hint: human_scale
renderability_hint: context_only
confidence: 0.4
direct_identity_evidence: false
direct_visual_evidence: false
costume_or_covering_evidence: false
movement_evidence: false
associated_entities: [the_hatter]
alias_or_role_evidence: true
unknowns: []
source_refs: []

[[SECTION markdown]]
# The March Hare
**Role:** Mentioned Inhabitant.

**Status:** Referenced.

**Description:** A character mentioned as living in the woods. 

**Notes:** Likely an animal or humanoid-animal hybrid, but visual details are not yet established.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
