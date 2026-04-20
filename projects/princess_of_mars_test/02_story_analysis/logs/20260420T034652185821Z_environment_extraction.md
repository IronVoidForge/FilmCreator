# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-20T03:46:52.185821+00:00
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

Chapter id: CH012

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

# Chapter Summary: CH012 - A Prisoner with Power

**Story Arc:**
*   **Interrogation:** Lorquas Ptomel addresses John Carter, acknowledging his prowess but warning him of his precarious position (prisoner yet chieftain). Accusations arise regarding a plot to escape with Dejah Thoris. Execution is threatened unless Tal Hajus commands otherwise.
*   **Warning:** Lorquas warns that if John runs off with the "red girl," he must account to Tal Hajus and Tars Tarkas. He states they await only two excuses for killing John: self-defense or attempted escape.
*   **Realization:** John leaves the audience chamber, realizing this is Sarkoja's persecution. He recalls conversations about escape and origin.
*   **Quarters Offered:** Tars Tarkas approaches John in the plaza. Offers him quarters on the third floor of a building adjoining Sola's residence. The first floor is occupied by Tars Tarkas; second by Sola/charges.
*   **Retinue & Loot:** Women and youths arrive bearing weapons, silks, furs, jewels, cooking utensils, food, and loot from air craft (property of two slain chieftains). John directs them to find quarters on upper floors.
*   **Room Selection:** John chooses a front room on the third floor to be near Dejah Thoris's apartment (second floor) to rig up communication means.
*   **Cultural Exposition:** John observes the Thark retinue customs: women and children are military units for which he is responsible, not wives or servants. Property is communal; surplus is passed to younger members. Mating is community-directed.

**Visual Continuity Facts:**
*   **Audience Chamber:** Lorquas Ptomel signals John to advance; his great, hideous eyes fix upon John.
*   **Plaza:** John wanders in gloomy forebodings; Tars Tarkas approaches with unchanged demeanor.
*   **Building Layout:** Three floors visible. First occupied by Tars Tarkas. Second by Sola and charges. Third vacant for John.
*   **Loot Items:** Weapons, silks, furs, jewels, cooking utensils, casks of food/drink, air craft loot.
*   **Court View:** Back rooms overlook an enormous court with yellow moss-like vegetation, fountains, statuary, benches, and pergola-like contraptions.
````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
task: environment_extraction
version: 1

[[SECTION environment_index_markdown]]
# Environment Index - Chapter CH012

## Audiences Chamber
- **Role:** Primary setting for interrogation scene
- **Architecture:** Great, hideous eyes of Lorquas Ptomel; audience chamber with court view
- **Lighting/Atmosphere:** Formal, tense atmosphere during confrontation
- **Scale:** Enormous court visible from back rooms

## Plaza
- **Role:** Transit setting for John's movement through city
- **Architecture:** Open plaza space adjoining Sola's residence building
- **Lighting/Atmosphere:** Gloomy forebodings; unchanged demeanor of Tars Tarkas
- **Scale:** Building layout with three visible floors

## Building (Three Floors)
- **Role:** Primary setting for John's quarters and retinue distribution
- **Architecture:** Three-story building adjoining Sola's residence; first floor occupied by Tars Tarkas, second by Sola/charges, third vacant for John
- **Lighting/Atmosphere:** Communal property distribution; women and children as military units
- **Scale:** Front room on third floor chosen for communication rigging near Dejah Thoris's apartment

## Court View (from Building)
- **Role:** Secondary setting visible from building back rooms
- **Architecture:** Enormous court with yellow moss-like vegetation, fountains, statuary, benches, pergola-like contraptions
- **Lighting/Atmosphere:** Yellow moss-like vegetation; formal court space
- **Scale:** Statuary and benches indicate grand scale

[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: audience_chamber

[[SECTION markdown]]
# Audience Chamber - CH012

## Environment Role
Primary setting for interrogation scene where Lorquas Ptomel addresses John Carter

## Architecture and Geography
Great, hideous eyes of Lorquas Ptomel fix upon John; audience chamber with formal court view from back rooms overlooking enormous court space

## Lighting and Atmosphere Cues
Formal, tense atmosphere during confrontation; great eyes create intimidating presence; accusations arise regarding escape plot with Dejah Thoris

## Scale Cues and Environmental Anchors
Enormous court visible from back rooms; statuary, benches, pergola-like contraptions indicate grand scale of Thark court space

## Descriptive Noun Phrases for Render-Facing Prompts
- Great hideous eyes of Lorquas Ptomel
- Audience chamber with formal court view
- Enormous court with yellow moss-like vegetation
- Statuary and benches in grand court space
- Pergola-like contraptions overlooking court

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: plaza

[[SECTION markdown]]
# Plaza - CH012

## Environment Role
Transit setting for John's movement through city; where Tars Tarkas approaches John

## Architecture and Geography
Open plaza space adjoining Sola's residence building; three-story building layout with first floor occupied by Tars Tarkas, second by Sola/charges, third vacant for John

## Lighting and Atmosphere Cues
Gloomy forebodings during John's wandering; unchanged demeanor of Tars Tarkas creates formal atmosphere; women and youths arrive bearing weapons and loot

## Scale Cues and Environmental Anchors
Three visible floors of building; first floor occupied by Tars Tarkas, second by Sola and charges, third vacant for John; front room on third floor chosen for communication rigging

## Descriptive Noun Phrases for Render-Facing Prompts
- Open plaza space adjoining residence building
- Three-story building with visible floors
- First floor occupied by Tars Tarkas
- Second floor by Sola and charges
- Third floor vacant for John's quarters
- Front room on third floor near Dejah Thoris's apartment

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: building_three_floors

[[SECTION markdown]]
# Building Three Floors - CH012

## Environment Role
Primary setting for John's quarters and retinue distribution; where women and youths arrive bearing weapons, silks, furs, jewels, cooking utensils, food, and loot from air craft

## Architecture and Geography
Three-story building adjoining Sola's residence; first floor occupied by Tars Tarkas, second by Sola/charges, third vacant for John; front room on third floor chosen for communication rigging near Dejah Thoris's apartment

## Lighting and Atmosphere Cues
Communal property distribution atmosphere; women and children as military units for which he is responsible; surplus passed to younger members; mating community-directed

## Scale Cues and Environmental Anchors
Three visible floors of building; front room on third floor chosen for communication rigging near Dejah Thoris's apartment (second floor); back rooms overlook enormous court with yellow moss-like vegetation, fountains, statuary, benches, pergola-like contraptions

## Descriptive Noun Phrases for Render-Facing Prompts
- Three-story building adjoining Sola's residence
- First floor occupied by Tars Tarkas
- Second floor by Sola and charges
- Third floor vacant for John's quarters
- Front room on third floor near Dejah Thoris's apartment
- Back rooms overlooking enormous court with yellow moss-like vegetation
- Fountains, statuary, benches in court space

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: court_view_from_building

[[SECTION markdown]]
# Court View from Building - CH012

## Environment Role
Secondary setting visible from building back rooms; enormous court space observed during John's quarters selection

## Architecture and Geography
Enormous court with yellow moss-like vegetation, fountains, statuary, benches, pergola-like contraptions; visible from back rooms of three-story building adjoining Sola's residence

## Lighting and Atmosphere Cues
Yellow moss-like vegetation creates distinctive atmosphere; formal court space with fountains and statuary indicates grand Thark architecture

## Scale Cues and Environmental Anchors
Enormous scale indicated by yellow moss-like vegetation, fountains, statuary, benches, pergola-like contraptions; back rooms of building overlook this court space

## Descriptive Noun Phrases for Render-Facing Prompts
- Enormous court with yellow moss-like vegetation
- Fountains and statuary in court space
- Benches and pergola-like contraptions
- Yellow moss-like vegetation distinctive atmosphere
- Court space visible from building back rooms

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
