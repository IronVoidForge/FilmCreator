# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-20T01:22:27.827100+00:00
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

Chapter id: CH016

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

**Story Summary:**
- **Arrival in Thark:** After 30 days on Barsoom, John Carter and Dejah Thoris enter the ancient city of Thark. They are assigned new quarters near the central plaza.
- **Meeting Allies:** John locates Sola and Woola. Woola is reunited with John after a period of separation.
- **Threat Revealed:** Sarkoja has been seen; she plans to throw Dejah Thoris to wild calots (dogs) in the arena during yearly games.
- **Escape Plan Formulated:** John proposes an escape to Helium. Sola agrees. They decide on a route via a northern waterway to avoid detection.
- **Night Departure Attempt:** John prepares two thoats for travel. He meets Dejah Thoris and Sola at the city boundary.
- **Discovery:** The plan is discovered by warriors who intend to capture John Carter upon his return alone.
- **Capture Threat:** John hides in a courtyard with his animals, then climbs back to Dejah Thoris's room. He overhears warriors planning to chain him in vaults beneath the Jeddak's quarters if he returns without her.

**Visual Continuity Facts:**
- **Architecture:** Thark features grand public buildings and large chambers; John Carter occupies a building with an entire floor. Quarters face the plaza or are assigned by community divisions.
- **Map Drawing:** Dejah Thoris draws the first map of Barsoomian territory on the marble floor using a diamond, showing waterways (straight lines) and cities (circles).
- **Night Movement:** Stealthy travel through city streets, courtyards with moss-like vegetation, and second-story windows.
- **Animals:** Thoats and zitidars move restlessly in paddocks; John Carter navigates the herd at night without saddling them initially.
- **Lighting:** Scenes transition from daylight to sunset/moonlight (wild Barsoomian heavens) affecting visibility during crossings.
````

## Raw Response
````text

````
