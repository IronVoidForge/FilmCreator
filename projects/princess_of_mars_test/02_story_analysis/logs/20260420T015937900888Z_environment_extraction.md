# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-20T01:59:37.900888+00:00
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

**Visual Continuity:**
The chapter opens on the Arizona Hills under clear morning light. Key locations include a mountainside trail, a valley with hog backs and plateaus, a water hole, and a large cave entrance (four feet high). The setting shifts from daylight to moonlight during the chase. Visual markers include burros, horses, Colt revolvers, cartridge belts, and Indian tepees clustered around a central object.
**Story Summary:**
John Carter reflects on his ageless existence and fear of death despite having died twice. He recounts his Civil War past and partnership with Captain Powell to mine gold in Arizona. After guarding the claim while Powell leaves for supplies, Carter discovers Powell's tracks have been followed by Apaches. He chases them into a valley where he finds an Apache camp surrounding Powell's body. Overwhelmed by duty, Carter charges the warriors alone, scattering them. He retrieves Powell's corpse and flees into a rocky defile leading to a cave. Inside the cave, he lays Powell down, confirms death, and succumbs to fatigue on the cave floor.
````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
task: environment_extraction
version: 1

[[SECTION environment_index_markdown]]
# Environment Index - CH001

## Arizona Hills
- Role: Primary setting for Carter's reflection and opening sequence
- Geography: Mountainside trail, hog backs, plateaus
- Lighting: Clear morning light transitioning to moonlight during chase
- Atmosphere: Desert landscape with burros, horses, Colt revolvers visible
- Scale: Large open terrain with rocky defiles leading to cave

## Valley
- Role: Transit setting during Apache chase sequence
- Geography: Valley floor with hog backs and plateaus surrounding
- Lighting: Daylight shifting to moonlight during pursuit
- Atmosphere: Open desert valley with Apache tepees clustered around central object
- Scale: Medium-sized valley with rocky defile entrance

## Cave
- Role: Primary setting for chapter conclusion
- Geography: Large cave entrance (four feet high), cave floor
- Lighting: Interior cave lighting, dim natural light
- Atmosphere: Fatigue-inducing interior space, Powell's body present
- Scale: Interior cave space with floor area for resting

## Apache Camp
- Role: Secondary setting discovered during chase
- Geography: Clustered tepees around central object
- Lighting: Daylight/moonlight depending on chase timing
- Atmosphere: Hostile camp environment, warriors surrounding Powell's corpse
- Scale: Medium-sized encampment with multiple structures

[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: arizona_hills

[[SECTION markdown]]
# Arizona Hills Environment

## Environment Role
Primary setting for Carter's reflection and opening sequence of the chapter.

## Architecture and Geography
Mountainside trail winding through desert landscape with hog backs and plateaus visible in distance. Rocky defiles lead toward cave entrance. Open terrain suitable for horse travel.

## Lighting and Atmosphere Cues
Clear morning light establishing initial scene, transitioning to moonlight during chase sequence. Desert atmosphere with burros, horses, Colt revolvers, cartridge belts visible as environmental markers.

## Scale Cues
Large open desert terrain providing expansive view of hog backs and plateaus. Rocky defiles create natural boundaries leading to cave interior.

## Descriptive Noun Phrases
- Mountainside trail winding through desert
- Hog backs rising in distance
- Plateaus visible across landscape
- Rocky defile entrance
- Burro tracks on trail
- Horse hooves on desert floor
- Colt revolvers resting nearby
- Cartridge belts hanging from saddle

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: valley_chase

[[SECTION markdown]]
# Valley Environment

## Environment Role
Transit setting during Apache chase sequence, medium-sized valley with rocky defile entrance.

## Architecture and Geography
Valley floor surrounded by hog backs and plateaus. Open desert space with Apache tepees clustered around central object. Rocky defile provides exit route to cave.

## Lighting and Atmosphere Cues
Daylight establishing initial chase scene, shifting to moonlight during pursuit sequence. Desert valley atmosphere with multiple environmental markers including horses, burros, Colt revolvers visible.

## Scale Cues
Medium-sized valley providing open space for horse travel and Apache encampment. Rocky defile entrance creates natural boundary between valley and cave interior.

## Descriptive Noun Phrases
- Valley floor surrounded by hog backs
- Plateaus framing valley edges
- Apache tepees clustered around central object
- Rocky defile exit route
- Horse tracks across valley floor
- Burro paths winding through desert
- Colt revolvers resting on trail
- Cartridge belts visible in scene

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: cave_interior

[[SECTION markdown]]
# Cave Interior Environment

## Environment Role
Primary setting for chapter conclusion, interior space with Powell's body present.

## Architecture and Geography
Large cave entrance four feet high leading to interior cave floor. Interior cave space providing resting area. Natural rock formations creating enclosed atmosphere.

## Lighting and Atmosphere Cues
Interior cave lighting with dim natural light filtering through entrance. Fatigue-inducing interior space atmosphere. Powell's body present as environmental anchor.

## Scale Cues
Interior cave space with floor area sufficient for resting. Cave entrance size (four feet high) establishing scale reference. Interior rock formations creating enclosed atmosphere.

## Descriptive Noun Phrases
- Large cave entrance four feet high
- Cave floor interior space
- Natural rock formations enclosing area
- Dim natural light filtering through entrance
- Powell's body as environmental anchor
- Fatigue-inducing interior atmosphere
- Rock walls surrounding resting area
- Cave interior providing shelter

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: apache_encampment

[[SECTION markdown]]
# Apache Encampment Environment

## Environment Role
Secondary setting discovered during chase, hostile camp environment with warriors surrounding Powell's corpse.

## Architecture and Geography
Clustered tepees around central object forming encampment structure. Multiple structures creating medium-sized encampment space. Rocky terrain surrounding Apache territory.

## Lighting and Atmosphere Cues
Daylight or moonlight depending on chase timing. Hostile camp environment atmosphere with warriors present. Desert valley lighting conditions affecting visibility.

## Scale Cues
Medium-sized encampment with multiple tepee structures. Central object anchoring encampment layout. Rocky terrain surrounding Apache territory establishing boundaries.

## Descriptive Noun Phrases
- Clustered tepees around central object
- Multiple encampment structures visible
- Warriors surrounding Powell's corpse
- Central object anchoring encampment layout
- Rocky terrain surrounding Apache territory
- Desert valley lighting conditions
- Hostile camp environment atmosphere
- Encampment entrance and exit routes

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
