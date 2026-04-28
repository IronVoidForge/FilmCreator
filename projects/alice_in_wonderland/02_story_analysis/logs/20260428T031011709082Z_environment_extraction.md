# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-28T03:10:11.709082+00:00
- task: environment_extraction

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

Chapter id: CH005

Task: extract environment families into an environment index plus one Markdown file per environment family.

Packet contract:
- task: environment_extraction
- version: 1
- first line: [[FILMCREATOR_PACKET]]
- last line: [[/FILMCREATOR_PACKET]]
- required sections: environment_index_markdown
- record type environment: fields=asset_id sections=markdown



Literal tag rules:

- begin with [[FILMCREATOR_PACKET]] on its own line

- end with [[/FILMCREATOR_PACKET]] on its own line

- wrap each environment item in [[FILMCREATOR_RECORD]] ... [[/FILMCREATOR_RECORD]]

- use [[SECTION environment_index_markdown]] and [[SECTION markdown]] exactly as written

- do not echo this instruction block back as an example packet; return the actual packet only



Asset id rules:

- lowercase snake_case

- stable across later reruns

- emit one explicit environment record per meaningful location or setting family

- every environment record must have a FILMCREATOR_RECORD wrapper with type environment

- keep the environment set small and useful

- use concise visible descriptions



Each environment Markdown file should include:

- environment role such as primary, secondary, or transit setting

- architecture or geography

- lighting and atmosphere cues

- scale cues and recurring environmental anchors

- useful descriptive noun phrases for later render-facing prompt writing



Chapter summary:

Fallback extraction chunk 1/2 for environment_extraction.

Use only the chapter excerpt below for this pass.

# Chapter
CH005

# Title
CHAPTER V.

# Text
Advice from a Caterpillar


The Caterpillar and Alice looked at each other for some time in
silence: at last the Caterpillar took the hookah out of its mouth, and
addressed her in a languid, sleepy voice.

“Who are _you?_” said the Caterpillar.

This was not an encouraging opening for a conversation. Alice replied,
rather shyly, “I—I hardly know, sir, just at present—at least I know
who I _was_ when I got up this morning, but I think I must have been
changed several times since then.”

“What do you mean by that?” said the Caterpillar sternly. “Explain
yourself!”

“I can’t explain _myself_, I’m afraid, sir,” said Alice, “because I’m
not myself, you see.”

“I don’t see,” said the Caterpillar.

“I’m afraid I can’t put it more clearly,” Alice replied very politely,
“for I can’t understand it myself to begin with; and being so many
different sizes in a day is very confusing.”

“It isn’t,” said the Caterpillar.

“Well, perhaps you haven’t found it so yet,” said Alice; “but when you
have to turn into a chrysalis—you will some day, you know—and then
after that into a butterfly, I should think you’ll feel it a little
queer, won’t you?”

“Not a bit,” said the Caterpillar.

“Well, perhaps your feelings may be different,” said Alice; “all I know
is, it would feel very queer to _me_.”

“You!” said the Caterpillar contemptuously. “Who are _you?_”

Which brought them back again to the beginning of the conversation.
Alice felt a little irritated at the Caterpillar’s making such _very_
short remarks, and she drew herself up and said, very gravely, “I
think, you ought to tell me who _you_ are, first.”

“Why?” said the Caterpillar.

Here was another puzzling question; and as Alice could not think of any
good reason, and as the Caterpillar seemed to be in a _very_ unpleasant
state of mind, she turned away.

“Come back!” the Caterpillar called after her. “I’ve something
important to say!”

This sounded promising, certainly: Alice turned and came back again.

“Keep your temper,” said the Caterpillar.

“Is that all?” said Alice, swallowing down her anger as well as she
could.

“No,” said the Caterpillar.

Alice thought she might as well wait, as she had nothing else to do,
and perhaps after all it might tell her something worth hearing. For
some minutes it puffed away without speaking, but at last it unfolded
its arms, took the hookah out of its mouth again, and said, “So you
think you’re changed, do you?”

“I’m afraid I am, sir,” said Alice; “I can’t remember things as I
used—and I don’t keep the same size for ten minutes together!”

“Can’t remember _what_ things?” said the Caterpillar.

“Well, I’ve tried to say “How doth the little busy bee,” but it all
came different!” Alice replied in a very melancholy voice.

“Repeat, ‘_You are old, Father William_,’” said the Caterpillar.

Alice folded her hands, and began:—

“You are old, Father William,” the young man said,
    “And your hair has become very white;
And yet you incessantly stand on your head—
    Do you think, at your age, it is right?”

“In my youth,” Father William replied to his son,
    “I feared it might injure the brain;
But, now that I’m perfectly sure I have none,
    Why, I do it again and again.”

“You are old,” said the youth, “as I mentioned before,
    And have grown most uncommonly fat;
Yet you turned a back-somersault in at the door—
    Pray, what is the reason of that?”

“In my youth,” said the sage, as he shook his grey locks,
    “I kept all my limbs very supple
By the use of this ointment—one shilling the box—
    Allow me to sell you a couple?”

“You are old,” said the youth, “and your jaws are too weak
    For anything tougher than suet;
Yet you finished the goose, with the bones and the beak—
    Pray, how did you manage to do it?”

“In my youth,” said his father, “I took to the law,
    And argued each case with my wife;
And the muscular strength, which it gave to my jaw,
    Has lasted the rest of my life.”

“You are old,” said the youth, “one would hardly suppose
    That your eye was as steady as ever;
Yet you balanced an eel on the end of your nose—
    What made you so awfully clever?”

“I have answered three questions, and that is enough,”
    Said his father; “don’t give yourself airs!
Do you think I can listen all day to such stuff?
    Be off, or I’ll kick you down stairs!”


“That is not said right,” said the Caterpillar.

“Not _quite_ right, I’m afraid,” said Alice, timidly; “some of the
words have got altered.”

“It is wrong from beginning to end,” said the Caterpillar decidedly,
and there was silence for some minutes.

The Caterpillar was the first to speak.

“What size do you want to be?” it asked.

“Oh, I’m not particular as to size,” Alice hastily replied; “only one
doesn’t like changing so often, you know.”

“I _don’t_ know,” said the Caterpillar.

Alice said nothing: she had never been so much contradicted in her life
before, and she felt that she was losing her temper.

“Are you content now?” said the Caterpillar.

“Well, I should like to be a _little_ larger, sir, if you wouldn’t
mind,” said Alice: “three inches is such a wretched height to be.”
````

## Raw Response
````text
[[FILMCREATOR_PACKET]]
[[SECTION environment_index_markdown]]
[[environment_family_mushroom_forest]]
- [mushroom_forest_setting](mushroom_forest_setting)
[[/SECTION]]
[[FILMCREATOR_RECORD]]
type: environment
asset_id: mushroom_forest_setting
[[SECTION markdown]]
### Environment Role
Primary setting

### Architecture or Geography
A surreal, organic landscape dominated by oversized fungal structures and natural growths. The terrain is uneven and non-human in scale.

### Lighting and Atmosphere Cues
Languid, sleepy, and heavy atmosphere. Dappled light filtering through large biological canopies; a sense of stillness punctuated by slow, rhythmic movements (like smoke from a hookah).

### Scale Cues and Recurring Environmental Anchors
Extreme scale shifts; massive mushroom caps providing platforms or ceilings; small-scale flora contrasted against giant insectoid inhabitants.

### Descriptive Noun Phrases
Oversized fungal canopy, languid woodland, surreal mycological landscape, hookah smoke plumes, giant caterpillar perch, dappled forest floor.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]
[[/FILMCREATOR_PACKET]]
````
