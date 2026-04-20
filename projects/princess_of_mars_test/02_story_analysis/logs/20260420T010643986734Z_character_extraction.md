# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-20T01:06:43.986734+00:00
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

Chapter id: CH011

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

*   **Scene 1: New Quarters & Sarkoja's Threat.** Carter arrives with Sola and Dejah Thoris at a new, ancient building near the audience chamber. He dismisses female guards to prevent Sarkoja from harming Dejah Thoris, threatening her demise if she continues her cruel attentions.
*   **Scene 2: Thark Hierarchy & Rank.** Sola explains Carter's promotion to eleventh Chieftain, noting his metal rank is close to Tars Tarkas (second only to Lorquas Ptomel). She clarifies that killing Lorquas Ptomel would make him first, but requires council approval or self-defense.
*   **Scene 3: Ancient Architecture & Frescoes.** They inspect the new quarters, which feature elaborate decorations of fair-haired, beardless Martians in robes. Dejah Thoris is captivated by the art of extinct people, while Sola ignores it. The room includes ancient metal beds and sleeping apartments.
*   **Scene 4: Origin Debate.** Dejah Thoris questions Carter's claim of being from Earth/Virginia, noting Barsoomians speak one tongue but he claims recent learning. She pleads for a denial, fearing the horror of a man returning from the "Barsoomian heaven or hell." Carter explains his Earth origin and Virginia customs.
*   **Scene 5: Belief & Martian Technology.** Dejah Thoris eventually believes him due to her emotional connection ("heart tells me that I believe"). She asks about Earth, explaining how Martians view other planets via screens/instruments. She notes the lack of ornaments on Carter proves his un-Barsoomian origin.
*   **Scene 6: History of Korad.** Dejah Thoris explains the history of the red race mixing with ancient fair-haired Martians and dark races due to drying seas. They discuss the city of Korad, built near a natural harbor, and the lost civilization of the ancient Martians.
*   **Scene 7: Conclusion.** After exploring the building and discussing customs, Carter receives a summons from Lorquas Ptomel to appear before him in the audience chamber.
````

## Raw Response
````text

````
