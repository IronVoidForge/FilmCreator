# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-18T15:51:22.734928+00:00
- task: character_extraction

## System Prompt
````text
You are FilmCreator's local authoring analyst.
Return exactly one FILMCREATOR packet in Markdown.
Do not return JSON.
Do not use markdown fences.
Do not add commentary before or after the packet.
Preserve uncertainty instead of inventing hidden facts.
When asked to write Markdown file contents, place the complete file body inside the requested SECTION tags.
When asked to extract render-facing facts, focus on visible, continuity-relevant details.
````

## User Prompt
````text
Project slug: princess_of_mars_test

Chapter id: CH001

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
manual_description_required: <value>
manual_description_reason: <value>

[[SECTION markdown]]
...markdown content...
[[/SECTION]]
[[/FILMCREATOR_RECORD]]
[[/FILMCREATOR_PACKET]]



Important rule:

- if a character does not have enough physical or visual description in the supplied material to support dependable later image generation, set manual_description_required to true

- explain exactly why in manual_description_reason

- do not guess ornate missing details just to avoid the flag



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

The chapter begins with green Martians retreating to city buildings after an open ground march. From a window, the narrator observes the arrival of a massive fleet of twenty gray airships. The Martians fire a volley and engage in a fierce battle, demonstrating deadly accuracy that destroys most vessels. One ship is disabled and drifted down. Martians capture, loot, and burn the vessel. The narrator feels a strange depression interpreting the fleet as kindred people defeated. Sola rushes to the narrator. A prisoner is dragged into a building. The narrator sees a slender girl resembling Earth women, beautiful but naked except for ornaments. She looks at him with hope then dejection before being dragged away.
````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
task: character_extraction
version: 1

[[SECTION character_index_markdown]]
# Character Index - Chapter CH001

| Asset ID | Display Name | Presence Status | Description Notes |
|----------|---------------|-----------------|-------------------|
| narrator | The Narrator | Physically Present (Observer) | First-person perspective, observes from window |
| sola | Sola | Physically Present | Rushes to narrator, no physical details provided |
| slender_girl_earth_women | Slender Girl Resembling Earth Women | Physically Present (Captured) | Slender build, ornaments only, dragged away |

**Note**: All characters require manual description due to insufficient visual detail for dependable image generation.
[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: narrator
manual_description_required: true
manual_description_reason: No physical appearance details provided in source material - only first-person perspective and emotional state described (depression, observation from window). Cannot reliably generate images without knowing hair color, eye color, height, build specifics.

[[SECTION markdown]]
# The Narrator

**Display Name**: The Narrator  
**Chapter Role**: First-Person Observer / Witness  
**Presence Status**: Physically Present (Observing from Window)  

## Physical Description
*Insufficient for reliable image generation - requires manual description.*

The source material provides no specific physical appearance details. The narrator is only described through their emotional state (feeling depression, strange feelings about the fleet) and their position (observing from a window). No information about hair color, eye color, height, body build, skin tone, or facial features is available in the text.

## Costume & Silhouette
*Unknown - requires manual description.*

No costume details are provided in the source material. The narrator's attire is not described.

## Continuity-Critical Traits
- Observes events from a window position
- Feels depression about the fleet being "kindred people" defeated
- Witnesses Martians capturing and dragging away prisoners
- Sees the slender girl resembling Earth women

## Render-Facing Prompt Notes
```
[NEEDS MANUAL DESCRIPTION]
- Hair: [UNKNOWN - requires specification]
- Eyes: [UNKNOWN - requires specification]  
- Height/Build: [UNKNOWN - requires specification]
- Skin Tone: [UNKNOWN - requires specification]
- Attire: [UNKNOWN - requires specification]
```

## Uncertainty Notes
**CRITICAL**: This character cannot be reliably rendered without manual description. The source material only provides emotional and positional context, not physical appearance details needed for dependable image generation.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: sola
manual_description_required: true
manual_description_reason: Only name is provided in source material ("Sola rushes to the narrator"). No physical appearance, costume, or visual details are described at all. Cannot generate images without complete physical description.

[[SECTION markdown]]
# Sola

**Display Name**: Sola  
**Chapter Role**: Companion / Rushing Figure  
**Presence Status**: Physically Present  

## Physical Description
*Insufficient for reliable image generation - requires manual description.*

The source material provides no physical appearance details whatsoever. Only the name "Sola" and the action of rushing to the narrator are described. No information about hair color, eye color, height, body build, skin tone, or facial features is available in the text.

## Costume & Silhouette
*Unknown - requires manual description.*

No costume details are provided in the source material. Sola's attire is not described.

## Continuity-Critical Traits
- Rushes to the narrator (urgent action)
- Relationship to narrator appears close enough for immediate physical contact
- No other actions or dialogue recorded in this chapter

## Render-Facing Prompt Notes
```
[NEEDS MANUAL DESCRIPTION]
- Hair: [UNKNOWN - requires specification]
- Eyes: [UNKNOWN - requires specification]  
- Height/Build: [UNKNOWN - requires specification]
- Skin Tone: [UNKNOWN - requires specification]
- Attire: [UNKNOWN - requires specification]
```

## Uncertainty Notes
**CRITICAL**: This character cannot be reliably rendered without manual description. The source material provides only the name and one action, with zero physical appearance details needed for dependable image generation.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: slender_girl_earth_women
manual_description_required: true
manual_description_reason: Source describes "slender girl resembling Earth women, beautiful but naked except for ornaments" - provides build type and ornament detail but lacks specific physical features (hair color, eye color, height specifics, facial features) needed for reliable image generation. Description is incomplete for dependable rendering.

[[SECTION markdown]]
# Slender Girl Resembling Earth Women

**Display Name**: Slender Girl Resembling Earth Women  
**Chapter Role**: Prisoner / Captured Figure  
**Presence Status**: Physically Present (Captured and Dragged Away)  

## Physical Description
*Partially described but insufficient for reliable image generation - requires manual description.*

The source material describes her as "slender" with a build resembling Earth women, beautiful, wearing ornaments only, and naked otherwise. However, specific physical features are not provided: no hair color, eye color, height specifics, facial features, or ornament details are described in the text.

## Costume & Silhouette
*Partially known - requires manual description.*

The source material states she wears "ornaments only" and is otherwise naked. No specific ornament types, colors, or placement are described. The silhouette is noted as slender but no further body proportions are detailed.

## Continuity-Critical Traits
- Resembles Earth women (cultural connection)
- Beautiful appearance
- Naked except for ornaments
- Looks at narrator with hope then dejection
- Dragged away by Martians after being captured
- Witnessed from window position

## Render-Facing Prompt Notes
```
[NEEDS MANUAL DESCRIPTION]
- Hair: [UNKNOWN - requires specification]
- Eyes: [UNKNOWN - requires specification]  
- Height/Build: Slender (confirmed)
- Skin Tone: [UNKNOWN - requires specification]
- Attire: Ornaments only (type/color unknown)
- Expression: Hope then dejection (emotional state known)
```

## Uncertainty Notes
**IMPORTANT**: While some physical traits are described (slender build, ornaments), the description lacks specific features needed for dependable image generation. Hair color, eye color, facial features, and ornament specifics are not provided in the source material. Manual description required to complete visual details for reliable rendering.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
