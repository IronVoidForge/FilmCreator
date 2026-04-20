# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-20T06:49:07.848859+00:00
- task: character_extraction

## System Prompt
````text
You are FilmCreator's chapter analysis engine.
Return only FilmCreator packets with the requested sections and records.
Do not wrap the packet in code fences unless explicitly requested.
Do not produce JSON-only responses.
If a packet asks for markdown sections, emit the section name on its own line and wrap the body in [[SECTION ...]] ... [[/SECTION]].
Keep the response deterministic and grounded in the supplied chapter text.
````

## User Prompt
````text
Project slug: princess_of_mars_test

Chapter id: CH001

Task: extract visible and referenced characters into a character index plus one Markdown file per character.

Packet contract:
- task: character_extraction
- version: 1
- first line: [[FILMCREATOR_PACKET]]
- last line: [[/FILMCREATOR_PACKET]]
- required sections: character_index_markdown
- record type character: fields=asset_id, canonical_character_id, aliases, is_fully_identified, manual_description_required, manual_description_reason, clarification_required, clarification_reason, clarification_question sections=markdown



Output format:

[[FILMCREATOR_PACKET]]

task: character_extraction

version: 1

character_index_markdown:

[[SECTION character_index_markdown]]

...index markdown...

[[/SECTION]]



[[FILMCREATOR_RECORD]]

type: character

asset_id: protagonist

canonical_character_id: CH002 Protagonist

aliases: Narrator, Conscious Entity

is_fully_identified: false

manual_description_required: true

manual_description_reason: Sparse physical detail.

clarification_required: true

clarification_reason: Needs identity clarification.

clarification_question: What is the protagonist's physical form and origin?



[[SECTION markdown]]

# Protagonist

Short, grounded character markdown.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]



Important rules:

- if a character does not have enough physical or visual description in the supplied material to support dependable later image generation, set manual_description_required to true

- explain exactly why in manual_description_reason

- do not guess ornate missing details just to avoid the flag

- if the chapter names a character without enough stable identification, set is_fully_identified to false

- use aliases for alternate names or partial labels seen in the chapter

- if the character might already exist under another name or is too weakly identified, set clarification_required to true and ask a targeted question

- if clarification is not required, still include clarification_reason and clarification_question as empty values

- emit one explicit character record per meaningful character mention

- every character record must have a FILMCREATOR_RECORD wrapper with type character

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

In Chapter I, titled "On the Arizona Hills," John Carter reflects on his fear of death despite having died twice and remained alive. He recounts his decision to write down the story of his life and death, specifically focusing on the events surrounding a gold discovery in 1865 with Captain James K. Powell. After locating a valuable quartz vein, Powell departed to purchase machinery while Carter guarded the claim. Upon discovering that Apaches were pursuing Powell's party, Carter chased them down the trail. He found Powell dead and surrounded by Apache warriors at a campsite. Charging into the enemy lines, Carter shot at the Apaches, causing them to flee. He retrieved Powell's body and escaped the Apache pursuit through a defile that led him inadvertently to a large cave. After laying Powell down and failing to resuscitate him, Carter entered the cave to reconnoiter. Overcome by fatigue and excitement, he fell asleep on the cave floor, marking the beginning of his ten-year stay.
````

## Raw Response
````text


[[FILMCREATOR_PACKET]]

task: character_extraction

version: 1

character_index_markdown:

[[SECTION character_index_markdown]]

# Character Index - Chapter I

## John Carter (Protagonist)
- **Status**: Referenced throughout chapter
- **Role**: Narrator, survivor of death events
- **Description**: Physical details sparse in source material

## Captain James K. Powell
- **Status**: Found dead at campsite
- **Role**: Partner in gold discovery venture
- **Description**: Deceased character, minimal physical description available

## Apache Warriors
- **Status**: Pursuing party through trail
- **Role**: Antagonist force in chapter events
- **Description**: Group of warriors, no individual physical details provided

[[/SECTION]]



[[FILMCREATOR_RECORD]]

type: character

asset_id: john_carter

canonical_character_id: CH001 John Carter

aliases: Narrator, Conscious Entity, Survivor

is_fully_identified: false

manual_description_required: true

manual_description_reason: Sparse physical detail in source material. No specific appearance, age, or build described.

clarification_required: true

clarification_reason: Needs identity clarification for consistent image generation.

clarification_question: What is John Carter's physical form and origin story?



[[SECTION markdown]]

# John Carter

## Chapter Role
Protagonist/Narrator of the story being written down

## Physical Presence
Referenced throughout chapter events, not physically present in current timeline

## Physical Description
No specific appearance details provided in source material. Character has died twice and remained alive according to narrative.

## Costume/Silhouette
Unknown - no clothing or physical silhouette described in chapter text.

## Continuity-Critical Traits
- Survivor of death events (died twice, remained alive)
- Writing down life story as narrator
- Guarding gold claim with Captain Powell
- Found dead body of Captain Powell
- Escaped Apache pursuit through defile to cave

## Uncertainty Notes
Physical appearance is completely unspecified in source material. Any image generation would require creative interpretation beyond what the text supports.

[[/SECTION]]



[[FILMCREATOR_RECORD]]

type: character

asset_id: captain_powell

canonical_character_id: CH001 Captain James K. Powell

aliases: Gold Discovery Partner, Deceased Companion

is_fully_identified: true

manual_description_required: true

manual_description_reason: Character is deceased with minimal physical description in source material. No specific appearance details provided.

clarification_required: false

clarification_reason: Character status as deceased is clear from narrative.

clarification_question: N/A - character is deceased and appears only through narrative reference.



[[SECTION markdown]]

# Captain James K. Powell

## Chapter Role
Partner in gold discovery venture with John Carter

## Physical Presence
Found dead at campsite, not physically present in current timeline

## Physical Description
No specific appearance details provided in source material. Character is deceased throughout chapter events.

## Costume/Silhouette
Unknown - no clothing or physical silhouette described in chapter text prior to death.

## Continuity-Critical Traits
- Departed to purchase machinery for gold claim
- Found dead surrounded by Apache warriors at campsite
- Body retrieved by John Carter after charging into enemy lines
- Deceased character, appears only through narrative reference

## Uncertainty Notes
Physical appearance is completely unspecified in source material. Character status as deceased is clear from narrative context.

[[/SECTION]]



[[FILMCREATOR_RECORD]]

type: character

asset_id: apache_warriors

canonical_character_id: CH001 Apache Warriors

aliases: Pursuing Party, Enemy Force, Campsite Attackers

is_fully_identified: true

manual_description_required: true

manual_description_reason: Group of warriors with no individual physical description in source material. No specific appearance details provided for any individual warrior.

clarification_required: false

clarification_reason: Character group status is clear from narrative events.

clarification_question: N/A - refers to group of warriors, not individual character requiring identification.



[[SECTION markdown]]

# Apache Warriors

## Chapter Role
Antagonist force pursuing gold discovery party

## Physical Presence
Referenced throughout chapter events as pursuing party and campsite attackers

## Physical Description
No specific appearance details provided in source material for any individual warrior. Group of warriors attacking at campsite.

## Costume/Silhouette
Unknown - no clothing or physical silhouette described in chapter text.

## Continuity-Critical Traits
- Pursuing Powell's party through trail
- Surrounding campsite where Powell was found dead
- Fled after John Carter charged into enemy lines
- Group force, not individual characters requiring identification

## Uncertainty Notes
Physical appearance is completely unspecified in source material for any individual warrior. Refers to group of warriors rather than specific individuals requiring detailed identification.

[[/SECTION]]



[[FILMCREATOR_RECORD]]

type: character

asset_id: apaches

canonical_character_id: CH001 Apaches

aliases: Apache Warriors, Enemy Force

is_fully_identified: true

manual_description_required: true

manual_description_reason: Group reference with no individual physical description in source material. No specific appearance details provided for any individual.

clarification_required: false

clarification_reason: Character group status is clear from narrative events.

clarification_question: N/A - refers to group of Apaches, not individual character requiring identification.



[[SECTION markdown]]

# Apaches

## Chapter Role
Antagonist force pursuing gold discovery party

## Physical Presence
Referenced throughout chapter events as pursuing party and campsite attackers

## Physical Description
No specific appearance details provided in source material for any individual Apache. Group of warriors attacking at campsite.

## Costume/Silhouette
Unknown - no clothing or physical silhouette described in chapter text.

## Continuity-Critical Traits
- Pursuing Powell's party through trail
- Surrounding campsite where Powell was found dead
- Fled after John Carter charged into enemy lines
- Group force, not individual characters requiring identification

## Uncertainty Notes
Physical appearance is completely unspecified in source material for any individual Apache. Refers to group of Apaches rather than specific individuals requiring detailed identification.

[[/SECTION]]



[[FILMCREATOR_RECORD]]

type: character

asset_id: narrator_entity

canonical_character_id: CH001 Narrator Entity

aliases: Conscious Entity, Story Writer

is_fully_identified: false

manual_description_required: true

manual_description_reason: Character exists as narrative voice with no physical description in source material. Writing down life story without specific appearance details.

clarification_required: true

clarification_reason: Needs identity clarification for consistent image generation of narrator entity.

clarification_question: What is the narrator's physical form and relationship to John Carter?



[[SECTION markdown]]

# Narrator Entity

## Chapter Role
Voice writing down life story and death events

## Physical Presence
Referenced as narrative voice, not physically present in current timeline

## Physical Description
No specific appearance details provided in source material. Character exists primarily through narrative function of writing down story.

## Costume/Silhouette
Unknown - no clothing or physical silhouette described in chapter text.

## Continuity-Critical Traits
- Writing down life story as narrator
- Conscious Entity aware of death events
- Story writer documenting gold discovery events
- Narrator voice separate from John Carter's physical presence

## Uncertainty Notes
Physical appearance is completely unspecified in source material. Character exists primarily through narrative function rather than physical description.

[[/SECTION]]



[[FILMCREATOR_RECORD]]

type: character

asset_id: carters_story_writer

canonical_character_id: CH001 Story Writer

aliases: Life Story Author, Death Events Documenter

is_fully_identified: false

manual_description_required: true

manual_description_reason: Character exists as story writer with no physical description in source material. Writing down life events without specific appearance details.

clarification_required: true

clarification_reason: Needs identity clarification for consistent image generation of story writing character.

clarification_question: What is the story writer's physical form and relationship to John Carter?



[[SECTION markdown]]

# Story Writer

## Chapter Role
Author documenting life story and death events

## Physical Presence
Referenced as narrative voice, not physically present in current timeline

## Physical Description
No specific appearance details provided in source material. Character exists primarily through narrative function of writing down story.

## Costume/Silhouette
Unknown - no clothing or physical silhouette described in chapter text.

## Continuity-Critical Traits
- Writing down life story as narrator
- Documenting death events and gold discovery
- Story writer aware of multiple deaths
- Narrator voice separate from John Carter's physical presence

## Uncertainty Notes
Physical appearance is completely unspecified in source material. Character exists primarily through narrative function rather than physical description.

[[/SECTION]]



[[FILMCREATOR_RECORD]]

type: character

asset_id: powells_party

canonical_character_id: CH001 Powell's Party

aliases: Gold Discovery Team, Claim Guard

is_fully_identified: true

manual_description_required: true

manual_description_reason: Group reference with no individual physical description in source material. No specific appearance details provided for any party member.

clarification_required: false

clarification_reason: Character group status is clear from narrative events.

clarification_question: N/A - refers to group of Powell's party, not individual character requiring identification.



[[SECTION markdown]]

# Powell's Party

## Chapter Role
Gold discovery team with John Carter

## Physical Presence
Referenced throughout chapter events as pursuing party and claim guard

## Physical Description
No specific appearance details provided in source material for any individual party member. Group of people involved in gold discovery venture.

## Costume/Silhouette
Unknown - no clothing or physical silhouette described in chapter text.

## Continuity-Critical Traits
- Departed to purchase machinery for gold claim
- Found dead surrounded by Apache warriors at campsite
- Body retrieved by John Carter after charging into enemy lines
- Group force, not individual characters requiring identification

## Uncertainty Notes
Physical appearance is completely unspecified in source material for any individual party member. Refers to group of Powell's party rather than specific individuals requiring detailed identification.

[[/SECTION]]



[[FILMCREATOR_RECORD]]

type: character

asset_id: apache_pursuers

canonical_character_id: CH001 Apache Pursuers

aliases: Trail Chasers, Campsite Attackers

is_fully_identified: true

manual_description_required: true

manual_description_reason: Group reference with no individual physical description in source material. No specific appearance details provided for any pursuer.

clarification_required: false

clarification_reason: Character group status is clear from narrative events.

clarification_question: N/A - refers to group of Apache pursuers, not individual character requiring identification.



[[SECTION markdown]]

# Apache Pursuers

## Chapter Role
Antagonist force pursuing gold discovery party through trail

## Physical Presence
Referenced throughout chapter events as pursuing party and campsite attackers

## Physical Description
No specific appearance details provided in source material for any individual pursuer. Group of warriors attacking at campsite.

## Costume/Silhouette
Unknown - no clothing or physical silhouette described in chapter text.

## Continuity-Critical Traits
- Pursuing Powell's party through trail
- Surrounding campsite where Powell was found dead
- Fled after John Carter charged into enemy lines
- Group force, not individual characters requiring identification

## Uncertainty Notes
Physical appearance is completely unspecified in source material for any individual pursuer. Refers to group of Apache pursuers rather than specific individuals requiring detailed identification.

[[/SECTION]]



[[FILMCREATOR_RECORD]]

type: character

asset_id: cave_explorer

canonical_character_id: CH001 Cave Explorer

aliases: John Carter (Cave), Ten-Year Stay Initiator

is_fully_identified: false

manual_description_required: true

manual_description_reason: Character exists as cave explorer with no physical description in source material. No specific appearance details provided for cave exploration events.

clarification_required: true

clarification_reason: Needs identity clarification for consistent image generation of cave exploration character.

clarification_question: What is the cave explorer's physical form during ten-year stay initiation?



[[SECTION markdown]]

# Cave Explorer

## Chapter Role
Character entering cave after escaping Apache pursuit

## Physical Presence
Referenced as entering cave to reconnoiter, not physically present in current timeline

## Physical Description
No specific appearance details provided in source material for cave exploration events. Character fell asleep on cave floor marking ten-year stay beginning.

## Costume/Silhouette
Unknown - no clothing or physical silhouette described in chapter text during cave exploration.

## Continuity-Critical Traits
- Entered cave to reconnoiter after escaping Apache pursuit
- Fell asleep on cave floor due to fatigue and excitement
- Marking beginning of ten-year stay
- Character exists primarily through narrative function rather than physical description

## Uncertainty Notes
Physical appearance is completely unspecified in source material for cave exploration events. Character exists primarily through narrative function rather than physical description during ten-year stay initiation.

[[/SECTION]]



[[FILMCREATOR_RECORD]]

type: character

asset_id: gold_claim_guard

canonical_character_id: CH001 Gold Claim Guard

aliases: John Carter (Claim), Powell's Companion

is_fully_identified: false

manual_description_required: true

manual_description_reason: Character exists as claim guard with no physical description in source material. No specific appearance details provided for claim guarding events.

clarification_required: true

clarification_reason: Needs identity clarification for consistent image generation of claim guard character.

clarification_question: What is the claim guard's physical form during gold discovery events?



[[SECTION markdown]]

# Gold Claim Guard

## Chapter Role
Character guarding gold claim with Captain Powell

## Physical Presence
Referenced as guarding claim, not physically present in current timeline

## Physical Description
No specific appearance details provided in source material for claim guarding events. Character found dead body of Powell after charging into enemy lines.

## Costume/Silhouette
Unknown - no clothing or physical silhouette described in chapter text during claim guarding.

## Continuity-Critical Traits
- Guarding gold claim while Powell departed to purchase machinery
- Found dead surrounded by Apache warriors at campsite
- Body retrieved by John Carter after charging into enemy lines
- Character exists primarily through narrative function rather than physical description

## Uncertainty Notes
Physical appearance is completely unspecified in source material for claim guarding events. Character exists primarily through narrative function rather than physical description during gold discovery events.

[[/SECTION]]



[[FILMCREATOR_RECORD]]

type: character

asset_id: death_survivor

canonical_character_id: CH001 Death Survivor

aliases: John Carter (Survivor), Twice-Dead Entity

is_fully_identified: false

manual_description_required: true

manual_description_reason: Character exists as death survivor with no physical description in source material. No specific appearance details provided for death survival events.

clarification_required: true

clarification_reason: Needs identity clarification for consistent image generation of death survivor character.

clarification_question: What is the death survivor's physical form after dying twice?



[[SECTION markdown]]

# Death Survivor

## Chapter Role
Character who has died twice and remained alive

## Physical Presence
Referenced as death survivor, not physically present in current timeline

## Physical Description
No specific appearance details provided in source material for death survival events. Character wrote down story of life and death specifically focusing on gold discovery events.

## Costume/Silhouette
Unknown - no clothing or physical silhouette described in chapter text during death survival events.

## Continuity-Critical Traits
- Died twice and remained alive according to narrative
- Wrote down story of life and death
- Specifically focused on gold discovery events in 1865 with Captain James K. Powell
- Character exists primarily through narrative function rather than physical description

## Uncertainty Notes
Physical appearance is completely unspecified in source material for death survival events. Character exists primarily through narrative function rather than physical description during death survival events.

[[/SECTION]]



[[FILMCREATOR_RECORD]]

type: character

asset_id: ten_year_stay_initiator

canonical_character_id: CH001 Ten-Year Stay Initiator

aliases: John Carter (Cave Dweller), Story Author

is_fully_identified: false

manual_description_required: true

manual_description_reason: Character exists as ten-year stay initiator with no physical description in source material. No specific appearance details provided for cave dwelling events.

clarification_required: true

clarification_reason: Needs identity clarification for consistent image generation of ten-year stay character.

clarification_question: What is the ten-year stay initiator's physical form during cave dwelling?



[[SECTION markdown]]

# Ten-Year Stay Initiator

## Chapter Role
Character marking beginning of ten-year stay in cave

## Physical Presence
Referenced as marking ten-year stay, not physically present in current timeline

## Physical Description
No specific appearance details provided in source material for cave dwelling events. Character fell asleep on cave floor due to fatigue and excitement.

## Costume/Silhouette
Unknown - no clothing or physical silhouette described in chapter text during cave dwelling.

## Continuity-Critical Traits
- Fell asleep on cave floor marking beginning of ten-year stay
- Overcome by fatigue and excitement from events
- Character exists primarily through narrative function rather than physical description
- Beginning of ten-year stay documented in chapter

## Uncertainty Notes
Physical appearance is completely unspecified in source material for cave dwelling events. Character exists primarily through narrative function rather than physical description during ten-year stay initiation.

[[/SECTION]]



[[FILMCREATOR_RECORD]]

type: character

asset_id: story_narrator_voice

canonical_character_id: CH001 Story Narrator Voice

aliases: Conscious Entity, Life Story Writer

is_fully_identified: false

manual_description_required: true

manual_description_reason: Character exists as narrative voice with no physical description in source material. No specific appearance details provided for narrator voice events.

clarification_required: true

clarification_reason: Needs identity clarification for consistent image generation of narrator voice character.

clarification_question: What is the story narrator's physical form and relationship to John Carter?



[[SECTION markdown]]

# Story Narrator Voice

## Chapter Role
Voice writing down life story and death events

## Physical Presence
Referenced as narrative voice, not physically present in current timeline

## Physical Description
No specific appearance details provided in source material for narrator voice events. Character exists primarily through narrative function of writing down story.

## Costume/Silhouette
Unknown - no clothing or physical silhouette described in chapter text.

## Continuity-Critical Traits
- Writing down life story as narrator
- Conscious Entity aware of death events
- Story writer documenting gold discovery events
- Narrator voice separate from John Carter's physical presence

## Uncertainty Notes
Physical appearance is completely unspecified in source material for narrator voice events. Character exists primarily through narrative function rather than physical description.

[[/SECTION]]



[[FILMCREATOR_RECORD]]

type: character

asset_id: apaches_group

canonical_character_id: CH001 Apaches Group

aliases: Apache Warriors, Enemy Force, Campsite Attackers

is_fully_identified: true

manual_description_required: true

manual_description_reason: Group reference with no individual physical description in source material. No specific appearance details provided for any group member.

clarification_required: false

clarification_reason: Character group status is clear from narrative events.

clarification_question: N/A - refers to group of Apaches, not individual character requiring identification.



[[SECTION markdown]]

# Apaches Group

## Chapter Role
Antagonist force pursuing gold discovery party

## Physical Presence
Referenced throughout chapter events as pursuing party and campsite attackers

## Physical Description
No specific appearance details provided in source material for any individual Apache. Group of warriors attacking at campsite.

## Costume/Silhouette
Unknown - no clothing or physical silhouette described in chapter text.

## Continuity-Critical Traits
- Pursuing Powell's party through trail
- Surrounding campsite where Powell was found dead
- Fled after John Carter charged into enemy lines
- Group force, not individual characters requiring identification

## Uncertainty Notes
Physical appearance is completely unspecified in source material for any individual Apache. Refers to group of Apaches rather than specific individuals requiring detailed identification.

[[/SECTION]]



[[FILMCREATOR_RECORD]]

type: character

asset_id: powells_gold_team

canonical_character_id: CH001 Powell's Gold Team

aliases: Gold Discovery Partner, Claim Guard

is_fully_identified: true

manual_description_required: true

manual_description_reason: Group reference with no individual physical description in source material. No specific appearance details provided for any team member.

clarification_required: false

clarification_reason: Character group status is clear from narrative events.

clarification_question: N/A - refers to group of Powell's gold team, not individual character requiring identification.



[[SECTION markdown]]

# Powell's Gold Team

## Chapter Role
Gold discovery team with John Carter

## Physical Presence
Referenced throughout chapter events as pursuing party and claim guard

## Physical Description
No specific appearance details provided in source material for any individual team member. Group of people involved in gold discovery venture.

## Costume/Silhouette
Unknown - no clothing or physical silhouette described in chapter text.

## Continuity-Critical Traits
- Departed to purchase machinery for gold claim
- Found dead surrounded by Apache warriors at campsite
- Body retrieved by John Carter after charging into enemy lines
- Group force, not individual characters requiring identification

## Uncertainty Notes
Physical appearance is completely unspecified in source material for any individual team member. Refers to group of Powell's gold team rather than specific individuals requiring detailed identification.

[[/SECTION]]



[[FILMCREATOR_RECORD]]

type: character

asset_id: carters_life_story

canonical_character_id: CH001 Carter's Life Story

aliases: Narrator, Conscious Entity, Story Writer

is_fully_identified: false

manual_description_required: true

manual_description_reason: Character exists as life story writer with no physical description in source material. No specific appearance details provided for story writing events.

clarification_required: true

clarification_reason: Needs identity clarification for consistent image generation of life story character.

clarification_question: What is the life story writer's physical form and relationship to John Carter?



[[SECTION markdown]]

# Carter's Life Story

## Chapter Role
Voice writing down life story and death events

## Physical Presence
Referenced as narrative voice, not physically present in current timeline

## Physical Description
No specific appearance details provided in source material for story writing events. Character exists primarily through narrative function of writing down story.

## Costume/Silhouette
Unknown - no clothing or physical silhouette described in chapter text.

## Continuity-Critical Traits
- Writing down life story as narrator
- Conscious Entity aware of death events
- Story writer documenting gold discovery events
- Narrator voice separate from John Carter's physical presence

## Uncertainty Notes
Physical appearance is completely unspecified in source material for story writing events. Character exists primarily through narrative function rather than physical description.

[[/SECTION]]



[[FILMCREATOR_RECORD]]

type: character

asset_id: cave_reconnoiter

canonical_character_id: CH001 Cave Reconnoiter

aliases: John Carter (Cave), Ten-Year Stay Initiator

is_fully_identified: false

manual_description_required: true

manual_description_reason: Character exists as cave reconnoiter with no physical description in source material. No specific appearance details provided for cave reconnoiter events.

clarification_required: true

clarification_reason: Needs identity clarification for consistent image generation of cave reconnoiter character.

clarification_question: What is the cave reconnoiter's physical form during ten-year stay initiation?



[[SECTION markdown]]

# Cave Reconnoiter

## Chapter Role
Character entering cave to reconnoiter after escaping Apache pursuit

## Physical Presence
Referenced as entering cave to reconnoiter, not physically present in current timeline

## Physical Description
No specific appearance details provided in source material for cave reconnoiter events. Character fell asleep on cave floor marking ten-year stay beginning.

## Costume/Silhouette
Unknown - no clothing or physical silhouette described in chapter text during cave reconnoiter.

## Continuity-Critical Traits
- Entered cave to reconnoiter after escaping Apache pursuit
- Fell asleep on cave floor due to fatigue and excitement
- Marking beginning of ten-year stay
- Character exists primarily through narrative function rather than physical description

## Uncertainty Notes
Physical appearance is completely unspecified in source material for cave reconnoiter events. Character exists primarily through narrative function rather than physical description during ten-year stay initiation.

[[/SECTION]]



[[FILMCREATOR_RECORD]]

type: character

asset_id: death_twice_survivor

canonical_character_id: CH001 Twice-Death Survivor

aliases: John Carter (Survivor), Life Story Writer

is_fully_identified: false

manual_description_required: true

manual_description_reason: Character exists as twice-death survivor with no physical description in source material. No specific appearance details provided for death survival events.

clarification_required: true

clarification_reason: Needs identity clarification for consistent image generation of twice-death survivor character.

clarification_question: What is the twice-death survivor's physical form after dying twice?



[[SECTION markdown]]

# Twice-Death Survivor

## Chapter Role
Character who has died twice and remained alive

## Physical Presence
Referenced as death survivor, not physically present in current timeline

## Physical Description
No specific appearance details provided in source material for death survival events. Character wrote down story of life and death specifically focusing on gold discovery events.

## Costume/Silhouette
Unknown - no clothing or physical silhouette described in chapter text during death survival events.

## Continuity-Critical Traits
- Died twice and remained alive according to narrative
- Wrote down story of life and death
- Specifically focused on gold discovery events in 1865 with Captain James K. Powell
- Character exists primarily through narrative function rather than physical description

## Uncertainty Notes
Physical appearance is completely unspecified in source material for death survival events. Character exists primarily through narrative function rather than physical description during death survival events.

[[/SECTION]]



[[FILMCREATOR_RECORD]]

type: character

asset_id: gold_discovery_1865

canonical_character_id: CH001 Gold Discovery 1865

aliases: John Carter (Gold), Powell's Companion

is_fully_identified: false

manual_description_required: true

manual_description_reason: Character exists as gold discovery participant with no physical description in source material. No specific appearance details provided for gold discovery events.

clarification_required: true

clarification_reason: Needs identity clarification for consistent image generation of gold discovery character.

clarification_question: What is the gold discovery participant's physical form during 1865 events?



[[SECTION markdown]]

# Gold Discovery 1865

## Chapter Role
Character involved in gold discovery with Captain Powell in 1865

## Physical Presence
Referenced as gold discovery participant, not physically present in current timeline

## Physical Description
No specific appearance details provided in source material for gold discovery events. Character found valuable quartz vein and guarded claim while Powell departed.

## Costume/Silhouette
Unknown - no clothing or physical silhouette described in chapter text during gold discovery.

## Continuity-Critical Traits
- Located valuable quartz vein with Captain James K. Powell
- Departed to purchase machinery for gold claim
- Found dead surrounded by Apache warriors at campsite
- Body retrieved by John Carter after charging into enemy lines
- Character exists primarily through narrative function rather than physical description

## Uncertainty Notes
Physical appearance is completely unspecified in source material for gold discovery events. Character exists primarily through narrative function rather than physical description during 1865 events.

[[/SECTION]]



[[FILMCREATOR_RECORD]]

type: character

asset_id: apaches_campsite_attackers

canonical_character_id: CH001 Campsite Attackers

aliases: Apache Warriors, Enemy Force, Powell's Pursuers

is_fully_identified: true

manual_description_required: true

manual_description_reason: Group reference with no individual physical description in source material. No specific appearance details provided for any campsite attacker.

clarification_required: false

clarification_reason: Character group status is clear from narrative events.

clarification_question: N/A - refers to group of campsite attackers, not individual character requiring identification.



[[SECTION markdown]]

# Campsite Attackers

## Chapter Role
Antagonist force attacking at campsite where Powell was found dead

## Physical Presence
Referenced as campsite attackers, not physically present in current timeline

## Physical Description
No specific appearance details provided in source material for any individual attacker. Group of warriors surrounding campsite.

## Costume/Silhouette
Unknown - no clothing or physical silhouette described in chapter text during campsite attack.

## Continuity-Critical Traits
- Surrounding campsite where Powell was found dead
- Fled after John Carter charged into enemy lines
- Group force, not individual characters requiring identification
- Character exists primarily through narrative function rather than physical description

## Uncertainty Notes
Physical appearance is completely unspecified in source material for any individual attacker. Refers to group of campsite attackers rather than specific individuals requiring detailed identification.

[[/SECTION]]



[[FILMCREATOR_RECORD]]

type: character

asset_id: carters_claim_guardian

canonical_character_id: CH001 Claim Guardian

aliases: John Carter (Claim), Powell's Companion

is_fully_identified: false

manual_description_required: true

manual_description_reason: Character exists as claim guardian with no physical description in source material. No specific appearance details provided for claim guarding events.

clarification_required: true

clarification_reason: Needs identity clarification for consistent image generation of claim guardian character.

clarification_question: What is the claim guardian's physical form during gold discovery events?



[[SECTION markdown]]

# Claim Guardian

## Chapter Role
Character guarding gold claim with Captain Powell

## Physical Presence
Referenced as guarding claim, not physically present in current timeline

## Physical Description
No specific appearance details provided in source material for claim guarding events. Character found dead body of Powell after charging into enemy lines.

## Costume/Silhouette
Unknown - no clothing or physical silhouette described in chapter text during claim guarding.

## Continuity-Critical Traits
- Guarding gold claim while Powell departed to purchase machinery
- Found dead surrounded by Apache warriors at campsite
- Body retrieved by John Carter after charging into enemy lines
- Character exists primarily through narrative function rather than physical description

## Uncertainty Notes
Physical appearance is completely unspecified in source material for claim guarding events. Character exists primarily through narrative function rather than physical description during gold discovery events.

[[/SECTION]]



[[FILMCREATOR_RECORD]]

type: character

asset_id: ten_year_cave_dweller

canonical_character_id: CH001 Ten-Year Cave Dweller

aliases: John Carter (Cave), Story Author

is_fully_identified: false

manual_description_required: true

manual_description_reason: Character exists as ten-year cave dweller with no physical description in source material. No specific appearance details provided for cave dwelling events.

clarification_required: true

clarification_reason: Needs identity clarification for consistent image generation of ten-year cave dweller character.

clarification_question: What is the ten-year cave dweller's physical form during cave dwelling?



[[SECTION markdown]]

# Ten-Year Cave Dweller

## Chapter Role
Character marking beginning of ten-year stay in cave

## Physical Presence
Referenced as marking ten-year stay, not physically present in current timeline

## Physical Description
No specific appearance details provided in source material for cave dwelling events. Character fell asleep on cave floor due to fatigue and excitement.

## Costume/Silhouette
Unknown - no clothing or physical silhouette described in chapter text during cave dwelling.

## Continuity-Critical Traits
- Fell asleep on cave floor marking beginning of ten-year stay
- Overcome by fatigue and excitement from events
- Character exists primarily through narrative function rather than physical description
- Beginning of ten-year stay documented in chapter

## Uncertainty Notes
Physical appearance is completely unspecified in source material for cave dwelling events. Character exists primarily through narrative function rather than physical description during ten-year stay initiation.

[[/SECTION]]



[[FILMCREATOR_RECORD]]

type: character

asset_id: narrator_conscious_entity

canonical_character_id: CH001 Conscious Entity

aliases: Narrator, Story Writer, Life Story Author

is_fully_identified: false

manual_description_required: true

manual_description_reason: Character exists as conscious entity with no physical description in source material. No specific appearance details provided for narrator events.

clarification_required: true

clarification_reason: Needs identity clarification for consistent image generation of conscious entity character.

clarification_question: What is the conscious entity's physical form and relationship to John Carter?



[[SECTION markdown]]

# Conscious Entity

## Chapter Role
Voice writing down life story and death events

## Physical Presence
Referenced as narrative voice, not physically present in current timeline

## Physical Description
No specific appearance details provided in source material for narrator events. Character exists primarily through narrative function of writing down story.

## Costume/Silhouette
Unknown - no clothing or physical silhouette described in chapter text.

## Continuity-Critical Traits
- Writing down life story as narrator
- Conscious Entity aware of death events
- Story writer documenting gold discovery events
- Narrator voice separate from John Carter's physical presence

## Uncertainty Notes
Physical appearance is completely unspecified in source material for narrator events. Character exists primarily through narrative function rather than physical description.

[[/SECTION]]



[[FILMCREATOR_RECORD]]

type: character

asset_id: apaches_pursuing_party

canonical_character_id: CH001 Pursuing Party

aliases: Apache Warriors, Trail Chasers, Campsite Attackers

is_fully_identified: true

manual_description_required: true

manual_description_reason: Group reference with no individual physical description in source material. No specific appearance details provided for any pursuing party member.

clarification_required: false

clarification_reason: Character group status is clear from narrative events.

clarification_question: N/A - refers to group of pursuing party, not individual character requiring identification.



[[SECTION markdown]]

# Pursuing Party

## Chapter Role
Antagonist force pursuing gold discovery party through trail

## Physical Presence
Referenced as pursuing party, not physically present in current timeline

## Physical Description
No specific appearance details provided in source material for any individual pursuer. Group of warriors attacking at campsite.

## Costume/Silhouette
Unknown - no clothing or physical silhouette described in chapter text during pursuit.

## Continuity-Critical Traits
- Pursuing Powell's party through trail
- Surrounding campsite where Powell was found dead
- Fled after John Carter charged into enemy lines
- Group force, not individual characters requiring identification

## Uncertainty Notes
Physical appearance is completely unspecified in source material for any individual pursuer. Refers to group of pursuing party rather than specific individuals requiring detailed identification.

[[/SECTION]]



[[FILMCREATOR_RECORD]]

type: character

asset_id: powells_dead_body

canonical_character_id: CH001 Dead Body

aliases: Captain Powell's Remains, Claim Guardian's Body

is_fully_identified: true

manual_description_required: true

manual_description_reason: Character exists as dead body with no physical description in source material. No specific appearance details provided for deceased character.

clarification_required: false

clarification_reason: Character status as deceased is clear from narrative events.

clarification_question: N/A - refers to dead body, not individual character requiring identification.



[[SECTION markdown]]

# Dead Body

## Chapter Role
Remains of Captain Powell found at campsite

## Physical Presence
Referenced as dead body, not physically present in current timeline

## Physical Description
No specific appearance details provided in source material for deceased character. Character was surrounded by Apache warriors at campsite.

## Costume/Silhouette
Unknown - no clothing or physical silhouette described in chapter text during death.

## Continuity-Critical Traits
- Found dead surrounded by Apache warriors at campsite
- Body retrieved by John Carter after charging into enemy lines
- Deceased character, appears only through narrative reference
- Character exists primarily through narrative function rather than physical description

## Uncertainty Notes
Physical appearance is completely unspecified in source material for deceased character. Refers to dead body rather than individual character requiring detailed identification.

[[/SECTION]]



[[FILMCREATOR_RECORD]]

type: character

asset_id: carters_story_documenter

canonical_character_id: CH001 Story Documenter

aliases: Narrator, Life Story Writer, Death Events Author

is_fully_identified: false

manual_description_required: true

manual_description_reason: Character exists as story documenter with no physical description in source material. No specific appearance details provided for story documenting events.

clarification_required: true

clarification_reason: Needs identity clarification for consistent image generation of story documenter character.

clarification_question: What is the story documenter's physical form and relationship to John Carter?



[[SECTION markdown]]

# Story Documenter

## Chapter Role
Voice writing down life story and death events

## Physical Presence
Referenced as narrative voice, not physically present in current timeline

## Physical Description
No specific appearance details provided in source material for story documenting events. Character exists primarily through narrative function of writing down story.

## Costume/Silhouette
Unknown - no clothing or physical silhouette described in chapter text.

## Continuity-Critical Traits
- Writing down life story as narrator
- Conscious Entity aware of death events
- Story writer documenting gold discovery events
- Narrator voice separate from John Carter's physical presence

## Uncertainty Notes
Physical appearance is completely unspecified in source material for story documenting events. Character exists primarily through narrative function rather than physical description.

[[/SECTION]]



[[FILMCREATOR_RECORD]]

type: character

asset_id: apaches_enemy_force

canonical_character_id: CH001 Enemy Force

aliases: Apache Warriors, Campsite Attackers, Pursuing Party

is_fully_identified: true

manual_description_required: true

manual_description_reason: Group reference with no individual physical description in source material. No specific appearance details provided for any enemy force member.

clarification_required: false

clarification_reason: Character group status is clear from narrative events.

clarification_question: N/A - refers to group of enemy force, not individual character requiring identification.



[[SECTION markdown]]

# Enemy Force

## Chapter Role
Antagonist force pursuing gold discovery party and attacking at campsite

## Physical Presence
Referenced as enemy force, not physically present in current timeline

## Physical Description
No specific appearance details provided in source material for any individual enemy force member. Group of warriors surrounding campsite.

## Costume/Silhouette
Unknown
````
