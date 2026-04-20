# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-20T02:18:56.199266+00:00
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

Chapter id: CH008

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

# Chapter Summary: A Fair Captive From The Sky

## Story Arc

### 1. The Retreat Order & Enemy Arrival
On the third day after the incubator ceremony, the procession is ordered to return home but immediately recalled due to the arrival of enemy airships. Twenty gray-painted vessels swing over the hills toward the city. The green Martians, trained for this evolution, melt into nearby buildings within three minutes.

### 2. The Naval Battle
The narrator climbs to an upper floor window to observe. A volley is fired from building windows by the Martians, causing the enemy fleet to return fire. Both sides display deadly accuracy; bullets drop at explosions and banners dissolve in flames. The enemy ships circle and turn back, intending to complete a great circle opposite the firing line.

### 3. The Disabled Ship & Recovery
Twenty minutes after the first volley, the fleet retreats, damaged and limping. One ship is entirely unmanned and helpless. Warriors rush to the roofs to cover the possibility of reinforcements or return fire. They chase the disabled craft, which drifts fifty feet above ground toward a building south of their position. Warriors board the vessel with spears and grappling hooks, hauling it to ground.

### 4. Looting and Burning
The warriors systematically rifle the vessel for several hours, requisitioning chariots to transport loot: arms, ammunition, silks, furs, jewels, stone vessels, and food/water (including casks of water). After removing the last load, they tow the craft out into the valley. They empty carboys over the dead sailors and decks. A final missile is thrown onto the vessel, igniting it. The ship soars majestically into the air as a floating funeral pyre, drifting southeast until lost in the distance.

### 5. The Prisoner's Appearance
Depressed by the defeat of a kindred people, the narrator descends to the street. Sola rushes up as the cavalcade returns to the plaza. Lorquas Ptomel remains at the deserted city due to fear of airship attack for over a week. As they enter the plaza, the narrator sees a prisoner being dragged into a nearby building by green Martian females. The creature is described as a slender, girlish figure similar to Earth women: oval face, coal black hair, light reddish copper skin, naked except for ornaments. She makes a sign (appeal for succor) with her free hand. Her eyes meet the narrator's; hope fades into dejection and contempt before she is dragged away.

## Visual Continuity Facts

### Character States & Locations
- **Narrator:** Positioned on upper floor window during battle, then descends to street/plaza. Accompanied by Woola (hound).
- **Sola:** Rushes up to narrator upon return to plaza; actively involved in procession defense.
- **Lorquas Ptomel:** Remains at deserted city with caravan/children due to safety concerns.
- **Green Martians:** Melt into building doorways during enemy arrival; swarm from windows during battle; board disabled ship from windows; rush onto plain to meet retreating fleet.
- **Enemy Fleet:** Gray-painted, long and low vessels. Initially twenty ships; one disabled at end of chapter.

### Environmental & Object Details
- **City:** Described as "open ground" with spacious doorways. Buildings have upper floors with windows facing the valley/hills.
- **Airships:** Long, low, gray-painted. Carried strange banners and odd devices on prow. Swung from stem to stern above upper works.
- **Battlefield:** Valley across which ships advance. Ground is open plain where warriors rush out to meet disabled ship.
- **Loot Items:** Arms, ammunition, silks, furs, jewels, strangely carved stone vessels, solid foods/liquids, casks of water.
- **Disabled Ship:** Drifting fifty feet above ground; bodies of crew strewn about; eventually set on fire and towed away.

### Temporal Markers
- **Incubator Ceremony:** Third day after this event marks the start of the chapter's action.
- **Battle Duration:** Lasts approximately twenty minutes from first volley to fleet retreat.
- **Looting Duration:** Requires several hours.
- **Post-Battle Stay:** Caravan remains at city for more than a week due to fear of return attack.
````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
task: character_extraction
version: 1

[[SECTION character_index_markdown]]
# Character Index - CH008

| Asset ID | Canonical Character ID | Display Name | Status |
|----------|------------------------|--------------|--------|
| narrator_ch008 | narrator | Narrator (POV) | Referenced, not physically present in all scenes |
| sola_ch008 | sola | Sola | Physically present |
| lorquas_ptomel_ch008 | lorquas_ptomel | Lorquas Ptomel | Referenced |
| woola_ch008 | woola | Woola (hound) | Physically present |
| prisoner_ch008 | prisoner | The Prisoner | Physically present, referenced |

*Note: Green Martians are a collective group and not individually indexed.*
[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: narrator_ch008
canonical_character_id: narrator
aliases: 
is_fully_identified: true
manual_description_required: true
manual_description_reason: No physical description provided in chapter summary; only actions and locations are described. Cannot support dependable image generation without additional details.
clarification_required: false
clarification_reason: 
clarification_question: 

[[SECTION markdown]]
# Narrator - CH008

## Display Name & Role
**Narrator** (POV Character)

## Physical Presence
Referenced throughout chapter; positioned on upper floor window during battle, then descends to street/plaza. Accompanied by Woola (hound).

## Physical Description
*No physical description provided in source material.*

## Costume & Silhouette
*Unknown - no costume or silhouette details available.*

## Continuity-Critical Traits
- POV character for chapter
- Observes battle from window position
- Witnesses prisoner being dragged away
- Descends to plaza after battle

## Render-Facing Prompt Notes
**Uncertainty:** Physical appearance completely unknown. Cannot generate reliable images without additional description. Would require manual description addition before image generation.

## Useful Descriptive Noun Phrases
- "The narrator" (as referenced in text)
- "POV character"
- "Observer from upper floor window"
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: sola_ch008
canonical_character_id: sola
aliases: 
is_fully_identified: true
manual_description_required: true
manual_description_reason: Only name and actions described in chapter; no physical appearance, costume, or silhouette details provided. Cannot support dependable image generation without additional description.
clarification_required: false
clarification_reason: 
clarification_question: 

[[SECTION markdown]]
# Sola - CH008

## Display Name & Role
**Sola** (Procession Defense Participant)

## Physical Presence
Physically present; rushes up to narrator upon return to plaza; actively involved in procession defense.

## Physical Description
*No physical description provided in source material.*

## Costume & Silhouette
*Unknown - no costume or silhouette details available.*

## Continuity-Critical Traits
- Rushes to narrator after battle
- Involved in procession defense activities
- Present at plaza during chapter events

## Render-Facing Prompt Notes
**Uncertainty:** Physical appearance completely unknown. Cannot generate reliable images without additional description. Would require manual description addition before image generation.

## Useful Descriptive Noun Phrases
- "Sola" (as referenced in text)
- "Procession defender"
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: lorquas_ptomel_ch008
canonical_character_id: lorquas_ptomel
aliases: 
is_fully_identified: true
manual_description_required: true
manual_description_reason: Only name and location/actions described in chapter; no physical appearance, costume, or silhouette details provided. Cannot support dependable image generation without additional description.
clarification_required: false
clarification_reason: 
clarification_question: 

[[SECTION markdown]]
# Lorquas Ptomel - CH008

## Display Name & Role
**Lorquas Ptomel** (Caravan Leader)

## Physical Presence
Referenced; remains at deserted city with caravan/children due to safety concerns.

## Physical Description
*No physical description provided in source material.*

## Costume & Silhouette
*Unknown - no costume or silhouette details available.*

## Continuity-Critical Traits
- Remains at deserted city for over a week
- Accompanied by caravan and children
- Stays due to fear of airship attack

## Render-Facing Prompt Notes
**Uncertainty:** Physical appearance completely unknown. Cannot generate reliable images without additional description. Would require manual description addition before image generation.

## Useful Descriptive Noun Phrases
- "Lorquas Ptomel" (as referenced in text)
- "Caravan leader"
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: woola_ch008
canonical_character_id: woola
aliases: 
is_fully_identified: true
manual_description_required: true
manual_description_reason: Only identified as a hound; no breed, size, color, or physical appearance details provided. Cannot support dependable image generation without additional description.
clarification_required: false
clarification_reason: 
clarification_question: 

[[SECTION markdown]]
# Woola - CH008

## Display Name & Role
**Woola** (Narrator's Hound)

## Physical Presence
Physically present; accompanies narrator throughout chapter events.

## Physical Description
*No physical description provided in source material beyond being a hound.*

## Costume & Silhouette
*Unknown - no costume or silhouette details available.*

## Continuity-Critical Traits
- Narrator's companion animal
- Present during battle observation
- Present when narrator descends to street/plaza

## Render-Facing Prompt Notes
**Uncertainty:** Physical appearance beyond "hound" classification is unknown. Cannot generate reliable images without additional description (breed, size, color, markings). Would require manual description addition before image generation.

## Useful Descriptive Noun Phrases
- "Woola" (as referenced in text)
- "Narrator's hound"
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: prisoner_ch008
canonical_character_id: prisoner
aliases: 
is_fully_identified: true
manual_description_required: true
manual_description_reason: Physical description provided is sparse (oval face, coal black hair, light reddish copper skin, naked except for ornaments). Not sufficient for dependable image generation; lacks details on build, age, specific ornamentation, facial features beyond oval shape. Cannot support reliable rendering without additional description.
clarification_required: false
clarification_reason: 
clarification_question: 

[[SECTION markdown]]
# The Prisoner - CH008

## Display Name & Role
**The Prisoner** (Earth Human Captive)

## Physical Presence
Physically present; being dragged into nearby building by green Martian females.

## Physical Description
- Slender, girlish figure similar to Earth women
- Oval face
- Coal black hair
- Light reddish copper skin
- Naked except for ornaments

## Costume & Silhouette
*Unknown - only "naked except for ornaments" noted; no specific ornament details provided.*

## Continuity-Critical Traits
- Described as having Earth-like appearance (oval face, coal black hair)
- Skin tone: light reddish copper
- Being dragged away by green Martian females
- Makes sign of appeal with free hand
- Eyes meet narrator's before being dragged away

## Render-Facing Prompt Notes
**Uncertainty:** Physical description is sparse and insufficient for dependable image generation. Missing details include: build specifics, age indicators, facial features beyond oval shape, ornament types, exact skin tone nuances. Would require manual description addition before reliable image generation.

## Useful Descriptive Noun Phrases
- "The prisoner" (as referenced in text)
- "Earth human captive"
- "Slender girlish figure"
- "Coal black hair"
- "Light reddish copper skin"
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_PACKET]]
````
