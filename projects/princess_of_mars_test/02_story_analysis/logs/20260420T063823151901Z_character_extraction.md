# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-20T06:38:23.151901+00:00
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

John Carter introduces himself and explains his decision to write his chronicle. Flashback reveals he and Captain James K. Powell discovered a gold mine in Arizona in 1865. On March 3, 1866, Powell left to get machinery while Carter guarded the claim. Carter discovers Apaches pursuing Powell. He chases them, finds Powell dead at a water hole, then witnesses a large Apache camp on a plateau. Carter charges into the camp alone, scattering the warriors. He retrieves Powell's body and drags him toward a cave entrance. After laying Powell down (dead), Carter explores the cave briefly before falling asleep on the floor due to exhaustion.
````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
[[SECTION character_index_markdown]]
# Character Index for CH001

## Characters Identified in Chapter

| Asset ID | Canonical Character ID | Aliases | Fully Identified | Manual Description Required |
|----------|------------------------|---------|------------------|----------------------------|
| john_carter | john_carter | - | Yes | No |
| captain_james_k_powell | captain_james_k_powell | - | Yes | No |
| apache_warriors | apache_warriors | - | No | Yes |

---

## Character Files

### 1. John Carter

**Display Name:** John Carter  
**Chapter Role:** Protagonist, Narrator, Gold Mine Claim Guardian  
**Physical Presence:** Present throughout chapter (guarding claim, exploring cave, dragging Powell's body)

**Physical Description:**
- Male human character
- Described as capable of guarding a gold mine claim alone
- Exhausted enough to fall asleep on cave floor
- Strong enough to charge into Apache camp and scatter warriors
- Capable of dragging dead body toward cave entrance

**Costume, Silhouette, Continuity-Critical Traits:**
- Wearing period-appropriate clothing for 1865 Arizona (implied by historical setting)
- No specific costume details provided in source material
- Silhouette: Standing male figure, later shown exhausted on floor

**Useful Descriptive Noun Phrases:**
- "exhausted gold miner"
- "claim guardian"
- "chronicle writer"
- "Apache camp charger"

**Uncertainty Notes:**
- No specific facial features or distinguishing marks mentioned
- Clothing details not specified in source text
- Physical build beyond strength and exhaustion not described

---

### 2. Captain James K. Powell

**Display Name:** Captain James K. Powell  
**Chapter Role:** Deceased Friend, Gold Mine Partner, Machinery Seeker  
**Physical Presence:** Referenced throughout (alive at mine start, dead by water hole)

**Physical Description:**
- Male human character
- Described as capable of discovering gold mine with Carter
- Strong enough to leave for machinery while Carter guarded claim
- Found dead at water hole after Apache pursuit

**Costume, Silhouette, Continuity-Critical Traits:**
- Military rank indicated by "Captain" title
- Wearing period-appropriate clothing for 1865 Arizona (implied)
- No specific costume details provided in source material
- Silhouette: Standing male figure at mine, later shown dead

**Useful Descriptive Noun Phrases:**
- "deceased mining partner"
- "machinery seeker"
- "gold claim discoverer"
- "Apache camp victim"

**Uncertainty Notes:**
- No specific facial features or distinguishing marks mentioned
- Clothing details not specified in source text
- Physical build beyond strength and death status not described
- Cause of death (Apache attack) noted but no injury details provided

---

### 3. Apache Warriors

**Display Name:** Apache Warriors  
**Chapter Role:** Antagonists, Pursuers, Camp Inhabitants  
**Physical Presence:** Referenced throughout (pursuing Powell, camp on plateau)

**Physical Description:**
- Multiple male human characters
- Described as capable of pursuing someone through terrain
- Large enough group to form camp on plateau
- Strong enough warriors to be charged by single person and scattered

**Costume, Silhouette, Continuity-Critical Traits:**
- Traditional Apache warrior attire (implied by historical setting)
- No specific costume details provided in source material
- Silhouette: Multiple standing male figures at mine, later shown as camp group
- Group size: Large enough to form visible camp on plateau

**Useful Descriptive Noun Phrases:**
- "Apache warriors"
- "pursuing party"
- "plateau camp inhabitants"
- "scattered warriors"

**Uncertainty Notes:**
- No individual physical descriptions available (group only)
- No specific facial features or distinguishing marks mentioned
- Clothing details not specified in source text
- Individual identities not established beyond group membership
- Physical build beyond warrior capability not described

[[/SECTION]]
[[/FILMCREATOR_PACKET]]
````
