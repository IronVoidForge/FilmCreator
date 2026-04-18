# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-18T18:02:11.402255+00:00
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

# Chapter Label
Chapter VIII - A Fair Captive from the Sky

# Story Summary
The procession returns home after the incubator ceremony but is ordered back immediately upon seeing a fleet of airships approaching. The narrator observes from an upper floor window as twenty gray-painted vessels sail toward the city. Green Martian warriors fire a volley from building windows, engaging the ships. The fleet returns fire and maneuvers to complete circles before retreating. One ship is disabled and drifting southeast. Warriors chase it, board with spears and grappling hooks, and loot the vessel of arms, jewels, water, and food. They empty carboys onto the dead crew and burn the ship as a funeral pyre. The narrator witnesses the burning from the roof until it drifts into the distance. Depressed by the defeat of a kindred people's forces, he descends to the street. In the plaza, he sees a prisoner being dragged into a building. He catches a glimpse of her before she enters: a slender, girlish figure with coal black hair and reddish copper skin. She looks at him with hope then dejection as she is dragged away.

# Visual Continuity Facts
- **Location:** Upper floor window (observation point), Plaza (encounter point).
- **Martian Warriors:** Green skin, erect walking, wear spears, banners, ornaments.
- **Airships:** Gray-painted, long, low, twenty total, carry strange devices on prow/stem.
- **Combat Visuals:** Figures drop at bullet explosions; banners dissolve in flame; ships swing broadside.
- **Prisoner Appearance:** Slender girlish figure, oval face, finely chiseled features, large lustrous eyes, coal black waving hair (loose coiffure), light reddish copper skin, crimson cheeks, ruby lips.
- **Attire:** Destitute of clothes, entirely naked save for highly wrought ornaments.
- **Height Comparison:** Prisoner considerably less than half as tall as green Martian warriors.
- **Movement:** Walks erect upon two legs; dragged by females into building.
- **Environment:** Deserted city buildings, open ground/plaza, valley/hills vista.
]]
````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
task: environment_extraction
version: 1

[[SECTION environment_index_markdown]]
# Environment Index - Chapter VIII

## Primary Observation Setting
- Upper floor window (narrator's vantage point)

## Transit/Encounter Setting  
- Plaza (public gathering space, prisoner encounter location)

## Combat/Background Setting
- Deserted city buildings (urban decay environment)
- Valley/hills vista (distant landscape backdrop)

[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: upper_floor_window

[[SECTION markdown]]
# Upper Floor Window Environment

## Environment Role
Primary observation setting for narrator's vantage point during fleet engagement sequence.

## Architecture and Geography
Upper floor interior space with window opening to exterior cityscape. Elevated position above street level, providing panoramic view of approaching airships and distant valley terrain.

## Lighting and Atmosphere Cues
Interior lighting suggests daytime conditions with natural light filtering through window frame. Exterior view shows clear visibility of gray-painted vessels against sky backdrop. Atmospheric tension conveyed through narrator's elevated perspective during combat sequence.

## Scale Cues and Environmental Anchors
Window frame serves as primary architectural anchor. Elevated position allows observation of: twenty airships at distance, green Martian warriors on building facades, burning ship drifting southeast across valley floor. Interior space provides intimate contrast to expansive exterior battlefield view.

## Descriptive Noun Phrases for Render-Facing Prompts
- elevated interior observation point
- window frame architectural anchor
- panoramic cityscape vista
- daylight natural illumination
- interior-exterior visual boundary
- narrator's vantage position
- upper floor residential space
- clear sky visibility conditions

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: plaza_encounter_space

[[SECTION markdown]]
# Plaza Encounter Space Environment

## Environment Role
Transit and encounter setting for public gathering space where prisoner is dragged into building.

## Architecture and Geography
Open ground/plaza within deserted city buildings. Public square or town center space with multiple building facades surrounding open area. Ground level position accessible from street, serving as transition zone between interior buildings and exterior valley vista.

## Lighting and Atmosphere Cues
Daylight conditions with natural illumination across open plaza surface. Atmospheric weight conveyed through prisoner's dejection and narrator's depression following fleet defeat. Open space allows visibility of distant burning ship while maintaining intimate encounter focus.

## Scale Cues and Environmental Anchors
Plaza ground plane serves as primary spatial anchor. Surrounding building facades provide vertical boundaries. Height comparison between green Martian warriors (erect walking) and prisoner (considerably less than half their height) establishes scale reference within open space. Distant valley/hills vista visible beyond plaza perimeter.

## Descriptive Noun Phrases for Render-Facing Prompts
- open ground public square
- deserted city plaza space
- building facade boundaries
- daylight natural illumination
- transition zone between interior-exterior
- prisoner encounter location
- street level gathering area
- distant valley vista visibility

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: deserted_city_buildings

[[SECTION markdown]]
# Deserted City Buildings Environment

## Environment Role
Combat and observation setting for urban decay environment during fleet engagement sequence.

## Architecture and Geography
Multiple building structures within city layout showing signs of abandonment or destruction. Building facades serve as elevated positions for green Martian warriors firing volleys from windows. Urban architecture provides vertical elements contrasting with horizontal airship movement across sky.

## Lighting and Atmosphere Cues
Daylight conditions with natural illumination across building surfaces. Atmospheric tension conveyed through combat visuals: figures dropping at bullet explosions, banners dissolving in flame, ships swinging broadside. Building interiors suggest abandonment while exteriors show active engagement during fleet battle.

## Scale Cues and Environmental Anchors
Building facades serve as primary vertical anchors for warrior positions. Window openings provide elevated firing positions. Height comparison between green Martian warriors (erect walking) and prisoner establishes scale reference within urban environment. Distant valley/hills vista visible beyond city perimeter provides landscape context.

## Descriptive Noun Phrases for Render-Facing Prompts
- abandoned urban architecture
- building facade vertical elements
- window opening elevated positions
- daylight natural illumination
- combat engagement surfaces
- deserted city structures
- urban decay environment
- distant valley vista visibility

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: valley_hills_vista

[[SECTION markdown]]
# Valley Hills Vista Environment

## Environment Role
Background landscape setting providing distant terrain context for fleet engagement sequence.

## Architecture and Geography
Distant valley floor with hills forming natural landscape backdrop. Open terrain visible from upper floor window and plaza positions. Natural topography provides expansive view of burning ship drifting southeast across valley floor before retreating into distance.

## Lighting and Atmosphere Cues
Daylight conditions with clear visibility across valley terrain. Atmospheric depth conveyed through distant ship movement across valley floor. Landscape vista provides scale reference for fleet engagement sequence, showing burning ship's journey from combat zone to distant horizon.

## Scale Cues and Environmental Anchors
Valley floor serves as primary horizontal anchor for distant ship movement. Hills form natural landscape boundaries providing vertical context. Distant position allows observation of burning ship's complete journey across valley terrain before disappearing into distance. Interior observation points (upper floor window, plaza) frame vista through architectural openings.

## Descriptive Noun Phrases for Render-Facing Prompts
- distant valley floor terrain
- hills natural landscape boundaries
- expansive view conditions
- daylight clear visibility
- burning ship journey path
- horizon distance reference
- landscape backdrop environment
- interior-exterior vista framing

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
