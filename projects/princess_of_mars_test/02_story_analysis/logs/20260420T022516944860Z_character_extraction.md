# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-20T02:25:16.944860+00:00
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

Chapter id: CH011

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

# Chapter Summary: CHAPTER XI

## Visual Continuity Facts
- **New Quarters Location:** Building near the audience chamber; second floor overlooking the plaza.
- **Room Architecture:** Ancient beds of highly wrought metal swinging from enormous gold chains depending from marble ceilings. Elaborate wall decoration portraying human figures (fair-haired Martians in robes).
- **Character Positions:** John Carter stands protectively over Dejah Thoris; Sola acts as guide/protector; Sarkoja descends outside the quarters eavesdropping.
- **Artifacts:** Accouterments carried by John Carter (metal weapon); bedding and food utensils brought by Sola.

## Broad Story Summary
- **Arrival & Threat:** John Carter arrives with Dejah Thoris and Sola. Sarkoja attempts to assume custody of Dejah Thoris; John waves her away and threatens her demise for harming Dejah. The threat fails on Mars (men do not kill women).
- **Hierarchy Discussion:** John explains his rank as 11th chieftain to Sola. Discusses the requirement to kill Lorquas Ptomel for first place (combat or self-defense).
- **Origin Conversation:** Dejah Thoris questions John's origin, noting he speaks her language but claims recent learning. She asks if he is from Valley Dor (where a different language is spoken). He denies it, stating he is from Earth (Virginia).
- **Earth Knowledge:** Dejah expresses curiosity about Earth customs and geography. She explains Martian viewing technology allows them to see Earth events on screens.
- **Room Inspection:** John and Dejah examine the new quarters' architecture and frescoes. Dejah is captivated by the art of extinct fair-haired Martians; Sola does not notice them.
- **History Lesson:** Dejah Thoris explains Martian race mixing (Red, Dark, Yellow) due to alliance against Green Men and drying seas. Discusses lost civilization of ancient Barsoomians and the city's history as Korad.
- **Sola's Return:** Sola returns with bedding and supplies. Sarkoja is seen descending outside; they suspect eavesdropping but dismiss it for now.
- **End Scene:** John receives a summons from Lorquas Ptomel to appear in the audience chamber immediately. He bids Dejah Thoris and Sola farewell and commands Woola to remain on guard.
````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
task: character_extraction
version: 1

[[SECTION character_index_markdown]]
# Character Index - Chapter XI

| Asset ID | Canonical Character ID | Aliases | Fully Identified | Manual Description Required |
|----------|------------------------|---------|------------------|------------------------------|
| john_carter | John Carter | - | true | true |
| dejah_thoris | Dejah Thoris | - | true | true |
| sola | Sola | - | true | true |
| sarkoja | Sarkoja | - | true | true |
| woola | Woola | - | false | true |

*Note: All characters lack sufficient physical description in this chapter for dependable image generation.*
[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: john_carter
canonical_character_id: John Carter
aliases: 
is_fully_identified: true
manual_description_required: true
manual_description_reason: No physical description provided in Chapter XI; only actions and positions mentioned (stands protectively, carries metal weapon). Insufficient visual details for dependable image generation.
clarification_required: false
clarification_reason: 
clarification_question: 

[[SECTION markdown]]
# John Carter - Chapter XI

**Display Name:** John Carter  
**Chapter Role:** Protagonist / 11th Chieftain  
**Physical Presence:** Present (stands protectively over Dejah Thoris)  
**Physical Description:** Not detailed in this chapter. Carries accouterments including a metal weapon.  
**Costume/Silhouette:** Unknown - no visual description provided  
**Continuity-Critical Traits:** 11th chieftain rank; from Earth (Virginia); speaks Martian language but claims recent learning; does not originate from Valley Dor  

**Uncertainty Notes:** 
- Physical appearance, height, build, and facial features are not described in this chapter
- Costume details beyond carrying a metal weapon are unknown
- Visual continuity must be established through external sources or manual description

**Useful Noun Phrases for Render Prompts:**
"protective stance", "metal weapon accouterments", "11th chieftain rank", "Earth origin", "Martian language speaker"
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: dejah_thoris
canonical_character_id: Dejah Thoris
aliases: 
is_fully_identified: true
manual_description_required: true
manual_description_reason: No physical description provided in Chapter XI; only actions and positions mentioned (examines quarters, captivated by art). Insufficient visual details for dependable image generation.
clarification_required: false
clarification_reason: 
clarification_question: 

[[SECTION markdown]]
# Dejah Thoris - Chapter XI

**Display Name:** Dejah Thoris  
**Chapter Role:** Female Lead / Martian Noble  
**Physical Presence:** Present (examines quarters with John Carter)  
**Physical Description:** Not detailed in this chapter. Captivated by ancient fair-haired Martian art.  
**Costume/Silhouette:** Unknown - no visual description provided  
**Continuity-Critical Traits:** Martian noble; questions John's origin; interested in Earth customs and geography; knowledgeable about Martian viewing technology; understands race mixing history (Red, Dark, Yellow Martians)  

**Uncertainty Notes:** 
- Physical appearance, height, build, and facial features are not described in this chapter
- Costume details beyond being a Martian noble are unknown
- Visual continuity must be established through external sources or manual description

**Useful Noun Phrases for Render Prompts:**
"Martian noble", "captivated by ancient art", "interested in Earth customs", "knowledgeable about race mixing history", "fair-haired Martian art enthusiast"
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: sola
canonical_character_id: Sola
aliases: 
is_fully_identified: true
manual_description_required: true
manual_description_reason: No physical description provided in Chapter XI; only actions and positions mentioned (acts as guide/protector, returns with bedding). Insufficient visual details for dependable image generation.
clarification_required: false
clarification_reason: 
clarification_question: 

[[SECTION markdown]]
# Sola - Chapter XI

**Display Name:** Sola  
**Chapter Role:** Guide / Protector Figure  
**Physical Presence:** Present (guides John and Dejah, returns with supplies)  
**Physical Description:** Not detailed in this chapter. Does not notice ancient frescoes that captivate Dejah.  
**Costume/Silhouette:** Unknown - no visual description provided  
**Continuity-Critical Traits:** Guide/protector role; brings bedding and food utensils; does not notice ancient fair-haired Martian art (unlike Dejah); returns with supplies  

**Uncertainty Notes:** 
- Physical appearance, height, build, and facial features are not described in this chapter
- Costume details are unknown
- Visual continuity must be established through external sources or manual description

**Useful Noun Phrases for Render Prompts:**
"guide figure", "protector role", "brings bedding and supplies", "does not notice ancient art", "practical helper"
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: sarkoja
canonical_character_id: Sarkoja
aliases: 
is_fully_identified: true
manual_description_required: true
manual_description_reason: No physical description provided in Chapter XI; only actions and positions mentioned (descends outside eavesdropping). Insufficient visual details for dependable image generation.
clarification_required: false
clarification_reason: 
clarification_question: 

[[SECTION markdown]]
# Sarkoja - Chapter XI

**Display Name:** Sarkoja  
**Chapter Role:** Antagonist / Custody Seeker  
**Physical Presence:** Present (outside eavesdropping from quarters)  
**Physical Description:** Not detailed in this chapter. Attempts to assume custody of Dejah Thoris; threatened by John Carter but threat fails on Mars.  
**Costume/Silhouette:** Unknown - no visual description provided  
**Continuity-Critical Traits:** Antagonist role; attempts custody over Dejah Thoris; eavesdrops from outside quarters; dismissed as threat for now  

**Uncertainty Notes:** 
- Physical appearance, height, build, and facial features are not described in this chapter
- Costume details are unknown
- Visual continuity must be established through external sources or manual description

**Useful Noun Phrases for Render Prompts:**
"antagonist figure", "custody seeker", "eavesdropping outside", "threatened by John Carter", "dismissed threat for now"
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: woola
canonical_character_id: Woola
aliases: 
is_fully_identified: false
manual_description_required: true
manual_description_reason: No physical description provided in Chapter XI; only mentioned at end scene ("remains on guard"). Insufficient visual details for dependable image generation.
clarification_required: true
clarification_reason: Character is weakly identified - only referenced at chapter's conclusion without prior introduction or detailed description. May already exist under another name or be too weakly identified for reliable continuity.
clarification_question: Is Woola a previously established character with known physical attributes, or should this be treated as a new character requiring full manual description?

[[SECTION markdown]]
# Woola - Chapter XI

**Display Name:** Woola  
**Chapter Role:** Guard / Companion Figure  
**Physical Presence:** Referenced only (not physically present in scene)  
**Physical Description:** Not detailed in this chapter. Commanded to remain on guard after John's departure.  
**Costume/Silhouette:** Unknown - no visual description provided  
**Continuity-Critical Traits:** Guard role; remains on duty while John Carter departs for audience chamber summons  

**Uncertainty Notes:** 
- Physical appearance, height, build, and facial features are not described in this chapter
- Costume details are unknown
- Character is weakly identified - only mentioned at chapter's conclusion without prior introduction
- Visual continuity must be established through external sources or manual description

**Useful Noun Phrases for Render Prompts:**
"guard figure", "remains on duty", "companion to John Carter", "on guard after departure"
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
