# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-20T00:28:07.613263+00:00
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

Chapter id: CH005

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

**Broad Story Summary**

*Scene 1: Observation and Sustenance*
- Sola leaves the chamber with the watch dog; the narrator examines the room's mural paintings (landscapes without animals) and food supplies (plant milk).
- Narrator sleeps through the night, waking cold but covered by fur.

*Scene 2: The Escape Attempt*
- Waking in daylight, the narrator observes five female occupants sleeping and the brute guarding the threshold.
- Deciding to test the brute's loyalty, the narrator exits the room; the brute follows with a shuffling gait.
- At the city edge, the brute attacks; the narrator jumps over him into open space.

*Scene 3: The Window Jump and Capture*
- The brute chases at high speed; the narrator leaps into a window thirty feet up on a building overlooking the valley.
- Upon reaching the sill, a hand grabs the narrator from behind inside the room.
- Thrown onto the back, the narrator sees a colossal ape-like creature (white, hairless, bristly head) standing over them.

**Visual Continuity Facts**

*Room Layout & Objects*
- Threshold: Guarded by the brute throughout the chapter.
- Floor Space: Contains food containers and fur coverings.
- Window Sill: Height of approximately thirty feet; overlooks the valley.
- Mural Paintings: Depict mountains, rivers, lakes, oceans, meadows, trees, flowers, winding roadways, sun-kissed gardens; no representation of living animals.

*Characters & Appearance*
- Sola: Female Martian, sympathetic, kind, unfailing ministrations.
- Watch Dog: Brute, short legs, fast runner, loyal protector, shuffling gait when walking.
- New Guardian: Colossal ape-like creature, white and hairless except for enormous shock of bristly hair on head.

*Environmental Details*
- Lighting: Martian nights are extremely cold; illuminated by two moons (nearer moon ~5,000 miles away, further ~14,000 miles).
- Atmosphere: Very thin; fails to diffuse starlight significantly.
- Temperature: Sudden changes between day and night; narrator feels cold upon waking.
````

## Raw Response
````text

````
