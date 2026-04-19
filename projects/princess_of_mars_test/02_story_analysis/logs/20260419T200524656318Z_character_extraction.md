# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-19T20:05:24.656318+00:00
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

Chapter id: CH006

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

# Chapter Summary: A FIGHT THAT WON FRIENDS

## Broad Story Summary
The narrator is pinned to the ground by a Bull Ape (Martian warrior) who intends to execute him with a stone cudgel. The Watch-thing attacks the Bull Ape, leading to a brutal struggle where the narrator must intervene to save his companion from choking death. After killing the first Bull Ape, an enraged second one arrives. The narrator fights and kills this second creature using both fists and the cudgel. Tars Tarkas, Sola, and warriors arrive to witness the battle. They applaud the narrator's physical strength but show indifference toward the Watch-thing, attempting to shoot it. The narrator defends the Watch-thing from a pistol shot, preventing its death. He leaves with Sola and the Watch-thing, while Tars Tarkas follows, having witnessed the narrator's valor.

## Visual Continuity Facts
*   **Weapon States:**
    *   Stone cudgel: Initially held by Bull Ape, falls to floor during struggle, used by narrator for both attacks, thrown at second Bull Ape, then seized again for finishing blow.
    *   Pistol: Drawn by warrior, discharged at Watch-thing, bullet explodes in window casing.
*   **Character Positions:**
    *   Narrator: Starts pinned to ground, moves to wall during fight, stands near window, kneels beside Watch-thing after defense.
    *   Bull Ape (First): Holds narrator with foot, swings cudgel, engaged in death struggle with Watch-thing, crushed skull by narrator.
    *   Bull Ape (Second): Enters doorway roaring, lunges at narrator, struck below knees, reeled and fell upon floor, finished off by narrator.
    *   Watch-thing: Attacks Bull Ape from doorway, sinks fangs into adversary's breast, choked out life, bulging eyes, blood from nostrils, defended by narrator from pistol shot.
*   **Group Composition:**
    *   Tars Tarkas, Sola, and three or four warriors standing in doorway upon arrival.
    *   Martians generally applauding narrator, except for warrior attempting to shoot Watch-thing.
*   **Environmental Details:**
    *   Doorway: Entry point for Bull Apes and allies.
    *   Window: Open during fight, allows Bull Ape (first) to leap through, bullet explodes in wooden casing.
    *   Floor: Where creatures roll during struggle, where narrator stands near window, where Watch-thing lies gasping.

## Scene Decomposition Notes
*   **Opening:** Narrator pinned, Bull Ape threatening with cudgel.
*   **Conflict 1:** Watch-thing intervenes; brutal death struggle ensues; narrator saves Watch-thing from choking.
*   **Resolution 1:** Narrator kills first Bull Ape with cudgel.
*   **Conflict 2:** Second Bull Ape arrives enraged; narrator fights using fists and cudgel; second Bull Ape defeated.
*   **Arrival:** Tars Tarkas, Sola, warriors enter chamber.
*   **Climax:** Martians show indifference to Watch-thing; warrior attempts to shoot it; narrator defends Watch-thing from pistol shot.
*   **Ending:** Narrator leaves with Watch-thing and Sola; Tars Tarkas follows; narrator reflects on loyalty of Watch-thing vs. Martians.
````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
task: character_extraction
version: 1

[[SECTION character_index_markdown]]
# Character Index - Chapter: A FIGHT THAT WON FRIENDS

## Characters Extracted

1.  **Narrator** (Protagonist)
2.  **Bull Ape (First)** (Antagonist)
3.  **Bull Ape (Second)** (Antagonist)
4.  **Watch-thing** (Companion)
5.  **Tars Tarkas** (Leader)
6.  **Sola** (Leader)
7.  **Warriors** (Supporting Group)

*Note: All characters listed above are extracted from the provided chapter summary and visual continuity facts.*
[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: narrator
canonical_character_id: narrator
aliases: 
is_fully_identified: true
manual_description_required: true
manual_description_reason: The source text describes actions and positions (pinned to ground, fighting Bull Apes) but lacks specific physical traits (height, build, hair, skin tone) required for dependable image generation.
clarification_required: false
clarification_reason: 
clarification_question: 

[[SECTION markdown]]
# Narrator - Chapter Role: Protagonist

## Status
Physically present and referenced throughout the chapter.

## Physical Description
*   **Source:** The text identifies the character as "The narrator" but does not provide specific visual details (e.g., height, build, hair color).
*   **Action:** Pinned to ground initially, moves to wall during fight, stands near window, kneels beside Watch-thing.

## Continuity Notes
*   **Weapon Interaction:** Uses stone cudgel for attacks on Bull Apes. Defends Watch-thing from pistol shot.
*   **Uncertainty:** Specific physical appearance is unknown. Image generation requires manual description input to define build and features consistent with the "Martian" setting or human protagonist depending on interpretation.

## Render Prompt Notes
*   *Subject:* Male figure (assumed based on context of "narrator" in this genre, but needs confirmation).
*   *Action:* Fighting stance, defensive posture.
*   *Missing:* Height, build, hair, skin tone. Needs manual override.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: bull_ape_first
canonical_character_id: bull_ape_first
aliases: Bull Ape (First)
is_fully_identified: true
manual_description_required: true
manual_description_reason: The source text describes the creature as a "Bull Ape" and "Martian warrior" but lacks specific physical traits (size, fur color, muscle mass) required for dependable image generation.
clarification_required: false
clarification_reason: 
clarification_question: 

[[SECTION markdown]]
# Bull Ape (First) - Chapter Role: Antagonist #1

## Status
Physically present and referenced in the opening conflict.

## Physical Description
*   **Source:** Identified as a "Bull Ape" and "Martian warrior". Holds stone cudgel initially.
*   **Action:** Pins narrator with foot, swings cudgel, engaged in death struggle with Watch-thing, crushed skull by narrator.
*   **Uncertainty:** Specific physical appearance (size, fur color) is unknown.

## Continuity Notes
*   **Weapon Interaction:** Holds stone cudgel, falls to floor during struggle, used by narrator for attacks.
*   **Outcome:** Killed by narrator using cudgel.

## Render Prompt Notes
*   *Subject:* Large primate-like creature (Martian).
*   *Action:* Aggressive stance, holding cudgel.
*   *Missing:* Fur color, specific build details. Needs manual override.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: bull_ape_second
canonical_character_id: bull_ape_second
aliases: Bull Ape (Second)
is_fully_identified: true
manual_description_required: true
manual_description_reason: The source text describes the creature as a "Bull Ape" and "Martian warrior" but lacks specific physical traits (size, fur color, muscle mass) required for dependable image generation.
clarification_required: false
clarification_reason: 
clarification_question: 

[[SECTION markdown]]
# Bull Ape (Second) - Chapter Role: Antagonist #2

## Status
Physically present and referenced in the second conflict.

## Physical Description
*   **Source:** Identified as a "Bull Ape" and "Martian warrior". Enters doorway roaring.
*   **Action:** Lunges at narrator, struck below knees, reeled and fell upon floor, finished off by narrator.
*   **Uncertainty:** Specific physical appearance (size, fur color) is unknown.

## Continuity Notes
*   **Weapon Interaction:** No weapon mentioned for this specific Bull Ape; defeated using fists and cudgel.
*   **Outcome:** Killed by narrator using fists and cudgel.

## Render Prompt Notes
*   *Subject:* Large primate-like creature (Martian).
*   *Action:* Roaring, lunging stance.
*   *Missing:* Fur color, specific build details. Needs manual override.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: watch_thing
canonical_character_id: watch_thing
aliases: Watch-thing
is_fully_identified: true
manual_description_required: true
manual_description_reason: The source text describes the creature as a "Watch-thing" but lacks specific physical traits (species, build, color) required for dependable image generation.
clarification_required: false
clarification_reason: 
clarification_question: 

[[SECTION markdown]]
# Watch-thing - Chapter Role: Companion

## Status
Physically present and referenced throughout the chapter.

## Physical Description
*   **Source:** Identified as a "Watch-thing". Attacks Bull Ape from doorway, sinks fangs into adversary's breast.
*   **Action:** Choked out life of Bull Ape (First), bulging eyes, blood from nostrils, defended by narrator from pistol shot.
*   **Uncertainty:** Specific physical appearance (species type, build) is unknown.

## Continuity Notes
*   **Weapon Interaction:** Uses fangs to attack Bull Ape. Defended by narrator from pistol shot.
*   **Outcome:** Survives the battle, leaves with Narrator and Sola.

## Render Prompt Notes
*   *Subject:* Alien creature (Watch-thing).
*   *Action:* Defensive posture after saving Watch-thing.
*   *Missing:* Species type, build details. Needs manual override.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: tars_tarkas
canonical_character_id: tars_tarkas
aliases: Tars Tarkas
is_fully_identified: true
manual_description_required: true
manual_description_reason: The source text names the character but lacks specific physical traits (height, build, hair) required for dependable image generation.
clarification_required: false
clarification_reason: 
clarification_question: 

[[SECTION markdown]]
# Tars Tarkas - Chapter Role: Leader/Observer

## Status
Physically present and referenced upon arrival.

## Physical Description
*   **Source:** Identified as "Tars Tarkas". Arrives with Sola and warriors.
*   **Action:** Witnesses battle, applauds narrator's physical strength, shows indifference toward Watch-thing, follows Narrator after witnessing valor.
*   **Uncertainty:** Specific physical appearance is unknown.

## Continuity Notes
*   **Group Composition:** Standing in doorway upon arrival with Sola and warriors.
*   **Outcome:** Follows Narrator after battle; reflects on loyalty of Watch-thing vs. Martians.

## Render Prompt Notes
*   *Subject:* Martian Leader figure.
*   *Action:* Observing stance, applauding gesture.
*   *Missing:* Height, build, hair. Needs manual override.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: sola
canonical_character_id: sola
aliases: Sola
is_fully_identified: true
manual_description_required: true
manual_description_reason: The source text names the character but lacks specific physical traits (height, build, hair) required for dependable image generation.
clarification_required: false
clarification_reason: 
clarification_question: 

[[SECTION markdown]]
# Sola - Chapter Role: Leader/Companion

## Status
Physically present and referenced upon arrival.

## Physical Description
*   **Source:** Identified as "Sola". Arrives with Tars Tarkas and warriors.
*   **Action:** Leaves with Watch-thing after battle.
*   **Uncertainty:** Specific physical appearance is unknown.

## Continuity Notes
*   **Group Composition:** Standing in doorway upon arrival with Tars Tarkas and warriors.
*   **Outcome:** Leaves chamber with Watch-thing; follows Narrator's path.

## Render Prompt Notes
*   *Subject:* Martian Leader figure.
*   *Action:* Walking/Leaving stance.
*   *Missing:* Height, build, hair. Needs manual override.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: warriors
canonical_character_id: martian_warriors
aliases: Warriors, Martians
is_fully_identified: false
manual_description_required: true
manual_description_reason: The source text refers to them as a group ("three or four warriors") without specific physical traits for individuals required for dependable image generation.
clarification_required: true
clarification_reason: The group is generic; individual visual identity needs clarification to ensure consistency with the Martian aesthetic established in the film.
clarification_question: Are these warriors distinct from Tars Tarkas and Sola, or are they additional generic Martians?

[[SECTION markdown]]
# Warriors - Chapter Role: Supporting Group

## Status
Physically present and referenced upon arrival.

## Physical Description
*   **Source:** Identified as "three or four warriors". Standing in doorway upon arrival.
*   **Action:** Attempt to shoot Watch-thing; narrator defends Watch-thing from pistol shot.
*   **Uncertainty:** Specific physical appearance for individuals is unknown. Group composition is generic.

## Continuity Notes
*   **Group Composition:** Standing in doorway with Tars Tarkas and Sola.
*   **Outcome:** Attempt to shoot Watch-thing; narrator intervenes.
*   **Clarification Needed:** Individual visual identity needs clarification to ensure consistency with the Martian aesthetic established in the film.

## Render Prompt Notes
*   *Subject:* Generic Martian Warrior figures.
*   *Action:* Aggressive stance (drawing pistol).
*   *Missing:* Height, build, hair for individuals. Needs manual override and clarification on group uniformity.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
