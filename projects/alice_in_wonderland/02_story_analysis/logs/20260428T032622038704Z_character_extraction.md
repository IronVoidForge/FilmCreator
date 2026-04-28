# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-28T03:26:22.038704+00:00
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
*   **Event:** A Frog-Footman (round face, large eyes, powdered curly hair) opens the door.
*   **Interaction/Object:** The Fish-Footman presents a massive letter (size of a man) to the Frog-Footman; it is an invitation from the Queen for the Duchess to play croquet.
*   **Visual Detail:** Both footmen bow low, and their powdered curls become entangled.
*   **Event:** Alice hides in the woods, laughing at the entanglement, then peeks out to see the Fish-Footman gone; the Frog-Footman is now sitting on the ground staring at the sky.
*   **Interaction:** Alice knocks on the door. The Frog-Footman refuses to help, noting he is on her side of the door and that loud noises are coming from inside.
*   **Audio/Visual Continuity:** Inside the house, there is constant howling, sneezing, and the sound of breaking dishes/kettles.
*   **Event:** A large plate skims out of the house, narrowly missing the Frog-Footman's nose, and breaks against a tree. The Footman remains indifferent.
*   **Decision:** Alice decides to ignore the Footman's idiocy and opens the door to enter.

**Location: The Kitchen (Interior)**
*   **Environment/Atmosphere:** A large, smoke-filled kitchen. High concentration of pepper in the air causing sneezing.
*   **Characters Present:** 
    *   The Duchess (sitting on a three-legged stool).
    *   The Cook (leaning over a fire, stirring a large cauldron of soup).
    *   The Baby (sneezing and howling).
    *   The Cheshire Cat (sitting on the hearth, grinning widely).
*   **Interaction:** Alice asks why the cat is grinning. The Duchess identifies it as a Cheshire Cat and shouts "Pig!" at the baby.
*   **Event/Action:** The Cook begins throwing kitchen items (fire-irons, saucepans, plates, dishes) at the Duchess and the baby. 
*   **Visual Detail:** The Duchess remains indifferent to being hit; Alice jumps in terror as a large saucepan nearly hits the baby's nose.
*   **Dialogue/Conflict:** Alice attempts to discuss the rotation of the earth (24 hours). The Duchess responds by telling the Cook to "chop off her head!"
*   **Event/Performance:** The Duchess sings a violent lullaby, shaking the baby violently at the end of every line. The Cook and Baby join in a chorus ("Wow! wow! wow!").
*   **Exit/Transition:** The Duchess flings the baby at Alice and exits to play croquet; the Cook throws a frying pan after her (misses).

**Location: Outside / The Woods**
*   **Character State:** Alice holds the "star-fish" shaped, snorting baby. She learns the "proper" way to nurse it: twisting it into a knot and holding its right ear and left foot.
*   **Transformation Event:** As Alice walks, the baby's nose becomes snout-like and eyes shrink. The baby grunts/sobs and transforms completely into a pig.
*   **Event:** Alice sets the pig down; it trots into the woods.
*   **Character Entrance:** The Cheshire Cat appears on a tree bough. 
*   **Visual Detail:** The Cat has very long claws and many teeth, but maintains a good-natured grin.
*   **Interaction/Dialogue:** The Cat provides directions. It informs Alice that the Hatter and March Hare live in different directions and that both are mad.
*   **Logic/Reveal:** The Cat argues they are all mad, using its own behavior (growling when pleased) as proof of madness.
*   **Visual Effect:** The Cat vanishes, then reappears, then vanishes again—this time vanishing slowly, starting with the tail and ending with a lingering grin.
*   **Event/Transition:** Alice walks toward the March Hare's house. 
*   **Location Detail:** The March Hare's house has chimneys shaped like ears and a thatched roof made of fur.
*   **Scale Shift:** Alice nibbles more mushroom to raise her height to approximately two feet before approaching the house.
````

## Raw Response
````text
[[FILMCREATOR_PACKET]]
[SECTION character_index_markdown]
[[SECTION markdown]]
# Character Index - Chapter 6

## Visible Characters
- [Fish-Footman](#fish_footman)
- [Frog-Footman](#frog_footman)
- [Alice](#alice)
- [The Duchess](#the_duchess)
- [The Cook](#the_cook)
- [The Baby](#the_baby)
- [Cheshire Cat](#cheshire_cat)
- [Pig](#pig)

## Referenced Characters
- [The Queen](#the_queen)
- [The Hatter](#the_hatter)
- [March Hare](#march_hare)
[[/SECTION]]
[[/SECTION]]

[[FILMCREATOR_RECORD]]
type=character
asset_id=fish_footman
canonical_character_id=fish_footman
aliases=[]
is_fully_identified=true
manual_description_required=false
manual_description_reason=""
clarification_required=false
clarification_reason=""
clarification_question=""
character_type_hint=humanoid_nonhuman
morphology_hint=biped
scale_hint=human_scale
renderability_hint=renderable
confidence=0.9
direct_identity_evidence="Fish-Footman"
direct_visual_evidence="fish-like face, powdered curly hair"
costume_or_covering_evidence="powdered curly hair"
movement_evidence="runs from the woods to a house and raps on the door; bows low"
associated_entities=["frog_footman"]
alias_or_role_evidence=""
unknowns=[]
source_refs=[]
[[SECTION markdown]]
# Fish-Footman
**Role:** Messenger/Footman

**Status:** Physically Present

**Physical Description:**
A humanoid figure with a fish-like face. He wears powdered curly hair.

**Costume & Silhouette:**
Characterized by his distinctive powdered curls which can become entangled with other characters during bowing.

**Descriptive Noun Phrases:**
Fish-faced footman, powdered curly hair, messenger of the Queen.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type=character
asset_id=frog_footman
canonical_character_id=frog_footman
aliases=[]
is_fully_identified=true
manual_description_required=false
manual_description_reason=""
clarification_required=false
clarification_reason=""
clarification_question=""
character_type_hint=humanoid_nonhuman
morphology_hint=biped
scale_hint=human_scale
renderability_hint=renderable
confidence=0.9
direct_identity_evidence="Frog-Footman"
direct_visual_evidence="round face, large eyes, powdered curly hair"
costume_or_covering_evidence="powdered curly hair"
movement_evidence="opens the door; bows low; sits on the ground staring at the sky"
associated_entities=["fish_footman"]
alias_or_role_evidence=""
unknowns=[]
source_refs=[]
[[SECTION markdown]]
# Frog-Footman
**Role:** Doorman/Footman

**Status:** Physically Present

**Physical Description:**
A humanoid figure with a round face and large eyes. He wears powdered curly hair.

**Costume & Silhouette:**
Characterized by his distinctive powdered curls which can become entangled with the Fish-Footman during bowing.

**Descriptive Noun Phrases:**
Frog-faced footman, large-eyed doorman, powdered curly hair.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type=character
asset_id=alice
canonical_character_id=alice
aliases=[]
is_fully_identified=true
manual_description_required=false
manual_description_reason=""
clarification_required=false
clarification_reason=""
clarification_question=""
character_type_hint=human
morphology_hint=biped
scale_hint=small
renderability_hint=renderable
confidence=1.0
direct_identity_evidence="Alice"
direct_visual_evidence="hides in the woods; peeks out; knocks on door; holds baby; nibbles mushroom to reach two feet height"
costume_or_covering_evidence=""
movement_evidence="hiding, peeking, walking, holding a baby, nibbling mushroom"
associated_entities=["the_baby", "cheshire_cat"]
alias_or_role_evidence=""
unknowns=[]
source_refs=[]
[[SECTION markdown]]
# Alice
**Role:** Protagonist

**Status:** Physically Present

**Physical Description:**
A young girl. Her scale fluctuates due to mushroom consumption; in this chapter, she reaches approximately two feet in height.

**Costume & Silhouette:**
Not explicitly described in this chapter.

**Descriptive Noun Phrases:**
Young girl, small-scale explorer, mushroom-nibbling traveler.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type=character
asset_id=the_duchess
canonical_character_id=the_duchess
aliases=[]
is_fully_identified=true
manual_description_required=false
manual_description_reason=""
clarification_required=false
clarification_reason=""
clarification_question=""
character_type_hint=human
morphology_hint=biped
scale_hint=human_scale
renderability_hint=renderable
confidence=0.8
direct_identity_evidence="The Duchess"
direct_visual_evidence="sitting on a three-legged stool; indifferent to being hit by kitchen items; sings violent lullabies; flings baby"
costume_or_covering_evidence=""
movement_evidence="sitting, singing, shaking baby, flinging baby, exiting"
associated_entities=["the_cook", "the_baby"]
alias_or_role_evidence=""
unknowns=[]
source_refs=[]
[[SECTION markdown]]
# The Duchess
**Role:** Chaotic resident of the house

**Status:** Physically Present

**Physical Description:**
A human woman. Her specific facial features are not detailed, but she exhibits a high degree of indifference to chaos and violence.

**Costume & Silhouette:**
Not explicitly described.

**Descriptive Noun Phrases:**
Indifferent Duchess, violent lullaby singer, chaotic hostess.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type=character
asset_id=the_cook
canonical_character_id=the_cook
aliases=[]
is_fully_identified=true
manual_description_required=false
manual_description_reason=""
clarification_required=false
clarification_reason=""
clarification_question=""
character_type_hint=human
morphology_hint=biped
scale_hint=human_scale
renderability_hint=renderable
confidence=0.8
direct_identity_evidence="The Cook"
direct_visual_evidence="leaning over a fire, stirring a large cauldron of soup; throwing kitchen items (fire-irons, saucepans, plates, dishes) at the Duchess and baby"
costume_or_covering_evidence=""
movement_evidence="stirring, leaning, throwing objects"
associated_entities=["the_duchess", "the_baby"]
alias_or_role_evidence=""
unknowns=[]
source_refs=[]
[[SECTION markdown]]
# The Cook
**Role:** Aggressive kitchen staff

**Status:** Physically Present

**Physical Description:**
A human woman. 

**Costume & Silhouette:**
Not explicitly described, though she is actively engaged in heavy kitchen work (stirring cauldrons).

**Descriptive Noun Phrases:**
Aggressive cook, cauldron-stirrer, projectile-throwing cook.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type=character
asset_id=the_baby
canonical_character_id=the_baby
aliases=[]
is_fully_identified=true
manual_description_required=false
manual_description_reason=""
clarification_required=false
clarification_reason=""
clarification_question=""
character_type_hint=humanoid_nonhuman
morphology_hint=biped
scale_hint=tiny
renderability_hint=renderable
confidence=0.7
direct_identity_evidence="The Baby"
direct_visual_evidence="sneezing and howling; star-fish shaped; snorting; nose becomes snout-like; eyes shrink; transforms into a pig"
costume_or_covering_evidence=""
movement_evidence="sneezing, howling, being shaken, being flung, transforming, trotting"
associated_entities=["the_duchess", "the_cook", "alice"]
alias_or_role_evidence=""
unknowns=[]
source_refs=[]
[[SECTION markdown]]
# The Baby / Pig
**Role:** Chaotic infant/animal

**Status:** Physically Present (Transforms)

**Physical Description:**
Initially a human-like baby with a "star-fish" shape. During transformation, the nose becomes snout-like and eyes shrink until it is completely a pig.

**Costume & Silhouette:**
Star-fish shaped silhouette initially; transitions to a porcine silhouette.

**Descriptive Noun Phrases:**
Star-fish shaped baby, snorting infant, transforming baby, trotting pig.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type=character
asset_id=cheshire_cat
canonical_character_id=cheshire_cat
aliases=[]
is_fully_identified=true
manual_description_required=false
manual_description_reason=""
clarification_required=false
clarification_reason=""
clarification_question=""
character_type_hint=animal
morphology_hint=quadruped
scale_hint=small
renderability_hint=renderable
confidence=1.0
direct_identity_evidence="the Cheshire Cat"
direct_visual_evidence="sitting on the hearth; grinning widely; sitting on a tree bough; very long claws; many teeth; good-natured grin; vanishes and reappears; vanishes slowly starting with tail, ending with lingering grin"
costume_or_covering_evidence=""
movement_evidence="sitting, vanishing, reappearing, disappearing slowly"
associated_entities=[]
alias_or_role_evidence=""
unknowns=[]
source_refs=[]
[[SECTION markdown]]
# Cheshire Cat
**Role:** Guide/Trickster

**Status:** Physically Present

**Physical Description:**
A cat with a wide, lingering grin, very long claws, and many teeth. It has the ability to vanish partially or completely.

**Costume & Silhouette:**
Standard feline silhouette, but capable of partial transparency/vanishing.

**Descriptive Noun Phrases:**
Grinning Cheshire Cat, vanishing cat, long-clawed feline.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type=character
asset_id=pig
canonical_character_id=pig
aliases=[]
is_fully_identified=true
manual_description_required=false
manual_description_reason=""
clarification_required=false
clarification_reason=""
clarification_question=""
character_type_hint=animal
morphology_hint=quadruped
scale_hint=small
renderability_hint=renderable
confidence=1.0
direct_identity_evidence="pig"
direct_visual_evidence="trots into the woods"
costume_or_covering_evidence=""
movement_evidence="trots"
associated_entities=[]
alias_or_role_evidence=""
unknowns=[]
source_refs=[]
[[SECTION markdown]]
# Pig
**Role:** Transformed entity

**Status:** Physically Present (Post-transformation)

**Physical Description:**
A pig that was formerly the baby. 

**Costume & Silhouette:**
Standard porcine silhouette.

**Descriptive Noun Phrases:**
Transformed pig, trotting pig.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type=character
asset_id=the_queen
canonical_character_id=the_queen
aliases=[]
is_fully_identified=false
manual_description_required=true
manual_description_reason="Character is only mentioned as the sender of an invitation; no physical description provided."
clarification_required=true
clarification_question="What is the Queen's physical appearance and attire?"
character_type_hint=human
morphology_hint=biped
scale_hint=human_scale
renderability_hint=context_only
confidence=0.5
direct_identity_evidence=""
direct_visual_evidence=""
costume_or_covering_evidence=""
movement_evidence=""
associated_entities=[]
alias_or_role_evidence="invitation from the Queen"
unknowns=["physical appearance", "clothing"]
source_refs=[]
[[SECTION markdown]]
# The Queen
**Role:** Referenced Authority

**Status:** Referenced Only

**Physical Description:**
Unknown. No physical details are provided in this chapter.

**Costume & Silhouette:**
Unknown.

**Descriptive Noun Phrases:**
The Queen (referenced).
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type=character
asset_id=the_hatter
canonical_character_id=the_hatter
aliases=[]
is_fully_identified=false
manual_description_required=true
manual_description_reason="Character is only mentioned by name; no physical description provided."
clarification_required=true
clarification_question="What does the Hatter look like?"
character_type_hint=humanoid_nonhuman
morphology_hint=biped
scale_hint=human_scale
renderability_hint=context_only
confidence=0.5
direct_identity_evidence=""
direct_visual_evidence=""
costume_or_covering_evidence=""
movement_evidence=""
associated_entities=[]
alias_or_role_evidence="the Hatter"
unknowns=["physical appearance", "clothing"]
source_refs=[]
[[SECTION markdown]]
# The Hatter
**Role:** Referenced Character

**Status:** Referenced Only

**Physical Description:**
Unknown. No physical details are provided in this chapter.

**Costume & Silhouette:**
Unknown.

**Descriptive Noun Phrases:**
The Hatter (referenced).
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type=character
asset_id=march_hare
canonical_character_id=march_hare
aliases=[]
is_fully_identified=false
manual_description_required=true
manual_description_reason="Character is only mentioned by name; no physical description provided."
clarification_required=true
clarification_question="What does the March Hare look like?"
character_type_hint=animal
morphology_hint=quadruped
scale_hint=small
renderability_hint=context_only
confidence=0.5
direct_identity_evidence=""
direct_visual_evidence=""
costume_or_covering_evidence=""
movement_evidence=""
associated_entities=[]
alias_or_role_evidence="March Hare"
unknowns=["physical appearance"]
source_refs=[]
[[SECTION markdown]]
# March Hare
**Role:** Referenced Character

**Status:** Referenced Only

**Physical Description:**
Unknown. No physical details are provided in this chapter.

**Costume & Silhouette:**
Unknown.

**Descriptive Noun Phrases:**
March Hare (referenced).
[[/SECTION]]
[[/FILMCREATOR_RECORD]]
[[/FILMCREATOR_PACKET]]
````
