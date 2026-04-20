# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-20T00:56:09.688031+00:00
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

Chapter id: CH007

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

# Chapter VII: Child-Raising on Mars - Scene Summary

## Opening Sequence
- **Location**: Plaza to incubator facility
- **Event**: Breakfast showing exact replica of preceding day's meal, index of every meal while with green men
- **Procession**: Sola escorts narrator to plaza where entire community watches harnessing of huge mastodonian animals to three-wheeled chariots

## Procession Details
- **Scale**: Approximately 250 vehicles, each drawn by single animal
- **Chariot Description**: Large, commodious, gorgeously decorated
- **Occupants**: Female Martians loaded with ornaments of metal, jewels, silks, furs; young Martian drivers perched on beasts
- **Animal Control**: No bit or bridle, guided entirely by telepathic means
- **Formation**: Single file line of march, 200 warriors at head (five abreast), like number at rear, 25-30 outriders flanking sides

## Incubator Ceremony
- **Location**: Remote fastness incubator facility
- **Participants**: Half a score warriors headed by enormous chieftain Lorquas Ptomel Jed, including Tars Tarkas and several lesser chiefs
- **Event**: Narrator performs leap over parked chariots for edification of Lorquas Ptomel

## Young Martian Release System
- **Incubator Contents**: All but very few eggs hatched, fairly alive with hideous little devils (3-4 feet tall)
- **Release Method**: Opening broken in wall large enough to permit exit of young Martians
- **Capture Process**: Women and younger Martians form two solid walls leading through chariots into plain; little Martians scamper wild as deer, captured one at a time by women/older children
- **Distribution**: Last in line captures first to reach end; opposite captures second; those caught by young men later turned over to women

## Child-Raising System Explanation
- **Education Focus**: Teaching them to talk and use weapons of warfare from very first year of life
- **Birth Rate**: Each adult female brings forth about thirteen eggs each year
- **Selection Process**: Council of twenty chieftains examines yearly supply; all but about one hundred most perfect destroyed out of each yearly supply
- **Incubation Period**: Five years in almost air-tight incubators hatched by sun's rays
- **Hatching Rate**: All but about one per cent of eggs hatching in two days

## Community Demographics
- **Population**: Some thirty thousand souls
- **Territory**: Arid and semi-arid land between forty and eighty degrees south latitude
- **Boundaries**: Bounded on east and west by two large fertile tracts
- **Headquarters**: Southwest corner near crossing of two so-called Martian canals

## Narrator's Development
- **Telepathic Abilities**: Developed under Sola's tutelage, shortly could sense practically everything around narrator
- **Language Mastery**: In a week could make all wants known and understand nearly everything said to narrator
- **Unique Advantage**: Could catch telepathic messages easily from others but no one could read anything from narrator's mind

## Closing Scene
- **Location**: Narrator and Sola in their chariot
- **Sola's Prize**: Male about four feet tall, very strong and physically perfect; learned quickly with considerable amusement over keen rivalry displayed
````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
task: character_extraction
version: 1

[[SECTION character_index_markdown]]
# Character Index - Chapter VII: Child-Raising on Mars

| Asset ID | Canonical Character ID | Display Name | Chapter Role | Physical Presence | Description Status |
|----------|------------------------|--------------|---------------|-------------------|-------------------|
| sola | sola | Sola | Narrator's telepathic tutor and escort | Referenced | Manual description required |
| narrator | unnamed_narrator | Narrator (Unnamed) | First-person protagonist | Present | Manual description required |
| lorquas_ptomel_jed | lorquas_ptomel_jed | Lorquas Ptomel Jed | Enormous chieftain at incubator ceremony | Referenced | Manual description required |
| tars_tarkas | tars_tarkas | Tars Tarkas | Warrior in incubator ceremony | Referenced | Manual description required |

*Note: All characters require manual physical descriptions as chapter summary provides no appearance details.*
[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: sola
canonical_character_id: sola
aliases: ""
is_fully_identified: true
manual_description_required: true
manual_description_reason: "Chapter summary identifies Sola as narrator's telepathic tutor and escort but provides no physical appearance, height, build, or distinctive features for image generation"
clarification_required: false
clarification_reason: ""
clarification_question: ""

[[SECTION markdown]]
# Character File: Sola

## Display Name
Sola

## Chapter Role
Narrator's telepathic tutor and escort companion

## Physical Presence Status
Referenced throughout chapter (escorts narrator to plaza, provides tutelage)

## Physical Description
**Status:** Uncertain - No physical description provided in source material

**Supported Details:** None available from chapter summary

**Uncertainty Notes:** 
- Height: Unknown
- Build: Unknown  
- Hair/Eyes: Not mentioned
- Distinguishing features: Not documented
- Costume/silhouette: Not described

## Render-Facing Prompt Guidance
```
[UNCERTAIN PHYSICAL DESCRIPTION]
Subject: Female companion character (based on context of narrator's tutor)
Note: Requires manual physical description specification for image generation
Available traits from source: None - all appearance details must be defined externally
```

## Continuity-Critical Traits
- Telepathic abilities developed under Sola's tutelage
- Unique advantage: Could catch telepathic messages easily from others but no one could read anything from narrator's mind
- Language mastery achieved in a week under Sola's instruction

## Source Material Limitations
Chapter VII summary provides functional role identification only. No physical appearance, costume, or silhouette details available for dependable image generation. Manual description required before render-facing work.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: narrator
canonical_character_id: unnamed_narrator
aliases: ""
is_fully_identified: false
manual_description_required: true
manual_description_reason: "Narrator is unnamed first-person protagonist with no physical description provided in chapter summary; cannot be reliably identified for image generation without external specification"
clarification_required: true
clarification_reason: "Character lacks stable identification (unnamed) and requires clarification on whether this represents a specific character identity or generic narrator role"
clarification_question: "Is the unnamed narrator intended to represent a specific character with defined physical traits, or is this a generic first-person perspective without appearance requirements?"

[[SECTION markdown]]
# Character File: Narrator (Unnamed)

## Display Name
Narrator (Unnamed Protagonist)

## Chapter Role
First-person protagonist experiencing events on Mars

## Physical Presence Status
Present throughout chapter (experiences all described events)

## Physical Description
**Status:** Uncertain - No physical description provided in source material

**Supported Details:** None available from chapter summary

**Uncertainty Notes:** 
- Height: Unknown
- Build: Unknown  
- Hair/Eyes: Not mentioned
- Distinguishing features: Not documented
- Costume/silhouette: Not described

## Render-Facing Prompt Guidance
```
[UNCERTAIN PHYSICAL DESCRIPTION]
Subject: First-person narrator character (Mars setting)
Note: Requires manual physical description specification for image generation
Available traits from source: None - all appearance details must be defined externally
Clarification pending on character identity requirements
```

## Continuity-Critical Traits
- Developed telepathic abilities under Sola's tutelage
- Language mastery achieved in a week
- Unique advantage: Could catch telepathic messages easily but no one could read anything from narrator's mind
- Experiences harnessing of mastodonian animals to three-wheeled chariots
- Performs leap over parked chariots for edification of Lorquas Ptomel

## Source Material Limitations
Chapter VII summary provides functional role identification only. No physical appearance, costume, or silhouette details available for dependable image generation. Manual description required before render-facing work. Clarification needed on character identity requirements.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: lorquas_ptomel_jed
canonical_character_id: lorquas_ptomel_jed
aliases: ""
is_fully_identified: true
manual_description_required: true
manual_description_reason: "Chapter summary identifies Lorquas Ptomel Jed as enormous chieftain but provides no physical appearance, height, build, or distinctive features for image generation"
clarification_required: false
clarification_reason: ""
clarification_question: ""

[[SECTION markdown]]
# Character File: Lorquas Ptomel Jed

## Display Name
Lorquas Ptomel Jed

## Chapter Role
Enormous chieftain leading warriors at incubator ceremony

## Physical Presence Status
Referenced (leads half a score warriors headed by enormous chieftain)

## Physical Description
**Status:** Uncertain - No physical description provided in source material

**Supported Details:** None available from chapter summary

**Uncertainty Notes:** 
- Height: Unknown (described as "enormous" but no specific measurement)
- Build: Unknown  
- Hair/Eyes: Not mentioned
- Distinguishing features: Not documented
- Costume/silhouette: Not described

## Render-Facing Prompt Guidance
```
[UNCERTAIN PHYSICAL DESCRIPTION]
Subject: Martian chieftain character (enormous stature implied)
Note: Requires manual physical description specification for image generation
Available traits from source: "Enormous" descriptor only - all appearance details must be defined externally
```

## Continuity-Critical Traits
- Leads half a score warriors at incubator ceremony
- Narrator performs leap over parked chariots for edification of Lorquas Ptomel
- Part of remote fastness incubator facility proceedings

## Source Material Limitations
Chapter VII summary provides functional role identification only. No physical appearance, costume, or silhouette details available for dependable image generation. Manual description required before render-facing work.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: tars_tarkas
canonical_character_id: tars_tarkas
aliases: ""
is_fully_identified: true
manual_description_required: true
manual_description_reason: "Chapter summary identifies Tars Tarkas as warrior but provides no physical appearance, height, build, or distinctive features for image generation"
clarification_required: false
clarification_reason: ""
clarification_question: ""

[[SECTION markdown]]
# Character File: Tars Tarkas

## Display Name
Tars Tarkas

## Chapter Role
Warrior in incubator ceremony procession

## Physical Presence Status
Referenced (included among warriors headed by enormous chieftain)

## Physical Description
**Status:** Uncertain - No physical description provided in source material

**Supported Details:** None available from chapter summary

**Uncertainty Notes:** 
- Height: Unknown
- Build: Unknown  
- Hair/Eyes: Not mentioned
- Distinguishing features: Not documented
- Costume/silhouette: Not described

## Render-Facing Prompt Guidance
```
[UNCERTAIN PHYSICAL DESCRIPTION]
Subject: Martian warrior character (incubator ceremony participant)
Note: Requires manual physical description specification for image generation
Available traits from source: None - all appearance details must be defined externally
```

## Continuity-Critical Traits
- Warrior included in half a score warriors headed by enormous chieftain Lorquas Ptomel Jed
- Part of incubator ceremony proceedings at remote fastness facility
- Includes several lesser chiefs alongside Tars Tarkas

## Source Material Limitations
Chapter VII summary provides functional role identification only. No physical appearance, costume, or silhouette details available for dependable image generation. Manual description required before render-facing work.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
