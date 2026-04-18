# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-18T15:52:38.119198+00:00
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

## Story Summary

Carter and Sola return from an incubator ceremony but are ordered to retreat immediately upon spotting a fleet of enemy airships approaching the city. A battle erupts where Green Martians fire first, catching the ships off guard. The Martians then target ship crews and equipment with high accuracy. One ship is disabled, drifting down toward the city. Martians board the vessel, loot arms, jewels, and water, then burn it from within before towing it away. Carter returns to the city plaza where he witnesses a captured humanoid female being dragged into a building. She makes eye contact with Carter and signals for help, but is taken away before he can respond due to his ignorance of local customs.

## Visual Continuity Facts

- **Characters:** John Carter (human), Sola (Martian companion), Woola (hound).
- **Enemies:** Green Martians (green attire, mounted warriors), Gray Airships (long, low, gray-painted, banners on stem/stern).
- **Prisoner:** Slender girlish figure, light reddish copper skin, coal black hair, no clothes except ornaments.
- **Locations:** City buildings (upper floors, windows), Valley, Hills, Plaza.
- **Objects:** Chariots, mastodons, spears, grappling hooks, casks of water, stone vessels.
- **Events:** Incubator ceremony aftermath, airship fleet arrival, volley fire, ship burning, prisoner capture.
````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
task: character_extraction
version: 1

[[SECTION character_index_markdown]]
# Character Index - CH001

| Asset ID | Display Name | Chapter Role | Physical Presence | Description Status |
|----------|---------------|---------------|-------------------|-------------------|
| john_carter | John Carter | Human protagonist, witness to prisoner capture | Physically present | Insufficient physical description for image generation |
| sola | Sola | Martian companion | Physically present | Insufficient physical description for image generation |
| woola | Woola | Hound companion | Physically present | Insufficient physical description for image generation |
| prisoner_figure | Slender Girlish Figure | Captured humanoid female, signaling for help | Referenced (captured) | Sufficient physical description for image generation |

## Notes

- John Carter, Sola, and Woola lack specific physical/visual details in source material to support dependable later image generation
- The prisoner figure has detailed visual continuity facts supporting reliable image generation
- All characters are from Chapter 001 of princess_of_mars_test project
[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: john_carter
manual_description_required: true
manual_description_reason: Source material only identifies John Carter as "human" with no specific physical features, facial structure, height, build, or distinguishing marks. Cannot support dependable later image generation without manual description of these fundamental visual elements.

[[SECTION markdown]]
# John Carter

## Display Name
John Carter

## Chapter Role
Human protagonist, witness to prisoner capture in CH001

## Physical Presence
Physically present - returns to city plaza after incubator ceremony, witnesses captured female being dragged into building

## Physical Description (Source-Supported)
- Human species
- No specific physical features documented in source material

## Costume & Silhouette
- No costume details available in source material
- Silhouette not described

## Continuity-Critical Traits
- Witness to prisoner capture event
- Returns to city plaza location
- Shows ignorance of local customs regarding captured female

## Render-Facing Prompt Noun Phrases
- human protagonist
- witness character
- city plaza observer
- ignorant of local customs

## Uncertainty Notes
**CRITICAL:** No physical description available in source material. Cannot generate reliable images without manual description of:
- Facial features and structure
- Height and body build
- Hair color and style
- Eye color
- Distinguishing marks or scars
- Clothing details (if any)

This character requires manual description before dependable image generation can proceed.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: sola
manual_description_required: true
manual_description_reason: Source material only identifies Sola as "Martian companion" with no specific physical features, species characteristics, or visual details. Cannot support dependable later image generation without manual description of these fundamental visual elements.

[[SECTION markdown]]
# Sola

## Display Name
Sola

## Chapter Role
Martian companion in CH001

## Physical Presence
Physically present - accompanies John Carter from incubator ceremony, retreats with him upon fleet arrival

## Physical Description (Source-Supported)
- Martian species
- No specific physical features documented in source material

## Costume & Silhouette
- No costume details available in source material
- Silhouette not described

## Continuity-Critical Traits
- Companion to John Carter
- Present during airship fleet arrival event
- Retreats immediately upon spotting enemy ships

## Render-Facing Prompt Noun Phrases
- Martian companion
- human ally character
- incubator ceremony participant
- retreat witness

## Uncertainty Notes
**CRITICAL:** No physical description available in source material. Cannot generate reliable images without manual description of:
- Facial features and structure
- Height and body build
- Hair color and style (if applicable)
- Eye color
- Species-specific physical traits
- Clothing or adornments

This character requires manual description before dependable image generation can proceed.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: woola
manual_description_required: true
manual_description_reason: Source material only identifies Woola as "hound" with no specific breed, physical features, or visual details. Cannot support dependable later image generation without manual description of these fundamental visual elements.

[[SECTION markdown]]
# Woola

## Display Name
Woola

## Chapter Role
Hound companion in CH001

## Physical Presence
Physically present - accompanies John Carter and Sola from incubator ceremony, retreats with them upon fleet arrival

## Physical Description (Source-Supported)
- Hound species
- No specific physical features documented in source material

## Costume & Silhouette
- No costume details available in source material
- Silhouette not described

## Continuity-Critical Traits
- Companion to John Carter and Sola
- Present during airship fleet arrival event
- Retreats immediately upon spotting enemy ships

## Render-Facing Prompt Noun Phrases
- hound companion
- animal ally character
- incubator ceremony participant
- retreat witness

## Uncertainty Notes
**CRITICAL:** No physical description available in source material. Cannot generate reliable images without manual description of:
- Breed or type
- Size and build
- Fur color and texture
- Facial features
- Ear shape and position
- Any distinguishing marks or scars

This character requires manual description before dependable image generation can proceed.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: prisoner_figure
manual_description_required: false
manual_description_reason: Source material provides sufficient physical description for dependable later image generation: light reddish copper skin, coal black hair, no clothes except ornaments. These details support reliable visual representation without manual description.

[[SECTION markdown]]
# Slender Girlish Figure (Prisoner)

## Display Name
Slender Girlish Figure

## Chapter Role
Captured humanoid female, signaling for help in CH001

## Physical Presence
Referenced - captured and dragged into building by Martians, makes eye contact with Carter before being taken away

## Physical Description (Source-Supported)
- Slender girlish figure
- Light reddish copper skin tone
- Coal black hair
- No clothes except ornaments

## Costume & Silhouette
- No clothing except ornaments
- Slender build
- Girlish proportions

## Continuity-Critical Traits
- Captured by Green Martians
- Makes eye contact with John Carter from city plaza
- Signals for help through eye contact
- Taken away before Carter can respond due to his ignorance of local customs
- Witnessed by Carter returning to city plaza

## Render-Facing Prompt Noun Phrases
- slender girlish figure
- light reddish copper skin
- coal black hair
- ornamented prisoner
- captured humanoid female
- signaling for help character
- city plaza witness target

## Uncertainty Notes
Physical description is sufficient for reliable image generation. No manual description required. Continuity-critical trait: Carter's ignorance of local customs prevents him from intervening despite witnessing the capture.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
