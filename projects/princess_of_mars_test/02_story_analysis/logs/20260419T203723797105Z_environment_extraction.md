# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-19T20:37:23.797105+00:00
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

Chapter id: CH018

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

**Story Summary:**
1.  **Awakening:** Narrator regains consciousness in a Warhoon camp room with sleeping silks/furs; ancient female and scarred jed (Dak Kova) present.
2.  **Departure:** Dak Kova plans to use narrator for "great games"; narrator strapped to wild thoat, escorted by warriors to main column.
3.  **Audience:** Reach Warhoon camp near dark; narrator taken before Jeddak Bar Comas.
4.  **Conflict & Battle:** Dak Kova insults Bar Comas and presents narrator for battle; Bar Comas kills Dak Kova in brutal hand-to-hand fight (tusks, slashing).
5.  **Ascension:** Bar Comas dies; Dak Kova becomes new Jeddak of Warhoon after three days (foot on neck of dead ruler).
6.  **Expedition Cancelled:** Injuries delay march; raid on Thark community postponed until after great games; warriors turn back to Warhoon.
7.  **Imprisonment:** Narrator cast into dungeon in Warhoon city, heavily chained to floor/walls; utter darkness, creeping things.
8.  **Escape Attempt:** Narrator kills jailer with chain to obtain keys; regains reason.
9.  **Discovery:** Six pairs of gleaming eyes approach and retreat from the darkness.

**Visual Continuity Facts:**
-   **Characters:** Green skin, tusks (single broken tusk on Dak Kova), ornaments (human skulls/hands strapped to breast).
-   **Animals:** Wild thoats (unmanageable, prone to bolting).
-   **Environment:** Small room with sleeping silks/furs; mossy floor; inky blackness of dungeon; creeping/crawling things; cold sinuous bodies.
-   **Lighting:** Dim torch light for food delivery; total darkness in dungeon; gleaming fiery eyes visible only in dark.
````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
task: environment_extraction
version: 1

[[SECTION environment_index_markdown]]
# Warhoon Environment Index

## warhoon_camp_room
- **Role:** Primary Setting
- **Description:** Small room with sleeping silks/furs; mossy floor. Dim torch light for food delivery.
- **Atmosphere:** Organic textures of furs contrast with cold stone/moss. Shadowed interior.

## warhoon_dungeon
- **Role:** Secondary/Transit Setting
- **Description:** Inky blackness of dungeon; utter darkness, creeping things; cold sinuous bodies. Gleaming fiery eyes visible only in dark.
- **Atmosphere:** Total darkness; oppressive atmosphere with creeping shadows. Cold, underground cell.
[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: warhoon_camp_room

[[SECTION markdown]]
## Warhoon Camp Room

**Role:** Primary Setting

**Architecture/Geography:** Small enclosed room within the Warhoon camp structure. Floor covered with moss and sleeping silks/furs.

**Lighting/Atmosphere:** Dim torch light used for food delivery; otherwise shadowed interior. Warm, organic textures of furs contrast with cold stone/moss.

**Scale/Anchors:** Human scale room; bed or resting area implied by silks/furs.

**Descriptive Noun Phrases:** Sleeping silks, mossy floor, dim torch light, Warhoon camp interior.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: warhoon_dungeon

[[SECTION markdown]]
## Warhoon Dungeon

**Role:** Secondary/Transit Setting

**Architecture/Geography:** Deep underground cell within the Warhoon city. Walls and floor heavily chained to anchor the prisoner.

**Lighting/Atmosphere:** Total darkness; inky blackness. Only light sources are gleaming fiery eyes of approaching entities. Cold, oppressive atmosphere with creeping shadows.

**Scale/Anchors:** Human scale cell; heavy chains on floor/walls serve as primary anchors.

**Descriptive Noun Phrases:** Inky blackness, utter darkness, creeping things, cold sinuous bodies, gleaming fiery eyes.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]
````
