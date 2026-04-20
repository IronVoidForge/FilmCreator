# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-20T01:43:14.614345+00:00
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

Chapter id: CH027

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

# Chapter Summary: Chapter XXVII - From Joy to Death

## Visual Continuity Facts
*   **Golden Incubator:** Located on the roof of the Helium Palace, containing a snow-white egg representing the unborn son.
*   **Airship Arrival:** A bright-white light approaches Helium, landing at the palace docks with dispatch signals for the Jeddak.
*   **Council Chamber:** Tardos Mors paces on the raised platform while members fill the chamber; silence follows his announcement of doom.
*   **Palace Garden:** Royal family (including Woola) gathers in a sunken garden within an inner courtyard as breathing becomes difficult.
*   **Flight Path:** Carter flies low across an old sea bottom to maintain sufficient air for breathing, discarding ornaments and lying on the deck.
*   **Atmosphere Plant Exterior:** Great walls loom before him; small door with crew laboring to pierce the wall.
*   **Plant Interior:** Three great doors open sequentially; Carter opens the second and third while collapsing unconscious.

## Broad Story Summary
Barsoom faces extinction as the atmosphere plant engine stops, causing air pressure to decrease rapidly. The Jeddak declares three days remaining before death by asphyxiation becomes inevitable for the entire population. John Carter discovers "nine long forgotten sounds" (thought waves) which serve as the key to unlock the three great doors of the atmosphere plant. He flies to the plant at high speed, discarding all weight except the engine and compass. Upon arrival, he opens the doors sequentially while his companion starts the pumps, saving Barsoom but collapsing from exhaustion.
````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
task: character_extraction
version: 1

[[SECTION character_index_markdown]]
# Character Index - Chapter XXVII

| Asset ID | Canonical Character ID | Aliases | Fully Identified | Manual Description Required | Clarification Required |
|----------|------------------------|---------|------------------|----------------------------|------------------------|
| tardos_mors | Tardos Mors | - | true | true | false |
| woola | Woola | - | true | true | false |
| john_carter | John Carter / Carter | - | true | true | false |
| companion | Companion | - | false | true | true |

**Notes:**
- All characters have minimal physical description in this chapter's source material
- Companion lacks stable identification and requires clarification
- Manual descriptions needed for all due to insufficient visual details for image generation
[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: tardos_mors
canonical_character_id: Tardos Mors
aliases: -
is_fully_identified: true
manual_description_required: true
manual_description_reason: Chapter summary only mentions "Tardos Mors paces on the raised platform" with no physical description, facial features, or costume details provided for image generation purposes.
clarification_required: false
clarification_reason: -
clarification_question: -

[[SECTION markdown]]
# tardos_mors

**Display Name:** Tardos Mors  
**Chapter Role:** Council Member / Platform Pacer  
**Physical Presence:** Referenced (Council Chamber)  

## Physical Description
*Unknown in this chapter source material.*

## Costume & Silhouette
*No costume or silhouette details provided in Chapter XXVII summary.*

## Continuity-Critical Traits
- Paces on raised platform during Council announcement of doom
- Member of ruling council at Helium Palace

## Render-Facing Prompt Notes
**Uncertainty:** This character requires manual description for image generation. No physical features, facial structure, or attire details are available in the supplied chapter material. Use established appearance from earlier chapters if permitted, otherwise flag for clarification.

**Key Noun Phrases:** council member, platform pacer, doom announcer, ruling authority
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: woola
canonical_character_id: Woola
aliases: -
is_fully_identified: true
manual_description_required: true
manual_description_reason: Chapter summary only identifies "Woola" as part of the Royal family gathering in Palace Garden with no physical description, facial features, or costume details provided.
clarification_required: false
clarification_reason: -
clarification_question: -

[[SECTION markdown]]
# woola

**Display Name:** Woola  
**Chapter Role:** Royal Family Member / Garden Gatherer  
**Physical Presence:** Referenced (Palace Garden)  

## Physical Description
*Unknown in this chapter source material.*

## Costume & Silhouette
*No costume or silhouette details provided in Chapter XXVII summary.*

## Continuity-Critical Traits
- Present during Royal family gathering in sunken garden
- Located within inner courtyard of Helium Palace

## Render-Facing Prompt Notes
**Uncertainty:** This character requires manual description for image generation. No physical features, facial structure, or attire details are available in the supplied chapter material. Use established appearance from earlier chapters if permitted, otherwise flag for clarification.

**Key Noun Phrases:** royal family member, garden gatherer, palace resident
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: john_carter
canonical_character_id: John Carter / Carter
aliases: Carter
is_fully_identified: true
manual_description_required: true
manual_description_reason: Chapter summary describes actions ("flies low across old sea bottom", "opens doors sequentially") but provides no physical description, facial features, or costume details for image generation purposes.
clarification_required: false
clarification_reason: -
clarification_question: -

[[SECTION markdown]]
# john_carter

**Display Name:** John Carter  
**Chapter Role:** Main Character / Atmosphere Plant Rescue Mission  
**Physical Presence:** Physically Present (Flight to Plant, Door Opening)  

## Physical Description
*Unknown in this chapter source material.*

## Costume & Silhouette
*No costume or silhouette details provided in Chapter XXVII summary.*

## Continuity-Critical Traits
- Discards ornaments and lies on deck during flight
- Opens second and third great doors of atmosphere plant
- Companion starts pumps while he collapses unconscious
- Flies at high speed to maintain sufficient air for breathing

## Render-Facing Prompt Notes
**Uncertainty:** This character requires manual description for image generation. No physical features, facial structure, or attire details are available in the supplied chapter material. Use established appearance from earlier chapters if permitted, otherwise flag for clarification.

**Key Noun Phrases:** atmosphere plant rescuer, door opener, flight pilot, unconscious collapse
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: companion
canonical_character_id: Companion
aliases: -
is_fully_identified: false
manual_description_required: true
manual_description_reason: Chapter summary only refers to "companion" with no name, physical description, or identity provided. Cannot generate images without clarification on who this character is and what they look like.
clarification_required: true
clarification_reason: Character lacks stable identification - referred to only as "companion" with no established name or visual details in source material.
clarification_question: Who is the companion that starts the pumps at the atmosphere plant? What is their name, physical appearance, and role relationship to John Carter?

[[SECTION markdown]]
# companion

**Display Name:** Companion (Unnamed)  
**Chapter Role:** Pump Operator / Atmosphere Plant Assistant  
**Physical Presence:** Physically Present (Plant Interior)  

## Physical Description
*Unknown - requires clarification.*

## Costume & Silhouette
*No costume or silhouette details provided in Chapter XXVII summary.*

## Continuity-Critical Traits
- Starts pumps at atmosphere plant interior
- Located inside plant when Carter opens doors sequentially
- Works alongside John Carter during rescue mission

## Render-Facing Prompt Notes
**Uncertainty:** This character requires both manual description AND clarification. No physical features, facial structure, attire, or identity are available in the supplied chapter material. Cannot generate images without knowing who this companion is and what they look like.

**Key Noun Phrases:** pump operator, plant interior resident, Carter's assistant
[[/SECTION]]
[[/FILMCREATOR_RECORD]]
[[/FILMCREATOR_PACKET]]
````
