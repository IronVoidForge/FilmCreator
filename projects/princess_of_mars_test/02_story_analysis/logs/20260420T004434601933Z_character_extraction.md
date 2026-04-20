# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-20T00:44:34.601933+00:00
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

# Chapter II Summary: The Escape of the Dead

## Scene Overview
Protagonist regains movement after hours of paralysis in the cave, escapes into Arizona night, and begins journey through space to Mars. This chapter marks the transition from terrestrial danger to cosmic exploration.

## Visual Continuity Facts (Scene-Specific)
- Protagonist stands with back against cave wall facing unknown foe
- Moonlight floods cave interior revealing protagonist's body on floor
- Protagonist's lifeless body remains clothed while standing form is naked
- Revolvers strapped to lifeless body cannot be touched by protagonist
- Carbine in boot strapped to saddle, horse has wandered off
- Protagonist leaps through opening into starlight of clear Arizona night
- Crisp mountain air acts as immediate tonic outside cave
- Protagonist pauses on brink of ledge upbraiding unwarranted apprehension
- Moonlit landscape shows rocky gorge and cacti-studded flat below
- Large red star (Mars) appears close to distant horizon
- Protagonist feels spell of fascination with Mars, god of war
- Protagonist closes eyes and stretches arms toward Mars
- Sudden sensation of cold and utter darkness during space transition

## Broad Story Summary (Scene-Specific)
Protagonist regains movement after hours of paralysis in the cave. The mysterious moan from cave depths frightens Apache warriors who flee in terror, with one brave hurled from cliff. Protagonist escapes into Arizona night and investigates sounds with rational thinking, concluding they result from natural causes like breeze through cave conformation. Moonlit landscape inspires protagonist with its beauty. Protagonist notices large red star (Mars) near horizon that fascinates him as fighting man. Mars holds irresistible enchantment for protagonist who feels drawn to it across space void. Protagonist experiences sudden cold and darkness during transition to Mars.

## Scene Decomposition Support
- Opening: Protagonist regains movement after paralysis
- Middle: Escape into Arizona night, landscape observation
- Climax: Fascination with Mars, attraction across space
- Ending: Cold and darkness during space transition

- Paralysis recovery occurs late afternoon until midnight silence
- Horse wanders off leaving protagonist alone with mysterious companion
- Protagonist decides to investigate after rationalizing sounds
- Moonlit landscape provides visual inspiration for protagonist
- Mars star appears as focal point drawing protagonist's attention
- Space transition marks chapter ending and next chapter beginning

## Continuity Notes
- Protagonist's physical state changes from clothed lifeless body to naked standing form
- Apache warriors' fear of cave entity contrasts with protagonist's rational investigation
- Moonlight serves dual purpose: reveals cave interior, illuminates landscape below
- Star observation marks transition from terrestrial to cosmic journey
````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
task: character_extraction
version: 1

[[SECTION character_index_markdown]]
# Character Index - Chapter II

| Asset ID | Display Name | Canonical ID | Status |
|----------|--------------|--------------|--------|
| protagonist | Protagonist | protagonist | Referenced |
| apache_warriors | Apache Warriors | apache_warriors | Referenced |
| mysterious_companion | Mysterious Companion | mysterious_companion | Uncertain |

**Notes:**
- All characters lack sufficient physical description for dependable image generation
- Mysterious companion requires clarification due to vague identification
[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: protagonist
canonical_character_id: protagonist
aliases: 
is_fully_identified: true
manual_description_required: true
manual_description_reason: Chapter describes physical state transitions (clothed lifeless body to naked standing form) but lacks specific physical details like height, build, hair, skin tone, age indicators needed for dependable image generation
clarification_required: false
clarification_reason: 
clarification_question: 

[[SECTION markdown]]
# Protagonist - Chapter II

## Display Name & Role
**Protagonist** - Central figure experiencing paralysis recovery and cosmic journey

## Physical Presence Status
**Referenced** - Character is the primary subject throughout chapter, physically present in cave scene and during space transition

## Physical Description (Source-Supported)
- Lifeless body remains clothed while standing form is naked
- Protagonist stands with back against cave wall
- Moonlight reveals protagonist's body on floor
- Revolvers strapped to lifeless body cannot be touched by protagonist
- Carbine in boot strapped to saddle, horse has wandered off

## Costume & Silhouette (Source-Supported)
- Lifeless form: clothed with revolvers and carbine attached
- Standing form: naked during space transition
- No specific clothing details provided for either state

## Continuity-Critical Traits
- Physical state changes from clothed lifeless body to naked standing form
- Moonlight serves dual purpose: reveals cave interior, illuminates landscape below
- Protagonist's fascination with Mars marks transition from terrestrial to cosmic journey

## Render-Facing Prompt Noun Phrases
- "naked figure standing against cave wall"
- "moonlit protagonist body on floor"
- "figure stretching arms toward red star"
- "lifeless clothed form with revolvers strapped"

## Uncertainty Notes
**CRITICAL:** No physical description details provided (height, build, hair, skin tone, age indicators). Manual description required for dependable image generation. Chapter focuses on physical state transitions rather than character appearance.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: apache_warriors
canonical_character_id: apache_warriors
aliases: 
is_fully_identified: true
manual_description_required: true
manual_description_reason: Chapter mentions they flee in terror but provides no visual details like clothing, appearance, tribal markings, weapons, or physical build needed for dependable image generation
clarification_required: false
clarification_reason: 
clarification_question: 

[[SECTION markdown]]
# Apache Warriors - Chapter II

## Display Name & Role
**Apache Warriors** - Native American warriors reacting to mysterious cave entity

## Physical Presence Status
**Referenced** - Warriors mentioned as fleeing in terror from mysterious moan, one brave hurled from cliff

## Physical Description (Source-Supported)
- No physical descriptions provided in chapter text
- Warriors flee in terror from cave depths' mysterious sound
- One warrior bravely hurled from cliff edge

## Costume & Silhouette (Source-Supported)
- No clothing or appearance details provided
- No weapons, tribal markings, or traditional attire described

## Continuity-Critical Traits
- Fear of cave entity contrasts with protagonist's rational investigation
- Warriors' reaction establishes danger level of mysterious companion
- One warrior's death from cliff fall marks escalation

## Render-Facing Prompt Noun Phrases
- "Apache warriors fleeing in terror"
- "native warriors reacting to mysterious sound"
- "warrior hurled from cliff edge"

## Uncertainty Notes
**CRITICAL:** No physical description details provided (clothing, appearance, tribal markings, weapons, build). Manual description required for dependable image generation. Chapter focuses on their reaction rather than visual characterization.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: mysterious_companion
canonical_character_id: mysterious_companion
aliases: 
is_fully_identified: false
manual_description_required: true
manual_description_reason: Chapter references this entity but provides no visual details like appearance, form, size, or physical characteristics needed for dependable image generation
clarification_required: true
clarification_reason: Entity is referred to vaguely as "mysterious companion" without clear identification; might be the cave entity mentioned in earlier chapters or separate being
clarification_question: Is this mysterious companion a separate entity from the protagonist, or is it the cave entity mentioned in earlier chapters?

[[SECTION markdown]]
# Mysterious Companion - Chapter II

## Display Name & Role
**Mysterious Companion** - Entity causing fascination and drawing protagonist toward Mars

## Physical Presence Status
**Uncertain** - Referenced vaguely throughout chapter without clear physical identification

## Physical Description (Source-Supported)
- No physical descriptions provided in chapter text
- Entity causes mysterious moan from cave depths that frightens Apache warriors
- Protagonist feels spell of fascination with entity's presence
- Entity draws protagonist across space void toward Mars

## Costume & Silhouette (Source-Supported)
- No clothing, form, or appearance details provided
- No visual characteristics described for image generation

## Continuity-Critical Traits
- Mysterious moan from cave depths frightens Apache warriors who flee in terror
- Protagonist's fascination marks transition from terrestrial danger to cosmic exploration
- Entity holds irresistible enchantment for protagonist who feels drawn to it across space void
- Space transition marks chapter ending and next chapter beginning

## Render-Facing Prompt Noun Phrases
- "mysterious entity causing cave moan"
- "entity drawing protagonist toward Mars"
- "fascinating presence across space void"

## Uncertainty Notes
**CRITICAL:** No physical description details provided (form, size, appearance, characteristics). Manual description required for dependable image generation. **CLARIFICATION REQUIRED:** Entity identification is too vague; might already exist under another name or be too weakly identified. Chapter does not provide stable visual identification for this character.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
