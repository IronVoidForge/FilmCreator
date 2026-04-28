# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-28T03:16:34.766529+00:00
- task: character_extraction

## System Prompt
````text
You are FilmCreator's chapter analysis engine.
Return only FilmCreator packets with the requested sections and records.
Do not wrap the packet in code fences unless explicitly requested.
Do not produce JSON-only responses.
If a packet asks for markdown sections, emit the section name on its own line and wrap the body in [[SECTION ...]] ... [[/SECTION]].
Do not put another [[SECTION ...]] tag inside a section body.
Copy every FILMCREATOR structural tag literally.
Do not rename, translate, partially rewrite, or decorate any PACKET, RECORD, or SECTION tag.
The only valid closing tags are [[/FILMCREATOR_PACKET]], [[/FILMCREATOR_RECORD]], and [[/SECTION]].
Keep the response deterministic and grounded in the supplied chapter text.
````

## User Prompt
````text
Project slug: alice_in_wonderland

Chapter id: CH002

Task: extract visible and referenced characters into a character index plus one Markdown file per character.

Packet contract:
- task: character_extraction
- version: 1
- first line: [[FILMCREATOR_PACKET]]
- last line: [[/FILMCREATOR_PACKET]]
- required sections: character_index_markdown
- record type character: fields=asset_id, canonical_character_id, aliases, is_fully_identified, manual_description_required, manual_description_reason, clarification_required, clarification_reason, clarification_question, character_type_hint, morphology_hint, scale_hint, renderability_hint, confidence, direct_identity_evidence, direct_visual_evidence, costume_or_covering_evidence, movement_evidence, associated_entities, alias_or_role_evidence, unknowns, source_refs sections=markdown



Literal tag rules:

- begin with [[FILMCREATOR_PACKET]] on its own line

- end with [[/FILMCREATOR_PACKET]] on its own line

- wrap each character item in [[FILMCREATOR_RECORD]] ... [[/FILMCREATOR_RECORD]]

- use [[SECTION character_index_markdown]] and [[SECTION markdown]] exactly as written

- do not invent alternate closing tags such as [[/FIL_RECORD]], [[end_section]], or misspelled FILMCREATOR tags

- do not echo this instruction block back as an example packet; return the actual packet only



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
CH002

# Title
CHAPTER II.

# Text
The Pool of Tears


“Curiouser and curiouser!” cried Alice (she was so much surprised, that
for the moment she quite forgot how to speak good English); “now I’m
opening out like the largest telescope that ever was! Good-bye, feet!”
(for when she looked down at her feet, they seemed to be almost out of
sight, they were getting so far off). “Oh, my poor little feet, I
wonder who will put on your shoes and stockings for you now, dears? I’m
sure _I_ shan’t be able! I shall be a great deal too far off to trouble
myself about you: you must manage the best way you can;—but I must be
kind to them,” thought Alice, “or perhaps they won’t walk the way I
want to go! Let me see: I’ll give them a new pair of boots every
Christmas.”

And she went on planning to herself how she would manage it. “They must
go by the carrier,” she thought; “and how funny it’ll seem, sending
presents to one’s own feet! And how odd the directions will look!

     _Alice’s Right Foot, Esq., Hearthrug, near the Fender,_ (_with
     Alice’s love_).

Oh dear, what nonsense I’m talking!”

Just then her head struck against the roof of the hall: in fact she was
now more than nine feet high, and she at once took up the little golden
key and hurried off to the garden door.

Poor Alice! It was as much as she could do, lying down on one side, to
look through into the garden with one eye; but to get through was more
hopeless than ever: she sat down and began to cry again.

“You ought to be ashamed of yourself,” said Alice, “a great girl like
you,” (she might well say this), “to go on crying in this way! Stop
this moment, I tell you!” But she went on all the same, shedding
gallons of tears, until there was a large pool all round her, about
four inches deep and reaching half down the hall.

After a time she heard a little pattering of feet in the distance, and
she hastily dried her eyes to see what was coming. It was the White
Rabbit returning, splendidly dressed, with a pair of white kid gloves
in one hand and a large fan in the other: he came trotting along in a
great hurry, muttering to himself as he came, “Oh! the Duchess, the
Duchess! Oh! won’t she be savage if I’ve kept her waiting!” Alice felt
so desperate that she was ready to ask help of any one; so, when the
Rabbit came near her, she began, in a low, timid voice, “If you please,
sir—” The Rabbit started violently, dropped the white kid gloves and
the fan, and skurried away into the darkness as hard as he could go.

Alice took up the fan and gloves, and, as the hall was very hot, she
kept fanning herself all the time she went on talking: “Dear, dear! How
queer everything is to-day! And yesterday things went on just as usual.
I wonder if I’ve been changed in the night? Let me think: was I the
same when I got up this morning? I almost think I can remember feeling
a little different. But if I’m not the same, the next question is, Who
in the world am I? Ah, _that’s_ the great puzzle!” And she began
thinking over all the children she knew that were of the same age as
herself, to see if she could have been changed for any of them.

“I’m sure I’m not Ada,” she said, “for her hair goes in such long
ringlets, and mine doesn’t go in ringlets at all; and I’m sure I can’t
be Mabel, for I know all sorts of things, and she, oh! she knows such a
very little! Besides, _she’s_ she, and _I’m_ I, and—oh dear, how
puzzling it all is! I’ll try if I know all the things I used to know.
Let me see: four times five is twelve, and four times six is thirteen,
and four times seven is—oh dear! I shall never get to twenty at that
rate! However, the Multiplication Table doesn’t signify: let’s try
Geography. London is the capital of Paris, and Paris is the capital of
Rome, and Rome—no, _that’s_ all wrong, I’m certain! I must have been
changed for Mabel! I’ll try and say ‘_How doth the little_—’” and she
crossed her hands on her lap as if she were saying lessons, and began
to repeat it, but her voice sounded hoarse and strange, and the words
did not come the same as they used to do:—

“How doth the little crocodile
    Improve his shining tail,
And pour the waters of the Nile
    On every golden scale!

“How cheerfully he seems to grin,
    How neatly spread his claws,
And welcome little fishes in
    With gently smiling jaws!”


“I’m sure those are not the right words,” said poor Alice, and her eyes
filled with tears again as she went on, “I must be Mabel after all, and
I shall have to go and live in that poky little house, and have next to
no toys to play with, and oh! ever so many lessons to learn! No, I’ve
made up my mind about it; if I’m Mabel, I’ll stay down here! It’ll be
no use their putting their heads down and saying ‘Come up again, dear!’
I shall only look up and say ‘Who am I then? Tell me that first, and
then, if I like being that person, I’ll come up: if not, I’ll stay down
here till I’m somebody else’—but, oh dear!” cried Alice, with a sudden
burst of tears, “I do wish they _would_ put their heads down! I am so
_very_ tired of being all alone here!”

As she said this she looked down at her hands, and was surprised to see
that she had put on one of the Rabbit’s little white kid gloves while
````

## Raw Response
````text
[[FILMCREATOR_PACKET]]
[[FILMCREATOR_RECORD]]
type: character
asset_id: alice
canonical_character_id: alice
aliases: []
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
direct_identity_evidence: "The text explicitly names her 'Alice' and she refers to herself as 'I'."
direct_visual_evidence: "She is described as being over nine feet tall in this chapter, having hair that does not go in ringlets (unlike Mabel), and having hands/feet that are currently far from her head due to size changes."
costume_or_covering_evidence: "Not explicitly detailed in this excerpt beyond the mention of shoes and stockings which she is worried about for her feet."
movement_evidence: "Lying down on one side, sitting down, crying, crossing hands on lap, fanning herself."
associated_entities: ["white_rabbit"]
alias_or_role_evidence: ""
unknowns: []
source_refs: ["CH002"]
[[SECTION character_index_markdown]]
[[markdown]]
# Alice
**Role:** Protagonist

**Status:** Physically Present

**Physical Description:**
- A young girl currently experiencing extreme size fluctuations. 
- In this chapter, she grows to over nine feet in height.
- Her hair is noted as *not* being in long ringlets (distinguishing her from Mabel).
- Currently distressed and crying, creating a large pool of tears around her.

**Costume & Silhouette:**
- Mention of shoes and stockings (though her feet are currently too far away to see clearly).
- Silhouette is characterized by extreme verticality/scale in this scene.

**Descriptive Noun Phrases:**
- Giant young girl
- Distressed child
- Nine-foot-tall girl
- Crying girl in a hall

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: white_rabbit
canonical_character_id: white_rabbit
aliases: ["Rabbit"]
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
direct_identity_evidence: "Explicitly named 'the White Rabbit'."
direct_visual_evidence: "Described as 'splendidly dressed', carrying white kid gloves and a large fan, and 'trotting along'."
costume_or_covering_evidence: "Splendidly dressed; carries white kid gloves and a large fan."
movement_evidence: "Trotting along in a great hurry, skurried away into the darkness."
associated_entities: ["alice", "the_duchess"]
alias_or_role_evidence: ""
unknowns: []
source_refs: ["CH002"]
[[SECTION character_index_markdown]]
[[markdown]]
# White Rabbit
**Role:** Supporting Character / Catalyst

**Status:** Physically Present

**Physical Description:**
- A white rabbit.
- Appears to be small in scale relative to the environment/Alice.

**Costume & Silhouette:**
- "Splendidly dressed."
- Carries a pair of white kid gloves in one hand and a large fan in the other.

**Descriptive Noun Phrases:**
- Dapper white rabbit
- Anthropomorphic white rabbit
- Rabbit in fine clothing

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: the_duchess
canonical_character_id: the_duchess
aliases: []
is_fully_identified: false
manual_description_required: true
manual_description_reason: "The character is only mentioned in dialogue by the White Rabbit and has no physical description provided in this chapter."
clarification_required: true
clarification_reason: "Character is only a verbal reference; visual identity is unknown."
clarification_question: "What is the Duchess's physical appearance, species, and attire?"
character_type_hint: unknown
morphology_hint: unknown
scale_hint: unknown
renderability_hint: context_only
confidence: 0.5
direct_identity_evidence: "Mentioned by name by the White Rabbit."
direct_visual_evidence: ""
costume_or_covering_evidence: ""
movement_evidence: ""
associated_entities: ["white_rabbit"]
alias_or_role_evidence: ""
unknowns: ["physical appearance", "species", "scale", "clothing"]
source_refs: ["CH002"]
[[SECTION character_index_markdown]]
[[markdown]]
# The Duchess
**Role:** Referenced Character

**Status:** Referenced (Not Present)

**Physical Description:**
- No physical description available in this text.

**Costume & Silhouette:**
- No costume information available.

**Descriptive Noun Phrases:**
- Mentioned Duchess
- Savage Duchess (per Rabbit's dialogue)

**Uncertainty Notes:**
- This character is only mentioned by the White Rabbit as someone who might be "savage" if kept waiting. There are no visual details to support rendering.

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: mabel
canonical_character_id: mabel
aliases: []
is_fully_identified: true
manual_description_required: false
manual_description_reason: ""
clarification_required: false
clarification_reason: ""
clarification_question: ""
character_type_hint: human
morphology_hint: biped
scale_hint: human_scale
renderability_hint: context_only
confidence: 0.8
direct_identity_evidence: "Alice compares herself to 'Mabel'."
direct_visual_evidence: "Described via contrast: has hair that goes in 'such long ringlets'."
costume_or_covering_evidence: ""
movement_evidence: ""
associated_entities: []
alias_or_role_evidence: ""
unknowns: ["exact age", "full appearance"]
source_refs: ["CH002"]
[[SECTION character_index_markdown]]
[[markdown]]
# Mabel
**Role:** Referenced Character (Comparison)

**Status:** Referenced (Not Present)

**Physical Description:**
- A child of similar age to Alice.
- Notable for having hair that goes in "long ringlets."

**Costume & Silhouette:**
- No specific costume mentioned.

**Descriptive Noun Phrases:**
- Girl with long ringlets
- Child peer

**Uncertainty Notes:**
- Mabel is used as a mental benchmark by Alice to determine her own identity; she is not physically present in the scene.

[[/SECTION]]
[[/FILMCREATOR_RECORD]]
[[/FILMCREATOR_PACKET]]
````
