# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-20T02:29:05.131257+00:00
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

Chapter id: CH013

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

# Chapter Summary: CHAPTER XIII (LOVE-MAKING ON MARS)

## Story Summary
Following the battle with air ships, the Thark community remains in the city for safety, abandoning their march home until they are assured the ships will not return. During this period of inactivity, John Carter undergoes intensive training with Tars Tarkas in Thark customs and warfare, specifically learning to ride and guide thoats. He demonstrates that kindness is more effective than violence in training these beasts, earning a reward from Lorquas Ptomel—a massive gold anklet—for his regiment of docile mounts.

On the eve of their departure march toward Thark city, John Carter arranges a secret meeting with Dejah Thoris on a great avenue leading into the plaza. They discuss the warriors' jealousy and dangerous treatment of her. An intimate moment occurs where John places his arm around her shoulder, confirming mutual affection. The chapter concludes with John's internal realization that he has loved Dejah Thoris since their first meeting in Korad, solidifying their bond despite the hostile environment.

## Visual Continuity Facts
### Locations and Environment
- **City Courtyard/Plaza:** Where the community resides and where training takes place.
- **Great Avenue:** Leads into the plaza from the east; setting for the secret meeting.
- **Martian Night:** Lighted by two moons, with Earth visible in the luminous green eye above.

### Objects and Artifacts
- **Thoats:** Great beasts used as mounts; dangerous but tractable when trained.
- **Pistol:** Used by John to subdue unresponsive thoats during training.
- **Gold Anklet:** Reward presented by Lorquas Ptomel from his own leg.
- **Silks:** Worn by John, removed and thrown across Dejah's shoulders for warmth.
- **Radium Powder/Projectiles:** Mentioned in context of Thark warfare (exploding bullets).

### Character Actions and States
- **John Carter:** Instructed in riding, training beasts, walking with Dejah, removing silks, placing arm on shoulder.
- **Dejah Thoris:** Absent from quarters during day, walking with Sola, meeting John secretly, smiling at John's approach.
- **Tars Tarkas:** Present for instruction (past tense in specific scenes), observing John's training.
- **Lorquas Ptomel:** Present for reward ceremony (mentioned).

### Time and Sequence
- **Day to Night Transition:** Occurs during the conversation on the avenue.
- **Eve of Departure:** The meeting happens immediately before the march resumes.
- **Duration:** Several days of inactivity followed by the specific evening event.
````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
task: environment_extraction
version: 1

[[SECTION environment_index_markdown]]
# Environment Index - Chapter XIII

## Primary Environments
- city_courtyard_plaza - Main community residence and training location
- great_avenue - Secret meeting setting leading into plaza
- martian_night - Atmospheric night environment with celestial bodies

## Secondary/Transit Environments
- thark_city_quarters - Character living spaces (mentioned)
- eastern_approach - Avenue entrance from east side

[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: city_courtyard_plaza

[[SECTION markdown]]
# City Courtyard Plaza

## Environment Role
Primary setting for Thark community residence and training activities

## Architecture and Geography
Open courtyard space within Thark city walls, plaza-style gathering area with eastern approach leading into main plaza. Flat ground suitable for beast training and movement.

## Lighting and Atmosphere
Daylight conditions transitioning to evening light during John's secret meeting. Martian ambient lighting with two moons visible in night scenes. Green atmospheric glow from Earth above.

## Scale Cues and Environmental Anchors
Large enough space for multiple Thoats to train simultaneously. Community buildings surrounding courtyard perimeter. Eastern avenue entrance serves as directional anchor point.

## Descriptive Noun Phrases
- Thark community residence area
- Beast training courtyard
- Eastern plaza approach
- Day-to-evening transition zone
- Two-moon lit gathering space
- Green Earth-glow atmosphere
- Community building perimeter
- Open ground training area

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: great_avenue

[[SECTION markdown]]
# Great Avenue

## Environment Role
Secondary/transit setting for secret intimate meeting between John and Dejah

## Architecture and Geography
Wide paved avenue leading from eastern approach into main plaza. Elevated walkway suitable for private conversation. Leads toward city center plaza entrance.

## Lighting and Atmosphere
Evening light conditions during secret meeting. Two moons visible in Martian night sky above. Green atmospheric glow from Earth luminous eye overhead.

## Scale Cues and Environmental Anchors
Wide enough for two characters to walk side-by-side. Eastern entrance serves as directional anchor. Plaza entrance at western terminus provides destination marker.

## Descriptive Noun Phrases
- Secret meeting avenue
- Eastern plaza approach path
- Two-moon lit walkway
- Green Earth-glow overhead
- Private conversation corridor
- Evening light transition zone
- City center leading passage
- Elevated ground walking area

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: martian_night

[[SECTION markdown]]
# Martian Night

## Environment Role
Atmospheric primary setting for celestial and environmental mood establishment

## Architecture and Geography
Open sky environment above Thark city. No physical architecture - pure atmospheric space with celestial bodies as main features. Ground level beneath two moons.

## Lighting and Atmosphere
Two-moon illumination creating dual light sources. Green luminous eye of Earth visible in night sky. Martian ambient darkness punctuated by celestial glow. Evening to night transition lighting.

## Scale Cues and Environmental Anchors
Vast sky space above city courtyard and avenue. Two moons serve as primary directional anchors. Earth's green glow provides atmospheric reference point. City buildings below create scale contrast.

## Descriptive Noun Phrases
- Two-moon lit Martian sky
- Green Earth luminous eye
- Celestial night atmosphere
- Dual moon illumination zone
- Atmospheric glow environment
- Night sky above city
- Evening darkness transition
- Open celestial space

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
