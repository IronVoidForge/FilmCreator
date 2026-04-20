# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-20T00:23:05.757657+00:00
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

Chapter id: CH004

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

**Story Flow:**
1. **Arrival:** Ground rises to mountains; party enters city via ruined road. Buildings appear ancient but not decayed.
2. **Observation:** Martians camped in plaza (900+). Appearance noted: naked except ornaments, women have larger tusks, children light colored. Life cycle details provided (death by violence vs sickness).
3. **Introduction:** Tars Tarkas (vice-chieftain) leads party to Chieftain's edifice. Ceremony involves name exchange between Martians.
4. **Conflict:** Martians surround narrator, demand performance ("sak"). Narrator struggles with walking/jumping.
5. **Fight:** Narrator punches a laughing Martian who bullied him. Crowd approves (applause).
6. **Performance:** Narrator performs "sakk" jump successfully.
7. **Resolution:** Narrator demands food/water. Sola (8ft female) takes him to quarters.
8. **Ending:** Ten-legged creature waddles into the room.

**Visual Continuity:**
- **Martians:** Naked except ornaments; women have larger tusks; adults 10-12ft tall.
- **Furniture:** Human-sized desks/chairs (too small for Martians).
- **Architecture:** White marble, gold inlay, broad steps.
- **Creature:** Ten short legs, frog-like head, three rows of sharp tusks.
````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
task: environment_extraction
version: 1

[[SECTION environment_index_markdown]]
# Martian City Environment Index

## Extracted Environments

| Asset ID | Environment Name | Role | Primary Features |
|----------|------------------|------|------------------|
| martian_city_plaza | Martian Plaza | Primary Setting | White marble, gold inlay, 900+ Martians camped |
| chieftain_edifice | Chieftain's Edifice | Secondary Setting | Broad steps, ancient architecture, ceremonial space |
| narrator_quarters | Narrator Quarters | Transit/Resolution Setting | Human-sized furniture, ten-legged creature enters |

## Environment Families Summary

- **Martian Plaza**: Main gathering space where party arrives and observes Martians
- **Chieftain's Edifice**: Ceremonial building for name exchange and meetings with leadership
- **Narrator Quarters**: Private space for resolution after performance

[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: martian_city_plaza

[[SECTION markdown]]
# Martian Plaza Environment

## Environment Role
Primary setting - main gathering space where party arrives and observes Martians

## Architecture and Geography
- White marble surfaces with gold inlay details
- Broad steps leading into plaza area
- Open-air plaza design accommodating 900+ Martians
- Ruined road entrance from city outskirts
- Ground rises to mountains in background

## Lighting and Atmosphere Cues
- Natural daylight illumination
- Ancient but not decayed building atmosphere
- Life cycle details visible (death by violence vs sickness)
- Crowd approval moments with applause lighting

## Scale Cues and Environmental Anchors
- Martians 10-12ft tall (adults)
- Human-sized desks/chairs appear too small for Martians
- Plaza accommodates large crowd gatherings
- Ten-legged creature waddles into room later

## Descriptive Noun Phrases
- White marble plaza floor
- Gold inlay architectural details
- Mountain background horizon
- Ruined road entrance path
- Crowd gathering space
- Ceremonial open-air area

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: chieftain_edifice

[[SECTION markdown]]
# Chieftain's Edifice Environment

## Environment Role
Secondary setting - ceremonial building for leadership meetings and name exchange ceremonies

## Architecture and Geography
- Ancient architecture style
- Broad steps leading to entrance
- White marble construction with gold inlay
- Interior space for ceremonies
- Tars Tarkas leads party to this location

## Lighting and Atmosphere Cues
- Ceremonial lighting during name exchange
- Formal atmosphere for leadership interactions
- Name exchange ceremony lighting
- Respectful gathering ambiance

## Scale Cues and Environmental Anchors
- Large ceremonial space
- Broad steps as entrance anchor
- Interior accommodates Martians of 10-12ft height
- Chieftain's presence defines space scale

## Descriptive Noun Phrases
- Ancient white marble structure
- Gold inlay ceremonial details
- Broad step entrance
- Ceremonial interior space
- Leadership meeting chamber
- Name exchange ceremony area

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: narrator_quarters

[[SECTION markdown]]
# Narrator Quarters Environment

## Environment Role
Transit/Resolution setting - private space where performance aftermath occurs and resolution happens

## Architecture and Geography
- Private interior room space
- Human-sized furniture (desks, chairs)
- Too small for Martian scale occupants
- Ten-legged creature waddles into room
- Sola takes narrator to this location

## Lighting and Atmosphere Cues
- Interior room lighting
- Resolution atmosphere after performance
- Food/water demand context
- Private gathering ambiance

## Scale Cues and Environmental Anchors
- Human-sized furniture scale
- Room accommodates 8ft female (Sola)
- Ten-legged creature enters as anchor
- Performance aftermath space

## Descriptive Noun Phrases
- Interior private room
- Human-sized desk and chair furniture
- Food and water storage area
- Creature entry point
- Resolution gathering space
- Sola's quarters entrance

[[/SECTION]]
[[/FILMCREATOR_RECORD]]
[[/FILMCREATOR_PACKET]]
````
