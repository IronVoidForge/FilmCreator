# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-18T19:21:50.826587+00:00
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

# Chapter Summary: A Fair Captive from the Sky (Chapter VIII)

**Plot Overview:**
Following an incubation ceremony, Carter and Sola return to their city but are ordered back immediately upon seeing a fleet of gray airships arriving over the hills. A battle ensues where Carter's warriors demonstrate deadly accuracy against the ships. One vessel is disabled and crashes near the city. Martians loot and burn the ship before dragging a prisoner into a building, who signals Carter with hope then dejection.

**Scene Decomposition & Visual Facts:**

1.  **The Arrival (Visual Continuity):**
    *   **Object:** Twenty gray-painted airships, long and low.
    *   **Details:** Each carries a strange banner from stem to stern; odd devices painted on prows gleam in sunlight.
    *   **Action:** Ships swing slowly over the crest of the nearest hill toward the city.

2.  **The Battle (Visual Continuity):**
    *   **Martian Action:** Green warriors fire a terrific volley from building windows.
    *   **Carter's Action:** Warriors return fire with high accuracy (approx. 75% hit rate).
    *   **Targeting:** Specific points targeted: wireless finding/sighting apparatus, smaller guns, gunners, officers, crew members, upper works, steering gear/propellers.
    *   **Effect:** Banners and upper works dissolve in spurts of flame; vessels swing broadside or turn back to complete circles.

3.  **The Crash (Visual Continuity):**
    *   **Object:** One barely moving craft receives the brunt of fire, appears unmanned.
    *   **Action:** Drifts slowly with light breeze in southeasterly direction; bodies of crew strewn about decks.
    *   **Martian Response:** Warriors rush to roofs, follow retreating armada with fusillade. One ship dips below hill crests until only one is visible.

4.  **The Recovery (Visual Continuity):**
    *   **Action:** Warriors swarm onto the craft from windows just before it strikes buildings.
    *   **Equipment:** Great spears ease collision shock; grappling hooks used to haul boat to ground.
    *   **Loot:** Arms, ammunition, silks, furs, jewels, carved stone vessels, solid foods/liquids, casks of water.

5.  **The Burning (Visual Continuity):**
    *   **Action:** Warriors tow craft far out into valley; empty contents of carboys onto dead sailors/decks.
    *   **Missile:** Last warrior throws missile back onto vessel; faint spurt of flame rises.
    *   **Result:** Guy ropes released; great warship soars majestically into air, decks/upper works a mass of roaring flames. Drifts to southeast, rising higher as flames eat wooden parts.

6.  **The Prisoner (Visual Continuity):**
    *   **Appearance:** Slender, girlish figure similar to earthly women; oval and beautiful face; finely chiseled features; large/lustrous eyes; coal black waving hair caught loosely into strange coiffure; light reddish copper skin; crimson glow of cheeks; ruby lips.
    *   **Attire:** Destitute of clothes, entirely naked save for highly wrought ornaments.
    *   **Action:** Dragged roughly into nearby building by green Martian females.
    *   **Interaction:** Eyes meet Carter's; she makes a little sign with free hand (ununderstood); expression shifts from hope/renewed courage to utter dejection/loathing/contempt because he did not answer her signal.

**Continuity Notes:**
*   The city remains deserted for over a week due to fear of return attack by air craft.
*   Carter feels depressed, viewing the scene as defeat of kindred people rather than routing of horde.
*   Sola rushes up to Carter upon his emergence onto street; Lorquas Ptomel remains at deserted city until danger passed.
````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
task: environment_extraction
version: 1

[[SECTION environment_index_markdown]]
# Environment Index - Princess of Mars Test (Chapter VIII)

## Stable Environment Families

| Asset ID | Role | Primary Anchor |
|----------|------|----------------|
| city | primary | urban windows, deserted streets |
| hills | transit | hill crests, arrival/dip zones |
| valley | secondary | open drift space, southeast direction |
| buildings | secondary | window firing positions, urban structures |
| airship | secondary | crashed vessel, wooden decks, upper works |

## Notes

- All environments stable across reruns
- Focus on visible geography and atmosphere
- Excludes literary abstractions
- Includes recurring environmental anchors
[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: city

[[SECTION markdown]]
# City - Primary Setting

## Environment Role
Primary setting where Carter and Sola return after incubation ceremony; remains deserted for over a week due to fear of air craft attack.

## Architecture or Geography
Urban structures with windows serving as firing positions for Martian warriors; streets accessible for street emergence; buildings near crash site for prisoner recovery.

## Lighting and Atmosphere Cues
Sunlight gleaming on odd devices painted on prows; gray-painted airships visible against city backdrop; deserted atmosphere with fear of return attack.

## Scale Cues and Recurring Environmental Anchors
City scale large enough to see fleet arriving over hills; windows at building heights for volley firing; streets accessible for street emergence; buildings near crash site for recovery operations.

## Descriptive Noun Phrases
- deserted urban streets
- window firing positions
- gray-painted airship arrival zone
- fear of return attack atmosphere
- street emergence points
- deserted cityscape
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: hills

[[SECTION markdown]]
# Hills - Transit Setting

## Environment Role
Transit setting where airships arrive over crest and dip below until only one visible; atmospheric transition zone between city and valley.

## Architecture or Geography
Hill crests serving as arrival/dip zones for airship fleet; elevated terrain above city; slopes leading to valley floor.

## Lighting and Atmosphere Cues
Sunlight gleaming on odd devices painted on prows; ships swing slowly over crest in sunlight; atmospheric transition from hill to valley.

## Scale Cues and Recurring Environmental Anchors
Hills large enough to see fleet arriving over them; crests at height above city; dip zones below hill crests until only one ship visible; atmospheric boundary between city and valley.

## Descriptive Noun Phrases
- hill crest arrival zone
- airship dip below point
- elevated terrain above city
- fleet swing over crest
- atmospheric transition boundary
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: valley

[[SECTION markdown]]
# Valley - Secondary Setting

## Environment Role
Secondary setting where burning ship drifts southeast; open space for ship to soar majestically into air and rise higher as flames eat wooden parts.

## Architecture or Geography
Open valley floor allowing ship to drift southeast; space large enough for warship to soar into air; directional flow toward southeast.

## Lighting and Atmosphere Cues
Southeasterly direction visible; flames rising higher as they eat wooden parts; open sky above valley floor.

## Scale Cues and Recurring Environmental Anchors
Valley large enough for great warship to soar majestically into air; space allowing ship to drift southeast; directional flow toward southeast; atmospheric openness for fire rise.

## Descriptive Noun Phrases
- open valley floor
- southeast drift direction
- soaring warship space
- flame rise zone
- open sky above valley
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: buildings

[[SECTION markdown]]
# Buildings - Secondary Setting

## Environment Role
Secondary setting for window firing positions; urban structures where warriors swarm onto craft from windows just before it strikes.

## Architecture or Geography
Building windows at height for volley firing; urban structures near crash site; windows serving as access points to craft recovery.

## Lighting and Atmosphere Cues
Sunlight gleaming on odd devices painted on prows visible from buildings; green warriors fire from building windows; urban lighting conditions.

## Scale Cues and Recurring Environmental Anchors
Windows at height for volley firing; buildings near crash site for warrior swarm access; urban scale allowing multiple window positions; structures large enough for craft to strike buildings.

## Descriptive Noun Phrases
- window firing positions
- urban structure windows
- warrior swarm access points
- building height zones
- crash site proximity structures
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: airship

[[SECTION markdown]]
# Airship - Secondary Setting

## Environment Role
Secondary setting as crashed vessel; focal point for recovery, burning, and prisoner extraction operations.

## Architecture or Geography
Wooden parts including upper works and decks; steering gear/propellers; wireless finding/sighting apparatus; smaller guns; gunners positions; officers quarters; crew member areas; carboys on dead sailors/decks.

## Lighting and Atmosphere Cues
Sunlight gleaming on odd devices painted on prows; banners dissolve in spurts of flame; upper works a mass of roaring flames; faint spurt of flame rises from missile.

## Scale Cues and Recurring Environmental Anchors
Large enough to carry twenty crew members; wooden parts large enough for flames to eat; decks large enough for bodies strewn about; upper works large enough for banners to dissolve in flame; craft large enough to soar into air.

## Descriptive Noun Phrases
- crashed vessel structure
- wooden deck surfaces
- upper works flame zone
- steering gear apparatus
- wireless finding equipment
- banner dissolution area
- crew strewn decks
[[/SECTION]]
[[/FILMCREATOR_RECORD]]
[[/FILMCREATOR_PACKET]]
````
