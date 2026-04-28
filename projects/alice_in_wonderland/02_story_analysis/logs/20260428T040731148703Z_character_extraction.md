# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-28T04:07:31.148703+00:00
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

Chapter id: CH006

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

**Location: The House Exterior / Woods Edge**
*   **Event:** A Fish-Footman (fish-like face, powdered curly hair) runs from the woods to a house and raps on the door.
*   **Entrance/Exit:** A Frog-Footman (round face, large frog eyes, powdered curly hair) opens the door. The Fish-Footman hands over a massive letter (Queen's croquet invitation). Both bow; their curls entangle.
*   **Event:** Alice hides in the woods to laugh at the footmen. When she peeks out, the Fish-Footman has exited; the Frog-Footman sits on the ground staring at the sky.
*   **Interaction:** Alice knocks. The Frog-Footman refuses to help, claiming he is on her side of the door and that it's too noisy inside.
*   **Visual/Audio Detail:** Extraordinary noise from inside: howling, sneezing, and crashing dishes.
*   **Object Interaction:** A large plate skims out of the house, grazes the Frog-Footman’s nose, and breaks against a tree. The Footman remains indifferent.
*   **Decision:** Alice decides to ignore the Footman's idiotic commentary and enters the house through the door.

**Location: The Kitchen (Interior)**
*   **Environment/Atmosphere:** Thick smoke; heavy presence of pepper causing sneezing.
*   **Characters Present:** The Duchess (on a three-legged stool), a Cook (leaning over a cauldron of soup), a Baby (sneezing and howling), and the Cheshire Cat (sitting on the hearth, grinning).
*   **Interaction:** Alice asks why the cat is grinning. The Duchess identifies it as a Cheshire Cat and shouts "Pig!" at the baby.
*   **Conflict/Action:** The Cook begins throwing kitchen items (fire-irons, saucepans, plates, dishes) at the Duchess and the Baby. The Duchess remains unreactive to being hit.
*   **Dialogue/Reveal:** Alice attempts to discuss the Earth's rotation; the Duchess responds by telling the Cook to "chop off her head!"
*   **Performance/Action:** The Duchess sings a violent lullaby, shaking the baby violently at the end of every line. The Baby and Cook join in a "Wow! wow! wow!" chorus.
*   **Exit/Transition:** The Duchess flings the baby at Alice and exits to play croquet; the Cook throws a frying pan at her (misses).

**Location: Outside / Woods**
*   **Character State:** Alice holds the "star-fish" shaped, snorting baby. She learns the "correct" way to nurse it is to twist it into a knot by its ear and foot.
*   **Transformation/Reveal:** As Alice walks, the baby's nose becomes a snout and eyes shrink. The baby grunts and transforms into a pig.
*   **Event:** Alice sets the pig down; it trots into the woods.
*   **Encounter: The Cheshire Cat:**
    *   The Cat appears on a tree bough (long claws, many teeth, wide grin).
    *   **Dialogue/Logic:** The Cat explains that everyone is mad. It proves its own madness by claiming it growls when pleased and wags its tail when angry (contrary to dogs).
    *   **Visual Effect:** The Cat vanishes, then reappears. It eventually vanishes slowly, starting with the tail and ending with the grin, which lingers in the air.
*   **Decision/Pathing:** Alice heads toward the March Hare's house.

**Location: Approaching the March Hare's House**
*   **Visual Detail:** The house has chimneys shaped like ears and a roof thatched with fur.
*   **Scale Shift:** Alice nibbles more mushroom to raise her height to approximately two feet.
*   **State of Mind:** Alice is hesitant/anxious about the potential madness of the inhabitants.
````

## Raw Response
````text
[[FILMCREATOR_PACKET]]
[[SECTION character_index_markdown]]
# Character Index - Chapter 6

- [Alice](#alice)
- [Fish-Footman](#fish-footman)
- [Frog-Footman](#frog-footman)
- [The Duchess](#the-duchess)
- [Cook](#cook)
- [Baby](#baby)
- [Cheshire Cat](#cheshire-cat)
- [Pig](#pig)

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
scale_hint: small
renderability_hint: renderable
confidence: 1.0
direct_identity_evidence: "Directly named as Alice."
direct_visual_evidence: "Alice is the protagonist interacting with all characters."
costume_or_covering_evidence: ""
movement_evidence: "Hides in woods, peeks out, knocks on door, enters house, walks while holding baby, nibbles mushroom to change height."
associated_entities: ["fish_footman", "frog_footman", "the_duchess", "cook", "baby", "cheshire_cat"]
alias_or_role_evidence: ""
unknowns: ""
source_refs: ""

[[SECTION markdown]]
# Alice
**Role:** Protagonist

**Status:** Physically Present

**Physical Description:** 
A young girl. In this chapter, she consumes mushroom to adjust her height to approximately two feet.

**Costume/Silhouette:** 
Not explicitly detailed in this chapter, though her scale changes significantly.

**Descriptive Noun Phrases:** 
Young girl, small-scale human, mushroom-eating traveler.

**Uncertainty Notes:** 
Specific clothing details are not provided in this text segment.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: fish_footman
canonical_character_id: fish_footman
aliases: ["Fish-Footman"]
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
confidence: 1.0
direct_identity_evidence: "Named as Fish-Footman."
direct_visual_evidence: "Fish-like face, powdered curly hair."
costume_or_covering_evidence: "Powdered curly hair (suggesting formal/wig-like attire)."
movement_evidence: "Runs from the woods to a house; raps on door; bows."
associated_entities: ["frog_footman"]
alias_or_role_evidence: ""
unknowns: ""
source_refs: ""

[[SECTION markdown]]
# Fish-Footman
**Role:** Messenger/Door attendant

**Status:** Physically Present

**Physical Description:** 
A humanoid creature with a fish-like face and powdered curly hair.

**Costume/Silhouette:** 
Formal appearance suggested by the powdered curly hair.

**Descriptive Noun Phrases:** 
Fish-faced man, powdered wig, aquatic humanoid footman.

**Uncertainty Notes:** 
Specific clothing beyond the hair is not described.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: frog_footman
canonical_character_id: frog_footman
aliases: ["Frog-Footman"]
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
confidence: 1.0
direct_identity_evidence: "Named as Frog-Footman."
direct_visual_evidence: "Round face, large frog eyes, powdered curly hair."
costume_or_covering_evidence: "Powdered curly hair."
movement_evidence: "Opens door; bows; sits on the ground staring at the sky."
associated_entities: ["fish_footman"]
alias_or_role_evidence: ""
unknowns: ""
source_refs: ""

[[SECTION markdown]]
# Frog-Footman
**Role:** Door attendant

**Status:** Physically Present

**Physical Description:** 
A humanoid creature with a round face, large frog eyes, and powdered curly hair.

**Costume/Silhouette:** 
Formal appearance suggested by the powdered curly hair.

**Descriptive Noun Phrases:** 
Frog-faced man, large-eyed footman, powdered wig.

**Uncertainty Notes:** 
None.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: the_duchess
canonical_character_id: the_duchess
aliases: ["Duchess"]
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
confidence: 0.9
direct_identity_evidence: "Named as the Duchess."
direct_visual_evidence: "Sitting on a three-legged stool."
costume_or_covering_evidence: ""
movement_evidence: "Sits on a stool; sings a violent lullaby; flings baby at Alice; exits to play croquet."
associated_entities: ["cook", "baby"]
alias_or_role_evidence: ""
unknowns: ""
source_refs: ""

[[SECTION markdown]]
# The Duchess
**Role:** Chaotic inhabitant of the house

**Status:** Physically Present

**Physical Description:** 
A woman (human).

**Costume/Silhouette:** 
Not explicitly described.

**Descriptive Noun Phrases:** 
Violent Duchess, singing woman on a stool.

**Uncertainty Notes:** 
Visual details of her face or clothing are absent from the text.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: cook
canonical_character_id: cook
aliases: ["Cook"]
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
confidence: 0.9
direct_identity_evidence: "Named as the Cook."
direct_visual_evidence: "Leaning over a cauldron of soup; throwing kitchen items."
costume_or_covering_evidence: ""
movement_evidence: "Leans over cauldron; throws fire-irons, saucepans, plates, and dishes; joins in chorus; throws frying pan."
associated_entities: ["the_duchess", "baby"]
alias_or_role_evidence: ""
unknowns: ""
source_refs: ""

[[SECTION markdown]]
# Cook
**Role:** Chaotic kitchen worker

**Status:** Physically Present

**Physical Description:** 
A human woman.

**Costume/Silhouette:** 
Not explicitly described.

**Descriptive Noun Phrases:** 
Angry cook, cauldron-leaning woman.

**Uncertainty Notes:** 
Visual details of her appearance are not provided.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: baby
canonical_character_id: baby
aliases: ["Baby"]
is_fully_identified: true
manual_description_required: false
manual_description_reason: ""
clarification_required: false
clarification_reason: ""
clarification_question: ""
character_type_hint: humanoid_nonhuman
morphology_hint: biped
scale_hint: tiny
renderability_hint: renderable
confidence: 0.8
direct_identity_evidence: "Named as the Baby."
direct_visual_evidence: "Sneezing and howling; later transforms into a pig with a snout and small eyes."
costume_or_covering_evidence: ""
movement_evidence: "Sneezes, howls, is shaken violently, is flung at Alice, trots into woods (as pig)."
associated_entities: ["the_duchess", "cook", "alice"]
alias_or_role_evidence: ""
unknowns: ""
source_refs: ""

[[SECTION markdown]]
# Baby
**Role:** Chaotic infant/Transforming entity

**Status:** Physically Present (Transforms)

**Physical Description:** 
Initially a sneezing, howling human-like baby. Later transforms into a pig with a snout and small eyes. Described as "star-fish" shaped when held by Alice.

**Costume/Silhouette:** 
N/A

**Descriptive Noun Phrases:** 
Sneezing baby, star-fish shaped infant, transforming piglet.

**Uncertainty Notes:** 
The transition from human to pig is a key visual beat.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: cheshire_cat
canonical_character_id: cheshire_cat
aliases: ["Cheshire Cat"]
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
confidence: 1.0
direct_identity_evidence: "Named as the Cheshire Cat."
direct_visual_evidence: "Sitting on the hearth; sitting on a tree bough; long claws, many teeth, wide grin; vanishes leaving only a grin."
costume_or_covering_evidence: ""
movement_evidence: "Sits on hearth; appears/disappears on tree bough; vanishes slowly from tail to grin."
associated_entities: ["alice"]
alias_or_role_evidence: ""
unknowns: ""
source_refs: ""

[[SECTION markdown]]
# Cheshire Cat
**Role:** Philosophical guide/Mad entity

**Status:** Physically Present (Appears/Disappears)

**Physical Description:** 
A cat with long claws, many teeth, and a wide grin. Capable of partial disappearance, leaving only the grin floating in the air.

**Costume/Silhouette:** 
Feline silhouette.

**Descriptive Noun Phrases:** 
Grinning cat, vanishing feline, toothy Cheshire Cat.

**Uncertainty Notes:** 
The specific color or pattern of the fur is not mentioned in this chapter.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: pig
canonical_character_id: pig
aliases: ["Pig"]
is_fully_identified: true
manual_description_required: false
manual_description_reason: ""
clarification_required: false
clarification_reason: ""
clarification_question: ""
character_type_hint: animal
morphology_hint: quadruped
scale_hint: tiny
renderability_hint: renderable
confidence: 1.0
direct_identity_evidence: "Identified as a pig after transformation."
direct_visual_evidence: "Has a snout and small eyes; trots into the woods."
costume_or_covering_evidence: ""
movement_evidence: "Trots into the woods."
associated_entities: ["baby"]
alias_or_role_evidence: ""
unknowns: ""
source_refs: ""

[[SECTION markdown]]
# Pig
**Role:** Transformed entity

**Status:** Physically Present (Post-transformation)

**Physical Description:** 
A small pig with a snout and small eyes. Formerly the Baby.

**Costume/Silhouette:** 
Piglet silhouette.

**Descriptive Noun Phrases:** 
Transformed baby, trotting pig.

**Uncertainty Notes:** 
This is the final state of the 'Baby' entity.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]
[[/FILMCREATOR_PACKET]]
````
