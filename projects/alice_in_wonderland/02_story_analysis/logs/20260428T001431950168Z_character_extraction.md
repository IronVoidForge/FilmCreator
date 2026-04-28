# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-28T00:14:31.950168+00:00
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

Fallback extraction chunk 1/2 for character_extraction.

Use only the chapter excerpt below for this pass.

# Chapter
CH011

# Title
CHAPTER XI.

# Text
Who Stole the Tarts?


The King and Queen of Hearts were seated on their throne when they
arrived, with a great crowd assembled about them—all sorts of little
birds and beasts, as well as the whole pack of cards: the Knave was
standing before them, in chains, with a soldier on each side to guard
him; and near the King was the White Rabbit, with a trumpet in one
hand, and a scroll of parchment in the other. In the very middle of the
court was a table, with a large dish of tarts upon it: they looked so
good, that it made Alice quite hungry to look at them—“I wish they’d
get the trial done,” she thought, “and hand round the refreshments!”
But there seemed to be no chance of this, so she began looking at
everything about her, to pass away the time.

Alice had never been in a court of justice before, but she had read
about them in books, and she was quite pleased to find that she knew
the name of nearly everything there. “That’s the judge,” she said to
herself, “because of his great wig.”

The judge, by the way, was the King; and as he wore his crown over the
wig, (look at the frontispiece if you want to see how he did it,) he
did not look at all comfortable, and it was certainly not becoming.

“And that’s the jury-box,” thought Alice, “and those twelve creatures,”
(she was obliged to say “creatures,” you see, because some of them were
animals, and some were birds,) “I suppose they are the jurors.” She
said this last word two or three times over to herself, being rather
proud of it: for she thought, and rightly too, that very few little
girls of her age knew the meaning of it at all. However, “jury-men”
would have done just as well.

The twelve jurors were all writing very busily on slates. “What are
they doing?” Alice whispered to the Gryphon. “They can’t have anything
to put down yet, before the trial’s begun.”

“They’re putting down their names,” the Gryphon whispered in reply,
“for fear they should forget them before the end of the trial.”

“Stupid things!” Alice began in a loud, indignant voice, but she
stopped hastily, for the White Rabbit cried out, “Silence in the
court!” and the King put on his spectacles and looked anxiously round,
to make out who was talking.

Alice could see, as well as if she were looking over their shoulders,
that all the jurors were writing down “stupid things!” on their slates,
and she could even make out that one of them didn’t know how to spell
“stupid,” and that he had to ask his neighbour to tell him. “A nice
muddle their slates’ll be in before the trial’s over!” thought Alice.

One of the jurors had a pencil that squeaked. This of course, Alice
could _not_ stand, and she went round the court and got behind him, and
very soon found an opportunity of taking it away. She did it so quickly
that the poor little juror (it was Bill, the Lizard) could not make out
at all what had become of it; so, after hunting all about for it, he
was obliged to write with one finger for the rest of the day; and this
was of very little use, as it left no mark on the slate.

“Herald, read the accusation!” said the King.

On this the White Rabbit blew three blasts on the trumpet, and then
unrolled the parchment scroll, and read as follows:—

“The Queen of Hearts, she made some tarts,
    All on a summer day:
The Knave of Hearts, he stole those tarts,
    And took them quite away!”


“Consider your verdict,” the King said to the jury.

“Not yet, not yet!” the Rabbit hastily interrupted. “There’s a great
deal to come before that!”

“Call the first witness,” said the King; and the White Rabbit blew
three blasts on the trumpet, and called out, “First witness!”

The first witness was the Hatter. He came in with a teacup in one hand
and a piece of bread-and-butter in the other. “I beg pardon, your
Majesty,” he began, “for bringing these in: but I hadn’t quite finished
my tea when I was sent for.”

“You ought to have finished,” said the King. “When did you begin?”

The Hatter looked at the March Hare, who had followed him into the
court, arm-in-arm with the Dormouse. “Fourteenth of March, I _think_ it
was,” he said.

“Fifteenth,” said the March Hare.

“Sixteenth,” added the Dormouse.

“Write that down,” the King said to the jury, and the jury eagerly
wrote down all three dates on their slates, and then added them up, and
reduced the answer to shillings and pence.

“Take off your hat,” the King said to the Hatter.

“It isn’t mine,” said the Hatter.

“_Stolen!_” the King exclaimed, turning to the jury, who instantly made
a memorandum of the fact.

“I keep them to sell,” the Hatter added as an explanation; “I’ve none
of my own. I’m a hatter.”

Here the Queen put on her spectacles, and began staring at the Hatter,
who turned pale and fidgeted.

“Give your evidence,” said the King; “and don’t be nervous, or I’ll
have you executed on the spot.”

This did not seem to encourage the witness at all: he kept shifting
from one foot to the other, looking uneasily at the Queen, and in his
confusion he bit a large piece out of his teacup instead of the
bread-and-butter.

Just at this moment Alice felt a very curious sensation, which puzzled
her a good deal until she made out what it was: she was beginning to
grow larger again, and she thought at first she would get up and leave
the court; but on second thoughts she decided to remain where she was
as long as there was room for her.

“I wish you wouldn’t squeeze so,” said the Dormouse, who was sitting
next to her. “I can hardly breathe.”

“I can’t help it,” said Alice very meekly: “I’m growing.”
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
- [King of Hearts](#king-of-hearts)
- [Queen of Hearts](#queen-of-hearts)
- [Knave of Hearts](#knave-of-hearts)
- [White Rabbit](#white-rabbit)
- [The Gryphon](#the-grypon)
- [Bill the Lizard](#bill-the-lizard)
- [The Hatter](#the-hatter)
- [March Hare](#march-hare)
- [Dormouse](#dormouse)

[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: alice
canonical_character_id: CH002 Alice
aliases: 
is_fully_identified: true
manual_description_required: false
manual_description_reason: 
clarification_required: false
clarification_reason: 
clarification_question: 
character_type_hint: human girl
morphology_hint: growing larger in size during the scene.
scale_hint: small/human scale (variable)
renderability_hint: high
confidence: 0.9
direct_identity_evidence: true
direct_visual_evidence: true
costume_or_covering_evidence: false
movement_evidence: false
associated_entities: The Gryphon, The King, The Queen, The White Rabbit, The Hatter, The March Hare, The Dormouse
alias_or_role_evidence: false
unknowns: 
source_refs: CH011
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: king_of_hearts
canonical_character_id: CH003 King of Hearts
aliases: The Judge
is_fully_identified: true
manual_description_required: false
manual_description_reason: 
clarification_required: false
clarification_reason: 
clarification_question: 
character_type_hint: king/judge
morphology_hint: wears a great wig with a crown on top.
scale_hint: human scale
renderability_hint: high
confidence: 0.8
direct_identity_evidence: true
direct_visual_evidence: true
costume_or_covering_evidence: wearing a large wig and a crown; wears spectacles.
movement_evidence: false
associated_entities: Queen of Hearts, White Rabbit, Knave ofs Hearts
alias_or_role_evidence: true
unknowns: 
source_refs: CH011
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: queen_of_hearts
canonical_character_id: CH004 Queen of Hearts
aliases: 
is_fully_identified: true
manual_description_required: false
manual_description_reason: 
clarification_required: false
clarification_reason: 
clarification_question: 
character_type_hint: queen
morphology_hint: 
scale_hint: human scale
renderability_hint: high
confidence: 0.8
direct_identity_evidence: true
direct_visual_evidence: true
costume_or_covering_evidence: wears spectacles to stare at the Hatter.
movement_evidence: false
associated_entities: King of Hearts, Knave of Hearts, The Hatter
alias_or_role_evidence: false
unknowns: 
source_refs: CH011
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: knave_of_hearts
canonical_character_id: CH005 Knave of Hearts
aliases: The Knave
is_fully_identified: true
manual_description_required: false
manual_description_reason: 
clarification_required: false
clarification_reason: 
clarification_question: 
character_type_hint: card soldier/prisoner
morphology_hint: in chains.
scale_hint: human scale
renderability_hint: high
confidence: 0.7
direct_identity_evidence: true
direct_visual_evidence: true
costume_or_covering_evidence: wearing chains.
movement_evidence: false
associated_entities: King of Hearts, Queen of Hearts
alias_or_role_evidence: true
unknowns: 
source_refs: CH011
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: white_rabbit
canonical_character_id: CH006 White Rabbit
aliases: Herald
is_fully_identified: true
manual_description_required: false
manual_description_reason: 
clarification_required: false
clarification_reason: 
character_type_hint: rabbit/herald
morphology_hint: 
scale_hint: small animal scale
renderability_hint: high
confidence: 0.9
direct_identity_evidence: true
direct_visual_evidence: true
costume_or_covering_evidence: carries a trumpet and a scroll of parchment.
movement_evidence: false
associated_entities: King of Hearts, The Knave
alias_or_role_evidence: true
unknowns: 
source_refs: CH011
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: gryphon
canonical_character_id: CH007 Gryphon
aliases: 
is_fully_identified: true
manual_description_required: false
manual_description_reason: 
clarification_required: false
clarification_reason: 
character_type_hint: mythical creature
morphology_hint: 
scale_hint: large/animal scale
renderability_hint: high
confidence: 0.7
direct_identity_evidence: true
direct_visual_evidence: false
costume_or_covering_evidence: false
movement_evidence: false
associated_entities: Alice
alias_or_role_evidence: false
unknowns: 
source_refs: CH011
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: bill_the_lizard
canonical_character_id: CH008 Bill the Lizard
aliases: one of the jurors / Bill
is_fully_identified: true
manual_description_required: false
manual_description_reason: 
clarification_required: false
clarification_reason: 
character_type_hint: lizard/juror
morphology_hint: a "poor little juror".
scale_hint: small animal scale
renderability_hint: high
confidence: 0.8
direct_identity_evidence: true
direct_visual_evidence: false
costume_or_covering_evidence: false
movement_evidence: false
associated_entities: Alice, the jury
alias_or_role_evidence: true
unknowns: 
source_refs: CH011
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: the_hatter
canonical_character_id: CH009 The Hatter
aliases: The witness
is_fully_identifed: true
manual_description_required: false
manual_description_reason: 
clarification_required: false
clarification_reason: 
character_type_hint: human/hatter
morphology_hint: carries a teacup and bread-and-butter; wears a hat.
scale_hint: human scale
renderability_hint: high
confidence: 0.8
direct_identity_evidence: true
direct_visual_evidence: true
costume_or_covering_evidence: wearing a hat.
movement_evidence: shifting from one foot to the other, biting teacup.
associated_entities: King of Hearts, Queen of Hearts, March Hare, Dormouse
alias_or_role_evidence: true
unknowns: 
source_refs: CH011
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: march_hare
canonical_character_id: CH010 March Hare
aliases: 
is_fully_identified: true
manual_description_required: false
manual_description_reason: 
clarification_required: false
clarification_reason: 
character_type_hint: hare/juror-adjacent
morphology_hint: 
scale_hint: small animal scale
renderability_hint: high
confidence: 0.7
direct_identity_evidence: true
direct_visual_evidence: false
costume_or_covering_evidence: false
movement_evidence: follows the Hatter arm-in-arm with the Dormouse.
associated_entities: The Hatter, Dormouse
alias_or_role_evidence: false
unknowns: 
source_refs: CH011
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: dormouse
canonical_character_id: CH011 Dormouse
aliases: 
is_fully_identified: true
manual_description_required: false
manualdescription_reason: 
clarification_required: false
clarification_reason: 
character_type_hint: mouse/juror-adjacent
morphology_hint: 
scale_hint: very small animal scale
renderability_hint: high
confidence: 0.7
direct_identity_evidence: true
direct_visual_evidence: false
costume_or_covering_evidence: false
movement_evidence: sitting next to Alice.
associated_entities: The Hatter, March Hare, Alice
alias_or_role_evidence: false
unknowns: 
source_refs: CH011
[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
