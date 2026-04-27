# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-27T23:32:01.151739+00:00
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

Fallback extraction chunk 2/2 for character_extraction.

Use only the chapter excerpt below for this pass.

finger; and the whole party at once crowded round her, calling out in a
confused way, “Prizes! Prizes!”

Alice had no idea what to do, and in despair she put her hand in her
pocket, and pulled out a box of comfits, (luckily the salt water had
not got into it), and handed them round as prizes. There was exactly
one a-piece, all round.

“But she must have a prize herself, you know,” said the Mouse.

“Of course,” the Dodo replied very gravely. “What else have you got in
your pocket?” he went on, turning to Alice.

“Only a thimble,” said Alice sadly.

“Hand it over here,” said the Dodo.

Then they all crowded round her once more, while the Dodo solemnly
presented the thimble, saying “We beg your acceptance of this elegant
thimble;” and, when it had finished this short speech, they all
cheered.

Alice thought the whole thing very absurd, but they all looked so grave
that she did not dare to laugh; and, as she could not think of anything
to say, she simply bowed, and took the thimble, looking as solemn as
she could.

The next thing was to eat the comfits: this caused some noise and
confusion, as the large birds complained that they could not taste
theirs, and the small ones choked and had to be patted on the back.
However, it was over at last, and they sat down again in a ring, and
begged the Mouse to tell them something more.

“You promised to tell me your history, you know,” said Alice, “and why
it is you hate—C and D,” she added in a whisper, half afraid that it
would be offended again.

“Mine is a long and a sad tale!” said the Mouse, turning to Alice, and
sighing.

“It _is_ a long tail, certainly,” said Alice, looking down with wonder
at the Mouse’s tail; “but why do you call it sad?” And she kept on
puzzling about it while the Mouse was speaking, so that her idea of the
tale was something like this:—

         “Fury said to a mouse, That he met in the house, ‘Let us both
         go to law: _I_ will prosecute _you_.—Come, I’ll take no
         denial; We must have a trial: For really this morning I’ve
         nothing to do.’ Said the mouse to the cur, ‘Such a trial, dear
         sir, With no jury or judge, would be wasting our breath.’
         ‘I’ll be judge, I’ll be jury,’ Said cunning old Fury: ‘I’ll
         try the whole cause, and condemn you to death.’”

“You are not attending!” said the Mouse to Alice severely. “What are
you thinking of?”

“I beg your pardon,” said Alice very humbly: “you had got to the fifth
bend, I think?”

“I had _not!_” cried the Mouse, sharply and very angrily.

“A knot!” said Alice, always ready to make herself useful, and looking
anxiously about her. “Oh, do let me help to undo it!”

“I shall do nothing of the sort,” said the Mouse, getting up and
walking away. “You insult me by talking such nonsense!”

“I didn’t mean it!” pleaded poor Alice. “But you’re so easily offended,
you know!”

The Mouse only growled in reply.

“Please come back and finish your story!” Alice called after it; and
the others all joined in chorus, “Yes, please do!” but the Mouse only
shook its head impatiently, and walked a little quicker.

“What a pity it wouldn’t stay!” sighed the Lory, as soon as it was
quite out of sight; and an old Crab took the opportunity of saying to
her daughter “Ah, my dear! Let this be a lesson to you never to lose
_your_ temper!” “Hold your tongue, Ma!” said the young Crab, a little
snappishly. “You’re enough to try the patience of an oyster!”

“I wish I had our Dinah here, I know I do!” said Alice aloud,
addressing nobody in particular. “She’d soon fetch it back!”

“And who is Dinah, if I might venture to ask the question?” said the
Lory.

Alice replied eagerly, for she was always ready to talk about her pet:
“Dinah’s our cat. And she’s such a capital one for catching mice you
can’t think! And oh, I wish you could see her after the birds! Why,
she’ll eat a little bird as soon as look at it!”

This speech caused a remarkable sensation among the party. Some of the
birds hurried off at once: one old Magpie began wrapping itself up very
carefully, remarking, “I really must be getting home; the night-air
doesn’t suit my throat!” and a Canary called out in a trembling voice
to its children, “Come away, my dears! It’s high time you were all in
bed!” On various pretexts they all moved off, and Alice was soon left
alone.

“I wish I hadn’t mentioned Dinah!” she said to herself in a melancholy
tone. “Nobody seems to like her, down here, and I’m sure she’s the best
cat in the world! Oh, my dear Dinah! I wonder if I shall ever see you
any more!” And here poor Alice began to cry again, for she felt very
lonely and low-spirited. In a little while, however, she again heard a
little pattering of footsteps in the distance, and she looked up
eagerly, half hoping that the Mouse had changed his mind, and was
coming back to finish his story.
````

## Raw Response
````text

````
