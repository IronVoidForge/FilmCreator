# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-19T05:17:21.284680+00:00
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

Asset id: martian_warrior

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



Character breakdown path: projects/princess_of_mars_test/02_story_analysis/character_breakdowns/martian_warrior.md

---
# Martian Warrior

## Chapter Role
Antagonist and victor in the battle. They fire volleys from windows, target specific points on enemy ships, and drag the human woman prisoner into a building. Female Martians are specifically mentioned during the prisoner reveal.

## Physical Presence
Visible. Warriors are seen firing from windows, melting into mist, and dragging the prisoner through a portal.

## Physical Description
**Partial.** The text identifies them as "Green warriors" and notes they can "melt into buildings within three minutes." However, no detailed physical breakdown (e.g., height, limb structure, specific facial features) is provided in this chapter summary.

## Costume & Silhouette
**Unknown.** No specific clothing or armor details are mentioned beyond their ability to melt.

## Continuity-Critical Traits
- **Melting Ability:** A key trait distinguishing them from humans (melt into buildings/mist).
- **Weaponry:** Fire volleys, use spears and grappling hooks for boarding disabled ships.
- **Gender:** Both general "Martians" and specific "Female Martians" are referenced.

## Render-Facing Prompt Notes
**Uncertainty Note:** Manual description is required for reliable image generation. While color ("Green") and action ("melting") are known, full anatomical details are missing from the source text to support dependable later rendering.
---

# Aliases

Green Warriors, Female Martians



# Canonical Character ID

martian_warrior



# Fully Identified

true

# Manual Description Input Required

No



# Manual Description Reason

None




Manual character description path: projects/princess_of_mars_test/01_source/character_descriptions/martian_warrior_manual_description.md

(missing)
````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
task: character_shared_prompts
version: 1

[[FILMCREATOR_RECORD]]
type: character_prompt
asset_id: martian_warrior

[[SECTION purpose]]
Generate consistent Martian Warrior images for story rendering. Focus on stable physical traits including green coloration, melting ability, female form, and weaponry (spears, grappling hooks). Use this prompt across multiple shots to maintain visual continuity of the antagonist character throughout the battle sequences.
[[/SECTION]]

[[SECTION positive_prompt]]
Green humanoid warrior with smooth skin texture, melting into mist or building structure, female facial features, slender build, holding spear weapon, wearing minimal armor, glowing green energy around body, floating in air, dramatic lighting, cinematic composition, detailed anatomy, sharp silhouette against background
[[/SECTION]]

[[SECTION negative_prompt]]
human face, human skin texture, standing still, walking, running, casual clothing, heavy armor, weapons not held, bright daylight, indoor setting, multiple characters, text, watermark, blurry, low resolution, distorted limbs, extra fingers, extra eyes, asymmetrical features, melting into solid objects only, green color on wrong body parts
[[/SECTION]]

[[SECTION inputs_markdown]]
```markdown
- Asset ID: martian_warrior
- Project: princess_of_mars_test
- Chapter Role: Antagonist and victor in battle
- Continuity Trait: Melting ability (melt into buildings/mist)
- Gender: Female Martians specifically referenced
- Weaponry: Spears, grappling hooks for boarding ships
```
[[/SECTION]]

[[SECTION continuity_notes_markdown]]
- Green coloration is primary visual identifier
- Melting ability distinguishes from human characters
- Female form confirmed during prisoner reveal sequence
- Minimal armor or clothing beyond functional gear
- Weapons include spears and grappling hooks for ship boarding
- Can transition between solid form and mist/building integration
- No detailed height, limb structure, or facial features in source text
[[/SECTION]]

[[SECTION repair_notes_markdown]]
Source text provides limited physical breakdown details. Manual description path is missing from project files. Color (green) and action (melting) are known but full anatomical specifications are absent from chapter summaries. Prompts must rely on descriptive noun phrases rather than proper nouns to maintain stability across generations. Face, hair, body type, costume logic, silhouette, and recurring materials should be prioritized over scene-specific blocking details.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]
[[/FILMCREATOR_PACKET]]
````
