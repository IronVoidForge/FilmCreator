# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-27T23:26:01.122250+00:00
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

Chapter id: CH003

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

Fallback extraction chunk 1/2 for character_extraction.

Use only the chapter excerpt below for this pass.

# Chapter
CH003

# Title
CHAPTER III.

# Text
A Caucus-Race and a Long Tale


They were indeed a queer-looking party that assembled on the bank—the
birds with draggled feathers, the animals with their fur clinging close
to them, and all dripping wet, cross, and uncomfortable.

The first question of course was, how to get dry again: they had a
consultation about this, and after a few minutes it seemed quite
natural to Alice to find herself talking familiarly with them, as if
she had known them all her life. Indeed, she had quite a long argument
with the Lory, who at last turned sulky, and would only say, “I am
older than you, and must know better;” and this Alice would not allow
without knowing how old it was, and, as the Lory positively refused to
tell its age, there was no more to be said.

At last the Mouse, who seemed to be a person of authority among them,
called out, “Sit down, all of you, and listen to me! _I’ll_ soon make
you dry enough!” They all sat down at once, in a large ring, with the
Mouse in the middle. Alice kept her eyes anxiously fixed on it, for she
felt sure she would catch a bad cold if she did not get dry very soon.

“Ahem!” said the Mouse with an important air, “are you all ready? This
is the driest thing I know. Silence all round, if you please! ‘William
the Conqueror, whose cause was favoured by the pope, was soon submitted
to by the English, who wanted leaders, and had been of late much
accustomed to usurpation and conquest. Edwin and Morcar, the earls of
Mercia and Northumbria—’”

“Ugh!” said the Lory, with a shiver.

“I beg your pardon!” said the Mouse, frowning, but very politely: “Did
you speak?”

“Not I!” said the Lory hastily.

“I thought you did,” said the Mouse. “—I proceed. ‘Edwin and Morcar,
the earls of Mercia and Northumbria, declared for him: and even
Stigand, the patriotic archbishop of Canterbury, found it advisable—’”

“Found _what_?” said the Duck.

“Found _it_,” the Mouse replied rather crossly: “of course you know
what ‘it’ means.”

“I know what ‘it’ means well enough, when _I_ find a thing,” said the
Duck: “it’s generally a frog or a worm. The question is, what did the
archbishop find?”

The Mouse did not notice this question, but hurriedly went on, “‘—found
it advisable to go with Edgar Atheling to meet William and offer him
the crown. William’s conduct at first was moderate. But the insolence
of his Normans—’ How are you getting on now, my dear?” it continued,
turning to Alice as it spoke.

“As wet as ever,” said Alice in a melancholy tone: “it doesn’t seem to
dry me at all.”

“In that case,” said the Dodo solemnly, rising to its feet, “I move
that the meeting adjourn, for the immediate adoption of more energetic
remedies—”

“Speak English!” said the Eaglet. “I don’t know the meaning of half
those long words, and, what’s more, I don’t believe you do either!” And
the Eaglet bent down its head to hide a smile: some of the other birds
tittered audibly.

“What I was going to say,” said the Dodo in an offended tone, “was,
that the best thing to get us dry would be a Caucus-race.”

“What _is_ a Caucus-race?” said Alice; not that she wanted much to
know, but the Dodo had paused as if it thought that _somebody_ ought to
speak, and no one else seemed inclined to say anything.

“Why,” said the Dodo, “the best way to explain it is to do it.” (And,
as you might like to try the thing yourself, some winter day, I will
tell you how the Dodo managed it.)

First it marked out a race-course, in a sort of circle, (“the exact
shape doesn’t matter,” it said,) and then all the party were placed
along the course, here and there. There was no “One, two, three, and
away,” but they began running when they liked, and left off when they
liked, so that it was not easy to know when the race was over. However,
when they had been running half an hour or so, and were quite dry
again, the Dodo suddenly called out “The race is over!” and they all
crowded round it, panting, and asking, “But who has won?”

This question the Dodo could not answer without a great deal of
thought, and it sat for a long time with one finger pressed upon its
forehead (the position in which you usually see Shakespeare, in the
pictures of him), while the rest waited in silence. At last the Dodo
said, “_Everybody_ has won, and all must have prizes.”

“But who is to give the prizes?” quite a chorus of voices asked.

“Why, _she_, of course,” said the Dodo, pointing to Alice with one
finger; and the whole party at once crowded round her, calling out in a
confused way, “Prizes! Prizes!”

Alice had no idea what to do, and in despair she put her hand in her
pocket, and pulled out a box of comfits, (luckily the salt water had
not got into it), and handed them round as prizes. There was exactly
````

## Raw Response
````text

````
