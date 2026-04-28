# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-28T04:14:02.092696+00:00
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

Chapter id: CH009

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

**Location: Croquet-ground / Path to the Mock Turtle**

**Characters:**
* **Alice:** Curious, polite but increasingly frustrated by nonsensical logic.
* **The Duchess:** Ugly, sharp-chinned, prone to delivering unsolicited and convoluted "morals."
* **The Queen of Hearts:** Volatile, aggressive, prone to ordering executions for minor delays.
* **The King of Hearts:** Calm, provides pardons in a low voice.
* **The Gryphon:** A creature that finds amusement in the Queen's chaos; somewhat cynical.
* **The Mock Turtle:** Melancholic, tearful, speaks in a deep/hollow tone; prone to heavy sobbing.

**Events & Scene Beats:**
1.  **Walking Sequence (Duchess & Alice):** The Duchess and Alice walk together. The Duchess is physically intrusive, resting her sharp chin on Alice's shoulder. They engage in a rapid-fire dialogue of nonsensical "morals" regarding pepper, vinegar, mustard, and the nature of being oneself.
2.  **The Queen’s Entrance:** The Duchess's voice cuts off mid-sentence as the Queen appears, frowning. The Queen issues an ultimatum to the Duchess: lose her head or be executed in half a time. 
3.  **Duchess Exit:** The Duchess chooses execution/flight and vanishes instantly.
4.  **Croquet Game Chaos:** Alice follows the Queen back to the croquet ground. The game is characterized by the Queen shouting "Off with his/her head!" at players. Soldiers (who were previously playing as arches) arrest players, leaving only the King, Queen, and Alice in the game.
5.  **The King's Pardon:** As Alice feels distressed by the executions, the King quietly whispers to the group that everyone is pardoned.
6.  **Meeting the Gryphon:** The Queen directs Alice to a sleeping Gryphon to find the Mock Turtle. The Queen exits to oversee more executions. 
7.  **Gryphon/Alice Interaction:** The Gryphon wakes up, watches the Queen leave, and chuckles at her behavior. He reveals that she never actually executes anyone.
8.  **Arrival at the Ledge:** Alice and the Gryphon find the Mock Turtle sitting alone on a rock ledge, visibly sobbing.
9.  **The Mock Turtle’s History (Dialogue Sequence):** 
    *   The Mock Turtle commands silence to begin his tale.
    *   He recounts his life as a "real" turtle attending school in the sea.
    *   **Educational Details:** The curriculum included "Reeling and Writhing," Arithmetic (Ambition, Distraction, Uglification, Derision), Seaography, Mystery, and Drawling (taught by a conger-eel). 
    *   **Conflict:** Alice's attempts to clarify or compare her own schooling lead to reprimands from both the Mock Turtle and the Gryphon.
    *   **The "Lessons" Pun:** The Gryphon explains that they are called "lessons" because they "lessen" (decrease) in hours every day.
10. **Transition:** The Gryphon interrupts Alice's line of questioning to move the conversation toward "the games."
````

## Raw Response
````text
[[FILMCREATOR_PACKET]]
[[SECTION character_index_markdown]]
[[markdown]]
# Character Index - Chapter 9

- [Alice](#alice)
- [The Duchess](#the-duchess)
- [The Queen of Hearts](#the-queen-of-hearts)
- [The King of Hearts](#the-king-of-hearts)
- [The Gryphon](#the-gryphon)
- [The Mock Turtle](#the-mock-turtle)

[[/SECTION]]
[[/FILMCREATOR_PACKET]]

[[FILMCREATOR_RECORD]]
type: character
[[SECTION markdown]]
# Alice
**Role:** Protagonist; curious, polite, increasingly frustrated by nonsensical logic.
**Presence:** Physically present.

### Description
A young girl navigating the illogical landscape of Wonderland. While specific physical traits (hair color, eye color) are not detailed in this chapter's summary, she is a human child.

### Render Notes
- **Keywords:** Human girl, curious expression, frustrated demeanor.
- **Uncertainty:** Specific clothing and hair details are not provided in this text segment.
[[/SECTION]]
asset_id: alice
canonical_character_id: alice
aliases: []
is_fully_identified: true
manual_description_required: true
manual_description_reason: The text provides personality and role but lacks specific physical descriptors (hair, eyes, clothing) necessary for consistent visual generation.
clarification_required: false
clarification_reason: 
clarification_question: 
character_type_hint: human
morphology_hint: biped
scale_hint: small
renderability_hint: renderable
confidence: 0.9
direct_identity_evidence: "Alice: Curious, polite but increasingly frustrated..."
direct_visual_evidence: 
costume_or_covering_evidence: 
movement_evidence: 
associated_entities: [the_duchess, the_queen_of_hearts, the_king_of_hearts, the_gryphon, the_mock_turtle]
alias_or_role_evidence: 
unknowns: 
source_refs: []
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
[[SECTION markdown]]
# The Duchess
**Role:** Antagonist/Supporting; delivers unsolicited "morals."
**Presence:** Physically present.

### Description
Described as "ugly" with a "sharp chin." She is physically intrusive, resting her chin on Alice's shoulder.

### Render Notes
- **Keywords:** Ugly woman, sharp chin, intrusive posture.
- **Uncertainty:** Specific clothing or body type beyond "ugly/sharp-chinned" is not specified.
[[/SECTION]]
asset_id: the_duchess
canonical_character_id: the_duchess
aliases: []
is_fully_identified: true
manual_description_required: true
manual_description_reason: Only "ugly" and "sharp-chinned" are provided; specific facial features, hair, or clothing are missing.
clarification_required: false
clarification_reason: 
clarification_question: 
character_type_hint: humanoid_nonhuman
morphology_hint: biped
scale_hint: human_scale
renderability_hint: renderable
confidence: 0.8
direct_identity_evidence: "The Duchess: Ugly, sharp-chinned..."
direct_visual_evidence: "resting her sharp chin on Alice's shoulder"
costume_or_covering_evidence: 
movement_evidence: "physically intrusive"
associated_entities: [alice, the_queen_of_hearts]
alias_or_role_evidence: 
unknowns: 
source_refs: []
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
[[SECTION markdown]]
# The Queen of Hearts
**Role:** Antagonist; volatile and aggressive ruler.
**Presence:** Physically present.

### Description
A volatile, aggressive figure prone to shouting "Off with his/her head!" She oversees executions and directs Alice.

### Render Notes
- **Keywords:** Aggressive queen, volatile expression, commanding presence.
- **Uncertainty:** No specific visual details regarding her crown, dress, or physical features are provided in this chapter summary.
[[/SECTION]]
asset_id: the_queen_of_hearts
canonical_character_id: the_queen_of_hearts
aliases: []
is_fully_identified: false
manual_description_required: true
manual_description_reason: Lacks any specific visual descriptors (clothing, facial features, crown) beyond her temperament and title.
clarification_required: false
clarification_reason: 
clarification_question: 
character_type_hint: humanoid_nonhuman
morphology_hint: biped
scale_hint: human_scale
renderability_hint: renderable
confidence: 0.7
direct_identity_evidence: "The Queen of Hearts: Volatile, aggressive..."
direct_visual_evidence: 
costume_or_covering_evidence: 
movement_evidence: "frowning", "shouting"
associated_entities: [alice, the_king_of_hearts, the_duchess]
alias_or_role_evidence: 
unknowns: 
source_refs: []
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
[[SECTION markdown]]
# The King of Hearts
**Role:** Supporting; calm counterpart to the Queen.
**Presence:** Physically present.

### Description
A calm figure who provides pardons in a low voice.

### Render Notes
- **Keywords:** Calm king, quiet demeanor.
- **Uncertainty:** No visual details provided regarding his appearance or royal attire.
[[/SECTION]]
asset_id: the_king_of_hearts
canonical_character_id: the_king_of_hearts
aliases: []
is_fully_identified: false
manual_description_required: true
manual_description_reason: No physical description provided; only temperament and vocal style.
clarification_required: false
clarification_reason: 
clarification_question: 
character_type_hint: humanoid_nonhuman
morphology_hint: biped
scale_hint: human_scale
renderability_hint: renderable
confidence: 0.7
direct_identity_evidence: "The King of Hearts: Calm, provides pardons..."
direct_visual_evidence: 
costume_or_covering_evidence: 
movement_evidence: "whispers"
associated_entities: [the_queen_of_hearts, alice]
alias_or_role_evidence: 
unknowns: 
source_refs: []
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
[[SECTION markdown]]
# The Gryphon
**Role:** Supporting; cynical observer and guide.
**Presence:** Physically present.

### Description
A creature that finds amusement in the Queen's chaos. He is capable of sleeping and later wakes to converse with Alice.

### Render Notes
- **Keywords:** Gryphon, mythical creature, cynical expression.
- **Uncertainty:** While a "Gryphon" implies a specific mythological form (lion/eagle hybrid), the text does not explicitly describe his specific appearance or scale in this chapter.
[[/SECTION]]
asset_id: the_gryphon
canonical_character_id: the_gryphon
aliases: []
is_fully_identified: false
manual_description_required: true
manual_description_reason: The text relies on the mythological archetype of a Gryphon without providing specific visual details or scale.
clarification_required: false
clarification_reason: 
clarification_question: 
character_type_hint: creature
morphology_hint: unknown
scale_hint: unknown
renderability_hint: renderable
confidence: 0.6
direct_identity_evidence: "The Gryphon: A creature that finds amusement..."
direct_visual_evidence: 
costume_or_covering_evidence: 
movement_evidence: "sleeping", "wakes up", "chuckles"
associated_entities: [alice, the_mock_turtle]
alias_or_role_evidence: 
unknowns: 
source_refs: []
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
[[SECTION markdown]]
# The Mock Turtle
**Role:** Supporting; melancholic storyteller.
**Presence:** Physically present.

### Description
A melancholic, tearful creature with a deep/hollow tone. He is found sitting alone on a rock ledge, visibly sobbing. He recounts his history as a "real" turtle.

### Render Notes
- **Keywords:** Mock Turtle, sobbing, melancholic, deep hollow voice.
- **Uncertainty:** The exact physical appearance of the "Mock" version (how it differs from a real turtle) is not visually described.
[[/SECTION]]
asset_id: the_mock_turtle
canonical_character_id: the_mock_turtle
aliases: []
is_fully_identified: false
manual_description_required: true
manual_description_reason: The text describes his temperament and voice but lacks specific physical morphology beyond being a "Mock Turtle."
clarification_required: false
clarification_reason: 
clarification_question: 
character_type_hint: creature
morphology_hint: unknown
scale_hint: small
renderability_hint: renderable
confidence: 0.6
direct_identity_evidence: "The Mock Turtle: Melancholic, tearful..."
direct_visual_evidence: "sitting alone on a rock ledge, visibly sobbing"
costume_or_covering_evidence: 
movement_evidence: "sobbing", "commands silence"
associated_entities: [the_gryphon, alice]
alias_or_role_evidence: 
unknowns: 
source_refs: []
[[/FILMCREATOR_RECORD]]
[[/FILMCREATOR_RECORD]]
````
