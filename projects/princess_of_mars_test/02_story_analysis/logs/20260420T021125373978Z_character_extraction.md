# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-20T02:11:25.373978+00:00
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

Chapter id: CH004

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

# Visual Continuity Facts
*   **Cityscape:** White marble city with ruined roadway entrance; broad steps leading to table land; plaza surrounded by buildings.
*   **Audience Chamber:** Low building, wide entrance (100 feet), canopy over hall; chamber dotted with carved wooden desks and chairs; rostrum platform.
*   **Martian Appearance:** 10-12 feet tall; naked except ornaments; females have larger tusks and nails on fingers/toes; light olive-green skin (Sola).
*   **Props & Furnishings:** Gleaming white marble inlaid with gold/stones; metal ornaments, feathers, leather trappings; human-sized desks/chairs (too small for Martians); ten-legged creature (frog-headed pony) waddles into room.

# Story Summary Beats
1.  **Arrival at City:** Carter and Tars Tarkas enter the city via ruined roadway; traverse narrow gorge to open valley; approach foot of mountains.
2.  **Audience Chamber Introduction:** ~50 Martians gathered around rostrum; Tars Tarkas (vice-chieftain) explains Carter's capture; formal greeting exchanged between leaders.
3.  **"Sak" Demonstration:** Chieftain requests performance; Carter jumps "sak" successfully, clearing 150 feet; wins approbation from crowd.
4.  **Hunger Negotiation:** Carter demands food/water instead of more jumping; Sola instructed to take him away; they cross plaza toward large building.
5.  **Accommodation:** Sola leads Carter to spacious chamber decorated with murals/mosaics; introduces ten-legged creature (frog-headed pony).

# Scene Decomposition Notes
*   **Scene 1: City Entry.** Focus on transition from mountain gorge to city plaza; visual of white marble architecture.
*   **Scene 2: Audience Chamber.** Focus on size mismatch between Martians and furniture; formal greeting ritual; Tars Tarkas' explanation.
*   **Scene 3: Sak Performance.** Focus on Carter's physical exertion; crowd reaction (laughter/applause); successful jump mechanics.
*   **Scene 4: Negotiation.** Focus on Carter's hunger cues; Sola's intervention; transition from plaza to accommodation building.
*   **Scene 5: Accommodation.** Focus on chamber interior details; introduction of ten-legged creature; establishing rest period.
````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
task: character_extraction
version: 1

[[SECTION character_index_markdown]]
# Character Index - Princess of Mars Chapter CH004

| Asset ID | Canonical Name | Role | Physical Presence | Description Status |
|----------|----------------|------|-------------------|-------------------|
| carter | Carter | Human protagonist, captive | Present | Sparse physical details |
| tars_tarkas | Tars Tarkas | Martian vice-chieftain | Present | General Martian traits |
| sola | Sola | Martian female companion | Present | General Martian traits |
| chieftain | Chieftain | Martian leader | Present | Unnamed, general traits |

*Note: All characters require manual description due to sparse physical details in source material.*
[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: carter
canonical_character_id: Carter
aliases: 
is_fully_identified: true
manual_description_required: true
manual_description_reason: Only identified as human; no specific physical features, height, build, or distinguishing marks documented in chapter. Cannot reliably generate images without additional description.
clarification_required: false
clarification_reason: 
clarification_question: 

[[SECTION markdown]]
# carter.md

## Display Name
Carter

## Chapter Role
Human protagonist; captive brought before Martian leaders

## Physical Presence
**Present** - Physically present in all scenes (city entry, audience chamber, sak performance, negotiation, accommodation)

## Physical Description
**Sparse** - Identified only as human. No specific height, build, hair color, eye color, or distinguishing physical features documented in chapter text.

## Costume/Silhouette
**Unknown** - No costume details provided; appears in standard human form during captivity demonstration

## Continuity-Critical Traits
- Human-sized (too small for Martian furniture)
- Capable of "sak" jumping (150 feet clearance)
- Subject of formal greeting between leaders

## Render-Facing Noun Phrases
- human male captive
- athletic build capable of long jumps
- standard clothing during captivity

## Uncertainty Notes
**CRITICAL**: This character requires manual description for reliable image generation. Current source material provides only "human" designation with no physical details. Recommend adding: height (5'8"-6'0"), hair color, eye color, facial features, and any distinguishing marks before proceeding with visual continuity work.

## Source Material Limitations
Chapter text focuses on action and dialogue rather than physical description of Carter. All visual continuity must be established through manual documentation.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: tars_tarkas
canonical_character_id: Tars Tarkas
aliases: vice-chieftain
is_fully_identified: true
manual_description_required: true
manual_description_reason: Identified by name and role only; physical description limited to general Martian traits (10-12 feet tall, olive-green skin, ornaments). No specific facial features, ornament details, or distinguishing marks documented.
clarification_required: false
clarification_reason: 
clarification_question: 

[[SECTION markdown]]
# tars_tarkas.md

## Display Name
Tars Tarkas

## Chapter Role
Martian vice-chieftain; explains Carter's capture to leaders

## Physical Presence
**Present** - Physically present in audience chamber scenes; delivers formal explanation

## Physical Description
**General Martian Traits**: 10-12 feet tall, light olive-green skin (Sola), naked except ornaments. Specific facial features, ornament types, or distinguishing marks not documented.

## Costume/Silhouette
**Martian Standard**: Ornamented but otherwise nude; silhouette matches general Martian appearance described in chapter

## Continuity-Critical Traits
- Vice-chieftain status (second-in-command)
- Delivers formal explanation of Carter's capture
- Participates in formal greeting ritual with chieftain
- Size mismatch with human furniture noted

## Render-Facing Noun Phrases
- Martian vice-chieftain
- 10-12 foot tall humanoid
- olive-green skin tone
- ornamented but nude
- formal posture during explanation

## Uncertainty Notes
**CRITICAL**: Requires manual description for reliable image generation. Current source provides only general Martian physical traits without specific facial features, ornament details, or distinguishing marks. Recommend documenting: specific ornament types (metal, feathers, leather), facial structure, and any unique identifiers before visual continuity work.

## Source Material Limitations
Chapter text focuses on dialogue and action rather than detailed physical description of Tars Tarkas. Visual continuity must be established through manual documentation of Martian-specific traits.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: sola
canonical_character_id: Sola
aliases: 
is_fully_identified: true
manual_description_required: true
manual_description_reason: Identified by name only; physical description limited to general Martian traits (10-12 feet tall, olive-green skin, larger tusks and nails on fingers/toes). No specific facial features or distinguishing marks documented.
clarification_required: false
clarification_reason: 
clarification_question: 

[[SECTION markdown]]
# sola.md

## Display Name
Sola

## Chapter Role
Martian female; takes Carter away after sak demonstration; leads him to accommodation

## Physical Presence
**Present** - Physically present in audience chamber and accommodation scenes; intervenes during hunger negotiation

## Physical Description
**General Martian Traits**: 10-12 feet tall, light olive-green skin (Sola), naked except ornaments. Female-specific traits: larger tusks and nails on fingers/toes. Specific facial features or ornament details not documented.

## Costume/Silhouette
**Martian Female Standard**: Ornamented but otherwise nude; silhouette matches general Martian female appearance described in chapter

## Continuity-Critical Traits
- Female Martian (distinguished by larger tusks/nails)
- Takes charge during hunger negotiation
- Leads Carter to accommodation chamber
- Introduces ten-legged creature to Carter

## Render-Facing Noun Phrases
- Martian female companion
- 10-12 foot tall humanoid
- olive-green skin tone
- ornamented but nude
- larger tusks and nails (female trait)
- formal intervention posture

## Uncertainty Notes
**CRITICAL**: Requires manual description for reliable image generation. Current source provides only general Martian physical traits without specific facial features, ornament details, or distinguishing marks beyond female-specific traits. Recommend documenting: specific ornament types, facial structure, and any unique identifiers before visual continuity work.

## Source Material Limitations
Chapter text focuses on action and dialogue rather than detailed physical description of Sola. Visual continuity must be established through manual documentation of Martian-specific traits and female distinguishing features.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: chieftain
canonical_character_id: Chieftain
aliases: 
is_fully_identified: false
manual_description_required: true
manual_description_reason: Identified only as "Chieftain" without personal name; physical description limited to general Martian traits (10-12 feet tall, olive-green skin). No specific facial features or distinguishing marks documented.
clarification_required: true
clarification_reason: Character is unnamed in source material; may already exist under another name or be too weakly identified for reliable visual continuity work.
clarification_question: Does the chieftain have a personal name not mentioned in this chapter, or should we document him as "Chieftain" only?

[[SECTION markdown]]
# chieftain.md

## Display Name
Chieftain (unnamed)

## Chapter Role
Martian leader; requests sak demonstration from Carter; exchanges formal greeting with vice-chieftain

## Physical Presence
**Present** - Physically present in audience chamber scenes; leads formal gathering

## Physical Description
**General Martian Traits**: 10-12 feet tall, light olive-green skin (Sola), naked except ornaments. Specific facial features or ornament details not documented.

## Costume/Silhouette
**Martian Leader Standard**: Ornamented but otherwise nude; silhouette matches general Martian appearance described in chapter

## Continuity-Critical Traits
- Highest-ranking Martian leader present
- Requests sak demonstration from Carter
- Exchanges formal greeting with vice-chieftain
- Wins approbation from crowd after Carter's jump

## Render-Facing Noun Phrases
- Martian chieftain (unnamed)
- 10-12 foot tall humanoid
- olive-green skin tone
- ornamented but nude
- formal leader posture
- highest-ranking present figure

## Uncertainty Notes
**CRITICAL**: Requires manual description for reliable image generation. Current source provides only general Martian physical traits without specific facial features or distinguishing marks. **ADDITIONAL CONCERN**: Character is unnamed in source material and may already exist under another name or be too weakly identified for reliable visual continuity work.

## Source Material Limitations
Chapter text focuses on dialogue and action rather than detailed physical description of the chieftain. Visual continuity must be established through manual documentation of Martian-specific traits. **RECOMMENDATION**: Clarify whether this character should be documented as "Chieftain" only or if a personal name exists in source material not mentioned in this chapter.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
