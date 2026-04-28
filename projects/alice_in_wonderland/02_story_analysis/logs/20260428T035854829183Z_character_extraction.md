# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-28T03:58:54.829183+00:00
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

Chapter id: CH001

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

**Location: Riverbank**
- **Characters:** Alice, Sister (off-screen/passive).
- **Events:** Alice sits by a riverbank on a hot day; she expresses boredom with her sister's book (no pictures or conversations).
- **Visual State:** Sunny, sleepy atmosphere.

**Location: The Hedge / Rabbit-Hole Entrance**
- **Characters:** Alice, White Rabbit.
- **Events:** A White Rabbit with pink eyes runs past Alice. The Rabbit checks a watch from its waistcoat-pocket and exclaims, "Oh dear! Oh dear! I shall be late!" Alice, driven by curiosity, chases the Rabbit. The Rabbit enters a large rabbit-hole under a hedge; Alice follows immediately.

**Location: The Vertical Well/Tunnel**
- **Characters:** Alice (falling).
- **Events:** The hole turns into a deep well. Alice falls slowly. 
- **Environment/Objects:** The walls are lined with cupboards, bookshelves, maps, and pictures on pegs. 
- **Interaction:** Alice grabs an empty jar labeled "ORANGE MARMALADE" from a shelf; she chooses to place it in a cupboard rather than drop it.
- **Internal Monologue/Action:** Alice calculates her depth (approx. 4000 miles) and contemplates the Antipathies. She attempts a curtsey while falling. She drifts into a sleepy state, dreaming of her cat Dinah.
- **Transition:** A loud "thump!" marks the end of the fall as she lands on a heap of sticks and dry leaves.

**Location: The Long Passage / Hall of Doors**
- **Characters:** Alice, White Rabbit (briefly).
- **Events:** Alice jumps up; it is dark overhead. She sees the White Rabbit hurrying down a long passage. She chases him around a corner. 
- **Environment/Objects:** A long, low hall lit by a row of lamps hanging from the roof. Numerous doors line the walls, but all are locked.
- **Discovery 1:** Alice finds a three-legged glass table in the middle of the hall. On it sits a tiny golden key. She tries the key on the large doors; it is too small/the locks are too large.
- **Discovery 2:** Alice finds a low curtain. Behind it is a small door (approx. 15 inches high). The golden key fits this lock perfectly.

**Location: The Small Passage / Garden View**
- **Characters:** Alice.
- **Events:** Alice opens the tiny door and looks through a passage (size of a rat-hole) into a beautiful garden with bright flowers and fountains. 
- **Conflict:** Alice realizes she is too large to fit through the door. She wishes she could "shut up like a telescope."

**Location: The Glass Table (Scale Shift 1)**
- **Characters:** Alice.
- **Events:** Alice returns to the glass table. A small bottle, previously unseen, is now on the table. It has a label: "DRINK ME."
- **Interaction:** Alice inspects the bottle for poison. Finding none, she drinks it. The liquid tastes of cherry-tart, custard, pineapple, roast turkey, toffee, and hot buttered toast.
- **Transformation:** Alice shrinks to ten inches high. 
- **Conflict/Failure:** Having shrunk, she realizes she left the golden key on top of the glass table. She tries to climb a table leg, but it is too slippery. She sits down and cries.

**Location: The Glass Table (Scale Shift 2)**
- **Characters:** Alice.
- **Events:** Alice discovers a small glass box under the table. Inside is a tiny cake marked "EAT ME" in currants.
- **Decision/Interaction:** Alice decides to eat the cake to either grow large enough to reach the key or small enough to fit under the door. She eats the cake. 
- **Visual State:** After eating, she initially remains the same size, then proceeds to finish the entire cake.
````

## Raw Response
````text
[[FILMCREATOR_PACKET]]
[[SECTION character_index_markdown]]
# Character Index - CH001

| ID | Name | Type | Status |
|:---|:---|:---|:---|
| alice | Alice | human | Physically Present |
| white_rabbit | White Rabbit | animal | Physically Present |
| sister | Sister | human | Referenced (Off-screen) |
| dinah | Dinah | animal | Referenced (Dreamt) |

[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: alice
canonical_character_id: alice
aliases: []
is_fully_identified: true
manual_description_required: true
manual_description_reason: While her actions and scale shifts are well-documented, the text provides no specific details regarding her hair color, eye color, or facial features.
clarification_required: false
clarification_reason: 
clarification_question: 
character_type_hint: human
morphology_hint: biped
scale_hint: unknown
renderability_hint: renderable
confidence: 0.9
direct_identity_evidence: "Alice, driven by curiosity, chases the Rabbit."
direct_visual_evidence: "Alice shrinks to ten inches high... Alice eats the cake."
costume_or_covering_evidence: 
movement_evidence: "Alice jumps up; it is dark overhead. She sees the White Rabbit hurrying down a long passage."
associated_entities: [white_rabbit, sister, dinah]
alias_or_role_evidence: 
unknowns: hair color, eye color, specific facial structure.
source_refs: []
[[SECTION markdown]]
# Alice
**Role:** Protagonist

**Status:** Physically Present (undergoing scale shifts)

**Physical Description:**
A young girl who experiences extreme size fluctuations. She shrinks to ten inches in height after drinking from a bottle and grows/remains large after eating a cake. 

**Costume & Silhouette:**
No specific clothing details are provided in this chapter, though she is capable of attempting a curtsey while falling.

**Descriptive Noun Phrases:**
- Small girl (10 inches tall)
- Falling child
- Curious explorer

**Uncertainty Notes:**
Visual appearance (hair/eyes/clothing) is not described in the text. Renderers will need to establish a consistent character design for her face and outfit.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: white_rabbit
canonical_character_id: white_rabbit
aliases: [White Rabbit]
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
direct_identity_evidence: "A White Rabbit with pink eyes runs past Alice."
direct_visual_evidence: "A White Rabbit with pink eyes... checks a watch from its waistcoat-pocket"
costume_or_covering_evidence: "checks a watch from its waistcoat-pocket"
movement_evidence: "runs past Alice", "hurrying down a long passage"
associated_entities: [alice]
alias_or_role_evidence: 
unknowns: 
source_refs: []
[[SECTION markdown]]
# White Rabbit
**Role:** Catalyst / Supporting Character

**Status:** Physically Present

**Physical Description:**
A white rabbit characterized by distinct pink eyes.

**Costume & Silhouette:**
Wears a waistcoat with a pocket used for carrying a watch.

**Descriptive Noun Phrases:**
- Pink-eyed white rabbit
- Rabbit in a waistcoat
- Hurrying rabbit

**Uncertainty Notes:**
None; visual markers (eyes, clothing) are explicitly stated.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: sister
canonical_character_id: sister
aliases: []
is_fully_identified: false
manual_description_required: true
manual_description_reason: Character is only mentioned as being present with a book; no physical description exists.
clarification_required: true
clarification_reason: The character is off-screen and lacks any visual descriptors.
clarification_question: Should the sister be designed as a specific age/appearance relative to Alice?
character_type_hint: human
morphology_hint: biped
scale_hint: human_scale
renderability_hint: context_only
confidence: 0.5
direct_identity_evidence: "Alice... expresses boredom with her sister's book"
direct_visual_evidence: 
costume_or_covering_evidence: 
movement_evidence: 
associated_entities: [alice]
alias_or_role_evidence: 
unknowns: appearance, age, clothing.
source_refs: []
[[SECTION markdown]]
# Sister
**Role:** Background / Referenced Character

**Status:** Referenced (Off-screen)

**Physical Description:**
No physical description provided.

**Costume & Silhouette:**
Unknown.

**Descriptive Noun Phrases:**
- Alice's sister
- Reader of the book

**Uncertainty Notes:**
This character is a passive presence in the opening scene and has no visual data for rendering.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: dinah
canonical_character_id: dinah
aliases: [Dinah]
is_fully_identified: false
manual_description_required: true
manual_description_reason: Character is only mentioned in a dream/thought; no physical description provided.
clarification_required: true
clarification_reason: The character's breed or appearance is not specified.
clarification_question: Is Dinah a specific breed of cat (e.g., tabby, calico)?
character_type_hint: animal
morphology_hint: quadruped
scale_hint: small
renderability_hint: context_only
confidence: 0.4
direct_identity_evidence: "dreaming of her cat Dinah"
direct_visual_evidence: 
costume_or_covering_evidence: 
movement_evidence: 
associated_entities: [alice]
alias_or_role_evidence: 
unknowns: color, breed, size.
source_refs: []
[[SECTION markdown]]
# Dinah
**Role:** Referenced Character (Dreamt)

**Status:** Referenced

**Physical Description:**
Identified only as Alice's cat.

**Costume & Silhouette:**
N/A

**Descriptive Noun Phrases:**
- Alice's cat
- Dreamt cat

**Uncertainty Notes:**
No visual details are provided for Dinah; she exists only in Alice's internal monologue/dream state.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]
[[/FILMCREATOR_PACKET]]
````
