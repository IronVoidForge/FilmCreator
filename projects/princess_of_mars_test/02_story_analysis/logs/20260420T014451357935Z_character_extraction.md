# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-20T01:44:51.357935+00:00
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

Chapter id: CH028

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

Visual Continuity:
The scene opens in darkness within a cave where the narrator finds stiff garments that crack and powder away upon rising. He discovers a match wrapped in oiled paper, which illuminates a grotesque tableau: a mummified old woman huddled over a charcoal burner with greenish powder, and human skeletons hanging from rawhide thongs across the roof. Stepping out onto a ledge reveals a new landscape of silvered mountains, cacti-studded valleys, and a stationary moon—identifying the location as Arizona rather than Mars.

Narrative Arc:
The narrator realizes he has returned to Earth after ten years on Mars (totaling twenty years since his first awakening). He feels consternation at the sight of the familiar Arizona landscape from which he once gazed longingly at Mars. Despite his wealth, he is broken and sorrowful, questioning whether Dejah Thoris lives or died beside her incubator in Tardos Mors's palace. The chapter concludes with him looking out his window at Mars, imagining Dejah Thoris and a young boy waiting for him across the abyss of space, suggesting an impending reunion or revelation regarding their fate.
````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
task: character_extraction
version: 1

[[SECTION character_index_markdown]]
# Character Index - CH028 (princess_of_mars_test)

| Asset ID | Canonical Character ID | Display Name | Presence Status | Description Complete |
|----------|------------------------|--------------|-----------------|---------------------|
| narrator | narrator | The Narrator | Referenced/Physical | Partial |
| dejah_thoris | dejah_thoris | Dejah Thoris | Referenced | Partial |
| mummified_old_woman | mummified_old_woman | Mummified Old Woman | Physical | Complete |
| young_boy | young_boy | Young Boy | Imagined/Referenced | Partial |

*Note: Characters marked "Partial" require manual description for reliable image generation.*
[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: narrator
canonical_character_id: narrator
aliases: 
is_fully_identified: false
manual_description_required: true
manual_description_reason: The chapter summary does not provide physical appearance details about the narrator beyond his experiences and discoveries. No description of his face, body, or clothing is given in this chapter material.
clarification_required: false
clarification_reason: 
clarification_question: 

[[SECTION markdown]]
# Narrator - CH028

**Display Name:** The Narrator  
**Chapter Role:** First-person perspective character, central figure experiencing the return from Mars to Earth  
**Physical Presence:** Referenced and implied physical presence (the narrator is the one discovering items and observing scenes)  

## Physical Description (Supported by Source)
- No specific physical details provided in this chapter material
- The narrator finds stiff garments that crack and powder away upon rising
- He discovers a match wrapped in oiled paper
- He observes a mummified old woman huddled over a charcoal burner with greenish powder
- Human skeletons hanging from rawhide thongs across the roof are visible to him

## Costume, Silhouette, Continuity-Critical Traits (Known)
- None specified in this chapter material
- The stiff garments that crack away may have been his clothing before discovery

## Descriptive Noun Phrases for Render-Facing Prompt Writing
- "man returning from Mars after ten years"
- "observer of grotesque cave tableau"
- "figure contemplating Dejah Thoris's fate"
- "wealthy but broken and sorrowful character"

## Uncertainty Notes
- Physical appearance is not described in this chapter material
- Current clothing state is uncertain (stiff garments found cracking away)
- Facial features, body type, and age are unknown from this source
- Manual description required for reliable image generation
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: dejah_thoris
canonical_character_id: dejah_thoris
aliases: 
is_fully_identified: false
manual_description_required: true
manual_description_reason: Dejah Thoris is only referenced in this chapter material—mentioned as possibly living or dead beside her incubator in Tardos Mors's palace, and imagined waiting with a young boy. No current physical appearance, clothing, or visual details are provided in this chapter source.
clarification_required: false
clarification_reason: 
clarification_question: 

[[SECTION markdown]]
# Dejah Thoris - CH028

**Display Name:** Dejah Thoris  
**Chapter Role:** Referenced love interest/central figure of narrator's emotional concern  
**Physical Presence:** Referenced only (imagined/waiting, not physically present in this scene)  

## Physical Description (Supported by Source)
- No physical description provided in this chapter material
- Only referenced as being in Tardos Mors's palace with an incubator
- Imagined as waiting for the narrator across space

## Costume, Silhouette, Continuity-Critical Traits (Known)
- None specified in this chapter material
- Her current state (alive or dead) is uncertain from this source

## Descriptive Noun Phrases for Render-Facing Prompt Writing
- "Dejah Thoris imagined waiting at palace"
- "figure of emotional significance to narrator"
- "character whose fate concerns the protagonist"
- "imagined companion across space abyss"

## Uncertainty Notes
- Physical appearance is not described in this chapter material
- Current state (alive/dead) is uncertain from this source
- Facial features, body type, and age are unknown from this chapter
- Manual description required for reliable image generation
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: mummified_old_woman
canonical_character_id: mummified_old_woman
aliases: 
is_fully_identified: true
manual_description_required: false
manual_description_reason: The chapter summary provides sufficient physical description of this character's presence and appearance in the cave scene.
clarification_required: false
clarification_reason: 
clarification_question: 

[[SECTION markdown]]
# Mummified Old Woman - CH028

**Display Name:** Mummified Old Woman  
**Chapter Role:** Physical presence in cave tableau, part of grotesque discovery  
**Physical Presence:** Physically present (huddled over charcoal burner in cave)  

## Physical Description (Supported by Source)
- Described as mummified old woman huddled over a charcoal burner with greenish powder
- Part of the grotesque tableau illuminated by match wrapped in oiled paper
- Located within dark cave environment

## Costume, Silhouette, Continuity-Critical Traits (Known)
- Mummified appearance (wrapped/bandaged form implied)
- Huddled posture over charcoal burner
- Associated with greenish powder and rawhide thongs in scene

## Descriptive Noun Phrases for Render-Facing Prompt Writing
- "mummified old woman huddled over charcoal"
- "figure wrapped in bandages, cave setting"
- "grotesque tableau element, greenish powder nearby"
- "dark cave discovery, mummified form"

## Uncertainty Notes
- Specific facial features beyond "old woman" are not detailed
- Exact mummification style is not specified
- Current condition (alive/dead) is uncertain from this source
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: young_boy
canonical_character_id: young_boy
aliases: 
is_fully_identified: false
manual_description_required: true
manual_description_reason: The young boy is only imagined as waiting with Dejah Thoris across space. No physical description, appearance details, or visual characteristics are provided in this chapter material.
clarification_required: false
clarification_reason: 
clarification_question: 

[[SECTION markdown]]
# Young Boy - CH028

**Display Name:** Young Boy  
**Chapter Role:** Imagined companion waiting with Dejah Thoris, part of narrator's hopeful vision  
**Physical Presence:** Imagined/Referenced only (not physically present in this scene)  

## Physical Description (Supported by Source)
- No physical description provided in this chapter material
- Only referenced as "a young boy" waiting for the narrator across space

## Costume, Silhouette, Continuity-Critical Traits (Known)
- None specified in this chapter material
- Age category: young boy

## Descriptive Noun Phrases for Render-Facing Prompt Writing
- "young boy imagined waiting at palace"
- "child figure accompanying Dejah Thoris in vision"
- "hopeful companion across space abyss"
- "imagined child, awaiting reunion"

## Uncertainty Notes
- Physical appearance is not described in this chapter material
- Facial features, body type, and age specifics are unknown from this source
- Current state (alive/dead) is uncertain from this chapter
- Manual description required for reliable image generation
[[/SECTION]]
[[/FILMCREATOR_RECORD]]
[[/FILMCREATOR_PACKET]]
````
