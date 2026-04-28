# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-28T00:13:39.197282+00:00
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
- [The Twelve Jurors](#the-twelve-jurors)
- [Gryphon](#gryphon)
- [Bill the Lizard](#bill-the-lizard)
- [The Hatter](#the-hatter)
- [March Hare](#march-hare)
- [Dormouse](#dormouse)

[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: alice
canonical_character_id: CH002 Alice
aliases: Alice
is_fully_identified: true
manual_description_required: false
manual_description_reason:
clarification_required: false
clarification_reason:
clarification_question:
character_type_hint: human
morphology_hint: biped
scale_hint: human_scale
renderability_hint: renderable
confidence: 1.0
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
**Role:** Protagonist / Observer

Alice is a young girl attending the court trial. During the proceedings, she experiences a physical sensation of growing larger in size. She is curious and somewhat opinionated about the proceedings around her.

**Physical Description:** A young girl, currently undergoing a growth spurt where she becomes larger than her surroundings.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: king_of_hearts
canonical_character_id: CH003 King of Hearts
aliases: The King, The Judge
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
confidence: 0.9
direct_identity_evidence: true
direct_visual_evidence: true
costume_or_covering_evidence: true
movement_evidence: false
associated_entities: [queen_of_hearts, white_rabbit]
alias_or_role_evidence: true
unknowns: []
source_refs: []

[[SECTION markdown]]
# King of Hearts
**Role:** Judge / Monarch

The King serves as the judge of the court. He wears a great wig with his crown placed over it, which looks somewhat uncomfortable and unbefitting. He uses spectacles to look at the witnesses and the crowd.

**Physical Description:** A figure wearing a large wig topped with a crown; he also wears spectacles.
[[/SECTION]]
[[end_of_record]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: queen_of_hearts
canonical_character_id: CH004 Queen of Hearts
aliases: The Queen
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
confidence: 0.9
direct_identity_evidence: true
direct_visual_evidence: false
costume_or_covering_evidence: false
movement_evidence: false
associated_entities: [king_of_hearts]
alias_or_role_evidence: true
unknowns: []
source_refs: []

[[SECTION markdown]]
# Queen of Hearts
**Role:** Monarch / Accuser

The Queen is seated on the throne. She wears spectacles and uses them to stare intensely at the witnesses, causing them to fidget.

**Physical Description:** A royal figure who wears spectacles for staring.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: knave_of_hearts
canonical_character_id: CH005 Knave of Hearts
aliases: The Knave
is_fully_identified: true
manual_description_required: true
manual_description_reason: He is only mentioned as being in chains.
clarification_required: false
clarification_reason:
clarification_question:
character_type_hint: humanoid_nonhuman
morphology_hint: biped
scale_hint: human_scale
renderability_hint: renderable
confidence: 0.7
direct_identity_evidence: true
direct_visual_evidence: false
costume_or_covering_end: false
movement_evidence: false
associated_entities: []
alias_or_role_evidence: true
unknowns: []
source_refs: []

[[SECTION markdown]]
# Knave of Hearts
**Role:** The Accused

The Knave is the prisoner in chains, standing before the court as the one accused of stealing the tarts.

**Physical Description:** A figure currently held in chains.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: white_rabbit
canonical_character_id: CH006 White Rabbit
aliases: The White Rabbit, The Herald
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
costume_or_covering_evidence: true
movement_evidence: false
associated_entities: [king_of_hearts]
alias_or_role_evidence: true
unknowns: []
source_refs: []

[[SECTION markdown]]
# White Rabbit
**Role:** Herald / Official

The White Rabbit acts as the herald, carrying a trumpet and a scroll of parchment. He calls for silence and reads out the accusations.

**Physical Description:** A rabbit-like creature carrying a trumpet in one hand and a parchment scroll in the other.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: jury_group
canonical_character_id: CH007 Jury
aliases: The Twelve Jurors, The Jury-men
is_fully_identified: true
manual_description_required: true
manual_description_reason: They are a diverse group of twelve creatures.
clarification_required: false
clarification_reason:
clarification_question:
character_type_hint: group
morphology_hint: unknown
scale_hint: small
renderability_hint: renderable
confidence: 0.8
direct_identity_evidence: true
direct_visual_evidence: true
costume_or_covering_evidence: false
movement_evidence: false
associated_entities: []
alias_or_role_evidence: true
unknowns: []
source_refs: []

[[SECTION markdown]]
# The Twelve Jurors
**Role:** Jury

A group of twelve diverse creatures (some animals, some birds) acting as the jury. They are seen writing on slates.

**Physical Description:** A collection of various small creatures, including birds and animals, all using slates to write.
[[/end_of_section]]
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: gryphon
canonical_character_id: CH008 Gryphon
aliases: The Gryphon
is_fully_identified: true
manual_description_required: true
manual_description_reason: Physical description is not provided in this chapter.
clarification_required: false
clarification_reason:
clarification_question:
character_type_hint: creature
morphology_hint: unknown
scale_hint: human_scale
renderability_hint: renderable
confidence: 0.6
direct_identity_evidence: true
direct_visual_evidence: false
costume_or_covering_evidence: false
movement_evidence: false
associated_entities: [alice]
alias_or_role_evidence: true
unknowns: []
source_refs: []

[[SECTION markdown]]
# Gryphon
**Role:** Witness/Companion to Alice

The Gryphon is present in the court and whispers information to Alice about the jurors.

**Physical Description:** A mythical creature of unknown specific morphology in this context.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: bill_the_lizard
canonical_character_id: CH009 Bill the Lizard
aliases: Bill, The Lizard
is_fully_identified: true
manual_description_required: false
manual_description_reason:
clarification_required: false
clarification_reason:
character_type_hint: animal
morphology_hint: quadruped
scale_hint: tiny
renderability_hint: renderable
confidence: 0.9
direct_identity_evidence: true
direct_visual_evidence: true
coststant_or_covering_evidence: false
movement_evidence: false
associated_entities: []
alias_or_role_evidence: true
unknowns: []
source_refs: []

[[SECTION markdown]]
# Bill the Lizard
**Role:** Juror

One of the twelve jurors, identified as Bill the Lizard. He is a "poor little juror" who loses his pencil.

**Physical Description:** A small lizard-like creature acting as a juror.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: the_hatter
canonical_character_id: CH010 The Hatter
aliases: The Hatter
is_fully_identified: true
manual_description_required: false
manual_description_reason:
clarification_required: false
clarification_reason:
character_type_hint: humanoid_nonhuman
morphology_hint: biped
scale_hint: human_scale
renderability_hint: renderable
confidence: 0.9
direct_identity_evidence: true
direct_visual_evidence: true
costume_or_covering_evidence: true
movement_evidence: true
associated_entities: [march_hare, dormouse]
alias_or_role_evidence: true
unknowns: []
source_refs: []

[[SECTION markdown]]
# The Hatter
**Role:** Witness / Accused-adjacent

The Hatter is a witness in the trial. He carries a teacup and a piece of bread-and-butter. He is nervous, fidgeting and biting his teacup.

**Physical Description:** A man-like figure wearing a hat (which he claims isn't his). He carries a teacup and bread-and-butter.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: march_hare
canonical_character_id: CH011 March Hare
aliases: The March Hare
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
direct_visual_evidence: false
costume_or_covering_evidence: false
movement_evidence: false
associated_entities: [the_hatter, dormouse]
alias_or_role_evidence: true
unknowns: []
source_refs: []

[[SECTION markdown]]
# March Hare
**Role:** Companion to the Hatter

The March Hare follows the Hatter into the court.

**Physical Description:** A hare-like creature.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: dormouse
canonical_character_id: CH012 Dormouse
aliases: The Dormouse
is_fully_identified: true
manual_description_required: false
manual_description_reason:
clarification_required: false
clarification_reason:
character_type_hint: animal
morphology_hint: quadruped
scale_hint: tiny
renderability_hint: renderable
confidence: 0.9
direct_identity_evidence: true
direct_visual_evidence: false
costume_or_covering_evidence: false
movement_evidence: false
associated_entities: [the_hatter, march_hare]
alias_or_role_evidence: true
unknowns: []
source_refs: []

[[SECTION markdown]]
# Dormouse
**Role:** Companion to the Hatter

The Dormouse is a very small creature that follows the Hatter and March Hare. It is squeezed own by Alice.

**Physical Description:** A tiny mouse-like creature.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
