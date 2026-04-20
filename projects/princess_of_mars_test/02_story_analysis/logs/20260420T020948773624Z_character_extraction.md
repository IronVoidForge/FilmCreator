# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-20T02:09:48.773624+00:00
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

Chapter id: CH003

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

# Chapter III: My Advent on Mars

## Narrative Arc
1. **Awakening & Physics:** Protagonist wakes on Mars, realizes lower gravity via jumping (3 yards high). Struggles with walking mechanics (hopping/sprawling) due to unfamiliar muscular exertion.
2. **Incubator Discovery:** Finds glass-walled enclosure containing large eggs (2.5 ft diameter) hatching into six-legged creatures (later clarified as two legs/arms + intermediaries). Creatures have blood red eyes, yellowish-green bodies.
3. **Confrontation & Escape:** Adult Martians arrive on mounts (10 ft shoulder height). Leader's spear (40 ft long) nearly hits protagonist. Protagonist jumps 30 ft high to escape enclosure.
4. **First Contact Resolution:** Martians observe agility, shift intent from killing to capturing. Leader approaches unarmed, offers metal armlet. Protagonist accepts and bows.
5. **Departure:** Protagonist rides behind Martian mount with others towards hills.

## Visual Continuity
- **Environment:** Yellowish moss, low hills, midday sun.
- **Enclosure:** Glass roof (4-5 inches thick), wall height (4 feet).
- **Creatures:** Egg diameter (2.5 ft), Eye placement (side-set, protruding), Body color (light yellowish-green).
- **Martians:** Height (15 ft Earth weight), Mount shoulder height (10 ft), Spear length (40 ft).
- **Rifles:** White metal stock, aluminum/steel barrel.
````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
task: character_extraction
version: 1

[[SECTION character_index_markdown]]
# Character Index - Chapter III: My Advent on Mars

| Asset ID | Canonical Character ID | Aliases | Fully Identified | Manual Description Required |
|----------|------------------------|---------|------------------|----------------------------|
| protagonist | protagonist | - | false | true |
| martian_leader | martian_leader | leader, spear-bearer | false | true |
| martians_group | martians_group | adult Martians, mount-riders | false | true |

**Notes:** All characters lack sufficient physical/visual description for dependable image generation. Manual descriptions are required for all entries.
[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: protagonist
canonical_character_id: protagonist
aliases: -
is_fully_identified: false
manual_description_required: true
manual_description_reason: No physical description, costume details, or visual identifiers provided in chapter. Narrative is first-person experience without appearance documentation.
clarification_required: true
clarification_reason: Character lacks stable identification for image generation purposes.
clarification_question: What are the protagonist's approximate height, build, hair color, and any distinguishing physical features?

[[SECTION markdown]]
# Protagonist - Chapter III

**Display Name:** Protagonist  
**Chapter Role:** First-person narrator, main character experiencing Mars awakening and first contact  
**Physical Presence:** Physically present throughout chapter (wakes, jumps, walks, escapes)  
**Physical Description:** Unknown - no visual documentation in source material  
**Costume/Silhouette:** Unknown - no clothing or appearance details provided  
**Continuity-Critical Traits:** None documented in chapter  
**Uncertainty Notes:** All physical and visual attributes are completely undocumented. Cannot generate reliable images without manual description. Display name only; no stable identification for render-facing prompts.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: martian_leader
canonical_character_id: martian_leader
aliases: leader, spear-bearer
is_fully_identified: false
manual_description_required: true
manual_description_reason: No individual physical description provided. Only role (leader), weapon (40 ft spear), and action (approaches unarmed) documented. Height/weight/silhouette unknown.
clarification_required: true
clarification_reason: Character lacks stable identification for image generation purposes.
clarification_question: What are the leader's approximate height, build, skin tone, hair color, facial features, and any distinguishing marks or accessories beyond the metal armlet?

[[SECTION markdown]]
# Martian Leader - Chapter III

**Display Name:** Martian Leader  
**Chapter Role:** Primary contact figure, spear-bearer who offers metal armlet  
**Physical Presence:** Physically present (approaches protagonist unarmed)  
**Physical Description:** Unknown - no visual documentation in source material  
**Costume/Silhouette:** Unknown - only weapon (40 ft spear) and offered item (metal armlet) documented  
**Continuity-Critical Traits:** Spear-bearer, approaches unarmed, offers metal armlet  
**Uncertainty Notes:** All physical attributes are completely undocumented. Cannot generate reliable images without manual description. Role-based identification only; no stable visual features for render-facing prompts.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: martians_group
canonical_character_id: martians_group
aliases: adult Martians, mount-riders
is_fully_identified: false
manual_description_required: true
manual_description_reason: Group reference only. No individual physical descriptions provided. Only collective traits (height 15 ft Earth weight, mount shoulder height 10 ft) documented.
clarification_required: true
clarification_reason: Character lacks stable identification for image generation purposes.
clarification_question: What are the approximate height, build, skin tone, hair color, facial features, and any distinguishing marks or accessories for individual Martians in the group?

[[SECTION markdown]]
# Martian Group - Chapter III

**Display Name:** Martian Group  
**Chapter Role:** Secondary contact figures, mount-riders observing protagonist  
**Physical Presence:** Physically present (arrive on mounts, observe agility)  
**Physical Description:** Unknown - no individual visual documentation in source material  
**Costume/Silhouette:** Unknown - only collective height (15 ft Earth weight) and mount shoulder height (10 ft) documented  
**Continuity-Critical Traits:** Mount-riders, observe protagonist's agility, shift intent from killing to capturing  
**Uncertainty Notes:** All individual physical attributes are completely undocumented. Cannot generate reliable images without manual description. Group-based identification only; no stable visual features for render-facing prompts.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_PACKET]]
````
