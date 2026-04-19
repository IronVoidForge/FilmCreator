# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-19T04:11:21.783215+00:00
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

Chapter id: CH008

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

# Chapter Summary: A Fair Captive from the Sky

## Sequence of Events
1.  **Return Order:** Immediately after an incubator ceremony, orders are given for a hasty return to the city. The Martians melt into buildings within three minutes.
2.  **Airship Arrival:** From the window, the narrator observes twenty gray airships sailing toward the valley. Each carries banners and glowing devices.
3.  **Battle Initiation:** Green warriors fire a volley from building windows. The lead vessel returns fire, swinging broadside to complete a circle.
4.  **Martian Victory:** Martians target specific points (sighting apparatus, gunners, officers). Twenty minutes later, the fleet retreats with several craft limping.
5.  **Disabled Ship Recovery:** One ship is unmanned and drifting. Warriors rush to intercept it before it hits buildings south of their position. They board using spears and grappling hooks.
6.  **Looting & Burning:** Martians search the vessel, removing arms, silks, jewels, and food (including water). Afterward, they empty carboys over dead sailors and set the ship ablaze with a missile. The burning ship drifts southeast as a funeral pyre.
7.  **Prisoner Reveal:** Warriors drag a small figure from the ship. The narrator sees a human woman being dragged into a building by female Martians.

## Visual Details for Scene Decomposition
*   **Ship Appearance:** Gray, low profile, long shape, banners on stem/stern, glowing devices on prow.
*   **Martian Fire:** Terrific volley from windows; bullets dropping at explosion points; banners dissolving in flame.
*   **Prisoner Appearance:** Slender girlish figure, oval face, large lustrous eyes, coal black waving hair (loose coiffure), light reddish copper skin, crimson cheeks, ruby lips, destitute of clothes save for ornaments.
*   **Movement:** Ships swing majestically then erratically; warriors melt into mist; prisoner dragged roughly through portal.

## Narrative Beats & Emotional Arc
*   **Awe/Depression:** The narrator feels the defeat marks a kindred people's annihilation rather than a simple victory.
*   **Hope/Fear:** Upon seeing the human woman, the narrator experiences mingled hope and fear.
*   **Regret:** The narrator realizes he failed to answer her signal for succor due to ignorance of Martian customs.
````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
task: character_extraction
version: 1

[[SECTION character_index_markdown]]
# Character Index: Chapter CH008

| Asset ID | Canonical Character ID | Aliases | Fully Identified | Manual Description Required |
| :--- | :--- | :--- | :--- | :--- |
| `narrator_human` | Narrator | - | Yes | No (Role clear) |
| `martian_warrior` | Martian Warrior | Green Warriors, Female Martians | Yes | Yes (Anatomy unclear) |
| `human_woman_prisoner` | Human Woman | Prisoner, Small Figure | Yes | No (Description detailed) |

*Note: "Fully Identified" refers to the character's role and presence being stable. "Manual Description Required" indicates if physical traits are missing for reliable image generation.*
[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: narrator_human
canonical_character_id: Narrator
aliases: -
is_fully_identified: true
manual_description_required: true
manual_description_reason: No physical traits provided in chapter summary; only emotional state and internal perspective are described.
clarification_required: false
clarification_reason: -
clarification_question: -

[[SECTION markdown]]
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
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: martian_warrior
canonical_character_id: Martian Warrior
aliases: Green Warriors, Female Martians
is_fully_identified: true
manual_description_required: true
manual_description_reason: Chapter describes actions (melting into buildings, firing volleys) and color ("Green"), but lacks detailed physical anatomy (height, specific body shape, skin texture) for reliable image generation.
clarification_required: false
clarification_reason: -
clarification_question: -

[[SECTION markdown]]
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
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: human_woman_prisoner
canonical_character_id: Human Woman
aliases: Prisoner, Small Figure
is_fully_identified: true
manual_description_required: false
manual_description_reason: Detailed physical description provided in text ("Slender girlish figure", "oval face", "coal black waving hair", "light reddish copper skin", etc.).
clarification_required: false
clarification_reason: -
clarification_question: -

[[SECTION markdown]]
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
[[/SECTION]]
[[/FILMCREATOR_RECORD]]
[[/FILMCREATOR_PACKET]]
````
