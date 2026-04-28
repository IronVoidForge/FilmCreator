# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-28T00:16:49.099841+00:00
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

Chapter id: CH011

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

Fallback extraction chunk 2/2 for character_extraction.

Use only the chapter excerpt below for this pass.

“I wish you wouldn’t squeeze so,” said the Dormouse, who was sitting
next to her. “I can hardly breathe.”

“I can’t help it,” said Alice very meekly: “I’m growing.”

“You’ve no right to grow _here_,” said the Dormouse.

“Don’t talk nonsense,” said Alice more boldly: “you know you’re growing
too.”

“Yes, but _I_ grow at a reasonable pace,” said the Dormouse: “not in
that ridiculous fashion.” And he got up very sulkily and crossed over
to the other side of the court.

All this time the Queen had never left off staring at the Hatter, and,
just as the Dormouse crossed the court, she said to one of the officers
of the court, “Bring me the list of the singers in the last concert!”
on which the wretched Hatter trembled so, that he shook both his shoes
off.

“Give your evidence,” the King repeated angrily, “or I’ll have you
executed, whether you’re nervous or not.”

“I’m a poor man, your Majesty,” the Hatter began, in a trembling voice,
“—and I hadn’t begun my tea—not above a week or so—and what with the
bread-and-butter getting so thin—and the twinkling of the tea—”

“The twinkling of the _what?_” said the King.

“It _began_ with the tea,” the Hatter replied.

“Of course twinkling begins with a T!” said the King sharply. “Do you
take me for a dunce? Go on!”

“I’m a poor man,” the Hatter went on, “and most things twinkled after
that—only the March Hare said—”

“I didn’t!” the March Hare interrupted in a great hurry.

“You did!” said the Hatter.

“I deny it!” said the March Hare.

“He denies it,” said the King: “leave out that part.”

“Well, at any rate, the Dormouse said—” the Hatter went on, looking
anxiously round to see if he would deny it too: but the Dormouse denied
nothing, being fast asleep.

“After that,” continued the Hatter, “I cut some more bread-and-butter—”

“But what did the Dormouse say?” one of the jury asked.

“That I can’t remember,” said the Hatter.

“You _must_ remember,” remarked the King, “or I’ll have you executed.”

The miserable Hatter dropped his teacup and bread-and-butter, and went
down on one knee. “I’m a poor man, your Majesty,” he began.

“You’re a _very_ poor _speaker_,” said the King.

Here one of the guinea-pigs cheered, and was immediately suppressed by
the officers of the court. (As that is rather a hard word, I will just
explain to you how it was done. They had a large canvas bag, which tied
up at the mouth with strings: into this they slipped the guinea-pig,
head first, and then sat upon it.)

“I’m glad I’ve seen that done,” thought Alice. “I’ve so often read in
the newspapers, at the end of trials, “There was some attempts at
applause, which was immediately suppressed by the officers of the
court,” and I never understood what it meant till now.”

“If that’s all you know about it, you may stand down,” continued the
King.

“I can’t go no lower,” said the Hatter: “I’m on the floor, as it is.”

“Then you may _sit_ down,” the King replied.

Here the other guinea-pig cheered, and was suppressed.

“Come, that finished the guinea-pigs!” thought Alice. “Now we shall get
on better.”

“I’d rather finish my tea,” said the Hatter, with an anxious look at
the Queen, who was reading the list of singers.

“You may go,” said the King, and the Hatter hurriedly left the court,
without even waiting to put his shoes on.

“—and just take his head off outside,” the Queen added to one of the
officers: but the Hatter was out of sight before the officer could get
to the door.

“Call the next witness!” said the King.

The next witness was the Duchess’s cook. She carried the pepper-box in
her hand, and Alice guessed who it was, even before she got into the
court, by the way the people near the door began sneezing all at once.

“Give your evidence,” said the King.

“Shan’t,” said the cook.

The King looked anxiously at the White Rabbit, who said in a low voice,
“Your Majesty must cross-examine _this_ witness.”

“Well, if I must, I must,” the King said, with a melancholy air, and,
after folding his arms and frowning at the cook till his eyes were
nearly out of sight, he said in a deep voice, “What are tarts made of?”

“Pepper, mostly,” said the cook.

“Treacle,” said a sleepy voice behind her.

“Collar that Dormouse,” the Queen shrieked out. “Behead that Dormouse!
Turn that Dormouse out of court! Suppress him! Pinch him! Off with his
whiskers!”

For some minutes the whole court was in confusion, getting the Dormouse
turned out, and, by the time they had settled down again, the cook had
disappeared.

“Never mind!” said the King, with an air of great relief. “Call the
next witness.” And he added in an undertone to the Queen, “Really, my
dear, _you_ must cross-examine the next witness. It quite makes my
forehead ache!”

Alice watched the White Rabbit as he fumbled over the list, feeling
very curious to see what the next witness would be like, “—for they
haven’t got much evidence _yet_,” she said to herself. Imagine her
surprise, when the White Rabbit read out, at the top of his shrill
little voice, the name “Alice!”
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
- [Dormouse](#dormouse)
- [Queen](#queen)
- [Hatter](#hatter)
- [King](#king)
- [March Hare](#march-hare)
- [Jury Member](#jury-member)
- [Guinea-pig](#guinea-pig)
s-1
- [Officer](#officer)
- [White Rabbit](#white-rabbit)
- [Duchess's Cook](#duchesses-cook)
[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: alice
canonical_character_id: CH002 Alice
aliases: Alice
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
direct_identity_evidence: true
direct_visual_evidence: false
costume_or_covering_evidence: false
movement_evidence: false
associated_entities: Dormouse, White Rabbit
alias_or_role_evidence: true
unknowns: ""
source_refs: ""

[[SECTION markdown]]
# Alice
**Role:** Protagonist / Witness.
**Status:** Physically present in the court.
**Description:** A young girl who is growing rapidly in size during the trial, causing her to squeeze the Dormouse. She is observant of the court proceedings and the "suppression" of the guinea-pigs.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: dormouse
canonical_character_id: CH003 Dormouse
aliases: The Dormouse
is_fully_identified: true
manual_description_required: false
manual_description_reason: ""
clarification_required: false
clarification_reason: ""
clarification_question: ""
character_type_hint: animal
morphology_hint: unknown
scale_hint: small
renderability_hint: renderable
confidence: 0.8
direct_identity_evidence: true
direct_visual_evidence: false
costume_or_covering_evidence: false
movement_evidence: false
associated_entities: Alice, Queen
alias_or_role_evidence: true
unknowns: ""
source_refs: ""

[[SECTION markdown]]
# Dormouse
**Role:** Defendant/Witness (intermittent).
**Status:** Physically present.
**Description:** A small creature sitting next to Alice. He is prone to sleepiness and is frequently threatened with being beheaded or pinched by the Queen.
[[/SECTION]]
[[/FILismCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: queen
canonical_character_id: CH004 Queen
aliases: Her Majesty
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
confidence: 0.8
direct_identity_evidence: true
direct_visual_evidence: false
costume_or_covering_evidence: false
movement_evidence: false
associated_entities: King, Hatter, Officers
alias_or_role_evidence: true
unknowns: ""
source_refs: ""

[[SECTION markdown]]
# Queen
**Role:** Authority figure / Accuser.
**Status:** Physically present.
**Description:** An authoritative and volatile figure who stares intensely at the Hatter and orders the suppression of dissenters. She is prone to sudden outbursts of "Off with his whiskers!" or beheading orders.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: hatter
canonical_character_id: CH005 Hatter
aliases: The Hatter, the wretched Hatter
is_fully_identified: true
manual_description_required: false
manual_description_reason: ""
clarification_required: false
clarification_reason: ""
character_type_hint: humanoid_nonhuman
morphology_hint: biped
scale_hint: human_scale
renderability_hint: renderable
confidence: 0.9
direct_identity_evidence: true
direct_visual_evidence: false
costume_or_covering_evidence: false
movement_evidence: false
associated_entities: Queen, King, Dormouse, March Hare
alias_or_role_evidence: true
unknowns: ""
source_refs: ""

[[SECTION markdown]]
# Hatter
**Role:** Defendant / Witness.
**Status:** Physically present.
**Description:** A nervous man who trembles under the Queen's gaze. He is accused of being involved in a "twinkling" tea-related event and is prone to dropping his teacup or shoes when startled.
[[ted_description: ""
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: king
canonical_character_id: CH006 King
aliases: His Majesty, the King
is_fully_identified: true
manual_description_required: false
manual_description_reason: ""
clarification_required: false
clarification_reason: ""
character_type_hint: humanoid_nonhuman
morphology_hint: biped
scale_hint: human_scale
renderability_hint: renderable
confidence: 0.9
direct_identity_evidence: true
direct_visual_evidence: false
costume_or_covering_evidence: false
movement_evidence: false
associated_entities: Queen, Hatter, White Rabbit
alias_or_role_evidence: true
unknowns: ""
source_refs: ""

[[SECTION markdown]]
# King
**Role:** Judge / Authority figure.
**Status:** Physically present.
**Description:** An authoritative but somewhat dim-witted ruler who presides over the court. He is prone to anger and threatens execution, yet shows a melancholy air when dealing with witnesses.
[[/SECTION]]
[[/FILMCREcut_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: march_hare
canonical_character_id: CH007 March Hare
aliases: The March Hare
is_fully_identified: true
manual_description_required: false
manual_description_reason: ""
clarification_required: false
clarification_reason: ""
character_type_hint: animal
morphology_hint: quadruped
scale_hint: small
renderability_hint: renderable
confidence: 0.8
direct_identity_evidence: true
direct_visual_evidence: false
costume_or_covering_evidence: false
movement_evidence: false
associated_entities: Hatter
alias_or_role_evidence: true
unknowns: ""
source_refs: ""

[[SECTION markdown]]
# March Hare
**Role:** Witness / Accused.
**Status:** Physically present (referenced in dialogue).
**Description:** A frantic character who interrupts the Hatter to deny his involvement in certain events.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILM𝓭_RECORD]]
type: character
asset_id: jury_member
canonical_character_id: CH008 Jury Member
aliases: one of the jury
is_fully_identified: true
manual_description_required: false
manual_description_reason: ""
clarification_required: false
clarification_reason: ""
character_type_hint: unknown
morphology_hint: unknown
scale_hint: human_scale
renderability_hint: context_only
confidence: 0.5
direct_identity_evidence: true
direct_visual_evidence: false
costume_or_covering_evidence: false
movement_evidence: false
associated_entities: ""
alias_or_role_evidence: true
unknowns: ""
source_refs: ""

[[SECTION markdown]]
# Jury Member
**Role:** Court official.
**Status:** Physically present (implied).
**Description:** An anonymous member of the jury asking questions about the Dormouse.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: guinea_pig
canonical_character_id: CH009 Guinea-pig
aliases: The guinea-pigs
is_fully_identified: true
manual_description_required: false
manualdescription_reason: ""
clarification_required: false
clarification_reason: ""
character_type_hint: animal
morphology_hint: quadruped
scale_hint: small
renderability_hint: renderable
confidence: 0.9
direct_identity_evidence: true
direct_visual_evidence: false
costume_or_covering_evidence: false
movement_evidence: false
associated_entities: ""
alias_or_role_evidence: true
unknowns: ""
source_refs: ""

[[SECTION markdown]]
# Guinea-pig
**Role:** Spectator / Accidental victim.
**Status:** Physically present (referenced as being suppressed).
**Description:** Small animals in the court that cheer and are then "suppressed" by being sat upon inside a canvas bag.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: officer
canonical_character_id: CH010 Officer
aliases: one of the officers
is_fully_identified: true
manual_description_required: false
manual_description_reason: ""
clarification_required: false
clarification_reason: ""
character_type_hint: humanoid_nonhuman
morphology_hint: biped
scale_hint: human_scale
renderability_hint: renderable
confidence: 0.8
direct_identity_evidence: true
direct_visual_evidence: false
costume_or_covering_evidence: false
movement_evidence: false
associated_entities: Queen, King
alias_or_role_evidence: true
unknowns: ""
source_refs: ""

[[SECTION markdown]]
# Officer
**Role:** Court official.
**Status:** Physically present.
**Description:** An officer of the court responsible for carrying out orders like "suppressing" applause or taking heads.
[[/end_section]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: white_rabbit
canonical_character_id: CH011 White Rabbit
aliases: The White Rabbit
is_fully_identified: true
manual_description_required: false
manual_description_reason: ""
clarification_required: false
clarification_reason: ""
character_type_hint: animal
morphology_hint: quadruped
scale_hint: small
renderability_hint: renderable
confidence: 0.9
direct_identity_evidence: true
direct_visual_evidence: false
costume_or_covering_evidence: false
movement_evidence: false
associated_entities: King, Alice
alias_or_role_evidence: true
unknowns: ""
source_refs: ""

[[SECTION markdown]]
# White Rabbit
**Role:** Court official / Witness-caller.
**Status:** Physically present.
**Description:** A small rabbit with a shrill voice who manages the list of witnesses and advises the King on cross-examination.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: duchesses_cook
canonical_character_id: CH012 Duchess's Cook
aliases: The cook, the Duchess’s cook
is_fully_identified: true
manual_description_required: false
manual_description_reason: ""
clarification_required: false
clarification_reason: ""
character_type_hint: humanoid_nonhuman
morphology_hint: biped
scale_hint: human_scale
renderability_hint: renderable
confidence: 0.9
direct_identity_evidence: true
direct_visual_evidence: false
costume_or_covering_evidence: false
movement_evidence: false
associated_entities: Duchess
alias_or_role_evidence: true
unknowns: ""
source_refs: ""

[[SECTION markdown]]
# Duchess's Cook
**Role:** Witness.
**Status:** Physically present.
**Description:** A witness who carries a pepper-box and is the subject of much sneezing in the court. She is defiant toward the King.
[[/SECTION]]
[[/FILмCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
