# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-20T01:13:54.723227+00:00
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

Chapter id: CH013

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

# Chapter Summary

## Scene 1: Recap of Training and Thoat Handling
John Carter reviews his training with Tars Tarkas, specifically the handling of thoats. He demonstrates that he can manage the beasts as well as native warriors but uses a method of kindness rather than violence. The community marvels at this, attributing it to an "earthly power." Tars Tarkas asks how he accomplished this, and John explains his philosophy: "By kindness." This moment marks the beginning of a new existence for the beasts and is presented before Lorquas Ptomel's warriors.

## Scene 2: Evening Before Departure
On the evening before the march resumes, John Carter spends time with Dejah Thoris. She had been absent from his quarters due to warrior supervision. He intercepts her while she walks with Sola, directing Sola away on a trivial errand so he can be alone with Dejah. This is driven by John's desire for companionship and the mutual interest they share despite being forty-eight million miles apart in origin.

## Scene 3: Dialogue on Status and Jealousy
Dejah Thoris reveals that the warriors are keeping them apart and subjecting her to dangerous labor (mixing radium powder, making exploding projectiles). She explains that the warriors hate their fates and wreak spite on her because she represents everything they crave but cannot attain. John defends his Earth customs (nursing enemies) against Martian norms (dead enemy means more to divide). Dejah calls him "my chieftain," a title of significance he does not yet fully grasp.

## Scene 4: Night Walk and Physical Intimacy
Day turns to night as they walk along the great avenue lit by the two moons, with Earth visible in the sky. John removes his silks and throws them across Dejah's shoulders. He rests his arm on her naked shoulder for a moment longer than necessary. She does not draw away or speak. This physical contact signifies mutual love and connection, described as "that which is ever oldest, yet ever new."

## Scene 5: Confirmation of Love
John Carter reflects on the touch of his arm upon her shoulder, interpreting it as words he would not mistake. He confirms that he loved Dejah Thoris since the first moment their eyes met in the plaza of the dead city of Korad. The chapter ends with this emotional realization amidst the chill of the Martian night.
````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
task: character_extraction
version: 1

[[SECTION character_index_markdown]]
# Character Index - Chapter CH013

| Asset ID | Canonical Character ID | Display Name | Presence Status | Description Support |
|----------|------------------------|---------------|------------------|---------------------|
| john_carter | john_carter | John Carter | Physically present throughout Scenes 2-5; referenced in Scene 1 | Limited - clothing and actions only |
| tars_tarkas | tars_tarkas | Tars Tarkas | Referenced in Scene 1 | None - role mentioned only |
| dejah_thoris | dejah_thoris | Dejah Thoris | Physically present throughout Scenes 2-5 | Limited - clothing and body parts only |
| sola | sola | Sola | Referenced in Scene 2 | None - walking companion only |
| lorquas_ptomels_warriors | lorquas_ptomels_warriors | Lorquas Ptomel's Warriors | Referenced in Scenes 1-3 | None - group reference only |

**Notes:**
- All characters require manual physical description for dependable image generation
- John Carter, Dejah Thoris, and Sola are individually identified; warriors are a collective group
- Tars Tarkas is referenced but no visual details provided
- Chapter summary provides emotional context but sparse physical descriptions
[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: john_carter
canonical_character_id: john_carter
aliases: 
is_fully_identified: true
manual_description_required: true
manual_description_reason: Physical description limited to clothing (silks) and actions; no stable physical traits documented for later image generation
clarification_required: false
clarification_reason: 
clarification_question: 

[[SECTION markdown]]
# John Carter - Character File

**Display Name:** John Carter  
**Chapter Role:** Protagonist / Earthman on Mars  
**Presence Status:** Physically present (Scenes 2-5), referenced (Scene 1)  

## Physical Description (Supported by Source)
- Wears silks that are removed in Scene 4
- Arm rests on Dejah Thoris's shoulder in Scene 4
- No stable physical traits documented (height, build, hair, eyes, etc.)

## Costume & Silhouette
- Silk clothing (removed and thrown across Dejah's shoulders)
- Earth customs referenced (nursing enemies vs. Martian norms)

## Continuity-Critical Traits
- Represents "earthly power" attributed by community in Scene 1
- Confirms love for Dejah Thoris since first meeting in Korad plaza
- Title of "chieftain" given by Dejah in Scene 3 (not yet fully grasped)

## Render-Facing Noun Phrases
- Earthman on Mars
- Silks-wearing protagonist
- Arm-resting lover
- Chieftain title recipient

## Uncertainty Notes
⚠️ **Physical description incomplete:** No stable physical traits documented for dependable image generation. Manual description required for later render-facing prompt writing.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: tars_tarkas
canonical_character_id: tars_tarkas
aliases: 
is_fully_identified: true
manual_description_required: true
manual_description_reason: No physical or visual description provided; only referenced as training partner with John Carter
clarification_required: false
clarification_reason: 
clarification_question: 

[[SECTION markdown]]
# Tars Tarkas - Character File

**Display Name:** Tars Tarkas  
**Chapter Role:** Martian Trainer / Beast Handler  
**Presence Status:** Referenced (Scene 1)  

## Physical Description (Supported by Source)
- None documented in chapter summary
- Only role as training partner mentioned

## Costume & Silhouette
- No costume details provided
- No silhouette information available

## Continuity-Critical Traits
- Trains John Carter on thoat handling
- Asks how John accomplished his method of kindness
- Represents Martian warrior tradition

## Render-Facing Noun Phrases
- Martian trainer
- Beast handler
- Training partner to John Carter

## Uncertainty Notes
⚠️ **Physical description incomplete:** No physical or visual description provided in source material. Manual description required for later image generation.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: dejah_thoris
canonical_character_id: dejah_thoris
aliases: 
is_fully_identified: true
manual_description_required: true
manual_description_reason: Physical description limited to clothing (silks removed) and body parts mentioned; no stable physical traits documented for later image generation
clarification_required: false
clarification_reason: 
clarification_question: 

[[SECTION markdown]]
# Dejah Thoris - Character File

**Display Name:** Dejah Thoris  
**Chapter Role:** Love Interest / Martian Princess  
**Presence Status:** Physically present (Scenes 2-5)  

## Physical Description (Supported by Source)
- Naked shoulder mentioned in Scene 4
- Silks removed and thrown across shoulders in Scene 4
- No stable physical traits documented (height, build, hair, eyes, etc.)

## Costume & Silhouette
- Silk clothing (removed by John Carter)
- Subject to dangerous labor (mixing radium powder, making projectiles)
- Represented as everything warriors crave but cannot attain

## Continuity-Critical Traits
- Called "my chieftain" by John in Scene 3
- Represents mutual love and connection with John
- Absent from quarters due to warrior supervision (Scene 2)
- Walks with Sola before being intercepted by John

## Render-Facing Noun Phrases
- Martian princess
- Silk-wearing love interest
- Chieftain title recipient
- Radium powder mixer
- Great avenue walker (two moons lit)

## Uncertainty Notes
⚠️ **Physical description incomplete:** No stable physical traits documented for dependable image generation. Manual description required for later render-facing prompt writing.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: sola
canonical_character_id: sola
aliases: 
is_fully_identified: true
manual_description_required: true
manual_description_reason: No physical or visual description provided; only referenced as walking companion with Dejah Thoris
clarification_required: false
clarification_reason: 
clarification_question: 

[[SECTION markdown]]
# Sola - Character File

**Display Name:** Sola  
**Chapter Role:** Walking Companion / Errand Runner  
**Presence Status:** Referenced (Scene 2)  

## Physical Description (Supported by Source)
- None documented in chapter summary
- Only mentioned as walking companion with Dejah Thoris

## Costume & Silhouette
- No costume details provided
- No silhouette information available

## Continuity-Critical Traits
- Walking companion to Dejah Thoris in Scene 2
- Directed away on trivial errand by John Carter
- Facilitates private moment between John and Dejah

## Render-Facing Noun Phrases
- Walking companion
- Errand runner
- Dejah's companion

## Uncertainty Notes
⚠️ **Physical description incomplete:** No physical or visual description provided in source material. Manual description required for later image generation.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: lorquas_ptomels_warriors
canonical_character_id: lorquas_ptomels_warriors
aliases: 
is_fully_identified: false
manual_description_required: true
manual_description_reason: No physical or visual description provided; only referenced as warrior group with Lorquas Ptomel
clarification_required: true
clarification_reason: Group reference without individual stable identification; need clarification on whether to treat as collective entity or require individual character breakdown
clarification_question: Should Lorquas Ptomel's warriors be treated as a collective group entity, or do you have specific warrior characters that should be individually identified?

[[SECTION markdown]]
# Lorquas Ptomel's Warriors - Character File

**Display Name:** Lorquas Ptomel's Warriors  
**Chapter Role:** Antagonist Group / Warrior Collective  
**Presence Status:** Referenced (Scenes 1-3)  

## Physical Description (Supported by Source)
- None documented in chapter summary
- Only referenced as warrior group

## Costume & Silhouette
- No costume details provided
- No silhouette information available

## Continuity-Critical Traits
- Keep John and Dejah apart (Scene 3)
- Subject Dejah to dangerous labor (mixing radium powder, making projectiles)
- Hate their fates and wreak spite on Dejah
- Represent Martian warrior tradition vs. Earth customs
- Mentioned as "before Lorquas Ptomel's warriors" in Scene 1

## Render-Facing Noun Phrases
- Warrior collective
- Antagonist group
- Radium powder supervisors
- Projectile makers
- Fate-hating warriors

## Uncertainty Notes
⚠️ **Physical description incomplete:** No physical or visual description provided in source material. Manual description required for later image generation.  
⚠️ **Identification unclear:** Group reference without stable individual identification. Clarification required on whether to treat as collective entity or break down into specific warrior characters.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]
[[/FILMCREATOR_PACKET]]
````
