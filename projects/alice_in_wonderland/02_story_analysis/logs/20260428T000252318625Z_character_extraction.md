# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-28T00:02:52.318625+00:00
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

Chapter id: CH008

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

“Did you say ‘What a pity!’?” the Rabbit asked.

“No, I didn’t,” said Alice: “I don’t think it’s at all a pity. I said
‘What for?’”

“She boxed the Queen’s ears—” the Rabbit began. Alice gave a little
scream of laughter. “Oh, hush!” the Rabbit whispered in a frightened
tone. “The Queen will hear you! You see, she came rather late, and the
Queen said—”

“Get to your places!” shouted the Queen in a voice of thunder, and
people began running about in all directions, tumbling up against each
other; however, they got settled down in a minute or two, and the game
began. Alice thought she had never seen such a curious croquet-ground
in her life; it was all ridges and furrows; the balls were live
hedgehogs, the mallets live flamingoes, and the soldiers had to double
themselves up and to stand on their hands and feet, to make the arches.

The chief difficulty Alice found at first was in managing her flamingo:
she succeeded in getting its body tucked away, comfortably enough,
under her arm, with its legs hanging down, but generally, just as she
had got its neck nicely straightened out, and was going to give the
hedgehog a blow with its head, it _would_ twist itself round and look
up in her face, with such a puzzled expression that she could not help
bursting out laughing: and when she had got its head down, and was
going to begin again, it was very provoking to find that the hedgehog
had unrolled itself, and was in the act of crawling away: besides all
this, there was generally a ridge or furrow in the way wherever she
wanted to send the hedgehog to, and, as the doubled-up soldiers were
always getting up and walking off to other parts of the ground, Alice
soon came to the conclusion that it was a very difficult game indeed.

The players all played at once without waiting for turns, quarrelling
all the while, and fighting for the hedgehogs; and in a very short time
the Queen was in a furious passion, and went stamping about, and
shouting “Off with his head!” or “Off with her head!” about once in a
minute.

Alice began to feel very uneasy: to be sure, she had not as yet had any
dispute with the Queen, but she knew that it might happen any minute,
“and then,” thought she, “what would become of me? They’re dreadfully
fond of beheading people here; the great wonder is, that there’s any
one left alive!”

She was looking about for some way of escape, and wondering whether she
could get away without being seen, when she noticed a curious
appearance in the air: it puzzled her very much at first, but, after
watching it a minute or two, she made it out to be a grin, and she said
to herself “It’s the Cheshire Cat: now I shall have somebody to talk
to.”

“How are you getting on?” said the Cat, as soon as there was mouth
enough for it to speak with.

Alice waited till the eyes appeared, and then nodded. “It’s no use
speaking to it,” she thought, “till its ears have come, or at least one
of them.” In another minute the whole head appeared, and then Alice put
down her flamingo, and began an account of the game, feeling very glad
she had someone to listen to her. The Cat seemed to think that there
was enough of it now in sight, and no more of it appeared.

“I don’t think they play at all fairly,” Alice began, in rather a
complaining tone, “and they all quarrel so dreadfully one can’t hear
oneself speak—and they don’t seem to have any rules in particular; at
least, if there are, nobody attends to them—and you’ve no idea how
confusing it is all the things being alive; for instance, there’s the
arch I’ve got to go through next walking about at the other end of the
ground—and I should have croqueted the Queen’s hedgehog just now, only
it ran away when it saw mine coming!”

“How do you like the Queen?” said the Cat in a low voice.

“Not at all,” said Alice: “she’s so extremely—” Just then she noticed
that the Queen was close behind her, listening: so she went on,
“—likely to win, that it’s hardly worth while finishing the game.”

The Queen smiled and passed on.

“Who _are_ you talking to?” said the King, going up to Alice, and
looking at the Cat’s head with great curiosity.

“It’s a friend of mine—a Cheshire Cat,” said Alice: “allow me to
introduce it.”

“I don’t like the look of it at all,” said the King: “however, it may
kiss my hand if it likes.”

“I’d rather not,” the Cat remarked.

“Don’t be impertinent,” said the King, “and don’t look at me like
that!” He got behind Alice as he spoke.

“A cat may look at a king,” said Alice. “I’ve read that in some book,
but I don’t remember where.”

“Well, it must be removed,” said the King very decidedly, and he called
the Queen, who was passing at the moment, “My dear! I wish you would
have this cat removed!”

The Queen had only one way of settling all difficulties, great or
small. “Off with his head!” she said, without even looking round.

“I’ll fetch the executioner myself,” said the King eagerly, and he
hurried off.

Alice thought she might as well go back, and see how the game was going
on, as she heard the Queen’s voice in the distance, screaming with
passion. She had already heard her sentence three of the players to be
executed for having missed their turns, and she did not like the look
of things at all, as the game was in such confusion that she never knew
whether it was her turn or not. So she went in search of her hedgehog.

The hedgehog was engaged in a fight with another hedgehog, which seemed
to Alice an excellent opportunity for croqueting one of them with the
other: the only difficulty was, that her flamingo was gone across to
the other side of the garden, where Alice could see it trying in a
helpless sort of way to fly up into a tree.

By the time she had caught the flamingo and brought it back, the fight
was over, and both the hedgehogs were out of sight: “but it doesn’t
matter much,” thought Alice, “as all the arches are gone from this side
of the ground.” So she tucked it away under her arm, that it might not
escape again, and went back for a little more conversation with her
friend.

When she got back to the Cheshire Cat, she was surprised to find quite
a large crowd collected round it: there was a dispute going on between
the executioner, the King, and the Queen, who were all talking at once,
while all the rest were quite silent, and looked very uncomfortable.

The moment Alice appeared, she was appealed to by all three to settle
the question, and they repeated their arguments to her, though, as they
all spoke at once, she found it very hard indeed to make out exactly
what they said.

The executioner’s argument was, that you couldn’t cut off a head unless
there was a body to cut it off from: that he had never had to do such a
thing before, and he wasn’t going to begin at _his_ time of life.

The King’s argument was, that anything that had a head could be
beheaded, and that you weren’t to talk nonsense.

The Queen’s argument was, that if something wasn’t done about it in
less than no time she’d have everybody executed, all round. (It was
this last remark that had made the whole party look so grave and
anxious.)

Alice could think of nothing else to say but “It belongs to the
Duchess: you’d better ask _her_ about it.”

“She’s in prison,” the Queen said to the executioner: “fetch her here.”
And the executioner went off like an arrow.

The Cat’s head began fading away the moment he was gone, and, by the
time he had come back with the Duchess, it had entirely disappeared; so
the King and the executioner ran wildly up and down looking for it,
while the rest of the party went back to the game.
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
- [Cheshire Cat](#cheshire_cat)
- [Duchess](#duchess)
- [Executioner](#executioner)
- [King](#king)
- [Queen](#queen)
- [Rabbit](#rabbit)
- [Soldiers](#soldiers)

[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: alice
canonical_character_id: CH001 Alice
aliases: 
is_fully_identified: true
manual_description_required: false
manual_description_reason: ""
clarification_required: false
clarification_reason: ""
clarification_question: ""
character_type_hint: human
morphology_hint: human girl
scale_hint: human scale
renderability_hint: high
confidence: 0.9
direct_identity_evidence: true
direct_visual_evidence: true
costume_or_covering_evidence: false
movement_evidence: true
associated_entities: [cheshire_cat, rabbit, queen, king, executioner]
alias_or_role_evidence: true
unknowns: ""
source_refs: ""

[[SECTION markdown]]
# Alice
**Role:** Protagonist / Player in the croquet game.

**Status:** Physically present.

**Description:** A young girl participating in a chaotic game of croquet using live animals as equipment. She is prone to laughter and can be easily unsettled by the Queen's temper.

**Traits:** 
- Curious and conversational.
- Easily distracted by the living nature of her flamingo and hedgehog.
- Observant of the strange phenomena (like the Cat's grin).

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: cheshire_cat
canonical_character_id: CH003 Cheshire Cat
aliases: The Cat
is_fully_identified: true
manual_description_required: false
manual_description_reason: ""
clarification_required: false
clarification_reason: ""
clarification_question: ""
character_type_hint: feline / supernatural
morphology_hint: a floating head that fades in and out.
scale_hint: head-sized or larger.
renderability_hint: high (requires transparency/fading effects).
confidence: 0.9
direct_identity_evidence: true
direct_visual_evidence: true
costume_or_covering_evidence: false
movement_evidence: true
associated_entities: [alice, king, queen]
alias_or_role_evidence: true
unknowns: ""
source_refs: ""

[[SECTION markdown]]
# Cheshire Cat
**Role:** An enigmatic entity appearing to Alice.

**Status:** Physically present (appearing/disappearing).

**Description:** A creature that manifests as a grin in the air before its eyes and head appear. It is capable of fading away entirely, leaving only its grin behind.

**Traits:** 
- Impertious and independent.
- Can speak with whatever part of itself is visible.
- Mysterious; fades from view when tension rises.

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILいFILMCREATOR_RECORD]]
type: character
asset_id: duchess
canonical_character_id: CH004 Duchess
aliases: 
is_fully_identified: true
manual_description_required: true
manual_description_reason: Mentioned as being in prison; physical description is sparse.
clarification_required: false
clarification_reason: ""
clarification_question: ""
character_type_hint: human
morphology_hint: unknown
scale_hint: human scale
renderability_hint: medium
confidence: 0.7
direct_identity_evidence: true
direct_visual_evidence: false
costume_or_covering_evidence: false
movement_evidence: false
associated_entities: [queen, executioner]
alias_or_role_evidence: true
unknowns: "Physical appearance not described in this chapter."
source_refs: ""

[[SECTION markdown]]
# Duchess
**Role:** A prisoner/authority figure.

**Status:** Referenced (briefly appearing at the end).

**Description:** Currently held in prison by the Queen's command.

**Traits:** 
- Mentioned as a subject of debate regarding the Cat's fate.

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: executioner
canonical_character_id: CH005 Executioner
aliases: 
is_fully_identified: true
manual_description_required: false
manual_description_reason: ""
clarification_required: false
clarification_reason: ""
clarification_question: ""
character_type_hint: human
morphology_hint: unknown
scale_hint: human scale
renderability_hint: medium
confidence: 0.8
direct_identity_evidence: true
direct_visual_evidence: false
costume_or_covering_evidence: false
movement_evidence: true
associated_entities: [queen, king, duchess]
alias_or_role_evidence: true
unknowns: ""
source_refs: ""

[[SECTION markdown]]
# Executioner
**Role:** The Queen's enforcer.

**Status:** Physically present (as a character/worker).

**Description:** A man tasked with the physical act of beheading, currently arguing about the logistics of cutting heads from bodies.

**Traits:** 
- Efficient and eager to fetch prisoners or carry out sentences.
- Concerned with the practicalities of his job at his "time of life."

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: king
canonical_character_id: CH006 King
aliases: 
is_fully_identified: true
manual_description_required: false
manual_description_reason: ""
clarification_required: false
clarification_reason: ""
clarification_question: ""
character_type_hint: human
morphology_hint: unknown
scale_hint: human scale
renderability_hint: medium
confidence: 0.8
direct_identity_evidence: true
direct_visual_evidence: false
coststant_or_covering_evidence: false
movement_evidence: true
associated_entities: [queen, alice, executioner]
alias_or_role_evidence: true
unknowns: ""
source_refs: ""

[[SECTION markdown]]
# King
**Role:** Ruler / Alice's interlocutor.

**Status:** Physically present.

**Description:** A ruler who interacts with Alice and the Cat, often standing behind her or arguing with the Queen/Executioner.

**Traits:** 
- Curious about the Cat but finds it impertinent.
- Tries to maintain order through debate and calls for the executioner.

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: queen
canonical_character_id: CH007 Queen
aliases: 
is_fully_identified: true
manual_description_required: false
manual_description_reason: ""
clarification_required: false
clarification_reason: ""
clarification_question: ""
character_type_hint: human
morphology_hint: unknown
scale_hint: human scale
renderability_hint: medium
confidence: 0.8
direct_identity_evidence: true
direct_visual_evidence: false
costume_or_covering_evidence: false
movement_evidence: true
associated_entities: [king, alice, executioner]
alias_or_role_evidence: true
unknowns: ""
source_refs: ""

[[SECTION markdown]]
# Queen
**Role:** Ruler / Antagonist.

**Status:** Physically present.

**Description:** A temperamental ruler with a voice like thunder who frequently orders executions.

**Traits:** 
- Furious and passionate; prone to stamping about.
- Rules through the threat of beheading.
- Settles all difficulties with immediate, often arbitrary, sentences.

[[/SECTION]]
[[/FILcut_record]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: rabbit
canonical_character_id: CH008 Rabbit
aliases: 
is_fully_identified: true
manual_description_required: false
manual_description_reason: ""
clarification_required: false
clarification_reason: ""
clarification_question: ""
character_type_hint: animal/humanoid
morphology_hint: unknown (likely a rabbit)
scale_hint: small to human-ish scale.
renderability_hint: medium
confidence: 0.8
direct_identity_evidence: true
direct_visual_evidence: false
costume_or_covering_evidence: false
movement_evidence: true
associated_entities: [alice]
alias_or_role_evidence: true
unknowns: ""
source_refs: ""

[[SECTION markdown]]
# Rabbit
**Role:** Messenger / Informant.

**Status:** Physically present (at the start).

**Description:** A character who communicates with Alice about the Queen's actions and the unfolding game.

**Traits:** 
- Nervous or frightened by the Queen's presence.
- Provides context for the current situation to Alice.

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: soldiers
canonical_character_id: CH009 Soldiers
aliases: 
is_fully_identified: true
manual_description_required: false
manual_description_reason: ""
clarification_required: false
clarification_reason: ""
clarification_question: ""
character_type_hint: human/card-like
morphology_hint: they double themselves up to form arches.
scale_hint: human scale.
renderability_hint: medium
confidence: 0.8
direct_identity_evidence: true
direct_visual_evidence: false
costume_or_covering_evidence: false
movement_evidence: true
associated_entities: [queen]
alias_or_role_evidence: true
unknowns: ""
source_refs: ""

[[SECTION markdown]]
# Soldiers
**Role:** The game's arches.

**Status:** Physically present (as part of the environment).

**Description:** They serve as the living structures for the croquet match, doubling themselves up to stand on hands and feet to form arches.

**Traits:** 
- They are prone to walking off to other parts of the ground mid-game.

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
