# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-28T00:00:08.863285+00:00
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

* [alice](#alice)
* [two](#two)
* [five](#five)
* [seven](#seven)
* [white_rabbit](#white_rabbit)
* [knave_of_hearts](#knave_of_hearts)
* [queen_of_hearts](#queen_of_hearts)
* [king_of_hearts](#king_of_hearts)

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
character_type_hint: human child
morphology_hint: human
scale_hint: human-sized
renderability_hint: high
confidence: 0.9
direct_identity_evidence: "She identifies herself as Alice."
direct_visual_evidence: "Standing watching gardeners; later joins the procession."
costume_or_covering_evidence: ""
movement_evidence: "Stands still, then walks with the procession."
associated_entities: ["two", "five", "seven", "white_rabbit", "queen_of_hearts", "king_of_hearts", "knave_of_hearts"]
alias_or_role_evidence: ""
unknowns: ""
source_refs: ""

[[SECTION markdown]]
# Alice
**Role:** Protagonist / Observer.
- **Presence:** Physically present throughout the chapter.
- **Description:** A young girl, described as a "child" by the King. She is brave and outspoken, even challenging the Queen.
- **Traits:** Polite but courageous; views the royals as merely a "pack ofs cards."
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: two
canonical_character_id: CH002 Two (Gardener)
aliases: Two
is_fully_identified: true
manual_description_required: false
manual_description_reason: ""
clarification_required: false
clarification_reason: ""
clarification_question: ""
character_type_hint: playing card / gardener
morphology_hint: flat, oblong-shaped (card-like)
scale_hint: human-sized when standing/kneeling
renderability_hint: high
confidence: 0.8
direct_identity_evidence: "Identified by name in dialogue."
direct_visual_evidence: "A gardener painting roses; kneels before the Queen."
costume_or_covering_evidence: "Part of a group of three gardeners/soldiers with card-like patterns on their backs."
movement_evidence: "Kneels humbly before the Queen."
associated_entities: ["five", "seven", "queen_ofs_hearts"]
alias_or_role_evidence: "One of the three gardeners."
unknowns: ""
source_refs: ""

[[SECTION markdown]]
# Two
**Role:** Gardener / Card.
- **Presence:** Physically present.
- **Description:** A gardener who is also a playing card. He is humble and somewhat fearful of the Queen.
- **Traits:** Explains the mistake with the rose-tree; kneels to show respect/submission.
[[/SECTION]]
[[/FIL_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: five
canonical_character_id: CH003 Five (Gardener)
aliases: Five
is_fully_identified: true
manual_description_required: false
manual_description_reason: ""
clarification_required: false
clarification_reason: ""
clarification_question: ""
character_type_hint: playing card / gardener
morphology_hint: flat, oblong-shaped (card-like)
scale_hint: human-sized when standing
renderability_hint: high
confidence: 0.8
direct_identity_evidence: "Identified by name in dialogue."
direct_visual_evidence: "One of the three gardeners painting roses; looks anxiously across the garden."
costume_or_covering_evidence: "Part of a group of three gardeners/soldiers with card-e-like patterns on their backs."
movement_evidence: "Looks anxiously; jumps up when ordered by the Queen."
associated_entities: ["two", "seven", "queen_of_hearts"]
alias_or_role_evidence: "One of the three gardeners."
unknowns: ""
source_refs: ""

[[SECTION markdown]]
# Five
**Role:** Gardener / Card.
- **Presence:** Physically present.
- **Description:** A gardener/card who is sulky and prone to blaming others.
- **Traits:** Anxious; watches the Queen's approach with concern.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: seven
canonical_character_id: CH004 Seven (Gardener)
aliases: Seven
is_fully_identified: true
manual_description_required: false
manual_description_reason: ""
clarification_required: false
clarification_reason: ""
clarification_question: ""
character_type_hint: playing card / gardener
morphology_hint: flat, oblong-shaped (card-like)
scale_hint: human-sized when standing
renderability_hint: high
confidence: 0.8
direct_identity_evidence: "Identsified by name in dialogue."
direct_visual_evidence: "One of the three gardeners painting roses; flings down his brush."
costume_or_covering_evidence: "Part of a group of three gardeners/soldiers with card-like patterns on their backs."
movement_evidence: "Flings down his brush when argued with."
associated_entities: ["two", "five", "queen_of_hearts"]
alias_or_role_evidence: "One of the three gardeners."
unknowns: ""
source_refs: ""

[[SECTION markdown]]
# Seven
**Role:** Gardener / Card.
- **Presence:** Physically present.
- **Description:** A gardener/card who is argumentative with Five and Seven.
- **Traits:** Defends himself against blame; flings his brush down in frustration.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: white_rabbit
canonical_character_id: CH005 White Rabbit
aliases: The White Rabbit
is_fully_identified: true
manual_description_required: false
manual_description_reason: ""
clarification_required: false
clarification_reason: ""
clarification_question: ""
character_type_hint: animal-humanoid hybrid / card
morphology_hint: rabbit features.
scale_hint: human-sized (walking in procession).
renderability_hint: high
confidence: 0.9
direct_identity_evidence: "Alice recognizes him as the White Rabbit."
direct_visual_evidence: "Walking in the procession; peeping anxiously into Alice's face."
costume_or_covering_evidence: ""
movement_evidence: "Walks in a hurried, nervous manner; raises himself on tiptoe to whisper."
associated_entities: ["alice"]
alias_or_role_evidence: "A guest in the procession."
unknowns: ""
source_refs: ""

[[SECTION markdown]]
# White Rabbit
**Role:** Guest / Messenger.
- **Presence:** Physically present.
- **Description:** A nervous, hurried figure who is part of the royal procession.
- **Traits:** Anxious; speaks in a low, hurried tone; acts as an informant to Alice.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: knave_of_hearts
canonical_character_id: CH006 Knave of Hearts
aliases: The Knave
is_fully_identified: true
manual_description_required: false
manual_description_reason: ""
clarification_required: false
clarification_reason: ""
clarification_question: ""
character_type_hint: playing card / courtier
morphology_hint: human-sized.
scale_hint: human-sized.
renderability_hint: high
confidence: 0.8
direct_identity_evidence: "Identified as the Knave of Hearts."
direct_visual_evidence: "Carrying the King's crown on a crimson velvet cushion; bows and smiles to the Queen."
costume_or_covering_evedince: ""
movement_evidence: "Carries the crown; bows with one foot used to turn over the gardeners."
associated_entities: ["queen_of_hearts", "king_of_hearts"]
alias_or_role_evidence: "Carrying the King's crown."
unknowns: ""
source_refs: ""

[[SECTION markdown]]
# Knave of Hearts
**Role:** Crown-bearer / Courtier.
- **Presence:** Physically present.
- **Description:** A member of the court carrying the royal crown.
- **Traits:** Obedient to the Queen; bows and smiles in response to her questioning.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: queen_of_hearts
canonical_character_id: CH007 Queen of Hearts
aliases: The Queen
is_fully_identified: true
manual_description_required: false
manual_description_reason: ""
clarification_required: false
clarification_reason: ""
clarification_question: ""
character_type_hint: royal / card
morphology_hint: human-sized.
scale_hint: human-sized.
renderability_hint: high
confidence: 0.9
direct_identity_evidence: "Identified as the Queen of Hearts."
direct_visual_evidence: "Leading a grand procession; pointing at gardeners; turning crimson with fury."
costume_or_covering_evidence: ""
movement_evidence: "Tosses her head impatiently; screams; examines roses."
associated_entities: ["king_of_s_hearts", "knave_of_hearts", "alice"]
alias_or_role_evidence: "The sovereign of the procession."
unknowns: ""
source_refs: ""

[[SECTION markdown]]
# Queen of Hearts
**Role:** Sovereign / Antagonist.
- **Presence:** Physically present.
- **Description:** A powerful, temperamental royal figure.
- **Traits:** Impatient, furious, and prone to shouting "Off with her head!" She is authoritative and easily offended.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: king_of_hearts
canonical_character_id: CH008 King of Hearts
aliases: The King
is_fully_identified: true
manual_description_required: false
manual_description_reason: ""
clarification_required: false
clarification_reason: ""
clarification_question: ""
character_type_hint: royal / card
morphology_hint: human-sized.
scale_hint: human-sized.
renderability_hint: high
confidence: 0.9
direct_identity_evidence: "Identified as the King of Hearts."
direct_visual_evidence: "Walking in the procession; laying a hand on the Queen's arm."
costume_or_covering_evidence: ""
movement_evidence: "Walks in the procession; acts timidly toward the Queen."
associated_entities: ["queen_of_hearts", "knave_of_hearts"]
alias_or_role_evidence: "The King."
unknowns: ""
source_refs: ""

[[SECTION markdown]]
# King of Hearts
**Role:** Sovereign.
- **Presence:** Physically present.
- **Description:** A member of the royal couple, appearing more gentle than the Queen.
- **Traits:** Timid toward the Queen; attempts to moderate her temper regarding Alice.
[[/end_section]]
[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
