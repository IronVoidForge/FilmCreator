# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-28T03:16:07.342069+00:00
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

Chapter id: CH002

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

**Location: The Hall / The Garden Door Subzone**
*   **Visual State:** Alice is giant-sized, standing over nine feet tall. Her feet appear extremely distant from her torso due to perspective/scale.
*   **Event:** Alice experiences a growth spurt/size shift where she feels like a "telescope opening out." She contemplates the logistics of sending Christmas boots to her own feet via carrier.
*   **Action:** Alice's head strikes the ceiling of the hall. She retrieves a small golden key.
*   **Action:** Alice attempts to look into the garden through the tiny door by lying on her side and using one eye, but she is too large to pass.
*   **Event/Transition:** Alice begins to cry uncontrollably. Her tears create a large pool of salt water, approximately four inches deep, spreading halfway down the hall.

**Location: The Hall (Flooded)**
*   **Character Entrance:** The White Rabbit enters, trotting hurriedly. He is dressed splendidly and carries white kid gloves in one hand and a large fan in the other. He mutters about "the Duchess."
*   **Interaction:** Alice attempts to speak to the Rabbit. The Rabbit reacts violently, drops the gloves and the fan, and scurries away into the darkness.
*   **Object Interaction:** Alice picks up the fan and the white kid gloves. 
*   **Character State/Internal Monologue:** Alice experiences an identity crisis, questioning if she has been changed into another child (Ada or Mabel). She attempts to verify her identity through math (4x5=12) and geography (London is the capital of Paris), failing both. She recites "How doth the little crocodile" but finds her voice sounds hoarse and strange.
*   **Visual/Scale Shift:** Alice notices she is wearing one of the Rabbit's white kid gloves. She measures herself against a table and realizes she has shrunk to approximately two feet tall. 
*   **Action/Risk:** Alice discovers that holding the fan causes her to shrink rapidly. She drops the fan to prevent shrinking into non-existence.
*   **Event:** Alice runs toward the garden door, but finds it shut. The golden key is back on the glass table.
*   **Physical Event:** Alice slips and falls into the pool of tears she previously created. She is now swimming in salt water up to her chin.

**Location: The Pool (In the Hall)**
*   **Character Encounter:** Alice hears splashing and discovers a Mouse swimming nearby.
*   **Interaction/Dialogue:** Alice attempts to communicate with the Mouse using formal "O Mouse" address and then switches to French ("Où est ma chatte?"). 
*   **Conflict:** The Mouse reacts with fright/anger to the mention of cats. Alice tries to soothe the Mouse by describing her cat, Dinah, which causes the Mouse to bristle and tremble with indignation.
*   **Conflict Escalation:** Alice attempts to change the subject to dogs (a terrier), but mentions the dog kills rats. The Mouse becomes highly offended and swims away in a commotion.
*   **Resolution of Interaction:** Alice calls the Mouse back, promising not to mention cats or dogs. The Mouse agrees to return and tells her they should reach the shore so he can explain his history.
*   **Character/Creature Entrance:** As they swim toward the shore, other animals emerge in the pool: a Duck, a Dodo, a Lory, and an Eaglet.
*   **Action/Exit:** Alice leads the group of animals/birds swimming toward the edge of the pool (the shore).
````

## Raw Response
````text
[[FILMCREATOR_PACKET]]
task: character_extraction
version: 1

[[FILMCREATOR_RECORD]]
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
morphology_hint: female child
scale_hint: variable (9ft tall, then 2ft tall)
renderability_hint: high
confidence: 1.0
direct_identity_evidence: "Alice experiences an identity crisis... questioning if she has been changed into another child"
direct_visual_evidence: "Alice is giant-sized, standing over nine feet tall... Alice notices she is wearing one of the Rabbit's white kid gloves... realizes she has shrunk to approximately two feet tall."
costume_or_covering_evidence: "wearing one of the Rabbit's white kid gloves"
movement_evidence: "strikes the ceiling... lies on her side... begins to cry... runs toward the garden door... slips and falls into the pool... swimming in salt water"
associated_entities: ["white_rabbit", "mouse", "dinah", "duck", "dodo", "lory", "eaglet"]
alias_or_role_evidence: ""
unknowns: []
source_refs: []
[[SECTION character_index_markdown]]
[[SECTION markdown]]
# Alice
**Role:** Protagonist

**Status:** Physically Present

**Physical Description:**
- Human female child.
- Scale is highly unstable: starts at over nine feet tall, shrinks to approximately two feet tall.
- During the shrinking phase, she is seen wearing a white kid glove that belongs to the White Rabbit.

**Costume & Silhouette:**
- Size shifts significantly (giant vs. small child).
- Wears one of the White Rabbit's white kid gloves during the mid-chapter transition.

**Descriptive Noun Phrases:**
- Giant-sized girl
- Two-foot tall child
- Swimming child in salt water pool

**Uncertainty Notes:**
- Exact facial features or hair color are not specified in this chapter text.
[[/SECTION]]
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
asset_id: white_rabbit
canonical_character_id: white_rabbit
aliases: []
is_fully_identified: true
manual_description_required: false
manual_description_reason: ""
clarification_required: false
clarification_reason: ""
clarification_question: ""
character_type_hint: anthropomorphic animal
morphology_hint: rabbit
scale_hint: small/standard rabbit scale
renderability_hint: high
confidence: 1.0
direct_identity_evidence: "The White Rabbit enters, trotting hurriedly."
direct_visual_evidence: "dressed splendidly and carries white kid gloves in one hand and a large fan in the other."
costume_or_covering_evidence: "dressed splendidly; carries white kid gloves and a large fan"
movement_evidence: "trotting hurriedly... reacts violently... scurries away into the darkness"
associated_entities: ["alice", "the_duchess"]
alias_or_role_evidence: ""
unknowns: []
source_refs: []
[[SECTION character_index_markdown]]
[[SECTION markdown]]
# White Rabbit
**Role:** Supporting Character

**Status:** Physically Present

**Physical Description:**
- Anthropomorphic rabbit.
- Dressed splendidly.

**Costume & Silhouette:**
- Splendid attire (details unspecified).
- Carries white kid gloves and a large fan.

**Descriptive Noun Phrases:**
- Splendidly dressed rabbit
- Hurried rabbit with gloves and fan

**Uncertainty Notes:**
- Specific colors of clothing or "splendid" details are not provided.
[[/SECTION]]
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
asset_id: mouse
canonical_character_id: mouse
aliases: []
is_fully_identified: true
manual_description_required: false
manual_description_reason: ""
clarification_required: false
clarification_reason: ""
clarification_question: ""
character_type_hint: animal
morphology_hint: mouse
scale_hint: small
renderability_hint: high
confidence: 1.0
direct_identity_evidence: "discovers a Mouse swimming nearby."
direct_visual_evidence: "Mouse swimming nearby... swims away in a commotion"
costume_or_covering_evidence: ""
movement_evidence: "swimming... bristle and tremble with indignation... swims away"
associated_entities: ["alice"]
alias_or_role_evidence: ""
unknowns: []
source_refs: []
[[SECTION character_index_markdown]]
[[SECTION markdown]]
# Mouse
**Role:** Supporting Character

**Status:** Physically Present

**Physical Description:**
- Small animal.

**Costume & Silhouette:**
- N/A

**Descriptive Noun Phrases:**
- Swimming mouse
- Indignant mouse

**Uncertainty Notes:**
- Specific breed or color not mentioned.
[[/SECTION]]
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
asset_id: dinah
canonical_character_id: dinah
aliases: []
is_fully_identified: false
manual_description_required: true
manual_description_reason: "Character is only mentioned in dialogue/thought and has no visual description."
clarification_required: false
clarification_reason: ""
clarification_question: ""
character_type_hint: animal
morphology_hint: cat
scale_hint: standard cat
renderability_hint: low
confidence: 0.8
direct_identity_evidence: "describing her cat, Dinah"
direct_visual_evidence: ""
costume_or_covering_evidence: ""
movement_evidence: ""
associated_entities: ["alice"]
alias_or_role_evidence: ""
unknowns: ["physical appearance", "color", "breed"]
source_refs: []
[[SECTION character_index_markdown]]
[[SECTION markdown]]
# Dinah
**Role:** Referenced Character

**Status:** Referenced (Not Present)

**Physical Description:**
- A cat.

**Costume & Silhouette:**
- N/A

**Descriptive Noun Phrases:**
- Alice's cat

**Uncertainty Notes:**
- No visual details provided in text; appearance is unknown.
[[/SECTION]]
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
asset_id: duck
canonical_character_id: duck
aliases: []
is_fully_identified: true
manual_description_required: false
manual_description_reason: ""
clarification_required: false
clarification_reason: ""
clarification_question: ""
character_type_hint: animal
morphology_hint: duck
scale_hint: small/standard bird
renderability_hint: medium
confidence: 0.9
direct_identity_evidence: "other animals emerge in the pool: a Duck..."
direct_visual_evidence: "emerge in the pool"
costume_or_covering_evidence: ""
movement_evidence: "swimming toward the edge of the pool"
associated_entities: ["alice", "dodo", "lory", "eaglet"]
alias_or_role_evidence: ""
unknowns: []
source_refs: []
[[SECTION character_index_markdown]]
[[SECTION markdown]]
# Duck
**Role:** Background Character

**Status:** Physically Present (Appears in pool)

**Physical Description:**
- A duck.

**Costume & Silhouette:**
- N/A

**Descriptive Noun Phrases:**
- Swimming duck

**Uncertainty Notes:**
- No specific color or breed mentioned.
[[/SECTION]]
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
asset_id: dodo
canonical_character_id: dodo
aliases: []
is_fully_identified: true
manual_description_required: false
manual_description_reason: ""
clarification_required: false
clarification_reason: ""
clarification_question: ""
character_type_hint: animal
morphology_hint: dodo
scale_hint: small/standard bird
renderability_hint: medium
confidence: 0.9
direct_identity_evidence: "other animals emerge in the pool: ... a Dodo..."
direct_visual_evidence: "emerge in the pool"
costume_or_covering_evidence: ""
movement_evidence: "swimming toward the edge of the pool"
associated_entities: ["alice", "duck", "lory", "eaglet"]
alias_or_role_evidence: ""
unknowns: []
source_refs: []
[[SECTION character_index_markdown]]
[[SECTION markdown]]
# Dodo
**Role:** Background Character

**Status:** Physically Present (Appears in pool)

**Physical Description:**
- A dodo bird.

**Costume & Silhouette:**
- N/A

**Descriptive Noun Phrases:**
- Swimming dodo

**Uncertainty Notes:**
- No specific visual details provided.
[[/SECTION]]
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
asset_id: lory
canonical_character_id: lory
aliases: []
is_fully_identified: true
manual_description_required: false
manual_description_reason: ""
clarification_required: false
clarification_reason: ""
clarification_question: ""
character_type_hint: animal
morphology_hint: lory (parrot)
scale_hint: small bird
renderability_hint: medium
confidence: 0.9
direct_identity_evidence: "other animals emerge in the pool: ... a Lory..."
direct_visual_evidence: "emerge in the pool"
costume_or_covering_evidence: ""
movement_evidence: "swimming toward the edge of the pool"
associated_entities: ["alice", "duck", "dodo", "eaglet"]
alias_or_role_evidence: ""
unknowns: []
source_refs: []
[[SECTION character_index_markdown]]
[[SECTION markdown]]
# Lory
**Role:** Background Character

**Status:** Physically Present (Appears in pool)

**Physical Description:**
- A lory (type of parrot).

**Costume & Silhouette:**
- N/A

**Descriptive Noun Phrases:**
- Swimming lory

**Uncertainty Notes:**
- No specific color or plumage details provided.
[[/SECTION]]
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
asset_id: eaglet
canonical_character_id: eaglet
aliases: []
is_fully_identified: true
manual_description_required: false
manual_description_reason: ""
clarification_required: false
clarification_reason: ""
clarification_question: ""
character_type_hint: animal
morphology_hint: eaglet (young eagle)
scale_hint: small bird
renderability_hint: medium
confidence: 0.9
direct_identity_evidence: "other animals emerge in the pool: ... and an Eaglet."
direct_visual_evidence: "emerge in the pool"
costume_or_covering_evidence: ""
movement_evidence: "swimming toward the edge of the pool"
associated_entities: ["alice", "duck", "dodo", "lory"]
alias_or_role_evidence: ""
unknowns: []
source_refs: []
[[SECTION character_index_markdown]]
[[SECTION markdown]]
# Eaglet
**Role:** Background Character

**Status:** Physically Present (Appears in pool)

**Physical Description:**
- An eaglet (young eagle).

**Costume & Silhouette:**
- N/A

**Descriptive Noun Phrases:**
- Swimming eaglet

**Uncertainty Notes:**
- No specific visual details provided.
[[/SECTION]]
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
asset_id: the_duchess
canonical_character_id: the_duchess
aliases: []
is_fully_identified: false
manual_description_required: true
manual_description_reason: "Character is only mentioned in dialogue and has no visual description."
clarification_required: false
clarification_reason: ""
clarification_question: ""
character_type_hint: unknown
morphology_hint: unknown
scale_hint: unknown
renderability_hint: low
confidence: 0.5
direct_identity_evidence: "He mutters about 'the Duchess.'"
direct_visual_evidence: ""
costume_or_covering_evidence: ""
movement_evidence: ""
associated_entities: ["white_rabbit"]
alias_or_role_evidence: ""
unknowns: ["physical appearance", "species", "gender", "scale"]
source_refs: []
[[SECTION character_index_markdown]]
[[SECTION markdown]]
# The Duchess
**Role:** Referenced Character

**Status:** Referenced (Not Present)

**Physical Description:**
- Unknown.

**Costume & Silhouette:**
- Unknown.

**Descriptive Noun Phrases:**
- The Duchess

**Uncertainty Notes:**
- No information available regarding her appearance or nature.
[[/SECTION]]
[[/SECTION]]
[[/FILMCREATOR_RECORD]]
[[/FILMCREATOR_PACKET]]
````
