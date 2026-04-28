# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-27T23:58:08.534825+00:00
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

Fallback extraction chunk 1/2 for character_extraction.

Use only the chapter excerpt below for this pass.

# Chapter
CH008

# Title
CHAPTER VIII.

# Text
The Queen’s Croquet-Ground


A large rose-tree stood near the entrance of the garden: the roses
growing on it were white, but there were three gardeners at it, busily
painting them red. Alice thought this a very curious thing, and she
went nearer to watch them, and just as she came up to them she heard
one of them say, “Look out now, Five! Don’t go splashing paint over me
like that!”

“I couldn’t help it,” said Five, in a sulky tone; “Seven jogged my
elbow.”

On which Seven looked up and said, “That’s right, Five! Always lay the
blame on others!”

“_You’d_ better not talk!” said Five. “I heard the Queen say only
yesterday you deserved to be beheaded!”

“What for?” said the one who had spoken first.

“That’s none of _your_ business, Two!” said Seven.

“Yes, it _is_ his business!” said Five, “and I’ll tell him—it was for
bringing the cook tulip-roots instead of onions.”

Seven flung down his brush, and had just begun “Well, of all the unjust
things—” when his eye chanced to fall upon Alice, as she stood watching
them, and he checked himself suddenly: the others looked round also,
and all of them bowed low.

“Would you tell me,” said Alice, a little timidly, “why you are
painting those roses?”

Five and Seven said nothing, but looked at Two. Two began in a low
voice, “Why the fact is, you see, Miss, this here ought to have been a
_red_ rose-tree, and we put a white one in by mistake; and if the Queen
was to find it out, we should all have our heads cut off, you know. So
you see, Miss, we’re doing our best, afore she comes, to—” At this
moment Five, who had been anxiously looking across the garden, called
out “The Queen! The Queen!” and the three gardeners instantly threw
themselves flat upon their faces. There was a sound of many footsteps,
and Alice looked round, eager to see the Queen.

First came ten soldiers carrying clubs; these were all shaped like the
three gardeners, oblong and flat, with their hands and feet at the
corners: next the ten courtiers; these were ornamented all over with
diamonds, and walked two and two, as the soldiers did. After these came
the royal children; there were ten of them, and the little dears came
jumping merrily along hand in hand, in couples: they were all
ornamented with hearts. Next came the guests, mostly Kings and Queens,
and among them Alice recognised the White Rabbit: it was talking in a
hurried nervous manner, smiling at everything that was said, and went
by without noticing her. Then followed the Knave of Hearts, carrying
the King’s crown on a crimson velvet cushion; and, last of all this
grand procession, came THE KING AND QUEEN OF HEARTS.

Alice was rather doubtful whether she ought not to lie down on her face
like the three gardeners, but she could not remember ever having heard
of such a rule at processions; “and besides, what would be the use of a
procession,” thought she, “if people had all to lie down upon their
faces, so that they couldn’t see it?” So she stood still where she was,
and waited.

When the procession came opposite to Alice, they all stopped and looked
at her, and the Queen said severely “Who is this?” She said it to the
Knave of Hearts, who only bowed and smiled in reply.

“Idiot!” said the Queen, tossing her head impatiently; and, turning to
Alice, she went on, “What’s your name, child?”

“My name is Alice, so please your Majesty,” said Alice very politely;
but she added, to herself, “Why, they’re only a pack of cards, after
all. I needn’t be afraid of them!”

“And who are _these?_” said the Queen, pointing to the three gardeners
who were lying round the rose-tree; for, you see, as they were lying on
their faces, and the pattern on their backs was the same as the rest of
the pack, she could not tell whether they were gardeners, or soldiers,
or courtiers, or three of her own children.

“How should _I_ know?” said Alice, surprised at her own courage. “It’s
no business of _mine_.”

The Queen turned crimson with fury, and, after glaring at her for a
moment like a wild beast, screamed “Off with her head! Off—”

“Nonsense!” said Alice, very loudly and decidedly, and the Queen was
silent.

The King laid his hand upon her arm, and timidly said “Consider, my
dear: she is only a child!”

The Queen turned angrily away from him, and said to the Knave “Turn
them over!”

The Knave did so, very carefully, with one foot.

“Get up!” said the Queen, in a shrill, loud voice, and the three
gardeners instantly jumped up, and began bowing to the King, the Queen,
the royal children, and everybody else.

“Leave off that!” screamed the Queen. “You make me giddy.” And then,
turning to the rose-tree, she went on, “What _have_ you been doing
here?”

“May it please your Majesty,” said Two, in a very humble tone, going
down on one knee as he spoke, “we were trying—”

“_I_ see!” said the Queen, who had meanwhile been examining the roses.
“Off with their heads!” and the procession moved on, three of the
soldiers remaining behind to execute the unfortunate gardeners, who ran
to Alice for protection.

“You shan’t be beheaded!” said Alice, and she put them into a large
flower-pot that stood near. The three soldiers wandered about for a
minute or two, looking for them, and then quietly marched off after the
others.

“Are their heads off?” shouted the Queen.

“Their heads are gone, if it please your Majesty!” the soldiers shouted
in reply.

“That’s right!” shouted the Queen. “Can you play croquet?”

The soldiers were silent, and looked at Alice, as the question was
evidently meant for her.

“Yes!” shouted Alice.

“Come on, then!” roared the Queen, and Alice joined the procession,
wondering very much what would happen next.

“It’s—it’s a very fine day!” said a timid voice at her side. She was
walking by the White Rabbit, who was peeping anxiously into her face.

“Very,” said Alice: “—where’s the Duchess?”

“Hush! Hush!” said the Rabbit in a low, hurried tone. He looked
anxiously over his shoulder as he spoke, and then raised himself upon
tiptoe, put his mouth close to her ear, and whispered “She’s under
sentence of execution.”

“What for?” said Alice.

“Did you say ‘What a pity!’?” the Rabbit asked.

“No, I didn’t,” said Alice: “I don’t think it’s at all a pity. I said
‘What for?’”
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
- [Two](#two)
- [Five](#five)
- [Seven](#seven)
- [White Rabbit](#white-rabbit)
- [Knave of Hearts](#knave-of-hearts)
- [Queen of Hearts](#queen-of-hearts)
- [King of Hearts](#king-of-hearts)
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
morphology_hint: biped
scale_hint: human_scale
renderability_hint: renderable
confidence: 1.0
direct_identity_evidence: true
direct_visual_evidence: true
costume_or_covering_evidence: false
movement_evidence: false
associated_entities: 
alias_or_role_evidence: false
unknowns: 
source_refs: 
[[SECTION markdown]]
# Alice
**Role:** Protagonist / Observer

**Physical Presence:** Physically present throughout the chapter.

**Description:** A young girl, described as a "child" by the King. She is brave and outspoken, standing her ground against the Queen.

**Notes:** In this scene, she interacts with the gardeners and the royal procession.
[[/SECTION]]
[[/FILEO_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: two
canonical_character_id: CH002 Two
aliases: Two
is_fully_identified: true
manual_description_required: true
manual_description_reason: The text implies he is a playing card, but his physical form as a "gardener" needs specific visual translation.
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
movement_evidence: true
associated_entities: Five, Seven
alias_or_role_evidence: true
unknowns: 
source_refs: 
[[SECTION markdown]]
# Two
**Role:** Gardener / Playing Card

**Physical Presence:** Physically present.

**Description:** One of the three gardeners painting roses. He is a playing card (Two) given human-like agency to paint and kneel.

**Notes:** He acts as a spokesperson for the gardeners, explaining their mistake with the white rose-tree.
[[ted_SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: five
canonical_character_id: CH003 Five
aliases: Five
is_fully_identified: true
manual_description_required: true
manual_description_reason: Physical description is tied to being a card-gardener.
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
movement_evidence: true
associated_entities: Two, Seven
alias_or_role_evidence: true
unknowns: 
source_refs: 
[[SECTION markdown]]
# Five
**Role:** Gardener / Playing Card

**Physical Presence:** Physically present.

**Description:** One of the three gardeners painting roses. He is a playing card (Five) with a sulky tone.

**Notes:** He is prone to blaming others and is wary of the Queen's arrival.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: seven
canonical_character_id: CH004 Seven
aliases: Seven
is_fully_identified: true
manual_description_required: true
manual_description_reason: Physical description is tied to being a card-gardener.
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
movement_evidence: true
associated_entities: Two, Five
alias_or_role_evidence: true
unknowns: 
source_refs: 
[[SECTION markdown]]
# Seven
**Role:** Gardener / Playing Card

**Physical Presence:** Physically present.

**Description:** One of the three gardeners painting roses. He is a playing card (Seven) who argues with Five.

**Notes:** He is described as being blamed by Five and eventually bows to the procession.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: white_rabbit
canonical_character_id: CH005 White Rabbit
aliases: The White Rabbit
is_fully_identified: true
manual_description_required: false
manual_description_reason: 
clarification_required: false
clarification_reason: 
clarification_question: 
character_type_hint: animal
morphology_hint: quadruped
scale_hint: small
renderability_hint: renderable
confidence: 0.9
direct_identity_evidence: true
direct_visual_evidence: true
costume_or_covering_evidence: false
movement_evidence: true
associated_entities: Alice
alias_or_role_evidence: true
unknowns: 
source_refs: 
[[SECTION markdown]]
# White Rabbit
**Role:** Guest / Messenger

**Physical Presence:** Physically present.

**Description:** A rabbit who walks among the guests in a hurried, nervous manner. He is smiling but anxious.

**Notes:** He interacts with Alice at the end of the chapter, whispering secrets about the Duchess.
[[/SECTION]]
[[/FILMcreator_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: knave_of_hearts
canonical_character_id: CH006 Knave of Hearts
aliases: The Knave
is_fully_identified: true
manual_description_required: true
manual_description_reason: He is a card-person; visual identity depends on the "Knave" suit.
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
movement_evidence: true
associated_entities: Queen of Hearts, King of Hearts
alias_or_role_evidence: true
unknowns: 
source_refs: 
[[SECTION markdown]]
# Knave of Hearts
**Role:** Courtier / Crown-bearer

**Physical Presence:** Physically present.

**Description:** A member of the royal procession carrying the King's crown on a crimson velvet cushion. He is described as an "idiot" by the Queen.

**Notes:** He bows and smiles to the Queen when questioned about Alice.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: queen_of_hearts
canonical_character_id: CH007 Queen of Hearts
aliases: The Queen
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
coststant_or_covering_evidence: true
movement_evidence: true
associated_entities: King of Hearts, Knave of Hearts
alias_or_role_evidence: true
unknowns: 
source_refs: 
[[SECTION markdown]]
# Queen of Hearts
**Role:** Ruler / Antagonist

**Physical Presence:** Physically present.

**Description:** A commanding and temperamental figure. She is prone to fits of fury, turning "crimson" when angry.

**Notes:** She commands the execution of gardeners and threatens Alice. Her authority is absolute within the procession.
[[/SECTION]]
[[/FILMCREator_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: king_of_hearts
canonical_character_id: CH008 King of Hearts
aliases: The King
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
associated_entities: Queen of Hearts, Knave of Hearts
alias_or_role_evidence: true
unknowns: 
source_refs: 
[[SECTION markdown]]
# King of Hearts
**Role:** Ruler

**Physical Presence:** Physically present.

**Description:** A more timid figure compared to the Queen, acting as a moderating influence on her temper.

**Notes:** He attempts to defend Alice's presence by calling her "only a child."
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
