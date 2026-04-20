# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-20T00:15:56.757767+00:00
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

**Narrative Arc:**
- **Introduction:** Carter explains his ageless state, fear of death, and purpose in writing this chronicle to avoid being pilloried as a liar.
- **Backstory:** Details the gold discovery with Powell (March 1865-1866) and the decision for Powell to return to civilization to purchase machinery while Carter holds the claim.
- **Incident:** Powell departs March 3, 1866. Apaches intercept him. Carter pursues on horseback.
- **Climax:** Carter finds Powell dead in an Apache camp. Charges warriors, escapes via wrong trail due to horse behavior.
- **Resolution:** Horse leads to cave entrance. Carter carries Powell's body into the cave chamber and collapses from exhaustion inside.

**Visual Continuity:**
- **Location:** Arizona Hills -> Valley -> Pass -> Cave Entrance (approx 4ft high).
- **Characters:** John Carter, James K. Powell (Corpse), Apache Warriors, Burros, Horses.
- **Props:** Colt Revolvers, Carbine, Cartridge Belts, Canteen, Saddle Horse.
- **State:** Powell (Dead, Arrowed), Carter (Alive, Exhausted, Armed).
- **Environment:** Clear Arizona mornings, Moonlight, Dark shadows of range, Cave interior (smooth floor, dense shadow at back).
````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
task: character_extraction
version: 1

[[SECTION character_index_markdown]]
# Character Index - Chapter CH001

| Asset ID | Canonical ID | Display Name | Status | Description Complete |
|----------|--------------|--------------|--------|---------------------|
| john_carter | john_carter | John Carter | Physically Present | Partial |
| james_k_powell | james_k_powell | James K. Powell | Referenced (Corpse) | Partial |
| apache_warriors | apache_warriors | Apache Warriors | Referenced (Group) | Partial |

**Notes:** All characters have incomplete physical descriptions for image generation purposes. Additional manual descriptions required.
[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: john_carter
canonical_character_id: john_carter
aliases: 
is_fully_identified: true
manual_description_required: true
manual_description_reason: Physical description incomplete for image generation - only armed state, exhaustion level, and alive status documented. No facial features, height, build, or distinctive markings provided in source material.
clarification_required: false
clarification_reason: 
clarification_question: 

[[SECTION markdown]]
# John Carter

**Display Name:** John Carter  
**Chapter Role:** Protagonist / Narrator  
**Physical Presence:** Physically Present (Alive)  
**Current State:** Armed, Exhausted, Alive  

## Physical Description (Source-Supported)
- **Armed Status:** Colt Revolvers, Carbine, Cartridge Belts documented
- **Condition:** Alive but exhausted from carrying Powell's body
- **Location Context:** Arizona Hills → Valley → Pass → Cave Entrance

## Continuity-Critical Traits
- **Equipment:** Saddle Horse (leads to cave entrance), Canteen, Colt Revolvers, Carbine
- **Action State:** Pursuing Apache camp after finding Powell dead
- **Movement:** On horseback during chase sequence

## Uncertainty Notes
**Missing Details for Image Generation:**
- No facial features or expression documented
- Height and build not specified
- Hair color/style unknown
- Eye color not mentioned
- Distinctive markings or scars absent from source
- Clothing details beyond "armed" status incomplete

**Render-Facing Prompt Suggestions:**
- Use armed frontier man archetype
- Emphasize exhaustion through posture (slumped, heavy breathing)
- Include equipment: Colt Revolvers, Carbine, cartridge belts
- Setting: Arizona morning light or moonlight depending on scene
- Horse companion present in many scenes

**Source Limitations:**
The chapter summary provides narrative context but lacks detailed physical description for dependable image generation. Manual description required to complete character visualization.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: james_k_powell
canonical_character_id: james_k_powell
aliases: 
is_fully_identified: true
manual_description_required: true
manual_description_reason: Physical description incomplete for image generation - only dead state, arrowed condition, and corpse status documented. No facial features, height, build, or distinctive markings provided in source material.
clarification_required: false
clarification_reason: 
clarification_question: 

[[SECTION markdown]]
# James K. Powell

**Display Name:** James K. Powell  
**Chapter Role:** Deceased Companion / Victim  
**Physical Presence:** Referenced (Corpse)  
**Current State:** Dead, Arrowed  

## Physical Description (Source-Supported)
- **Condition:** Dead (corpse state documented)
- **Cause of Death:** Apache attack (arrowed)
- **Location Context:** Found in Apache camp, later carried into cave

## Continuity-Critical Traits
- **Equipment:** None (deceased)
- **Action State:** Body found by Carter after pursuit
- **Movement:** Carried by Carter from Apache camp to cave entrance

## Uncertainty Notes
**Missing Details for Image Generation:**
- No facial features or expression documented (corpse state)
- Height and build not specified
- Hair color/style unknown
- Eye color not mentioned
- Distinctive markings or scars absent from source
- Clothing details beyond "corpse" status incomplete

## Render-Facing Prompt Suggestions
- Use deceased frontier man archetype
- Emphasize arrow wounds on body
- Include context: found in Apache camp, carried into cave
- Setting: Arizona morning light (clear mornings documented)
- Body state: Exhausted from journey, collapsed inside cave chamber

**Source Limitations:**
The chapter summary provides narrative context but lacks detailed physical description for dependable image generation. Manual description required to complete character visualization.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: apache_warriors
canonical_character_id: apache_warriors
aliases: 
is_fully_identified: false
manual_description_required: true
manual_description_reason: Physical description incomplete for image generation - only group status, warrior role, and attack context documented. No individual facial features, height, build, or distinctive markings provided in source material.
clarification_required: true
clarification_reason: Collective group may already exist under another name or is too weakly identified as a unified entity for consistent character tracking across chapters.
clarification_question: Should Apache Warriors be treated as a single collective character asset or broken into individual warrior assets for more detailed physical descriptions?

[[SECTION markdown]]
# Apache Warriors

**Display Name:** Apache Warriors  
**Chapter Role:** Antagonists / Attackers  
**Physical Presence:** Referenced (Group)  
**Current State:** Active during attack sequence  

## Physical Description (Source-Supported)
- **Condition:** Active warriors during camp attack
- **Role:** Intercepted Powell, killed him, pursued Carter
- **Location Context:** Apache camp in Arizona range

## Continuity-Critical Traits
- **Equipment:** None individually documented (group status only)
- **Action State:** Attacking, pursuing, intercepting
- **Movement:** Camp-based, range environment

## Uncertainty Notes
**Missing Details for Image Generation:**
- No individual facial features or expressions documented
- Height and build not specified
- Hair color/style unknown
- Eye color not mentioned
- Distinctive markings or scars absent from source
- Clothing details beyond "warrior" status incomplete
- Number of warriors not specified

## Render-Facing Prompt Suggestions
- Use Apache warrior archetype (collective)
- Emphasize attack context: camp raid, pursuit
- Include setting: Arizona range, dark shadows of range documented
- Group composition: Multiple warriors in camp environment
- Action state: Attacking, pursuing, intercepting

**Source Limitations:**
The chapter summary provides narrative context but lacks detailed physical description for dependable image generation. Manual description required to complete character visualization. Collective group status may require clarification on asset structure.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
