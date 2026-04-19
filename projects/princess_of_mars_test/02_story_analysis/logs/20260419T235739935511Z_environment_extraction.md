# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-19T23:57:39.935511+00:00
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

Chapter id: CH006

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

## Story Summary
The protagonist is captured by a bull ape creature while pinned to the ground. Another bull ape attacks with a stone cudgel, intending to brain him. The beast intervenes, fighting the first ape. The second ape arrives and fights the beast, choking it on its throat. The protagonist kills the first ape with the cudgel. He prepares to flee but sees the dying beast appealing for protection. He fights the enraged second bull ape using earthly tactics. Tars Tarkas, Sola, and warriors arrive through the doorway and applaud his bravery. A warrior attempts to shoot the beast; the protagonist stops him by striking up the arm. They return to the plaza with the beast following close at heel.

## Visual Continuity
The bull apes are 10-15 feet tall with close eyes, high lateral ears, and gorilla-like snouts. The fight involves a stone cudgel swinging in an arc. The beast has bulging eyes and blood flowing from its nostrils during the struggle. The protagonist uses earthly tactics (fist to chin, smash to stomach). Tars Tarkas and Sola enter through the doorway of the chamber. The warrior draws an evil looking pistol from its holster. The bullet striking the wooden casing of the window explodes, blowing a hole completely through the wood and masonry.
````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
task: environment_extraction
version: 1

[[SECTION environment_index_markdown]]
# Environment Index - Princess of Mars Chapter CH006

## Chamber/Room (Primary Setting)
- Role: Primary fight setting where protagonist is captured and battles bull apes
- Architecture: Chamber with doorway entrance, windows with wooden casings, masonry walls
- Lighting: Interior lighting with window light sources
- Atmosphere: Tense combat environment, blood-stained struggle
- Scale: Human-sized interior space, 10-15 foot tall bull apes operate within
- Anchors: Doorway (entry point for Tars Tarkas/Sola), wooden window casings

## Plaza (Secondary Setting)
- Role: Transit/return setting where protagonist and companions arrive after fight
- Architecture: Open plaza space, exterior environment
- Lighting: Natural daylight
- Atmosphere: Public gathering space, celebratory mood with warriors applauding
- Scale: Larger open area compared to chamber interior
- Anchors: Entry from chamber doorway, beast following at heel

[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: chamber

[[SECTION markdown]]
# Chamber Environment - Primary Fight Setting

## Role
Primary setting for the bull ape combat sequence where protagonist is captured and engages in earthly tactics against multiple 10-15 foot tall bull apes.

## Architecture/Geography
Interior chamber space with doorway entrance point, windows featuring wooden casings that can be struck through (bullet explosion creates hole through wood and masonry), solid masonry walls forming the room structure.

## Lighting/Atmosphere
Interior ambient lighting supplemented by window light sources creating directional illumination during combat. Blood-stained atmosphere from struggle, tense combat environment with high lateral ears of bull apes visible in close-up shots.

## Scale/Cues
Human-sized interior proportions accommodating 10-15 foot tall gorilla-like creatures. Doorway serves as primary entry anchor for Tars Tarkas and Sola arrival sequence. Window casings provide secondary visual anchors during combat exchanges.

## Descriptive Noun Phrases
- Interior chamber with wooden window casings
- Doorway entrance point for warrior arrivals  
- Masonry walls forming room structure
- Blood-stained combat environment
- Window casing explosion point
- Bull ape close-up viewing area

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: plaza

[[SECTION markdown]]
# Plaza Environment - Secondary Return Setting

## Role
Secondary transit setting where protagonist, Tars Tarkas, Sola, and warriors return after combat sequence. Public gathering space with celebratory atmosphere as warriors applaud protagonist's bravery.

## Architecture/Geography
Open exterior plaza space accessible from chamber doorway. Larger open area compared to interior chamber, allowing beast to follow at heel through the environment.

## Lighting/Atmosphere
Natural daylight illumination creating bright exterior conditions. Celebratory mood atmosphere with applause and warrior presence. Public gathering space characteristics.

## Scale/Cues
Larger open plaza proportions accommodating multiple warriors and beast movement. Entry point from chamber doorway serves as transition anchor between interior fight setting and exterior return sequence.

## Descriptive Noun Phrases
- Open exterior plaza gathering space
- Warrior applause area
- Beast following at heel path
- Chamber doorway entry transition
- Public celebration environment
- Natural daylight exterior conditions

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
