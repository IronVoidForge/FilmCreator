# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-20T04:07:08.267546+00:00
- task: environment_extraction

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

Chapter id: CH022

Task: extract environment families into an environment index plus one Markdown file per environment family.

Return exactly one Markdown packet using this outer envelope:
[[FILMCREATOR_PACKET]]
task: environment_extraction
version: 1

[[SECTION environment_index_markdown]]
...environment_index_markdown content...
[[/SECTION]]

Repeat one FILMCREATOR_RECORD block for every extracted item of that type.

[[FILMCREATOR_RECORD]]
type: environment
asset_id: <value>

[[SECTION markdown]]
...markdown content...
[[/SECTION]]
[[/FILMCREATOR_RECORD]]
[[/FILMCREATOR_PACKET]]



Asset id rules:

- lowercase snake_case

- stable across later reruns

- include stable environment families rather than every one-off mention

- prefer visible geography and atmosphere over literary abstraction



Each environment Markdown file should include:

- environment role such as primary, secondary, or transit setting

- architecture or geography

- lighting and atmosphere cues

- scale cues and recurring environmental anchors

- useful descriptive noun phrases for later render-facing prompt writing



Chapter summary:

# Chapter Summary: I FIND DEJAH (CH022)

## Scene 1: The Announcement in Than Kosis's Apartment
John Carter is stationed in a passage behind tapestries guarding the Jeddak. Dejah Thoris enters with four soldiers, surrounded by courtiers. She stands before Than Kosis and Sab Than, radiant with smiles. She announces her engagement to Sab Than, explaining that on Barsoom women may change their mind regarding heart matters but once a promise is made, it is final. She begs Than Kosis to forget her rash words from two days ago. Than Kosis accepts the assurance and orders a proclamation issued. Dejah leaves with her guards. Carter realizes his dream of happiness is dashed as she has given herself to the son of her people's enemy.

## Scene 2: The Fight in the Antechamber
Carter leaves his post to confront Dejah Thoris. He navigates the maze of winding corridors behind the tapestries and finds her antechamber. Four guardsmen stop him, demanding an order or password. Carter refuses, tapping his long-sword as his order. The guards draw weapons; a fight ensues. Carter kills three guardsmen quickly, then the fourth within ten seconds. Dejah Thoris stands at the door of her apartment watching throughout the conflict with Sola at her back. She does not recognize him initially.

## Scene 3: Confrontation and Refusal
Carter sheathes his bloody blade and approaches Dejah Thoris. He identifies himself as John Carter, her chieftain. She sways toward him but draws back in misery, stating it is too late because she has promised herself to Sab Than. She explains that on Barsoom, a promise given is final; the ceremonies are meaningless formalities. She states she cannot wed the man who slays her husband, even in self-defense, due to custom. Carter asks for forgiveness and declares his love again. Dejah explains the custom of two kinds of women in cities: those fought for to be asked in marriage, and those fought for but never asked. She bids him farewell as "chieftain that was."

## Scene 4: Escape from Zodanga
Carter realizes he is lost and must escape the city due to suspicion regarding the dead guardsmen. He follows a spiral runway to a lower floor and hides inside a huge hanging ornament in a hall. He overhears guards discussing the dead men and Than Kosis's search. Darkness falls outside. Carter slips from his hiding place onto a balcony overlooking an avenue. He jumps through a glass wall to the ground below, escaping the palace grounds as the court searches for him.
````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
task: environment_extraction
version: 1

[[SECTION environment_index_markdown]]
# Zodanga Palace Environment Index

## Environment Families Identified

| Asset ID | Name | Role | Key Features |
|----------|------|-------|--------------|
| than_kosis_antechamber | Than Kosis Antechamber | Primary Setting | Interior room with tapestries, guard positions, ceremonial space |
| palace_corridors | Palace Corridors | Transit Setting | Winding passages behind tapestries, maze-like structure |
| zodanga_grounds | Zodanga Palace Grounds | Escape Setting | Spiral runway, balcony, glass wall, hanging ornament |

## Environment Summary

The chapter takes place entirely within the Zodanga Palace complex in Zodanga city. Three distinct environment families emerge: the ceremonial antechamber where confrontations occur, the labyrinthine corridors connecting palace sections, and the exterior palace grounds used for escape sequences. All environments share Barsoomian palace architecture with tapestry barriers, spiral stairways, and ornamental hanging fixtures.

[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: than_kosis_antechamber

[[SECTION markdown]]
# Than Kosis Antechamber

## Environment Role
Primary setting for confrontation scenes between John Carter and Dejah Thoris

## Architecture and Geography
Interior room within Zodanga Palace featuring tapestry barriers, guard positions at doorways, ceremonial court space with Jeddak seating area. Room contains doorway leading to apartment interior, surrounded by courtiers and soldiers.

## Lighting and Atmosphere Cues
Indoor palace lighting creating formal ceremonial atmosphere. Tense courtly mood with radiant smiles contrasting underlying conflict. Darkness falls outside through windows during escape sequences.

## Scale Cues and Environmental Anchors
Medium-sized interior space with multiple guard positions anchoring perimeter. Doorway serves as primary focal point for confrontation scenes. Tapestry barriers create visual boundaries between spaces. Hanging ornament visible in adjacent hall.

## Descriptive Noun Phrases
Ceremonial antechamber, tapestry-guarded doorway, courtly interior space, palace guard positions, Jeddak seating area, formal confrontation room, ornamental hanging fixture, spiral runway entrance

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: palace_corridors

[[SECTION markdown]]
# Palace Corridors

## Environment Role
Transit setting connecting different palace sections and tapestry-guarded areas

## Architecture and Geography
Winding corridors behind tapestries forming maze-like structure. Spiral runway leading to lower floors. Multiple guard positions at corridor intersections. Tapestry barriers creating visual boundaries between palace sections.

## Lighting and Atmosphere Cues
Dim palace corridor lighting creating mysterious atmosphere. Maze-like quality with winding passages. Suspenseful mood during escape sequences as Carter navigates unfamiliar territory.

## Scale Cues and Environmental Anchors
Long winding passages with multiple turns and intersections. Spiral runway serves as primary navigation anchor. Tapestry barriers create recurring visual anchors throughout corridors. Hanging ornament visible in adjacent hall.

## Descriptive Noun Phrases
Winding corridor maze, tapestry-guarded passage, spiral runway entrance, palace interior walkway, guard-positioned corridor, labyrinthine palace structure, ornamental hanging fixture, lower floor access point

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: zodanga_grounds

[[SECTION markdown]]
# Zodanga Palace Grounds

## Environment Role
Escape setting for final sequence where Carter leaves palace grounds

## Architecture and Geography
Exterior palace grounds featuring spiral runway, balcony with glass wall, hanging ornament in hall. Avenue visible from balcony overlooking city below. Glass wall providing barrier between interior and exterior spaces.

## Lighting and Atmosphere Cues
Darkness falling outside creating dangerous escape conditions. Suspenseful atmosphere during court search for Carter. Glass wall transparency revealing ground below. Ornamental hanging fixture creates visual anchor point.

## Scale Cues and Environmental Anchors
Large exterior palace grounds with multiple levels accessible via spiral runway. Balcony serves as primary observation and escape point. Glass wall provides structural boundary between interior and exterior spaces. Hanging ornament visible from balcony.

## Descriptive Noun Phrases
Spiral runway, glass-walled balcony, palace exterior grounds, hanging ornament fixture, avenue overlooking city, multi-level palace structure, ornamental hall space, court search territory

[[/SECTION]]
[[/FILMCREATOR_RECORD]]
[[/FILMCREATOR_PACKET]]
````
