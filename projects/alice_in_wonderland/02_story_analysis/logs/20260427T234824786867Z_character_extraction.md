# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-27T23:48:24.786867+00:00
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

Fallback extraction chunk 1/2 for character_extraction.

Use only the chapter excerpt below for this pass.

# Chapter
CH006

# Title
CHAPTER VI.

# Text
Pig and Pepper


For a minute or two she stood looking at the house, and wondering what
to do next, when suddenly a footman in livery came running out of the
wood—(she considered him to be a footman because he was in livery:
otherwise, judging by his face only, she would have called him a
fish)—and rapped loudly at the door with his knuckles. It was opened by
another footman in livery, with a round face, and large eyes like a
frog; and both footmen, Alice noticed, had powdered hair that curled
all over their heads. She felt very curious to know what it was all
about, and crept a little way out of the wood to listen.

The Fish-Footman began by producing from under his arm a great letter,
nearly as large as himself, and this he handed over to the other,
saying, in a solemn tone, “For the Duchess. An invitation from the
Queen to play croquet.” The Frog-Footman repeated, in the same solemn
tone, only changing the order of the words a little, “From the Queen.
An invitation for the Duchess to play croquet.”

Then they both bowed low, and their curls got entangled together.

Alice laughed so much at this, that she had to run back into the wood
for fear of their hearing her; and when she next peeped out the
Fish-Footman was gone, and the other was sitting on the ground near the
door, staring stupidly up into the sky.

Alice went timidly up to the door, and knocked.

“There’s no sort of use in knocking,” said the Footman, “and that for
two reasons. First, because I’m on the same side of the door as you
are; secondly, because they’re making such a noise inside, no one could
possibly hear you.” And certainly there _was_ a most extraordinary
noise going on within—a constant howling and sneezing, and every now
and then a great crash, as if a dish or kettle had been broken to
pieces.

“Please, then,” said Alice, “how am I to get in?”

“There might be some sense in your knocking,” the Footman went on
without attending to her, “if we had the door between us. For instance,
if you were _inside_, you might knock, and I could let you out, you
know.” He was looking up into the sky all the time he was speaking, and
this Alice thought decidedly uncivil. “But perhaps he can’t help it,”
she said to herself; “his eyes are so _very_ nearly at the top of his
head. But at any rate he might answer questions.—How am I to get in?”
she repeated, aloud.

“I shall sit here,” the Footman remarked, “till tomorrow—”

At this moment the door of the house opened, and a large plate came
skimming out, straight at the Footman’s head: it just grazed his nose,
and broke to pieces against one of the trees behind him.

“—or next day, maybe,” the Footman continued in the same tone, exactly
as if nothing had happened.

“How am I to get in?” asked Alice again, in a louder tone.

“_Are_ you to get in at all?” said the Footman. “That’s the first
question, you know.”

It was, no doubt: only Alice did not like to be told so. “It’s really
dreadful,” she muttered to herself, “the way all the creatures argue.
It’s enough to drive one crazy!”

The Footman seemed to think this a good opportunity for repeating his
remark, with variations. “I shall sit here,” he said, “on and off, for
days and days.”

“But what am _I_ to do?” said Alice.

“Anything you like,” said the Footman, and began whistling.

“Oh, there’s no use in talking to him,” said Alice desperately: “he’s
perfectly idiotic!” And she opened the door and went in.

The door led right into a large kitchen, which was full of smoke from
one end to the other: the Duchess was sitting on a three-legged stool
in the middle, nursing a baby; the cook was leaning over the fire,
stirring a large cauldron which seemed to be full of soup.

“There’s certainly too much pepper in that soup!” Alice said to
herself, as well as she could for sneezing.

There was certainly too much of it in the air. Even the Duchess sneezed
occasionally; and as for the baby, it was sneezing and howling
alternately without a moment’s pause. The only things in the kitchen
that did not sneeze, were the cook, and a large cat which was sitting
on the hearth and grinning from ear to ear.

“Please would you tell me,” said Alice, a little timidly, for she was
not quite sure whether it was good manners for her to speak first, “why
your cat grins like that?”

“It’s a Cheshire cat,” said the Duchess, “and that’s why. Pig!”

She said the last word with such sudden violence that Alice quite
jumped; but she saw in another moment that it was addressed to the
baby, and not to her, so she took courage, and went on again:—

“I didn’t know that Cheshire cats always grinned; in fact, I didn’t
know that cats _could_ grin.”

“They all can,” said the Duchess; “and most of ’em do.”

“I don’t know of any that do,” Alice said very politely, feeling quite
pleased to have got into a conversation.

“You don’t know much,” said the Duchess; “and that’s a fact.”

Alice did not at all like the tone of this remark, and thought it would
be as well to introduce some other subject of conversation. While she
was trying to fix on one, the cook took the cauldron of soup off the
fire, and at once set to work throwing everything within her reach at
the Duchess and the baby—the fire-irons came first; then followed a
shower of saucepans, plates, and dishes. The Duchess took no notice of
them even when they hit her; and the baby was howling so much already,
that it was quite impossible to say whether the blows hurt it or not.

“Oh, _please_ mind what you’re doing!” cried Alice, jumping up and down
in an agony of terror. “Oh, there goes his _precious_ nose!” as an
unusually large saucepan flew close by it, and very nearly carried it
off.

“If everybody minded their own business,” the Duchess said in a hoarse
growl, “the world would go round a deal faster than it does.”

“Which would _not_ be an advantage,” said Alice, who felt very glad to
get an opportunity of showing off a little of her knowledge. “Just
think of what work it would make with the day and night! You see the
earth takes twenty-four hours to turn round on its axis—”

“Talking of axes,” said the Duchess, “chop off her head!”

Alice glanced rather anxiously at the cook, to see if she meant to take
the hint; but the cook was busily stirring the soup, and seemed not to
be listening, so she went on again: “Twenty-four hours, I _think_; or
is it twelve? I—”

“Oh, don’t bother _me_,” said the Duchess; “I never could abide
figures!” And with that she began nursing her child again, singing a
sort of lullaby to it as she did so, and giving it a violent shake at
the end of every line:

“Speak roughly to your little boy,
    And beat him when he sneezes:
He only does it to annoy,
    Because he knows it teases.”


CHORUS.
(In which the cook and the baby joined):


“Wow! wow! wow!”


While the Duchess sang the second verse of the song, she kept tossing
the baby violently up and down, and the poor little thing howled so,
````

## Raw Response
````text
[[FILMCREATOR_PACKET]]

task: character_extraction

version: 1

character_index_markdown:

[[SECTION character_index_markdown]]

* [alice](asset_id: alice)
* [fish_footman](asset_id: fish_footman)
* [frog_footman](asset_id: frog_footman)
* [duchess](asset_id: duchess)
* [cook](asset_id: cook)
* [cheshire_cat](asset_id: cheshire_cat)
* [baby](asset_id: baby)

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
character_type_hint: human girl
morphology_hint: unknown
scale_hint: human-sized
renderability_hint: unknown
confidence: 0.9
direct_identity_evidence: true
direct_visual_evidence: false
costume_or_covering_evidence: false
movement_evidence: false
associated_entities: []
alias_or_role_evidence: ""
unknowns: ""
source_refs: ""

[[SECTION markdown]]
# Alice
**Role:** Protagonist / Observer.
**Status:** Physically present.
Alice is a curious girl who wanders from the woods to a house. She is polite but can be quite talkative and opinionated about scientific facts (like the earth's rotation). She reacts with terror to the chaotic environment of the kitchen.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: fish_footman
canonical_character_id: CH006 Fish-Footman
aliases: The Fish
is_fully_identified: true
manual_description_required: false
manual_description_reason: ""
clarification_required: false
clarification_reason: ""
clarification_question: ""
character_type_hint: humanoid/fish hybrid
morphology_hint: face resembles a fish.
scale_hint: human-sized
renderability_hint: unknown
confidence: 0.8
direct_identity_evidence: true
direct_visual_evidence: true
costume_or_covering_evidence: wearing livery; carries a large letter.
movement_evidence: running out of the wood, bowing low.
associated_entities: [frog_footman]
alias_or_role_evidence: ""
unknowns: ""
source_refs: ""

[[SECTION markdown]]
# Fish-Footman
**Role:** Messenger / House Staff.
**Status:** Physically present.
A footman in livery with a face that looks like a fish. He carries a massive letter nearly as large as himself. He is solemn but somewhat vacuous, staring up at the sky.
[[/SECTION]]
[[/FILM{{/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: frog_footman
canonical_character_id: CH006 Frog-Footman
aliases: The Frog
is_fully_identified: true
manual_description_required: false
manual_description_reason: ""
clarification_required: false
clarification_reason: ""
clarification_question: ""
character_type_hint: humanoid/frog hybrid
morphology_hint: round face, large eyes like a frog.
scale_hint: human-sized
renderability_hint: unknown
confidence: 0.8
direct_identity_evidence: true
direct_visual_evidence: true
costume_or_covering_evidence: wearing livery; powdered hair that curls all over his head.
movement_evidence: bowing low, sitting on the ground staring at the sky.
associated_entities: [fish_footman]
alias_s_role_evidence: ""
unknowns: ""
source_refs: ""

[[SECTION markdown]]
# Frog-Footman
**Role:** Messenger / House Staff.
**Status:** Physically present.
A footman in livery with a round face and large eyes like a frog. He has heavily curled powdered hair. He is solemn but prone to staring stupidly at the sky.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: duchess
canonical_character_id: CH006 Duchess
aliases: 
is_fully_identified: true
manual_description_required: false
manual_description_reason: ""
clarification_required: false
clarification_reason: ""
clarification_question: ""
character_type_hint: human female
morphology_hint: unknown
scale_hint: human-sized
renderability_hint: unknown
confidence: 0.8
direct_identity_evidence: true
direct_visual_evidence: true
costume_or_covering_evidence: sitting on a three-legged stool.
movement_evidence: nursing a baby, being hit by flying dishes.
associated_entities: [baby, cook, cheshire_cat]
alias_or_role_evidence: ""
unknowns: ""
source_refs: ""

[[SECTION markdown]]
# Duchess
**Role:** Resident of the house.
**Status:** Physically present.
A woman sitting on a three-legged stool in a smoky kitchen, nursing a baby. She has a hoarse growl and is somewhat dismissive/rude to Alice. She is remarkably unfazed by flying dishes hitting her.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: cook
canonical_character_id: CH006 Cook
aliases: 
is_fully_identified: true
manual_description_required: false
manual_description_reason: ""
clarification_required: false
clarification_reason: ""
clarification_question: ""
character_type_hint: human female
morphology_hint: unknown
scale_hint: human-sized
renderability_hint: unknown
confidence: 0.8
direct_identity_evidence: true
direct_visual_evidence: true
costume_or_covering_evidence: leaning over the fire, stirring a large cauldron.
movement_evidence: throwing things at the Duchess and baby.
associated_entities: [duchess, baby]
alias_or_role_evidence: ""
unknowns: ""
source_refs: ""

[[SECTION markdown]]
# Cook
**Role:** Kitchen staff.
**Status:** Physically present.
A woman leaning over a fire, stirring a large cauldron of soup. She is busy and somewhat indifferent to the chaos, throwing dishes at the Duchess and baby when necessary.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: cheshire_cat
canonical_character_id: CH006 Cheshire Cat
aliases: 
is_fully_identified: true
manual_description_required: false
manual_description_reason: ""
clarification_required: false
clarification_reason: ""
clarification_question: ""
character_type_hint: feline
morphology_hint: a large cat that grins from ear to ear.
scale_hint: cat-sized
renderability_hint: unknown
confidence: 0.9
direct_identity_evidence: true
direct_visual_evidence: true
costume_or_covering_evidence: sitting on the hearth.
movement_evidence: grinning.
associated_entities: [duchess]
alias_or_role_evidence: ""
unknowns: ""
source_refs: ""

[[SECTION markdown]]
# Cheshire Cat
**Role:** Household pet/entity.
**Status:** Physically present.
A large cat sitting on the hearth, characterized by a constant, wide grin from ear to ear.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: baby
canonical_character_id: CH006 Baby
aliases: 
is_fully_identified: true
manual_description_required: false
manual_description_reason: ""
clarification_required: false
clarification_reason: ""
clarification_question: ""
character_type_hint: infant
morphology_hint: unknown
scale_hint: infant-sized
renderability_hint: unknown
confidence: 0.9
direct_identity_evidence: true
direct_visual_evidence: true
costume_or_covering_evidence: being nursed by the Duchess.
movement_evidence: sneezing, howling, and being tossed violently.
associated_entities: [duchess, cook]
alias_or_role_evidence: ""
unknowns: ""
source_refs: ""

[[SECTION markdown]]
# Baby
**Role:** The Duchess's child.
**Status:** Physically present.
An infant who sneezes and howls constantly due to the pepper in the air. The baby is tossed violently up and down by the Duchess as part of a lullaby/song.
[[/section]]
[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
