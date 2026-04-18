# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-18T17:19:00.321236+00:00
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

## Story Arc
1.  **Retreat:** The procession returns to a deserted city immediately after an incubator ceremony due to sudden orders.
2.  **Airship Arrival:** Twenty gray-painted airships swing over the hills toward the city. They are met with a volley of fire from building windows.
3.  **Naval Engagement:** Green Martian warriors return fire with high accuracy, targeting crew points and upper works. Several ships limp away; one is disabled and drifting.
4.  **Recovery Operation:** Warriors board the disabled ship to loot arms, ammunition, jewels, and water. They burn the vessel from within before towing it away.
5.  **Discovery:** While returning to the plaza, the narrator spots a slender, girlish figure being dragged into a building by green Martian females.

## Visual Continuity Facts
- **Locations:**
    - Upper floor window (view of valley/hills).
    - Building roofs (observation point).
    - Plaza (crowded with Martians).
    - Building interior (portal/depths).
- **Characters & Appearance:**
    - **Narrator:** Observes from distance, descends to street.
    - **Sola:** Rushes up to narrator upon arrival at plaza.
    - **Woola:** Hound follows close at heel.
    - **Captive:** Slender, girlish figure. Skin: light reddish copper. Hair: coal black, loosely caught. Features: Oval face, large lustrous eyes, finely chiseled. Attire: Destitute of clothes except ornaments.
- **Actions:**
    - Warriors melt like mist into doorways.
    - Ships swing broadside and circle.
    - Bodies strewn about decks (crews dead/unmanned).
    - Grappling hooks used to haul ship to ground.
    - Missile thrown back onto vessel causing flame spurt.
- **Atmosphere:**
    - Initial: Peaceful advance of ships.
    - Middle: Deadly accuracy, fire, smoke.
    - End: Hope mixed with dejection; captive looks at narrator with hope then loathing.
````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
task: character_extraction
version: 1

[[SECTION character_index_markdown]]
# Character Index: CH001

| Asset ID | Canonical Character ID | Aliases | Fully Identified | Manual Description Required | Clarification Required |
|----------|------------------------|---------|------------------|------------------------------|------------------------|
| narrator_ch001 | narrator | - | true | true | false |
| sola_ch001 | sola | - | true | true | false |
| woola_ch001 | woola | - | true | true | false |
| captive_ch001 | captive | - | true | false | false |

[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: narrator_ch001
canonical_character_id: narrator
aliases: -
is_fully_identified: true
manual_description_required: true
manual_description_reason: No physical description provided in source material; cannot support dependable image generation without additional details
clarification_required: false
clarification_reason: -
clarification_question: -

[[SECTION markdown]]
# Narrator (CH001)

## Display Name
Narrator

## Chapter Role
Observer / Witness

## Physical Presence
Uncertain (observes from distance, descends to street)

## Physical Description
Not described in source material. No physical attributes provided for reliable image generation.

## Costume & Silhouette
Unknown. No costume details available in chapter text.

## Continuity-Critical Traits
- Observes events from elevated position initially
- Descends to street level by end of chapter
- Witness to naval engagement and captive discovery

## Render-Facing Prompt Notes
- Requires manual description for image generation
- Focus on observational perspective rather than physical presence
- Consider positioning relative to airships, plaza, and building interiors

## Uncertainty Notes
**CRITICAL:** No physical description provided in source material. Cannot generate dependable images without additional details about appearance, age, gender, or distinguishing features.

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: sola_ch001
canonical_character_id: sola
aliases: -
is_fully_identified: true
manual_description_required: true
manual_description_reason: No physical description provided in source material; only name and action (rushes to narrator) documented
clarification_required: false
clarification_reason: -
clarification_question: -

[[SECTION markdown]]
# Sola (CH001)

## Display Name
Sola

## Chapter Role
Companion / Guide

## Physical Presence
Present at plaza upon arrival

## Physical Description
Not described in source material. No physical attributes provided for reliable image generation.

## Costume & Silhouette
Unknown. No costume details available in chapter text.

## Continuity-Critical Traits
- Rushes up to narrator upon arrival at plaza
- Appears to be familiar with narrator (implied relationship)

## Render-Facing Prompt Notes
- Requires manual description for image generation
- Consider approach from plaza toward narrator
- May need clarification on species, age, or distinguishing features

## Uncertainty Notes
**CRITICAL:** No physical description provided in source material. Cannot generate dependable images without additional details about appearance, age, gender, or distinguishing features.

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: woola_ch001
canonical_character_id: woola
aliases: -
is_fully_identified: true
manual_description_required: true
manual_description_reason: Only identified as "Hound" with no breed, size, color, or physical details provided in source material
clarification_required: false
clarification_reason: -
clarification_question: -

[[SECTION markdown]]
# Woola (CH001)

## Display Name
Woola

## Chapter Role
Companion / Hound

## Physical Presence
Present following close at heel

## Physical Description
Not described in source material beyond being a hound. No breed, size, color, or physical attributes provided for reliable image generation.

## Costume & Silhouette
Unknown. No costume details available in chapter text.

## Continuity-Critical Traits
- Follows narrator close at heel throughout chapter
- Present during plaza arrival and naval engagement scenes

## Render-Facing Prompt Notes
- Requires manual description for image generation
- Consider breed, size, coat color, and distinguishing features
- May need clarification on species (dog, wolf, or other canine)

## Uncertainty Notes
**CRITICAL:** No physical description provided in source material beyond being a hound. Cannot generate dependable images without additional details about breed, size, color, or distinguishing features.

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: captive_ch001
canonical_character_id: captive
aliases: -
is_fully_identified: true
manual_description_required: false
manual_description_reason: -
clarification_required: false
clarification_reason: -
clarification_question: -

[[SECTION markdown]]
# Captive (CH001)

## Display Name
Captive

## Chapter Role
Subject of Discovery / Witnessed Victim

## Physical Presence
Present being dragged into building by green Martian females

## Physical Description
- **Skin:** Light reddish copper
- **Hair:** Coal black, loosely caught
- **Face:** Oval face, large lustrous eyes, finely chiseled features
- **Attire:** Destitute of clothes except ornaments

## Costume & Silhouette
- Minimal clothing with ornamental pieces
- Slender, girlish figure
- Being dragged by force into building interior

## Continuity-Critical Traits
- Observed from distance by narrator during return to plaza
- Looks at narrator with hope then loathing
- Skin tone and features distinguish from human characters
- Ornamentation may indicate cultural or personal significance

## Render-Facing Prompt Notes
- Sufficient physical description for dependable image generation
- Focus on slender girlish proportions
- Light reddish copper skin tone (distinctive)
- Coal black hair loosely caught
- Oval face with large lustrous eyes
- Finely chiseled facial features
- Ornamental pieces rather than full clothing

## Uncertainty Notes
**NO CRITICAL UNCERTAINTY:** Physical description is complete and sufficient for reliable image generation. No additional manual description required.

[[/SECTION]]
[[/FILMCREATOR_RECORD]]
[[/FILMCREATOR_PACKET]]
````
