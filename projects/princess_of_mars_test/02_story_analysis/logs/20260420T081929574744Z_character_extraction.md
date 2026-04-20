# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-20T08:19:29.574744+00:00
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

Chapter id: CH024

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

In Chapter XXIV, John Carter crashes his craft into a fierce battle between Tharks and Warhoons on ancient Mars. He saves Tars Tarkas from death by Warhoons, earning the green warrior's respect and friendship. Woola, the dog, also returns to Thark. Tars Tarkas brings John Carter before Jeddak Tal Hajus, who seeks revenge for a previous injury. During a council meeting, John Carter exposes Tal Hajus as a coward unfit to rule. The Thark council votes to challenge Tal Hajus to combat with Tars Tarkas. Tars Tarkas wins and becomes the new Jeddak of Thark. He is made a chieftain and proposes an alliance with Helium to rescue Dejah Thoris from Zodanga. The Tharks agree, gathering a massive force of 150,000 warriors. They march on Zodanga and enter the city through a gate constructed by John Carter using his men as steps.
````

## Raw Response
````text


[[FILMCREATOR_PACKET]]

task: character_extraction

version: 1

character_index_markdown:

[[SECTION character_index_markdown]]

# Character Index - Chapter XXIV

| Asset ID | Canonical Character ID | Aliases | Fully Identified | Manual Description Required |
|----------|------------------------|---------|------------------|----------------------------|
| john_carter | CH001 John Carter | Protagonist, Green Warrior | true | false |
| tars_tarkas | CH002 Tars Tarkas | Jeddak of Thark, Chieftain | true | false |
| woola | CH003 Woola | Dog, Companion | true | false |
| tal_hajus | CH004 Tal Hajus | Jeddak (former) | true | false |
| dejah_thoris | CH005 Dejah Thoris | Princess of Helium | false | true |

[[/SECTION]]



[[FILMCREATOR_RECORD]]

type: character

asset_id: john_carter

canonical_character_id: CH001 John Carter

aliases: Protagonist, Green Warrior

is_fully_identified: true

manual_description_required: false

manual_description_reason: 

clarification_required: false

clarification_reason: 

clarification_question: 

[[SECTION markdown]]

# John Carter

**Chapter Role:** Protagonist, crash-landed visitor from Helium

**Physical Presence:** Referenced throughout chapter as active participant in battle and council

**Physical Description:** Green-skinned warrior with muscular build, wearing Thark-style armor. Crashed his craft into Mars surface during fierce battle between Tharks and Warhoons.

**Costume/Silhouette:** Woola's dog companion nearby. Used men as steps to construct gate for city entry.

**Continuity-Critical Traits:** Saved Tars Tarkas from death, exposed Tal Hajus as coward, constructed gate using men as steps, proposed alliance with Helium to rescue Dejah Thoris.

[[/SECTION]]



[[FILMCREATOR_RECORD]]

type: character

asset_id: tars_tarkas

canonical_character_id: CH002 Tars Tarkas

aliases: Jeddak of Thark, Chieftain, Green Warrior

is_fully_identified: true

manual_description_required: false

manual_description_reason: 

clarification_required: false

clarification_reason: 

clarification_question: 

[[SECTION markdown]]

# Tars Tarkas

**Chapter Role:** Former Jeddak of Thark, becomes new Chieftain

**Physical Presence:** Active participant in battle and council meetings

**Physical Description:** Green-skinned warrior with muscular build. Saved from death by Warhoons by John Carter. Won combat challenge against Tal Hajus to become new Jeddak.

**Costume/Silhouette:** Woola's dog companion nearby. Proposed alliance with Helium after becoming chieftain.

**Continuity-Critical Traits:** Earned John Carter's respect and friendship, won combat challenge against Tal Hajus, became new Jeddak of Thark, proposed alliance with Helium to rescue Dejah Thoris from Zodanga, gathered force of 150,000 warriors for march on Zodanga.

[[/SECTION]]



[[FILMCREATOR_RECORD]]

type: character

asset_id: woola

canonical_character_id: CH003 Woola

aliases: Dog, Companion, Thark's Dog

is_fully_identified: true

manual_description_required: false

manual_description_reason: 

clarification_required: false

clarification_reason: 

clarification_question: 

[[SECTION markdown]]

# Woola

**Chapter Role:** Dog companion of John Carter and Tars Tarkas

**Physical Presence:** Referenced as returning to Thark after battle

**Physical Description:** Dog with leashed appearance, loyal companion. Returned to Thark alongside John Carter's arrival.

**Costume/Silhouette:** Leashed dog companion, appears near both John Carter and Tars Tarkas throughout chapter events.

**Continuity-Critical Traits:** Loyal companion who returned to Thark during John Carter's crash landing and subsequent council meetings.

[[/SECTION]]



[[FILMCREATOR_RECORD]]

type: character

asset_id: tal_hajus

canonical_character_id: CH004 Tal Hajus

aliases: Jeddak (former), Former Chieftain, Coward

is_fully_identified: true

manual_description_required: false

manual_description_reason: 

clarification_required: false

clarification_reason: 

clarification_question: 

[[SECTION markdown]]

# Tal Hajus

**Chapter Role:** Former Jeddak of Thark, exposed as coward

**Physical Presence:** Active participant in council meeting where he was challenged

**Physical Description:** Green-skinned warrior with muscular build. Sought revenge for previous injury to John Carter. Exposed as coward unfit to rule during council meeting.

**Costume/Silhouette:** Woola's dog companion nearby. Lost combat challenge against Tars Tarkas, resulting in removal from Jeddak position.

**Continuity-Critical Traits:** Sought revenge for previous injury, exposed as coward by John Carter during council meeting, voted out of Jeddak position after losing combat challenge to Tars Tarkas.

[[/SECTION]]



[[FILMCREATOR_RECORD]]

type: character

asset_id: dejah_thoris

canonical_character_id: CH005 Dejah Thoris

aliases: Princess of Helium, Queen of Helium

is_fully_identified: false

manual_description_required: true

manual_description_reason: Only mentioned in passing as rescue target from Zodanga; no physical description provided in chapter material.

clarification_required: true

clarification_reason: Needs identity clarification for accurate image generation and character consistency.

clarification_question: What is Dejah Thoris's current physical appearance, attire, and location during the alliance proposal?

[[SECTION markdown]]

# Dejah Thoris

**Chapter Role:** Princess of Helium, rescue target from Zodanga

**Physical Presence:** Referenced only in passing as alliance objective; not physically present in chapter events.

**Physical Description:** Unknown - no physical description provided in Chapter XXIV material. Mentioned only as rescue target from Zodanga during Tars Tarkas's alliance proposal.

**Costume/Silhouette:** Unknown - costume and silhouette details not available in chapter source material.

**Continuity-Critical Traits:** Rescue objective for Thark alliance with Helium, captured by Zodanga forces requiring military intervention to liberate.

[[/SECTION]]



[[FILMCREATOR_RECORD]]

type: character

asset_id: thark_council

canonical_character_id: CH006 Thark Council

aliases: Council Members, Warriors, Chieftains

is_fully_identified: false

manual_description_required: true

manual_description_reason: Collective group with no individual physical descriptions; only referenced as voting body in council meeting.

clarification_required: true

clarification_reason: Needs identity clarification for accurate image generation and character consistency.

clarification_question: What are the physical appearances, attire, and positioning of individual Thark Council members during the combat vote?

[[SECTION markdown]]

# Thark Council

**Chapter Role:** Voting body in council meeting, decides Jeddak succession

**Physical Presence:** Referenced as collective group during council meeting; not individually detailed.

**Physical Description:** Collective green-skinned warriors with muscular builds. No individual physical descriptions provided in chapter material.

**Costume/Silhouette:** Thark-style armor and weapons. Positioned around council chamber during voting proceedings.

**Continuity-Critical Traits:** Voted to challenge Tal Hajus to combat with Tars Tarkas, voted out former Jeddak after losing challenge, gathered force of 150,000 warriors for march on Zodanga.

[[/SECTION]]



[[FILMCREATOR_RECORD]]

type: character

asset_id: warhoons

canonical_character_id: CH007 Warhoons

aliases: Enemy Warriors, Battle Opponents

is_fully_identified: false

manual_description_required: true

manual_description_reason: Collective group referenced only as battle opponents; no individual physical descriptions provided in chapter material.

clarification_required: true

clarification_reason: Needs identity clarification for accurate image generation and character consistency.

clarification_question: What are the physical appearances, attire, and positioning of Warhoon warriors during the battle with John Carter's craft?

[[SECTION markdown]]

# Warhoons

**Chapter Role:** Enemy warriors in fierce battle on Mars surface

**Physical Presence:** Referenced as battle opponents during John Carter's crash landing; not individually detailed.

**Physical Description:** Collective green-skinned warriors with muscular builds. No individual physical descriptions provided in chapter material.

**Costume/Silhouette:** Thark-style armor and weapons. Positioned around battle site during fierce combat between Tharks and Warhoons.

**Continuity-Critical Traits:** Attempted to kill Tars Tarkas before John Carter's intervention, engaged in fierce battle on Mars surface during crash landing sequence.

[[/SECTION]]



[[FILMCREATOR_RECORD]]

type: character

asset_id: zodanga_forces

canonical_character_id: CH008 Zodanga Forces

aliases: Enemy Army, Zodanga Warriors

is_fully_identified: false

manual_description_required: true

manual_description_reason: Collective group referenced only as rescue target location; no individual physical descriptions provided in chapter material.

clarification_required: true

clarification_reason: Needs identity clarification for accurate image generation and character consistency.

clarification_question: What are the physical appearances, attire, and positioning of Zodanga forces during the planned military march on their city?

[[SECTION markdown]]

# Zodanga Forces

**Chapter Role:** Enemy army holding Dejah Thoris captive in Zodanga city

**Physical Presence:** Referenced only as rescue target location; not physically present in chapter events.

**Physical Description:** Collective green-skinned warriors with muscular builds. No individual physical descriptions provided in chapter material.

**Costume/Silhouette:** Thark-style armor and weapons. Positioned within Zodanga city gates constructed by John Carter's men.

**Continuity-Critical Traits:** Captured Dejah Thoris requiring military intervention, planned march on their city through gate constructed by John Carter using men as steps.

[[/SECTION]]



[[FILMCREATOR_RECORD]]

type: character

asset_id: mars_surface

canonical_character_id: CH009 Mars Surface

aliases: Ancient Mars, Battle Ground

is_fully_identified: false

manual_description_required: true

manual_description_reason: Environmental setting referenced only as location; no individual physical descriptions provided in chapter material.

clarification_required: true

clarification_reason: Needs identity clarification for accurate image generation and character consistency.

clarification_question: What are the specific environmental features, terrain details, and atmospheric conditions of ancient Mars during the battle sequence?

[[SECTION markdown]]

# Mars Surface

**Chapter Role:** Ancient battle ground between Tharks and Warhoons

**Physical Presence:** Referenced as location of crash landing and fierce battle; not individually detailed.

**Physical Description:** Ancient Martian terrain with green-skinned warrior population. No individual physical descriptions provided in chapter material.

**Costume/Silhouette:** Thark-style armor and weapons throughout battle site. Positioned around ancient Mars surface during crash landing sequence.

**Continuity-Critical Traits:** Location of John Carter's craft crash, fierce battle between Tharks and Warhoons, Tars Tarkas rescue from death by Warhoons, council meeting location for Jeddak succession vote.

[[/SECTION]]



[[FILMCREATOR_RECORD]]

type: character

asset_id: helium_alliance

canonical_character_id: CH010 Helium Alliance

aliases: Rescue Force, Helium Warriors

is_fully_identified: false

manual_description_required: true

manual_description_reason: Collective group referenced only as alliance partner; no individual physical descriptions provided in chapter material.

clarification_required: true

clarification_reason: Needs identity clarification for accurate image generation and character consistency.

clarification_question: What are the physical appearances, attire, and positioning of Helium alliance warriors during the proposed rescue mission from Zodanga?

[[SECTION markdown]]

# Helium Alliance

**Chapter Role:** Rescue force proposed by Tars Tarkas to save Dejah Thoris

**Physical Presence:** Referenced only as alliance partner; not physically present in chapter events.

**Physical Description:** Collective green-skinned warriors with muscular builds. No individual physical descriptions provided in chapter material.

**Costume/Silhouette:** Thark-style armor and weapons. Positioned around proposed rescue mission from Zodanga city.

**Continuity-Critical Traits:** Proposed alliance partner for rescue of Dejah Thoris from Zodanga, gathered force of 150,000 warriors for march on Zodanga, agreed to military intervention after Tars Tarkas's proposal.

[[/SECTION]]



[[FILMCREATOR_RECORD]]

type: character

asset_id: gate_construction

canonical_character_id: CH011 Gate Construction

aliases: City Entry Point, Step Gate

is_fully_identified: false

manual_description_required: true

manual_description_reason: Environmental feature referenced only as city entry point; no individual physical descriptions provided in chapter material.

clarification_required: true

clarification_reason: Needs identity clarification for accurate image generation and character consistency.

clarification_question: What are the specific dimensions, materials, and construction details of the gate built by John Carter's men using steps?

[[SECTION markdown]]

# Gate Construction

**Chapter Role:** City entry point constructed by John Carter's men

**Physical Presence:** Referenced as city entry point for Zodanga; not individually detailed.

**Physical Description:** Gate constructed using John Carter's men as steps. No individual physical descriptions provided in chapter material.

**Costume/Silhouette:** Thark-style armor and weapons throughout gate construction site. Positioned at Zodanga city entrance during march on their city.

**Continuity-Critical Traits:** Constructed by John Carter's men using them as steps, allowed entry into Zodanga city during military march, enabled rescue operation for Dejah Thoris from Zodanga forces.

[[/SECTION]]



[[FILMCREATOR_RECORD]]

type: character

asset_id: thark_chief_position

canonical_character_id: CH012 Thark Chief Position

aliases: Chieftain Title, Leadership Role

is_fully_identified: false

manual_description_required: true

manual_description_reason: Positional title referenced only as leadership role; no individual physical descriptions provided in chapter material.

clarification_required: true

clarification_reason: Needs identity clarification for accurate image generation and character consistency.

clarification_question: What are the specific ceremonial details, attire, and positioning associated with the Thark chieftain position after Tars Tarkas's victory?

[[SECTION markdown]]

# Thark Chief Position

**Chapter Role:** Leadership title awarded to Tars Tarkas after combat victory

**Physical Presence:** Referenced only as leadership role; not individually detailed.

**Physical Description:** Green-skinned warrior with muscular build. No individual physical descriptions provided in chapter material.

**Costume/Silhouette:** Thark-style armor and weapons. Positioned as new Jeddak of Thark after winning combat challenge against Tal Hajus.

**Continuity-Critical Traits:** Awarded to Tars Tarkas after winning combat challenge against Tal Hajus, proposed alliance with Helium to rescue Dejah Thoris from Zodanga, gathered force of 150,000 warriors for march on Zodanga.

[[/SECTION]]



[[FILMCREATOR_RECORD]]

type: character

asset_id: jeddak_position

canonical_character_id: CH013 Jeddak Position

aliases: Former Jeddak, Leadership Title

is_fully_identified: false

manual_description_required: true

manual_description_reason: Positional title referenced only as leadership role; no individual physical descriptions provided in chapter material.

clarification_required: true

clarification_reason: Needs identity clarification for accurate image generation and character consistency.

clarification_question: What are the specific ceremonial details, attire, and positioning associated with the Jeddak position before Tal Hajus's removal?

[[SECTION markdown]]

# Jeddak Position

**Chapter Role:** Leadership title held by Tal Hajus before combat challenge

**Physical Presence:** Referenced only as leadership role; not individually detailed.

**Physical Description:** Green-skinned warrior with muscular build. No individual physical descriptions provided in chapter material.

**Costume/Silhouette:** Thark-style armor and weapons. Positioned as former Jeddak of Thark before losing combat challenge to Tars Tarkas.

**Continuity-Critical Traits:** Held by Tal Hajus seeking revenge for previous injury, exposed as coward by John Carter during council meeting, voted out after losing combat challenge to Tars Tarkas.

[[/SECTION]]



[[FILMCREATOR_RECORD]]

type: character

asset_id: thark_warriors_collective

canonical_character_id: CH014 Thark Warriors Collective

aliases: Warrior Force, Battle Army

is_fully_identified: false

manual_description_required: true

manual_description_reason: Collective group referenced only as warrior force; no individual physical descriptions provided in chapter material.

clarification_required: true

clarification_reason: Needs identity clarification for accurate image generation and character consistency.

clarification_question: What are the specific formations, attire, and positioning of Thark warriors during the march on Zodanga with 150,000 warriors?

[[SECTION markdown]]

# Thark Warriors Collective

**Chapter Role:** Warrior force gathered by Tars Tarkas for rescue mission

**Physical Presence:** Referenced only as warrior force; not individually detailed.

**Physical Description:** Collective green-skinned warriors with muscular builds. No individual physical descriptions provided in chapter material.

**Costume/Silhouette:** Thark-style armor and weapons throughout warrior formation. Positioned around march on Zodanga city through gate constructed by John Carter's men.

**Continuity-Critical Traits:** Gathered force of 150,000 warriors for march on Zodanga, marched on Zodanga after alliance proposal with Helium, entered city through gate constructed by John Carter using men as steps.

[[/SECTION]]



[[FILMCREATOR_RECORD]]

type: character

asset_id: council_meeting_location

canonical_character_id: CH015 Council Meeting Location

aliases: Thark Council Chamber, Voting Room

is_fully_identified: false

manual_description_required: true

manual_description_reason: Environmental feature referenced only as meeting location; no individual physical descriptions provided in chapter material.

clarification_required: true

clarification_reason: Needs identity clarification for accurate image generation and character consistency.

clarification_question: What are the specific architectural details, seating arrangements, and ceremonial features of the Thark council chamber during the Jeddak succession vote?

[[SECTION markdown]]

# Council Meeting Location

**Chapter Role:** Venue for Jeddak succession vote and Tal Hajus exposure

**Physical Presence:** Referenced only as meeting location; not individually detailed.

**Physical Description:** Green-skinned warrior population with muscular builds. No individual physical descriptions provided in chapter material.

**Costume/Silhouette:** Thark-style armor and weapons throughout council chamber. Positioned around voting proceedings during Jeddak succession vote.

**Continuity-Critical Traits:** Venue for John Carter's exposure of Tal Hajus as coward, voting body for combat challenge against Tal Hajus with Tars Tarkas, location where Tars Tarkas won and became new Jeddak of Thark.

[[/SECTION]]



[[FILMCREATOR_RECORD]]

type: character

asset_id: zodanga_city

canonical_character_id: CH016 Zodanga City

aliases: Enemy Capital, Rescue Target Location

is_fully_identified: false

manual_description_required: true

manual_description_reason: Environmental feature referenced only as rescue target location; no individual physical descriptions provided in chapter material.

clarification_required: true

clarification_reason: Needs identity clarification for accurate image generation and character consistency.

clarification_question: What are the specific architectural details, gate structures, and defensive features of Zodanga city during the planned military march?

[[SECTION markdown]]

# Zodanga City

**Chapter Role:** Enemy capital holding Dejah Thoris captive

**Physical Presence:** Referenced only as rescue target location; not individually detailed.

**Physical Description:** Green-skinned warrior population with muscular builds. No individual physical descriptions provided in chapter material.

**Costume/Silhouette:** Thark-style armor and weapons throughout city gates. Positioned at Zodanga city entrance during march on their city through gate constructed by John Carter's men.

**Continuity-Critical Traits:** Captured Dejah Thoris requiring rescue operation, entered through gate constructed by John Carter using men as steps, planned military march with 150,000 Thark warriors for liberation of Princess from Zodanga forces.

[[/SECTION]]



[[FILMCREATOR_RECORD]]

type: character

asset_id: crash_landing_site

canonical_character_id: CH017 Crash Landing Site

aliases: Craft Impact Point, Battle Ground Start

is_fully_identified: false

manual_description_required: true

manual_description_reason: Environmental feature referenced only as crash landing location; no individual physical descriptions provided in chapter material.

clarification_required: true

clarification_reason: Needs identity clarification for accurate image generation and character consistency.

clarification_question: What are the specific terrain features, atmospheric conditions, and battle damage details of John Carter's craft crash landing site on ancient Mars?

[[SECTION markdown]]

# Crash Landing Site

**Chapter Role:** Location of John Carter's craft impact during fierce battle

**Physical Presence:** Referenced only as crash landing location; not individually detailed.

**Physical Description:** Ancient Martian terrain with green-skinned warrior population. No individual physical descriptions provided in chapter material.

**Costume/Silhouette:** Thark-style armor and weapons throughout crash site. Positioned around battle between Tharks and Warhoons during John Carter's craft impact.

**Continuity-Critical Traits:** Location of John Carter's craft crash into fierce battle between Tharks and Warhoons on ancient Mars, saved Tars Tarkas from death by Warhoons, earned green warrior's respect and friendship, Woola dog returned to Thark alongside crash landing sequence.

[[/SECTION]]



[[FILMCREATOR_RECORD]]

type: character

asset_id: battle_sequence

canonical_character_id: CH018 Battle Sequence

aliases: Fierce Combat, Mars Surface Fight

is_fully_identified: false

manual_description_required: true

manual_description_reason: Environmental event referenced only as battle sequence; no individual physical descriptions provided in chapter material.

clarification_required: true

clarification_reason: Needs identity clarification for accurate image generation and character consistency.

clarification_question: What are the specific combat formations, weapon types, and battle damage details during the fierce battle between Tharks and Warhoons on ancient Mars?

[[SECTION markdown]]

# Battle Sequence

**Chapter Role:** Fierce combat between Tharks and Warhoons on ancient Mars

**Physical Presence:** Referenced only as battle sequence; not individually detailed.

**Physical Description:** Green-skinned warrior population with muscular builds. No individual physical descriptions provided in chapter material.

**Costume/Silhouette:** Thark-style armor and weapons throughout battle site. Positioned around fierce combat between Tharks and Warhoons during John Carter's craft crash landing.

**Continuity-Critical Traits:** Fierce battle between Tharks and Warhoons on ancient Mars, John Carter crashed his craft into battle sequence, saved Tars Tarkas from death by Warhoons, earned green warrior's respect and friendship, Woola dog returned to Thark during battle sequence aftermath.

[[/SECTION]]



[[FILMCREATOR_RECORD]]

type: character

asset_id: rescue_mission_proposal

canonical_character_id: CH019 Rescue Mission Proposal

aliases: Alliance Offer, Helium Rescue Plan

is_fully_identified: false

manual_description_required: true

manual_description_reason: Event referenced only as proposal; no individual physical descriptions provided in chapter material.

clarification_required: true

clarification_reason: Needs identity clarification for accurate image generation and character consistency.

clarification_question: What are the specific ceremonial details, warrior formations, and logistical arrangements of Tars Tarkas's alliance proposal with Helium to rescue Dejah Thoris from Zodanga?

[[SECTION markdown]]

# Rescue Mission Proposal

**Chapter Role:** Alliance offer by Tars Tarkas to rescue Dejah Thoris from Zodanga

**Physical Presence:** Referenced only as proposal; not individually detailed.

**Physical Description:** Green-skinned warrior population with muscular builds. No individual physical descriptions provided in chapter material.

**Costume/Silhouette:** Thark-style armor and weapons throughout proposal ceremony. Positioned around alliance offer with Helium to rescue Dejah Thoris from Zodanga city.

**Continuity-Critical Traits:** Proposed by Tars Tarkas after becoming chieftain, made to gather force of 150,000 warriors for march on Zodanga, Tharks agreed to military intervention after alliance proposal with Helium, gathered massive force for rescue mission from Zodanga forces.

[[/SECTION]]



[[FILMCREATOR_RECORD]]

type: character

asset_id: thark_agreement

canonical_character_id: CH020 Thark Agreement

aliases: Council Vote, Alliance Acceptance

is_fully_identified: false

manual_description_required: true

manual_description_reason: Event referenced only as agreement; no individual physical descriptions provided in chapter material.

clarification_required: true

clarification_reason: Needs identity clarification for accurate image generation and character consistency.

clarification_question: What are the specific ceremonial details, warrior formations, and voting arrangements of Thark council's agreement to march on Zodanga after alliance proposal with Helium?

[[SECTION markdown]]

# Thark Agreement

**Chapter Role:** Council vote accepting alliance proposal with Helium for rescue mission

**Physical Presence:** Referenced only as agreement; not individually detailed.

**Physical Description:** Green-skinned warrior population with muscular builds. No individual physical descriptions provided in chapter material.

**Costume/Silhouette:** Thark-style armor and weapons throughout council chamber. Positioned around voting proceedings during alliance acceptance with Helium to rescue Dejah Thoris from Zodanga.

**Continuity-Critical Traits:** Voted to accept alliance proposal with Helium after Tars Tarkas's offer, gathered force of 150,000 warriors for march on Zodanga, agreed to military intervention after alliance proposal with Helium, marched on Zodanga and entered city through gate constructed by John Carter using men as steps.

[[/SECTION]]



[[FILMCREATOR_RECORD]]

type: character

asset_id: march_on_zodanga

canonical_character_id: CH021 March on Zodanga

aliases: Military Campaign, Rescue Expedition

is_fully_identified: false

manual_description_required: true

manual_description_reason: Event referenced only as military campaign; no individual physical descriptions provided in chapter material.

clarification_required: true

clarification_reason: Needs identity clarification for accurate image generation and character consistency.

clarification_question: What are the specific formations, weapon types, and battle damage details during the march on Zodanga with 150,000 Thark warriors through gate constructed by John Carter's men?

[[SECTION markdown]]

# March on Zodanga

**Chapter Role:** Military campaign to rescue Dejah Thoris from Zodanga city

**Physical Presence:** Referenced only as military campaign; not individually detailed.

**Physical Description:** Green-skinned warrior population with muscular builds. No individual physical descriptions provided in chapter material.

**Costume/Silhouette:** Thark-style armor and weapons throughout march formation. Positioned around march on Zodanga city through gate constructed by John Carter using men as steps.

**Continuity-Critical Traits:** Gathered force of 150,000 warriors for march on Zodanga after alliance proposal with Helium, marched on Zodanga and entered city through gate constructed by John Carter using men as steps, rescue mission from Zodanga forces to liberate Dejah Thoris.

[[/SECTION]]



[[FILMCREATOR_RECORD]]

type: character

asset_id: city_entry_gate

canonical_character_id: CH022 City Entry Gate

aliases: Zodanga Gate, Step Gate Entrance

is_fully_identified: false

manual_description_required: true

manual_description_reason: Environmental feature referenced only as gate structure; no individual physical descriptions provided in chapter material.

clarification_required: true

clarification_reason: Needs identity clarification for accurate image generation and character consistency.

clarification_question: What are the specific dimensions, materials, construction details, and ceremonial features of the gate built by John Carter's men using them as steps for Zodanga city entry?

[[SECTION markdown]]

# City Entry Gate

**Chapter Role:** Gate structure allowing entry into Zodanga city during military march

**Physical Presence:** Referenced only as gate structure; not individually detailed.

**Physical Description:** Green-skinned warrior population with muscular builds. No individual physical descriptions provided in chapter material.

**Costume/Silhouette:** Thark-style armor and weapons throughout gate construction site. Positioned at Zodanga city entrance during march on their city through gate constructed by John Carter's men using them as steps.

**Continuity-Critical Traits:** Constructed by John Carter's men using them as steps, allowed entry into Zodanga city during military march with 150,000 Thark warriors, enabled rescue operation for Dejah Thoris from Zodanga forces, entered through gate constructed by John Carter using men as steps.

[[/SECTION]]



[[FILMCREATOR_RECORD]]

type: character

asset_id: thark_council_vote

canonical_character_id: CH023 Thark Council Vote

aliases: Succession Vote, Combat Challenge Vote

is_fully_identified: false

manual_description_required: true

manual_description_reason: Event referenced only as voting body; no individual physical descriptions provided in chapter material.

clarification_required: true

clarification_reason: Needs identity clarification for accurate image generation and character consistency.

clarification_question: What are the specific ceremonial details, warrior formations, and voting arrangements of Thark council's vote to challenge Tal Hajus to combat with Tars Tarkas?

[[SECTION markdown]]

# Thark Council Vote

**Chapter Role:** Voting body deciding Jeddak succession through combat challenge

**Physical Presence:** Referenced only as voting body; not individually detailed.

**Physical Description:** Green-skinned warrior population with muscular builds. No individual physical descriptions provided in chapter material.

**Costume/Silhouette:** Thark-style armor and weapons throughout council chamber. Positioned around voting proceedings during combat challenge vote against Tal Hajus with Tars Tarkas.

**Continuity-Critical Traits:** Voted to challenge Tal Hajus to combat with Tars Tarkas after John Carter's exposure of him as coward, voted out former Jeddak after losing combat challenge to Tars Tarkas, became new Jeddak of Thark after winning combat challenge against Tal Hajus.

[[/SECTION]]



[[FILMCREATOR_RECORD]]

type: character

asset_id: jeddak_succession_event

canonical_character_id: CH024 Jeddak Succession Event

aliases: Leadership Transfer, Combat Victory Award

is_fully_identified: false

manual_description_required: true

manual_description_reason: Event referenced only as succession event; no individual physical descriptions provided in chapter material.

clarification_required: true

clarification_reason: Needs identity clarification for accurate image generation and character consistency.

clarification_question: What are the specific ceremonial details, warrior formations, and positioning arrangements of Tars Tarkas's victory and new Jeddak position after winning combat challenge against Tal Hajus?

[[SECTION markdown]]

# Jeddak Succession Event

**Chapter Role:** Leadership transfer from Tal Hajus to Tars Tarkas through combat victory

**Physical Presence:** Referenced only as succession event; not individually detailed.

**Physical Description:** Green-skinned warrior population with muscular builds. No individual physical descriptions provided in chapter material.

**Costume/Silhouette:** Thark-style armor and weapons throughout succession ceremony. Positioned around new Jeddak of Thark after winning combat challenge against Tal Hajus, became chieftain and proposed alliance with Helium to rescue Dejah Thoris from Zodanga.

**Continuity-Critical Traits:** Tars Tarkas won combat challenge against Tal Hajus, became new Jeddak of Thark after victory, made a chieftain and proposed alliance with Helium to rescue Dejah Thoris from Zodanga, gathered force of 150,000 warriors for march on Zodanga.

[[/SECTION]]



[[FILMCREATOR_RECORD]]

type: character

asset_id: tal_hajus_exposure

canonical_character_id: CH025 Tal Hajus Exposure

aliases: Coward Revelation, Council Accusation

is_fully_identified: false

manual_description_required: true

manual_description_reason: Event referenced only as exposure; no individual physical descriptions provided in chapter material.

clarification_required: true

clarification_reason: Needs identity clarification for accurate image generation and character consistency.

clarification_question: What are the specific ceremonial details, warrior formations, and positioning arrangements of John Carter's exposure of Tal Hajus as coward during council meeting?

[[SECTION markdown]]

# Tal Hajus Exposure

**Chapter Role:** Council accusation exposing former Jeddak as unfit to rule

**Physical Presence:** Referenced only as exposure event; not individually detailed.

**Physical Description:** Green-skinned warrior population with muscular builds. No individual physical descriptions provided in chapter material.

**Costume/Silhouette:** Thark-style armor and weapons throughout council chamber. Positioned around John Carter's exposure of Tal Hajus as coward during council meeting, voted to challenge Tal Hajus to combat with Tars Tarkas after exposure.

**Continuity-Critical Traits:** John Carter exposed Tal Hajus as coward unfit to rule during council meeting, sought revenge for previous injury before exposure, voted out after losing combat challenge to Tars Tarkas following exposure as coward by John Carter.

[[/SECTION]]



[[FILMCREATOR_RECORD]]

type: character

asset_id: thark_respect_earned

canonical_character_id: CH026 Thark Respect Earned

aliases: Friendship Award, Warrior Honor

is_fully_identified: false

manual_description_required: true

manual_description_reason: Event referenced only as respect earned; no individual physical descriptions provided in chapter material.

clarification_required: true

clarification_reason: Needs identity clarification for accurate image generation and character consistency.

clarification_question: What are the specific ceremonial details, warrior formations, and positioning arrangements of Tars Tarkas earning John Carter's respect and friendship after saving him from death by Warhoons?

[[SECTION markdown]]

# Thark Respect Earned

**Chapter Role:** Honor awarded to John Carter for saving Tars Tarkas from death

**Physical Presence:** Referenced only as respect earned; not individually detailed.

**Physical Description:** Green-skinned warrior population with muscular builds. No individual physical descriptions provided in chapter material.

**Costume/Silhouette:** Thark-style armor and weapons throughout battle site. Positioned around John Carter's saving of Tars Tarkas from death by Warhoons, earned green warrior's respect and friendship during crash landing sequence.

**Continuity-Critical Traits:** John Carter saved Tars Tarkas from death by Warhoons during crash landing, earned green warrior's respect and friendship after rescue, Woola dog returned to Thark alongside crash landing sequence aftermath.

[[/SECTION]]



[[FILMCREATOR_RECORD]]

type: character

asset_id: woola_return_event

canonical_character_id: CH027 Woola Return Event

aliases: Dog Reunion, Companion Return

is_fully_identified: false

manual_description_required: true

manual_description_reason: Event referenced only as return event; no individual physical descriptions provided in chapter material.

clarification_required: true

clarification_reason: Needs identity clarification for accurate image generation and character consistency.

clarification_question: What are the specific ceremonial details, warrior formations, and positioning arrangements of Woola's dog returning to Thark alongside John Carter's crash landing sequence?

[[SECTION markdown]]

# Woola Return Event

**Chapter Role:** Dog companion returning to Thark after crash landing

**Physical Presence:** Referenced only as return event; not individually detailed.

**Physical Description:** Green-skinned warrior population with muscular builds. No individual physical descriptions provided in chapter material.

**Costume/Silhouette:** Thark-style armor and weapons throughout battle site. Positioned around Woola's dog returning to Thark alongside John Carter's crash landing sequence, saved Tars Tarkas from death by Warhoons.

**Continuity-Critical Traits:** Woola dog returned to Thark after crash landing sequence, saved Tars Tarkas from death by Warhoons during battle, earned green warrior's respect and friendship after rescue.

[[/SECTION]]



[[FILMCREATOR_PACKET]]
````
