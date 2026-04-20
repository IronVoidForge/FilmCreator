# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-20T01:25:02.667238+00:00
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

Chapter id: CH017

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

# Chapter Summary: CHAPTER XVII - A COSTLY RECAPTURE

## Plot Beats

### Beat 1: The Rescue in Thark City
John Carter overhears Tal Hajus's plan to torture Dejah Thoris for ten days and claim her for one hour. Upon hearing this, Carter kills Tal Hajus with a punch while protecting Dejah Thoris from the jeddak's grasp. He rescues Dejah Thoris and Sola from the unlighted third floor of the building using straps and leather trappings, lowering them to the ground below. They escape the city of Thark through the courtyard on their thoats, heading south towards Helium.

### Beat 2: The Journey Through the Waste
The party travels through the mossy waste but gets lost due to lack of waterways. Woola joins them after sleeping near Carter. They suffer from exhaustion and hunger. One of the two thoats collapses and is left behind; they continue with one beast, walking while Dejah Thoris rides.

### Beat 3: The Pursuit by Thark Warriors
While traveling towards the hills, they spot a party of mounted Thark warriors heading southwesterly. Carter shoots a chieftain using his rifle, but is immediately pursued by the remaining warriors (some thousand men). Dejah Thoris sacrifices herself to save Carter, staying behind to die with him while he fights off the green warriors alone.

### Beat 4: The Capture
Carter fights the pursuing warriors alone, firing until his rifle is empty. He is eventually struck by a projecting piece of quartz and falls. Despite drawing his long-sword, he is overwhelmed by the torrent of blows from the green warriors and goes down to oblivion, captured by them.

## Visual Continuity Facts

### Locations
- **Thark City:** Courtyard, third floor windows, inner chamber with raised platform, winding runway.
- **Mossy Waste:** Yellow moonlit moss, hills, ridges, passes, sea bottom (flat terrain).
- **Helium:** Mentioned as the destination and home of Dejah Thoris's people.

### Character States & Objects
- **John Carter:** Armed with rifle, revolvers, sword; determined but exhausted; eventually captured.
- **Dejah Thoris:** Riding thoat; injured/threatened; sacrifices herself to save Carter.
- **Sola:** Riding thoat; loyal companion; follows Carter's commands.
- **Woola:** Faithful beast; joins the party after sleeping near Carter.
- **Tal Hajus:** Dead jeddak; killed by Carter.
- **Thoats:** Two beasts initially; one collapses and is left behind due to exhaustion.
- **Weapons:** Rifle (empty), revolvers, long-sword, fieldglass.

### Environmental Details
- **Terrain:** Yellow moss, hills, ridges, passes, waterways (missing).
- **Lighting:** Moonlit nights, daylight travel.
- **Atmosphere:** Tense pursuit, exhaustion, sacrifice, danger of capture.
````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
task: character_extraction
version: 1
[[SECTION character_index_markdown]]
# Chapter XVII Character Index

| Asset ID | Canonical Name | Role in Chapter | Physical Presence |
| :--- | :--- | :--- | :--- |
| john_carter | John Carter | Protagonist, Rescue Leader | Present (Active) |
| dejah_thoris | Dejah Thoris | Love Interest, Sacrifice | Present (Riding) |
| sola | Sola | Companion, Loyalist | Present (Riding) |
| woola | Woola | Faithful Beast | Present (Joined) |
| tal_hajus | Tal Hajus | Antagonist, Dead Jeddak | Referenced (Dead) |

*Note: Physical descriptions are flagged as requiring manual input due to lack of specific visual details in the source text.*
[[/SECTION]]
[[FILMCREATOR_RECORD]]
type: character
asset_id: john_carter
canonical_character_id: John Carter
aliases: 
is_fully_identified: true
manual_description_required: true
manual_description_reason: The chapter summary lacks specific physical descriptors such as complexion, hair style, or facial features required for reliable image generation.
clarification_required: false
clarification_reason: 
clarification_question: 
[[SECTION markdown]]
# John Carter

**Display Name:** John Carter  
**Chapter Role:** Protagonist / Rescue Leader  

**Physical Presence:** Physically present and active throughout the chapter (Beat 1-4).  

**Supported Physical Description:** Armed with rifle, revolvers, sword; determined but exhausted. Eventually captured by Thark warriors.  

**Costume & Silhouette:** Wearing attire suitable for travel/combat on Barsoom (implied). Silhouette defined by weaponry and exhaustion.  

**Continuity-Critical Traits:**  
- **Weaponry:** Rifle (empty), revolvers, long-sword, fieldglass.  
- **State:** Exhausted, determined, captured.  
- **Action:** Kills Tal Hajus, rescues Dejah Thoris/Sola, fights pursuing warriors alone.  

**Uncertainty Notes:** Specific physical features (complexion, height, hair) are not detailed in the provided text and require manual description for image generation.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]
[[FILMCREATOR_RECORD]]
type: character
asset_id: dejah_thoris
canonical_character_id: Dejah Thoris
aliases: 
is_fully_identified: true
manual_description_required: true
manual_description_reason: The chapter summary lacks specific physical descriptors such as complexion, hair style, or facial features required for reliable image generation.
clarification_required: false
clarification_reason: 
clarification_question: 
[[SECTION markdown]]
# Dejah Thoris

**Display Name:** Dejah Thoris  
**Chapter Role:** Love Interest / Sacrifice  

**Physical Presence:** Physically present and active throughout the chapter (Beat 1-4).  

**Supported Physical Description:** Riding thoat; injured/threatened. Sacrifices herself to save Carter.  

**Costume & Silhouette:** Attire suitable for riding/combat on Barsoom (implied). Silhouette defined by riding posture and vulnerability.  

**Continuity-Critical Traits:**  
- **Mount:** Riding a thoat.  
- **State:** Injured, threatened, sacrificial.  
- **Action:** Protected by Carter, sacrifices herself to save him from Thark warriors.  

**Uncertainty Notes:** Specific physical features (complexion, height, hair) are not detailed in the provided text and require manual description for image generation.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]
[[FILMCREATOR_RECORD]]
type: character
asset_id: sola
canonical_character_id: Sola
aliases: 
is_fully_identified: true
manual_description_required: true
manual_description_reason: The chapter summary lacks specific physical descriptors such as complexion, hair style, or facial features required for reliable image generation.
clarification_required: false
clarification_reason: 
clarification_question: 
[[SECTION markdown]]
# Sola

**Display Name:** Sola  
**Chapter Role:** Companion / Loyalist  

**Physical Presence:** Physically present and active throughout the chapter (Beat 1-4).  

**Supported Physical Description:** Riding thoat; loyal companion. Follows Carter's commands.  

**Costume & Silhouette:** Attire suitable for riding/combat on Barsoom (implied). Silhouette defined by riding posture and loyalty.  

**Continuity-Critical Traits:**  
- **Mount:** Riding a thoat.  
- **State:** Loyal, obedient.  
- **Action:** Joins Carter's escape, follows commands during pursuit.  

**Uncertainty Notes:** Specific physical features (complexion, height, hair) are not detailed in the provided text and require manual description for image generation.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]
[[FILMCREATOR_RECORD]]
type: character
asset_id: woola
canonical_character_id: Woola
aliases: 
is_fully_identified: true
manual_description_required: true
manual_description_reason: The chapter summary lacks specific physical descriptors such as complexion, hair style, or facial features required for reliable image generation.
clarification_required: false
clarification_reason: 
clarification_question: 
[[SECTION markdown]]
# Woola

**Display Name:** Woola  
**Chapter Role:** Faithful Beast  

**Physical Presence:** Physically present and active throughout the chapter (Beat 1-4).  

**Supported Physical Description:** Faithful beast; joins the party after sleeping near Carter.  

**Costume & Silhouette:** Natural beast form (likely canine-like based on context, but unspecified in text). Silhouette defined by animalistic movement.  

**Continuity-Critical Traits:**  
- **State:** Faithful, exhausted.  
- **Action:** Sleeps near Carter, joins the party during escape.  

**Uncertainty Notes:** Specific physical features (species details, size, markings) are not detailed in the provided text and require manual description for image generation.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]
[[FILMCREATOR_RECORD]]
type: character
asset_id: tal_hajus
canonical_character_id: Tal Hajus
aliases: 
is_fully_identified: true
manual_description_required: true
manual_description_reason: The chapter summary lacks specific physical descriptors such as complexion, hair style, or facial features required for reliable image generation.
clarification_required: false
clarification_reason: 
clarification_question: 
[[SECTION markdown]]
# Tal Hajus

**Display Name:** Tal Hajus  
**Chapter Role:** Antagonist / Dead Jeddak  

**Physical Presence:** Referenced as dead throughout the chapter (Beat 1).  

**Supported Physical Description:** Dead jeddak; killed by Carter with a punch.  

**Costume & Silhouette:** Attire of a jeddak (implied). Silhouette defined by death and lack of movement.  

**Continuity-Critical Traits:**  
- **State:** Dead, captured/killed.  
- **Action:** Planned to torture Dejah Thoris; killed by Carter to save her.  

**Uncertainty Notes:** Specific physical features (complexion, height, hair) are not detailed in the provided text and require manual description for image generation.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]
[[/FILMCREATOR_PACKET]]
````
