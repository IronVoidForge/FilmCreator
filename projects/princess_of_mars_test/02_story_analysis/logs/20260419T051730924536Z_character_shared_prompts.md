# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-19T05:17:30.924536+00:00
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

Asset id: narrator_human

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



Character breakdown path: projects/princess_of_mars_test/02_story_analysis/character_breakdowns/narrator_human.md

---
# Narrator (Human)

## Chapter Role
Observer and participant in the aftermath of the Martian victory. The narrator feels regret for failing to answer the human woman's signal due to ignorance of Martian customs.

## Physical Presence
Uncertain/Implied Present. The narrator is observing from a window and feeling internal emotions, but no physical description of their own body is provided in this chapter.

## Physical Description
**None Provided.** The text focuses entirely on the narrator's observations of others (Martians, Human Woman) and their internal emotional arc (Awe/Depression, Hope/Fear, Regret). No height, build, or facial features are mentioned for the narrator themselves.

## Costume & Silhouette
**Unknown.** No clothing or silhouette details are available in the source material.

## Continuity-Critical Traits
- **Internal Perspective:** The character serves as the lens for the reader's understanding of the scene.
- **Emotional State:** Defined by regret and hope regarding the human woman.

## Render-Facing Prompt Notes
**Uncertainty Note:** Manual description is required for reliable image generation. No physical traits exist in the source text to support dependable later rendering. Use placeholder or generic human features if forced to render, but flag as "Description Missing".
---

# Aliases

-



# Canonical Character ID

narrator_human



# Fully Identified

true

# Manual Description Input Required

No



# Manual Description Reason

None




Manual character description path: projects/princess_of_mars_test/01_source/character_descriptions/narrator_human_manual_description.md

(missing)
````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
task: character_shared_prompts
version: 1

[[FILMCREATOR_RECORD]]
type: character_prompt
asset_id: narrator_human

[[SECTION purpose]]
Observer and participant in the aftermath of the Martian victory. The character serves as the lens for the reader's understanding of the scene, defined by internal emotions of regret and hope regarding the human woman. No specific physical traits are provided in the source text.
[[/SECTION]]

[[SECTION positive_prompt]]
human figure, neutral expression, stable face, generic build, simple clothing, soft lighting, interior window view, observer perspective
[[/SECTION]]

[[SECTION negative_prompt]]
text, blurry, distorted, extra limbs, bright sunlight, outdoor scene, specific facial features, detailed costume, complex background
[[/SECTION]]

[[SECTION inputs_markdown]]
Character breakdown path: projects/princess_of_mars_test/02_story_analysis/character_breakdowns/narrator_human.md
Manual description path: projects/princess_of_mars_test/01_source/character_descriptions/narrator_human_manual_description.md (missing)
[[/SECTION]]

[[SECTION continuity_notes_markdown]]
**Uncertainty Note:** Manual description is required for reliable image generation. No physical traits exist in the source text to support dependable later rendering. Use placeholder or generic human features if forced to render, but flag as "Description Missing". The character serves primarily as an internal perspective lens rather than a fully realized physical entity in this chapter.
[[/SECTION]]

[[SECTION repair_notes_markdown]]
If manual description is unavailable, apply generic human silhouette with neutral expression. Flag the image generation as requiring future refinement once specific traits are defined. Avoid scene-specific blocking; focus on stable face and body type logic.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]
[[/FILMCREATOR_PACKET]]
````
