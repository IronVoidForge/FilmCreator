# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-20T01:16:38.665573+00:00
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

Chapter id: CH014

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

*Scene 1: Introspection & Departure*
- **Visuals:** Carter sits cross-legged in his chamber (gold/marble mosaics), then moves to the plaza/chariots. Dejah Thoris is in a departing chariot, heavily chained by one ankle to the vehicle side.
- **Story:** Carter reflects on his love for Dejah Thoris and her rejection of him due to his perceived weakness or the situation. He observes her silence and refusal to acknowledge him.

*Scene 2: The Chains & Tars Tarkas*
- **Visuals:** Carter examines the manacles (massive spring lock). Tars Tarkas intervenes, agreeing to hold the key himself rather than Sarkoja.
- **Story:** Sarkoja's cruelty is highlighted by the chains. Tars Tarkas ensures security while allowing for potential escape later.

*Scene 3: Camp Life & Earth Memories*
- **Visuals:** Carter sits cross-legged on silks in camp, moonlit skies.
- **Story:** Carter meditates on love and mortality. He recalls his family in Virginia (Carters), feeling homesick despite being a wanderer.

*Scene 4: Warhoon Incubator Incident*
- **Visuals:** An incubator with small eggs found to the right of the march. Tars Tarkas investigates with warriors. Eggs are demolished.
- **Story:** Discovery of green men's (Warhoons) incubator. Carter asks about egg size differences; Tars Tarkas explains growth period.

*Scene 5: Duel with Zad*
- **Visuals:** Zad strikes Carter's animal with a long-sword. Carter draws his own sword. Community surrounds them, leaving a clear space (100 feet diameter). Long, straight, needle-like swords flash.
- **Story:** Fight initiated by Zar striking the animal. Carter chooses to fight with same weapon. Fight is long and delayed march.

*Scene 6: The Trap & Sacrifice*
- **Visuals:** Blinding flash of light strikes Carter's eyes (mirror). Dejah Thoris throws something from hand (tiny mirror) which spins to ground. Sarkoja aims dagger at Dejah Thoris; Sola sprang between them, knife descending on her shielding breast.
- **Story:** Sarkoja blinds Carter with a mirror while trying to kill him. Dejah Thoris throws the mirror. Sola sacrifices herself to protect Dejah Thoris from Sarkoja's counter-attack during the fight.

*Scene 7: Wounding & Collapse*
- **Visuals:** Carter feels sharp point of sword at breast, throws himself on enemy. Steel tears into chest. Head whirled, knees giving beneath.
- **Story:** Carter is wounded in the duel, collapsing as darkness takes him.
````

## Raw Response
````text

````
