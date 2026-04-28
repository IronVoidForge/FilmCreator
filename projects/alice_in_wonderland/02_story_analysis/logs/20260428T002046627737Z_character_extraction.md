# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-28T00:20:46.627737+00:00
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

Chapter id: CH012

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

**Setting:** A courtroom where a jury sits in a box; later, a riverbank under trees as the sun sets.

**Characters:**
- **Alice:** Currently at her full size (nearly two miles high), then shrinking back to normal size.
- **The King:** An authoritative but somewhat bumbling figure who reads from a notebook and issues rules.
- **The Queen:** A temperamental ruler prone to sudden outbursts of anger.
- **The White Rabbit:** The court official/messenger, respectful yet hurried.
- **The Knave:** The prisoner, made of cardboard.
- **The Jury/Lizard (Bill):** A group of creatures; the Lizard is a specific jury member who gets knocked over and then has ink spilled on him by the Queen.
- **Alice's Sister:** Appears at the end in the real world.

**Key Events:**
1. **The Accident:** Alice, growing large, accidentally tips over the jury-box while jumping up. The jurymen fall out like goldfish; one is a Lizard (Bill) who is placed head-downward and then later has an inkstand thrown at him by the Queen.
2. **Rule 42:** The King reads "Rule Forty-two," stating those over a mile high must leave. Alice argues she is nearly two miles high, leading to a debate on the validity of the rule.
3. **The Evidence:** The White Rabbit presents a piece of paper—a set of verses found in the prisoner's possession. 
4. **Reading the Verses:** The White Rabbit reads a cryptic poem regarding "she," "him," and "the tarts." The King attempts to interpret the verses as evidence of the Knave's guilt regarding the stolen tarts.
5. **The Conflict:** Alice challenges the meaninglessness of the verses. The Queen, furious at the interruption, orders "Off with her head!" 
6. **The Escape/Awakening:** Alice tells the cards they are nothing but a pack of cards; the cards fly at her, causing her to wake up on the riverbank in the real world.
7. **The Epilogue:** Alice tells her sister about the dream. The sister watches the sunset, reflecting on how the sounds of the natural world (rustling grass, sheep-bells) mirror the sounds of Wonderland.

**Visual/Continuity Elements:**
- **Scale Shift:** Alice starts huge, causing the jury to fall; she ends as a normal girl in the real world.
- **The Jury Box:** A structure that is tipped over and then restored.
- **The Verses:** A physical piece of paper read by the White Rabbit.
- **The Knave's Physicality:** He is made of cardboard, making his "lack of ability to swim" a literal visual gag.
- **The Transition:** The transition from the "pack of cards" flying at Alice to her waking up on the grass serves as the bridge between the dream and reality.
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
- [The King](#the-king)
- [The Queen](#the-queen)
- [The White Rabbit](#the-white-rabbit)
- [The Knave](#the-knave)
- [Bill the Lizard](#bill-the-lizard)
- [Alice's Sister](#alices-sister)

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
character_type_hint: human
morphology_hint: massive scale (two miles high) transitioning to normal human size.
scale_hint: giant/human
renderability_hint: needs transition from colossal to child-sized.
confidence: 0.9
direct_identity_evidence: true
direct_visual_evidence: true
costume_or_covering_evidence: false
movement_evidence: jumping, arguing, waking up.
associated_entities: Alice's Sister, The Queen, The White Rabbit, The Knave, The Jury
alias_or_role_evidence: protagonist
unknowns: specific clothing details not provided in text.
source_refs: CH012

[[SECTION markdown]]
# Alice
**Role:** Protagonist

**Status:** Physically present (massive scale) then transitioning to human size.

**Physical Description:** 
Initially depicted at a colossal scale, nearly two miles high. Later shrinks back to the size of a young girl in the real world.

**Notes:** 
The transition from her giant form to her normal size is a key narrative beat between the dream and reality.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: the_king
canonical_character_id: CH012 King
aliases: 
is_fully_identified: true
manual_description_required: false
manual_description_reason: ""
clarification_required: false
clarification_reason: ""
clarification_question: ""
character_type_hint: human/playing-card-entity
morphology_hint: authoritative figure.
scale_hint: small (relative to Alice)
renderability_hint: bumbling authority.
confidence: 0.8
direct_identity_evidence: true
direct_visual_evidence: true
costume_or_covering_evidence: false
movement_evidence: reading from a notebook.
associated_entities: The Queen, The White Rabbit, Alice
alias_or_role_evidence: ruler
unknowns: specific costume details.
source_refs: CH012

[[SECTION markdown]]
# The King
**Role:** Ruler / Judge

**Status:** Physically present.

**Physical Description:** 
An authoritative but somewhat bumbling figure who reads from a notebook to issue rules and interpret evidence.

**Notes:** 
His role is centered on the legalistic absurdity of Rule 42 and interpreting verses.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: the_queen
canonical_character_id: CH012 Queen
aliases: 
is_fully_identified: true
manual_description_required: false
manual_description_reason: ""
clarification_required: false
clarification_reason: ""
clarification_question: ""
character_type_hint: human/playing-card-entity
morphology_hint: temperamental ruler.
scale_hint: small (relative to Alice)
renderability_hint: high emotional volatility.
confidence: 0.8
direct_identity_evidence: true
direct_visual_evidence: true
costume_or_covering_evidence: false
movement_evidence: throwing an inkstand.
associated_entities: The King, Alice, Bill the Lizard
alias_or_role_evidence: ruler
unknowns: specific costume details.
source_refs: CH012

[[SECTION markdown]]
# The Queen
**Role:** Ruler / Antagonist

**Status:** Physically present.

**Physical Description:** 
A temperamental and furious ruler known for sudden outbursts of anger.

**Notes:** 
She is the source of the "Off with her head!" command and physically interacts with the jury by throwing an inkstand at Bill the Lizard.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: the_white_rabbit
canonical_character_id: CH012 White Rabbit
aliases: 
is_fully_identified: true
manual_description_required: false
manual_description_reason: ""
clarification_required: false
clarification_reason: ""
clarification_question: ""
character_type_hint: animal/playing-card-entity
morphology_hint: official messenger.
scale_hint: small (relative to Alice)
renderability_hint: hurried and respectful.
confidence: 0.8
direct_identity_evidence: true
direct_visual_evidence: true
costume_or_covering_evedence: false
movement_evidence: presenting papers/reading verses.
associated_entities: The King, Alice, The Knave
alias_or_role_evidence: court official
unknowns: specific clothing details.
source_refs: CH012

[[SECTION markdown]]
# The White Rabbit
**Role:** Court Official / Messenger

**Status:** Physically present.

**Physical Description:** 
A hurried and respectful figure who presents evidence (the verses) to the court.

**Notes:** 
Acts as the presenter of the cryptic poem that drives the trial's tension.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: the_knave
canonical_character_id: CH012 Knave
aliases: 
is_fully_identified: true
manual_description_required: false
manual_description_reason: ""
clarification_required: false
clarification_reason: ""
clarification_question: ""
character_type_hint: cardboard-entity
morphology_hint: flat/cardboard construction.
scale_hint: small (relative to Alice)
renderability_hint: literal cardboard texture.
confidence: 0.9
direct_identity_evidence: true
direct_visual_evidence: true
costume_or_covering_evidence: true
movement_evidence: being the subject of trial/theft accusation.
associated_entities: The King, The White Rabbit, Alice
alias_or_role_evidence: prisoner
unknowns: specific facial features.
source_refs: CH0ty2

[[SECTION markdown]]
# The Knave
**Role:** Prisoner / Defendant

**Status:** Referenced/Present as a concept of the trial.

**Physical Description:** 
A figure made entirely of cardboard, making him physically incapable of swimming.

**Notes:** 
The central figure of the trial's accusation regarding stolen tarts.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: bill_the_lizard
canonical_character_id: CH012 Bill the Lizard
aliases: Bill
is_fully_identified: true
manual_description_required: false
manual_description_reason: ""
clarification_required: false
clarification_reason: ""
clarification_question: ""
character_type_hint: animal/jury-member
morphology_hint: a lizard.
scale_hint: small
renderability_hint: prone to being knocked over or splashed with ink.
confidence: 0.9
direct_identity_evidence: true
direct_visual_evidence: true
costume_or_covering_evidence: false
movement_evidence: falling out of the jury box, being hit by an inkstand.
associated_entities: The Queen, Alice
alias_or_role_evidence: jury member
unknowns: ""
source_refs: CH012

[[SECTION markdown]]
# Bill the Lizard
**Role:** Jury Member

**Status:** Physically present.

**Physical Description:** 
A lizard serving as a juror; he is knocked over when the jury box tips and later has ink spilled on him.

**Notes:** 
He represents the physical chaos of the courtroom scene.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: alices_sister
canonical_character_id: CH012 Alice's Sister
aliases: 
is_fully_identified: true
manual_description_required: false
manual_description_reason: ""
clarification_required: false
clarification_reason: ""
clarification_question: ""
character_type_hint: human
morphology_hint: human.
scale_hint: normal
renderability_hint: grounded/real-world aesthetic.
confidence: 0.7
direct_identity_evidence: true
direct_visual_evidence: true
costume_or_covering_evidence: false
movement_evidence: watching the sunset.
associated_entities: Alice
alias_or_role_evidence: sister
unknowns: specific clothing details.
source_refs: CH012

[[SECTION markdown]]
# Alice's Sister
**Role:** Real-world observer

**Status:** Physically present (at the end).

**Physical Description:** 
A human figure in the real world, watching the sunset.

**Notes:** 
She serves as the bridge to reality, reflecting on the sounds of the natural world.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
