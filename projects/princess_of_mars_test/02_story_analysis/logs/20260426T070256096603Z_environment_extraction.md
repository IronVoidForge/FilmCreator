# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-26T07:02:56.096603+00:00
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

Chapter id: CH022

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

**Setting:**
The palace of Zodanga, specifically the private apartments of Jeddak Than Kosis, winding corridors, antechambers, and a great hall with a balcony overlooking a Zodangan avenue.

**Characters:**
* **John Carter:** A human warrior serving as a guard in Zodanga; he is searching for Dejah Thoris.
* **Dejah Thoris:** Princess of Helium; she has publicly pledged herself to Sab Than to ensure peace between their nations.
* **Than Kosis:** The Jeddak (ruler) of Zodanga.
* **Sab Than:** Prince of Zodanga and son of Than Kosis.
* **Notan:** The Royal Psychologist.
* **Guardsmen:** Four unnamed Zodangan soldiers killed by Carter during his confrontation.

**Events:**
* **The Betrayal:** While stationed behind a tapestry to guard Than Kosis, John Carter witnesses Dejah Thoris enter the chamber and publicly declare her intention to marry Sab Than, effectively renouncing her previous connection to Carter.
* **The Confrontation:** Distraught, Carter abandons his post to find Dejah Thoris. He is intercepted by four guards in an antechamber. After a fierce battle lasting twenty minutes, Carter kills all four guardsmen.
* **The Reunion:** Carter confronts Dejah Thoris. She recognizes him but explains that due to Barsoomian custom, her promise to marry Sab Than is final and binding, even if she still loves Carter. She informs him that he cannot wed her while Sab Than lives, nor can he wed a man who kills her husband.
* **The Investigation:** As the palace goes into an uproar over the murdered guards, Carter hides in a large hanging ornament in a great hall. He overhears the Royal Psychologist, Notan, reporting to Than Kosis that a single, superhuman fighter was responsible for the deaths.
* **The Escape:** Realizing he is a wanted man, Carter waits for darkness to fall and uses his superior physical abilities to leap from a balcony and escape the palace grounds into the city of Zodanga.
````

## Raw Response
````text
[[FILMCREATOR_PACKET]]

task: environment_extraction

version: 1

environment_index_markdown:

[[SECTION environment_index_markdown]]

# Environment Index: CH022

- [zodanga_palace_interior](zodanga_palace_interior)
- [zodanga_city_streets](zodanga_city_streets)

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: zodanga_palace_interior

[[SECTION markdown]]

# Zodanga Palace Interior

**Role:** Primary setting.

**Architecture or Geography:** A complex of private apartments, winding corridors, and formal antechambers. Features include heavy tapestries used for concealment, large hanging ornaments/decorations suitable for hiding, and a great hall with high ceilings.

**Lighting and Atmosphere Cues:** Formal and oppressive; transitions from the controlled lighting of royal chambers to the sudden chaos of combat in narrow halls; shifts to darkness during the escape sequence.

**Scale Cues and Recurring Environmental Anchors:** Grand scale indicated by wide halls and balconies; recurring anchors include heavy tapestries, ornate hanging decorations, and stone/metal architectural details typical of Zodangan royalty.

**Descriptive Noun Phrases:** Winding palace corridors, royal antechambers, heavy ceremonial tapestries, grand hall with balcony, large hanging ornaments, Zodangan palace architecture.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: zodanga_city_streets

[[SECTION markdown]]

# Zodanga City Streets

**Role:** Transit setting / Escape route.

**Architecture or Geography:** Urban landscape viewed from height; wide avenues visible from palace balconies.

**Lighting and Atmosphere Cues:** Nighttime/darkness; high-contrast shadows; sense of urgency and pursuit.

**Scale Cues and Recurring Environmental Anchors:** Vast urban expanse seen from elevated vantage points; city streets stretching away from the palace grounds.

**Descriptive Noun Phrases:** Zodangan avenues, nocturnal cityscapes, urban street canyons, palace balcony overlook.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
