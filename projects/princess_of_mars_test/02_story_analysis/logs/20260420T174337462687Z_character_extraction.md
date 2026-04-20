# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-20T17:43:37.462687+00:00
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
The chapter begins with a journey across a rising landscape toward the edge of a long-dead Martian sea. The party arrives at an enormous, ancient city situated on a low table land. The city features grand, white marble and gold architecture that appears far too large for its current inhabitants, suggesting it was built by a long-extinct race. Key locations include a central plaza and a magnificent audience chamber filled with oversized furniture.

**Characters:**
* **The Narrator (Human):** A captive being escorted through the Martian city. He struggles with his physical inadequacy compared to the Martians but demonstrates strength and agility.
* **Tars Tarkas:** A Green Martian vice-chieftain, described as a capable statesman and warrior. He acts as the narrator's escort/guard.
* **The Chieftain:** The ruler of the local community, an enormous warrior adorned in metal, feathers, and silk.
* **Sola:** A young female Martian (approx. 8 feet tall) with light olive-green skin, belonging to Tars Tarkas's retinue. She provides the narrator with food and shelter.
* **The Martians (Green Men):** A violent, multi-legged species. They are characterized by their lack of clothing (except ornaments), large tusks, and a culture that finds humor in death and suffering.

**Key Events:**
* **Arrival at the City:** The narrator and Tars Tarkas enter a deserted but grand city, discovering it is populated by hundreds of Green Martians.
* **The Audience Chamber:** The party enters a massive hall to meet the Chieftain. The narrator observes that the Martian's furniture is scaled for humans, implying an older, lost civilization.
* **Physical Confrontation:** After struggling to walk due to his different physiology, the narrator accidentally strikes a Martian who was mocking him. Instead of being punished, he is met with laughter and applause, earning a rare sign of respect.
* **The "Sak" Demonstration:** To prove his worth/ability, the narrator performs a massive leap (sakk) of 150 feet, impressing the gathered warriors.
* **Request for Sustenance:** The narrator refuses to perform further jumps until he is fed and watered, using gestures to communicate his hunger.
* **Introduction to Sola and Martian Fauna:** Tars Tarkas assigns Sola to care for the narrator. She leads him to a decorated sleeping chamber, where the narrator encounters a small, ten-legged, frog-like creature with three rows of tusks that acts as a pet.
````

## Raw Response
````text
[[FILMCREATOR_PACKET]]

task: character_extraction

version: 1

character_index_markdown:

[[SECTION character_index_markdown]]

# Character Index - CH004

- [narrator](#narrator)
- [tars_tarkas](#tars_tarkas)
- [the_chieftain](#the_chieftain)
- [sola](#sola)
- [martians](#martians)

[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: narrator
canonical_character_id: CH004 Narrator
aliases: Human, Captive
is_fully_identified: true
manual_description_required: true
manual_description_reason: Physical appearance (facial features, hair, build) is not detailed beyond being human and having different physiology than Martians.
clarification_required: false
clarification_reason: 
clarification_question: 
[[SECTION markdown]]
# Narrator
**Role:** Protagonist / Captive
**Presence:** Physically Present
**Physical Description:** A human male. Demonstrates high agility and strength relative to his size, capable of a 150-foot leap (sakk). Appears physically small/inadequate compared to the Martian species.
**Costume/Silhouette:** Not explicitly described; likely captive attire.
**Prompt Phrases:** Human male, agile, small stature relative to Martians, performing massive leaps.
**Uncertainty Notes:** Specific facial features and clothing are unknown.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: tars_tarkas
canonical_character_id: CH004 Tars Tarkas
aliases: Green Martian Vice-Chieftain, Escort
is_fully_identified: true
manual_description_required: false
clarification_required: false
clarification_reason: 
clarification_question: 
[[SECTION markdown]]
# Tars Tarkas
**Role:** Vice-chieftain / Guard
**Presence:** Physically Present
**Physical Description:** A Green Martian. Capable statesman and warrior. Part of the multi-legged, tusked species.
**Costume/Silhouette:** Green Martian physiology; likely minimal clothing/ornaments consistent with his race.
**Prompt Phrases:** Green Martian, multi-legged, large tusks, warrior, statesman.
**Uncertainty Notes:** Specific ornamentation or exact limb count not specified in this chapter.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: the_chieftain
canonical_character_id: CH004 The Chieftain
aliases: Ruler
is_fully_identified: true
manual_description_required: false
clarification_required: false
clarification_reason: 
clarification_question: 
[[SECTION markdown]]
# The Chieftain
**Role:** Local Ruler
**Presence:** Physically Present
**Physical Description:** An enormous Green Martian warrior.
**Costume/Silhouette:** Adorned in metal, feathers, and silk. Massive scale.
**Prompt Phrases:** Enormous Green Martian, warrior, wearing metal ornaments, feathers, and silk, massive silhouette.
**Uncertainty Notes:** None.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: sola
canonical_character_id: CH004 Sola
aliases: Martian Retinue Member
is_fully_identified: true
manual_description_required: false
clarification_required: false
clarification_reason: 
clarification_question: 
[[SECTION markdown]]
# Sola
**Role:** Caretaker / Attendant
**Presence:** Physically Present
**Physical Description:** Young female Martian, approximately 8 feet tall, with light olive-green skin.
**Costume/Silhouette:** Consistent with Green Martian species (minimal clothing/ornaments).
**Prompt Phrases:** Female Martian, 8 feet tall, light olive-green skin, young appearance.
**Uncertainty Notes:** None.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: martians
canonical_character_id: CH004 Martians
aliases: Green Men
is_fully_identified: true
manual_description_required: false
clarification_required: false
clarification_reason: 
clarification_question: 
[[SECTION markdown]]
# The Martians
**Role:** Background Population / Warriors
**Presence:** Physically Present
**Physical Description:** A violent, multi-legged species with large tusks.
**Costume/Silhouette:** Generally lack clothing, wearing only ornaments.
**Prompt Phrases:** Green Martians, multi-legged, large tusks, minimal clothing, ornamental jewelry.
**Uncertainty Notes:** Specific number of legs or exact tusk shape not defined.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
