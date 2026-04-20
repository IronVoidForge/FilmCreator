# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-20T01:59:19.176650+00:00
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

Chapter id: CH001

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

**Visual Continuity:**
The chapter opens on the Arizona Hills under clear morning light. Key locations include a mountainside trail, a valley with hog backs and plateaus, a water hole, and a large cave entrance (four feet high). The setting shifts from daylight to moonlight during the chase. Visual markers include burros, horses, Colt revolvers, cartridge belts, and Indian tepees clustered around a central object.
**Story Summary:**
John Carter reflects on his ageless existence and fear of death despite having died twice. He recounts his Civil War past and partnership with Captain Powell to mine gold in Arizona. After guarding the claim while Powell leaves for supplies, Carter discovers Powell's tracks have been followed by Apaches. He chases them into a valley where he finds an Apache camp surrounding Powell's body. Overwhelmed by duty, Carter charges the warriors alone, scattering them. He retrieves Powell's corpse and flees into a rocky defile leading to a cave. Inside the cave, he lays Powell down, confirms death, and succumbs to fatigue on the cave floor.
````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
task: character_extraction
version: 1

[[SECTION character_index_markdown]]
# Character Index - CH001

| Asset ID | Canonical Character ID | Aliases | Fully Identified | Manual Description Required |
|----------|------------------------|---------|------------------|----------------------------|
| john_carter | John Carter | - | true | true |
| captain_powell | Captain Powell | - | true | true |
| apaches | Apaches | Apache warriors, Apache camp | false | true |

**Notes:** All characters lack physical descriptions in source material for image generation purposes.
[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: john_carter
canonical_character_id: John Carter
aliases: 
is_fully_identified: true
manual_description_required: true
manual_description_reason: No physical description, costume, or silhouette details provided in chapter summary for image generation. Character is only identified by name and role (protagonist reflecting on ageless existence).
clarification_required: false
clarification_reason: 
clarification_question: 

[[SECTION markdown]]
# John Carter

**Display Name:** John Carter  
**Chapter Role:** Protagonist / Civil War veteran / Gold miner partner  

**Physical Presence:** Referenced throughout chapter (reflects on ageless existence, guards claim, discovers tracks, chases Apaches, retrieves corpse)  

**Physical Description:** None provided in source material. Character is only identified by name and narrative role.  

**Costume/Silhouette:** Unknown - no visual details available for image generation.  

**Continuity-Critical Traits:** 
- Ageless existence (reflects on having died twice)
- Civil War past
- Partnership with Captain Powell to mine gold in Arizona
- Guardian of the claim while Powell leaves for supplies

**Uncertainty Notes:** 
- No physical description supports dependable later image generation
- Manual description required before character can be rendered visually
- Character is fully identified by name and role but lacks visual continuity markers

**Useful Descriptive Noun Phrases:** 
- "Ageless protagonist reflecting on mortality"
- "Civil War veteran guarding gold claim in Arizona"
- "Partner to Captain Powell in mining operations"
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: captain_powell
canonical_character_id: Captain Powell
aliases: 
is_fully_identified: true
manual_description_required: true
manual_description_reason: No physical description, costume, or silhouette details provided in chapter summary for image generation. Character is only identified by name and role (Carter's mining partner).
clarification_required: false
clarification_reason: 
clarification_question: 

[[SECTION markdown]]
# Captain Powell

**Display Name:** Captain Powell  
**Chapter Role:** Deceased Mining Partner / Civil War veteran  

**Physical Presence:** Referenced throughout chapter (leaves for supplies, body discovered dead by Carter)  

**Physical Description:** None provided in source material. Character is only identified by name and narrative role.  

**Costume/Silhouette:** Unknown - no visual details available for image generation.  

**Continuity-Critical Traits:** 
- Mining partner to John Carter
- Civil War veteran
- Leaves claim for supplies, body discovered dead by Apaches
- Carter retrieves corpse after charging Apache camp

**Uncertainty Notes:** 
- No physical description supports dependable later image generation
- Manual description required before character can be rendered visually
- Character is fully identified by name and role but lacks visual continuity markers
- Deceased status affects rendering considerations

**Useful Descriptive Noun Phrases:** 
- "Deceased mining partner in Arizona"
- "Civil War veteran with John Carter"
- "Body discovered surrounded by Apache warriors"
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: apaches
canonical_character_id: Apaches
aliases: Apache warriors, Apache camp
is_fully_identified: false
manual_description_required: true
manual_description_reason: No physical description, costume, or silhouette details provided in chapter summary for image generation. Character is only identified as collective group (Apache warriors surrounding Powell's body).
clarification_required: true
clarification_reason: Apaches mentioned as collective group without individual identification. May need clarification on whether to treat as single character entity or multiple individual characters for rendering purposes.
clarification_question: Should Apaches be treated as a single collective character entity or broken into individual warrior characters for image generation?

[[SECTION markdown]]
# Apaches

**Display Name:** Apaches  
**Chapter Role:** Antagonists / Apache warriors  

**Physical Presence:** Referenced throughout chapter (tracks followed by Apaches, camp surrounding Powell's body)  

**Physical Description:** None provided in source material. Character is only identified as collective group without individual visual details.  

**Costume/Silhouette:** Unknown - no visual details available for image generation.  

**Continuity-Critical Traits:** 
- Tracks follow Captain Powell leaving claim
- Camp discovered surrounding Powell's body after Carter chases them into valley
- Warriors scatter when Carter charges alone
- Clustered around central object (Powell's body)

**Uncertainty Notes:** 
- No physical description supports dependable later image generation
- Manual description required before character can be rendered visually
- Character is not fully identified as individual entities - only collective group mentioned
- Clarification needed on rendering approach for group vs individuals

**Useful Descriptive Noun Phrases:** 
- "Apache warriors surrounding Powell's body"
- "Collective antagonists in Arizona valley"
- "Warriors scattered by John Carter's charge"
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
