# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-19T20:29:02.413884+00:00
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

Chapter id: CH015

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

# Chapter Summary: CHAPTER XV - SOLA TELLS ME HER STORY

## Narrative Beats & Scene Decomposition

### Scene 1: Recovery from Zad's Attack
- **Action:** John Carter regains consciousness after being stabbed by Zad. He finds his sword buried in Zad's green breast and removes it from his own left breast (flesh wound only).
- **Visual Continuity:** Green moss, ochre moss of ancient sea bottom, sword piercing ribs, blood.
- **Outcome:** Carter is bleeding but weak; he moves toward the chariots carrying his retinue.

### Scene 2: Wound Healing & Visit to Dejah/Sola
- **Action:** Martian women apply healing agents to Carter (instantaneous recovery). Carter visits the chariot of Dejah Thoris where Sola is bandaged and Dejah is sobbing (believing Carter dead).
- **Dialogue:** Sola explains Dejah's grief; Carter promises not to force himself on Dejah.
- **Visual Continuity:** Bandages, silks and furs, torch light, Sola standing, Dejah prone.

### Scene 3: The Caravan March Description
- **Action:** Carter leaves the chariot and joins Tars Tarkas at the rear of the column. The text describes the silent march of the caravan.
- **Visual Continuity:** 250 ornate chariots, 50 extra mastodons (zitidars), 500+ loose thoats, advance guard of mounted warriors. Landscape is moss-covered with no dust or sound from movement.
- **Atmosphere:** Phantasmagoria-like silence, guttural growling of animals breaking the stillness.

### Scene 4: Sola's Backstory (The Core Narrative)
- **Action:** Carter finds Sola working by torchlight at night. She tells her story of her parents' forbidden love, the hidden egg/incubation, Sarkoja's discovery, and her mother's death by torture.
- **Key Details:** Mother was too small for Thark breeding; father was a simple warrior; egg hidden in ruined tower; Sarkoja heard story but not father's name; mother died protecting Sola; father is Tars Tarkas.
- **Visual Continuity:** Torchlight, shadows of doorway, lesser moon swinging clear, chariot tailboard.

### Scene 5: Revelation & Departure
- **Action:** Sola reveals her father's name is Tars Tarkas. Carter promises to tell Dejah he is alive and leaves to join Tars Tarkas at the rear of the column.
- **Visual Continuity:** Sola wrapped in gloomy thoughts, Carter on waiting thoat, column moving across yellow landscape.

## Visual Continuity Facts (Separate from Story Summary)
- **Landscape:** Moss-covered sea bottom, no dust (except cultivated districts), silent movement due to padded feet/tires.
- **Lighting:** Lesser moon provides illumination during Sola's story; torchlight used at night camp.
- **Characters:** Green Martians converse in monosyllables; Dejah Thoris is prone/sobbing; Sola is standing/bandaged; Tars Tarkas is at rear of column.
- **Objects:** Swords, bandages, torches, chariots, thoats, zitidars, metal ornaments, silks and furs.
````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
task: environment_extraction
version: 1

[[SECTION environment_index_markdown]]
# Environment Index - Chapter XV

| Asset ID | Description | Role |
|----------|-------------|------|
| sea_bottom_mossy_landscape | Moss-covered ancient sea bottom, silent movement, torch/lesser moon lighting | Primary |
| chariot_interior_camp | Chariot interior with bandaged occupants, torchlight, silks and furs | Secondary |
| caravan_column_march | Large scale march with ornate chariots, mastodons, thoats across yellow landscape | Transit |

[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: sea_bottom_mossy_landscape

[[SECTION markdown]]
**Environment Role:** Primary setting for recovery and caravan movement.

**Architecture or Geography:** Moss-covered ancient sea bottom, no dust (except cultivated districts), yellow landscape visible during departure. Ruined tower mentioned in backstory context.

**Lighting and Atmosphere Cues:** Lesser moon provides illumination during night scenes; torchlight used at camp; phantasmagoria-like silence with guttural growling of animals breaking stillness. Green moss, ochre moss of ancient sea bottom.

**Scale Cues and Recurring Environmental Anchors:** 250 ornate chariots, 50 extra mastodons (zitidars), 500+ loose thoats, advance guard of mounted warriors. Silent movement due to padded feet/tires. Landscape is moss-covered with no dust or sound from movement.

**Useful Descriptive Noun Phrases:** Moss-covered sea bottom, silent march landscape, lesser moon illumination, torchlit camp ground, yellow desert floor, ancient sea bed vegetation, padded foot movement, guttural animal growls.

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: chariot_interior_camp

[[SECTION markdown]]
**Environment Role:** Secondary setting for intimate character moments and storytelling.

**Architecture or Geography:** Chariot interior with tailboard, bandaged occupants (Sola, Dejah), silks and furs lining the space. Doorway shadows visible during backstory narration.

**Lighting and Atmosphere Cues:** Torchlight at night camp; gloomy thoughts atmosphere; shadows of doorway; lesser moon swinging clear. Bandages, silks and furs create soft texture under torch illumination.

**Scale Cues and Recurring Environmental Anchors:** Chariot tailboard, bandaged figures (Sola standing, Dejah prone), metal ornaments, lesser moon position relative to chariot structure.

**Useful Descriptive Noun Phrases:** Torchlit chariot interior, bandaged warrior space, silks and furs lining, doorway shadows, lesser moon glow, gloomy thought atmosphere, chariot tailboard structure, night camp torchlight.

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: caravan_column_march

[[SECTION markdown]]
**Environment Role:** Transit setting for large scale movement and journey progression.

**Architecture or Geography:** Column of 250 ornate chariots, 50 extra mastodons (zitidars), 500+ loose thoats across yellow landscape. Advance guard of mounted warriors. Landscape is moss-covered with no dust or sound from movement.

**Lighting and Atmosphere Cues:** Phantasmagoria-like silence, guttural growling of animals breaking stillness. Torchlight at night camp; lesser moon illumination during Sola's story. Yellow landscape visible during departure.

**Scale Cues and Recurring Environmental Anchors:** 250 ornate chariots, 50 extra mastodons (zitidars), 500+ loose thoats, advance guard of mounted warriors. Silent movement due to padded feet/tires. Column moving across yellow landscape.

**Useful Descriptive Noun Phrases:** Ornate chariot column, mastodon herd march, loose thoat caravan, mounted warrior advance guard, yellow desert floor, silent padded movement, moss-covered journey path, phantasmagoria silence atmosphere.

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
