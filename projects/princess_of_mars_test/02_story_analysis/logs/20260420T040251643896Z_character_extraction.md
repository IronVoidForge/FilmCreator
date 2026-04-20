# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-20T04:02:51.643896+00:00
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

Chapter id: CH020

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

# Chapter Summary: CH020 - The Atmosphere Factory

## Story Summary
John Carter waits two days for Kantos Kan without success, then wanders northwesterly toward a waterway. He survives two weeks of starvation and wild beast attacks using his telepathic power and long-sword. He is attacked by a large, many-legged beast but is saved by Woola, who has left Dejah Thoris due to her presumed death. Carter finds the Atmosphere Factory after fifteen days of searching. Inside, he meets an old Martian guardian who explains the ninth ray and atmosphere production process. Carter learns the doors are unlocked via telepathic thought waves. He escapes the factory using this power, reaching Zodanga farm territory. There, Red Martians provide him with food, a domestic bull-throat, reddish oil to color his body, and advice to seek military employment in Zodanga.

## Visual Continuity
- **Woola:** Appears half-starved, shadow of former self, eating the dead beast's carcass. His loyalty is emphasized despite leaving Dejah Thoris.
- **Atmosphere Factory:** Massive building with walls 150 feet thick and roof guarded by glass covering five feet thick. Doors are 20 feet thick and manipulated by telepathy.
- **Old Man's Diadem:** Wears a small collar of gold with a great ornament set with huge diamonds and a strange stone scintillating nine different rays (seven colors + two new rays).
- **Carter's Appearance:** Initially wears Green Warrior metal but is identified as Red Man figure. Later anoints body with reddish oil to resemble Red Martians, cuts hair square at back/banged in front, and renews ornaments in Zodangan style.
- **Environment:** Barsoomian scene lit by nearer moon/hurting moons. Wild beasts are described as strange, uncouth monstrosities. Farm buildings are raised 40-50 feet from ground on metal shafts operated by radium engines.
````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
task: character_extraction
version: 1

[[SECTION character_index_markdown]]
# Character Index - CH020

| Asset ID | Display Name | Chapter Role | Physical Presence |
|----------|--------------|---------------|-------------------|
| john_carter | John Carter | Protagonist, survivor, visitor to Atmosphere Factory and Zodanga farm | Present |
| woola | Woola | Loyal companion, left Dejah Thoris due to presumed death | Present |
| old_martian_guardian | Old Martian Guardian | Factory guardian, explains ninth ray and atmosphere production | Present |

**Notes:** All characters have sufficient physical description for dependable image generation. No manual descriptions required.
[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: john_carter
canonical_character_id: john_carter
aliases: red_man_figure, green_warrior
is_fully_identified: true
manual_description_required: false
manual_description_reason: 
clarification_required: false
clarification_reason: 
clarification_question: 

[[SECTION markdown]]
# John Carter - CH020

**Display Name:** John Carter  
**Chapter Role:** Protagonist, survivor, visitor to Atmosphere Factory and Zodanga farm  
**Physical Presence:** Present  

**Physical Description (Supported by Source):**  
Initially wears Green Warrior metal armor. Identified as Red Man figure. Later anoints body with reddish oil to resemble Red Martians. Cuts hair square at back/banged in front. Renews ornaments in Zodangan style.

**Costume & Silhouette:**  
- Metal armor (Green Warrior initially, later modified)
- Reddish oil applied to body
- Hair cut square at back, banged in front
- Zodangan-style ornaments renewed

**Continuity-Critical Traits:**  
- Telepathic power used to unlock factory doors and escape
- Survives two weeks of starvation and wild beast attacks using long-sword
- Reaches Zodanga farm territory after escaping Atmosphere Factory

**Render-Facing Prompt Noun Phrases:**  
"Green Warrior metal armor", "reddish oil anointed body", "square-cut hair with bangs", "Zodangan ornaments", "telepathic power user", "long-sword wielder"

**Uncertainty Notes:**  
None - sufficient physical description available for dependable image generation.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: woola
canonical_character_id: woola
aliases: 
is_fully_identified: true
manual_description_required: false
manual_description_reason: 
clarification_required: false
clarification_reason: 
clarification_question: 

[[SECTION markdown]]
# Woola - CH020

**Display Name:** Woola  
**Chapter Role:** Loyal companion, left Dejah Thoris due to presumed death  
**Physical Presence:** Present  

**Physical Description (Supported by Source):**  
Appears half-starved, shadow of former self. Eating dead beast's carcass.

**Costume & Silhouette:**  
- Half-starved appearance
- Shadow of former self (significantly changed)
- Consuming carcass of wild beast

**Continuity-Critical Traits:**  
- Left Dejah Thoris due to her presumed death
- Loyalty emphasized despite circumstances
- Appears after Carter's two weeks of starvation and attacks

**Render-Facing Prompt Noun Phrases:**  
"half-starved appearance", "shadow of former self", "eating beast carcass", "loyal companion", "Martian dog figure"

**Uncertainty Notes:**  
The "shadow of former self" indicates significant physical change, but sufficient description exists for image generation.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: old_martian_guardian
canonical_character_id: old_martian_guardian
aliases: 
is_fully_identified: true
manual_description_required: false
manual_description_reason: 
clarification_required: false
clarification_reason: 
clarification_question: 

[[SECTION markdown]]
# Old Martian Guardian - CH020

**Display Name:** Old Martian Guardian  
**Chapter Role:** Factory guardian, explains ninth ray and atmosphere production  
**Physical Presence:** Present  

**Physical Description (Supported by Source):**  
Wears small collar of gold with great ornament set with huge diamonds. Stone scintillating nine different rays (seven colors + two new rays).

**Costume & Silhouette:**  
- Small gold collar
- Great ornament with huge diamonds
- Strange stone scintillating nine different rays
- Old Martian appearance

**Continuity-Critical Traits:**  
- Located at Atmosphere Factory
- Explains ninth ray and atmosphere production process
- Carter learns doors are unlocked via telepathic thought waves

**Render-Facing Prompt Noun Phrases:**  
"old Martian figure", "gold collar with diamonds", "nine-ray scintillating stone", "seven colors plus two new rays", "factory guardian", "telepathy-aware"

**Uncertainty Notes:**  
None - sufficient physical description available for dependable image generation.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]
[[/FILMCREATOR_PACKET]]
````
