# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-19T04:11:40.129610+00:00
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

Chapter id: CH008

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

## Sequence of Events
1.  **Return Order:** Immediately after an incubator ceremony, orders are given for a hasty return to the city. The Martians melt into buildings within three minutes.
2.  **Airship Arrival:** From the window, the narrator observes twenty gray airships sailing toward the valley. Each carries banners and glowing devices.
3.  **Battle Initiation:** Green warriors fire a volley from building windows. The lead vessel returns fire, swinging broadside to complete a circle.
4.  **Martian Victory:** Martians target specific points (sighting apparatus, gunners, officers). Twenty minutes later, the fleet retreats with several craft limping.
5.  **Disabled Ship Recovery:** One ship is unmanned and drifting. Warriors rush to intercept it before it hits buildings south of their position. They board using spears and grappling hooks.
6.  **Looting & Burning:** Martians search the vessel, removing arms, silks, jewels, and food (including water). Afterward, they empty carboys over dead sailors and set the ship ablaze with a missile. The burning ship drifts southeast as a funeral pyre.
7.  **Prisoner Reveal:** Warriors drag a small figure from the ship. The narrator sees a human woman being dragged into a building by female Martians.

## Visual Details for Scene Decomposition
*   **Ship Appearance:** Gray, low profile, long shape, banners on stem/stern, glowing devices on prow.
*   **Martian Fire:** Terrific volley from windows; bullets dropping at explosion points; banners dissolving in flame.
*   **Prisoner Appearance:** Slender girlish figure, oval face, large lustrous eyes, coal black waving hair (loose coiffure), light reddish copper skin, crimson cheeks, ruby lips, destitute of clothes save for ornaments.
*   **Movement:** Ships swing majestically then erratically; warriors melt into mist; prisoner dragged roughly through portal.

## Narrative Beats & Emotional Arc
*   **Awe/Depression:** The narrator feels the defeat marks a kindred people's annihilation rather than a simple victory.
*   **Hope/Fear:** Upon seeing the human woman, the narrator experiences mingled hope and fear.
*   **Regret:** The narrator realizes he failed to answer her signal for succor due to ignorance of Martian customs.
````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
task: environment_extraction
version: 1

[[SECTION environment_index_markdown]]
# Environment Index - Chapter CH008

## Airship Fleet (asset_id: airship_fleet)
Gray low-profile vessels with banners on stem/stern and glowing devices on prow. Primary transit setting for Martian fleet operations.

## Martian Buildings/Valley (asset_id: martian_buildings_valley)
Building interiors where Martians melt into structures within three minutes. Secondary battle setting with window fire positions.

## Disabled Ship (asset_id: disabled_ship)
Unmanned gray ship drifting south of position, later burned as funeral pyre. Primary recovery and looting setting.

## Building Interior/Portal (asset_id: building_interior_portal)
Building entrance where prisoner dragged through portal by female Martians. Secondary transit setting for human capture sequence.

[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: airship_fleet

[[SECTION markdown]]
# Airship Fleet Environment

## Environment Role
Primary transit setting for Martian fleet operations and battle engagement.

## Architecture or Geography
Gray low-profile vessels with long shape, banners mounted on stem and stern, glowing devices positioned on prow. Fleet sails toward valley with swinging motion from window perspective.

## Lighting and Atmosphere Cues
Glowing devices emit light from prow positions. Banners dissolve in flame during battle sequence. Ships swing majestically then erratically through air. Gray color palette dominates fleet appearance.

## Scale Cues and Recurring Environmental Anchors
Twenty vessels visible from narrator's window position. Fleet retreats with several craft limping after twenty minutes. Lead vessel completes circle swinging broadside. Drifting ship intercepted before hitting buildings south of position.

## Useful Descriptive Noun Phrases
Gray airship fleet, glowing prow devices, banner-stem stern, drifting unmanned vessel, funeral pyre ship, swinging broadside vessel, limping retreat craft, gray low-profile vessels, banner-mounted stem stern, glowing device prow.

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: martian_buildings_valley

[[SECTION markdown]]
# Martian Buildings/Valley Environment

## Environment Role
Secondary battle setting with window fire positions and interior melting sequences.

## Architecture or Geography
Building interiors where Martians melt into structures within three minutes. Window positions serve as firing points for green warriors. Valley serves as approach route for airship fleet.

## Lighting and Atmosphere Cues
Terrific volley from windows with bullets dropping at explosion points. Banners dissolve in flame during battle sequence. Warriors melt into mist after engagement. Green warrior fire creates dramatic lighting effects.

## Scale Cues and Recurring Environmental Anchors
Green warriors fire volley from building windows. Lead vessel returns fire swinging broadside. Martians target specific points including sighting apparatus, gunners, officers. Fleet retreats with several craft limping. Building interiors serve as melting positions for Martians.

## Useful Descriptive Noun Phrases
Martian building interiors, window firing positions, green warrior volley, mist-melting warriors, explosion point bullets, sighting apparatus target, gunner position target, officer position target, valley approach route, building interior melting sequence.

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: disabled_ship

[[SECTION markdown]]
# Disabled Ship Environment

## Environment Role
Primary recovery and looting setting for unmanned vessel.

## Architecture or Geography
Unmanned gray ship drifting south of position. Vessel boarded using spears and grappling hooks. Martians search interior removing arms, silks, jewels, food including water. Carboys emptied over dead sailors. Ship set ablaze with missile.

## Lighting and Atmosphere Cues
Ship burns as funeral pyre drifting southeast. Missile ignition creates dramatic lighting effect. Banners dissolve in flame during burning sequence. Gray color palette dominates vessel appearance.

## Scale Cues and Recurring Environmental Anchors
One ship unmanned and drifting before hitting buildings south of position. Warriors rush to intercept disabled vessel. Martians search interior removing arms, silks, jewels, food. Burning ship drifts southeast as funeral pyre. Several craft limping after fleet retreat.

## Useful Descriptive Noun Phrases
Unmanned gray ship, drifting south position, spear-grappling hook boarding, interior looting sequence, carboy-emptying sailors, missile ignition burning, funeral pyre drift, arms silks jewels food removal, dead sailor carboys, southeast drifting burn.

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: building_interior_portal

[[SECTION markdown]]
# Building Interior/Portal Environment

## Environment Role
Secondary transit setting for human capture sequence and prisoner reveal.

## Architecture or Geography
Building entrance where prisoner dragged through portal by female Martians. Warriors drag small figure from ship into building interior. Portal serves as transition point between exterior fleet operations and interior captivity.

## Lighting and Atmosphere Cues
Prisoner dragged roughly through portal creating dramatic lighting effect. Female Martian figures create intimate lighting contrast to battle exterior. Interior space contrasts with gray airship exterior.

## Scale Cues and Recurring Environmental Anchors
Small figure dragged from ship into building. Warriors drag small figure from disabled vessel. Human woman being dragged into building by female Martians. Portal serves as entry point for prisoner reveal sequence.

## Useful Descriptive Noun Phrases
Building entrance portal, prisoner drag sequence, female Martian figures, interior captivity space, exterior-to-interior transition, small figure reveal, human woman capture, warrior drag sequence, portal entry point, female Martian captors.

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
