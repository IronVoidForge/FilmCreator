# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-28T00:17:52.857978+00:00
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
- [alice](#alice)
- [dormouse](#dormouse)
- [queen](#queen)
- [hatter](#hatter)
- [king](#king)
- [march_hare](#march_hare)
- [guinea_pig](#guinea_pig)
- [white_rabbit](#white_rabbit)
- [duchess_cook](#duchess_cook)

[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: alice
canonical_character_id: CH011 Alice
aliases: 
is_fully_identified: true
manual_description_required: false
manual_description_reason: ""
clarification_required: false
clarification_reason: ""
clarification_question: ""
character_type_hint: human
morphology_hint: growing in size during the scene.
scale_hint: child-sized but expanding.
renderability_hint: needs to look like she is physically crowding others.
confidence: 0.9
direct_identity_evidence: "said Alice very meekly"
direct_visual_evidence: "I'm growing."
costume_or_covering_evidence: ""
movement_evidence: "growing"
associated_entities: dormouse, white_rabbit
alias_or_role_evidence: protagonist
unknowns: ""
source_refs: ""

[[SECTION markdown]]
# Alice
**Role:** Protagonist / Witness.
**Status:** Physically present.
**Description:** A girl who is growing in size during the trial, causing her to squeeze others. She is observant of the court proceedings and the behavior of the officers.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: dormouse
canonical_character_id: CH011 Dormouse
aliases: 
is_fully_identified: true
manual_description_required: false
manual_description_reason: ""
clarification_required: false
clarification_reason: ""
clarification_question: ""
character_type_hint: small animal/creature
morphology_hint: small enough to sit next to Alice; has whiskers.
scale_hint: very small.
renderability_hint: sleepy, often being suppressed or turned out of court.
confidence: 0.9
direct_identity_evidence: "said the Dormouse"
direct_visual_evidence: "sitting next to her", "being fast asleep", "off with his whiskers!"
costume_or_covering_evidence: ""
movement_evidence: "fast asleep", "turned out of court"
associated_entities: alice, queen, hatter
alias_or_role_evidence: ""
unknowns: ""
source_refs: ""

[[SECTION markdown]]
# Dormouse
**Role:** Defendant/Witness (implied) / Court participant.
**Status:** Physically present.
**Description:** A small, sleepy creature who sits next to Alice. He is prone to falling asleep during the trial and is subject to the Queen's sudden outbursts of rage.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: queen
canonical_character_id: CH011 Queen
aliases: 
is_fully_identified: true
manual_description_required: false
manual_description_reason: ""
clarification_required: false
clarification_reason: ""
clarification_question: ""
character_type_hint: human/royal
morphology_hint: ""
scale_hint: ""
renderability_hint: authoritative, prone to sudden shrieking.
confidence: 0.8
direct_identity_evidence: "the Queen had never left off staring"
direct_visual_evidence: "reading the list of singers", "shrieked out"
costume_or_covering_evidence: ""
movement_evidence: ""
associated_entities: king, hatter, officers
alias_or_role_evidence: "the Queen added to one of the officers"
unknowns: ""
source_refs: ""

[[SECTION markdown]]
# Queen
**Role:** Authority figure.
**Status:** Physically present.
**Description:** An authoritative and volatile figure who stares intensely at the Hatter and commands the court with sudden, sharp outbursts. She is focused on the list of singers.
[[/SECTION]]
[[/FILMCRECTOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: hatter
canonical_character_id: CH011 Hatter
aliases: 
is_fully_identified: true
manual_description_required: false
manual_description_reason: ""
clarification_required: false
clarification_reason: ""
clarification_question: ""
character_type_hint: human
morphology_hint: "the miserable Hatter"
scale_hint: ""
renderability_hint: trembling, anxious, wearing shoes that can be shaken off.
confidence: 0.9
direct_identity_evidence: "said the Hatter"
direct_visual_evidence: "shook both his shoes off", "dropped his teacup and bread-and-butter", "went down on one knee"
costume_or_covering_evidence: "shoes"
movement_evidence: "trembling voice", "looking anxiously round"
associated_entities: queen, king, dormouse, march_hare
alias_or_role_evidence: "the wretched Hatter"
unknowns: ""
source_refs: ""

[[SECTION markdown]]
# Hatter
**Role:** Defendant.
**Status:** Physically present.
**Description:** A nervous, trembling man who is on trial. He is a poor speaker and is highly anxious about the Queen's gaze. He carries a teacup and bread-and-butter.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: king
canonical_character_id: CH011 King
aliases: 
is_fully_identified: true
manual_description_required: false
manual_description_reason: ""
clarification_required: false
clarification_reason: ""
clarification_question: ""
character_type_hint: human/royal
morphology_hint: ""
scale_hint: ""
renderability_hint: authoritative, can be angry or melancholy.
confidence: 0
direct_identity_evidence: "said the King"
direct_visual_evidence: "folding his arms and frowning"
costume_or_covering_evidence: ""
movement_evidence: ""
associated_entities: queen, hatter, white_rabbit
alias_or_role_evidence: "His Majesty"
unknowns: ""
source_refs: ""

[[SECTION markdown]]
# King
**Role:** Judge/Authority figure.
**Status:** Physically present.
**Description:** The presiding authority in the court. He alternates between anger at the witnesses and a melancholy air of fatigue, often deferring cross-examination to the Queen.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: march_hare
canonical_character_id: CH011 March Hare
aliases: 
is_fully_identified: true
manual_description_required: false
manual_description_reason: ""
clarification_required: false
clarification_reason: ""
clarification_question: ""
character_type_hint: animal/creature
morphology_hint: ""
scale_hint: ""
renderability_hint: "interrupted in a great hurry"
confidence: 0.8
direct_identity_evidence: "said the March Hare"
direct_visual_evidence: ""
costume_or_covering_evidence: ""
movement_evidence: "interrupted in a great hurry"
associated_entities: hatter, king
alias_or_role_evidence: ""
unknowns: ""
source_refs: ""

[[SECTION markdown]]
# March Hare
**Role:** Court participant.
**Status:** Physically present.
**Description:** A character who interrupts the Hatter's testimony in a great hurry to argue about what was said.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: guinea_pig
canonical_character_id: CH011 Guinea-Pig
aliases: 
is_fully_identified: true
manual_description_required: false
manual_description_reason: ""
clarification_required: false
clarification_reason: ""
clarification_question: ""
character_type_hint: animal
morphology_hint: ""
scale_hint: small enough to fit in a canvas bag.
renderability_hint: being suppressed by sitting on them.
confidence: 0.7
direct_identity_evidence: "one of the guinea-pigs cheered"
direct_visual_evidence: "slipped the guinea-pig, head first"
costume_or_covering_evidence: ""
movement_evidence: "cheered"
associated_entities: officers
alias_or_role_evidence: ""
unknowns: ""
source_refs: ""

[[SECTION markdown]]
# Guinea-Pig
**Role:** Spectator/Audience.
**Status:** Physically present (referenced as a group).
**Description:** Small creatures in the court who cheer, only to be suppressed by being sat upon inside a large canvas bag.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: white_rabbit
canonical_character_id: CH011 White Rabbit
aliases: 
is_fully_identified: true
manual_description_required: false
manual_description_reason: ""
clarification_required: false
clarification_reason: ""
clarification_question: ""
character_type_hint: animal/creature
morphology_hint: ""
scale_hint: ""
renderability_hint: "shrill little voice", "fumbled over the list"
confidence: 0.9
direct_identity_evidence: "looked anxiously at the White Rabbit"
direct_visual_evidence: "fumbled over the list"
costume_or_covering_evidence: ""
movement_evidence: "fumbled"
associated_entities: king, alice
alias_or_role_evidence: "The next witness"
unknowns: ""
source_refs: ""

[[SECTION markdown]]
# White Rabbit
**Role:** Court official / Witness.
**Status:** Physically present.
**Description:** An official who manages the list of names and calls witnesses. He has a shrill voice and is seen fumbling with papers to decide the next witness.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: duchess_cook
canonical_character_id: CH011 Duchess's Cook
aliases: 
is_fully_identifed: true
manual_description_required: false
manual_description_reason: ""
clarification_required: false
clarification_reason: ""
clarification_question: ""
character_type_hint: human
morphology_hint: ""
scale_hint: ""
renderability_hint: carries a pepper-box.
confidence: 0.8
direct_identity_evidence: "The next witness was the Duchess’s cook"
direct_visual_evidence: "She carried the pepper-box in her hand"
costume_or_covering_evidence: ""
movement_evidence: ""
associated_entities: king, duchess
alias_or_role_evidence: "the cook"
unknowns: ""
source_refs: ""

[[SECTION markdown]]
# Duchess's Cook
**Role:** Witness.
**Status:** Physically present.
**Description:** The next witness called to the court. She carries a pepper-box and is the subject of much sneezing among the crowd.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
[[/FILMCREATOR_PACKET]]
````
