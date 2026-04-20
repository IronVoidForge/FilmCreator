# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-20T00:58:15.522366+00:00
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

Chapter id: CH008

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

# Chapter Summary: CH008 - A Fair Captive From The Sky

## Scene 1: Return & Enemy Fleet Arrival
- **Action:** Narrator and Sola return to the deserted city after the incubation ceremony. Martians retreat immediately upon sighting enemy airships.
- **Visual Continuity:**
    - **Martian Warriors:** Green, melting into doorways like mist.
    - **Enemy Vessels:** Huge craft, long, low, gray-painted, swinging over hill crests.
    - **Quantity:** Twenty vessels advancing majestically toward the city.
- **Outcome:** Immediate hasty return ordered; Martians fire volley from windows as ships approach.

## Scene 2: Battle Observation & Naval Engagement
- **Action:** Narrator climbs to an upper floor window to observe the cause of retreat. A naval battle ensues between city defenders and enemy fleet.
- **Visual Continuity:**
    - **Enemy Ships:** Each carries a strange banner; odd devices gleam on prows. Figures crowd forward decks.
    - **Fire Exchange:** Martians fire from building windows; enemy ships return fire with guns.
    - **Accuracy:** Narrator notes deadly accuracy of Martians (little figure drops at each explosion); enemy fire ineffectual due to suddenness.
    - **Damage:** Foremost vessel swings broadside, others follow in wake. Several craft limping perceptibly.
- **Outcome:** Enemy fleet retreats trailing off; one ship disabled and drifting.

## Scene 3: Capture of Disabled Vessel & Looting
- **Action:** Warriors capture the unmanned drifting ship. Systematic rifling of vessel occurs over several hours.
- **Visual Continuity:**
    - **Ship Status:** Drifting fifty feet above ground, bodies of crew strewn about, no sign of life.
    - **Capture Method:** Warriors swarm from windows with great spears; grappling hooks used to haul boat to ground.
    - **Loot Contents:** Arms, ammunition, silks, furs, jewels, strangely carved stone vessels, solid foods/liquids, casks of water.
    - **Disposal:** Warriors empty carboys over dead sailors/decks; ship set on fire with missile.
- **Outcome:** Ship burns as floating funeral pyre, drifting southeast until lost in distance.

## Scene 4: Narrator's Depression & Prisoner Discovery
- **Action:** Narrator descends to street feeling depressed about the defeat of a kindred people. Lorquas Ptomel keeps caravan safe in city due to fear of attack.
- **Visual Continuity:**
    - **Atmosphere:** Awe-inspiring sight of floating funeral pyre; narrator feels strange yearning toward unknown foemen.
    - **Prisoner Entry:** Human woman dragged into nearby building by Green Martian females.
    - **Physical Description:** Slender, girlish figure; oval face, beautiful features; coal black waving hair; light reddish copper skin; naked save for highly wrought ornaments.
    - **Interaction:** Woman makes sign (appeal for succor); narrator fails to respond due to ignorance of customs.
- **Outcome:** Woman dragged away into depths of deserted edifice in dejection and contempt.
````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
task: character_extraction
version: 1

[[SECTION character_index_markdown]]
# Character Index - Chapter CH008

| Character | Role | Physical Presence | Description Status |
|-----------|------|-------------------|-------------------|
| Narrator | POV Character | Present | No physical description in source |
| Sola | Companion | Referenced | No physical description in source |
| Martian Warriors | Enemy Combatants | Present | Green, mist-like appearance |
| Lorquas Ptomel | Caravan Keeper | Referenced | Named, no physical description |
| Human Woman Prisoner | Captive | Present | Detailed visual description provided |

**Notes:**
- Narrator and Sola lack physical descriptions for image generation
- Martian Warriors have group-level visual traits but not individual details
- Lorquas Ptomel is identified by name only
- Human Woman Prisoner has complete visual documentation
[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: narrator_ch008
canonical_character_id: narrator
aliases: 
is_fully_identified: false
manual_description_required: true
manual_description_reason: No physical description provided in chapter text; cannot generate reliable images without additional visual documentation
clarification_required: true
clarification_reason: Character is unnamed POV figure with no established identity beyond narrative role
clarification_question: What are the narrator's physical characteristics (age, build, hair color, skin tone, distinguishing features)?

[[SECTION markdown]]
# Narrator - Chapter CH008

**Display Name:** Narrator  
**Chapter Role:** Point-of-View Character  

**Physical Presence:** Present (narrative POV)  

**Physical Description:** Not provided in source material. No visual details available for image generation.  

**Costume/Silhouette:** Unknown; no clothing or silhouette information given in chapter text.  

**Continuity-Critical Traits:** None documented in this chapter.  

**Uncertainty Notes:** This character lacks any physical description in the supplied chapter material. Cannot generate reliable images without additional visual documentation. Manual description required for later render-facing work.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: sola_ch008
canonical_character_id: sola
aliases: 
is_fully_identified: false
manual_description_required: true
manual_description_reason: Character is mentioned only by name with no physical description provided in chapter text; cannot generate reliable images without additional visual documentation
clarification_required: true
clarification_reason: Companion character lacks established identity and physical appearance beyond name reference
clarification_question: What are Sola's physical characteristics (age, build, hair color, skin tone, distinguishing features)?

[[SECTION markdown]]
# Sola - Chapter CH008

**Display Name:** Sola  
**Chapter Role:** Companion Character  

**Physical Presence:** Referenced (returns with narrator)  

**Physical Description:** Not provided in source material. No visual details available for image generation.  

**Costume/Silhouette:** Unknown; no clothing or silhouette information given in chapter text.  

**Continuity-Critical Traits:** None documented in this chapter.  

**Uncertainty Notes:** This character is mentioned only by name with no physical description in the supplied chapter material. Cannot generate reliable images without additional visual documentation. Manual description required for later render-facing work.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: martian_warriors_ch008
canonical_character_id: martian_warrior
aliases: green_martians, martian_females
is_fully_identified: false
manual_description_required: true
manual_description_reason: Group-level visual traits only (green, mist-like) without individual physical descriptions; cannot generate reliable images of specific warriors without additional visual documentation
clarification_required: true
clarification_reason: Multiple unnamed warrior figures with group-level appearance but no established individual identities or detailed physical characteristics
clarification_question: What are the specific physical characteristics of individual Martian warriors (age range, build variations, hair color, skin tone details, distinguishing features)?

[[SECTION markdown]]
# Martian Warriors - Chapter CH008

**Display Name:** Martian Warriors  
**Chapter Role:** Enemy Combatants  

**Physical Presence:** Present (multiple figures throughout scenes)  

**Physical Description:** Green-skinned; described as "melting into doorways like mist" or "Green Martian females." Group-level visual traits only.  

**Costume/Silhouette:** No specific clothing details provided in chapter text. Silhouette suggests fluid, mist-like quality.  

**Continuity-Critical Traits:** Green skin tone; mist/melting appearance; some are female (Martian females).  

**Uncertainty Notes:** Only group-level visual traits documented (green, mist-like appearance). Individual physical descriptions not provided in source material. Cannot generate reliable images of specific warriors without additional visual documentation. Manual description required for later render-facing work.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: lorquas_ptomel_ch008
canonical_character_id: lorquas_ptomel
aliases: 
is_fully_identified: true
manual_description_required: true
manual_description_reason: Character has stable name identification but no physical description provided in chapter text; cannot generate reliable images without additional visual documentation
clarification_required: true
clarification_reason: Named character lacks established physical appearance beyond name reference
clarification_question: What are Lorquas Ptomel's physical characteristics (age, build, hair color, skin tone, distinguishing features)?

[[SECTION markdown]]
# Lorquas Ptomel - Chapter CH008

**Display Name:** Lorquas Ptomel  
**Chapter Role:** Caravan Keeper  

**Physical Presence:** Referenced (keeps caravan safe in city)  

**Physical Description:** Not provided in source material. No visual details available for image generation.  

**Costume/Silhouette:** Unknown; no clothing or silhouette information given in chapter text.  

**Continuity-Critical Traits:** None documented in this chapter.  

**Uncertainty Notes:** This character is identified by stable name but lacks any physical description in the supplied chapter material. Cannot generate reliable images without additional visual documentation. Manual description required for later render-facing work.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: human_woman_prisoner_ch008
canonical_character_id: human_woman_prisoner
aliases: captive, prisoner
is_fully_identified: true
manual_description_required: false
manual_description_reason: Detailed physical description provided in source material (slender girlish figure; oval face with beautiful features; coal black waving hair; light reddish copper skin; naked save for highly wrought ornaments); sufficient visual documentation exists for reliable image generation
clarification_required: false
clarification_reason: Character has complete visual identification and stable appearance documented in chapter text
clarification_question: 

[[SECTION markdown]]
# Human Woman Prisoner - Chapter CH008

**Display Name:** Human Woman Prisoner  
**Chapter Role:** Captive  

**Physical Presence:** Present (dragged into building by Green Martian females)  

**Physical Description:** Slender, girlish figure; oval face with beautiful features; coal black waving hair; light reddish copper skin; naked save for highly wrought ornaments.  

**Costume/Silhouette:** No clothing except "highly wrought ornaments"; nude appearance with decorative jewelry/ornaments.  

**Continuity-Critical Traits:** Coal black hair; light reddish copper skin tone; slender girlish build; oval face shape; beautiful features; ornamental jewelry.  

**Uncertainty Notes:** Complete visual description provided in source material. No uncertainty flags for physical characteristics. Sufficient documentation exists for reliable image generation without manual description requirement.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
