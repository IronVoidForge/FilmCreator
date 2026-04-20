# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-20T01:23:00.021646+00:00
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


[[FILMCREATOR_PACKET]]
task: character_extraction
version: 1

[[SECTION character_index_markdown]]
# Character Index - Chapter 016

| Character | Asset ID | Status | Description |
|-----------|----------|--------|-------------|
| John Carter | john_carter | Fully Identified | Protagonist, enters Thark with Dejah Thoris |
| Dejah Thoris | dejah_thoris | Fully Identified | Enters Thark, plans escape to Helium |
| Sola | sola | Fully Identified | Located in Thark, agrees to escape plan |
| Woola | woola | Fully Identified | John's animal companion, reunited after separation |
| Sarkoja | sarkoja | Referenced | Seen planning arena threat against Dejah |
| Jeddak | jeddak | Referenced | Quarters mentioned beneath his vaults |

*Note: Characters extracted from chapter summary. Physical descriptions limited to source material.*
[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: john_carter
canonical_character_id: john_carter
aliases: 
is_fully_identified: true
manual_description_required: true
manual_description_reason: Chapter summary references John Carter's presence and actions but provides no physical description (appearance, height, build, facial features) for dependable image generation. Source material only describes his movements and decisions.
clarification_required: false
clarification_reason: 
clarification_question: 
[[SECTION markdown]]
# John Carter - Character Profile

**Display Name:** John Carter  
**Chapter Role:** Protagonist / Leader of Escape Plan  
**Physical Presence:** Referenced throughout chapter (enters Thark, meets allies, prepares departure)  
**Physical Description:** Not provided in source material. Summary describes his actions and decisions but lacks visual details for rendering.  
**Costume/Silhouette:** Unknown from chapter summary. Would require additional source material for accurate depiction.  
**Continuity Traits:** Central figure in escape plot; navigates Thark with animals (zitidars/thoats); climbs to Dejah Thoris's room; hides in courtyard.  

**Render-Facing Notes:** 
- Character is physically present and referenced multiple times
- No stable visual identification available from chapter summary alone
- Would need canonical Barsoom source material for accurate physical description
- Continuity-critical: Leader of escape plan, moves through city with animals

**Uncertainty Statement:** 
Physical appearance details are missing from this chapter's source material. For dependable image generation, additional canonical descriptions would be required beyond what is provided in the chapter summary.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: dejah_thoris
canonical_character_id: dejah_thoris
aliases: 
is_fully_identified: true
manual_description_required: true
manual_description_reason: Chapter summary references Dejah Thoris's presence and actions but provides no physical description (appearance, height, build, facial features) for dependable image generation. Source material only describes her movements and decisions.
clarification_required: false
clarification_reason: 
clarification_question: 
[[SECTION markdown]]
# Dejah Thoris - Character Profile

**Display Name:** Dejah Thoris  
**Chapter Role:** Protagonist / Escape Plan Co-organizer  
**Physical Presence:** Referenced throughout chapter (enters Thark, meets allies, plans departure)  
**Physical Description:** Not provided in source material. Summary describes her actions and decisions but lacks visual details for rendering.  
**Costume/Silhouette:** Unknown from chapter summary. Would require additional source material for accurate depiction.  
**Continuity Traits:** Central figure in escape plot; draws map on marble floor; meets at city boundary; climbs to room; overhears warrior plans.  

**Render-Facing Notes:** 
- Character is physically present and referenced multiple times
- No stable visual identification available from chapter summary alone
- Would need canonical Barsoom source material for accurate physical description
- Continuity-critical: Draws map, moves through city with animals

**Uncertainty Statement:** 
Physical appearance details are missing from this chapter's source material. For dependable image generation, additional canonical descriptions would be required beyond what is provided in the chapter summary.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: sola
canonical_character_id: sola
aliases: 
is_fully_identified: true
manual_description_required: true
manual_description_reason: Chapter summary references Sola's presence and actions but provides no physical description (appearance, height, build, facial features) for dependable image generation. Source material only describes her movements and decisions.
clarification_required: false
clarification_reason: 
clarification_question: 
[[SECTION markdown]]
# Sola - Character Profile

**Display Name:** Sola  
**Chapter Role:** Ally / Escape Plan Participant  
**Physical Presence:** Referenced throughout chapter (located in Thark, agrees to escape plan)  
**Physical Description:** Not provided in source material. Summary describes her actions and decisions but lacks visual details for rendering.  
**Costume/Silhouette:** Unknown from chapter summary. Would require additional source material for accurate depiction.  
**Continuity Traits:** Located with John Carter; agrees to escape via northern waterway; meets at city boundary.  

**Render-Facing Notes:** 
- Character is physically present and referenced multiple times
- No stable visual identification available from chapter summary alone
- Would need canonical Barsoom source material for accurate physical description
- Continuity-critical: Participant in escape plan, moves through city

**Uncertainty Statement:** 
Physical appearance details are missing from this chapter's source material. For dependable image generation, additional canonical descriptions would be required beyond what is provided in the chapter summary.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: woola
canonical_character_id: woola
aliases: 
is_fully_identified: true
manual_description_required: true
manual_description_reason: Chapter summary references Woola's presence and actions but provides no physical description (appearance, height, build, facial features) for dependable image generation. Source material only describes her movements and decisions.
clarification_required: false
clarification_reason: 
clarification_question: 
[[SECTION markdown]]
# Woola - Character Profile

**Display Name:** Woola  
**Chapter Role:** Animal Companion / Reunited Ally  
**Physical Presence:** Referenced throughout chapter (located in Thark, reunited with John)  
**Physical Description:** Not provided in source material. Summary describes her actions and decisions but lacks visual details for rendering.  
**Costume/Silhouette:** Unknown from chapter summary. Would require additional source material for accurate depiction.  
**Continuity Traits:** Animal companion to John Carter; separated then reunited; moves with John through city; navigates herd at night.  

**Render-Facing Notes:** 
- Character is physically present and referenced multiple times
- No stable visual identification available from chapter summary alone
- Would need canonical Barsoom source material for accurate physical description
- Continuity-critical: Animal companion, moves with John through city

**Uncertainty Statement:** 
Physical appearance details are missing from this chapter's source material. For dependable image generation, additional canonical descriptions would be required beyond what is provided in the chapter summary.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: sarkoja
canonical_character_id: sarkoja
aliases: 
is_fully_identified: true
manual_description_required: true
manual_description_reason: Chapter summary references Sarkoja's presence and actions but provides no physical description (appearance, height, build, facial features) for dependable image generation. Source material only describes her movements and decisions.
clarification_required: false
clarification_reason: 
clarification_question: 
[[SECTION markdown]]
# Sarkoja - Character Profile

**Display Name:** Sarkoja  
**Chapter Role:** Antagonist / Threat Revealed  
**Physical Presence:** Referenced in chapter (seen planning arena threat)  
**Physical Description:** Not provided in source material. Summary describes her actions and decisions but lacks visual details for rendering.  
**Costume/Silhouette:** Unknown from chapter summary. Would require additional source material for accurate depiction.  
**Continuity Traits:** Seen by John Carter; plans to throw Dejah Thoris to wild calots during arena games; threat revealed in chapter.  

**Render-Facing Notes:** 
- Character is referenced but not physically present in main escape sequence
- No stable visual identification available from chapter summary alone
- Would need canonical Barsoom source material for accurate physical description
- Continuity-critical: Antagonist planning arena threat

**Uncertainty Statement:** 
Physical appearance details are missing from this chapter's source material. For dependable image generation, additional canonical descriptions would be required beyond what is provided in the chapter summary.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: jeddak
canonical_character_id: jeddak
aliases: 
is_fully_identified: false
manual_description_required: true
manual_description_reason: Chapter summary references Jeddak's quarters and vaults but provides no physical description (appearance, height, build, facial features) for dependable image generation. Source material only describes his property and not the person himself.
clarification_required: true
clarification_reason: Character is referenced only through property (quarters beneath his vaults). Physical identification is weak - only known as "Jeddak" without additional descriptors or context that would stabilize visual representation.
clarification_question: Does the chapter summary provide any canonical physical description of Jeddak from other source material, or should this character be treated as unidentified for image generation purposes?
[[SECTION markdown]]
# Jeddak - Character Profile

**Display Name:** Jeddak  
**Chapter Role:** Referenced Authority / Property Owner  
**Physical Presence:** Not physically present in chapter (only quarters/vaults referenced)  
**Physical Description:** Not provided in source material. Summary describes his property but not the person himself.  
**Costume/Silhouette:** Unknown from chapter summary. Would require additional source material for accurate depiction.  
**Continuity Traits:** Quarters mentioned beneath his vaults; warriors plan to chain John Carter there if he returns without Dejah Thoris.  

**Render-Facing Notes:** 
- Character is referenced but not physically present in chapter
- No stable visual identification available from chapter summary alone
- Would need canonical Barsoom source material for accurate physical description
- Continuity-critical: Property owner whose quarters are central to threat

**Uncertainty Statement:** 
Physical appearance details are missing from this chapter's source material. For dependable image generation, additional canonical descriptions would be required beyond what is provided in the chapter summary. Character identification is weak - only known through property references without stable visual descriptors.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
