# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-21T07:08:57.042350+00:00
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

Chapter id: CH008

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

**Setting:** A deserted Martian city and its surrounding hills/valleys.

**Events:**
- As the protagonist and Sola prepare to depart from the city, a sudden retreat by the green Martians occurs as twenty large, gray-painted airships approach the valley.
- A fierce battle ensues between the Martian warriors in the city buildings and the approaching fleet. The green Martians utilize highly disciplined, specialized marksmanship to target specific components of the ships (guns, officers, steering gear).
- The Martian fleet is routed, with most ships retreating. One unmanned, damaged vessel drifts erratically toward the city.
- The green warriors intercept the drifting craft, haul it to the ground using grappling hooks, and systematically loot it for arms, jewels, food, and water.
- After stripping the ship, the warriors set it ablaze, creating a massive floating funeral pyre that drifts into the distance.
- The protagonist feels an unexpected sense of melancholy and empathy for the defeated crew of the airships.
- Upon returning to the city plaza, the protagonist spots the prisoner taken from the airship: a beautiful, slender, copper-skinned woman with black hair who resembles Earthly women in form. 
- The woman makes a silent gesture toward the protagonist, seeking help; however, due to his ignorance of Martian customs, he fails to respond, leading her to look at him with dejection and contempt before she is taken away.

**Characters:**
- **The Protagonist:** Observes the battle from a window; feels a strange kinship with the defeated airship crew.
- **Sola:** Accompanies the protagonist.
- **Green Martian Warriors:** Highly organized, disciplined military force.
- **The Prisoner:** A beautiful, slender, copper-skinned female captive from the airship; she appears to be of a different, more refined species than the green Martians.
- **Woola:** The Martian hound accompanying the protagonist.
````

## Raw Response
````text
[[FILMCREATOR_PACKET]]

task: character_extraction

version: 1

character_index_markdown:

[[SECTION character_index_markdown]]

# Character Index - Chapter CH008

- [Protagonist](#protagonist)
- [Sola](#sola)
- [Green Martian Warriors](#green-martian-warriors)
- [The Prisoner](#the-prisoner)
- [Woola](#woola)

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: protagonist

canonical_character_id: CH002 Protagonist

aliases: Narrator

is_fully_identified: false

manual_description_required: true

manual_description_reason: No physical description or visual traits provided in this chapter.

clarification_required: true

clarification_reason: Physical appearance and species are unknown.

clarification_question: What is the protagonist's physical appearance, height, and species?

[[SECTION markdown]]

# Protagonist
**Role:** Observer/Narrator

**Status:** Physically Present

**Physical Description:** 
Unknown. The character observes the battle from a window and interacts with Sola and Woola, but no visual details are provided in this chapter.

**Uncertainty Notes:** 
Complete lack of visual data for image generation.

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: sola

canonical_character_id: CH003 Sola

aliases: 

is_fully_identified: false

manual_description_required: true

manual_description_reason: No physical description provided in this chapter.

clarification_required: true

clarification_reason: Physical appearance is not established in the text.

clarification_question: What does Sola look like?

[[SECTION markdown]]

# Sola
**Role:** Companion to Protagonist

**Status:** Physically Present

**Physical Description:** 
Unknown. Accompanies the protagonist during the departure from the city.

**Uncertainty Notes:** 
No visual traits or costume details provided.

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: green_martian_warriors

canonical_character_id: CH005 Green Martians

aliases: Martian warriors

is_fully_identified: true

manual_description_required: false

manual_description_reason: 

clarification_required: false

clarification_reason: 

clarification_question: 

[[SECTION markdown]]

# Green Martian Warriors
**Role:** Combatants/Lovers of the city

**Status:** Physically Present

**Physical Description:** 
Highly disciplined and organized military force. They demonstrate specialized marksmanship and use grappling hooks to secure vessels.

**Costume/Traits:** 
Disciplined, tactical, and highly coordinated in combat.

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: the_prisoner

canonical_character_id: CH009 Prisoner

aliases: Airship captive

is_fully_identified: true

manual_description_required: false

manual_description_reason: 

clarification_required: false

clarification_reason: 

clarification_question: 

[[SECTION markdown]]

# The Prisoner
**Role:** Captive from the airship fleet

**Status:** Physically Present

**Physical Description:** 
A beautiful, slender woman with copper-colored skin and black hair. Her form resembles Earthly women, suggesting a more refined species than the green Martians.

**Costume/Traits:** 
Slender silhouette, copper skin, black hair. Expresses silent gestures for help, followed by dejection and contempt.

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: woola

canonical_character_id: CH006 Woola

aliases: Martian hound

is_fully_identified: true

manual_description_required: false

manual_description_reason: 

clarification_required: false

clarification_reason: 

clarification_question: 

[[SECTION markdown]]

# Woola
**Role:** Companion/Pet

**Status:** Physically Present

**Physical Description:** 
A Martian hound accompanying the protagonist.

**Uncertainty Notes:** 
Specific breed or visual details are not described in this chapter, but identity as a "Martian hound" is established.

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
