# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-18T19:57:16.983735+00:00
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

# Chapter Summary: A Fair Captive from the Sky

## Event Sequence
1.  **Retreat Order:** Following the incubation ceremony, orders are given for an immediate return to the city. The green Martians melt into buildings within three minutes.
2.  **Fleet Arrival:** From a window, the protagonist observes twenty gray air vessels swinging low above the ground toward the valley. Each carries a banner and odd devices.
3.  **Fire Exchange:**
    *   Green Martians fire a volley from building windows first.
    *   The fleet returns fire with high accuracy; figures drop at bullet explosions, banners dissolve in flames.
    *   Fleet damage is evident (limping vessels) after twenty minutes.
4.  **Fleet Retreat & Capture:** The fleet trails off. One vessel drifts helpless, unmanned, and damaged. Warriors rush to capture it before it hits the ground.
5.  **Looting & Burning:** Warriors search the vessel for loot (arms, jewels, water). After removal, they tow it away, then empty carboys over the dead sailors and burn the vessel. The ship drifts southeast as a funeral pyre.
6.  **Prisoner Discovery:** As the protagonist descends to the street, Sola rushes up. A prisoner is being dragged into a building by green Martian females.
7.  **Prisoner Description:** The figure is slender and girlish, similar to earthly women. Features include an oval face, coal black waving hair, light reddish copper skin, and ruby lips. She is naked except for ornaments.
8.  **Emotional Impact:** The prisoner makes a sign of appeal (unanswered by the protagonist). Her expression shifts from hope to dejection and loathing as she is dragged away.

## Visual Continuity Notes
*   **Protagonist's Viewpoint:** Observes fleet arrival and burning ship from an upper window/balcony.
*   **Prisoner Entry:** Observed from street level as she enters the building portal.
*   **Martian Reaction:** Warriors rush to roofs to cover the possibility of return attack or reinforcements.
````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
task: character_extraction
version: 1

[[SECTION character_index_markdown]]
# Character Index - CH001

| Asset ID | Canonical ID | Name/Role | Physical Presence | Description Status |
|----------|--------------|-----------|-------------------|--------------------|
| protagonist | protagonist_ch001 | Unnamed Observer (Window Viewpoint) | Referenced | Missing physical description |
| sola | sola_ch001 | Sola (Street Level Contact) | Present | Missing physical description |
| prisoner | prisoner_ch001 | Captured Figure (Building Portal Entry) | Present | Fully described physically |
| green_martian_female | green_martian_female_ch001 | Female Warriors (Prisoner Draggers) | Referenced | Minimal description (green, female) |
| green_martian_warrior | green_martian_warrior_ch001 | Warrior Fleet (Vessel Capturers) | Referenced | Minimal description (warrior) |

[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: protagonist_ch001
canonical_character_id: protagonist_ch001
aliases: 
is_fully_identified: false
manual_description_required: true
manual_description_reason: No physical description provided in chapter summary; only viewpoint role established (window observer)
clarification_required: true
clarification_reason: Character may exist under another name or identity not yet revealed in this chapter
clarification_question: Does the protagonist have a known name, appearance, or background from prior chapters that should be incorporated?

[[SECTION markdown]]
# Protagonist - CH001

## Display Name & Role
**Protagonist (Unnamed Observer)** - Window Viewpoint Character

## Physical Presence Status
**Referenced** - Observed from upper window/balcony throughout chapter events

## Physical Description
*No physical description provided in source material.*

- Viewpoint role: Observes fleet arrival and burning ship from elevated position
- No costume, silhouette, or continuity-critical traits documented in this chapter

## Continuity Notes
- Primary viewpoint character for chapter events
- No established appearance for image generation purposes

## Render-Facing Prompt Guidance
**Uncertainty Note:** Physical description missing; requires manual description before reliable image generation. Use existing canonical data if available from prior chapters.

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: sola_ch001
canonical_character_id: sola_ch001
aliases: 
is_fully_identified: true
manual_description_required: true
manual_description_reason: Character is named but no physical description, costume, or visual traits provided in chapter summary
clarification_required: false
clarification_reason: Name is stable; no indication of alternate identity
clarification_question: 

[[SECTION markdown]]
# Sola - CH001

## Display Name & Role
**Sola** - Street Level Contact Character

## Physical Presence Status
**Present** - Rushes up to protagonist from street level as chapter progresses

## Physical Description
*No physical description provided in source material.*

- No costume, silhouette, or continuity-critical traits documented in this chapter

## Continuity Notes
- Appears at emotional climax of prisoner discovery scene
- Makes contact with protagonist during prisoner being dragged away

## Render-Facing Prompt Guidance
**Uncertainty Note:** Physical description missing; requires manual description before reliable image generation. Character name is stable for identification purposes.

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: prisoner_ch001
canonical_character_id: prisoner_ch001
aliases: 
is_fully_identified: true
manual_description_required: false
manual_description_reason: Physical description fully provided in chapter summary (oval face, coal black waving hair, light reddish copper skin, ruby lips)
clarification_required: false
clarification_reason: Character is clearly identified as prisoner; no indication of alternate identity
clarification_question: 

[[SECTION markdown]]
# Prisoner - CH001

## Display Name & Role
**Captured Figure** - Building Portal Entry Character

## Physical Presence Status
**Present** - Dragged into building by green Martian females, observed from street level

## Physical Description
*Fully described in source material.*

- Build: Slender and girlish, similar to earthly women
- Face: Oval shape
- Hair: Coal black, waving
- Skin: Light reddish copper tone
- Lips: Ruby colored
- Attire: Naked except for ornaments (no specific costume details)

## Continuity Notes
- Makes sign of appeal to protagonist (unanswered)
- Expression shifts from hope to dejection and loathing during capture
- Gender presentation: Female (similar to earthly women)

## Render-Facing Prompt Guidance
**Supported Description:** Use provided physical traits for accurate image generation. Ornament details unspecified; may require manual description if specific ornament types are needed.

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: green_martian_female_ch001
canonical_character_id: green_martian_female_ch001
aliases: 
is_fully_identified: false
manual_description_required: true
manual_description_reason: Only minimal description provided (green, female); no physical features, costume, or silhouette details in chapter summary
clarification_required: true
clarification_reason: Character may exist under another name or identity; "green Martian" designation may be species identifier rather than individual name
clarification_question: Do green Martians have individual names or stable identifiers beyond species designation?

[[SECTION markdown]]
# Green Martian Female - CH001

## Display Name & Role
**Female Warriors** - Prisoner Draggers Character Group

## Physical Presence Status
**Referenced** - Observed dragging prisoner into building, no specific individual focus

## Physical Description
*Minimal description provided in source material.*

- Species identifier: Green (Martian)
- Gender: Female
- No physical features, costume, or silhouette details documented in this chapter

## Continuity Notes
- Drag prisoner into building during emotional climax scene
- Group action rather than individual character focus

## Render-Facing Prompt Guidance
**Uncertainty Note:** Physical description incomplete; requires manual description beyond species/gender identifiers. "Green" may be species trait requiring clarification for accurate rendering.

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: green_martian_warrior_ch001
canonical_character_id: green_martian_warrior_ch001
aliases: 
is_fully_identified: false
manual_description_required: true
manual_description_reason: Only minimal description provided (warrior, fleet member); no physical features, costume, or silhouette details in chapter summary
clarification_required: true
clarification_reason: Character may exist under another name or identity; "green Martian" designation may be species identifier rather than individual name
clarification_question: Do green Martians have individual names or stable identifiers beyond species designation?

[[SECTION markdown]]
# Green Martian Warrior - CH001

## Display Name & Role
**Warrior Fleet** - Vessel Capturers Character Group

## Physical Presence Status
**Referenced** - Observed rushing to capture damaged vessel, no specific individual focus

## Physical Description
*Minimal description provided in source material.*

- Species identifier: Green (Martian)
- Role: Warrior/Fleet member
- No physical features, costume, or silhouette details documented in this chapter

## Continuity Notes
- Rush to roofs during fleet retreat sequence
- Group action rather than individual character focus
- Capture damaged vessel before it hits ground

## Render-Facing Prompt Guidance
**Uncertainty Note:** Physical description incomplete; requires manual description beyond species/role identifiers. "Green" may be species trait requiring clarification for accurate rendering.

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
