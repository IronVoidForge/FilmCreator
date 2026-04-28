# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-28T03:37:49.498516+00:00
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

**Location: The House Exterior / Woods**
- **Event:** A Fish-Footman (fish-like face, powdered curly hair) runs from the woods to a house and raps on the door.
- **Character Entrance:** A Frog-Footman (round face, large eyes, powdered curly hair) opens the door.
- **Interaction/Object:** The Fish-Footman presents a massive letter (size of a man) to the Frog-Footman; it is an invitation from the Queen for the Duchess to play croquet.
- **Visual Gag:** Both footmen bow low and their powdered curls become entangled.
- **Character Action:** Alice hides in the woods, laughing, then peeks out. The Fish-Footman exits; the Frog-Footman sits on the ground staring at the sky.
- **Interaction:** Alice knocks. The Frog-Footman refuses to help because he is on the same side of the door as her and the noise inside is too loud (howling, sneezing, crashing).
- **Visual/Sound Event:** A large plate skims out of the house, grazes the Frog-Footman's nose, and breaks against a tree. The Footman remains indifferent.
- **Decision:** Alice decides to enter the house despite the Footman's apathy.

**Location: The Kitchen (Interior)**
- **Environment/Atmosphere:** Thick smoke; heavy presence of pepper causing constant sneezing.
- **Character Entrances/Presence:** 
    - The Duchess: Sitting on a three-legged stool, nursing a baby.
    - The Cook: Leaning over a fire, stirring a large cauldron of soup.
    - The Cheshire Cat: Sitting on the hearth, grinning widely.
- **Interaction:** Alice asks why the cat is grinning. The Duchess identifies it as a Cheshire Cat and shouts "Pig!" at the baby.
- **Conflict/Action:** The Cook begins throwing kitchen items (fire-irons, saucepans, plates, dishes) at the Duchess and the baby. 
- **Visual Continuity:** The Duchess remains unbothered by the projectiles; the baby is constantly howling and sneezing. A large saucepan nearly hits the baby's nose.
- **Dialogue/Decision:** Alice attempts to discuss the earth's rotation; the Duchess responds by ordering "Chop off her head!" 
- **Performance/Sound:** The Duchess sings a violent lullaby, shaking the baby at the end of every line. The Cook and Baby join in a chorus of "Wow! wow! wow!"
- **Character Exit/Transition:** The Duchess flings the baby at Alice and exits to play croquet; the Cook throws a frying pan at her (misses).

**Location: Exterior / Woods (Near the House)**
- **Object Interaction:** Alice catches the "starfish-shaped" baby. She learns to nurse it by twisting it into a knot, holding its right ear and left foot.
- **Transformation Event:** As Alice carries the baby outside, the creature's nose becomes a snout and eyes shrink. The baby grunts/sobs and transforms into a pig.
- **Character Action:** Alice sets the pig down; it trots into the woods.
- **Character Entrance:** The Cheshire Cat appears on a tree bough. 
- **Interaction/Dialogue:** Alice asks for directions. The Cat explains that everyone is mad (including Alice). The Cat uses its own behavior (growling when pleased, wagging tail when angry) to prove its madness.
- **Visual Effect:** The Cat mentions the croquet game and vanishes. It reappears, asks about the baby, and then vanishes slowly—starting with the tail and ending with a lingering grin.

**Location: March Hare's House (Exterior)**
- **Environment/Setting:** A large house with chimneys shaped like ears and a roof thatched with fur.
- **Character Action/Scale Shift:** Alice nibbles on a piece of mushroom to adjust her height to approximately two feet.
- **Decision:** Alice approaches the house timidly, feeling uncertain about visiting the March Hare versus the Hatter.
````

## Raw Response
````text
[[FILMCREATOR_PACKET]]
task: character_extraction
version: 1

[[FILMCREATOR_RECORD]]
asset_id: fish_footman
canonical_character_id: fish_footman
aliases: []
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
direct_identity_evidence: "Identified as Fish-Footman."
direct_visual_evidence: "Fish-like face, powdered curly hair."
costume_or_covering_evidence: "Powdered curly hair (suggests wig or formal styling)."
movement_evidence: "Runs from the woods to a house; bows low."
associated_entities: ["frog_footman", "queen_of_hearts"]
alias_or_role_evidence: ""
unknowns: []
source_refs: []
[[SECTION character_index_markdown]]
[[SECTION markdown]]
# Fish-Footman
**Role:** Messenger/Footman

**Status:** Physically Present

**Physical Description:**
- Fish-like facial features.
- Wears or possesses powdered curly hair (likely a formal wig).

**Visual Cues:**
- Bipedal movement.
- Formal, bowing posture.

**Uncertainty Notes:**
- Specific fish species for the face is not defined.
[[/SECTION]]
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
asset_id: frog_footman
canonical_character_id: frog_footman
aliases: []
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
direct_identity_evidence: "Identified as Frog-Footman."
direct_visual_evidence: "Round face, large eyes, powdered curly hair."
costume_or_covering_evidence: "Powdered curly hair (likely a formal wig)."
movement_evidence: "Opens door; bows low; sits on the ground staring at the sky."
associated_entities: ["fish_footman"]
alias_or_role_evidence: ""
unknowns: []
source_refs: []
[[SECTION character_index_markdown]]
[[SECTION markdown]]
# Frog-Footman
**Role:** Doorman/Footman

**Status:** Physically Present

**Physical Description:**
- Round face.
- Large eyes.
- Powdered curly hair (likely a formal wig).

**Visual Cues:**
- Bipedal movement.
- Formal, bowing posture.
- Indifferent temperament.

**Uncertainty Notes:**
- Specific frog species is not defined.
[[/SECTION]]
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
asset_id: alice
canonical_character_id: alice
aliases: ["Alice"]
is_fully_identified: true
manual_description_required: false
manual_description_reason: ""
clarification_required: false
clarification_reason: ""
clarification_question: ""
character_type_hint: human
morphology_hint: biped
scale_hint: variable
renderability_hint: renderable
confidence: 1.0
direct_identity_evidence: "Identified as Alice."
direct_visual_evidence: "N/A (Visuals described via actions and scale changes)."
costume_or_covering_evidence: ""
movement_evidence: "Hides in woods; peeks out; knocks on door; carries baby; nibbles mushroom to change height."
associated_entities: ["cheshire_cat", "duchess", "baby_pig"]
alias_or_role_evidence: ""
unknowns: []
source_refs: []
[[SECTION character_index_markdown]]
[[SECTION markdown]]
# Alice
**Role:** Protagonist

**Status:** Physically Present

**Physical Description:**
- Scale is variable (shrinks to approximately two feet via mushroom).

**Visual Cues:**
- Humanoid.

**Uncertainty Notes:**
- Specific clothing or hair color not mentioned in this chapter.
[[/SECTION]]
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
asset_id: queen_of_hearts
canonical_character_id: queen_of_hearts
aliases: ["the Queen"]
is_fully_identified: true
manual_description_required: true
manual_description_reason: "The character is only referenced via a letter; no physical description provided."
clarification_required: false
clarification_reason: ""
clarification_question: ""
character_type_hint: humanoid
morphology_hint: biped
scale_hint: human_scale
renderability_hint: context_only
confidence: 0.5
direct_identity_evidence: "The letter is an invitation from the Queen."
direct_visual_evidence: ""
costume_or_covering_evidence: ""
movement_evidence: ""
associated_entities: ["fish_footman", "duchess"]
alias_or_role_evidence: ""
unknowns: []
source_refs: []
[[SECTION character_index_markdown]]
[[SECTION markdown]]
# Queen of Hearts
**Role:** Authority Figure (Referenced)

**Status:** Referenced

**Physical Description:**
- Unknown.

**Visual Cues:**
- N/A

**Uncertainty Notes:**
- No physical description available in this chapter.
[[/SECTION]]
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
asset_id: duchess
canonical_character_id: duchess
aliases: ["The Duchess"]
is_fully_identified: true
manual_description_required: true
manual_description_reason: "No specific physical features (hair, eyes, etc.) are described, only her actions and role."
clarification_required: false
clarification_reason: ""
clarification_question: ""
character_type_hint: human
morphology_hint: biped
scale_hint: human_scale
renderability_hint: renderable
confidence: 0.7
direct_identity_evidence: "Identified as the Duchess."
direct_visual_evidence: ""
costume_or_covering_evidence: ""
movement_evidence: "Sitting on a three-legged stool; flings baby at Alice; exits to play croquet."
associated_entities: ["baby_pig", "cook", "alice"]
alias_or_role_evidence: ""
unknowns: []
source_refs: []
[[SECTION character_index_markdown]]
[[SECTION markdown]]
# The Duchess
**Role:** Resident of the house

**Status:** Physically Present

**Physical Description:**
- Unknown.

**Visual Cues:**
- Humanoid.

**Uncertainty Notes:**
- Lacks specific physical descriptors for rendering.
[[/SECTION]]
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
asset_id: cook
canonical_character_id: cook
aliases: ["The Cook"]
is_fully_identified: true
manual_description_required: true
manual_description_reason: "No specific physical features described."
clarification_required: false
clarification_reason: ""
clarification_question: ""
character_type_hint: human
morphology_hint: biped
scale_hint: human_scale
renderability_hint: renderable
confidence: 0.7
direct_identity_evidence: "Identified as the Cook."
direct_visual_evidence: ""
costume_or_covering_evidence: ""
movement_evidence: "Leaning over a fire; stirring a cauldron; throwing kitchen items at Duchess/baby; throws frying pan at Alice."
associated_entities: ["duchess", "baby_pig"]
alias_or_role_evidence: ""
unknowns: []
source_refs: []
[[SECTION character_index_markdown]]
[[SECTION markdown]]
# The Cook
**Role:** Kitchen Staff

**Status:** Physically Present

**Physical Description:**
- Unknown.

**Visual Cues:**
- Humanoid.

**Uncertainty Notes:**
- Lacks specific physical descriptors for rendering.
[[/SECTION]]
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
asset_id: cheshire_cat
canonical_character_id: cheshire_cat
aliases: ["the cat", "Cheshire Cat"]
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
direct_identity_evidence: "Identified as the Cheshire Cat."
direct_visual_evidence: "Grinning widely; tail wags when angry; growls when pleased; vanishes starting with the tail, leaving a lingering grin."
costume_or_covering_evidence: ""
movement_evidence: "Sitting on the hearth; sitting on a tree bough; vanishing/reappearing."
associated_entities: ["alice"]
alias_or_role_evidence: ""
unknowns: []
source_refs: []
[[SECTION character_index_markdown]]
[[SECTION markdown]]
# Cheshire Cat
**Role:** Guide/Enigma

**Status:** Physically Present

**Physical Description:**
- A cat capable of vanishing.
- Notable for a wide, lingering grin that remains after the body disappears.

**Visual Cues:**
- Wags tail when angry.
- Growls when pleased.
- Vanishing effect: Body fades away, leaving only the grin.

**Uncertainty Notes:**
- Specific fur color or pattern is not mentioned.
[[/SECTION]]
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
asset_id: baby_pig
canonical_character_id: baby_pig
aliases: ["the baby", "Pig"]
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
direct_identity_evidence: "Transforms from a baby into a pig."
direct_visual_evidence: "Initially a baby; nose becomes a snout and eyes shrink during transformation; eventually a pig."
costume_or_covering_evidence: ""
movement_evidence: "Howling, sneezing, and grunting/sobbing; trots into the woods."
associated_entities: ["duchess", "cook", "alice"]
alias_or_role_evidence: ""
unknowns: []
source_refs: []
[[SECTION character_index_markdown]]
[[SECTION markdown]]
# The Baby (Pig)
**Role:** Chaotic infant/Animal

**Status:** Physically Present (Transforms)

**Physical Description:**
- Starts as a human baby.
- Transforms into a pig: nose becomes a snout, eyes shrink.
- Described by Alice as "starfish-shaped" during the transition.

**Visual Cues:**
- Constant howling and sneezing.
- Grunts/sobs during transformation.

**Uncertainty Notes:**
- The exact appearance of the baby before transformation is not detailed beyond its shape.
[[/SECTION]]
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
asset_id: march_hare
canonical_character_id: march_hare
aliases: ["the March Hare"]
is_fully_identified: true
manual_description_required: true
manual_description_reason: "The character is only mentioned as a destination/location owner; no physical description provided."
clarification_required: false
clarification_reason: ""
clarification_question: ""
character_type_hint: animal
morphology_hint: quadruped
scale_hint: unknown
renderability_hint: context_only
confidence: 0.5
direct_identity_evidence: "March Hare's House."
direct_visual_evidence: ""
costume_or_covering_evidence: ""
movement_evidence: ""
associated_entities: []
alias_or_role_evidence: ""
unknowns: []
source_refs: []
[[SECTION character_index_markdown]]
[[SECTION markdown]]
# March Hare
**Role:** Resident (Referenced)

**Status:** Referenced

**Physical Description:**
- Unknown.

**Visual Cues:**
- N/A

**Uncertainty Notes:**
- No physical description provided in this chapter.
[[/SECTION]]
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
asset_id: mad_hatter
canonical_character_id: mad_hatter
aliases: ["the Hatter"]
is_fully_identified: true
manual_description_required: true
manual_description_reason: "The character is only mentioned as a destination; no physical description provided."
clarification_required: false
clarification_reason: ""
clarification_question: ""
character_type_hint: humanoid
morphology_hint: biped
scale_hint: unknown
renderability_hint: context_only
confidence: 0.5
direct_identity_evidence: "Alice considers visiting the Hatter."
direct_visual_evidence: ""
costume_or_covering_evidence: ""
movement_evidence: ""
associated_entities: []
alias_or_role_evidence: ""
unknowns: []
source_refs: []
[[SECTION character_index_markdown]]
[[SECTION markdown]]
# Mad Hatter
**Role:** Potential contact (Referenced)

**Status:** Referenced

**Physical Description:**
- Unknown.

**Visual Cues:**
- N/A

**Uncertainty Notes:**
- No physical description provided in this chapter.
[[/SECTION]]
[[/SECTION]]
[[/FILMCREATOR_RECORD]]
[[/FILMCREATOR_PACKET]]
````
