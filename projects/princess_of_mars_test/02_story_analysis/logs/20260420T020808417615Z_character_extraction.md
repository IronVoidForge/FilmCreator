# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-20T02:08:08.417615+00:00
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

Chapter id: CH002

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

# Chapter Summary: THE ESCAPE OF THE DEAD

## Visual Continuity Facts
- **Location:** Interior of a cave (dim light, opening to daylight), Cliff ledge (trail between cave and cliff turn), Arizona night landscape (rocky gorge, cacti-studded flat, mountains).
- **Props & Objects:** Horse (standing with dragging rein initially, later wandering off), Revolvers (strapped to lifeless body), Carbine (in boot on saddle), Dead friend's body (lying within range of vision on ledge).
- **Character States:** Narrator (paralyzed/turned to stone -> standing naked vs clothed corpse), Indians (war-bonneted, paint-streaked faces, savage eyes).
- **Lighting:** Early morning sun through opening, Moonlight flooding cave, Starlight outside.
- **Key Visuals:** Vapor filling cave (tenuous), Red star on horizon (Mars), Naked narrator standing against cave wall vs clothed lifeless body on floor.

## Story Summary
The chapter begins with the narrator paralyzed in a cave, unable to move despite mental faculties intact. Approaching horses stop near the opening, revealing stealthy Indians creeping along the ledge. The warriors view the narrator with awe and fear but do not approach. A sound from behind the narrator causes the Indians to flee in terror, one falling off the cliff.

The narrator remains paralyzed until late afternoon when his horse wanders off. Silence persists until midnight, then a weird moan returns. With a superhuman effort of will, the narrator breaks free from paralysis. He discovers his original body lies lifeless and clothed on the cave floor while he stands naked. Unable to defend himself (revolvers/carbine inaccessible), he flees into the Arizona night.

Outside, he investigates the landscape under moonlight, reasoning that natural causes likely produced the sounds heard inside. He observes a large red star near the horizon—Mars—which fascinates him as a fighting man. Feeling drawn irresistibly to the god of war, he closes his eyes and is pulled through space into an instant of cold and darkness.
````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
task: character_extraction
version: 1

[[SECTION character_index_markdown]]
# Character Index - THE ESCAPE OF THE DEAD (CH002)

| Asset ID | Display Name | Chapter Role | Physical Presence | Description Status |
|----------|--------------|---------------|-------------------|-------------------|
| narrator_ch002 | Narrator | Protagonist, paralyzed in cave then breaks free | Present | Limited physical description |
| indians_ch002 | Indians | Antagonists, warriors on cliff ledge | Present | Group identification only |

**Notes:**
- Character descriptions are based on visual continuity facts from the chapter summary
- Some characters lack detailed physical descriptions for later image generation
- Clarification may be needed for group identifications
[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: narrator_ch002
canonical_character_id: narrator_ch002
aliases: 
is_fully_identified: true
manual_description_required: true
manual_description_reason: No detailed physical description beyond naked/clothed state; lacks height, build, facial features, hair, skin tone, or other render-facing details needed for dependable image generation
clarification_required: false
clarification_reason: 
clarification_question: 

[[SECTION markdown]]
# Narrator - CH002

**Display Name:** Narrator  
**Chapter Role:** Protagonist, paralyzed in cave then breaks free  
**Physical Presence:** Present (in cave initially, then standing naked vs clothed corpse)  

**Visual Description:**
- State transitions from paralyzed/turned to stone to standing naked against cave wall
- Original body found lifeless and clothed on cave floor
- No specific physical details beyond state of dress

**Continuity-Critical Traits:**
- Naked vs clothed distinction is important visual marker
- Paralyzed state affects movement capability throughout chapter

**Render-Facing Notes:**
- Lacks detailed physical description for image generation
- Focus on state transitions (paralyzed → standing) rather than specific features
- Consider emphasizing the contrast between living narrator and dead body
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: indians_ch002
canonical_character_id: indians_ch002
aliases: 
is_fully_identified: false
manual_description_required: true
manual_description_reason: Group identification only; no individual names or detailed physical descriptions beyond war-bonneted, paint-streaked faces, savage eyes
clarification_required: true
clarification_reason: Might exist under another name or too weakly identified for dependable later image generation
clarification_question: Are these specific named warriors or generic group representation?

[[SECTION markdown]]
# Indians - CH002

**Display Name:** Indians  
**Chapter Role:** Antagonists, warriors on cliff ledge  
**Physical Presence:** Present (creeping along ledge)  

**Visual Description:**
- War-bonneted appearance
- Paint-streaked faces
- Savage eyes
- Multiple warriors mentioned as group

**Continuity-Critical Traits:**
- Group identification rather than individual characters
- Stealthy movement along cliff ledge
- React with awe and fear to narrator's paralysis
- One warrior falls off cliff in terror

**Render-Facing Notes:**
- Limited physical description beyond cultural markers (war-bonnet, paint)
- Consider whether specific names or detailed features are needed
- Group representation may require clarification for image generation
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
