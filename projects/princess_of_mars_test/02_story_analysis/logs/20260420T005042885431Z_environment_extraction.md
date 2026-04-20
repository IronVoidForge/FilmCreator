# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-20T00:50:42.885431+00:00
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

Chapter id: CH004

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
task: environment_extraction
version: 1

[[SECTION environment_index_markdown]]
| Asset ID | Role | Description |
| :--- | :--- | :--- |
| martian_city_approach | Transit/Entry | Gorge, valley, ruined roadway, broad steps leading to city. |
| chieftain_audience_hall | Primary | White marble building interior with galleries and rostrum. |
| martian_plaza | Secondary | Open space connecting buildings in the city. |
| sola_private_chamber | Primary | Decorated room with murals, mosaics, and silks. |
[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: martian_city_approach

[[SECTION markdown]]
**Role:** Transit/Entry
**Architecture:** Narrow gorge transitioning to open valley; low table land at extremity; ruined roadway ending in broad steps.
**Lighting:** Natural daylight, mountain shadows.
**Atmosphere:** Arid, monumental scale, transition zone.
**Scale:** Enormous city silhouette against mountains; human-sized ruins vs massive landscape.
**Anchors:** Mountains, city extremity, abrupt steps.
**Noun Phrases:** Ruined roadway, broad steps, low table land, mountain foot.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: chieftain_audience_hall

[[SECTION markdown]]
**Role:** Primary
**Architecture:** Magnificent white marble building; main entrance 100 feet wide with huge canopy; interior encircled by galleries.
**Lighting:** Interior illumination reflecting off gleaming white marble and gold/brilliant stones inlay.
**Atmosphere:** Formal, imposing, assembly hall.
**Scale:** Enormous chamber; human-sized furniture (too small for Martians).
**Anchors:** Rostrum, highly carved wooden desks, scarlet silk lining on cape.
**Noun Phrases:** White marble building, gold inlay, galleries, rostrum, carved wooden desks.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: martian_plaza

[[SECTION markdown]]
**Role:** Secondary/Transit
**Architecture:** Open plaza between buildings fronting on the plaza.
**Lighting:** Daylight.
**Atmosphere:** Public transit space, gathering area.
**Scale:** Spacious enough for movement across; connects major buildings.
**Anchors:** Building facades, open ground.
**Noun Phrases:** Open plaza, building facades, transit space.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: sola_private_chamber

[[SECTION markdown]]
**Role:** Primary
**Architecture:** Spacious chamber in one of the buildings; large windows; decorated with mural paintings and mosaics.
**Lighting:** Well lighted by large windows.
**Atmosphere:** Luxurious, intimate, decorated.
**Scale:** Floor litter of silks and furs upon the floor.
**Anchors:** Mural paintings, mosaic floors, window light, silks and furs.
**Noun Phrases:** Spacious chamber, mural paintings, mosaics, silks and furs, large windows.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
