# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-20T03:26:23.785184+00:00
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

**Visual Context:**
- Landscape: Yellowish moss, quartz rocks, low hills, frozen poles (mentioned as exception).
- Enclosure: Glass roof (4-5 inches thick), 4 feet high wall, no doors/windows on near side.
- Eggs: Snowy white, 2.5 ft diameter, hatching process visible.
- Martians: Olive green skin (darker in males), blood red iris, six limbs (young), antennae ears, longitudinal slit noses.
- Mounts: Slate color, four legs, broad flat tail, nailless feet.
- Weapons: Metal-shod spear (40 feet long), rifle (white metal/wood stock).

**Story Beats:**
1. Awakening & Gravity Check: Narrator wakes in circular basin. Tests movement; hops instead of walking due to low gravity.
2. The Incubator: Discovers glass-walled enclosure with giant eggs. Observes hatching grotesque creatures.
3. Warrior Arrival: Adult Martians approach silently on mounts. Leader's spear nearly hits narrator. Mounts described (slate color, four legs).
4. The Leap: Narrator jumps 30 feet to escape spear point. Lands safely across enclosure. Martians observe with astonishment.
5. Negotiation & Ride: Leader approaches unarmed. Offers metal armlet. Narrator accepts. Taken prisoner on mount, cavalcade rides toward hills.
````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
task: character_extraction
version: 1

[[SECTION character_index_markdown]]
# Character Index - CH003

| Asset ID | Canonical Character ID | Display Name | Chapter Role | Presence Status | Fully Identified | Manual Description Required |
|----------|------------------------|--------------|---------------|-----------------|------------------|----------------------------|
| narrator_ch003 | narrator_main | Narrator | First-person protagonist, awakening in circular basin | Physically present | true | true |
| martian_leader_ch003 | martian_adult_leader | Martian Leader | Adult warrior approaching with spear, then unarmed | Physically present | true | true |
| martian_soldier_ch003 | martian_adult_soldier | Other Martians | Adult warriors on mounts observing narrator | Physically present | true | true |
| hatching_creature_ch003 | creature_egg_hatchling | Hatching Creatures | Grotesque creatures emerging from giant eggs | Physically present | false | true |

**Notes:**
- All characters have olive green skin, blood red iris, six limbs, antennae ears, longitudinal slit noses (Martians)
- Physical descriptions are insufficient for complete image generation
- Hatching creatures lack stable identification
[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: narrator_ch003
canonical_character_id: narrator_main
aliases: 
is_fully_identified: true
manual_description_required: true
manual_description_reason: Insufficient physical appearance details for dependable image generation - only movement behavior (hopping due to low gravity) is documented, no facial features, hair, body type, or clothing described in source material.
clarification_required: false
clarification_reason: 
clarification_question: 

[[SECTION markdown]]
# Narrator

**Display Name:** Narrator  
**Chapter Role:** First-person protagonist awakening in circular basin  
**Presence Status:** Physically present (wakes in circular basin, tests movement, hops)  

**Physical Description:**  
- Movement behavior: Hops instead of walking due to low gravity environment  
- No specific facial features, hair, body type, or clothing documented in source material  

**Costume/Silhouette Traits:**  
- Unknown - no clothing or physical appearance details provided in chapter summary  

**Continuity-Critical Traits:**  
- Capable of 30-foot jumps (demonstrated when escaping spear point)  
- Lands safely across enclosure without injury  

**Uncertainty Notes:**  
- Physical appearance is completely undocumented for image generation purposes  
- No clothing, facial features, or body type described in source material  
- Only behavioral capabilities (hopping, jumping) are known from chapter events  
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: martian_leader_ch003
canonical_character_id: martian_adult_leader
aliases: 
is_fully_identified: true
manual_description_required: true
manual_description_reason: Insufficient physical appearance details for dependable image generation - while species traits are documented (olive green skin, blood red iris, six limbs, antennae ears, longitudinal slit noses), specific individual features like facial markings, exact height, or distinguishing characteristics beyond "leader" status are not described.
clarification_required: false
clarification_reason: 
clarification_question: 

[[SECTION markdown]]
# Martian Leader

**Display Name:** Martian Leader  
**Chapter Role:** Adult warrior approaching with spear, then unarmed negotiator  
**Presence Status:** Physically present (approaches narrator on mount, then approaches unarmed)  

**Physical Description:**  
- Species traits: Olive green skin (darker in males), blood red iris, six limbs (young), antennae ears, longitudinal slit noses  
- Individual features: Not specifically documented beyond species characteristics  

**Costume/Silhouette Traits:**  
- Mounts: Slate color, four legs, broad flat tail, nailless feet  
- Weapons: Metal-shod spear (40 feet long) initially, then unarmed approach  
- Armlet: Offers metal armlet to narrator  

**Continuity-Critical Traits:**  
- Approaches silently on mount  
- Nearly hits narrator with spear point during initial encounter  
- Takes narrator prisoner after negotiation  
- Leads cavalcade toward hills  

**Uncertainty Notes:**  
- Specific facial features or distinguishing marks beyond species traits not documented  
- Gender not explicitly confirmed (though darker skin noted for males)  
- Individual appearance details insufficient for complete image generation  
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: martian_soldier_ch003
canonical_character_id: martian_adult_soldier
aliases: 
is_fully_identified: true
manual_description_required: true
manual_description_reason: Insufficient physical appearance details for dependable image generation - while species traits are documented (olive green skin, blood red iris, six limbs, antennae ears, longitudinal slit noses), specific individual features or distinguishing characteristics beyond "adult Martian on mount" status are not described.
clarification_required: false
clarification_reason: 
clarification_question: 

[[SECTION markdown]]
# Other Martians

**Display Name:** Other Martians  
**Chapter Role:** Adult warriors on mounts observing narrator  
**Presence Status:** Physically present (multiple adult Martians approach on mounts)  

**Physical Description:**  
- Species traits: Olive green skin, blood red iris, six limbs (young), antennae ears, longitudinal slit noses  
- Individual features: Not specifically documented beyond species characteristics  

**Costume/Silhouette Traits:**  
- Mounts: Slate color, four legs, broad flat tail, nailless feet  
- Weapons: Metal-shod spear (40 feet long) visible on at least one mount  

**Continuity-Critical Traits:**  
- Approach silently on mounts  
- Observe narrator with astonishment after 30-foot jump  
- Leader approaches unarmed for negotiation  
- Take narrator prisoner and lead cavalcade toward hills  

**Uncertainty Notes:**  
- Specific facial features or distinguishing marks beyond species traits not documented  
- Individual appearance details insufficient for complete image generation  
- Number of soldiers not specified in chapter summary  
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: hatching_creature_ch003
canonical_character_id: creature_egg_hatchling
aliases: 
is_fully_identified: false
manual_description_required: true
manual_description_reason: Insufficient physical appearance details for dependable image generation - only described as "grotesque creatures" emerging from eggs, no specific anatomical features, size, coloration, or distinguishing characteristics documented in source material.
clarification_required: true
clarification_reason: Hatching creatures lack stable identification and may represent unknown species or transitional forms that require clarification for accurate representation.
clarification_question: Are the hatching creatures intended to be a specific known species, a transitional form of Martians, or entirely separate creatures? What anatomical features should they display?

[[SECTION markdown]]
# Hatching Creatures

**Display Name:** Hatching Creatures  
**Chapter Role:** Grotesque creatures emerging from giant eggs in incubator enclosure  
**Presence Status:** Physically present (visible hatching process documented)  

**Physical Description:**  
- Species traits: Not specifically documented - only described as "grotesque creatures"  
- Individual features: No specific anatomical features, size, coloration, or distinguishing characteristics documented in source material  

**Costume/Silhouette Traits:**  
- Eggs: Snowy white, 2.5 ft diameter  
- Mounts: None documented for hatching creatures  

**Continuity-Critical Traits:**  
- Hatching process visible in glass-walled enclosure  
- Grotesque appearance noted by narrator  
- No interaction with Martians or narrator during hatching phase  

**Uncertainty Notes:**  
- Physical appearance is completely undocumented beyond "grotesque" descriptor  
- Species classification unclear - may be Martian offspring, separate species, or transitional forms  
- Specific anatomical features not described in chapter summary  
- Stable identification insufficient for dependable image generation  
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
