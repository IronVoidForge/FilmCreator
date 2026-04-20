# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-20T03:32:37.192561+00:00
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

Chapter id: CH006

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

# Chapter Summary: A Fight That Won Friends

## Scene 1: The Bull Ape Confrontation
**Action:** The protagonist is pinned to the ground by a bull ape holding him with one huge foot. The ape jabbers and gesticulates at another creature behind it. A mate approaches bearing a mighty stone cudgel intended to brain the protagonist.
**Visual Continuity:** The bull ape is described as having intermediary arms/legs, close-together non-protruding eyes, high-set lateral ears, and snouts/teeth like an African gorilla. It is "not unlovely" compared to green Martians.
**Climax:** A bolt of myriad-legged horror (the beast) hurled itself through the doorway onto the executioner's breast. The ape holding the protagonist leaps through the window, but its mate engages in a death struggle with the beast.

## Scene 2: The Battle and Protagonist's Intervention
**Action:** The protagonist witnesses the battle between the beast and the bull ape. The beast gains an advantage by sinking fangs into the ape's breast, but the ape locks the throat of the guardian. The beast weakens (eyes bulging, blood from nostrils).
**Visual Continuity:** Both creatures roll back and forth on the floor without emitting sound of fear or pain. The beast's eyes bulge completely from sockets; blood flows from nostrils.
**Intervention:** The protagonist gains his feet, backs against the wall, and seizes the cudgel. He crashes it full upon the head of the ape, crushing his skull as though it had been an eggshell.

## Scene 3: Arrival of Tars Tarkas and Warriors
**Action:** Immediately after the blow, a new danger appears. The bull ape's mate returns to the scene roaring in rage at his lifeless fellow. The protagonist considers flight but is drawn back by the beast's pitiful appeal for protection.
**Visual Continuity:** The protagonist throws the cudgel as heavily as possible at the advancing bulk of the mate, striking him just below the knees. He follows with a smashing left to the pit of the stomach.
**Resolution:** The mate reeled and fell upon the floor doubled up with pain. The protagonist leaps over his prostrate body and finishes the monster before he could regain his feet.

## Scene 4: Martians Witness the Victory
**Action:** A low laugh rings out behind the protagonist. He turns to behold Tars Tarkas, Sola, and three or four warriors standing in the doorway. They offer zealously guarded applause for his feats.
**Visual Continuity:** The Martians are devoid of finer sentiments; they worship physical prowess. Sola is sober with apparent solicitude, unlike others whose faces were twisted in laughter. She rushes to examine the protagonist's body for wounds.

## Scene 5: Saving the Beast from Execution
**Action:** Tars Tarkas and warriors enter and stand over the rapidly reviving brute (the beast). They seem deep in argument. A warrior draws an evil-looking pistol intending to put an end to the creature.
**Visual Continuity:** The protagonist springs forward and strikes up the warrior's arm. The bullet striking the wooden casing of the window explodes, blowing a hole completely through the wood and masonry.
**Resolution:** The protagonist kneels beside the beast, raises it to its feet, and motions for it to follow him. The Martians look on with ludicrous surprise.

## Scene 6: Return to the Plaza
**Action:** Tars Tarkas signs that the protagonist be left to his own devices. They return to the plaza with the great beast following close at heel. Sola grasps the protagonist tightly by the arm.
**Visual Continuity:** The beast follows close at heel; Sola grasps me tightly by the arm.
**Conclusion:** The protagonist now has two friends on Mars: a young woman (Sola) and a dumb brute (the beast).
````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
task: environment_extraction
version: 1

[[SECTION environment_index_markdown]]
# Environment Index - Chapter CH006

## Interior Combat Space (Primary Setting)
- Role: Primary setting for confrontation and battle sequences
- Features: Floor, walls, doorway with wooden casing, window with wooden casing
- Atmosphere: Tense combat zone with physical violence occurring

## Doorway/Entrance (Transit Setting)
- Role: Transit point between interior and exterior spaces
- Features: Wooden casing, doorway structure, multiple Martians standing here
- Atmosphere: Threshold of observation and intervention

## Window (Secondary Setting)
- Role: Secondary setting for escape routes and structural damage
- Features: Wooden casing, glass/masonry elements
- Atmosphere: Vulnerable point during combat sequences

## Plaza (Destination Setting)
- Role: Exterior destination and social gathering space
- Features: Open plaza area, return location after victory
- Atmosphere: Social observation zone with Martians present

[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: interior_combat_space

[[SECTION markdown]]
# Interior Combat Space

## Environment Role
Primary setting for confrontation and battle sequences where the protagonist engages multiple bull apes and the beast.

## Architecture or Geography
Interior room space with defined floor area, vertical walls, doorway entrance, and window opening. Wooden casing frames both doorway and window structures.

## Lighting and Atmosphere Cues
Combat-lit interior with physical violence occurring. No specific lighting descriptors but implied functional illumination for movement and action sequences. Tense atmosphere marked by roaring, jabbering creatures and physical struggle.

## Scale Cues and Recurring Environmental Anchors
Floor serves as primary combat surface where creatures roll back and forth. Walls provide backing position for protagonist during intervention moments. Doorway and window act as structural anchors marking escape routes and entry points. Wooden casing on both doorway and window are recurring damage points during battle sequences.

## Useful Descriptive Noun Phrases
- Interior room with wooden-framed doorway
- Combat floor surface
- Wall-backed confrontation zone
- Window with wooden casing structure
- Doorway entrance threshold
- Masonry and wood structural elements
- Floor space for creature movement
- Vertical wall surfaces
- Wooden frame structures

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: doorway_entrance

[[SECTION markdown]]
# Doorway Entrance

## Environment Role
Transit setting between interior combat space and exterior plaza, serving as observation point for Martians.

## Architecture or Geography
Doorway structure with wooden casing framing the entrance. Threshold connecting interior room to exterior plaza space. Multiple Martians stand here during victory celebration sequences.

## Lighting and Atmosphere Cues
Threshold lighting marking transition between spaces. Appearances of Martians in doorway suggest well-lit exterior connection. Atmosphere shifts from combat intensity to social observation when Martians appear.

## Scale Cues and Recurring Environmental Anchors
Doorway width accommodates multiple Martians standing together. Wooden casing provides structural anchor point for bullet impact sequences. Doorway serves as primary entry/exit point for protagonist movement between spaces.

## Useful Descriptive Noun Phrases
- Doorway with wooden casing structure
- Entrance threshold zone
- Multiple Martian observation point
- Transition space between interior and exterior
- Wooden frame doorway structure
- Threshold for social gathering
- Entry point for protagonist movement
- Doorway opening structure
- Casing-framed entrance

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: window_structure

[[SECTION markdown]]
# Window Structure

## Environment Role
Secondary setting for escape routes and structural damage points during combat sequences.

## Architecture or Geography
Window opening with wooden casing structure. Glass or masonry elements within the frame. Structural element connecting interior space to exterior environment.

## Lighting and Atmosphere Cues
Window provides light source from exterior. Wooden casing frames the opening. Damage occurs when bullet strikes wooden casing, blowing hole through wood and masonry.

## Scale Cues and Recurring Environmental Anchors
Window size accommodates escape routes for creatures jumping through. Wooden casing serves as impact target during combat sequences. Window acts as structural anchor marking vulnerable points in interior walls.

## Useful Descriptive Noun Phrases
- Window with wooden casing structure
- Glass or masonry window frame
- Structural opening element
- Escape route aperture
- Wooden frame window structure
- Impact target for projectile damage
- Interior wall opening
- Window glass surface
- Masonry and wood structural elements

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: plaza_destination

[[SECTION markdown]]
# Plaza Destination

## Environment Role
Exterior destination and social gathering space where Martians observe victory and protagonist receives recognition.

## Architecture or Geography
Open exterior plaza area serving as return location after combat sequences. Social observation zone with multiple Martians present including Tars Tarkas, Sola, and warriors.

## Lighting and Atmosphere Cues
Exterior daylight illumination for plaza space. Social atmosphere marked by applause, laughter, and solemn observation from different Martian characters.

## Scale Cues and Recurring Environmental Anchors
Plaza accommodates multiple Martians standing together in doorway view. Open exterior space contrasts with interior combat room. Plaza serves as destination anchor after victory sequences.

## Useful Descriptive Noun Phrases
- Exterior plaza gathering space
- Open outdoor area
- Social observation zone
- Destination return location
- Martian social gathering point
- Exterior daylight environment
- Plaza entrance threshold
- Open exterior space
- Social applause zone

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
