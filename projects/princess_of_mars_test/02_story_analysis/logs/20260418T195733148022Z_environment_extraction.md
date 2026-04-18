# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-18T19:57:33.148022+00:00
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

# Chapter Summary: A Fair Captive from the Sky

## Event Sequence
1.  **Retreat Order:** Following the incubation ceremony, orders are given for an immediate return to the city. The green Martians melt into buildings within three minutes.
2.  **Fleet Arrival:** From a window, the protagonist observes twenty gray air vessels swinging low above the ground toward the valley. Each carries a banner and odd devices.
3.  **Fire Exchange:**
    *   Green Martians fire a volley from building windows first.
    *   The fleet returns fire with high accuracy; figures drop at bullet explosions, banners dissolve in flames.
    *   Fleet damage is evident (limping vessels) after twenty minutes.
4.  **Fleet Retreat & Capture:** The fleet trails off. One vessel drifts helpless, unmanned, and damaged. Warriors rush to capture it before it hits the ground.
5.  **Looting & Burning:** Warriors search the vessel for loot (arms, jewels, water). After removal, they tow it away, then empty carboys over the dead sailors and burn the vessel. The ship drifts southeast as a funeral pyre.
6.  **Prisoner Discovery:** As the protagonist descends to the street, Sola rushes up. A prisoner is being dragged into a building by green Martian females.
7.  **Prisoner Description:** The figure is slender and girlish, similar to earthly women. Features include an oval face, coal black waving hair, light reddish copper skin, and ruby lips. She is naked except for ornaments.
8.  **Emotional Impact:** The prisoner makes a sign of appeal (unanswered by the protagonist). Her expression shifts from hope to dejection and loathing as she is dragged away.

## Visual Continuity Notes
*   **Protagonist's Viewpoint:** Observes fleet arrival and burning ship from an upper window/balcony.
*   **Prisoner Entry:** Observed from street level as she enters the building portal.
*   **Martian Reaction:** Warriors rush to roofs to cover the possibility of return attack or reinforcements.
````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
task: environment_extraction
version: 1

[[SECTION environment_index_markdown]]
# Environment Index - Chapter CH001

## Primary Settings
- **upper_window_balcony** - Protagonist observation point for fleet arrival and burning ship
- **valley_ground** - Fleet arrival zone where air vessels swing low above ground

## Secondary Settings  
- **building_interior_portal** - Where Martians retreat into buildings, prisoner dragged through building portal
- **street_level** - Transit setting for protagonist descent, Sola's approach point

[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: upper_window_balcony

[[SECTION markdown]]
# Upper Window/Balcony Setting

## Environment Role
Primary observation and vantage point

## Architecture or Geography
Interior room with large windows and balcony overlooking valley. Building facade visible from exterior perspective.

## Lighting and Atmosphere Cues
Interior light looking outward to daylight scene. Fleet appears as distant gray shapes against sky. Burning ship creates orange/red glow visible through glass. Smoke trails drift across window view.

## Scale Cues and Recurring Environmental Anchors
Protagonist positioned at elevated height observing fleet arrival from above. Window frame provides visual boundary for observation. Balcony railing marks edge of interior space.

## Descriptive Noun Phrases
- elevated interior observation point
- large glass windows overlooking valley
- balcony with exterior view
- interior room looking outward to daylight scene
- window frame as visual boundary
- distant fleet visible through glass
- burning ship glow through window
- smoke trails across window view

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: valley_ground

[[SECTION markdown]]
# Valley Ground Setting

## Environment Role
Primary fleet arrival and activity zone

## Architecture or Geography
Open valley floor with buildings clustered along edges. Ground level where air vessels swing low above surface. Building portals visible at valley perimeter.

## Lighting and Atmosphere Cues
Daylight scene viewed from elevated position. Fleet appears as gray shapes against sky. Burning vessel creates funeral pyre glow on ground. Smoke rises from burning ship drifting southeast.

## Scale Cues and Recurring Environmental Anchors
Fleet vessels swing low above ground level toward valley center. Buildings cluster at valley edges providing reference points. Ground surface visible beneath aerial activity.

## Descriptive Noun Phrases
- open valley floor with building clusters
- ground level below aerial fleet
- valley perimeter with building portals
- daylight scene viewed from elevation
- burning vessel funeral pyre on ground
- smoke rising from burning ship
- aerial fleet against sky backdrop

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: building_interior_portal

[[SECTION markdown]]
# Building Interior/Portal Setting

## Environment Role
Secondary setting for retreat and prisoner movement

## Architecture or Geography
Building interior spaces with doors and portals. Building facade visible from exterior. Doorways leading into buildings where Martians retreat and prisoners dragged.

## Lighting and Atmosphere Cues
Interior light dimmer than exterior daylight. Urgent atmosphere of retreat and capture. Green Martian figures moving through building interiors. Burning vessel glow visible from windows.

## Scale Cues and Recurring Environmental Anchors
Building interior spaces at street level. Doorways serve as transition points between exterior and interior. Building portal marks entry point for prisoner movement.

## Descriptive Noun Phrases
- building interior with doors and portals
- building facade visible from exterior
- doorway leading into building interior
- interior space at street level
- building portal as entry point
- green Martian figures in building interior
- urgent atmosphere of retreat and capture

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: street_level

[[SECTION markdown]]
# Street Level Setting

## Environment Role
Transit setting for protagonist descent and Sola's approach

## Architecture or Geography
Street level with buildings at ground floor. Building portals visible at street level. Ground surface where protagonist descends to street.

## Lighting and Atmosphere Cues
Daylight scene viewed from above looking down. Street level appears below elevated observation point. Burning vessel glow visible from street perspective.

## Scale Cues and Recurring Environmental Anchors
Protagonist descends from elevated position to street level. Building portals at ground floor serve as entry points. Street surface marks transition from interior to exterior.

## Descriptive Noun Phrases
- street level with buildings at ground floor
- building portals visible at street level
- ground surface below elevated observation
- daylight scene viewed from above looking down
- protagonist descent to street level
- burning vessel glow from street perspective

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
