# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-19T23:31:30.007792+00:00
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

# Chapter Summary: CH001

## Story Summary

- **Introduction:** Narrator reflects on his age and mortality. He is a soldier of fortune recounting strange events during ten years in an Arizona cave.
- **Backstory:** Carter finds a gold vein with Captain James K. Powell. They uncover over a million dollars worth of ore in three months.
- **Inciting Incident:** Powell leaves to buy machinery; Carter guards the claim alone.
- **Rising Action:** Carter sees Powell's party vanish into shadows. He follows tracks, discovering they are unshod ponies galloping away.
- **Climax:** Carter finds an Apache camp under moonlight. Powell is dead, riddled with arrows. Carter charges the warriors single-handedly.
- **Falling Action:** Carter escapes pursuit by taking a wrong trail into a defile. He reaches a cave mouth at dawn.
- **Resolution:** Carter lays Powell's body down. He enters the cave but collapses from exhaustion against the wall.

## Visual Continuity

- **Lighting:** Clear Arizona mornings; bright moonlight during night chase; sudden daylight without warning at cave entrance.
- **Props:** Colt revolvers, carbine, cartridge belts, saddle horse, burros, canteen water.
- **Locations:** Arizona hills, valley, plateau, Apache tepee camp, narrow gorge, cave mouth (4ft high, 3-4ft wide).
- **Environment:** Dusty trails, rocky ravines, jagged rock formations, dense shadow in cave back.
````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
task: environment_extraction
version: 1

[[SECTION environment_index_markdown]]
# Environment Index - CH001

## Extracted Environments

| Asset ID | Role | Primary Geography | Lighting/Atmosphere | Scale Anchors |
|----------|------|-------------------|---------------------|---------------|
| arizona_hills_valley_plateau | primary | Rolling hills, valley floor, elevated plateau | Clear Arizona morning light, dusty trails | Rocky ravines, jagged rock formations |
| apache_tepee_camp | secondary | Apache tepee encampment under moonlight | Bright moonlight during night chase | Dense shadow in cave back |
| narrow_gorge_defile | transit | Narrow gorge with defile entrance | Sudden daylight without warning | 4ft high, 3-4ft wide cave mouth |
| cave_mouth_interior | resolution | Cave interior with collapsed wall | Dim light from cave entrance | Exhaustion against wall anchor |

[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: arizona_hills_valley_plateau

[[SECTION markdown]]
arizona_hills_valley_plateau

**Role:** primary setting for narrator's ten-year recounting

**Architecture/Geography:** Rolling hills, valley floor, elevated plateau with rocky ravines and jagged rock formations. Dusty trails wind through terrain.

**Lighting/Atmosphere:** Clear Arizona morning light dominates. Bright sun creates sharp shadows across dusty ground. Atmospheric dust hangs in air during day scenes.

**Scale Cues:** Rocky ravines provide natural depth markers. Jagged rock formations establish vertical scale. Valley floor offers horizontal expanse for movement.

**Environmental Anchors:** Colt revolvers, carbine, cartridge belts visible on characters. Saddle horse and burros mark transit routes. Canteen water indicates survival needs.

**Render-Facing Noun Phrases:** dusty arizona trail, rocky ravine formation, jagged rock outcrop, clear morning sunbeam, valley floor expanse, elevated plateau ridge, atmospheric dust haze, natural rock shelter entrance

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: apache_tepee_camp

[[SECTION markdown]]
apache_tepee_camp

**Role:** secondary setting for climactic confrontation

**Architecture/Geography:** Apache tepee encampment with multiple dwellings arranged in circular pattern. Moonlight illuminates camp from above. Dense shadows create depth within camp perimeter.

**Lighting/Atmosphere:** Bright moonlight during night chase scene. Sudden daylight without warning at cave entrance. Camp exists under full moon illumination with sharp contrast between light and shadow.

**Scale Cues:** Tepee structures establish vertical height markers. Camp perimeter defines horizontal boundaries. Warriors positioned around camp create human scale reference.

**Environmental Anchors:** Powell's body riddled with arrows marks tragedy location. Apache warriors single-handed charge creates action focal point. Moonlight serves as primary illumination source.

**Render-Facing Noun Phrases:** apache tepee dwelling, circular camp arrangement, full moon illumination, sharp light shadow contrast, warrior encampment perimeter, night chase scene lighting, dramatic moonlit landscape, arrow-marked tragedy site

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: narrow_gorge_defile

[[SECTION markdown]]
narrow_gorge_defile

**Role:** transit setting for escape sequence

**Architecture/Geography:** Narrow gorge with defile entrance leading into cave system. 4ft high, 3-4ft wide cave mouth serves as primary passage point. Rocky walls create natural corridor.

**Lighting/Atmosphere:** Sudden daylight without warning at cave entrance. Bright moonlight during night chase transitions to sudden daylight. Dusty trails continue through gorge terrain.

**Scale Cues:** Cave mouth dimensions (4ft high, 3-4ft wide) establish precise scale. Narrow gorge walls create vertical compression. Defile entrance marks transition point between exterior and interior spaces.

**Environmental Anchors:** Wrong trail taken into defile marks escape route. Cave mouth at dawn serves as resolution anchor. Rocky ravines continue from valley terrain through gorge passage.

**Render-Facing Noun Phrases:** narrow gorge passage, 4ft high cave mouth, 3-4ft wide entrance opening, sudden daylight transition, rocky wall corridor, defile entrance marker, wrong trail escape route, dawn cave mouth illumination

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: cave_mouth_interior

[[SECTION markdown]]
cave_mouth_interior

**Role:** resolution setting for chapter conclusion

**Architecture/Geography:** Cave interior with collapsed wall. Cave mouth entrance visible from exterior. Dense shadow in cave back creates depth beyond entrance point. 4ft high, 3-4ft wide opening serves as primary access.

**Lighting/Atmosphere:** Dim light from cave entrance illuminates interior space. Exhaustion against wall anchor marks character collapse location. Bright moonlight during night chase transitions to dim interior lighting.

**Scale Cues:** Collapsed wall provides vertical scale reference. Cave mouth dimensions establish precise opening size. Dense shadow in cave back creates depth perception beyond immediate entrance area.

**Environmental Anchors:** Carter collapses from exhaustion against wall. Powell's body laid down marks previous location. Cave interior serves as final resting place for chapter narrative.

**Render-Facing Noun Phrases:** collapsed cave wall, dim interior lighting, dense shadow cave back, 4ft high opening, 3-4ft wide entrance, exhaustion collapse anchor, cave mouth illumination transition, interior depth shadow marker

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
