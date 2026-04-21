# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-21T06:57:03.291662+00:00
- task: character_extraction

## System Prompt
````text
You are FilmCreator's chapter analysis engine.
Return only FilmCreator packets with the requested sections and records.
Do not wrap the packet in code fences unless explicitly requested.
Do not produce JSON-only responses.
If a packet asks for markdown sections, emit the section name on its own line and wrap the body in [[SECTION ...]] ... [[/SECTION]].
Keep the response deterministic and grounded in the supplied chapter text.
````

## User Prompt
````text
Project slug: princess_of_mars_test

Chapter id: CH004

Task: extract visible and referenced characters into a character index plus one Markdown file per character.

Packet contract:
- task: character_extraction
- version: 1
- first line: [[FILMCREATOR_PACKET]]
- last line: [[/FILMCREATOR_PACKET]]
- required sections: character_index_markdown
- record type character: fields=asset_id, canonical_character_id, aliases, is_fully_identified, manual_description_required, manual_description_reason, clarification_required, clarification_reason, clarification_question sections=markdown



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

**Setting:**
An enormous, ancient city situated on a low table land near the edge of a dried-up Martian sea. The city features magnificent marble and gold architecture that appears far too large for its current inhabitants, suggesting it was built by a forgotten, more advanced race. Key locations include a central plaza and a grand audience chamber filled with human-sized furniture that the Martians struggle to use.

**Characters:**
* **The Narrator (Protagonist):** An Earthman captured by Martians; physically much smaller than his captors but capable of surprising feats of strength and agility.
* **Tars Tarkas:** A high-ranking Green Martian, vice-chieftain of the community, and a skilled statesman/warrior who acts as the narrator's escort.
* **The Chieftain:** The ruler of the local Martian community, adorned in elaborate metal, feather, and silk regalia.
* **Sola:** A young female Martian (approx. 8 feet tall) with light olive-green skin, belonging to Tars Tarkas's retinue; she provides the narrator with food/sustenance.
* **The Martians:** A race of ten-foot-tall, multi-legged creatures characterized by extreme violence, a lack of empathy for suffering, and a culture where death is often treated as a source of amusement.

**Key Events:**
* **Arrival at the City:** The narrator and Tars Tarkas arrive at the deserted, ancient city and enter the central plaza, which is populated by hundreds of Martians.
* **The Audience:** The narrator is presented to the Chieftain in a grand hall. He observes the discrepancy between the Martian biology and the human-sized furniture, noting the antiquity of the ruins.
* **Demonstration of Strength:** After being mocked for his clumsy movement, the narrator punches a Martian warrior who treats him roughly. To his surprise, this act of violence earns him respect and applause from the crowd.
* **The "Sak" Test:** The narrator is commanded to perform "sak" (jumping). He successfully clears 150 feet in a single leap, impressing the assembly.
* **Demand for Sustenance:** Refusing to jump again until his needs are met, the narrator signals his hunger and thirst through gestures.
* **Introduction to Sola:** Tars Tarkas assigns Sola to care for the narrator. She leads him to a decorated sleeping chamber, where he encounters a small, ten-legged Martian creature resembling a pony with a frog-like head and three rows of tusks.
````

## Raw Response
````text
[[FILMCREATOR_PACKET]]

task: character_extraction

version: 1

character_index_markdown:

[[SECTION character_index_markdown]]

# Character Index - CH004

- [protagonist](#protagonist)
- [tars_tarkas](#tars_tarkas)
- [the_chieftain](#the_chieftain)
- [sola](#sola)
- [martian_warrior](#martian_warrior)

[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: protagonist
canonical_character_id: CH004 Protagonist
aliases: Narrator, Earthman
is_fully_identified: false
manual_description_required: true
manual_description_reason: Physical appearance (facial features, hair, build) is not described beyond being an "Earthman" and smaller than Martians.
clarification_required: true
clarification_reason: Needs specific human physical traits for consistent rendering.
clarification_question: What are the protagonist's specific facial features, hair color/style, and clothing?

[[SECTION markdown]]
# Protagonist
**Role:** Narrator / Captive
**Status:** Physically Present
**Description:** An Earthman captured by Martians. He is significantly smaller than the ten-foot Martian inhabitants. He possesses surprising strength and agility, capable of jumping 150 feet in a single leap.
**Visual Cues:** Human scale (relative to giant architecture), agile movement.
**Uncertainty Notes:** Specific facial features, hair, and clothing are currently unknown.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: tars_tarkas
canonical_character_id: CH004 Tars Tarkas
aliases: Vice-chieftain
is_fully_identified: false
manual_description_required: true
manual_description_reason: While identified as a Green Martian, specific physical details like exact limb structure or facial features are not provided in this chapter.
clarification_required: true
clarification_reason: Needs detailed anatomical description for consistent Martian design.
clarification_question: What is the specific morphology of Tars Tarkas's face and limbs?

[[SECTION markdown]]
# Tars Tarkas
**Role:** Vice-chieftain / Escort
**Status:** Physically Present
**Description:** A high-ranking Green Martian and skilled statesman/warrior. He acts as the narrator's escort through the ancient city.
**Visual Cues:** Green skin, large stature (approx 10 feet), multi-legged.
**Uncertainty Notes:** Specific facial details and exact number of limbs/appendages are not specified beyond "multi-legged."
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: the_chieftain
canonical_character_id: CH004 Chieftain
aliases: Ruler
is_fully_identified: false
manual_description_required: true
manual_description_reason: Only described by his regalia; specific biological features are missing.
clarification_required: false
clarification_reason: 
clarification_question: 

[[SECTION markdown]]
# The Chieftain
**Role:** Ruler of the local Martian community
**Status:** Physically Present
**Description:** The leader of the Martians encountered in the grand audience chamber.
**Visual Cues:** Adorned in elaborate metal, feather, and silk regalia. 
**Uncertainty Notes:** Biological appearance is unknown; character identity is tied to his ornate costume.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: sola
canonical_character_id: CH004 Sola
aliases: 
is_fully_identified: true
manual_description_required: false
manual_description_reason: 
clarification_required: false
clarification_reason: 
clarification_question: 

[[SECTION markdown]]
# Sola
**Role:** Caretaker / Retinue member
**Status:** Physically Present
**Description:** A young female Martian belonging to Tars Tarkas's retinue. She is responsible for the narrator's sustenance and comfort.
**Visual Cues:** Approximately 8 feet tall, light olive-green skin.
**Uncertainty Notes:** None provided for basic identification.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: martian_warrior
canonical_character_id: CH004 Martian Warrior
aliases: 
is_fully_identified: false
manual_description_required: true
manual_description_reason: Generic Martian type; lacks individualizing features.
clarification_required: false
clarification_reason: 
clarification_question: 

[[SECTION markdown]]
# Martian Warrior
**Role:** Antagonist / Crowd member
**Status:** Physically Present
**Description:** A member of the violent, ten-foot-tall Martian race who treats the narrator roughly.
**Visual Cues:** Ten feet tall, multi-legged, green skin.
**Uncertainty Notes:** This is a generic character type representing the broader Martian species.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
