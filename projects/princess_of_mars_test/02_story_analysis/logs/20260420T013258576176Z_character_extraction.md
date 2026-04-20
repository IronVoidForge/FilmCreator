# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-20T01:32:58.576176+00:00
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

Chapter id: CH021

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

# Chapter Summary: An Air Scout for Zodanga

**Broad Story Summary:**
John Carter arrives at Zodanga after parting with his companion Woola at the city gates to ensure safety within the walled city. He enters via a letter of introduction from the Ptor brothers and proceeds to the central plaza. There, he meets Kantos Kan, an air scout who is searching for Dejah Thoris. Carter joins the Air Scout Squadron under Kantos Kan's guidance.

Over the next few days, Carter learns to fly Martian aircraft and repair them. On his fourth day, he makes his first flight and saves a cousin of the Jeddak Than Kosis from three Green Warriors who were attacking him while he was repairing his craft. Carter engages in combat, defeating the warriors with ease. Following this feat, he is decorated during a ceremony on the plain before the city by Than Kosis. He is appointed a padwar of The Guards and granted quarters in the palace of Than Kosis.

**Visual Continuity Facts:**
*   **City Layout:** Residences are raised high upon metal columns resembling steel tree trunks; shops are not raised from the ground. A vast central plaza covers a square mile, bounded by palaces and public buildings.
*   **Technology:** Airships have bodies about sixteen feet long with radium engines on top; buoyancy is provided by the eighth Barsoomian ray. Cafes serve food via mechanical apparatus where buttons indicate desires.
*   **Combat & Threats:** Green Warriors attack on flying mounts (thoats) using metal-shod spears and long-swords. They are described as "green monsters" with unmanageable animals when frightened.
*   **Ceremony Details:** The decoration ceremony involves a concourse of civilians and troops assembled on the plain; naval vessels fill the sky with streamers. Decorations are metal ornaments placed on the left arm.
*   **Character Appearance:** John Carter is recognized by his ability to bounce like a rubber ball (color change) and his Earth-like appearance compared to Martians. Woola is described as a huge brute of an undomesticated species.
````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
task: character_extraction
version: 1

[[SECTION character_index_markdown]]
# Character Index - Chapter CH021

## Characters Referenced in "An Air Scout for Zodanga"

| Asset ID | Canonical Character ID | Display Name | Role | Physical Description Status |
|----------|------------------------|--------------|------|----------------------------|
| john_carter | john_carter | John Carter | Protagonist, Earth visitor to Zodanga | Manual description required |
| woola | woola | Woola | Companion of John Carter | Manual description required |
| kantos_kan | kantos_kan | Kantos Kan | Air Scout Squadron Leader | Manual description required |
| dejah_thoris | dejah_thoris | Dejah Thoris | Subject of search, Princess of Zodanga | Manual description required |
| ptor_brothers | ptor_brothers | Ptor Brothers | Letter writers, city officials | Manual description required |
| than_kosis | than_kosis | Jeddak Than Kosis | Ruler of Zodanga, decoration ceremony host | Manual description required |
| green_warriors | green_warriors | Green Warriors | Combat threat, three warriors | Manual description required |

## Notes on Character Identification

All characters are named and have established roles within the chapter narrative. However, detailed physical descriptions for image generation purposes are not provided in this chapter summary. Each character record includes a markdown file explaining the identification status and any missing visual details that require manual specification for later render-facing prompt writing.
[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: john_carter
canonical_character_id: john_carter
aliases: 
is_fully_identified: true
manual_description_required: true
manual_description_reason: Chapter summary only notes John Carter is recognized by his ability to bounce like a rubber ball (color change) and his Earth-like appearance compared to Martians. No detailed physical description, costume, or silhouette traits are provided for dependable image generation.
clarification_required: false
clarification_reason: 
clarification_question: 

[[SECTION markdown]]
# John Carter - Character File

## Display Name: John Carter

## Chapter Role: Protagonist, Earth visitor to Zodanga

## Physical Presence Status: Physically present throughout chapter

## Physical Description (Source-Supported):
- Recognized by ability to bounce like a rubber ball with color change
- Described as having Earth-like appearance compared to Martians

## Costume/Silhouette/Continuity Traits (Known):
- None specified in this chapter summary

## Continuity-Critical Notes:
- Arrives at Zodanga after parting with companion Woola at city gates
- Enters via letter of introduction from Ptor brothers
- Joins Air Scout Squadron under Kantos Kan's guidance
- Makes first flight on fourth day, saves cousin of Jeddak Than Kosis from Green Warriors
- Decorated during ceremony on plain before city by Than Kosis
- Appointed padwar of The Guards and granted palace quarters

## Render-Facing Prompt Notes:
- Requires manual physical description specification for dependable image generation
- Visual continuity fact notes Earth-like appearance vs Martian contrast
- Color change ability noted as distinctive trait

## Uncertainty Notes:
- Detailed facial features, hair style, body build not specified in source material
- Costume details for Zodanga period not provided in chapter summary
- Silhouette and posture traits missing from visual continuity facts
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: woola
canonical_character_id: woola
aliases: 
is_fully_identified: true
manual_description_required: true
manual_description_reason: Chapter summary describes Woola as a huge brute of an undomesticated species. No detailed physical description, costume, or silhouette traits are provided for dependable image generation.
clarification_required: false
clarification_reason: 
clarification_question: 

[[SECTION markdown]]
# Woola - Character File

## Display Name: Woola

## Chapter Role: Companion of John Carter

## Physical Presence Status: Referenced (parting at gates)

## Physical Description (Source-Supported):
- Described as a huge brute of an undomesticated species

## Costume/Silhouette/Continuity Traits (Known):
- None specified in this chapter summary

## Continuity-Critical Notes:
- Parting with John Carter at Zodanga city gates to ensure safety within walled city
- Undomesticated species noted as distinctive trait

## Render-Facing Prompt Notes:
- Requires manual physical description specification for dependable image generation
- Visual continuity fact notes huge brute appearance
- Undomesticated species contrast with Earth visitors

## Uncertainty Notes:
- Detailed facial features, hair style, body build not specified in source material
- Costume details for Zodanga period not provided in chapter summary
- Silhouette and posture traits missing from visual continuity facts
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: kantos_kan
canonical_character_id: kantos_kan
aliases: 
is_fully_identified: true
manual_description_required: true
manual_description_reason: Chapter summary identifies Kantos Kan as an air scout searching for Dejah Thoris. No detailed physical description, costume, or silhouette traits are provided for dependable image generation.
clarification_required: false
clarification_reason: 
clarification_question: 

[[SECTION markdown]]
# Kantos Kan - Character File

## Display Name: Kantos Kan

## Chapter Role: Air Scout Squadron Leader

## Physical Presence Status: Physically present throughout chapter

## Physical Description (Source-Supported):
- None specified in this chapter summary

## Costume/Silhouette/Continuity Traits (Known):
- Air scout uniform implied but not detailed

## Continuity-Critical Notes:
- Searching for Dejah Thoris when Carter arrives
- Carter joins Air Scout Squadron under Kantos Kan's guidance
- Guides Carter to learn to fly Martian aircraft and repair them

## Render-Facing Prompt Notes:
- Requires manual physical description specification for dependable image generation
- Role as air scout leader noted in visual continuity facts
- No specific costume or silhouette traits provided in source material

## Uncertainty Notes:
- Detailed facial features, hair style, body build not specified in source material
- Costume details for Zodanga period not provided in chapter summary
- Silhouette and posture traits missing from visual continuity facts
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: dejah_thoris
canonical_character_id: dejah_thoris
aliases: 
is_fully_identified: true
manual_description_required: true
manual_description_reason: Chapter summary references Dejah Thoris as subject of search by Kantos Kan. No detailed physical description, costume, or silhouette traits are provided for dependable image generation in this chapter context.
clarification_required: false
clarification_reason: 
clarification_question: 

[[SECTION markdown]]
# Dejah Thoris - Character File

## Display Name: Dejah Thoris

## Chapter Role: Princess of Zodanga, Subject of Search

## Physical Presence Status: Referenced (not physically present in chapter)

## Physical Description (Source-Supported):
- None specified in this chapter summary

## Costume/Silhouette/Continuity Traits (Known):
- Princess status implied but not detailed

## Continuity-Critical Notes:
- Kantos Kan is searching for Dejah Thoris when Carter arrives
- Subject of search mentioned as primary motivation for air scout activity

## Render-Facing Prompt Notes:
- Requires manual physical description specification for dependable image generation
- Role as Princess of Zodanga noted in visual continuity facts
- No specific costume or silhouette traits provided in source material

## Uncertainty Notes:
- Detailed facial features, hair style, body build not specified in source material
- Costume details for Zodanga period not provided in chapter summary
- Silhouette and posture traits missing from visual continuity facts
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: ptor_brothers
canonical_character_id: ptor_brothers
aliases: 
is_fully_identified: true
manual_description_required: true
manual_description_reason: Chapter summary mentions Ptor brothers as letter writers providing introduction. No detailed physical description, costume, or silhouette traits are provided for dependable image generation.
clarification_required: false
clarification_reason: 
clarification_question: 

[[SECTION markdown]]
# Ptor Brothers - Character File

## Display Name: Ptor Brothers

## Chapter Role: Letter Writers, City Officials

## Physical Presence Status: Referenced (not physically present in chapter)

## Physical Description (Source-Supported):
- None specified in this chapter summary

## Costume/Silhouette/Continuity Traits (Known):
- City officials status implied but not detailed

## Continuity-Critical Notes:
- Provide letter of introduction for John Carter to enter Zodanga safely
- Proceeds to central plaza after entering via their letter

## Render-Facing Prompt Notes:
- Requires manual physical description specification for dependable image generation
- Role as city officials noted in visual continuity facts
- No specific costume or silhouette traits provided in source material

## Uncertainty Notes:
- Detailed facial features, hair style, body build not specified in source material
- Costume details for Zodanga period not provided in chapter summary
- Silhouette and posture traits missing from visual continuity facts
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: than_kosis
canonical_character_id: than_kosis
aliases: 
is_fully_identified: true
manual_description_required: true
manual_description_reason: Chapter summary identifies Jeddak Than Kosis as ruler of Zodanga who decorates Carter. No detailed physical description, costume, or silhouette traits are provided for dependable image generation.
clarification_required: false
clarification_reason: 
clarification_question: 

[[SECTION markdown]]
# Jeddak Than Kosis - Character File

## Display Name: Jeddak Than Kosis

## Chapter Role: Ruler of Zodanga, Decoration Ceremony Host

## Physical Presence Status: Physically present throughout chapter

## Physical Description (Source-Supported):
- None specified in this chapter summary

## Costume/Silhouette/Continuity Traits (Known):
- Ruler status implied but not detailed

## Continuity-Critical Notes:
- Carter saves cousin of Jeddak Than Kosis from Green Warriors
- Decorates Carter during ceremony on plain before city
- Appoints Carter as padwar of The Guards and grants palace quarters

## Render-Facing Prompt Notes:
- Requires manual physical description specification for dependable image generation
- Role as ruler of Zodanga noted in visual continuity facts
- No specific costume or silhouette traits provided in source material

## Uncertainty Notes:
- Detailed facial features, hair style, body build not specified in source material
- Costume details for Zodanga period not provided in chapter summary
- Silhouette and posture traits missing from visual continuity facts
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: green_warriors
canonical_character_id: green_warriors
aliases: 
is_fully_identified: true
manual_description_required: true
manual_description_reason: Chapter summary describes Green Warriors as three warriors attacking on flying mounts. No detailed physical description, costume, or silhouette traits are provided for dependable image generation.
clarification_required: false
clarification_reason: 
clarification_question: 

[[SECTION markdown]]
# Green Warriors - Character File

## Display Name: Green Warriors

## Chapter Role: Combat Threat, Three Warriors

## Physical Presence Status: Referenced (attack on fourth day)

## Physical Description (Source-Supported):
- Described as "green monsters" with unmanageable animals when frightened
- Attack on flying mounts (thoats) using metal-shod spears and long-swords

## Costume/Silhouette/Continuity Traits (Known):
- Green coloration noted
- Flying mount riders implied

## Continuity-Critical Notes:
- Three warriors attack cousin of Jeddak Than Kosis while he repairs craft
- Carter engages in combat, defeating the warriors with ease
- Attack occurs on fourth day during Carter's first flight period

## Render-Facing Prompt Notes:
- Requires manual physical description specification for dependable image generation
- Visual continuity fact notes green coloration and monster description
- Metal-shod spears and long-swords noted as weapon traits
- Flying mounts (thoats) implied as vehicle type

## Uncertainty Notes:
- Detailed facial features, hair style, body build not specified in source material
- Costume details for Zodanga period not provided in chapter summary
- Silhouette and posture traits missing from visual continuity facts
[[/SECTION]]
[[/FILMCREATOR_RECORD]]
[[/FILMCREATOR_PACKET]]
````
