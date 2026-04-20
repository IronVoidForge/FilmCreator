# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-20T01:10:34.613798+00:00
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

# Chapter Summary: CH012 - A Prisoner With Power

## Scene 1: The Audience Chamber Warning
**Visual Continuity:** John Carter enters the audience chamber and salutes. Lorquas Ptomel signals him to advance, fixing his great, hideous eyes upon Carter.
**Story Beat:** Lorquas Ptomel addresses Carter's high position among the Tharks but emphasizes he is not one of them and owes no allegiance. He warns that Carter is a prisoner giving commands which must be obeyed.
**Conflict:** Lorquas Ptomel reports accusations that Carter plotted to escape with Dejah Thoris ("the red girl"). Either accusation (escape plot or running off with her) would warrant execution, but the Tharks are just and will grant a trial on their return to Thark if Tal Hajus commands.
**Threat:** Lorquas Ptomel states that if Carter runs off with the red girl, he (Lorquas Ptomel) must account to Tal Hajus and face Tars Tarkas. He warns that under two conditions only may Carter be killed without orders: personal combat in self-defense or apprehended in an attempt to escape.
**Resolution:** Lorquas Ptomel emphasizes the importance of safe delivery of Dejah Thoris to Tal Hajus. He concludes, "You may go."

## Scene 2: Realization and Decision
**Visual Continuity:** Carter turns and leaves the audience chamber.
**Story Beat:** Carter realizes this is the beginning of Sarkoja's persecution (Sarkoja being Tars Tarkas' oldest and most trusted female). He recalls conversations touching on escape and origin.
**Internal Monologue:** Instead of putting thoughts of escape from his mind, the audience centers every faculty on this subject. The absolute necessity for escape regarding Dejah Thoris is impressed upon him, convinced that some horrible fate awaits her at Tal Hajus's headquarters.
**Visual Continuity:** Carter wanders about the plaza lost in gloomy forebodings.

## Scene 3: Meeting Tars Tarkas
**Visual Continuity:** Tars Tarkas approaches Carter on his way from the audience chamber. His demeanor toward Carter is unchanged; he greets Carter as though they had not just parted moments before.
**Dialogue:** Tars Tarkas asks for Carter's quarters. Carter replies he has selected none, awaiting advice or opportunity to ask advice. He smiles, noting he is not yet familiar with all Thark customs.
**Action:** Tars Tarkas directs Carter to come with him; they move off across the plaza to a building adjoined by Sola and her charges.

## Scene 4: Quarters Selection and Social Explanation
**Visual Continuity:** Tars Tarkas states his quarters are on the first floor of this building, second floor fully occupied by warriors, third floor and above vacant. Carter may take choice.
**Dialogue:** Tars Tarkas notes Carter gave up his woman to the red prisoner. He explains that as a chieftain, Carter may select any or all females from retinues of chieftains whose metal he now wears.
**Action:** Carter thanks him but assures him he can get along without assistance except preparing food. Tars Tarkas promises to send women for food and care of arms/ammunition. Carter suggests they bring sleeping silks and furs belonging to him as spoils of combat.
**Visual Continuity:** Tars Tarkas promises and departs. Left alone, Carter ascends winding corridor to upper floors in search of suitable quarters.

## Scene 5: Room Selection and Loot Arrival
**Visual Continuity:** Beauties of other buildings are repeated; Carter is soon lost in tour of investigation and discovery. He finally chooses a front room on the third floor because it brings him nearer to Dejah Thoris (apartment on second floor of adjoining building).
**Plan:** Carter flashes upon rigging up means of communication whereby she might signal him in case she needs services or protection.
**Visual Continuity:** Adjoining sleeping apartment are baths, dressing rooms, and other sleeping/living apartments (some ten rooms on this floor). Windows of back rooms overlook enormous court forming center of square made by buildings facing four contiguous streets. Court given over to quartering various animals belonging to warriors occupying adjoining buildings.
**Description:** Court entirely overgrown with yellow, moss-like vegetation; numerous fountains, statuary, benches, and pergola-like contraptions bear witness to beauty presented in bygone times.

## Scene 6: Arrival of Women and Social Customs Explanation
**Visual Continuity:** Advent of several young females bearing loads of weapons, silks, furs, jewels, cooking utensils, and casks of food/drink (considerable loot from air craft). All this property belonged to two chieftains Carter had slain; now by customs of Tharks it has become his.
**Action:** At Carter's direction they place stuff in one back room, then depart only to return with second load advised as balance of goods. Second trip accompanied by ten or fifteen other women and youths forming retinues of two chieftains.
**Explanation:** Women/children of man's retinue likened to military unit for which he is responsible (instruction, discipline, sustenance). Not families, wives, or servants; relationship peculiar. All property owned in common except personal weapons, ornaments, sleeping silks/furs. Surplus held as custodian passed on to younger members.
**Customs:** Mating is matter of community interest solely, directed without reference to natural selection. Council of chieftains control matter. Results shown in cold, cruel creatures and gloomy, loveless existence. Green Martians are absolutely virtuous except degenerates like Tal Hajus.

## Scene 7: Final Arrangement
**Visual Continuity:** Carter finds he must assume responsibility for these creatures whether he would or not; makes best of it and directs them to find quarters on upper floors, leaving third floor to him.
**Action:** One girl charged with duties of simple cuisine; others directed to take up various activities formerly constituting vocations. Thereafter Carter sees little of them nor cares to.
````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
task: environment_extraction
version: 1

[[SECTION environment_index_markdown]]
# Environment Index - CH012

| Asset ID | Environment Name | Role | Key Features |
|----------|------------------|------|--------------|
| audience_chamber | Audience Chamber | Primary | High-status Thark interior, warning space |
| plaza_court | Plaza Court | Secondary/Transit | Overgrown central square with fountains and statuary |
| thark_building_complex | Thark Building Complex | Primary/Secondary | Multi-story structure housing warriors and quarters |
| carter_quarters | Carter's Quarters | Primary | Third-floor front room, communication hub |

[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: audience_chamber

[[SECTION markdown]]
**Environment Role:** Primary setting for authority warnings and prisoner status declarations.

**Architecture/Geography:** High-status Thark interior chamber with formal seating arrangements. Great, hideous eyes visible from Lorquas Ptomel's position. Audience chamber connects to plaza via exit path.

**Lighting/Atmosphere:** Formal, imposing lighting emphasizing power dynamics. Gloomy forebodings noted in adjacent plaza space. Interior maintains dignified but threatening atmosphere.

**Scale/Anchors:** Large enough for multiple Thark warriors and visitors. Fixed positions for Lorquas Ptomel (seated) and John Carter (standing/saluting). Exit leads directly to plaza.

**Descriptive Noun Phrases:** Audience chamber, high-status interior, formal seating, great hideous eyes, warning space, prisoner status room, Thark authority chamber, exit path to plaza.

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: plaza_court

[[SECTION markdown]]
**Environment Role:** Secondary/transit setting for movement between buildings and contemplation spaces.

**Architecture/Geography:** Enormous court forming center of square made by buildings facing four contiguous streets. Overgrown with yellow, moss-like vegetation. Numerous fountains, statuary, benches, and pergola-like contraptions bear witness to beauty presented in bygone times. Court given over to quartering various animals belonging to warriors occupying adjoining buildings.

**Lighting/Atmosphere:** Gloomy forebodings noted during Carter's wandering. Yellow moss-like vegetation creates aged, abandoned atmosphere. Fountains and statuary suggest former beauty now decayed.

**Scale/Anchors:** Enormous court scale with multiple fountain clusters. Statuary serves as visual anchors throughout space. Pergola contraptions mark architectural interest points. Animal quarters occupy portions of court.

**Descriptive Noun Phrases:** Plaza court, enormous central square, yellow moss-like vegetation, overgrown fountains, bygone beauty statuary, animal quartering spaces, four contiguous streets, decayed grandeur, moss-covered benches, pergola contraptions.

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: thark_building_complex

[[SECTION markdown]]
**Environment Role:** Primary/Secondary housing structure for Thark warriors and quarter selection.

**Architecture/Geography:** Multi-story building with first floor housing Tars Tarkas's quarters, second floor fully occupied by warriors, third floor and above vacant. Adjoining sleeping apartments include baths, dressing rooms, and other sleeping/living apartments (some ten rooms on this floor). Winding corridor leads to upper floors.

**Lighting/Atmosphere:** Interior corridors maintain formal warrior atmosphere. Upper floors vacant suggest potential for customization. Sleeping areas maintain Thark functional design aesthetic.

**Scale/Anchors:** First floor quarters anchor lower level. Second floor warrior occupation marks middle section. Third floor vacancy provides selection flexibility. Winding corridor serves as primary vertical circulation element.

**Descriptive Noun Phrases:** Multi-story building, first floor quarters, second floor warrior occupation, third floor vacancy, winding corridor, upper floors, adjoining sleeping apartments, baths and dressing rooms, ten-room floor, vacant upper levels.

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: carter_quarters

[[SECTION markdown]]
**Environment Role:** Primary personal space for Carter's communication hub and living quarters.

**Architecture/Geography:** Front room on third floor chosen because it brings him nearer to Dejah Thoris (apartment on second floor of adjoining building). Adjoining sleeping apartment includes baths, dressing rooms, and other sleeping/living apartments. Windows of back rooms overlook enormous court forming center of square.

**Lighting/Atmosphere:** Third-floor positioning provides elevated view over plaza court. Window placement enables visual connection to Dejah Thoris's location. Interior maintains functional living space atmosphere with communication rigging potential.

**Scale/Anchors:** Front room serves as primary living anchor. Windows serve as visual anchors connecting to plaza and Dejah Thoris's apartment. Back rooms overlook court providing secondary viewing points.

**Descriptive Noun Phrases:** Third floor front room, elevated view quarters, window connection space, communication hub, back room windows, overlooking court, near Dejah Thoris apartment, living quarters, rigging potential, visual signal point.

[[/SECTION]]
[[/FILMCREATOR_RECORD]]
[[/FILMCREATOR_PACKET]]
````
