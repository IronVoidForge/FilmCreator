# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-20T02:16:42.465635+00:00
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

# Chapter Summary: Child-Raising on Mars (CH007)

## Scene 1: The Procession to the Incubator
**Visual Continuity:**
- Sola escorts the narrator to the plaza where ~250 three-wheeled chariots are being harnessed to mastodonian animals.
- Warriors ride at the head (five abreast) and rear of the caravan; outriders flank sides.
- Animals are guided telepathically, wearing no bit or bridle.
- The cavalcade moves in single file toward the incubator location.

**Narrative:**
- The narrator is dragged into an empty chariot by Sola and proceeds with the procession.
- They travel across the valley before the city, through hills, down to the dead sea bottom (incubator terminal point).
- Upon arrival, chariots are parked with military precision on four sides of the enclosure.

## Scene 2: The Hatching Ceremony
**Visual Continuity:**
- Half a score of warriors dismount and advance toward the incubator.
- Tars Tarkas explains to Lorquas Ptomel Jed regarding the subject of conversation.
- The incubator is alive with hideous little devils (young Martians) ranging 3-4 feet in height.
- Warriors command relative to the incubator; narrator leaps over parked chariots for edification.

**Narrative:**
- Tars Tarkas signs for Sola to send the narrator to him.
- The narrator repeats his performance of leaping over chariots for Lorquas Ptomel's edification.
- Warriors break an opening in the incubator wall large enough for exit of young Martians.

## Scene 3: Child Capture and Rearing Ritual
**Visual Continuity:**
- Women and younger Martians form two solid walls leading out through chariots into the plain.
- Little Martians scamper between walls; captured one at a time by women/older children.
- Last in line captures first to reach end; opposite captures second, etc.
- Women fall out of line and return to respective chariots; young men turn over captured ones to women.

**Narrative:**
- The ceremony involves capturing young Martians as they leave the incubator.
- Work of rearing consists solely in teaching them to talk and use weapons from first year.
- Young Martians are common children of the community, unknown to their mothers or fathers.
- Education devolves upon females who chance to capture them (e.g., Sola).

## Scene 4: Explanation of Martian Child-Rearing System
**Visual Continuity:**
- Incubators built in remote fastnesses to avoid discovery by other tribes.
- Discovery of alien incubator results in no children for another five years.
- Community composed of ~30,000 souls roaming arid land between 40-80 degrees south latitude.

**Narrative:**
- System involves careful selection of hardiest specimens; birth rate regulated to offset death loss.
- Each female brings forth ~13 eggs/year; only ~100 most perfect chosen from yearly supply.
- Eggs hidden in subterranean vaults (too low for incubation) until examined by council of twenty chieftains.
- After five years, ~500 almost perfect eggs placed in air-tight incubators to hatch by sun's rays.
- System causes loss of finer feelings and higher humanitarian instincts among Martians.

## Scene 5: Narrator's Development and Return
**Visual Continuity:**
- Sola's duties doubled caring for young Martian as well as narrator.
- Both require little attention; equally advanced in Martian education.
- Narrator develops telepathic powers shortly after tutelage.

**Narrative:**
- After return to dead city, narrator passes several days in comparative idleness.
- Warriors ride forth early morning and return just before darkness (transporting eggs to incubator).
- Sola takes upon herself to train narrator and young Martian together.
- Narrator masters language within a week; understands nearly everything said.
- Narrator develops telepathic powers so that he can sense practically everything around him.
- **Key Fact:** While narrator catches telepathic messages easily from others, no one could read a jot from his mind under any circumstances (undoubted advantage over Martians).
````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
task: character_extraction
version: 1

[[SECTION character_index_markdown]]
# Character Index - Child-Raising on Mars (CH007)

| Character | Role | Physical Presence | Description Available |
|-----------|------|-------------------|----------------------|
| Sola | Educator/Caregiver | Referenced | No physical description |
| Narrator | Protagonist | Referenced | No physical description |
| Tars Tarkas | Martian Warrior/Educator | Referenced | No physical description |
| Lorquas Ptomel Jed | Council Member | Referenced | No physical description |

[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: sola
canonical_character_id: Sola
aliases: 
is_fully_identified: true
manual_description_required: true
manual_description_reason: Chapter summary provides no physical description of Sola's appearance, costume, or silhouette. Only her actions and role are described (escorting narrator, taking care of him, training him).
clarification_required: false
clarification_reason: 
clarification_question: 

[[SECTION markdown]]
# Sola

## Chapter Role
Escorts narrator to plaza, cares for narrator and young Martian, trains narrator in language and telepathic powers

## Physical Presence
Referenced throughout chapter (escorts narrator, signs for narrator, takes care of narrator)

## Physical Description
No physical description provided in chapter summary. Only actions described: escorting, taking care of, training.

## Costume & Silhouette
Unknown. No costume or silhouette details available from source material.

## Continuity-Critical Traits
- Female character (referred to as "female" in child-rearing system explanation)
- Educator role (teaches narrator language and telepathic powers)
- Caregiver role (takes care of both narrator and young Martian)

## Render-Facing Prompt Notes
Use uncertainty markers for appearance. Focus on her actions: escorting, training, caring. No specific visual traits to describe.

## Uncertainty Notes
Physical appearance is completely unknown from this chapter summary. Any visual description would be speculative.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: narrator
canonical_character_id: Narrator
aliases: 
is_fully_identified: true
manual_description_required: true
manual_description_reason: Chapter summary provides no physical description of the narrator's appearance, costume, or silhouette. Only his actions and role are described (being dragged into chariot, leaping over chariots, developing telepathic powers).
clarification_required: false
clarification_reason: 
clarification_question: 

[[SECTION markdown]]
# Narrator

## Chapter Role
Protagonist, receives education from Sola, develops telepathic powers

## Physical Presence
Referenced throughout chapter (dragged into chariot, leaping over chariots, developing telepathic powers)

## Physical Description
No physical description provided in chapter summary. Only actions described: being dragged, leaping, developing powers.

## Costume & Silhouette
Unknown. No costume or silhouette details available from source material.

## Continuity-Critical Traits
- Human character (implied by "narrator" and context of Mars story)
- Recipient of Martian education
- Develops telepathic abilities
- Can read minds but cannot be read by others

## Render-Facing Prompt Notes
Use uncertainty markers for appearance. Focus on his actions: being dragged, leaping, developing powers. No specific visual traits to describe.

## Uncertainty Notes
Physical appearance is completely unknown from this chapter summary. Any visual description would be speculative.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: tars_tarkas
canonical_character_id: Tars Tarkas
aliases: 
is_fully_identified: true
manual_description_required: true
manual_description_reason: Chapter summary provides no physical description of Tars Tarkas's appearance, costume, or silhouette. Only his actions and role are described (explaining conversation, signing for Sola).
clarification_required: false
clarification_reason: 
clarification_question: 

[[SECTION markdown]]
# Tars Tarkas

## Chapter Role
Explains conversation with Lorquas Ptomel Jed, signs for Sola to send narrator

## Physical Presence
Referenced in Scene 2 (explains conversation, signs for Sola)

## Physical Description
No physical description provided in chapter summary. Only actions described: explaining conversation, signing.

## Costume & Silhouette
Unknown. No costume or silhouette details available from source material.

## Continuity-Critical Traits
- Martian warrior (implied by "warriors" context and name)
- Educator/mentor role (explains to narrator about child-rearing system)
- Council member (part of twenty chieftains mentioned in Scene 4)

## Render-Facing Prompt Notes
Use uncertainty markers for appearance. Focus on his actions: explaining, signing. No specific visual traits to describe.

## Uncertainty Notes
Physical appearance is completely unknown from this chapter summary. Any visual description would be speculative.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: lorquas_ptomel_jed
canonical_character_id: Lorquas Ptomel Jed
aliases: 
is_fully_identified: true
manual_description_required: true
manual_description_reason: Chapter summary provides no physical description of Lorquas Ptomel Jed's appearance, costume, or silhouette. Only his role in conversation is described (subject of discussion with Tars Tarkas).
clarification_required: false
clarification_reason: 
clarification_question: 

[[SECTION markdown]]
# Lorquas Ptomel Jed

## Chapter Role
Subject of conversation with Tars Tarkas in Scene 2

## Physical Presence
Referenced in Scene 2 (subject of conversation)

## Physical Description
No physical description provided in chapter summary. Only role described: subject of conversation.

## Costume & Silhouette
Unknown. No costume or silhouette details available from source material.

## Continuity-Critical Traits
- Martian character (implied by name and context)
- Council member (part of twenty chieftains mentioned in Scene 4)
- Subject of discussion about child-rearing system

## Render-Facing Prompt Notes
Use uncertainty markers for appearance. Focus on his role as subject of conversation. No specific visual traits to describe.

## Uncertainty Notes
Physical appearance is completely unknown from this chapter summary. Any visual description would be speculative.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]
[[/FILMCREATOR_PACKET]]
````
