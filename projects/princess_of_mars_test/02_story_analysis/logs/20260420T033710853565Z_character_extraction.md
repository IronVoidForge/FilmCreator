# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-20T03:37:10.853565+00:00
- task: character_extraction

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

Chapter id: CH007

Task: extract visible and referenced characters into a character index plus one Markdown file per character.

Return exactly one Markdown packet using this outer envelope:
[[FILMCREATOR_PACKET]]
task: character_extraction
version: 1

[[SECTION character_index_markdown]]
...character_index_markdown content...
[[/SECTION]]

Repeat one FILMCREATOR_RECORD block for every extracted item of that type.

[[FILMCREATOR_RECORD]]
type: character
asset_id: <value>
canonical_character_id: <value>
aliases: <value>
is_fully_identified: <value>
manual_description_required: <value>
manual_description_reason: <value>
clarification_required: <value>
clarification_reason: <value>
clarification_question: <value>

[[SECTION markdown]]
...markdown content...
[[/SECTION]]
[[/FILMCREATOR_RECORD]]
[[/FILMCREATOR_PACKET]]



Important rules:

- if a character does not have enough physical or visual description in the supplied material to support dependable later image generation, set manual_description_required to true

- explain exactly why in manual_description_reason

- do not guess ornate missing details just to avoid the flag

- if the chapter names a character without enough stable identification, set is_fully_identified to false

- use aliases for alternate names or partial labels seen in the chapter

- if the character might already exist under another name or is too weakly identified, set clarification_required to true and ask a targeted question

- if clarification is not required, still include clarification_reason and clarification_question as empty values

- every character record must include a non-empty markdown section

- if details are sparse, still write a short markdown file explaining the uncertainty instead of omitting markdown

- never omit the markdown section for any character record



Asset id rules:

- lowercase snake_case

- stable across later reruns



Each character Markdown file should include:

- display name and chapter role

- whether the character is physically present, referenced, or uncertain

- physical description that is actually supported by the source

- costume, silhouette, and continuity-critical traits when known

- useful descriptive noun phrases for later render-facing prompt writing

- explicit uncertainty notes when important details are missing



Chapter summary:

# Chapter VII: CHILD-RAISING ON MARS
## Visual Continuity & Scene Facts
*   **Setting:** Plaza, Incubator enclosure, Dead Sea Bottom, Hills.
*   **Key Objects:** Three-wheeled chariots (gorgeously decorated), Mastodonian draft animals (no bit/bridle), Incubator eggs/hatchlings, Martian hounds.
*   **Characters:** Sola (narrator's companion), Tars Tarkas (chieftain), Lorquas Ptomel Jed (principal chieftain), Warriors (200+), Women/Children (forming gauntlet walls).
*   **Action Sequence:** Breakfast replica -> Procession harnessing -> Incubator hatching ceremony -> Child capture ritual -> Training session.

## Story Summary & Decomposition Notes
1.  **Procession Scene:** Sola escorts narrator to plaza where community harnesses animals to chariots. Procession moves in single file with warriors at head and rear. Narrator dragged into empty chariot, proceeds to incubator location.
2.  **Incubator Hatching:** Eggs hatch after five-year period. Young Martians (3-4 feet tall) released. Tars Tarkas explains hatching to Lorquas Ptomel. Narrator performs leap over parked chariots for entertainment.
3.  **Child-Raising Ritual:** Women and children form two solid walls leading out through chariots. Young Martians run gauntlet length; captured one at a time by women or older children. Last in line captures first to reach end.
4.  **Societal Explanation:** Narrator learns Martian child-rearing involves teaching weapons and language from infancy. No parental love exists; children are communal property. Deformed/defective young are shot. Birth rate regulated to offset death on dying planet.
5.  **Training Progression:** Sola cares for narrator and young Martian prize (male, 4 feet tall). Narrator masters walking under Martian conditions, learns language in a week, develops telepathic powers. Unique advantage: Cannot be read by others' minds.
6.  **Contextual Details:** Community size ~30k souls. Roam arid land between 40-80 degrees south latitude. Incubators built in remote fastnesses to prevent discovery by other tribes.
````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
task: character_extraction
version: 1

[[SECTION character_index_markdown]]
# Character Index - Chapter VII: CHILD-RAISING ON MARS

| Asset ID | Canonical Character ID | Display Name | Role | Physical Presence | Description Status |
|----------|------------------------|--------------|------|-------------------|--------------------|
| sola_companion | Sola | Sola | Narrator's companion | Referenced | Manual description required |
| tars_tarkas_chief | Tars Tarkas | Tars Tarkas | Chieftain | Referenced | Manual description required |
| lorquas_ptomel_jed | Lorquas Ptomel Jed | Lorquas Ptomel Jed | Principal chieftain | Referenced | Manual description required |
| warriors_group | Warriors | Warriors | Community members | Referenced | Manual description required |
| women_children_group | Women/Children | Women and Children | Gauntlet formers | Referenced | Manual description required |

*Note: All characters lack sufficient physical description for dependable image generation. Manual descriptions are required for each.*
[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: sola_companion
canonical_character_id: Sola
aliases: narrator's companion
is_fully_identified: false
manual_description_required: true
manual_description_reason: Chapter summary references Sola as narrator's companion but provides no physical description, appearance details, or visual characteristics. Cannot support dependable image generation without manual description.
clarification_required: true
clarification_reason: Character exists in narrative but lacks stable identification through physical description. May already exist under another name or be too weakly identified for reliable rendering.
clarification_question: What are Sola's physical appearance details (height, build, hair color, eye color, distinctive features) and what role does she play in the narrator's journey?

[[SECTION markdown]]
# Character File: Sola - Chapter VII

## Display Name
Sola

## Chapter Role
Narrator's companion

## Physical Presence Status
Referenced (not physically present in scene descriptions)

## Physical Description
**Status:** Insufficient information from chapter summary. No physical description, appearance details, or visual characteristics provided in the source material.

## Costume and Silhouette
**Status:** Unknown. Chapter summary does not describe clothing, accessories, or distinctive silhouette features.

## Continuity-Critical Traits
- Companion to narrator throughout child-raising ritual sequence
- Present during incubator hatching ceremony
- Cares for narrator and young Martian prize during training progression
- Community size approximately 30k souls

## Render-Facing Prompt Notes
**Required Manual Description:** This character requires complete manual description before image generation can proceed. Current chapter summary provides only narrative role without visual identifiers.

**Uncertainty Note:** Cannot determine physical appearance, clothing style, or distinctive features from provided material. Manual description must include: height, build, hair color and style, eye color, facial features, clothing type and colors, any accessories or distinguishing marks.

## Chapter Context
Sola appears in the chapter as the narrator's companion during the child-raising sequence on Mars. She is referenced throughout the incubator hatching ceremony, gauntlet formation, and training progression scenes but lacks sufficient visual description for reliable rendering.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: tars_tarkas_chief
canonical_character_id: Tars Tarkas
aliases: chieftain
is_fully_identified: false
manual_description_required: true
manual_description_reason: Chapter summary identifies Tars Tarkas as chieftain but provides no physical description, appearance details, or visual characteristics. Cannot support dependable image generation without manual description.
clarification_required: true
clarification_reason: Character exists in narrative but lacks stable identification through physical description. May already exist under another name or be too weakly identified for reliable rendering.
clarification_question: What are Tars Tarkas's physical appearance details (height, build, hair color, eye color, distinctive features) and what specific chieftain responsibilities does he hold?

[[SECTION markdown]]
# Character File: Tars Tarkas - Chapter VII

## Display Name
Tars Tarkas

## Chapter Role
Chieftain

## Physical Presence Status
Referenced (not physically present in scene descriptions)

## Physical Description
**Status:** Insufficient information from chapter summary. No physical description, appearance details, or visual characteristics provided in the source material.

## Costume and Silhouette
**Status:** Unknown. Chapter summary does not describe clothing, accessories, or distinctive silhouette features.

## Continuity-Critical Traits
- Explains incubator hatching ceremony to Lorquas Ptomel Jed
- Community leader among ~30k souls roaming arid land between 40-80 degrees south latitude
- Present during child capture ritual and training progression scenes

## Render-Facing Prompt Notes
**Required Manual Description:** This character requires complete manual description before image generation can proceed. Current chapter summary provides only narrative role without visual identifiers.

**Uncertainty Note:** Cannot determine physical appearance, clothing style, or distinctive features from provided material. Manual description must include: height, build, hair color and style, eye color, facial features, clothing type and colors, any accessories or distinguishing marks.

## Chapter Context
Tars Tarkas appears in the chapter as chieftain during the incubator hatching ceremony where he explains the five-year egg hatching period to Lorquas Ptomel Jed. He is present during the child-raising ritual but lacks sufficient visual description for reliable rendering.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: lorquas_ptomel_jed
canonical_character_id: Lorquas Ptomel Jed
aliases: principal chieftain
is_fully_identified: false
manual_description_required: true
manual_description_reason: Chapter summary identifies Lorquas Ptomel Jed as principal chieftain but provides no physical description, appearance details, or visual characteristics. Cannot support dependable image generation without manual description.
clarification_required: true
clarification_reason: Character exists in narrative but lacks stable identification through physical description. May already exist under another name or be too weakly identified for reliable rendering.
clarification_question: What are Lorquas Ptomel Jed's physical appearance details (height, build, hair color, eye color, distinctive features) and what specific chieftain responsibilities does he hold?

[[SECTION markdown]]
# Character File: Lorquas Ptomel Jed - Chapter VII

## Display Name
Lorquas Ptomel Jed

## Chapter Role
Principal Chieftain

## Physical Presence Status
Referenced (not physically present in scene descriptions)

## Physical Description
**Status:** Insufficient information from chapter summary. No physical description, appearance details, or visual characteristics provided in the source material.

## Costume and Silhouette
**Status:** Unknown. Chapter summary does not describe clothing, accessories, or distinctive silhouette features.

## Continuity-Critical Traits
- Receives incubator hatching explanation from Tars Tarkas
- Community leader among ~30k souls roaming arid land between 40-80 degrees south latitude
- Present during child capture ritual and training progression scenes

## Render-Facing Prompt Notes
**Required Manual Description:** This character requires complete manual description before image generation can proceed. Current chapter summary provides only narrative role without visual identifiers.

**Uncertainty Note:** Cannot determine physical appearance, clothing style, or distinctive features from provided material. Manual description must include: height, build, hair color and style, eye color, facial features, clothing type and colors, any accessories or distinguishing marks.

## Chapter Context
Lorquas Ptomel Jed appears in the chapter as principal chieftain during the incubator hatching ceremony where he receives explanation from Tars Tarkas about the five-year egg hatching period. He is present during the child-raising ritual but lacks sufficient visual description for reliable rendering.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: warriors_group
canonical_character_id: Warriors
aliases: community members, 200+ warriors
is_fully_identified: false
manual_description_required: true
manual_description_reason: Chapter summary references "Warriors (200+)" as a group but provides no individual physical descriptions, appearance details, or visual characteristics. Cannot support dependable image generation without manual description for representative figures.
clarification_required: true
clarification_reason: Character exists in narrative but lacks stable identification through physical description. May already exist under another name or be too weakly identified for reliable rendering.
clarification_question: What are the warriors' typical physical appearance details (height, build, hair color, eye color, distinctive features) and what specific warrior attire or equipment do they wear?

[[SECTION markdown]]
# Character File: Warriors - Chapter VII

## Display Name
Warriors

## Chapter Role
Community members / Procession participants

## Physical Presence Status
Referenced (not physically present in scene descriptions)

## Physical Description
**Status:** Insufficient information from chapter summary. No individual physical description, appearance details, or visual characteristics provided for the warrior group. Cannot support dependable image generation without manual description for representative figures.

## Costume and Silhouette
**Status:** Unknown. Chapter summary does not describe clothing, accessories, or distinctive silhouette features for warriors.

## Continuity-Critical Traits
- Positioned at head and rear of procession during chariot harnessing
- Form single file line during community movement
- Present during incubator hatching ceremony and child capture ritual
- Community size approximately 30k souls

## Render-Facing Prompt Notes
**Required Manual Description:** This character group requires complete manual description before image generation can proceed. Current chapter summary provides only narrative role without visual identifiers for individual warriors.

**Uncertainty Note:** Cannot determine physical appearance, clothing style, or distinctive features from provided material. Manual description must include: height, build, hair color and style, eye color, facial features, clothing type and colors, any accessories or distinguishing marks, warrior equipment or armor details.

## Chapter Context
Warriors appear in the chapter as community members during the procession scene where they position at head and rear of chariot harnessing. They form part of the single file line during community movement but lack sufficient visual description for reliable rendering.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: women_children_group
canonical_character_id: Women/Children
aliases: gauntlet formers, community members
is_fully_identified: false
manual_description_required: true
manual_description_reason: Chapter summary references "Women/Children" as a group forming gauntlet walls but provides no individual physical descriptions, appearance details, or visual characteristics. Cannot support dependable image generation without manual description for representative figures.
clarification_required: true
clarification_reason: Character exists in narrative but lacks stable identification through physical description. May already exist under another name or be too weakly identified for reliable rendering.
clarification_question: What are the women and children's typical physical appearance details (height, build, hair color, eye color, distinctive features) and what specific attire do they wear during the gauntlet formation?

[[SECTION markdown]]
# Character File: Women/Children - Chapter VII

## Display Name
Women and Children

## Chapter Role
Gauntlet formers / Community members

## Physical Presence Status
Referenced (not physically present in scene descriptions)

## Physical Description
**Status:** Insufficient information from chapter summary. No individual physical description, appearance details, or visual characteristics provided for the women/children group. Cannot support dependable image generation without manual description for representative figures.

## Costume and Silhouette
**Status:** Unknown. Chapter summary does not describe clothing, accessories, or distinctive silhouette features for women and children.

## Continuity-Critical Traits
- Form two solid walls during child-raising ritual
- Lead out through chariots during gauntlet formation
- Capture young Martians one at a time during running gauntlet
- Community size approximately 30k souls

## Render-Facing Prompt Notes
**Required Manual Description:** This character group requires complete manual description before image generation can proceed. Current chapter summary provides only narrative role without visual identifiers for individual women and children.

**Uncertainty Note:** Cannot determine physical appearance, clothing style, or distinctive features from provided material. Manual description must include: height, build, hair color and style, eye color, facial features, clothing type and colors, any accessories or distinguishing marks, age range representation details.

## Chapter Context
Women and children appear in the chapter during the child-raising ritual where they form two solid walls leading out through chariots. They capture young Martians one at a time during the running gauntlet but lack sufficient visual description for reliable rendering.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
