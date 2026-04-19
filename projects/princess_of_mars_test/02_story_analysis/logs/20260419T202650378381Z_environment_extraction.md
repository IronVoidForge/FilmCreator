# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-19T20:26:50.378381+00:00
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

Chapter id: CH014

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

# Chapter Summary: A Duel to the Death (CH014)

## Narrative Overview
This chapter details the departure from Korad and the journey toward Thark. John Carter grapples with his feelings for Dejah Thoris, who avoids him due to perceived humiliation regarding her captivity. The narrative focuses on logistics of travel, security measures involving chains, and a climactic duel with a warrior named Zad that is interrupted by Dejah Thoris's intervention.

## Scene Breakdown

### Scene 1: Departure and Internal Conflict
- **Setting:** Camp near Korad, morning departure for Thark.
- **Action:** Carter reflects on his love for Dejah Thoris while she avoids him. He observes her chained to the chariot.
- **Dialogue:** Discussion with Sola regarding the key to the manacles (held by Sarkoja).
- **Resolution:** Carter intervenes with Tars Tarkas regarding the chains, agreeing to custody of the key for safety until Thark is reached.

### Scene 2: Camp Life and Incubator Incident
- **Setting:** Camp during the march.
- **Action:** Carter observes Zad (o mad) and Sarkoja's interaction. An incubator belonging to Warhoon green men is found; eggs are destroyed by Tars Tarkas' warriors.
- **Lore:** Explanation of egg growth rates on Barsoom (small at laying, growing over five years).

### Scene 3: The Duel with Zad
- **Setting:** Camp halt during the march.
- **Action:** Zad strikes Carter's animal; Carter engages in a duel using long-swords.
- **Combat:** Long fight involving parries and thrusts. Zad blinds Carter with a flash of light (mirror).
- **Climax:** Dejah Thoris, Sola, and Sarkoja watch from the chariot. Dejah Thoris throws the mirror to blind Carter's enemy but Sarkoja attacks her; Sola attempts to shield Dejah Thoris and is struck by Sarkoja's dagger.
- **Ending:** Carter is wounded in the shoulder/chest, blinded momentarily, and collapses as the chapter concludes.

## Visual Continuity Facts

### Character Appearance & Attire
- **John Carter:** Wears silks and furs; divided riding cloths between two thoats (animals).
- **Dejah Thoris:** Queenly carriage, heavily chained by one ankle to chariot side; wears silks and furs.
- **Sarkoja:** Black, venomous look; wields dagger and mirror.
- **Zad:** Hulking brute, uses long-sword.

### Props & Objects
- **Chains/Manacles:** Massive spring lock on Dejah Thoris' ankle; key held by Sarkoja initially.
- **Weapons:** Long-swords (needle-like), short-swords, daggers, hatchets.
- **Mirror:** Small object used to blind Carter during the duel.
- **Incubator:** Little enclosure with small eggs (Warhoon).

### Setting Details
- **Chariot:** Side of vehicle where Dejah Thoris is chained; doorway leading to quarters.
- **Camp:** Moon-haunted ground, velvety carpeting of moss.
- **Sky:** Nearer moon of Barsoom racing through western sky.
````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
task: environment_extraction
version: 1

[[SECTION environment_index_markdown]]
# Environment Index - Chapter CH014

## Primary Environments

### camp_near_korad
- **Role:** Primary setting for departure and internal conflict scenes
- **Geography:** Moon-haunted ground with velvety moss carpeting
- **Atmosphere:** Morning departure, western sky moon racing through
- **Scale:** Camp halt during march, chariot quarters accessible via doorway

### chariot_transport
- **Role:** Secondary setting for Dejah Thoris's confinement and observation point
- **Geography:** Side of vehicle with chained anchor point
- **Atmosphere:** Queenly carriage interior, doorway leading to quarters
- **Scale:** Observation viewpoint during duel scenes

[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: camp_near_korad

[[SECTION markdown]]
# Camp Near Korad - Environment File

## Environment Role
Primary setting for departure and internal conflict scenes; spans multiple narrative moments including morning departure, camp life during march, and duel halt.

## Architecture & Geography
- Moon-haunted ground surface with velvety carpeting of moss
- Open camp layout allowing chariot access via doorway leading to quarters
- Ground level terrain suitable for animal movement (thoats)
- Camp perimeter defined by moonlight patterns on terrain

## Lighting & Atmosphere Cues
- Morning departure lighting conditions
- Western sky moon racing through visible during scenes
- Moon-haunted quality of ground illumination
- Atmospheric tension from chained Dejah Thoris observation point

## Scale Cues & Environmental Anchors
- Camp halt during march serves as spatial anchor for duel scene
- Chariot doorway provides access point to quarters
- Ground moss carpeting establishes terrain consistency
- Moon position in western sky marks temporal progression

## Descriptive Noun Phrases
camp ground, moon-haunted surface, velvety moss carpeting, chariot quarters, camp halt, western sky moon, ground level terrain, open camp layout, moonlight patterns, animal movement zone

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: chariot_transport

[[SECTION markdown]]
# Chariot Transport - Environment File

## Environment Role
Secondary setting for Dejah Thoris's confinement and observation point; serves as viewpoint during duel scenes and primary location for character interaction.

## Architecture & Geography
- Side of vehicle with chained anchor point at ankle level
- Doorway leading to quarters accessible from ground level
- Interior space designed for queenly carriage function
- Vehicle structure allowing external observation through doorway

## Lighting & Atmosphere Cues
- Queenly carriage interior lighting conditions
- Observation viewpoint during duel scenes
- Atmospheric tension from chained confinement
- Moonlight filtering through vehicle structure

## Scale Cues & Environmental Anchors
- Doorway provides access point to quarters
- Chained anchor point establishes spatial relationship to ground
- Observation viewpoint marks temporal progression of duel
- Vehicle side serves as primary observation platform

## Descriptive Noun Phrases
chariot side, chained anchor point, queenly carriage interior, doorway leading to quarters, observation viewpoint, vehicle structure, moonlight filtering, confinement space, access point, observation platform

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
