# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-28T03:17:18.683777+00:00
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

Fallback extraction chunk 2/2 for character_extraction.

Use only the chapter excerpt below for this pass.

here till I’m somebody else’—but, oh dear!” cried Alice, with a sudden
burst of tears, “I do wish they _would_ put their heads down! I am so
_very_ tired of being all alone here!”

As she said this she looked down at her hands, and was surprised to see
that she had put on one of the Rabbit’s little white kid gloves while
she was talking. “How _can_ I have done that?” she thought. “I must be
growing small again.” She got up and went to the table to measure
herself by it, and found that, as nearly as she could guess, she was
now about two feet high, and was going on shrinking rapidly: she soon
found out that the cause of this was the fan she was holding, and she
dropped it hastily, just in time to avoid shrinking away altogether.

“That _was_ a narrow escape!” said Alice, a good deal frightened at the
sudden change, but very glad to find herself still in existence; “and
now for the garden!” and she ran with all speed back to the little
door: but, alas! the little door was shut again, and the little golden
key was lying on the glass table as before, “and things are worse than
ever,” thought the poor child, “for I never was so small as this
before, never! And I declare it’s too bad, that it is!”

As she said these words her foot slipped, and in another moment,
splash! she was up to her chin in salt water. Her first idea was that
she had somehow fallen into the sea, “and in that case I can go back by
railway,” she said to herself. (Alice had been to the seaside once in
her life, and had come to the general conclusion, that wherever you go
to on the English coast you find a number of bathing machines in the
sea, some children digging in the sand with wooden spades, then a row
of lodging houses, and behind them a railway station.) However, she
soon made out that she was in the pool of tears which she had wept when
she was nine feet high.

“I wish I hadn’t cried so much!” said Alice, as she swam about, trying
to find her way out. “I shall be punished for it now, I suppose, by
being drowned in my own tears! That _will_ be a queer thing, to be
sure! However, everything is queer to-day.”

Just then she heard something splashing about in the pool a little way
off, and she swam nearer to make out what it was: at first she thought
it must be a walrus or hippopotamus, but then she remembered how small
she was now, and she soon made out that it was only a mouse that had
slipped in like herself.

“Would it be of any use, now,” thought Alice, “to speak to this mouse?
Everything is so out-of-the-way down here, that I should think very
likely it can talk: at any rate, there’s no harm in trying.” So she
began: “O Mouse, do you know the way out of this pool? I am very tired
of swimming about here, O Mouse!” (Alice thought this must be the right
way of speaking to a mouse: she had never done such a thing before, but
she remembered having seen in her brother’s Latin Grammar, “A mouse—of
a mouse—to a mouse—a mouse—O mouse!”) The Mouse looked at her rather
inquisitively, and seemed to her to wink with one of its little eyes,
but it said nothing.

“Perhaps it doesn’t understand English,” thought Alice; “I daresay it’s
a French mouse, come over with William the Conqueror.” (For, with all
her knowledge of history, Alice had no very clear notion how long ago
anything had happened.) So she began again: “Où est ma chatte?” which
was the first sentence in her French lesson-book. The Mouse gave a
sudden leap out of the water, and seemed to quiver all over with
fright. “Oh, I beg your pardon!” cried Alice hastily, afraid that she
had hurt the poor animal’s feelings. “I quite forgot you didn’t like
cats.”

“Not like cats!” cried the Mouse, in a shrill, passionate voice. “Would
_you_ like cats if you were me?”

“Well, perhaps not,” said Alice in a soothing tone: “don’t be angry
about it. And yet I wish I could show you our cat Dinah: I think you’d
take a fancy to cats if you could only see her. She is such a dear
quiet thing,” Alice went on, half to herself, as she swam lazily about
in the pool, “and she sits purring so nicely by the fire, licking her
paws and washing her face—and she is such a nice soft thing to
nurse—and she’s such a capital one for catching mice—oh, I beg your
pardon!” cried Alice again, for this time the Mouse was bristling all
over, and she felt certain it must be really offended. “We won’t talk
about her any more if you’d rather not.”

“We indeed!” cried the Mouse, who was trembling down to the end of his
tail. “As if _I_ would talk on such a subject! Our family always
_hated_ cats: nasty, low, vulgar things! Don’t let me hear the name
again!”

“I won’t indeed!” said Alice, in a great hurry to change the subject of
conversation. “Are you—are you fond—of—of dogs?” The Mouse did not
answer, so Alice went on eagerly: “There is such a nice little dog near
our house I should like to show you! A little bright-eyed terrier, you
know, with oh, such long curly brown hair! And it’ll fetch things when
you throw them, and it’ll sit up and beg for its dinner, and all sorts
of things—I can’t remember half of them—and it belongs to a farmer, you
know, and he says it’s so useful, it’s worth a hundred pounds! He says
it kills all the rats and—oh dear!” cried Alice in a sorrowful tone,
“I’m afraid I’ve offended it again!” For the Mouse was swimming away
from her as hard as it could go, and making quite a commotion in the
pool as it went.

So she called softly after it, “Mouse dear! Do come back again, and we
won’t talk about cats or dogs either, if you don’t like them!” When the
Mouse heard this, it turned round and swam slowly back to her: its face
was quite pale (with passion, Alice thought), and it said in a low
trembling voice, “Let us get to the shore, and then I’ll tell you my
history, and you’ll understand why it is I hate cats and dogs.”

It was high time to go, for the pool was getting quite crowded with the
birds and animals that had fallen into it: there were a Duck and a
Dodo, a Lory and an Eaglet, and several other curious creatures. Alice
led the way, and the whole party swam to the shore.
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
scale_hint: tiny
renderability_hint: renderable
confidence: 1.0
direct_identity_evidence: "cried Alice"
direct_visual_evidence: "she was now about two feet high... she had put on one of the Rabbit’s little white kid gloves"
costume_or_covering_evidence: "one of the Rabbit’s little white kid gloves"
movement_evidence: "ran with all speed", "swam about", "led the way"
associated_entities: ["mouse", "dinah", "dodo", "duck", "lory", "eaglet"]
alias_or_role_evidence: ""
unknowns: []
source_refs: []
[[SECTION character_index_markdown]]
[[markdown]]
# Alice
**Role:** Protagonist

**Status:** Physically Present

**Physical Description:**
A young girl who is currently undergoing rapid shrinking. At the start of this segment, she is approximately two feet high.

**Costume & Traits:**
- Wearing one of the Rabbit's little white kid gloves.
- Currently wet from swimming in a pool of tears.

**Descriptive Noun Phrases:**
- small girl
- shrinking child
- swimming girl
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: mouse
canonical_character_id: mouse
aliases: ["O Mouse", "Mouse dear"]
is_fully_identified: true
manual_description_required: false
manual_description_reason: ""
clarification_required: false
clarification_reason: ""
clarification_question: ""
character_type_hint: animal
morphology_hint: quadruped
scale_hint: tiny
renderability_hint: renderable
confidence: 0.9
direct_identity_evidence: "it was only a mouse"
direct_visual_evidence: "wink with one of its little eyes", "bristling all over", "trembling down to the end of his tail", "face was quite pale"
costume_or_covering_evidence: ""
movement_evidence: "splashing about", "sudden leap out of the water", "swimming away... as hard as it could go"
associated_entities: ["alice"]
alias_or_role_evidence: "O Mouse"
unknowns: []
source_refs: []
[[SECTION character_index_markdown]]
[[markdown]]
# Mouse
**Role:** Supporting Character / Conversationalist

**Status:** Physically Present

**Physical Description:**
A small mouse capable of speech. It exhibits high emotion, appearing to "wink" with an eye and becoming visibly agitated (bristling/trembling). Alice notes its face looks "quite pale" during a moment of passion.

**Costume & Traits:**
- Small, sensitive, and easily offended.
- Has a tail that trembles.

**Descriptive Noun Phrases:**
- small mouse
- talking mouse
- indignant mouse
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: dinah
canonical_character_id: dinah
aliases: ["cat"]
is_fully_identified: true
manual_description_required: true
manual_description_reason: "The character is only mentioned in dialogue/memory; no visual description of her appearance (color, breed, size) is provided in the text."
clarification_required: false
clarification_reason: ""
clarification_question: ""
character_type_hint: animal
morphology_hint: quadruped
scale_hint: unknown
renderability_hint: context_only
confidence: 0.8
direct_identity_evidence: "our cat Dinah"
direct_visual_evidence: ""
costume_or_covering_evidence: ""
movement_evidence: "sits purring so nicely by the fire, licking her paws and washing her face"
associated_entities: ["alice"]
alias_or_role_evidence: "cat Dinah"
unknowns: ["physical appearance", "size"]
source_refs: []
[[SECTION character_index_markdown]]
[[markdown]]
# Dinah
**Role:** Referenced Character (Alice's pet)

**Status:** Referenced

**Physical Description:**
No specific visual details provided. Alice describes her temperament as a "dear quiet thing" who purrs by the fire and licks her paws.

**Costume & Traits:**
- A cat.
- Described as "nice soft thing".

**Descriptive Noun Phrases:**
- quiet cat
- purring cat
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: rabbit
canonical_character_id: rabbit
aliases: []
is_fully_identified: true
manual_description_required: true
manual_description_reason: "The Rabbit is only referenced via an object he owns (gloves); no physical description of the creature itself is present in this chapter."
clarification_required: false
clarification_reason: ""
clarification_question: ""
character_type_hint: animal
morphology_hint: unknown
scale_hint: small
renderability_hint: context_only
confidence: 0.5
direct_identity_evidence: "the Rabbit’s little white kid gloves"
direct_visual_evidence: ""
costume_or_covering_evidence: ""
movement_evidence: ""
associated_entities: ["alice"]
alias_or_role_evidence: ""
unknowns: ["physical appearance", "species/morphology"]
source_refs: []
[[SECTION character_index_markdown]]
[[markdown]]
# Rabbit
**Role:** Referenced Character

**Status:** Referenced

**Physical Description:**
No physical description provided in this chapter.

**Costume & Traits:**
- Associated with "little white kid gloves".

**Descriptive Noun Phrases:**
- the rabbit
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: dodo
canonical_character_id: dodo
aliases: []
is_fully_identified: true
manual_description_required: true
manual_description_reason: "Mentioned only as part of a group in the pool; no specific physical traits provided."
clarification_required: false
clarification_reason: ""
clarification_question: ""
character_type_hint: animal
morphology_hint: unknown
scale_hint: unknown
renderability_hint: context_only
confidence: 0.5
direct_identity_evidence: "there were a Duck and a Dodo"
direct_visual_evidence: ""
costume_or_covering_evidence: ""
movement_evidence: ""
associated_entities: ["alice", "duck", "lory", "eaglet"]
alias_or_role_evidence: ""
unknowns: []
source_refs: []
[[SECTION character_index_markdown]]
[[markdown]]
# Dodo
**Role:** Background Character

**Status:** Physically Present (in pool)

**Physical Description:**
No specific physical description provided.

**Costume & Traits:**
- Part of the "curious creatures" in the pool.

**Descriptive Noun Phrases:**
- dodo bird
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: duck
canonical_character_id: duck
aliases: []
is_fully_identified: true
manual_description_required: true
manual_description_reason: "Mentioned only as part of a group in the pool; no specific physical traits provided."
clarification_required: false
clarification_reason: ""
clarification_question: ""
character_type_hint: animal
morphology_hint: unknown
scale_hint: unknown
renderability_hint: context_only
confidence: 0.5
direct_identity_evidence: "there were a Duck and a Dodo"
direct_visual_evidence: ""
costume_or_covering_evidence: ""
movement_evidence: ""
associated_entities: ["alice", "dodo", "lory", "eaglet"]
alias_or_role_evidence: ""
unknowns: []
source_refs: []
[[SECTION character_index_markdown]]
[[markdown]]
# Duck
**Role:** Background Character

**Status:** Physically Present (in pool)

**Physical Description:**
No specific physical description provided.

**Costume & Traits:**
- Part of the "curious creatures" in the pool.

**Descriptive Noun Phrases:**
- duck
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: lory
canonical_character_id: lory
aliases: []
is_fully_identified: true
manual_description_required: true
manual_description_reason: "Mentioned only as part of a group in the pool; no specific physical traits provided."
clarification_required: false
clarification_reason: ""
clarification_question: ""
character_type_hint: animal
morphology_hint: unknown
scale_hint: unknown
renderability_hint: context_only
confidence: 0.5
direct_identity_evidence: "a Lory and an Eaglet"
direct_visual_evidence: ""
costume_or_covering_evidence: ""
movement_evidence: ""
associated_entities: ["alice", "duck", "dodo", "eaglet"]
alias_or_role_evidence: ""
unknowns: []
source_refs: []
[[SECTION character_index_markdown]]
[[markdown]]
# Lory
**Role:** Background Character

**Status:** Physically Present (in pool)

**Physical Description:**
No specific physical description provided.

**Costume & Traits:**
- Part of the "curious creatures" in the pool.

**Descriptive Noun Phrases:**
- lory bird
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: eaglet
canonical_character_id: eaglet
aliases: []
is_fully_identified: true
manual_description_required: true
manual_description_reason: "Mentioned only as part of a group in the pool; no specific physical traits provided."
clarification_required: false
clarification_reason: ""
clarification_question: ""
character_type_hint: animal
morphology_hint: unknown
scale_hint: unknown
renderability_hint: context_only
confidence: 0.5
direct_identity_evidence: "a Lory and an Eaglet"
direct_visual_evidence: ""
costume_or_covering_evidence: ""
movement_evidence: ""
associated_entities: ["alice", "duck", "dodo", "lory"]
alias_or_role_evidence: ""
unknowns: []
source_refs: []
[[SECTION character_index_markdown]]
[[markdown]]
# Eaglet
**Role:** Background Character

**Status:** Physically Present (in pool)

**Physical Description:**
No specific physical description provided.

**Costume & Traits:**
- Part of the "curious creatures" in the pool.

**Descriptive Noun Phrases:**
- eaglet bird
[[/SECTION]]
[[/FILMCREATOR_RECORD]]
[[/FILMCREATOR_PACKET]]
````
