# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-28T03:27:09.331642+00:00
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
[[SECTION character_index_markdown]]
[[markdown]]
# Character Index

- [Alice](#alice)
- [Cheshire Cat](#cheshire_cat)
- [Cook](#cook)
- [Duchess](#duchess)
- [Fish-Footman](#fish_footman)
- [Frog-Footman](#frog_footman)
- [March Hare](#march_hare) (referenced)
- [the Baby / Pig](#the_baby_pig)

---

## Alice
**Role:** Protagonist. Present in chapter.

## Cheshire Cat
**Role:** Guide/Enigma. Present in chapter.

## Cook
**Role:** Chaotic kitchen staff. Present in chapter.

## Duchess
**Role:** Hostile resident. Present in chapter.

## Fish-Footman
**Role:** Messenger. Present in chapter.

## Frog-Footman
**Role:** Doorman. Present in chapter.

## March Hare
**Role:** Resident (referenced).

## The Baby / Pig
**Role:** Transforming infant/animal. Present in chapter.
[[/SECTION]]
[[/FILMCREATOR_PACKET]]

[[FILMCREATOR_RECORD]]
[[SECTION markdown]]
# Alice
**Role:** Protagonist

### Status
Physically present.

### Description
- **Physicality:** Height fluctuates (nibbles mushroom to reach approx. 2 feet).
- **Traits:** Observant, reactive to chaos, attempts logical discourse.

### Prompting Keywords
- young girl, curious expression, varying scale, interacting with magical creatures.
[[/SECTION]]
asset_id: alice
canonical_character_id: alice
aliases: []
is_fully_identified: true
manual_description_required: false
manual_description_reason: 
clarification_required: false
clarification_reason: 
clarification_question: 
character_type_hint: human
morphology_hint: human
scale_hint: variable (approx 2ft at end of chapter)
renderability_hint: high
confidence: 1.0
direct_identity_evidence: "Alice knocks on the door."
direct_visual_evidence: "Alice jumps in terror..."
costume_or_covering_evidence: 
movement_evidence: "Alice walks toward the March Hare's house."
associated_entities: [the_baby_pig, cheshire_cat]
alias_or_role_evidence: 
unknowns: 
source_refs: CH006
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
[[SECTION markdown]]
# Cheshire Cat
**Role:** Guide / Enigma

### Status
Physically present.

### Description
- **Physicality:** Sitting on a hearth, then on a tree bough. Large grin. Very long claws and many teeth.
- **Behavior:** Vanishes and reappears; vanishes slowly starting with the tail until only the grin remains. Growls when pleased.

### Prompting Keywords
- grinning cat, wide smile, long claws, sharp teeth, disappearing effect, fading grin, magical feline.
[[/SECTION]]
asset_id: cheshire_cat
canonical_character_id: cheshire_cat
aliases: []
is_fully_identified: true
manual_description_required: false
manual_description_reason: 
clarification_required: false
clarification_reason: 
clarification_question: 
character_type_hint: animal
morphology_hint: feline
scale_hint: standard cat
renderability_hint: high (requires vanishing VFX)
confidence: 1.0
direct_identity_evidence: "The Duchess identifies it as a Cheshire Cat"
direct_visual_evidence: "sitting on the hearth, grinning widely", "very long claws and many teeth", "vanishing slowly... ending with a lingering grin"
costume_or_covering_evidence: 
movement_evidence: "appears on a tree bough", "vanishes, then reappears"
associated_entities: [alice]
alias_or_role_evidence: 
unknowns: 
source_refs: CH006
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
[[SECTION markdown]]
# Cook
**Role:** Chaotic kitchen staff

### Status
Physically present.

### Description
- **Physicality:** Leaning over a fire, stirring a large cauldron of soup.
- **Behavior:** Violent/Aggressive; throws kitchen items (fire-irons, saucepans, plates, dishes) at the Duchess and baby. Joins in singing "Wow! wow! wow!".

### Prompting Keywords
- cook, apron, stirring cauldron, throwing pans, aggressive movement, chaotic kitchen setting.
[[/SECTION]]
asset_id: cook
canonical_character_id: cook
aliases: []
is_fully_identified: true
manual_description_required: false
manual_description_reason: 
clarification_required: false
clarification_reason: 
clarification_question: 
character_type_hint: human
morphology_hint: human
scale_hint: standard adult
renderability_hint: high
confidence: 1.0
direct_identity_evidence: "The Cook begins throwing kitchen items"
direct_visual_evidence: "leaning over a fire, stirring a large cauldron of soup"
costume_or_covering_evidence: 
movement_evidence: "throwing kitchen items", "joins in a chorus"
associated_entities: [duchess, the_baby_pig]
alias_or_role_evidence: 
unknowns: 
source_refs: CH006
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
[[SECTION markdown]]
# Duchess
**Role:** Hostile resident

### Status
Physically present.

### Description
- **Physicality:** Sitting on a three-legged stool. Indifferent to being hit by flying objects.
- **Behavior:** Shouts at the baby, sings violent lullabies while shaking the baby, tells the cook to "chop off [Alice's] head!".

### Prompting Keywords
- woman, sitting on three-legged stool, indifferent expression, singing aggressively, chaotic kitchen environment.
[[/SECTION]]
asset_id: duchess
canonical_character_id: duchess
aliases: []
is_fully_identified: true
manual_description_required: false
manual_description_reason: 
clarification_required: false
clarification_reason: 
clarification_question: 
character_type_hint: human
morphology_hint: human
scale_hint: standard adult
renderability_hint: high
confidence: 1.0
direct_identity_evidence: "The Duchess (sitting on a three-legged stool)."
direct_visual_evidence: "sitting on a three-legged stool", "remains indifferent to being hit"
costume_or_covering_evidence: 
movement_evidence: "sings a violent lullaby", "flings the baby at Alice"
associated_entities: [the_baby_pig, cook]
alias_or_role_evidence: 
unknowns: 
source_refs: CH006
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
[[SECTION markdown]]
# Fish-Footman
**Role:** Messenger

### Status
Physically present.

### Description
- **Physicality:** Fish-like face, powdered curly hair.
- **Behavior:** Runs from woods to house, raps on door, bows low (entangling hair with Frog-Footman).

### Prompting Keywords
- fish-faced man, humanoid fish, powdered curly hair, formal footman attire, bowing.
[[/SECTION]]
asset_id: fish_footman
canonical_character_id: fish_footman
aliases: []
is_fully_identified: true
manual_description_required: false
manual_description_reason: 
clarification_required: false
clarification_reason: 
clarification_question: 
character_type_hint: humanoid
morphology_hint: fish-faced human
scale_hint: standard adult
renderability_hint: high
confidence: 1.0
direct_identity_evidence: "A Fish-Footman... runs from the woods"
direct_visual_evidence: "fish-like face, powdered curly hair"
costume_or_covering_evidence: "powdered curly hair"
movement_evidence: "runs from the woods", "raps on the door", "bows low"
associated_entities: [frog_footman]
alias_or_role_evidence: 
unknowns: 
source_refs: CH006
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
[[SECTION markdown]]
# Frog-Footman
**Role:** Doorman

### Status
Physically present.

### Description
- **Physicality:** Round face, large eyes, powdered curly hair.
- **Behavior:** Opens door, bows low (entangling hair with Fish-Footman), sits on ground staring at sky, refuses to help Alice.

### Prompting Keywords
- frog-faced man, humanoid frog, round face, large eyes, powdered curly hair, formal footman attire.
[[/SECTION]]
asset_id: frog_footman
canonical_character_id: frog_footman
aliases: []
is_fully_identified: true
manual_description_required: false
manual_description_reason: 
clarification_required: false
clarification_reason: 
clarification_question: 
character_type_hint: humanoid
morphology_hint: frog-faced human
scale_hint: standard adult
renderability_hint: high
confidence: 1.0
direct_identity_evidence: "A Frog-Footman... opens the door."
direct_visual_evidence: "round face, large eyes, powdered curly hair"
costume_or_covering_evidence: "powdered curly hair"
movement_evidence: "opens the door", "bows low", "sitting on the ground staring at the sky"
associated_entities: [fish_footman]
alias_or_role_evidence: 
unknowns: 
source_refs: CH006
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
[[SECTION markdown]]
# March Hare
**Role:** Resident (referenced)

### Status
Referenced.

### Description
- **Notes:** Lives in a house with chimneys shaped like ears and a thatched roof made of fur. Described as "mad".

### Prompting Keywords
- mad hare, whimsical rabbit character.
[[/SECTION]]
asset_id: march_hare
canonical_character_id: march_hare
aliases: []
is_fully_identified: false
manual_description_required: true
manual_description_reason: "Character is only referenced via dialogue and house description; no direct visual of the hare itself."
clarification_required: false
clarification_reason: 
clarification_question: 
character_type_hint: animal
morphology_hint: hare
scale_hint: unknown
renderability_hint: medium
confidence: 0.5
direct_identity_evidence: "the Hatter and March Hare live in different directions"
direct_visual_evidence: 
costume_or_covering_evidence: 
movement_evidence: 
associated_entities: [alice]
alias_or_role_evidence: 
unknowns: "Physical appearance of the hare."
source_refs: CH006
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
[[SECTION markdown]]
# The Baby / Pig
**Role:** Transforming infant/animal

### Status
Physically present.

### Description
- **Initial State (Baby):** Sneezing and howling; "star-fish" shaped; snorting.
- **Transformation:** Nose becomes snout-like, eyes shrink.
- **Final State (Pig):** A pig that trots into the woods.

### Prompting Keywords
- starfish shaped baby, snorting infant, transforming baby, piglet, snout, small animal.
[[/SECTION]]
asset_id: the_baby_pig
canonical_character_id: the_baby_pig
aliases: [the Baby, Pig]
is_fully_identified: true
manual_description_required: false
manual_description_reason: 
clarification_required: false
clarification_reason: 
clarification_question: 
character_type_hint: animal
morphology_hint: starfish-shaped infant transitioning to pig
scale_hint: small/infant
renderability_hint: high (requires transformation VFX)
confidence: 1.0
direct_identity_evidence: "The Baby (sneezing and howling)", "transforms completely into a pig"
direct_visual_evidence: "star-fish shaped, snorting baby", "nose becomes snout-like and eyes shrink"
costume_or_covering_evidence: 
movement_evidence: "sneezing and howling", "trots into the woods"
associated_entities: [duchess, alice]
alias_or_role_evidence: 
unknowns: 
source_refs: CH006
[[/FILMCREATOR_RECORD]]
````
