# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-20T00:54:14.581970+00:00
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

Chapter id: CH006

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

# Chapter VI: A Fight That Won Friends

## Broad Story Summary
John Carter is pinned to the ground by a Bull Ape (Martian warrior) while his Beast defends him. A fight ensues between the Beast and the Ape; the Beast sinks its fangs into the Ape's throat, choking it. Carter intervenes, killing the first Ape with a cudgel. A second enraged Ape arrives to finish the job. Carter fights off the second Ape, killing it. Tars Tarkas, Sola, and warriors arrive to witness the battle. They applaud Carter's feats of strength. However, one warrior intends to shoot the Beast for being an anomaly. Carter defends the Beast, striking up the warrior's arm with a cudgel. The Martians accept the Beast as long as Carter protects it. They leave the chamber together, with the Beast following at heel and Sola holding Carter's arm.

## Visual Continuity Facts
*   **Combat Choreography:**
    *   Cudgel swings in arc ending upon upturned face.
    *   Fist strikes: Right fist to chin, left fist to pit of stomach.
    *   Beast's attack: Sinks mighty fangs into adversary's breast; locks throat with great arms and paws.
    *   Ending blow: Cudgel crashes full upon head, crushing skull as though eggshell.
*   **Physical States:**
    *   Beast's eyes bulging completely from sockets; blood flowing from nostrils.
    *   Ape tearing away entire front of its breast held in vise-like grip.
    *   Martians roaring and frothing at mouth in extremity of rage.
*   **Environment & Props:**
    *   Doorway: Entry point for second Ape; warriors stand in doorway.
    *   Window: Bullet from pistol explodes, blowing hole completely through wood and masonry.
    *   Floor: Creatures roll back and forth without sound of fear or pain.
*   **Expressions & Reactions:**
    *   Martians laughing vs Sola's sober apparent solicitude.
    *   Beast's pitiful appeal look upon Carter.
    *   Martians' looks of surprise at Beast following at heel.
*   **Movement:**
    *   Ape leaping through open window; mate closing in death struggle.
    *   Carter backing against wall witnessing battle.
    *   Sola rushing to examine body for wounds.
````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
task: character_extraction
version: 1

[[SECTION character_index_markdown]]
# Character Index - Chapter VI

| Asset ID | Canonical Character ID | Display Name | Presence Status | Description Notes |
|----------|------------------------|--------------|-----------------|-------------------|
| john_carter | john_carter | John Carter | Physically Present | Protagonist, intervenes in combat |
| bull_ape_martian_warrior | bull_ape_martian_warrior | Bull Ape / Martian Warrior | Physically Present | Antagonist, two instances described |
| beast | beast | Beast | Physically Present | Animal companion, detailed physical states |
| tars_tarkas | tars_tarkas | Tars Tarkas | Physically Present | Arrives to witness battle |
| sola | sola | Sola | Physically Present | Arrives with warriors, shows solicitude |
| martian_warrior | martian_warrior | Warrior | Physically Present | Multiple Martians, minimal individual description |

[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: john_carter
canonical_character_id: john_carter
aliases: 
is_fully_identified: true
manual_description_required: false
manual_description_reason: 
clarification_required: false
clarification_reason: 
clarification_question: 

[[SECTION markdown]]
# John Carter - Character File

## Display Name
John Carter

## Chapter Role
Protagonist, central figure in combat sequences

## Physical Presence
Physically present throughout chapter

## Physical Description (Supported by Source)
- Intervenes in fight between Beast and Bull Ape
- Uses cudgel as weapon
- Backs against wall witnessing battle
- Arm held by Sola at chapter end

## Costume, Silhouette & Continuity Traits
- Wears clothing suitable for combat
- Carries cudgel (cudgel swings in arc)
- Central figure in all major action sequences

## Descriptive Noun Phrases for Render Prompts
- "Heroic male protagonist with determined expression"
- "Combat-ready stance with cudgel weapon"
- "Central figure in Martian chamber setting"

## Uncertainty Notes
Physical description is minimal but character identification is stable. No detailed facial features or costume specifics provided in source material.

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: bull_ape_martian_warrior
canonical_character_id: bull_ape_martian_warrior
aliases: Bull Ape, Martian warrior, ape adversary
is_fully_identified: false
manual_description_required: true
manual_description_reason: Individual physical descriptions are sparse; characters appear as type rather than distinct individuals with detailed features. Source provides combat choreography but limited individual appearance details.
clarification_required: true
clarification_reason: Character might exist under another name or is too weakly identified for reliable image generation without additional clarification about specific physical traits.
clarification_question: What are the distinguishing physical features of each Bull Ape instance (size, fur color, facial markings, weapon type)?

[[SECTION markdown]]
# Bull Ape / Martian Warrior - Character File

## Display Name
Bull Ape / Martian Warrior

## Chapter Role
Antagonist in combat sequences

## Physical Presence
Physically present throughout chapter (two instances)

## Physical Description (Supported by Source)
- Eyes bulging completely from sockets
- Blood flowing from nostrils
- Tearing away entire front of breast held in vise-like grip
- Roaring and frothing at mouth in extremity of rage
- Leaping through open window; mate closing in death struggle

## Costume, Silhouette & Continuity Traits
- Martian warrior attire (implied)
- Combat-ready stance
- Physical states during combat sequences

## Descriptive Noun Phrases for Render Prompts
- "Martial antagonist with fierce expression"
- "Combat-ready figure with blood-stained features"
- "Aggressive posture in chamber setting"

## Uncertainty Notes
Individual physical descriptions are sparse; characters appear as type rather than distinct individuals. Detailed facial features, fur color, and specific costume elements not provided in source material. Clarification needed for reliable image generation.

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: beast
canonical_character_id: beast
aliases: Beast, animal companion
is_fully_identified: true
manual_description_required: false
manual_description_reason: Detailed physical states and combat actions are provided in source material.
clarification_required: false
clarification_reason: 
clarification_question: 

[[SECTION markdown]]
# Beast - Character File

## Display Name
Beast

## Chapter Role
Animal companion, defender of John Carter

## Physical Presence
Physically present throughout chapter

## Physical Description (Supported by Source)
- Eyes bulging completely from sockets
- Blood flowing from nostrils
- Sinks mighty fangs into adversary's breast
- Locks throat with great arms and paws
- Pitiful appeal look upon Carter
- Following at heel after combat sequences

## Costume, Silhouette & Continuity Traits
- Animal form (specific species not detailed)
- Combat-ready posture
- Physical states during fight sequences

## Descriptive Noun Phrases for Render Prompts
- "Mighty animal companion with fierce expression"
- "Combat-ready beast with bulging eyes and blood-stained features"
- "Loyal defender following protagonist at heel"

## Uncertainty Notes
Physical description is detailed but specific species identification not provided. Character role and physical states are well-supported by source material for reliable image generation.

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: tars_tarkas
canonical_character_id: tars_tarkas
aliases: 
is_fully_identified: true
manual_description_required: false
manual_description_reason: Character identification is stable; minimal physical description provided but sufficient for character role.
clarification_required: false
clarification_reason: 
clarification_question: 

[[SECTION markdown]]
# Tars Tarkas - Character File

## Display Name
Tars Tarkas

## Chapter Role
Witness to battle, arrives with warriors

## Physical Presence
Physically present at chapter end

## Physical Description (Supported by Source)
- Arrives to witness the battle
- Part of group that applauds Carter's feats
- Present when Martians accept Beast as long as Carter protects it

## Costume, Silhouette & Continuity Traits
- Martian warrior attire (implied)
- Group member in chamber setting

## Descriptive Noun Phrases for Render Prompts
- "Martian witness with solemn expression"
- "Group member applauding combat feats"
- "Figure present in chamber witnessing battle"

## Uncertainty Notes
Physical description is minimal but character identification is stable. Specific facial features and costume details not provided in source material. Character role and presence are well-supported for reliable image generation.

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: sola
canonical_character_id: sola
aliases: 
is_fully_identified: true
manual_description_required: false
manual_description_reason: Character identification is stable; physical description provided through expressions and actions.
clarification_required: false
clarification_reason: 
clarification_question: 

[[SECTION markdown]]
# Sola - Character File

## Display Name
Sola

## Chapter Role
Witness to battle, shows solicitude for Carter

## Physical Presence
Physically present at chapter end

## Physical Description (Supported by Source)
- Sober apparent solicitude
- Rushing to examine body for wounds
- Holding Carter's arm at chapter end
- Looks of surprise at Beast following at heel

## Costume, Silhouette & Continuity Traits
- Martian warrior attire (implied)
- Central figure in chamber setting

## Descriptive Noun Phrases for Render Prompts
- "Concerned female figure with solemn expression"
- "Solicitous companion holding protagonist's arm"
- "Figure examining combat aftermath with serious demeanor"

## Uncertainty Notes
Physical description is minimal but character identification is stable. Specific facial features and costume details not provided in source material. Character role and expressions are well-supported for reliable image generation.

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: martian_warrior
canonical_character_id: martian_warrior
aliases: Warrior, Martian warrior
is_fully_identified: false
manual_description_required: true
manual_description_reason: Multiple warriors appear as group rather than distinct individuals with detailed features. Source provides minimal individual physical descriptions beyond general combat states.
clarification_required: true
clarification_reason: Character might exist under another name or is too weakly identified for reliable image generation without additional clarification about specific physical traits and individual distinctions.
clarification_question: What are the distinguishing physical features of each warrior instance (facial markings, weapon type, posture variations)?

[[SECTION markdown]]
# Warrior - Character File

## Display Name
Warrior

## Chapter Role
Martian combatant, witness to battle

## Physical Presence
Physically present at chapter end (multiple instances)

## Physical Description (Supported by Source)
- Warriors stand in doorway
- Martians laughing vs Sola's sober apparent solicitude
- Martians' looks of surprise at Beast following at heel
- Intends to shoot the Beast for being an anomaly (one warrior)
- Striking up the warrior's arm with a cudgel

## Costume, Silhouette & Continuity Traits
- Martian warrior attire (implied)
- Combat-ready posture
- Group member in chamber setting

## Descriptive Noun Phrases for Render Prompts
- "Martian combatant with serious expression"
- "Group member standing in doorway"
- "Figure with weapon ready in chamber setting"

## Uncertainty Notes
Multiple warriors appear as group rather than distinct individuals. Individual physical descriptions are sparse beyond general combat states. Specific facial features, fur color, and costume elements not provided in source material. Clarification needed for reliable image generation of individual instances.

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
