# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-20T00:49:51.156710+00:00
- task: character_extraction

## System Prompt
````text
You are FilmCreator's local authoring analyst.
Work like a careful local planning assistant for chapter analysis and shot-prep authoring.
Return exactly one FILMCREATOR packet in Markdown.
Do not return JSON.
Do not use markdown fences.
Do not add commentary before or after the packet.
Preserve uncertainty instead of inventing hidden facts.
Prefer short, concrete section bodies over long prose.
Follow the requested headings and record fields exactly.
When asked to write Markdown file contents, place the complete file body inside the requested SECTION tags.
When asked to extract render-facing facts, focus on visible, continuity-relevant details.
If information is missing, say so briefly instead of guessing.
````

## User Prompt
````text
Project slug: princess_of_mars_test

Chapter id: CH004

Task: extract visible and referenced characters into a character index plus one Markdown file per character.

Return exactly one Markdown packet using this outer envelope:
[[FILMCREATOR_PACKET]]
task: character_extraction
version: 1

[[SECTION character_index_markdown]]
...character_index_markdown content...
[[/SECTION]]

Repeat one FILMCREATOR_RECORD block for every extracted item of that type.

[[FILMCREATOR_RECORD]]
type: character
asset_id: <value>
canonical_character_id: <value>
aliases: <value>
is_fully_identified: <value>
manual_description_required: <value>
manual_description_reason: <value>
clarification_required: <value>
clarification_reason: <value>
clarification_question: <value>

[[SECTION markdown]]
...markdown content...
[[/SECTION]]
[[/FILMCREATOR_RECORD]]
[[/FILMCREATOR_PACKET]]



Important rules:

- if a character does not have enough physical or visual description in the supplied material to support dependable later image generation, set manual_description_required to true

- explain exactly why in manual_description_reason

- do not guess ornate missing details just to avoid the flag

- if the chapter names a character without enough stable identification, set is_fully_identified to false

- use aliases for alternate names or partial labels seen in the chapter

- if the character might already exist under another name or is too weakly identified, set clarification_required to true and ask a targeted question

- if clarification is not required, still include clarification_reason and clarification_question as empty values

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

# Chapter Summary: CHAPTER IV - A PRISONER

## Narrative Breakdown
### Scene 1: Arrival at the City
- **Action:** The party travels from the bottom of a dead sea, gaining the foot of mountains and traversing a narrow gorge.
- **Setting:** They reach an open valley with a low table land at the extremity containing an enormous city.
- **Entry:** Enter by what appears to be a ruined roadway leading out from the city but ending abruptly in broad steps.

### Scene 2: Audience with the Chieftain
- **Location:** A magnificent white marble building (low, enormous area) with a main entrance of some hundred feet width and a huge canopy.
- **Interior:** Enormous chamber encircled by galleries, dotted with highly carved wooden desks and chairs.
- **Assembly:** About forty or fifty male Martians assembled around the steps of a rostrum; an enormous warrior (Chieftain) squats on the platform.
- **Interaction:** Tars Tarkas (vice-chieftain) explains the capture; Chieftain addresses the narrator. Narrator replies in English to show misunderstanding.

### Scene 3: Physical Demonstration & Fight
- **Demonstration:** Martians command "sak" (jumping). Narrator demonstrates jumping ability, clearing 150 feet and landing squarely.
- **Conflict:** Hungry/thirsty gestures ignored commands; narrator skips/flits about like a grasshopper, bruising himself.
- **Fight:** A towering fellow laughs at misfortunes; narrator punches him squarely to the jaw. He falls like a felled ox.
- **Resolution:** Other Martians break into wild peals of laughter and applause (manifestation of approbation). Tars Tarkas advances with an arm offered.

### Scene 4: Feeding & Meeting Sola
- **Action:** Narrator ignores commands to "sak," motions to mouth/stomach.
- **Transition:** Tars Tarkas calls a young female; narrator accompanies her across the plaza toward a large building.
- **Location:** Spacious chamber in one of the buildings fronting on the plaza, well lighted by large windows.
- **Decor:** Beautifully decorated with mural paintings and mosaics; litter of silks and furs upon the floor.

### Scene 5: Creature Introduction
- **Signal:** Sola makes a peculiar hissing sound signaling someone in an adjoining room.
- **Creature:** A ten-legged waddler squats down before the girl like an obedient puppy.
- **Appearance:** Size of a Shetland pony; head bears slight resemblance to a frog (jaws equipped with three rows of long, sharp tusks).

## Visual Continuity Facts
- **Architecture:** White marble building with gold and brilliant stones inlay; main entrance 100 feet wide.
- **Furniture:** Highly carved wooden desks and chairs sized for human beings (too small for Martians).
- **Characters:** Tars Tarkas (green skin, ornaments); Chieftain (enormous warrior, white fur cape with scarlet silk lining); Sola (light olive-green, 8 feet tall).
- **Materials:** Gleaming white marble, gold, brilliant stones, wood, scarlet silk, leather trappings.
- **Colors:** Green skin (olive), white fur, scarlet silk, light olive-green females/children.
- **Creature:** Ten-legged waddler; frog-like head; three rows of long sharp tusks.
````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
task: character_extraction
version: 1

[[SECTION character_index_markdown]]
| Character Name | Role/Title | Physical Presence | Identification Status |
| :--- | :--- | :--- | :--- |
| Narrator | Protagonist / Prisoner | Physically Present | Fully Identified (Role) |
| Tars Tarkas | Vice-Chieftain | Physically Present | Fully Identified (Name) |
| Chieftain | Enormous Warrior | Physically Present | Fully Identified (Title) |
| Sola | Young Female / Guide | Physically Present | Fully Identified (Name) |
[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: narrator
canonical_character_id: Narrator
aliases: The Prisoner, I
is_fully_identified: true
manual_description_required: true
manual_description_reason: Source text lacks specific physical traits (hair, eyes, facial features) required for consistent image generation.
clarification_required: false
clarification_reason: 
clarification_question: 

[[SECTION markdown]]
# Narrator Character File

## Role and Presence
The protagonist of the chapter, referred to as "Narrator," "I," or "The Prisoner." Physically present throughout all scenes in the city.

## Visual Continuity
- **Species:** Human (implied by English language usage and size comparison).
- **Scale:** Standard human dimensions relative to Martians.
- **Physical Traits:** Specific features (hair color, eye color, facial structure) are not described in the source text.
- **Attire:** Not specified beyond general clothing implied for a traveler.

## Uncertainty Notes
This character record relies on role identification rather than detailed physical description. Image generation will require manual specification of facial features and attire to match the "Prisoner" persona without contradicting the sparse source material.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: tars_tarkas
canonical_character_id: Tars Tarkas
aliases: Vice-Chieftain
is_fully_identified: true
manual_description_required: true
manual_description_reason: Specific ornament details are not described beyond "ornaments," requiring manual specification for consistent rendering.
clarification_required: false
clarification_reason: 
clarification_question: 

[[SECTION markdown]]
# Tars Tarkas Character File

## Role and Presence
Vice-Chieftain of the Martian assembly. Physically present in the audience chamber, explaining the capture and offering assistance.

## Visual Continuity
- **Skin:** Green skin (olive tone).
- **Attire:** Wears ornaments (specific type/material not detailed).
- **Role Indicators:** Distinguished by rank within the assembly.

## Uncertainty Notes
While skin tone is specified, the nature of the "ornaments" is vague. Manual description is required to define jewelry style and material for accurate image generation.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: chieftain
canonical_character_id: Chieftain
aliases: Enormous Warrior, Martian Leader
is_fully_identified: true
manual_description_required: true
manual_description_reason: Exact scale and facial features are not detailed beyond "enormous," requiring manual specification for consistent rendering.
clarification_required: false
clarification_reason: 
clarification_question: 

[[SECTION markdown]]
# Chieftain Character File

## Role and Presence
The supreme leader of the Martian assembly, squatting on the rostrum platform. Addresses the narrator directly.

## Visual Continuity
- **Scale:** Enormous warrior (significantly larger than humans).
- **Attire:** White fur cape with scarlet silk lining.
- **Role Indicators:** Squats on the platform; commands attention.

## Uncertainty Notes
The term "enormous" implies large scale but lacks specific metric data. Facial features are not described. Manual description is required to define the extent of size and facial structure for image generation.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: sola
canonical_character_id: Sola
aliases: Young Female, Light Olive-Green Female
is_fully_identified: true
manual_description_required: true
manual_description_reason: Source text specifies skin tone and height but lacks facial feature details.
clarification_required: false
clarification_reason: 
clarification_question: 

[[SECTION markdown]]
# Sola Character File

## Role and Presence
Young female Martian, introduced by Tars Tarkas. Accompanies the narrator across the plaza to a spacious chamber.

## Visual Continuity
- **Skin:** Light olive-green.
- **Height:** 8 feet tall.
- **Role Indicators:** Young female; acts as a guide/introducer.

## Uncertainty Notes
While height and skin tone are specified, facial features (eyes, hair, mouth) are not described. Manual description is required to define these specific traits for accurate image generation.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]
````
