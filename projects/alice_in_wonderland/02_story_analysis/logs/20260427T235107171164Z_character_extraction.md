# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-27T23:51:07.171164+00:00
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

Chapter id: CH006

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

“Wow! wow! wow!”


While the Duchess sang the second verse of the song, she kept tossing
the baby violently up and down, and the poor little thing howled so,
that Alice could hardly hear the words:—

“I speak severely to my boy,
    I beat him when he sneezes;
For he can thoroughly enjoy
    The pepper when he pleases!”


CHORUS.


“Wow! wow! wow!”


“Here! you may nurse it a bit, if you like!” the Duchess said to Alice,
flinging the baby at her as she spoke. “I must go and get ready to play
croquet with the Queen,” and she hurried out of the room. The cook
threw a frying-pan after her as she went out, but it just missed her.

Alice caught the baby with some difficulty, as it was a queer-shaped
little creature, and held out its arms and legs in all directions,
“just like a star-fish,” thought Alice. The poor little thing was
snorting like a steam-engine when she caught it, and kept doubling
itself up and straightening itself out again, so that altogether, for
the first minute or two, it was as much as she could do to hold it.

As soon as she had made out the proper way of nursing it, (which was to
twist it up into a sort of knot, and then keep tight hold of its right
ear and left foot, so as to prevent its undoing itself,) she carried it
out into the open air. “If I don’t take this child away with me,”
thought Alice, “they’re sure to kill it in a day or two: wouldn’t it be
murder to leave it behind?” She said the last words out loud, and the
little thing grunted in reply (it had left off sneezing by this time).
“Don’t grunt,” said Alice; “that’s not at all a proper way of
expressing yourself.”

The baby grunted again, and Alice looked very anxiously into its face
to see what was the matter with it. There could be no doubt that it had
a _very_ turn-up nose, much more like a snout than a real nose; also
its eyes were getting extremely small for a baby: altogether Alice did
not like the look of the thing at all. “But perhaps it was only
sobbing,” she thought, and looked into its eyes again, to see if there
were any tears.

No, there were no tears. “If you’re going to turn into a pig, my dear,”
said Alice, seriously, “I’ll have nothing more to do with you. Mind
now!” The poor little thing sobbed again (or grunted, it was impossible
to say which), and they went on for some while in silence.

Alice was just beginning to think to herself, “Now, what am I to do
with this creature when I get it home?” when it grunted again, so
violently, that she looked down into its face in some alarm. This time
there could be _no_ mistake about it: it was neither more nor less than
a pig, and she felt that it would be quite absurd for her to carry it
further.

So she set the little creature down, and felt quite relieved to see it
trot away quietly into the wood. “If it had grown up,” she said to
herself, “it would have made a dreadfully ugly child: but it makes
rather a handsome pig, I think.” And she began thinking over other
children she knew, who might do very well as pigs, and was just saying
to herself, “if one only knew the right way to change them—” when she
was a little startled by seeing the Cheshire Cat sitting on a bough of
a tree a few yards off.

The Cat only grinned when it saw Alice. It looked good-natured, she
thought: still it had _very_ long claws and a great many teeth, so she
felt that it ought to be treated with respect.

“Cheshire Puss,” she began, rather timidly, as she did not at all know
whether it would like the name: however, it only grinned a little
wider. “Come, it’s pleased so far,” thought Alice, and she went on.
“Would you tell me, please, which way I ought to go from here?”

“That depends a good deal on where you want to get to,” said the Cat.

“I don’t much care where—” said Alice.

“Then it doesn’t matter which way you go,” said the Cat.

“—so long as I get _somewhere_,” Alice added as an explanation.

“Oh, you’re sure to do that,” said the Cat, “if you only walk long
enough.”

Alice felt that this could not be denied, so she tried another
question. “What sort of people live about here?”

“In _that_ direction,” the Cat said, waving its right paw round, “lives
a Hatter: and in _that_ direction,” waving the other paw, “lives a
March Hare. Visit either you like: they’re both mad.”

“But I don’t want to go among mad people,” Alice remarked.

“Oh, you can’t help that,” said the Cat: “we’re all mad here. I’m mad.
You’re mad.”

“How do you know I’m mad?” said Alice.

“You must be,” said the Cat, “or you wouldn’t have come here.”

Alice didn’t think that proved it at all; however, she went on “And how
do you know that you’re mad?”

“To begin with,” said the Cat, “a dog’s not mad. You grant that?”

“I suppose so,” said Alice.

“Well, then,” the Cat went on, “you see, a dog growls when it’s angry,
and wags its tail when it’s pleased. Now _I_ growl when I’m pleased,
and wag my tail when I’m angry. Therefore I’m mad.”

“_I_ call it purring, not growling,” said Alice.

“Call it what you like,” said the Cat. “Do you play croquet with the
Queen to-day?”

“I should like it very much,” said Alice, “but I haven’t been invited
yet.”

“You’ll see me there,” said the Cat, and vanished.

Alice was not much surprised at this, she was getting so used to queer
things happening. While she was looking at the place where it had been,
it suddenly appeared again.

“By-the-bye, what became of the baby?” said the Cat. “I’d nearly
forgotten to ask.”

“It turned into a pig,” Alice quietly said, just as if it had come back
in a natural way.

“I thought it would,” said the Cat, and vanished again.

Alice waited a little, half expecting to see it again, but it did not
appear, and after a minute or two she walked on in the direction in
which the March Hare was said to live. “I’ve seen hatters before,” she
said to herself; “the March Hare will be much the most interesting, and
perhaps as this is May it won’t be raving mad—at least not so mad as it
was in March.” As she said this, she looked up, and there was the Cat
again, sitting on a branch of a tree.

“Did you say pig, or fig?” said the Cat.

“I said pig,” replied Alice; “and I wish you wouldn’t keep appearing
and vanishing so suddenly: you make one quite giddy.”

“All right,” said the Cat; and this time it vanished quite slowly,
beginning with the end of the tail, and ending with the grin, which
remained some time after the rest of it had gone.

“Well! I’ve often seen a cat without a grin,” thought Alice; “but a
grin without a cat! It’s the most curious thing I ever saw in my life!”

She had not gone much farther before she came in sight of the house of
the March Hare: she thought it must be the right house, because the
chimneys were shaped like ears and the roof was thatched with fur. It
was so large a house, that she did not like to go nearer till she had
nibbled some more of the lefthand bit of mushroom, and raised herself
to about two feet high: even then she walked up towards it rather
timidly, saying to herself “Suppose it should be raving mad after all!
I almost wish I’d gone to see the Hatter instead!”
````

## Raw Response
````text
[[FILMCREATOR_PACKET]]

task: character_extraction

version: 1

character_index_markdown:

[[SECTION character_index_markdown]]

* [alice](#alice)
* [baby](#baby)
* [cheshire_cat](#cheshire_cat)
* [cook](#cook)
* [duchess](#ducess)
* [march_hare](#march_hare)
* [the_hatter](#the_hatter)
* [queen](#queen)

[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: alice
canonical_character_id: CH001 Alice
aliases: 
is_fully_identified: true
manual_description_required: false
manual_description_reason: 
clarification_required: false
clarification_reason: 
clarification_question: 
character_type_hint: human girl
morphology_hint: 
scale_hint: human-sized
renderability_hint: 
confidence: 0.9
direct_identity_evidence: true
direct_visual_evidence: true
costume_or_covering_evidence: false
movement_evidence: false
associated_entities: [baby, cheshire_cat, cook, duchess, march_hare, the_hatter, queen]
alias_or_role_evidence: false
unknowns: false
source_refs: 
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: baby
canonical_character_id: CH003 Baby
aliases: little thing, creature, pig
is_fully_identified: true
manual_description_required: false
manual_description_reason: 
clarification_required: false
clarification_reason: 
clarification_question: 
character_type_hint: shapeshifting infant/animal
morphology_hint: star-fish shaped, turn-up nose (snout), small eyes; eventually a pig.
scale_hint: small enough to be carried by Alice.
renderability_hint: 
confidence: 0.8
direct_identity_evidence: true
direct_visual_evidence: true
costume_or_covering_evidence: false
movement_evidence: doubling up and straightening out; trotting away as a pig.
associated_entities: [alice, duchess]
alias_or_role_evidence: true
unknowns: false
source_refs: 
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: cheshire_cat
canonical_character_id: CH004 Cheshire Cat
aliases: Cheshire Puss
is_fully_identified: true
manual_description_required: false
manual_description_reason: 
clarification_required: false
clarification_reason: 
clarification_question: 
character_type_hint: feline
morphology_hint: long claws, great many teeth, vanishing/reappearing ability.
scale_hint: cat-sized.
renderability_hint: 
confidence: 0.9
direct_identity_evidence: true
direct_visual_evidence: true
costume_or_covering_evidence: false
movement_evidence: sitting on a bough, vanishing/appearing.
associated_entities: [alice]
alias_or_role_evidence: true
unknowns: false
source_refs: 
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: cook
canonical_character_id: CH005 Cook
aliases: 
is_fully_identified: false
manual_description_required: true
manual_description_reason: Only mentioned as a brief action.
clarification_required: false
clarification_reason: 
clarification_question: 
character_type_hint: human
morphology_hint: 
scale_hint: human-sized
renderability_hint: 
confidence: 0.5
direct_identity_evidence: true
direct_visual_evidence: false
costume_or_covering_evidence: false
movement_evidence: throwing a frying-pan.
associated_entities: [duchess]
alias_or_role_evidence: false
unknowns: false
source_refs: 
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: duchess
canonical_character_id: CH006 Duchess
aliases: 
is_fully_identified: true
manual_description_required: false
manual_description_reason: 
clarification_required: false
clarification_reason: 
clarification_question: 
character_type_hint: human
morphology_hint: 
scale_hint: human-sized
renderability_hint: 
confidence: 0.7
direct_identity_evidence: true
direct_visual_evidence: false
costume_or_covering_evidence: false
movement_evidence: singing and tossing the baby.
associated_entities: [baby, cook, alice]
alias_or_role_evidence: false
unknowns: false
source_refs: 
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: march_hare
canonical_character_id: CH007 March Hare
aliases: 
is_fully_identified: false
manual_description_required: true
manual_description_reason: Referenced but not physically present in the scene.
clarification_required: false
clarification_reason: 
clarration_question: 
character_type_hint: anthropomorphic hare
morphology_hint: 
scale_hint: 
renderability_hint: 
confidence: 0.4
direct_identity_evidence: true
direct_visual_evidence: false
costume_or_covering_evidence: false
movement_evidence: false
associated_entities: [alice, cheshire_cat]
alias_or_role_evidence: true
unknowns: true
source_refs: 
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: the_hatter
canonical_character_id: CH008 The Hatter
aliases: 
is_fully_identified: false
manual_description_required: true
manual_description_reason: Referenced but not physically present.
clarification_required: false
clarification_reason: 
clarification_question: 
character_type_hint: human/anthropomorphic
morphology_hint: 
scale_hint: 
renderability_hint: 
confidence: 0.4
direct_identity_evidence: true
direct_visual_evidence: false
costume_or_covering_evidence: false
movement_evidence: false
associated_entities: [alice, cheshire_cat]
alias_or_role_evidence: true
unknowns: true
source_refs: 
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: queen
canonical_character_id: CH009 Queen
aliases: 
is_fully_identified: false
manual_description_required: true
manual_description_reason: Referenced but not physically present.
clarification_required: false
clarification_reason: 
clarification_question: 
character_type_hint: human/anthropomorphic
morphology_hint: 
scale_hint: 
renderability_hint: 
confidence: 0.4
direct_identity_evidence: true
direct_visual_evidence: false
costume_or_covering_evidence: false
movement_evidence: false
associated_entities: [duchess]
alias_or_role_evidence: true
unknowns: true
source_refs: 
[[/FILMCREATOR_RECORD]]

[[SECTION markdown]]
# Alice
*Role: Protagonist / Traveler*
**Status:** Physically Present.
**Description:** A young girl who is currently about two feet high after eating mushroom. She is curious, somewhat polite but firm in her logic, and prone to questioning the strange things around her.
**Notes:** Currently navigating a wood-like environment with large houses (like the March Hare's) that have ear-shaped chimneys and fur-thatched roofs.
[[/SECTION]]

[[SECTION markdown]]
# Baby
*Role: The "Creature" being carried*
**Status:** Physically Present (until it trots away).
**Description:** A queer-shaped little creature with a turn-up nose like a snout and eyes that shrink as it ages. It is capable of doubling up or straightening out like a starfish. 
**Notes:** Eventually transforms into a pig, at which point it becomes a "handsome pig" and trots off into the woods.
[[/SECTION]]

[[SECTION markdown]]
# Cheshire Cat
*Role: Guide / Enigmatic Entity*
**Status:** Physically Present.
**Description:** A cat with very long claws and a great many teeth, capable of vanishing entirely, leaving only its grin behind. It is wise-cracking and slightly mischievous.
**Notes:** Its presence is marked by the ability to disappear and reappear suddenly, sometimes leaving just a floating grin.
[[/SECTION]]

[[SECTION markdown]]
# Cook
*Role: Supporting Character (Brief)*
**Status:** Physically Present (briefly).
**Description:** A domestic worker who throws a frying-pan after the Duchess as she leaves.
**Notes:** Likely an inhabitant of the Duchess's household.
[[-%/SECTION]]

[[SECTION markdown]]
# Duchess
*Role: Supporting Character*
**Status:** Physically Present (briefly).
**Description:** A woman who sings a verse about beating her son and tosses the baby violently to Alice.
**Notes:** She is in a hurry to play croquet with the Queen.
[[/SECTION]]

[[SECTION markdown]]
# March Hare
*Role: Referenced Character*
**Status:** Referenced (not physically present).
**Description:** A resident of the area, described as "mad." His house has chimneys shaped like ears and a roof thatched with fur.
**Notes:** Alice is heading toward his house at the end of the chapter.
[[/SECTION]]

[[SECTION markdown]]
# The Hatter
*Role: Referenced Character*
**Status:** Referenced (not physically present).
**Description:** A resident living in a certain direction, described as "mad."
**Notes:** Mentioned by the Cheshire Cat as a local inhabitant.
[[/SECTION]]

[[SECTION markdown]]
# Queen
*Role: Referenced Character*
**Status:** Referenced (not physically present).
**Description:** The person the Duchess is going to play croquet with.
**Notes:** A figure of authority in this land.
[[-%/SECTION]]

[[/FILMCREATOR_PACKET]]
````
