# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-18T20:56:27.510258+00:00
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

# Chapter Title
Chapter VIII - A Fair Captive from the Sky

# Scene 1: Retreat & Investigation
- **Event:** Martians retreat immediately after incubation ceremony procession debouches into open ground.
- **Action:** Narrator investigates cause of sudden retreat from upper floor window.
- **Visual:** Twenty gray air ships swing slowly over hill crests, each carrying strange banners and odd devices on prows.

# Scene 2: Battle
- **Event:** Green warriors fire a terrific volley from building windows facing the valley.
- **Action:** Air fleet returns fire with guns; ships move parallel to firing line then turn back.
- **Visual:** Banners dissolve in spurts of flame; green figures drop at bullet explosions; fire from vessels is ineffectual due to suddenness of first volley.
- **Outcome:** Fleet limps away; one ship receives brunt of fire, appears unmanned and helpless.

# Scene 3: Disabled Ship & Loot
- **Event:** Warriors chase disabled ship; board with spears and grappling hooks.
- **Action:** Ship hauled to ground; systematic rifling of vessel.
- **Visual:** Loot includes arms, ammunition, silks, furs, jewels, stone vessels, food/water.
- **Outcome:** Ship towed out, emptied, set on fire by missile from last warrior. Drifts away as floating funeral pyre.

# Scene 4: Return & Prisoner
- **Event:** Warriors return to plaza; danger of air craft passed for a week.
- **Action:** Narrator sees prisoner dragged into building by green Martian females.
- **Visual:** Slender girlish figure, Earthly woman appearance, oval face, coal black hair, light reddish copper skin, naked except ornaments.
- **Interaction:** She looks at narrator, makes sign (appeal for help), then is dragged away. Narrator feels hope and dejection.

# Emotional Beats
- **Depression:** Narrator feels defeat of kindred people rather than routing of horde.
- **Hope:** Mixed surge of hope, fear, exultation, and depression upon seeing prisoner.
- **Regret:** Realizes he did not answer her signal for succor due to ignorance of Martian customs.
````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
task: character_extraction
version: 1

[[SECTION character_index_markdown]]
# Character Index - Chapter VIII - A Fair Captive from the Sky

| Asset ID | Canonical Character ID | Display Name | Role | Physical Presence | Description Status |
|----------|------------------------|--------------|------|-------------------|-------------------|
| narrator | CH001_NARRATOR | The Narrator | Observer/Investigator | Referenced | Manual description required |
| green_martian_females | CH001_GREEN_MARTIAN_FEMALES | Green Martian Females | Warriors/Captors | Referenced | Manual description required |
| earthly_woman_prisoner | CH001_EARTHLY_WOMAN_PRISONER | Earthly Woman / Prisoner | Captive/Subject | Physically Present | Fully identified |
| green_warriors | CH001_GREEN_WARRIORS | Green Warriors | Combatants | Referenced | Manual description required |

**Notes:**
- All characters except the prisoner lack sufficient physical description for dependable image generation
- The narrator's identity is stable but physically undefined in source material
- Martian warriors appear as a group without individual differentiation
- Prisoner has detailed visual description but may require cultural clarification
[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: narrator
canonical_character_id: CH001_NARRATOR
aliases: 
is_fully_identified: true
manual_description_required: true
manual_description_reason: No physical description provided in chapter summary; only role as observer/investigator from upper floor window is documented. Cannot support dependable image generation without manual description.
clarification_required: false
clarification_reason: 
clarification_question: 

[[SECTION markdown]]
# The Narrator

**Chapter Role:** Observer / Investigator  
**Physical Presence:** Referenced (not physically present in scenes)  

## Physical Description
*No physical description provided in source material.*

## Costume & Silhouette
*Unknown - no visual documentation available.*

## Continuity-Critical Traits
- Observes events from upper floor window
- Investigates cause of Martians' sudden retreat
- Witnesses prisoner being dragged into building
- Experiences mixed emotions: hope, fear, exultation, depression
- Feels defeat of kindred people rather than routing of horde

## Render-Facing Prompt Notes
**Uncertainty:** Physical appearance completely undefined in source. Any image generation would require manual description specification.  
**Key Phrases for Later Use:** "observer from upper floor," "witness to Martian events," "investigator of sudden retreat"

## Important Notes
This character's physical identity is stable (narrator role) but visually undefined. Manual description required before any image generation can proceed reliably.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: green_martian_females
canonical_character_id: CH001_GREEN_MARTIAN_FEMALES
aliases: 
is_fully_identified: false
manual_description_required: true
manual_description_reason: Only described as "green" in chapter summary. No detailed physical features, facial structure, or individual characteristics documented. Insufficient for dependable image generation without manual description.
clarification_required: true
clarification_reason: Character may already exist under different name or cultural designation; "green" descriptor alone is too weak for stable identification across reruns.
clarification_question: What specific physical features distinguish these green Martian females from other Martians? Are there additional descriptive terms beyond "green"?

[[SECTION markdown]]
# Green Martian Females

**Chapter Role:** Warriors / Captors  
**Physical Presence:** Referenced (not individually present)  

## Physical Description
*Only described as "green" in source material. No detailed physical features documented.*

## Costume & Silhouette
*Unknown - no visual documentation available beyond color descriptor.*

## Continuity-Critical Traits
- Fire volley from building windows facing valley
- Drag prisoner into building with green Martian females
- Board disabled ship with spears and grappling hooks
- Systematically rifle vessel for loot
- Set disabled ship on fire as floating funeral pyre

## Render-Facing Prompt Notes
**Uncertainty:** Physical appearance extremely limited. "Green" is only documented feature.  
**Key Phrases for Later Use:** "green Martian females," "warriors from building windows," "captors of prisoner"

## Important Notes
- Character identification too weak for stable reruns without clarification
- May already exist under different cultural name or designation
- Manual description required before any image generation can proceed reliably
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: earthly_woman_prisoner
canonical_character_id: CH001_EARTHLY_WOMAN_PRISONER
aliases: prisoner, captive, Earthly woman
is_fully_identified: true
manual_description_required: false
manual_description_reason: Detailed physical description provided in source material. Supports dependable image generation without manual description.
clarification_required: false
clarification_reason: 
clarification_question: 

[[SECTION markdown]]
# Earthly Woman / Prisoner

**Chapter Role:** Captive / Subject  
**Physical Presence:** Physically Present (dragged into building by warriors)  

## Physical Description
- Slender girlish figure
- Earthly woman appearance
- Oval face
- Coal black hair
- Light reddish copper skin
- Naked except ornaments

## Costume & Silhouette
- Wears only ornaments (no clothing documented)
- Girlish silhouette
- Ornamented body

## Continuity-Critical Traits
- Looks at narrator from building window
- Makes sign of appeal for help
- Dragged away by green Martian females
- Narrator feels hope and dejection upon seeing her
- Represents mixed emotions: hope, fear, exultation, depression in narrator

## Render-Facing Prompt Notes
**Key Phrases for Later Use:** "slender girlish figure," "oval face with coal black hair," "light reddish copper skin," "naked except ornaments," "Earthly woman appearance"  
**Uncertainty:** Cultural context of ornaments and their significance may require clarification

## Important Notes
- Fully identified character with sufficient physical description for image generation
- May require cultural clarification regarding ornament types and meanings
- Emotional significance to narrator is well-documented
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: green_warriors
canonical_character_id: CH001_GREEN_WARRIORS
aliases: 
is_fully_identified: false
manual_description_required: true
manual_description_reason: Only described as "green figures" in source material. No detailed physical features, facial structure, or individual characteristics documented. Insufficient for dependable image generation without manual description.
clarification_required: true
clarification_reason: Character may already exist under different name or cultural designation; "green figures" descriptor alone is too weak for stable identification across reruns.
clarification_question: What specific physical features distinguish these green warriors from other Martians? Are there additional descriptive terms beyond "green"?

[[SECTION markdown]]
# Green Warriors

**Chapter Role:** Combatants / Fleet Operators  
**Physical Presence:** Referenced (not individually present)  

## Physical Description
*Only described as "green figures" in source material. No detailed physical features documented.*

## Costume & Silhouette
*Unknown - no visual documentation available beyond color descriptor.*

## Continuity-Critical Traits
- Fire terrific volley from building windows facing valley
- Air fleet returns fire with guns
- Ships move parallel to firing line then turn back
- Chase disabled ship; board with spears and grappling hooks
- Systematically rifle vessel for loot (arms, ammunition, silks, furs, jewels, stone vessels, food/water)
- Set disabled ship on fire as floating funeral pyre

## Render-Facing Prompt Notes
**Uncertainty:** Physical appearance extremely limited. "Green figures" is only documented feature.  
**Key Phrases for Later Use:** "green warriors," "combatants from building windows," "boarders of disabled ship," "riflers of vessel loot"

## Important Notes
- Character identification too weak for stable reruns without clarification
- May already exist under different cultural name or designation
- Manual description required before any image generation can proceed reliably
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
