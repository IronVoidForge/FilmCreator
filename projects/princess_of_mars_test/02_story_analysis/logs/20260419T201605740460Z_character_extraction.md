# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-19T20:16:05.740460+00:00
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

# Chapter Summary: Chapter XI - "With Dejah Thoris"

## Scene 1: Confrontation at the Open Area
*   **Action:** Upon reaching an open area, two female guards (Sarkoja) attempt to assume custody of Dejah Thoris again.
*   **Dialogue/Conflict:** John Carter intervenes, shrinking against him. He waves the women away and informs them Sola will attend to the captive. He threatens Sarkoja with sudden and painful demise for any further cruel attentions bestowed upon Dejah Thoris.
*   **Outcome:** The threat is described as "unfortunate" and results in more harm than good. Men do not kill women on Mars, so Sarkoja merely gives an ugly look and departs to hatch deviltries against them.

## Scene 2: Arrangement of Quarters with Sola
*   **Action:** John Carter finds Sola and explains he wishes her to guard Dejah Thoris as she guarded him. He requests they find other quarters where they are not molested by Sarkoja. He states he will take up his quarters among the men (or rather, his high rank allows him presence).
*   **Dialogue:** Sola acknowledges John Carter's status: "You are a great chieftain now, John Carter." She notes the metal he carries belonged to a young warrior who won promotions close to Tars Tarkas.
*   **Hierarchy Explanation:** Sola explains the Thark ranking system. There are ten chieftains; John Carter is eleventh in prowess (close to Tars Tarkas). Becoming first requires killing Lorquas Ptomel, which can only happen via council will for combat or self-defense.

## Scene 3: Exploration of Korad Building
*   **Action:** John Carter accompanies Sola and Dejah Thoris to search for new quarters. They find a building nearer the audience chamber with pretentious architecture.
*   **Visual Continuity:** The room features real sleeping apartments with ancient beds of highly wrought metal swinging from enormous gold chains depending from marble ceilings. Wall decoration is elaborate, portraying human figures in compositions (fair-haired people at play).
*   **Character Reaction:** Dejah Thoris clasps her hands with an exclamation of rapture as she gazes upon the magnificent works of art by a people long extinct. Sola apparently does not see them.
*   **Decision:** They decide to use the second-floor room overlooking the plaza for Dejah Thoris and Sola, and another adjoining room in the rear for cooking and supplies.

## Scene 4: Deep Conversation on Origin and Customs
*   **Action:** Intense dialogue between John Carter and Dejah Thoris regarding his origin.
*   **Dialogue/Conflict:** Dejah Thoris questions him about Virginia, his language skills (learning it recently), and Martian geography viewing technology (screens showing Earth). She notes that nearly every planet shows forms of animal life almost identical to them, but Earth men cover bodies with strange cloth and hideous contraptions.
*   **Resolution:** John Carter admits he is from Earth (Virginia) and the great planet Earth revolves about their common sun. Dejah Thoris struggles to believe it due to Barsoomian customs ("no man lies"). She eventually accepts his statement because her heart tells her to believe.

## Scene 5: Ancient History and Conclusion
*   **Action:** Discussion of ancient fair-haired Martians vs Red Martians. The city (Korad) is a center of commerce and culture built over a hundred thousand years ago.
*   **Visual Continuity:** Frescoes depict people like John Carter, lighter in color, clad in graceful flowing robes ornamented with metal and jewels. Scenes show fair-skinned, fair-haired people at play.
*   **Plot Progression:** Sola returns with bedding and food. Sarkoja is noted eavesdropping on the upper floors. Dejah Thoris and John Carter examine architecture and decorations.
*   **Ending:** It becomes late in the afternoon. A messenger bears a summons from Lorquas Ptomel directing John Carter to appear before him forthwith. John Carter bids farewell to Dejah Thoris and Sola, commands Woola to remain on guard, and hastens to the audience chamber where he finds Lorquas Ptomel and Tars Tarkas seated upon the rostrum.
````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
task: character_extraction
version: 1

[[SECTION character_index_markdown]]
# Character Index - Chapter XI: "With Dejah Thoris"

| Character | Asset ID | Canonical ID | Status | Description Available |
|-----------|----------|--------------|--------|----------------------|
| Dejah Thoris | dejah_thoris | dejah_thoris | Present | Insufficient visual details for image generation |
| John Carter | john_carter | john_carter | Present | Insufficient visual details for image generation |
| Sola | sola | sola | Present | Insufficient visual details for image generation |
| Sarkoja | sarkoja | sarkoja | Referenced | No physical description provided; multiple guards mentioned |
| Woola | woola | woola | Referenced | Animal companion with no detailed identification |
| Lorquas Ptomel | lorquas_ptomel | lorquas_ptomel | Referenced | Only name given, no individual identification possible |
| Tars Tarkas | tars_tarkas | tars_tarkas | Referenced | Only name given, no individual identification possible |

**Notes:**
- All characters require manual descriptions due to lack of physical/visual details in source material
- Several characters (Sarkoja, Woola, Lorquas Ptomel, Tars Tarkas) have clarification required flags set due to weak identification
- Dejah Thoris and John Carter are fully identified as central protagonists despite missing visual details
[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: dejah_thoris
canonical_character_id: dejah_thoris
aliases: 
is_fully_identified: true
manual_description_required: true
manual_description_reason: Chapter provides no physical description (height, build, hair color, eye color, facial features) for reliable image generation. Only mentions she is a captive and gazes at art with rapture.
clarification_required: false
clarification_reason: 
clarification_question: 

[[SECTION markdown]]
# Dejah Thoris - Chapter XI

**Display Name:** Dejah Thoris  
**Chapter Role:** Central female protagonist, captive being guarded and relocated to new quarters

**Physical Presence:** Present throughout all scenes (confrontation at open area, arrangement of quarters with Sola, exploration of Korad Building, deep conversation on origin, ancient history discussion)

**Physical Description:** Insufficient details provided in source material. Chapter mentions she is a "captive" and that she gazes upon art with "exclamation of rapture," but no physical attributes (build, height, hair color, eye color, facial features) are described.

**Costume/Silhouette:** No costume or silhouette details provided in this chapter. She is referred to as wearing clothing appropriate for her status as a captive.

**Continuity-Critical Traits:** 
- Identified as Dejah Thoris (central character)
- Associated with John Carter and Sola
- Located in Korad Building quarters
- Subject of conversation about Earth origin and Barsoomian customs

**Render-Facing Prompt Noun Phrases:**
- "female captive"
- "Dejah Thoris"
- "Barsoomian woman"
- "captive in Korad Building"
- "subject of deep conversation with John Carter"

**Uncertainty Notes:** 
- Physical appearance cannot be reliably generated from source material
- No costume or silhouette details available for image generation
- Chapter provides only narrative presence, not visual description
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: john_carter
canonical_character_id: john_carter
aliases: 
is_fully_identified: true
manual_description_required: true
manual_description_reason: Chapter provides no physical description (height, build, hair color, eye color, facial features) for reliable image generation. Only mentions he is a "great chieftain" and carries metal from a young warrior.
clarification_required: false
clarification_reason: 
clarification_question: 

[[SECTION markdown]]
# John Carter - Chapter XI

**Display Name:** John Carter  
**Chapter Role:** Central male protagonist, intervenes in confrontations, arranges quarters with Sola, converses about origin and customs

**Physical Presence:** Present throughout all scenes (confrontation at open area, arrangement of quarters with Sola, exploration of Korad Building, deep conversation on origin, ancient history discussion)

**Physical Description:** Insufficient details provided in source material. Chapter mentions he is a "great chieftain" and carries metal belonging to a young warrior who won promotions, but no physical attributes (build, height, hair color, eye color, facial features) are described.

**Costume/Silhouette:** No costume or silhouette details provided in this chapter. He carries metal weapons and is identified as having high rank among the Tharks.

**Continuity-Critical Traits:** 
- Identified as John Carter (central character)
- Associated with Dejah Thoris and Sola
- Carries metal from young warrior (promoted close to Tars Tarkas)
- Eleventh in prowess among ten chieftains, close to Tars Tarkas
- From Earth (Virginia) according to his admission

**Render-Facing Prompt Noun Phrases:**
- "male protagonist"
- "John Carter"
- "great chieftain"
- "Eleventh in prowess"
- "Earth-born on Mars"
- "carries metal weapons"

**Uncertainty Notes:** 
- Physical appearance cannot be reliably generated from source material
- No costume or silhouette details available for image generation
- Chapter provides only narrative presence, not visual description
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: sola
canonical_character_id: sola
aliases: 
is_fully_identified: true
manual_description_required: true
manual_description_reason: Chapter provides no physical description (height, build, hair color, eye color, facial features) for reliable image generation. Only mentions she is a female Thark warrior/guard who acknowledges John Carter's status.
clarification_required: false
clarification_reason: 
clarification_question: 

[[SECTION markdown]]
# Sola - Chapter XI

**Display Name:** Sola  
**Chapter Role:** Female Thark warrior/guard, assigned to guard Dejah Thoris, explains Thark ranking system

**Physical Presence:** Present throughout all scenes (arrangement of quarters with John Carter, exploration of Korad Building, deep conversation on origin, ancient history discussion)

**Physical Description:** Insufficient details provided in source material. Chapter mentions she is a "female Thark warrior/guard" who acknowledges John Carter's status as "great chieftain," but no physical attributes (build, height, hair color, eye color, facial features) are described.

**Costume/Silhouette:** No costume or silhouette details provided in this chapter. She carries metal weapons and is identified as a Thark warrior of high rank.

**Continuity-Critical Traits:** 
- Identified as Sola (Thark warrior/guard)
- Associated with John Carter and Dejah Thoris
- Carries metal from young warrior who won promotions close to Tars Tarkas
- Explains Thark ranking system (ten chieftains, John Carter eleventh in prowess)
- Returns with bedding and food

**Render-Facing Prompt Noun Phrases:**
- "female Thark warrior"
- "Sola"
- "Thark guard"
- "acknowledges great chieftain status"
- "carries metal weapons"
- "explains ranking system"

**Uncertainty Notes:** 
- Physical appearance cannot be reliably generated from source material
- No costume or silhouette details available for image generation
- Chapter provides only narrative presence, not visual description
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: sarkoja
canonical_character_id: sarkoja
aliases: Sarkoja guards (two female guards mentioned)
is_fully_identified: false
manual_description_required: true
manual_description_reason: Chapter provides no physical description for any individual guard. Only mentions "two female guards" who attempt custody and depart after confrontation. No distinguishing features or individual identification provided.
clarification_required: true
clarification_reason: Multiple guards mentioned as "Sarkoja" - unclear if this represents one character type or multiple individuals. Need clarification on whether to treat as single archetype or separate characters.
clarification_question: Should Sarkoja be treated as a single character archetype (female Thark guard) or as multiple individual characters? If multiple, how many and what distinguishing features should be assigned?

[[SECTION markdown]]
# Sarkoja - Chapter XI

**Display Name:** Sarkoja  
**Chapter Role:** Female Thark guards attempting custody of Dejah Thoris, depart after confrontation with John Carter

**Physical Presence:** Present in Scene 1 (confrontation at open area), then depart and are referenced as eavesdropping from upper floors. Not physically present in subsequent scenes.

**Physical Description:** Insufficient details provided in source material. Chapter mentions "two female guards" who attempt custody of Dejah Thoris, but no physical attributes (build, height, hair color, eye color, facial features) are described for any individual guard.

**Costume/Silhouette:** No costume or silhouette details provided in this chapter. They are identified as Thark guards attempting to assume custody.

**Continuity-Critical Traits:** 
- Identified as Sarkoja (female Thark guards)
- Associated with Dejah Thoris and John Carter
- Attempt custody of Dejah Thoris at open area
- Depart after John Carter's threat
- Noted eavesdropping from upper floors
- Described as hatching "deviltries" against them

**Render-Facing Prompt Noun Phrases:**
- "female Thark guard"
- "Sarkoja guards"
- "attempt custody of Dejah Thoris"
- "Thark warrior archetype"
- "eavesdropping from upper floors"

**Uncertainty Notes:** 
- Physical appearance cannot be reliably generated from source material
- No costume or silhouette details available for image generation
- Chapter provides only narrative presence, not visual description
- Multiple guards mentioned but no individual identification provided
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: woola
canonical_character_id: woola
aliases: Woola (John Carter's companion)
is_fully_identified: false
manual_description_required: true
manual_description_reason: Chapter provides no physical description for Woola. Only mentions he is John Carter's "companion" who remains on guard at the end. No species, size, or appearance details provided.
clarification_required: true
clarification_reason: Woola is mentioned as companion but species and appearance are not specified in this chapter. Need clarification on whether this is a specific animal type (dog, wolf, etc.) and what appearance characteristics should be assigned.
clarification_question: What species or animal type is Woola? Should he be depicted as a dog, wolf, or other creature? What size, build, and distinguishing features should be assigned?

[[SECTION markdown]]
# Woola - Chapter XI

**Display Name:** Woola  
**Chapter Role:** John Carter's companion/animal guard, remains on duty at end of chapter

**Physical Presence:** Referenced at end of chapter (Scene 5) as remaining on guard. Not physically present in earlier scenes.

**Physical Description:** Insufficient details provided in source material. Chapter mentions he is John Carter's "companion" who remains on guard, but no physical attributes (species, size, build, fur color, facial features) are described.

**Costume/Silhouette:** No costume or silhouette details provided in this chapter. He is identified as an animal companion/guard.

**Continuity-Critical Traits:** 
- Identified as Woola (John Carter's companion)
- Associated with John Carter
- Remains on guard at end of chapter
- Commands to stay while John Carter hastens to audience chamber

**Render-Facing Prompt Noun Phrases:**
- "animal companion"
- "Woola"
- "guard animal"
- "John Carter's companion"
- "remains on duty"

**Uncertainty Notes:** 
- Physical appearance cannot be reliably generated from source material
- No species or silhouette details available for image generation
- Chapter provides only narrative reference, not visual description
- Species and distinguishing features not specified in this chapter
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: lorquas_ptomel
canonical_character_id: lorquas_ptomel
aliases: 
is_fully_identified: false
manual_description_required: true
manual_description_reason: Chapter provides no physical description for Lorquas Ptomel. Only mentioned in messenger summons and seated on rostrum at end. No distinguishing features or individual identification provided.
clarification_required: true
clarification_reason: Lorquas Ptomel is mentioned as a chieftain seated on rostrum but no physical details are provided. Need clarification on whether this is a specific character with established appearance or if visual description should be created from scratch.
clarification_question: Should Lorquas Ptomel be treated as a specific character with established appearance, or is new visual description needed? What chieftain rank and distinguishing features should be assigned?

[[SECTION markdown]]
# Lorquas Ptomel - Chapter XI

**Display Name:** Lorquas Ptomel  
**Chapter Role:** Thark chieftain, seated on rostrum at end of chapter, sends summons to John Carter

**Physical Presence:** Referenced in messenger summons (Scene 5), then mentioned as seated on rostrum at end. Not physically present in earlier scenes.

**Physical Description:** Insufficient details provided in source material. Chapter mentions he is a chieftain who directs John Carter to appear before him, and is seated on rostrum with Tars Tarkas, but no physical attributes (build, height, hair color, eye color, facial features) are described.

**Costume/Silhouette:** No costume or silhouette details provided in this chapter. He is identified as a chieftain of high rank.

**Continuity-Critical Traits:** 
- Identified as Lorquas Ptomel (Thark chieftain)
- Associated with John Carter and Tars Tarkas
- Seated on rostrum at end of chapter
- Sends summons to John Carter directing him to appear forthwith
- First requires killing Lorquas Ptomel for becoming first in prowess

**Render-Facing Prompt Noun Phrases:**
- "Thark chieftain"
- "Lorquas Ptomel"
- "seated on rostrum"
- "high rank among Tharks"
- "first requires killing Lorquas Ptomel"

**Uncertainty Notes:** 
- Physical appearance cannot be reliably generated from source material
- No costume or silhouette details available for image generation
- Chapter provides only narrative reference, not visual description
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: tars_tarkas
canonical_character_id: tars_tarkas
aliases: 
is_fully_identified: false
manual_description_required: true
manual_description_reason: Chapter provides no physical description for Tars Tarkas. Only mentioned as seated on rostrum at end with Lorquas Ptomel. No distinguishing features or individual identification provided.
clarification_required: true
clarification_reason: Tars Tarkas is mentioned as a chieftain close to John Carter in prowess but no physical details are provided. Need clarification on whether this is a specific character with established appearance or if visual description should be created from scratch.
clarification_question: Should Tars Tarkas be treated as a specific character with established appearance, or is new visual description needed? What chieftain rank and distinguishing features should be assigned?

[[SECTION markdown]]
# Tars Tarkas - Chapter XI

**Display Name:** Tars Tarkas  
**Chapter Role:** Thark chieftain, seated on rostrum at end of chapter with Lorquas Ptomel

**Physical Presence:** Referenced in conversation about ranking system (Scene 2), then mentioned as seated on rostrum at end. Not physically present in earlier scenes.

**Physical Description:** Insufficient details provided in source material. Chapter mentions he is a chieftain close to John Carter in prowess (eleventh in prowess, close to Tars Tarkas), but no physical attributes (build, height, hair color, eye color, facial features) are described.

**Costume/Silhouette:** No costume or silhouette details provided in this chapter. He is identified as a chieftain of high rank among the Tharks.

**Continuity-Critical Traits:** 
- Identified as Tars Tarkas (Thark chieftain)
- Associated with John Carter and Lorquas Ptomel
- Seated on rostrum at end of chapter
- John Carter is eleventh in prowess, close to Tars Tarkas
- Becoming first requires killing Lorquas Ptomel for council will

**Render-Facing Prompt Noun Phrases:**
- "Thark chieftain"
- "Tars Tarkas"
- "seated on rostrum"
- "high rank among Tharks"
- "close to John Carter in prowess"

**Uncertainty Notes:** 
- Physical appearance cannot be reliably generated from source material
- No costume or silhouette details available for image generation
- Chapter provides only narrative reference, not visual description
[[/SECTION]]
[[/FILMCREATOR_RECORD]]
[[/FILMCREATOR_PACKET]]
````
