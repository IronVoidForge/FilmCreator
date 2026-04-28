# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-28T00:01:02.371299+00:00
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
- [White Rabbit](#white_rabbit)
- [Queen of Hearts](#queen_of_hearts)
- [Cheshire Cat](#cheshire_cat)
- [King of Hearts](#king_of_hearts)
- [Executioner](#executioner)
- [Duchess](#duchess)
[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: alice
canonical_character_id: CH001 Alice
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
confidence: 1.0
direct_identity_evidence: "Alice is a named character interacting with the Rabbit, Queen, and Cat."
direct_visual_evidence: ""
costume_or_covering_evidence: ""
movement_evidence: ""
associated_entities: [white_rabbit, queen_of_hearts, cheshire_cat, king_of_hearts, executioner, duchess]
alias_or_role_evidence: ""
unknowns: ""
source_refs: ""

[[SECTION markdown]]
# Alice
**Role:** Protagonist.
**Presence:** Physically present throughout the chapter.
**Description:** A young girl participating in a chaotic game of croquet. She is prone to laughter and finds the living game pieces (flamingos and hedgehogs) both difficult and amusing to manage.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: white_rabbit
canonical_character_id: CH003 White Rabbit
aliases: The Rabbit
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
direct_identity_evidence: "The Rabbit is speaking to Alice about the Queen."
direct_visual_evidence: ""
costume_or_covering_evidence: ""
movement_evidence: ""
associated_entities: [alice, queen_of_hearts]
alias_or_role_evidence: ""
unknowns: ""
source_refs: ""

[[SECTION markdown]]
# White Rabbit
**Role:** Messenger/Informant.
**Presence:** Physically present in the opening scene.
**Description:** A small animal who warns Alice about the Queen's temper and the consequences of her laughter.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: queen_of_hearts
canonical_character_id: CH004 Queen of Hearts
aliases: The Queen
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
direct_identity_evidence: "The Queen is a central authority figure in the game."
direct_visual_evidence: ""
costume_or_covering_evidence: ""
movement_s_evidence: "Stamps about in fury; passes through the garden."
associated_entities: [alice, king_of_hearts, executioner, duchess]
alias_or_role_evidence: ""
unknowns: ""
source_refs: ""

[[SECTION markdown]]
# Queen of Hearts
**Role:** Antagonist/Authority.
**Presence:** Physically present.
**Description:** A volatile and furious ruler who frequently commands executions ("Off with his head!"). She is a dominant, commanding presence in the croquet game.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: cheshire_cat
canonical_character_id: CH005 Cheshire Cat
aliases: The Cat
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
direct_identity_evidence: "Alice identifies the appearance as the Cheshire Cat."
direct_visual_evidence: "Appears first as a grin in the air, then eyes, then a full head; fades away partially."
costume_or_covering_evidence: ""
movement_evidence: "Fades in and out of visibility."
associated_entities: [alice, king_of_hearts]
alias_or_role_evidence: ""
unknowns: ""
source_refs: ""

[[SECTION markdown]]
# Cheshire Cat
**Role:** Confidant/Enigma.
**Presence:** Physically present (appearing and disappearing).
**Description:** A creature that manifests as a floating grin in the air before its full head appears. It is capable of fading from view, leaving only parts of itself visible to Alice.
[[/end_section]]
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: king_of_hearts
canonical_character_id: CH006 King of Hearts
aliases: The King
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
direct_identity_evidence: "The King interacts with Alice and the Queen."
direct_visual_evidence: ""
costume_or_covering_evidence: ""
movement_evidence: "He gets behind Alice; runs after the Cat."
associated_entities: [queen_of_hearts, alice, executioner]
alias_or_role_evidence: ""
unknowns: ""
source_refs: ""

[[SECTION markdown]]
# King of Hearts
**Role:** Authority/Consort.
**Presence:** Physically present.
**Description:** A curious and somewhat indecisive ruler who argues with the executioner and the Queen regarding the Cat's fate. He is often seen in the company of the Queen.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: executioner
canonical_character_id: CH007 Executioner
aliases: The Executioner
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
direct_identity_evidence: "The executioner is a distinct character in the group."
direct_visual_evidence: ""
coststant_or_covering_evidence: ""
movement_evidence: "Runs off like an arrow to fetch the Duchess."
associated_entities: [queen_of_hearts, king_of_hearts]
alias_or_role_evidence: ""
unknowns: ""
source_refs: ""

[[SECTION markdown]]
# Executioner
**Role:** Official/Worker.
**Presence:** Physically present.
**Description:** A man tasked with carrying out the Queen's commands. He engages in logical disputes about the practicality of beheading heads without bodies.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: duchess
canonical_character_id: CH008 Duchess
aliases: The Duchess
is_fully_identified: false
manual_description_required: true
manual_description_reason: "Only mentioned as being in prison; her physical appearance is not described."
clarification_required: true
clarification_reason: "Physical description is missing from this chapter."
clarification_question: "What does the Duchess look like?"
character_type_hint: humanoid_nonhuman
morphology_hint: biped
scale_hint: human_scale
renderability_hint: context_only
confidence: 0.7
direct_identity_evidence: "Mentioned by Alice and fetched by the executioner."
direct_visual_evidence: ""
costume_or_covering_evidence: ""
movement_evidence: ""
associated_entities: [queen_of_hearts]
alias_or_role_evidence: ""
unknowns: ""
source_refs: ""

[[SECTION markdown]]
# Duchess
**Role:** Prisoner/Subject.
**Presence:** Referenced (and briefly appears at the end).
**Description:** A figure currently in prison, brought forth to settle a dispute about the Cat. Her physical appearance is not yet established.
[[/SECTION]]
[[/FILMCREcut_record]]

[[/FILMCREATOR_PACKET]]
````
