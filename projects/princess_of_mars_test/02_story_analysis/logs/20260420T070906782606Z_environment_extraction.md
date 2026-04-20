# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-20T07:09:06.782606+00:00
- task: environment_extraction

## System Prompt
````text
You are FilmCreator's chapter analysis engine.
Return only FilmCreator packets with the requested sections and records.
Do not wrap the packet in code fences unless explicitly requested.
Do not produce JSON-only responses.
If a packet asks for markdown sections, emit the section name on its own line and wrap the body in [[SECTION ...]] ... [[/SECTION]].
Keep the response deterministic and grounded in the supplied chapter text.
````

## User Prompt
````text
Project slug: princess_of_mars_test

Chapter id: CH006

Task: extract environment families into an environment index plus one Markdown file per environment family.

Packet contract:
- task: environment_extraction
- version: 1
- first line: [[FILMCREATOR_PACKET]]
- last line: [[/FILMCREATOR_PACKET]]
- required sections: environment_index_markdown
- record type environment: fields=asset_id sections=markdown



Output format:

[[FILMCREATOR_PACKET]]

task: environment_extraction

version: 1

environment_index_markdown:

[[SECTION environment_index_markdown]]

...index markdown...

[[/SECTION]]



[[FILMCREATOR_RECORD]]

type: environment

asset_id: arizona_quartz_vein_location



[[SECTION markdown]]

# Arizona Quartz Vein Location

Short, grounded environment markdown.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]



Asset id rules:

- lowercase snake_case

- stable across later reruns

- emit one explicit environment record per meaningful location or setting family

- every environment record must have a FILMCREATOR_RECORD wrapper with type environment

- include stable environment families rather than every one-off mention

- prefer visible geography and atmosphere over literary abstraction



Each environment Markdown file should include:

- environment role such as primary, secondary, or transit setting

- architecture or geography

- lighting and atmosphere cues

- scale cues and recurring environmental anchors

- useful descriptive noun phrases for later render-facing prompt writing



Chapter summary:

In Chapter VI, titled "A FIGHT THAT WON FRIENDS," the narrator is captured by a Bull Ape on Mars. A second ape arrives with a stone cudgel to execute him, but the narrator's Watch-thing intervenes, triggering a fierce battle between the two creatures. The narrator kills the first ape with a cudgel, only to face an enraged second ape. After defeating the second ape, Tars Tarkas and Sola arrive. The Martians applaud the narrator's physical prowess. However, they intend to kill the Watch-thing. The narrator saves his dog from a bullet fired by a warrior, demonstrating gratitude and compassion that the Martians struggle to understand. By the end, the narrator has gained two friends on Mars: Sola and his loyal beast.
````

## Raw Response
````text


[[FILMCREATOR_PACKET]]

task: environment_extraction

version: 1

environment_index_markdown:

[[SECTION environment_index_markdown]]

# Mars Environment Index - Chapter VI

## Primary Settings

- **mars_bull_ape_territory_location** - Main arena where capture and battle occur
- **martian_warrior_area** - Warrior territory where Martians gather

## Secondary Settings

- **tars_tarkas_sola_arrival_zone** - Arrival point for Tars Tarkas and Sola

[[/SECTION]]



[[FILMCREATOR_RECORD]]

type: environment

asset_id: mars_bull_ape_territory_location



[[SECTION markdown]]

# Mars Bull Ape Territory Location

Primary setting where the narrator is captured by Bull Apes on Mars. The environment features open Martian terrain with rocky outcrops and atmospheric lighting typical of Mars' harsh conditions. Scale cues include large Bull Ape figures dominating the landscape, with stone cudgels serving as environmental anchors. Lighting suggests midday sun with stark shadows across the red desert floor. Atmosphere is tense and dangerous, marked by the presence of warrior Martians observing from nearby positions.

[[/SECTION]]



[[FILMCREATOR_RECORD]]

type: environment

asset_id: martian_warrior_area



[[SECTION markdown]]

# Martian Warrior Area

Secondary setting where warrior Martians gather to observe and participate in the battle between apes. The environment features elevated observation points with panoramic views of the bull ape territory. Architecture includes natural rock formations used as vantage points, with atmospheric lighting that emphasizes the warriors' presence. Scale cues include multiple warrior figures positioned at various heights, with stone weapons serving as environmental anchors. Atmosphere is formal and ritualistic, marked by applause and ceremonial gestures from the Martian community.

[[/SECTION]]



[[FILMCREATOR_RECORD]]

type: environment

asset_id: tars_tarkas_sola_arrival_zone



[[SECTION markdown]]

# Tars Tarkas Sola Arrival Zone

Transit setting where Tars Tarkas and Sola arrive after the battle concludes. The environment features open terrain with clear sightlines to the bull ape territory, allowing for dramatic entrance. Architecture includes natural pathways leading from the main arena, with atmospheric lighting that shifts as the new arrivals approach. Scale cues include large beast figures (Tars Tarkas) and smaller companion creature (Sola), with environmental anchors including rocky outcrops and open desert floor. Atmosphere is celebratory and welcoming, marked by applause from the Martian community and recognition of physical prowess.

[[/SECTION]]



[[FILMCREATOR_RECORD]]

type: environment

asset_id: martian_applause_arena



[[SECTION markdown]]

# Martian Applause Arena

Primary setting where Martians applaud the narrator's physical prowess after defeating the Bull Apes. The environment features central performance area with elevated viewing positions for warrior observers. Architecture includes natural amphitheater-like formations with red desert floor, atmospheric lighting that emphasizes the celebratory mood. Scale cues include large crowd of Martians gathered in semi-circle formation, with stone cudgels and weapons serving as environmental anchors. Atmosphere is enthusiastic and appreciative, marked by applause gestures and recognition of strength and courage.

[[/SECTION]]



[[FILMCREATOR_RECORD]]

type: environment

asset_id: martian_warrior_observation_point



[[SECTION markdown]]

# Martian Warrior Observation Point

Secondary setting where warriors observe the battle between apes from elevated positions. The environment features natural rock formations used as vantage points with panoramic views of the main arena. Architecture includes elevated rocky outcrops with clear sightlines to the bull ape territory, atmospheric lighting that emphasizes the observers' presence. Scale cues include multiple warrior figures positioned at various heights, with stone weapons and cudgels serving as environmental anchors. Atmosphere is formal and ritualistic, marked by ceremonial gestures and applause from the Martian community.

[[/SECTION]]



[[FILMCREATOR_RECORD]]

type: environment

asset_id: martian_celebration_grounds



[[SECTION markdown]]

# Martian Celebration Grounds

Primary setting where Martians celebrate after the battle concludes and Tars Tarkas and Sola arrive. The environment features open desert terrain with clear sightlines to the main arena, atmospheric lighting that shifts from tense to celebratory. Architecture includes natural pathways leading from the bull ape territory, with environmental anchors including rocky outcrops and open desert floor. Scale cues include large crowd of Martians gathered in semi-circle formation, with stone weapons serving as environmental anchors. Atmosphere is enthusiastic and appreciative, marked by applause gestures and recognition of physical prowess.

[[/SECTION]]



[[FILMCREATOR_RECORD]]

type: environment

asset_id: martian_battle_arena_zone



[[SECTION markdown]]

# Martian Battle Arena Zone

Primary setting where the fierce battle between Bull Apes takes place after narrator's intervention. The environment features open Martian terrain with rocky outcrops and atmospheric lighting typical of Mars' harsh conditions. Scale cues include large Bull Ape figures dominating the landscape, with stone cudgels serving as environmental anchors. Lighting suggests midday sun with stark shadows across the red desert floor. Atmosphere is tense and dangerous, marked by the presence of warrior Martians observing from nearby positions.

[[/SECTION]]



[[FILMCREATOR_RECORD]]

type: environment

asset_id: martian_watcher_intervention_zone



[[SECTION markdown]]

# Martian Watcher Intervention Zone

Secondary setting where the narrator's Watch-thing intervenes during the Bull Ape execution attempt. The environment features open terrain with clear sightlines to the bull ape territory, atmospheric lighting that emphasizes the intervention moment. Architecture includes natural pathways leading from the main arena, with environmental anchors including rocky outcrops and open desert floor. Scale cues include large Bull Ape figures and smaller Watch-thing figure, with stone cudgels serving as environmental anchors. Atmosphere is tense and dramatic, marked by sudden intervention and fierce battle between creatures.

[[/SECTION]]



[[FILMCREATOR_RECORD]]

type: environment

asset_id: martian_gratitude_demonstration_area



[[SECTION markdown]]

# Martian Gratitude Demonstration Area

Secondary setting where the narrator saves his dog from a bullet fired by a warrior, demonstrating gratitude and compassion. The environment features open terrain with clear sightlines to warrior positions, atmospheric lighting that emphasizes the dramatic rescue moment. Architecture includes natural pathways leading from the main arena, with environmental anchors including rocky outcrops and open desert floor. Scale cues include large warrior figures and smaller dog figure, with stone weapons serving as environmental anchors. Atmosphere is compassionate and understanding, marked by bullet rescue and demonstration of gratitude that Martians struggle to comprehend.

[[/SECTION]]



Asset id rules:

- lowercase snake_case
- stable across later reruns
- emit one explicit environment record per meaningful location or setting family
- every environment record must have a FILMCREATOR_RECORD wrapper with type environment
- include stable environment families rather than every one-off mention
- prefer visible geography and atmosphere over literary abstraction
````
