# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-20T07:18:33.876792+00:00
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

Chapter id: CH009

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

Chapter IX details the protagonist's rapid acquisition of the Martian language and his subsequent weapons training under the tutelage of local women, who are responsible for manufacturing all goods and educating the youth. The chapter highlights the gendered division of labor in Martian society, with men handling strategy and law while women manage production and combat training. A significant portion focuses on a discussion regarding the fate of a female prisoner, where Sola expresses compassion and critiques the constant warfare, contrasting her views with the harsher attitudes of others like Sarkoja. The chapter concludes with the protagonist deciding to seek Sola's assistance for an escape plan.
````

## Raw Response
````text


[[FILMCREATOR_PACKET]]

task: environment_extraction

version: 1

environment_index_markdown:

[[SECTION environment_index_markdown]]
# Environment Index - Chapter IX (princess_of_mars_test)

## Training Grounds
- **arizona_quartz_vein_location** - Primary weapons training setting where protagonist receives instruction from local women

## Prison Facilities  
- **martian_prisoner_holding_area** - Secondary location where female prisoner is detained and discussed by community members

## Martian Settlement Core
- **martian_community_workspace** - Transit/primary setting where women manufacture goods, educate youth, and conduct daily operations

[[/SECTION]]



[[FILMCREATOR_RECORD]]

type: environment

asset_id: arizona_quartz_vein_location



[[SECTION markdown]]
# Arizona Quartz Vein Location

Primary weapons training ground. Grounded, industrial atmosphere with focused lighting for combat instruction. Medium-scale facility with recurring environmental anchors of weapon racks and training dummies. Architecture suggests functional, utilitarian design prioritizing safety and efficiency. Lighting cues indicate controlled visibility for tactical demonstrations. Atmosphere carries tension between discipline and mentorship. Scale anchored by open floor space accommodating multiple trainees simultaneously.

[[/SECTION]]



[[FILMCREATOR_RECORD]]

type: environment

asset_id: martian_prisoner_holding_area



[[SECTION markdown]]
# Martian Prisoner Holding Area

Secondary detention facility within community infrastructure. Dim, subdued lighting with restricted access points. Small-scale enclosure designed for secure containment of female prisoner. Architecture emphasizes security over comfort with reinforced barriers and monitoring stations. Atmosphere carries weight of institutional authority and community judgment. Scale anchored by observation windows allowing community members to view prisoner status. Lighting cues suggest minimal illumination for surveillance purposes.

[[/SECTION]]



[[FILMCREATOR_RECORD]]

type: environment

asset_id: martian_community_workspace



[[SECTION markdown]]
# Martian Community Workspace

Primary settlement core where women manufacture goods and educate youth. Bright, communal atmosphere with natural lighting from open structures. Large-scale facility serving multiple functions including production, instruction, and social gathering. Architecture combines workshop elements with educational spaces featuring demonstration areas. Atmosphere reflects gendered division of labor with organized workstations and teaching stations. Scale anchored by central gathering area accommodating community discussions and training sessions. Lighting cues indicate daylight-dominant environment with practical illumination for detailed craftwork.

[[/SECTION]]



[[FILMCREATOR_RECORD]]

type: environment

asset_id: martian_training_corridor



[[SECTION markdown]]
# Martian Training Corridor

Transit setting connecting training grounds to community workspace. Medium-scale passage with functional lighting and directional flow markers. Architecture suggests purpose-built pathway for movement between instructional areas. Atmosphere carries transitional energy between discipline and daily operations. Scale anchored by consistent width accommodating weapon transport and trainee movement. Lighting cues indicate practical illumination for safe passage through facility zones.

[[/SECTION]]



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
````
