# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-20T01:08:08.565364+00:00
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

Chapter id: CH011

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

*   **Scene 1: New Quarters & Sarkoja's Threat.** Carter arrives with Sola and Dejah Thoris at a new, ancient building near the audience chamber. He dismisses female guards to prevent Sarkoja from harming Dejah Thoris, threatening her demise if she continues her cruel attentions.
*   **Scene 2: Thark Hierarchy & Rank.** Sola explains Carter's promotion to eleventh Chieftain, noting his metal rank is close to Tars Tarkas (second only to Lorquas Ptomel). She clarifies that killing Lorquas Ptomel would make him first, but requires council approval or self-defense.
*   **Scene 3: Ancient Architecture & Frescoes.** They inspect the new quarters, which feature elaborate decorations of fair-haired, beardless Martians in robes. Dejah Thoris is captivated by the art of extinct people, while Sola ignores it. The room includes ancient metal beds and sleeping apartments.
*   **Scene 4: Origin Debate.** Dejah Thoris questions Carter's claim of being from Earth/Virginia, noting Barsoomians speak one tongue but he claims recent learning. She pleads for a denial, fearing the horror of a man returning from the "Barsoomian heaven or hell." Carter explains his Earth origin and Virginia customs.
*   **Scene 5: Belief & Martian Technology.** Dejah Thoris eventually believes him due to her emotional connection ("heart tells me that I believe"). She asks about Earth, explaining how Martians view other planets via screens/instruments. She notes the lack of ornaments on Carter proves his un-Barsoomian origin.
*   **Scene 6: History of Korad.** Dejah Thoris explains the history of the red race mixing with ancient fair-haired Martians and dark races due to drying seas. They discuss the city of Korad, built near a natural harbor, and the lost civilization of the ancient Martians.
*   **Scene 7: Conclusion.** After exploring the building and discussing customs, Carter receives a summons from Lorquas Ptomel to appear before him in the audience chamber.
````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
task: environment_extraction
version: 1

[[SECTION environment_index_markdown]]
# Environment Index: CH011

- **ancient_quarters_building**: Primary residence/inspection area for Carter, Sola, and Dejah Thoris. Features ancient frescoes and metal furniture.
- **audience_chamber**: High-status location near the quarters where Lorquas Ptomel resides. Destination for summons.
[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: ancient_quarters_building

[[SECTION markdown]]
## Role
Primary residence and inspection space for Carter, Sola, and Dejah Thoris.

## Architecture & Geography
Ancient building structure containing sleeping apartments. Located adjacent to the audience chamber.

## Lighting & Atmosphere
Dimly lit by age; atmosphere of antiquity emphasized by frescoes.

## Scale & Anchors
Large sleeping apartments; ancient metal beds serve as primary anchors.

## Descriptive Noun Phrases
- Fair-haired beardless Martians in robes
- Ancient metal beds
- Elaborate decorations
- Extinct people art
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: audience_chamber

[[SECTION markdown]]
## Role
Secondary setting / Destination for high-ranking summons.

## Architecture & Geography
Audience chamber near the new building; implies formal gathering space.

## Lighting & Atmosphere
Formal atmosphere associated with Lorquas Ptomel's rank.

## Scale & Anchors
Central audience area; proximity to quarters suggests connected complex.

## Descriptive Noun Phrases
- Audience chamber
- High-status location
[[/SECTION]]
[[/FILMCREATOR_RECORD]]
[[/FILMCREATOR_PACKET]]
````
