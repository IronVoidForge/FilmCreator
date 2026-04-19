# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-19T23:51:08.043993+00:00
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

**Visual Continuity:**
- Environment: Yellowish moss terrain, glass enclosure roof (4-5 inches thick), low hills in distance.
- Flora/Fauna: Giant eggs (2.5 ft diameter), hatchlings (six legs, red eyes, white tusks), adult Martians (15 ft tall), mounts (dark slate color, four legs each side, broad tail).
- Equipment: Metal-shod spears (40 ft long), rifles (white metal/wood stock, aluminum/steel barrel).

**Narrative Arc:**
1. Waking & Gravity Test: Narrator wakes on Mars, discovers low gravity via hopping instead of walking.
2. Discovery: Finds glass incubator with hatching eggs and strange hatchlings.
3. Encounter: Adult Martians arrive; narrator nearly impaled by spear but escapes using agility leap.
4. Resolution: Martian leader approaches unarmed, offers metal armlet for peace. Narrator accepts armlet and rides off towards hills.
````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
task: character_extraction
version: 1

[[SECTION character_index_markdown]]
# Character Index - CH003

| Asset ID | Display Name | Role | Physical Presence | Description Status |
|----------|--------------|------|-------------------|-------------------|
| narrator | The Narrator | Protagonist | Present | Manual description required |
| martian_adults | Adult Martians | Antagonists | Referenced | Manual description required |
| martian_leader | Martian Leader | Peace Offerer | Present | Manual description required |

**Notes:** All characters lack sufficient physical/visual description in source material for dependable image generation.
[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: narrator
canonical_character_id: narrator
aliases: 
is_fully_identified: true
manual_description_required: true
manual_description_reason: Source chapter provides narrative events but no physical description of narrator's appearance, clothing, or distinguishing features. Only actions and movements are documented (waking, hopping, finding eggs, escaping spear).
clarification_required: false
clarification_reason: 
clarification_question: 

[[SECTION markdown]]
# Narrator - CH003

**Display Name:** The Narrator  
**Chapter Role:** Protagonist / First-Person Observer  
**Physical Presence:** Present (waking on Mars, hopping through terrain, finding incubator, encountering Martians)  

## Physical Description
*Source-supported details:* None provided in chapter material. Character is identified only through narrative actions and perspective.

## Costume & Silhouette
*Source-supported details:* Unknown. No clothing or physical form described in source text.

## Continuity-Critical Traits
- Uses agility leap to escape spear attack (demonstrates physical capability)
- Accepts metal armlet from Martian leader (wears as peace token)
- Rides off towards hills after encounter

## Render-Facing Prompt Notes
**Uncertainty:** Physical appearance, clothing, and distinguishing features are not documented in source material. Any visual representation will be speculative based on narrative context alone.

**Suggested Approach:** Focus on character actions and emotional state rather than physical details when generating imagery. Consider silhouette-based or expression-focused prompts to capture the character's presence without inventing unsupported physical traits.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: martian_adults
canonical_character_id: martian_adults
aliases: 
is_fully_identified: false
manual_description_required: true
manual_description_reason: Chapter references adult Martians as arriving and nearly impaling narrator, but provides no individual physical descriptions. Only general traits are mentioned (15 ft tall, dark slate mounts). Character identification is weak - they function as a group rather than individually identified entities.
clarification_required: true
clarification_reason: Adult Martians may exist under different names or be too weakly identified for reliable image generation without additional source material.
clarification_question: Are there any additional chapters or source documents that provide physical descriptions of the adult Martians beyond the general height and mount information?

[[SECTION markdown]]
# Adult Martians - CH003

**Display Name:** Adult Martians  
**Chapter Role:** Antagonists / Encounter Group  
**Physical Presence:** Referenced (arrive, nearly impale narrator)  

## Physical Description
*Source-supported details:* 15 ft tall. No individual facial features, skin texture, or body structure described beyond general size.

## Costume & Silhouette
*Source-supported details:* Dark slate mounts with four legs each side and broad tail. No clothing or armor described on Martians themselves.

## Continuity-Critical Traits
- Arrive in group formation
- Use metal-shod spears (40 ft long) for attack
- One approaches unarmed to offer peace (Martian Leader)
- Offer metal armlet as peace token

## Render-Facing Prompt Notes
**Uncertainty:** Individual Martians are not physically described beyond general size. They function as a group entity rather than individually identified characters. Mounts are described but Martians' physical form is vague.

**Suggested Approach:** Consider depicting the group as silhouettes or shadow figures to acknowledge their presence without inventing unsupported physical details. Focus on the dramatic encounter moment rather than detailed character portraits.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: martian_leader
canonical_character_id: martian_leader
aliases: 
is_fully_identified: true
manual_description_required: true
manual_description_reason: Chapter identifies this specific Martian as approaching unarmed to offer peace, but provides no physical description of appearance, clothing, or distinguishing features. Only actions and intent are documented (offering armlet for peace).
clarification_required: false
clarification_reason: 
clarification_question: 

[[SECTION markdown]]
# Martian Leader - CH003

**Display Name:** Martian Leader  
**Chapter Role:** Peace Offerer / Resolution Figure  
**Physical Presence:** Present (approaches narrator unarmed, offers armlet)  

## Physical Description
*Source-supported details:* None provided in chapter material. Character is identified only through actions and intent (peace offering).

## Costume & Silhouette
*Source-supported details:* Unknown. No clothing or physical form described in source text.

## Continuity-Critical Traits
- Approaches unarmed (demonstrates peaceful intent)
- Offers metal armlet as peace token
- Narrator accepts armlet and rides off towards hills after encounter

## Render-Facing Prompt Notes
**Uncertainty:** Physical appearance, clothing, and distinguishing features are not documented in source material. Character is identified only through narrative actions and emotional state (peace offering).

**Suggested Approach:** Consider depicting this character with visual cues that suggest peaceful intent (open posture, unarmed stance) rather than physical details. Focus on the symbolic gesture of offering the armlet as the key visual element.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
