# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-27T23:46:51.222388+00:00
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

# Character Index
- [alice](#alice)
- [fish_footman](#fish_footman)
- [frog_footman](#frog_footman)
- [duchess](#duchess)
- [cook](#cook)
- [baby](#baby)
- [cheshire_cat](#cheshire_cat)

[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: alice
canonical_character_id: CH001 Alice
aliases: Alice
is_fully_identified: true
manual_description_required: false
manual_description_reason: 
clarification_required: false
clarification_reason: 
clarification_question: 
character_type_hint: human
morphology_hint: bitoe
scale_hint: human_scale
renderability_hint: renderable
confidence: 0.9
direct_identity_evidence: true
direct_visual_evidence: false
costume_or_covering_evidence: false
movement_evidence: false
associated_entities: []
alias_or_role_evidence: false
unknowns: []
source_refs: []

[[SECTION markdown]]
# Alice
**Role:** Protagonist / Observer.
- **Physical Description:** A young girl, curious and polite but easily startled. 
- **Notes:** She is the primary perspective character in this chapter.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: fish_footman
canonical_character_id: CH006 Fish-Footman
aliases: The Fish-Footman, Footman
is_fully_identified: true
manual_description_required: false
manual_description_reason: 
clarification_required: false
clarification_reason: 
clarification_question: 
character_type_hint: humanoid_nonhuman
morphology_hint: biped
scale_hint: human_scale
renderability_hint: renderable
confidence: 0.8
direct_identity_evidence: true
direct_visual_evidence: true
costume_or_covering_evidence: true
movement_evidence: false
associated_entities: [frog_footman]
alias_or_role_evidence: true
unknowns: []
source_refs: []

[[SECTION markdown]]
# Fish-Footman
**Role:** Messenger / House Servant.
- **Physical Description:** A man whose face resembles a fish; wears formal livery and has hair that is powdered and curled all over his head.
- **Notes:** He carries a large letter nearly as big as himself.
[[/SECTION]]
[[/FILcit_footman]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: frog_footman
canonical_character_id: CH006 Frog-Footman
aliases: The Frog-Footman, Footman
is_fully_identified: true
manual_description_required: false
manual_description_reason: 
clarification_required: false
clarification_reason: 
clarification_question: 
character_type_hint: humanoid_nonhuman
morphology_hint: biped
scale_hint: human_scale
renderability_hint: renderable
confidence: 0.8
direct_identity_evidence: true
direct_visual_evidence: true
costume_or_covering_evidence: true
movement_evidence: false
associated_entities: [fish_footman]
alias_or_role_evidence: true
unknowns: []
source_refs: []

[[SECTION markdown]]
# Frog-Footman
**Role:** Messenger / House Servant.
- **Physical Description:** A man with a round face and large eyes like a frog; wears formal livery and has hair that is powdered and curled all over his head.
- **Notes:** He sits on the ground near the door, staring up at the sky.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: duchess
canonical_character_id: CH006 Duchess
aliases: The Duchess
is_fully_identified: true
manual_description_required: false
manual_description_reason: 
clarification_required: false
clarification_reason: 
character_type_hint: human
morphology_hint: biped
scale_hint: human_scale
renderability_hint: renderable
confidence: 0.7
direct_identity_evidence: true
direct_visual_evidence: false
costume_or_covering_evidence: false
movement_evidence: false
associated_entities: [baby, cook, cheshire_cat]
alias_or_role_evidence: true
unknowns: []
source_refs: []

[[SECTION markdown]]
# Duchess
**Role:** Resident of the house.
- **Physical Description:** A woman sitting on a three-legged stool in a smoky kitchen. 
- **Notes:** She has a hoarse growl and is somewhat dismissive/rude to Alice.
[[/end_section]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: cook
canonical_character_id: CH006 Cook
aliases: The Cook
is_fully_identified: true
manual_description_required: false
manual_description_reason: 
clarification_required: false
clarification_reason: 
character_type_hint: human
morphology_hint: biped
scale_hint: human_scale
renderability_hint: renderable
confidence: 0.7
direct_identity_evidence: true
direct_visual_evidence: false
costume_or_covering_evidence: false
movement_evidence: false
associated_entities: [duchess, baby]
alias_or_role_evidence: true
unknowns: []
source_refs: []

[[SECTION markdown]]
# Cook
**Role:** Kitchen worker.
- **Physical Description:** A woman leaning over a fire, stirring a large cauldron of soup.
- **Notes:** She is busy and somewhat indifferent to the Duchess's commands or Alice's presence.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: baby
canonical_character_id: CH006 Baby
aliases: The Baby, Little Boy
is_fully_identified: true
manual_description_required: false
manual_description_reason: 
clarification_required: false
clarification_reason: 
character_type_hint: human
morphology_hint: biped
scale_hint: tiny
renderability_hint: renderable
confidence: 0.7
direct_identity_evidence: true
direct_visual_evidence: false
costume_or_covering_evidence: false
movement_evidence: false
associated_entities: [duchess, cook]
alias_or_role_evidence: true
unknowns: []
source_refs: []

[[SECTION markdown]]
# Baby
**Role:** The Duchess's child.
- **Physical Description:** A small infant/baby.
- **Notes:** Constantly sneezing and howling; is tossed violently by the Duchess during her song.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: cheshire_cat
canonical_character_id: CH006 Cheshire Cat
aliases: The Cheshire Cat, Cat
is_fully_identified: true
manual_description_required: false
manual_description_reason: 
clarification_required: false
clarification_reason: 
character_type_hint: animal
morphology_hint: quadruped
scale_hint: small
renderability_hint: renderable
confidence: 0.9
direct_identity_evidence: true
direct_visual_evidence: true
costume_or_covering_evidence: false
movement_evidence: false
associated_entities: []
alias_or_role_evidence: true
unknowns: []
source_refs: []

[[SECTION markdown]]
# Cheshire Cat
**Role:** Resident of the house.
- **Physical Description:** A large cat sitting on the hearth, grinning from ear to ear.
- **Notes:** Known for its constant grin.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
