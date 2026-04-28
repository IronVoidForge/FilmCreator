# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-28T04:16:45.862585+00:00
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

Chapter id: CH011

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

**Location:** The Court of Justice (an outdoor or large open court setting).
**Characters Present:** 
- Alice (growing in size)
- The King of Hearts (acting as Judge, wearing a crown over a large wig)
- The Queen of Hearts (wearing spectacles)
- The White Rabbit (Herald/Officer, carrying a trumpet and parchment scroll)
- The Knave of Hearts (Defendant, in chains, guarded by two soldiers)
- The Gryphon (Witness/Companion to Alice)
- The Jury (Twelve creatures: mix of animals and birds; writing on slates)
- Bill the Lizard (Juror)
- The Hatter (Witness, carrying a teacup and bread-and-butter)
- The March Hare (Witness/Companion to Hatter)
- The Dormouse (Witness/Companion to Hatter, prone to sleeping/being erratic)
- The Duchess's Cook (Witness, carrying a pepper-box)
- Guinea-pigs (Court spectators)
- Court Officers

**Key Events & Visual Continuity:**
- **Setting Establishment:** A large dish of tarts sits on a central table. The Knave is in chains with guards.
- **Jury Interaction:** Jurors are writing names on slates. Alice calls them "stupid things" aloud; the White Rabbit commands silence. One juror (Bill the Lizard) loses his squeaky pencil after Alice steals it; he must write with a finger (leaving no marks).
- **The Accusation:** The White Rabbit blows three trumpet blasts and reads the charge: The Knave of Hearts stole the Queen's tarts.
- **Witness 1 - The Hatter:** Enters carrying tea and bread-and-butter, accompanied by the March Hare and Dormouse. 
    - The King questions the date he began his tea (March 14th, 15th, or 16th); jurors record all three and perform math on their slates.
    - The Hatter is accused of "stealing" a hat; he explains it is for sale.
    - The Queen stares intensely at the Hatter; he becomes so nervous he bites his teacup instead of bread.
- **Alice's Physical Shift:** Alice begins to grow in size, causing discomfort to the Dormouse. The Dormouse sulkily moves to the other side of the court.
- **Hatter's Testimony:** A nonsensical exchange regarding "the twinkling of the tea." The March Hare denies saying things; the Dormouse is asleep and offers no testimony. 
- **Court Suppression:** Two guinea-pigs cheer and are "suppressed" by being put into a large canvas bag and sat upon by officers.
- **Hatter's Exit:** The Hatter drops his tea/bread, kneels, and leaves the court in a hurry without his shoes. The Queen orders his head removed, but he is gone before the officer arrives.
- **Witness 2 - The Cook:** Enters carrying a pepper-box; causes immediate sneezing among nearby spectators.
    - The King cross-examines her: "What are tarts made of?" She answers "Pepper, mostly."
    - The Dormouse (from behind) says "Treacle."
    - **The Queen's Outburst:** The Queen shrieks a series of contradictory commands to behead/suppress/pinch the Dormouse. In the ensuing chaos, the Cook disappears.
- **The Reveal:** The White Rabbit consults his list and announces the next witness: Alice.
````

## Raw Response
````text
[[FILMCREATOR_PACKET]]
[[SECTION environment_index_markdown]]
# Environment Index

- [court_of_justice](court_of_justice)
[[/SECTION]]

[[FILMCREATOR_RECORD type="environment"]]
asset_id: court_of_justice
[[SECTION markdown]]
# Court of Justice

**Role:** Primary Setting

**Architecture or Geography:** 
A large, open-air judicial arena. The space is defined by a central area for the trial and tiered or clustered seating/standing areas for the jury (a mix of animals and birds) and spectators (guinea-pigs). A central table holds evidence, such as a dish of tarts.

**Lighting and Atmosphere Cues:** 
Bright, exposed outdoor lighting. The atmosphere is chaotic, nonsensical, and high-tension, oscillating between formal judicial proceedings and sudden outbursts of violence or absurdity. Occasional puffs of pepper dust from the Cook's box create localized atmospheric haze.

**Scale Cues and Recurring Environmental Anchors:** 
- **The Central Table:** Holds the stolen tarts and serves as a focal point for evidence.
- **The Jury Slates:** Small, handheld writing surfaces used by the animal/bird jurors.
- **The Witness Stand/Path:** The route taken by eccentric witnesses like the Hatter and the Cook.
- **Scale Shift:** Alice's physical growth creates a dynamic change in the perceived scale of the court, making the environment feel increasingly cramped or small relative to her.

**Descriptive Noun Phrases:** 
Open-air courtroom, animal jury with slates, central evidence table, dish of tarts, chaotic judicial arena, oversized witness testimony, pepper-filled atmosphere, nonsensical legal setting.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]
[[/FILMCREATOR_PACKET]]
````
