# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-20T01:29:28.548340+00:00
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

Chapter id: CH019

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

# Chapter Summary: Battling in the Arena

## Story Summary
John Carter regains composure after a failed escape attempt, realizing Dejah Thoris and Sola were taken to be devoured. He endures two days of hunger before Kantos Kan is brought in as a fellow prisoner. They exchange greetings ("kaor") and backstories; Kantos reveals the expedition's defeat and the futile search for Dejah Thoris by Helium fleets.

Both are caged for the arena games, which last ten days. The amphitheater fills with 20,000 Warhoons. Initial contests involve green females versus calots (wild dogs), followed by beast battles. John Carter fights men and beasts, winning easily due to strength and agility; the crowd demands he join the hordes.

The final three combatants are a giant green warrior, Kantos Kan, and John Carter. The green warrior is killed when Kantos throws his sword at the giant's heart using Martian swordsmanship. Kantos then fights John Carter. To avoid death, they stage a duel until dark. John pretends to be dead by having Kantos thrust his sword into his chest; he falls to the ground with the weapon protruding. Kantos places his foot on John's neck and delivers a final blow through the neck, but the blade slips harmlessly into the sand.

Kantos leaves to claim his freedom, instructing John to meet him in the hills east of the city. John Carter creeps to the top of the amphitheater and escapes into the untenanted portion of the dead city, reaching the hills beyond.

## Visual Continuity Facts
- **Setting:** Underground amphitheater excavated below ground surface; partially filled with debris from ruined edifices.
- **Audience:** 20,000 Warhoons seated on raised platform; Dak Kova at center of one side.
- **Cages:** Constructed at each end to hold captives until turns come; stone piled around arena to prevent escape.
- **Combatants:** Red Martians (John/Kantos), Green Warriors (Enemies), Calots (dogs), Zitidars, Mad Zitidars.
- **Weapons:** Long-swords used for combat and sword throws; daggers given to female captives.
- **Lighting:** Dim torch light in dungeon; darkness falls during final encounter between Kantos and John.
- **Exit:** Top of amphitheater leads to untenanted portion of dead city, allowing access to hills east of city.
````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
task: character_extraction
version: 1

[[SECTION character_index_markdown]]
# Character Index: Battling in the Arena

| Name | Role | Status | Description |
| :--- | :--- | :--- | :--- |
| John Carter | Protagonist | Present | Red Martian, arena fighter, escapes to hills. |
| Kantos Kan | Prisoner/Fighter | Present | Red Martian, fellow prisoner, leaves for freedom. |
| Dejah Thoris | Referenced | Absent | Taken/devoured, referenced in backstory. |
| Sola | Referenced | Absent | Taken/devoured, referenced in backstory. |
| Dak Kova | Audience Member | Present | Seated on raised platform, center of one side. |
| Green Warrior | Combatant | Present | Giant green warrior, killed by Kantos Kan. |
| Warhoons | Audience | Present | 20,000 spectators seated in amphitheater. |
[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: john_carter
canonical_character_id: john_carter
aliases: 
is_fully_identified: true
manual_description_required: false
manual_description_reason: 
clarification_required: false
clarification_reason: 
clarification_question: 

[[SECTION markdown]]
# John Carter

**Display Name:** John Carter  
**Chapter Role:** Protagonist / Arena Combatant  
**Physical Presence:** Present (Fights in arena, escapes)  

**Visual Description:** Red Martian. Wears standard attire for combatants (implied). Sustains a sword thrust to the chest during final duel.  

**Continuity Traits:** High strength and agility noted. Escapes via amphitheater top into dead city hills.  

**Uncertainty Notes:** Specific facial features or costume details not provided in text beyond species designation "Red Martian".
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: kantos_kan
canonical_character_id: kantos_kan
aliases: 
is_fully_identified: true
manual_description_required: false
manual_description_reason: 
clarification_required: false
clarification_reason: 
clarification_question: 

[[SECTION markdown]]
# Kantos Kan

**Display Name:** Kantos Kan  
**Chapter Role:** Prisoner / Arena Combatant  
**Physical Presence:** Present (Fights in arena, leaves)  

**Visual Description:** Red Martian. Wears standard attire for combatants (implied). Uses long-sword for combat and sword throws.  

**Continuity Traits:** Master of Martian swordsmanship. Claims freedom after duel with John Carter. Instructs John to meet him in hills east of city.  

**Uncertainty Notes:** Specific facial features or costume details not provided in text beyond species designation "Red Martian".
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: dejah_thoris
canonical_character_id: dejah_thoris
aliases: 
is_fully_identified: true
manual_description_required: true
manual_description_reason: Character is referenced as taken/devoured and not physically present in the scene. Visual continuity facts do not describe her appearance here.
clarification_required: false
clarification_reason: 
clarification_question: 

[[SECTION markdown]]
# Dejah Thoris

**Display Name:** Dejah Thoris  
**Chapter Role:** Referenced Character (Taken)  
**Physical Presence:** Absent (Referenced as taken/devoured)  

**Visual Description:** Not described in this chapter text.  

**Continuity Traits:** Subject of expedition defeat and futile search by Helium fleets mentioned by Kantos Kan.  

**Uncertainty Notes:** Appearance details are missing from supplied material; manual description required for image generation support.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: sola
canonical_character_id: sola
aliases: 
is_fully_identified: true
manual_description_required: true
manual_description_reason: Character is referenced as taken/devoured and not physically present in the scene. Visual continuity facts do not describe her appearance here.
clarification_required: false
clarification_reason: 
clarification_question: 

[[SECTION markdown]]
# Sola

**Display Name:** Sola  
**Chapter Role:** Referenced Character (Taken)  
**Physical Presence:** Absent (Referenced as taken/devoured)  

**Visual Description:** Not described in this chapter text.  

**Continuity Traits:** Mentioned alongside Dejah Thoris as taken to be devoured.  

**Uncertainty Notes:** Appearance details are missing from supplied material; manual description required for image generation support.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: dak_kova
canonical_character_id: dak_kova
aliases: 
is_fully_identified: true
manual_description_required: true
manual_description_reason: No physical description provided in the supplied chapter text. Only identified by name and seating position.
clarification_required: false
clarification_reason: 
clarification_question: 

[[SECTION markdown]]
# Dak Kova

**Display Name:** Dak Kova  
**Chapter Role:** Audience Member  
**Physical Presence:** Present (Seated on raised platform)  

**Visual Description:** Not described in this chapter text.  

**Continuity Traits:** Seated at center of one side of the amphitheater among 20,000 Warhoons.  

**Uncertainty Notes:** Appearance details are missing from supplied material; manual description required for image generation support.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: green_warrior
canonical_character_id: green_warrior
aliases: 
is_fully_identified: false
manual_description_required: true
manual_description_reason: Only described as 'giant green warrior' with no specific facial or costume details in the text.
clarification_required: false
clarification_reason: 
clarification_question: 

[[SECTION markdown]]
# Green Warrior

**Display Name:** Green Warrior  
**Chapter Role:** Combatant (Final Contest)  
**Physical Presence:** Present (Fights in arena, killed)  

**Visual Description:** Giant green warrior. No specific facial or costume details provided in text.  

**Continuity Traits:** Killed when Kantos Kan throws his sword at the giant's heart using Martian swordsmanship.  

**Uncertainty Notes:** Appearance details are missing from supplied material; manual description required for image generation support.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: warhoons
canonical_character_id: warhoons
aliases: 
is_fully_identified: true
manual_description_required: false
manual_description_reason: 
clarification_required: false
clarification_reason: 
clarification_question: 

[[SECTION markdown]]
# Warhoons

**Display Name:** Warhoons  
**Chapter Role:** Audience / Spectators  
**Physical Presence:** Present (Seated in amphitheater)  

**Visual Description:** Generic audience members. No specific individual description provided in text.  

**Continuity Traits:** 20,000 spectators seated on raised platform. Demand John Carter join the hordes after his victories.  

**Uncertainty Notes:** Group entity; no specific individual appearance details required for general representation.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
