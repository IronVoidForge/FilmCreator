# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-18T21:58:52.843770+00:00
- task: character_shared_prompts

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

Asset id: the_narrator

Task: write one reusable shared character-reference prompt draft for stable local generation.

Return exactly one Markdown packet using this outer envelope:
[[FILMCREATOR_PACKET]]
task: character_shared_prompts
version: 1

Repeat one FILMCREATOR_RECORD block for every extracted item of that type.

[[FILMCREATOR_RECORD]]
type: character_prompt
asset_id: <value>

[[SECTION purpose]]
...purpose content...
[[/SECTION]]

[[SECTION positive_prompt]]
...positive_prompt content...
[[/SECTION]]

[[SECTION negative_prompt]]
...negative_prompt content...
[[/SECTION]]

[[SECTION inputs_markdown]]
...inputs_markdown content...
[[/SECTION]]

[[SECTION continuity_notes_markdown]]
...continuity_notes_markdown content...
[[/SECTION]]

[[SECTION repair_notes_markdown]]
...repair_notes_markdown content...
[[/SECTION]]
[[/FILMCREATOR_RECORD]]
[[/FILMCREATOR_PACKET]]



Rules:

- purpose and inputs may use stable asset ids

- final positive and negative prompt bodies should avoid proper nouns and use descriptive noun phrases

- keep prompts concrete and visible

- prefer stable face, hair, body type, costume logic, silhouette, and recurring materials over scene-specific blocking



Character breakdown path: projects/princess_of_mars_test/02_story_analysis/character_breakdowns/the_narrator.md

# The Narrator

## Display Name & Role
**Name:** The Narrator  
**Role:** Protagonist / Observer

## Presence Status
**Status:** Referenced / Present (implied by narrative voice)  
**Note:** Character is the primary viewpoint of the chapter.

## Physical Description
**Supported Details:** None provided in this chapter.  
**Uncertainty Notes:** No physical traits (height, build, hair color, skin tone) are described in the text. Only actions ("climbs to window", "descends to street") and emotions ("depressed") are recorded.

## Costume & Silhouette
**Details:** Unknown.  
**Continuity Traits:** None specified in this chapter.

## Render-Facing Prompt Phrases
- "Male figure observing from upper floor window"
- "Depressed expression on face"
- "Standing on street level"
- "Uncertain physical build"

# Aliases

None



# Canonical Character ID

the_narrator



# Fully Identified

true

# Manual Description Input Required

No



# Manual Description Reason

None




Manual character description path: projects/princess_of_mars_test/01_source/character_descriptions/the_narrator_manual_description.md

(missing)
````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
task: character_shared_prompts
version: 1

[[FILMCREATOR_RECORD]]
type: character_prompt
asset_id: the_narrator

[[SECTION purpose]]
Reusable shared prompt for generating consistent character reference images of the Narrator protagonist. Captures core visual identity including gender presentation, emotional state, and general silhouette without scene-specific blocking. Designed for stable local generation workflows requiring face, hair, body type, costume logic, and recurring material consistency across multiple renders.

[[/SECTION]]

[[SECTION positive_prompt]]
Male figure with uncertain physical build observing from upper floor window. Depressed expression on face showing emotional weight. Standing posture at street level or elevated position. Neutral to muted clothing palette suggesting contemplative mood. Silhouette conveys observer role with minimal scene interaction. Face shows signs of melancholy without specific age markers. Hair style remains consistent across renders. Body type maintains stable proportions throughout image generation sequence.

[[/SECTION]]

[[SECTION negative_prompt]]
Proper nouns, brand names, or character-specific identifiers. Scene-specific blocking or action sequences. Bright or saturated color schemes contradicting contemplative mood. Exaggerated facial expressions beyond depressed emotion. Dynamic camera angles that break continuity. Specific age markers or detailed biographical information. Complex background elements that distract from character focus. Overly detailed costume patterns or textures.

[[/SECTION]]

[[SECTION inputs_markdown]]
Character breakdown reference: projects/princess_of_mars_test/02_story_analysis/character_breakdowns/the_narrator.md
Canonical Character ID: the_narrator
Display Name: The Narrator
Role: Protagonist / Observer
Render-Facing Prompt Phrases from source: Male figure observing from upper floor window, Depressed expression on face, Standing on street level, Uncertain physical build

[[/SECTION]]

[[SECTION continuity_notes_markdown]]
Maintain consistent male gender presentation across all character reference images. Keep depressed emotional state visible without over-exaggerating facial expressions. Preserve uncertain physical build description rather than specifying exact height or weight measurements. Ensure clothing remains in neutral to muted palette to support contemplative mood. Face consistency is critical for character recognition across multiple renders. Hair style should remain stable throughout image generation sequence. Body proportions must maintain consistent silhouette logic. Avoid scene-specific blocking that would break continuity between different character reference images generated from this prompt.

[[/SECTION]]

[[SECTION repair_notes_markdown]]
No manual description available at projects/princess_of_mars_test/01_source/character_descriptions/the_narrator_manual_description.md - proceeding with breakdown-based visual identity only. Physical traits remain intentionally vague per source material to preserve character mystery and observational role. Emotional state (depressed) is the primary defining characteristic beyond basic gender presentation.

[[/FILMCREATOR_RECORD]]
[[/FILMCREATOR_PACKET]]
````
