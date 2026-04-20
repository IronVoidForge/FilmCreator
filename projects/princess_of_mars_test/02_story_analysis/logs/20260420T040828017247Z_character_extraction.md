# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-20T04:08:28.017247+00:00
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

Chapter id: CH023

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

**Scene 1: Infiltration & Warning.** Carter enters Kantos Kan's room in Zodanga without detection. He informs Kan that Dejah Thoris has promised her hand to Sab Than. Kan reacts with dismay, declaring the alliance impossible for Helium lovers.
**Scene 2: The Plan.** Kan pledges his sword to kill Sab Than for Dejah Thoris and Helium. Carter agrees to go to Helium while Kan attempts the assassination at the palace.
**Scene 3: Roof Access.** Carter climbs the barracks building using ornamental ledges. He swings up to the roof using a leather strap with a hook, risking a fall from a thousand feet. He neutralizes the sentry by throwing him over the edge and binding him there.
**Scene 4: Machine Retrieval & Takeoff.** Carter retrieves his machine and Kan's machine from the sheds. They take off together towards the palace route.
**Scene 5: Pursuit & Crash.** Zodanga air scouts pursue them. Carter uses Helium gearing tricks to increase speed but is hit by a shot from a cruiser. The craft suffers concussion damage and plunges downward.
**Scene 6: Navigation Loss.** After recovering near the ground, Carter's compass and speedometer are destroyed by the projectile fragment. He flies blindly for nearly six hours.
**Scene 7: Wrong City Realization.** Morning finds him over a vast expanse of dead sea bottom. He approaches a city but realizes it is not Helium due to its lack of twin towers (scarlet and yellow). He must correct his course southeast.
````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
task: character_extraction
version: 1

[[SECTION character_index_markdown]]
# Character Index - CH023

| Asset ID | Display Name | Presence | Description Status |
|----------|--------------|----------|-------------------|
| carter | Carter | Physically Present | Manual Description Required |
| kantos_kan | Kantos Kan | Physically Present | Manual Description Required |
| dejah_thoris | Dejah Thoris | Referenced Only | Manual Description Required |
| sab_than | Sab Than | Referenced Only | Manual Description Required |

*Note: All characters require manual physical description as none are described in this chapter summary.*
[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: carter
canonical_character_id: carter
aliases: 
is_fully_identified: true
manual_description_required: true
manual_description_reason: No physical description provided in chapter summary. Character is physically present but appearance details are not documented.
clarification_required: false
clarification_reason: 
clarification_question: 

[[SECTION markdown]]
# carter.md

## Display Name
Carter

## Chapter Role
Protagonist - infiltrator, pilot, action character

## Physical Presence
Physically present throughout scenes 1-7 (enters rooms, climbs buildings, flies machines)

## Physical Description Status
**UNCERTAIN** - No physical description provided in this chapter summary. Requires manual documentation for image generation.

## Known Actions & Traits
- Enters Kantos Kan's room without detection
- Climbs barracks building using ornamental ledges
- Swings to roof using leather strap with hook
- Neutralizes sentry by throwing him over edge
- Retrieves machines from sheds
- Flies toward palace route
- Uses Helium gearing tricks for speed
- Survives crash and concussion damage
- Flies blindly for six hours after navigation loss

## Continuity-Critical Notes
- Machine pilot (owns flying craft)
- Operates in Zodanga/Kantos Kan's territory
- Has compass/speedometer destroyed mid-flight

## Render-Facing Prompt Noun Phrases
- Male protagonist figure
- Airship/machine operator
- Climbing action specialist
- Pilot with navigation equipment

## Uncertainty Notes
Physical appearance, costume details, and facial features are not documented in this chapter. Manual description required for dependable image generation.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: kantos_kan
canonical_character_id: kantos_kan
aliases: 
is_fully_identified: true
manual_description_required: true
manual_description_reason: No physical description provided in chapter summary. Character is physically present but appearance details are not documented.
clarification_required: false
clarification_reason: 
clarification_question: 

[[SECTION markdown]]
# kantos_kan.md

## Display Name
Kantos Kan

## Chapter Role
Antagonist/Ally - palace figure, sword-wielder

## Physical Presence
Physically present in scenes 1-2 (receives warning from Carter, pledges sword)

## Physical Description Status
**UNCERTAIN** - No physical description provided in this chapter summary. Requires manual documentation for image generation.

## Known Actions & Traits
- Receives warning about Dejah Thoris promising hand to Sab Than
- Reacts with dismay at alliance impossibility
- Pledges sword to kill Sab Than for Dejah Thoris and Helium
- Attempts assassination at palace while Carter goes to Helium

## Continuity-Critical Notes
- Palace resident (Kantos Kan's room)
- Sword-wielder/assassin
- Zodanga-based figure
- Works with Carter on dual mission plan

## Render-Facing Prompt Noun Phrases
- Male antagonist/ally figure
- Palace official
- Sword-wielding assassin
- Helium supporter despite alliance concerns

## Uncertainty Notes
Physical appearance, costume details, and facial features are not documented in this chapter. Manual description required for dependable image generation.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: dejah_thoris
canonical_character_id: dejah_thoris
aliases: 
is_fully_identified: true
manual_description_required: true
manual_description_reason: Character only referenced in chapter summary. No physical description provided and not physically present. Requires manual documentation for image generation.
clarification_required: false
clarification_reason: 
clarification_question: 

[[SECTION markdown]]
# dejah_thoris.md

## Display Name
Dejah Thoris

## Chapter Role
Referenced character - marriage promise recipient

## Physical Presence
**UNCERTAIN** - Only referenced in chapter summary, not physically present. Appears as subject of conversation between Carter and Kantos Kan.

## Physical Description Status
**UNCERTAIN** - No physical description provided in this chapter summary. Requires manual documentation for image generation.

## Known Actions & Traits
- Promises her hand to Sab Than (mentioned by Carter)
- Subject of alliance discussion between male characters

## Continuity-Critical Notes
- Helium princess figure
- Marriage promise recipient
- Central to alliance plotline
- Zodanga/Helium connection point

## Render-Facing Prompt Noun Phrases
- Female protagonist figure
- Princess/marriage candidate
- Helium royalty representative
- Alliance negotiation subject

## Uncertainty Notes
Physical appearance, costume details, and facial features are not documented in this chapter. Character is only referenced, not present. Manual description required for dependable image generation.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: sab_than
canonical_character_id: sab_than
aliases: 
is_fully_identified: true
manual_description_required: true
manual_description_reason: Character only referenced in chapter summary. No physical description provided and not physically present. Requires manual documentation for image generation.
clarification_required: false
clarification_reason: 
clarification_question: 

[[SECTION markdown]]
# sab_than.md

## Display Name
Sab Than

## Chapter Role
Referenced character - marriage promise recipient

## Physical Presence
**UNCERTAIN** - Only referenced in chapter summary, not physically present. Appears as subject of conversation between Carter and Kantos Kan.

## Physical Description Status
**UNCERTAIN** - No physical description provided in this chapter summary. Requires manual documentation for image generation.

## Known Actions & Traits
- Receives marriage promise from Dejah Thoris (mentioned by Carter)
- Subject of assassination plan by Kantos Kan

## Continuity-Critical Notes
- Zodanga figure (implied by location context)
- Marriage promise recipient
- Target of assassination attempt
- Alliance disruption point

## Render-Facing Prompt Noun Phrases
- Male antagonist figure
- Marriage candidate
- Assassination target
- Zodanga royalty representative

## Uncertainty Notes
Physical appearance, costume details, and facial features are not documented in this chapter. Character is only referenced, not present. Manual description required for dependable image generation.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]
[[/FILMCREATOR_PACKET]]
````
