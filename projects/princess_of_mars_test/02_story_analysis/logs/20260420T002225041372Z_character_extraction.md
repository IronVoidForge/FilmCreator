# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-20T00:22:25.041372+00:00
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

Chapter id: CH004

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

**Story Flow:**
1. **Arrival:** Ground rises to mountains; party enters city via ruined road. Buildings appear ancient but not decayed.
2. **Observation:** Martians camped in plaza (900+). Appearance noted: naked except ornaments, women have larger tusks, children light colored. Life cycle details provided (death by violence vs sickness).
3. **Introduction:** Tars Tarkas (vice-chieftain) leads party to Chieftain's edifice. Ceremony involves name exchange between Martians.
4. **Conflict:** Martians surround narrator, demand performance ("sak"). Narrator struggles with walking/jumping.
5. **Fight:** Narrator punches a laughing Martian who bullied him. Crowd approves (applause).
6. **Performance:** Narrator performs "sakk" jump successfully.
7. **Resolution:** Narrator demands food/water. Sola (8ft female) takes him to quarters.
8. **Ending:** Ten-legged creature waddles into the room.

**Visual Continuity:**
- **Martians:** Naked except ornaments; women have larger tusks; adults 10-12ft tall.
- **Furniture:** Human-sized desks/chairs (too small for Martians).
- **Architecture:** White marble, gold inlay, broad steps.
- **Creature:** Ten short legs, frog-like head, three rows of sharp tusks.
````

## Raw Response
````text

````
