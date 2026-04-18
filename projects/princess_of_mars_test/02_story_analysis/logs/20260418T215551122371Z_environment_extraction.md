# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-18T21:55:51.122371+00:00
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

Chapter id: CH001

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

# Chapter Title
Chapter VIII - A Fair Captive from the Sky

# Scene 1: Return to City & Observation
**Action:** The procession returns to the city after the incubator ceremony. Orders are given for immediate retreat. Narrator climbs to an upper floor window to observe the cause of the sudden scurrying.
**Visuals:** Green Martians melting into building doorways like mist. View of valley and hills from window.
**Key Detail:** The narrator identifies a huge gray craft swinging over the crest of the nearest hill as the cause.

# Scene 2: Fleet Arrival & Battle Initiation
**Action:** Twenty gray ships appear, sailing slowly toward the city. Martians fire a terrific volley from building windows. Fleet returns fire with guns.
**Visuals:** Gray ships with banners and devices gleaming in sunlight. Figures crowding forward decks. Window firing positions.
**Key Detail:** The first volley catches ship crews unprepared. Bullets drop figures at explosions; banners dissolve in spurts of flame.

# Scene 3: Fleet Maneuver & Damage Assessment
**Action:** Fleet circles to position opposite the firing line, then retreats trailing off. Several craft are limping perceptibly. One ship receives the brunt of fire and seems entirely unmanned.
**Visuals:** Ships moving parallel to front, turning back. Depleted crews controlling damaged vessels. Erratic movement of the last ship.
**Key Detail:** The last ship is drifting some fifty feet above ground, helpless and unable to escape.

# Scene 4: Drifting Ship Rescue & Loot Operation
**Action:** Warriors rush to the plain to meet the drifting ship. They board with spears and grappling hooks, hauling it to ground. Systematic rifling of the vessel begins.
**Visuals:** Bodies of crew strewn about decks. Grappling hooks thrown out. Chariots requisitioned for transport. Loot includes arms, ammunition, silks, furs, jewels, stone vessels, water casks.
**Key Detail:** The ship is towed far out into the valley in a southwesterly direction after loot removal.

# Scene 5: Ship Fire & Funeral Pyre
**Action:** Warriors empty carboys upon dead bodies and decks. Last warrior throws missile back onto vessel, causing flame spurt. Guy ropes released; ship soars majestically into air as funeral pyre.
**Visuals:** Decks and upper works a mass of roaring flames. Ship drifting to southeast, rising higher. Dim vistas of distance.
**Key Detail:** The sight is described as an awe-inspiring floating funeral pyre typifying the life story of the strange creatures.

# Scene 6: Narrator's Reaction & Prisoner Discovery
**Action:** Narrator descends to street, feeling depressed by the defeat. Sola rushes up. Cavalcade returns to plaza. Narrator enters plaza and catches glimpse of prisoner being dragged into building.
**Visuals:** Narrator emerging upon street. Throng of Martians in plaza. Building portal where prisoner is dragged.
**Key Detail:** The prisoner is a slender, girlish figure similar to earthly women, wearing highly wrought ornaments but otherwise naked.

# Scene 7: The Princess Close-Up & Interaction
**Action:** Close-up of the prisoner (Dejah Thoris). Her eyes meet narrator's. She makes a sign with free hand. Look of hope fades into dejection, loathing, and contempt. She is dragged away.
**Visuals:** Oval face, coal black waving hair, light reddish copper skin, crimson cheeks, ruby lips. Eyes large and lustrous.
**Key Detail:** Narrator realizes he did not answer her signal for succor and protection due to ignorance of Martian customs.

# Scene 8: Aftermath & Safety Measures
**Action:** Lorquas Ptomel remains at deserted city until danger passed. Fear of return attack by air craft prevents recommencement of homeward march for a week.
**Visuals:** Deserted city environment. Plaza gathering.
**Key Detail:** The city remains occupied to avoid open plains with caravan of chariots and children due to fear of fleet return or reinforcements.
````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
task: environment_extraction
version: 1
[[SECTION environment_index_markdown]]
# Environment Index - Chapter 1
- City Plaza & Exterior
- Martian Valley & Hills
[[/SECTION]]
[[FILMCREATOR_RECORD]]
type: environment
asset_id: city_plaza_exterior
[[SECTION markdown]]
Role: Primary setting for action and aftermath.
Architecture: Multi-story buildings with doorways, windows, portals. Paved plaza and streets.
Lighting: Bright sunlight casting shadows on buildings. Dim interiors visible through windows.
Atmosphere: Initially bustling (procession), then deserted after battle. Smoke from burning ship.
Scale: Urban structures towering over the plaza.
Anchors: Building doorways, upper floor windows, building portals.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]
[[FILMCREATOR_RECORD]]
type: environment
asset_id: martian_valley_hills
[[SECTION markdown]]
Role: Secondary setting for ship movement and burning.
Architecture: Open plain, hills with crests.
Lighting: Sunlight gleaming on ships, dim vistas of distance.
Atmosphere: Vast, open, awe-inspiring.
Scale: Ship drifting fifty feet above ground, rising higher into air.
Anchors: Hill crest, valley floor, distant horizon.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]
[[/FILMCREATOR_PACKET]]
````
