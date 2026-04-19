# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-19T05:17:09.699432+00:00
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

Asset id: human_woman_prisoner

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



Character breakdown path: projects/princess_of_mars_test/02_story_analysis/character_breakdowns/human_woman_prisoner.md

---
# Human Woman (Prisoner)

## Chapter Role
Captive and object of the narrator's hope/fear. Dragged from a disabled ship by female Martians into a building. Represents the "human" element in contrast to the Martians.

## Physical Presence
Visible. The figure is dragged roughly through a portal into a building after being removed from the unmanned ship.

## Physical Description
**Detailed.**
- **Build:** Slender girlish figure.
- **Face:** Oval face, large lustrous eyes.
- **Hair:** Coal black waving hair (loose coiffure).
- **Skin:** Light reddish copper skin.
- **Features:** Crimson cheeks, ruby lips.
- **Attire:** Destitute of clothes save for ornaments.

## Costume & Silhouette
**Ornamented.** Wearing only ornaments; otherwise naked. The specific style or nature of the ornaments is not detailed beyond "save for ornaments".

## Continuity-Critical Traits
- **Signal:** Previously sent a signal for succor (ignored by narrator).
- **Vulnerability:** Dragged roughly, indicating lack of agency in this scene.

## Render-Facing Prompt Notes
**Ready for Image Generation.** All key physical traits are explicitly described in the source text. Use these details for render-facing prompts: "Slender girlish figure, oval face, large lustrous eyes, coal black waving hair, light reddish copper skin, crimson cheeks, ruby lips, wearing ornaments only."
---

# Aliases

Prisoner, Small Figure



# Canonical Character ID

human_woman_prisoner



# Fully Identified

true

# Manual Description Input Required

No



# Manual Description Reason

None




Manual character description path: projects/princess_of_mars_test/01_source/character_descriptions/human_woman_prisoner_manual_description.md

(missing)
````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
task: character_shared_prompts
version: 1

[[FILMCREATOR_RECORD]]
type: character_prompt
asset_id: human_woman_prisoner

[[SECTION purpose]]
Generate consistent image renderings of the prisoner character with stable physical traits across scenes. Focus on facial structure, hair texture, skin tone, and ornamentation style while maintaining silhouette consistency for continuity tracking.
[[/SECTION]]

[[SECTION positive_prompt]]
slender girlish figure, oval face, large lustrous eyes, coal black waving hair, light reddish copper skin, crimson cheeks, ruby lips, wearing ornamental jewelry pieces, loose flowing hairstyle, delicate body build, minimal clothing coverage, decorative accessories only
[[/SECTION]]

[[SECTION negative_prompt]]
proper nouns, specific brand names, detailed scene blocking, complex background elements, multiple characters, text overlays, distorted facial features, inconsistent skin tone, mismatched hair color, heavy clothing, full garments, realistic lighting variations, environmental details
[[/SECTION]]

[[SECTION inputs_markdown]]
# Character Reference Inputs

## Stable Physical Traits
- Build: slender girlish figure
- Face: oval face with large lustrous eyes
- Hair: coal black waving hair in loose coiffure
- Skin: light reddish copper skin tone
- Features: crimson cheeks, ruby lips
- Attire: ornaments only (specific style uncertain)

## Continuity Requirements
- Maintain consistent facial structure across renders
- Preserve hair texture and color accuracy
- Keep skin tone uniform without environmental shifts
- Ensure ornamentation remains decorative rather than functional

## Render Notes
All key physical traits explicitly described in source text. Use these details for render-facing prompts: "Slender girlish figure, oval face, large lustrous eyes, coal black waving hair, light reddish copper skin, crimson cheeks, ruby lips, wearing ornaments only."
[[/SECTION]]

[[SECTION continuity_notes_markdown]]
# Continuity Tracking Notes

## Signal History
Previously sent signal for succor (ignored by narrator). This trait may inform character expression in future scenes but does not affect current visual rendering.

## Vulnerability Indicators
Dragged roughly through portal indicates lack of agency. Consider posture and positioning to reflect this state without compromising physical trait consistency.

## Material Consistency
Ornaments are specified as decorative only. Avoid functional interpretations (weapons, tools) that contradict the "save for ornaments" description.

## Scene-Specific Blocking
Avoid detailed scene blocking in character renders. Focus on isolated character shots with neutral backgrounds to maintain trait stability across different narrative contexts.
[[/SECTION]]

[[SECTION repair_notes_markdown]]
# Repair and Uncertainty Notes

## Ornamentation Ambiguity
Source text specifies "save for ornaments" but does not detail specific style or nature of ornaments. This creates uncertainty in rendering. Recommendation: Use generic ornamental jewelry pieces rather than specific cultural artifacts to avoid misinterpretation.

## Skin Tone Variation
Light reddish copper skin may appear differently under various lighting conditions. Maintain consistent base tone while allowing natural highlights that don't contradict the described color palette.

## Hair Texture Consistency
Coal black waving hair requires careful texture matching across renders. Avoid shifts between straight, curly, or wavy interpretations beyond the specified "waving" description.

## Facial Feature Proportion
Large lustrous eyes and oval face must maintain proportional consistency. Avoid exaggerated features that deviate from the described proportions while keeping character recognizable.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]
[[/FILMCREATOR_PACKET]]
````
