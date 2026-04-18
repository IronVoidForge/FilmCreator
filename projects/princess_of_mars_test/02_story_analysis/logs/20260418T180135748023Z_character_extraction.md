# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-18T18:01:35.748522+00:00
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

# Chapter Label
Chapter VIII - A Fair Captive from the Sky

# Story Summary
The procession returns home after the incubator ceremony but is ordered back immediately upon seeing a fleet of airships approaching. The narrator observes from an upper floor window as twenty gray-painted vessels sail toward the city. Green Martian warriors fire a volley from building windows, engaging the ships. The fleet returns fire and maneuvers to complete circles before retreating. One ship is disabled and drifting southeast. Warriors chase it, board with spears and grappling hooks, and loot the vessel of arms, jewels, water, and food. They empty carboys onto the dead crew and burn the ship as a funeral pyre. The narrator witnesses the burning from the roof until it drifts into the distance. Depressed by the defeat of a kindred people's forces, he descends to the street. In the plaza, he sees a prisoner being dragged into a building. He catches a glimpse of her before she enters: a slender, girlish figure with coal black hair and reddish copper skin. She looks at him with hope then dejection as she is dragged away.

# Visual Continuity Facts
- **Location:** Upper floor window (observation point), Plaza (encounter point).
- **Martian Warriors:** Green skin, erect walking, wear spears, banners, ornaments.
- **Airships:** Gray-painted, long, low, twenty total, carry strange devices on prow/stem.
- **Combat Visuals:** Figures drop at bullet explosions; banners dissolve in flame; ships swing broadside.
- **Prisoner Appearance:** Slender girlish figure, oval face, finely chiseled features, large lustrous eyes, coal black waving hair (loose coiffure), light reddish copper skin, crimson cheeks, ruby lips.
- **Attire:** Destitute of clothes, entirely naked save for highly wrought ornaments.
- **Height Comparison:** Prisoner considerably less than half as tall as green Martian warriors.
- **Movement:** Walks erect upon two legs; dragged by females into building.
- **Environment:** Deserted city buildings, open ground/plaza, valley/hills vista.
]]
````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
task: character_extraction
version: 1

[[SECTION character_index_markdown]]
# Character Index - Chapter VIII - A Fair Captive from the Sky

| Asset ID | Display Name | Chapter Role | Physical Presence | Manual Description Required |
|----------|--------------|---------------|-------------------|----------------------------|
| narrator_observing | The Narrator | Observer/Protagonist | Referenced (observes from upper floor window) | Yes - insufficient physical description for image generation |
| martian_warriors | Martian Warriors | Combatants/Antagonists | Present (firing volley, chasing ship) | Yes - group character with limited individual detail |
| prisoner_captive | The Prisoner/Captive | Central Character | Referenced (caught glimpse before entering building) | Yes - missing name and specific ornament details |

**Notes:**
- All characters require manual description due to insufficient physical/visual information for dependable image generation
- Martian Warriors function as a group character with consistent visual traits but no individual variations documented
- The Prisoner has detailed physical description but lacks identifying name and specific ornament documentation
[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: narrator_observing
canonical_character_id: narrator_observing
aliases: the_narrator, observer_from_window
is_fully_identified: false
manual_description_required: true
manual_description_reason: Insufficient physical description for image generation - only identified as "he" observing from upper floor window; missing age, facial features, clothing, build, and other visual identifiers needed for dependable rendering
clarification_required: true
clarification_reason: Character lacks stable identification beyond narrative function; needs targeted clarification on physical appearance before image generation can proceed
clarification_question: What are the narrator's specific physical characteristics (age range, facial features, hair, clothing style) that would support reliable image generation?
[[/FILMCREATOR_RECORD]]

[[SECTION markdown]]
# The Narrator - Chapter VIII - A Fair Captive from the Sky

**Display Name:** The Narrator  
**Chapter Role:** Observer/Protagonist  
**Physical Presence:** Referenced (observes events from upper floor window)  

## Physical Description (Source-Supported)
- Identified only as "he" in narrative text
- Observing position: Upper floor window, later roof

## Continuity-Critical Traits
- **Location:** Upper floor window (observation point), roof (witnesses burning)
- **Function:** Witness to Martian Warriors' engagement with airships and subsequent prisoner capture
- **Movement:** Descends from upper floor to street after witnessing events

## Visual Description Notes
**Supported by Source:** None beyond gender identification ("he")  
**Missing Information:** Age, facial features, hair, clothing style, build, distinguishing marks  
**Uncertainty:** Character lacks sufficient physical detail for dependable image generation; all visual identifiers are absent from source material  

## Render-Facing Prompt Elements
- **Noun Phrases:** "male observer," "person at window," "narrator figure"  
- **Descriptive Nouns:** "observer," "witness," "protagonist"  
- **Continuity Markers:** "upper floor position," "window viewpoint"  

## Explicit Uncertainty Notes
⚠️ **CRITICAL:** No physical description provided in source material beyond gender identification. Character cannot be reliably rendered for image generation without manual description intervention. All visual identifiers (age, facial features, clothing, build) are completely absent from chapter text.

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: martian_warriors
canonical_character_id: martian_warriors
aliases: green_martians, warriors, combatants
is_fully_identified: true
manual_description_required: true
manual_description_reason: Group character with consistent visual traits but no individual variations documented; insufficient detail for dependable image generation of specific warrior figures beyond general group representation
clarification_required: false
clarification_reason: Character identification is stable as a group entity with documented physical traits
clarification_question: N/A - group character with established visual continuity
[[/FILMCREATOR_RECORD]]

[[SECTION markdown]]
# Martian Warriors - Chapter VIII - A Fair Captive from the Sky

**Display Name:** Martian Warriors  
**Chapter Role:** Combatants/Antagonists  
**Physical Presence:** Present (firing volley from building windows, chasing disabled ship)  

## Physical Description (Source-Supported)
- **Skin:** Green skin
- **Posture:** Erect walking upon two legs
- **Equipment:** Wear spears, banners, ornaments
- **Height Comparison:** Prisoner considerably less than half as tall as green Martian warriors

## Continuity-Critical Traits
- **Location:** Building windows (firing position), open ground/plaza (chase location)
- **Function:** Engage airships in combat, loot disabled vessel, burn ship as funeral pyre
- **Visual Consistency:** Green skin, erect walking, spears, banners, ornaments maintained throughout chapter

## Visual Description Notes
**Supported by Source:** 
- Green skin coloration
- Erect bipedal movement
- Equipment: spears, banners, ornaments (general category)
- Height relative to prisoner documented

**Missing Information:** 
- Individual variations in appearance
- Specific ornament details beyond "highly wrought ornaments"
- Facial features or distinguishing marks
- Clothing specifics beyond general ornamentation

## Render-Facing Prompt Elements
- **Noun Phrases:** "green-skinned warrior," "Martian combatant," "figure with spear and banner"  
- **Descriptive Nouns:** "warrior," "combatant," "guard," "soldier"  
- **Continuity Markers:** "green skin," "erect walking," "spear equipment," "banner display"  

## Explicit Uncertainty Notes
⚠️ **LIMITED DETAIL:** Character is a group entity with consistent visual traits but no individual variations documented. While physical description is supported (green skin, erect movement, spears/banners/ornaments), insufficient detail exists for dependable image generation of specific warrior figures beyond general group representation. Individual ornament details and facial features are not specified in source material.

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: prisoner_captive
canonical_character_id: prisoner_captive
aliases: the_prisoner, captive, girl_from_airship
is_fully_identified: false
manual_description_required: true
manual_description_reason: Detailed physical description provided but missing identifying name and specific ornament details; insufficient for dependable image generation without manual intervention on missing identifiers
clarification_required: true
clarification_reason: Character lacks stable identification (no name) and specific visual documentation (ornament details) needed for reliable rendering
clarification_question: What is the prisoner's name or identifying designation, and what are the specific details of her ornaments (type, placement, style)?
[[/FILMCREATOR_RECORD]]

[[SECTION markdown]]
# The Prisoner/Captive - Chapter VIII - A Fair Captive from the Sky

**Display Name:** The Prisoner/Captive  
**Chapter Role:** Central Character  
**Physical Presence:** Referenced (caught glimpse before entering building)  

## Physical Description (Source-Supported)
- **Build:** Slender girlish figure
- **Face:** Oval face, finely chiseled features, large lustrous eyes
- **Hair:** Coal black waving hair (loose coiffure)
- **Skin:** Light reddish copper skin, crimson cheeks, ruby lips
- **Attire:** Destitute of clothes, entirely naked save for highly wrought ornaments

## Continuity-Critical Traits
- **Location:** Plaza (encounter point), building interior (destination)
- **Movement:** Walks erect upon two legs; dragged by females into building
- **Height Comparison:** Considerably less than half as tall as green Martian warriors
- **Emotional State:** Looks with hope then dejection

## Visual Description Notes
**Supported by Source:** 
- Slender girlish build
- Oval face with finely chiseled features
- Large lustrous eyes
- Coal black waving hair (loose coiffure)
- Light reddish copper skin tone
- Crimson cheeks, ruby lips
- Naked save for highly wrought ornaments

**Missing Information:** 
- Name or identifying designation
- Specific ornament details (type, placement, style)
- Age range
- Distinguishing marks beyond described features

## Render-Facing Prompt Elements
- **Noun Phrases:** "slender girlish figure," "oval-faced captive," "coal black haired prisoner"  
- **Descriptive Nouns:** "prisoner," "captive," "girl," "figure"  
- **Continuity Markers:** "reddish copper skin," "coal black hair," "highly wrought ornaments," "erect walking"  

## Explicit Uncertainty Notes
⚠️ **MISSING IDENTIFIERS:** While detailed physical description is provided, character lacks stable identification (no name) and specific ornament documentation. Cannot be reliably rendered for image generation without manual intervention on missing identifiers. Ornament details are specified only as "highly wrought ornaments" without specific type, placement, or style information.

[[/SECTION]]
[[/FILMCREATOR_PACKET]]
````
