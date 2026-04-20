# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-20T01:00:17.280684+00:00
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

Chapter id: CH009

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

Visual Continuity Facts:
- Warrior presents full accouterments and arms at the building doorway.
- Women remodel armor trappings to fit narrator's proportions in sleeping quarters.
- Narrator practices weapons on the plaza with young Martians under Sola's instruction.
- Nighttime conversations occur in sleeping quarters among females, Woola, and the narrator.
- Narrator observes guards treating the prisoner harshly during transport to audience chamber.

Broad Story Summary:
- Narrator learns Martian language rapidly due to familiarity with earthly concepts.
- Sola expresses concern regarding narrator's interaction with the prisoner, hinting at jealousy or protective feelings.
- Women explain Martian society: women produce all goods/weapons and train in defense; men handle strategy and laws.
- Discussions reveal plans for the prisoner's death/exhibition at Thark games before Tal Hajus.
- Narrator realizes Sola hates cruelty and decides to ask her for help escaping later.
````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
task: environment_extraction
version: 1

[[SECTION environment_index_markdown]]
# Environment Index - Chapter CH009

## Building Doorway
- Role: Primary setting for Warrior's arrival
- Geography: Exterior entrance to main building structure
- Lighting: Natural daylight with architectural shadows
- Atmosphere: Formal, ceremonial tone
- Scale: Large doorway framing full figure presentation
- Anchors: Doorframe, Warrior accouterments display

## Sleeping Quarters
- Role: Primary setting for intimate conversations and armor work
- Geography: Interior private chambers
- Lighting: Soft interior lighting, nighttime ambiance
- Atmosphere: Intimate, protective, feminine space
- Scale: Personal quarters with multiple occupants
- Anchors: Armor trappings, sleeping arrangements, conversation circle

## Plaza
- Role: Secondary setting for weapons training
- Geography: Open exterior plaza space
- Lighting: Daylight with open sky visibility
- Atmosphere: Training-focused, instructional environment
- Scale: Large open area accommodating multiple trainees
- Anchors: Weapons display, young Martian trainees, Sola's instruction station

## Audience Chamber
- Role: Transit setting for prisoner transport
- Geography: Interior formal chamber space
- Lighting: Dim interior with harsh treatment atmosphere
- Atmosphere: Oppressive, cruel, intimidating
- Scale: Large formal space with guard presence
- Anchors: Prisoner display area, guard positions, transport route

## Thark Games Arena (Future Reference)
- Role: Future primary setting for prisoner exhibition
- Geography: Large arena space for public spectacle
- Lighting: Variable lighting for dramatic presentation
- Atmosphere: Anticipated cruelty and entertainment
- Scale: Massive arena accommodating audience
- Anchors: Exhibition platform, Tal Hajus seating area

[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: building_doorway

[[SECTION markdown]]
# Building Doorway

## Environment Role
Primary setting for Warrior's ceremonial arrival and accouterment presentation.

## Architecture and Geography
Exterior entrance to main building structure with large doorway framing full figure presentation. Formal architectural elements suggest importance of the space.

## Lighting and Atmosphere
Natural daylight conditions with architectural shadows creating depth. Formal, ceremonial tone established through lighting contrast.

## Scale and Anchors
Large doorway scale accommodates full Warrior figure display. Doorframe serves as primary visual anchor for accouterments presentation.

## Descriptive Noun Phrases
- Ceremonial entrance structure
- Full-figure presentation space
- Accouterment display area
- Architectural shadow framing
- Formal doorway threshold

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: sleeping_quarters

[[SECTION markdown]]
# Sleeping Quarters

## Environment Role
Primary setting for intimate conversations, armor work, and nighttime discussions among females.

## Architecture and Geography
Interior private chambers designed for personal quarters with multiple occupants. Space accommodates armor trappings and conversation circle arrangements.

## Lighting and Atmosphere
Soft interior lighting conditions with nighttime ambiance. Intimate, protective atmosphere established through feminine space design.

## Scale and Anchors
Personal quarters scale with sleeping arrangements visible. Armor trappings and conversation circle serve as primary visual anchors.

## Descriptive Noun Phrases
- Private interior chamber space
- Armor work station area
- Nighttime conversation circle
- Feminine protective environment
- Sleeping arrangement cluster

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: plaza

[[SECTION markdown]]
# Plaza

## Environment Role
Secondary setting for weapons training and instructional activities under Sola's guidance.

## Architecture and Geography
Open exterior plaza space with large open area accommodating multiple trainees. Sky visibility provides natural orientation reference.

## Lighting and Atmosphere
Daylight conditions with open sky visibility. Training-focused atmosphere established through instructional environment design.

## Scale and Anchors
Large open area scale accommodates weapons display and young Martian trainees. Sola's instruction station serves as primary anchor point.

## Descriptive Noun Phrases
- Open exterior plaza space
- Weapons training area
- Instructional station platform
- Sky-visible orientation space
- Trainee gathering zone

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: audience_chamber

[[SECTION markdown]]
# Audience Chamber

## Environment Role
Transit setting for prisoner transport and harsh treatment display during movement to formal chamber.

## Architecture and Geography
Interior formal chamber space with large formal area accommodating guard presence. Transport route through oppressive interior design.

## Lighting and Atmosphere
Dim interior lighting conditions with harsh treatment atmosphere. Oppressive, cruel, intimidating environment established through spatial design.

## Scale and Anchors
Large formal space scale with prisoner display area visible. Guard positions and transport route serve as primary visual anchors.

## Descriptive Noun Phrases
- Formal chamber interior space
- Prisoner transport corridor
- Guard position stationing area
- Oppressive treatment zone
- Audience chamber threshold

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: thark_games_arena_future

[[SECTION markdown]]
# Thark Games Arena (Future Reference)

## Environment Role
Future primary setting for prisoner exhibition and public spectacle before Tal Hajus.

## Architecture and Geography
Large arena space designed for public spectacle with massive area accommodating audience seating. Exhibition platform for prisoner display.

## Lighting and Atmosphere
Variable lighting conditions for dramatic presentation anticipated. Cruelty and entertainment atmosphere expected through spatial design.

## Scale and Anchors
Massive arena scale accommodating full audience capacity. Exhibition platform and Tal Hajus seating area serve as primary anchors.

## Descriptive Noun Phrases
- Public spectacle arena space
- Prisoner exhibition platform
- Audience seating configuration
- Dramatic lighting zone
- Tal Hajus viewing section

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
