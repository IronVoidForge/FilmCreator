# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-19T19:59:08.576641+00:00
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

Chapter id: CH004

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

# Chapter IV: A PRISONER - Scene Decomposition

## Opening Sequence (Travel to City)
**Visual Continuity**: Carter and Tars Tarkas traveling on foot, ground rising rapidly toward edge of dead sea, traversing narrow gorge into open valley with low table land at extremity.

**Story Beat**: They gallop toward enormous city visible from distance, entering by ruined roadway that ends abruptly in broad steps.

## City Entry & Plaza Scene
**Visual Continuity**: Buildings appear deserted but not greatly decayed, showing signs of vacancy for years/ages. Large plaza with 900-1000 Martians camped around it.

**Character Details**: 
- Martians naked except ornaments, women have larger tusks curving to high-set ears
- Adult females 10-12 feet tall, children light in color all looking alike
- No extreme age visible among population

## Audience Chamber Introduction
**Visual Continuity**: Magnificent edifice of gleaming white marble with gold and brilliant stones. Main entrance 100 feet wide with huge canopy. Enormous chamber encircled by galleries.

**Scene Details**: 
- 40-50 male Martians assembled around rostrum steps
- Enormous warrior on platform heavily loaded with metal ornaments, feathers, leather trappings with precious stones
- White fur cape lined with scarlet silk from shoulders

## Formal Greeting Ceremony
**Visual Continuity**: Tars Tarkas (vice-chieftain) explains expedition and Carter's capture. Chieftain addresses Carter at length.

**Cultural Notes**: 
- Green Martians exchange names or ornaments depending on mission type
- Customary greeting between green Martians involves name exchanges
- Tars Tarkas virtually vice-chieftain, great ability as statesman and warrior

## Carter's Physical Demonstrations
**Visual Continuity**: Carter skips and flits among desks/chairs like monstrous grasshopper after signal failure. Creeps then gets roughly jerked to feet by towering fellow who laughed at misfortunes.

**Key Actions**: 
- "Sak" jumping demonstration: Tars Tarkas jumps while repeating word
- "Sakked" long jump: Carter clears 150 feet, lands squarely without falling
- Exhibition witnessed by several hundred lesser Martians demanding repetition

## Combat Scene (Fighting Warrior)
**Visual Continuity**: Fights one warrior after being banged down upon feet. Swings fist to jaw, opponent falls like felled ox. Other Martians initially struck dumb with wonderment then break into wild peals of laughter and applause.

**Cultural Significance**: Carter wins manifestation of approbation - rare honor among Martians. Fellow remains where fallen, no mates approach him.

## Food Request & Sola Introduction
**Visual Continuity**: Tars Tarkas and chief exchange words. Young female instructed by Tars Tarkas, Carter accompanies her across plaza toward large building on far side.

**Character Details**: 
- Sola about 8 feet tall, light olive-green color with smooth glossy hide
- Belongs to retinue of Tars Tarkas
- Conducts Carter to spacious chamber with silks and furs littering floor

## Strange Creature Appearance
**Visual Continuity**: Room well lighted by large windows, beautifully decorated with mural paintings and mosaics. Sola makes peculiar hissing sound signaling someone in adjoining room.

**Creature Description**: 
- Waddles in on ten short legs, squats down before girl like obedient puppy
- About size of Shetland pony, head bears slight resemblance to frog except jaws equipped with three rows of long sharp tusks

## Scene End Points
**Decomposition Markers**: 
- Carter's physical limitations (cannot walk properly)
- Martian cultural differences (humor based on violence/death)
- Ancient architecture predating current Martians
- Introduction of strange ten-legged creature species
````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
task: character_extraction
version: 1

[[SECTION character_index_markdown]]
# Character Index - Chapter IV: A PRISONER

| Character | Asset ID | Status | Description Available |
|-----------|----------|--------|----------------------|
| Carter | carter | Primary human protagonist | No physical description provided |
| Tars Tarkas | tars_tarkas | Vice-chieftain, statesman and warrior | No physical description provided |
| Chieftain | chieftain | Martian leader | Identified by title only |
| Sola | sola | Young female Martian | Physical description available |
| Martian (general) | martian | Multiple unnamed individuals | General population traits noted |

**Notes:**
- Carter and Tars Tarkas lack physical/visual descriptions for image generation
- Chieftain identified by title without personal name
- Sola has complete physical description in source material
- Multiple unnamed Martians referenced throughout chapter
[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: carter
canonical_character_id: CH004-CARTER
aliases: 
is_fully_identified: true
manual_description_required: true
manual_description_reason: No physical or visual description of Carter's appearance is provided in the chapter summary; only his movements and limitations are described (skips, flits, cannot walk properly)
clarification_required: false
clarification_reason: 
clarification_question: 

[[SECTION markdown]]
# carter

**Display Name:** Carter  
**Chapter Role:** Primary human protagonist / prisoner of Martians  
**Physical Presence:** Referenced throughout chapter; physically present in scenes with Tars Tarkas and Martians  

**Supported Physical Description:** None - no visual or physical description provided in source material. Only movement patterns described (skipping, flitting like grasshopper, creeping, jumping demonstrations).

**Costume/Silhouette/Continuity Traits:** Unknown - no costume or silhouette details available in chapter summary.

**Render-Facing Noun Phrases:** human male protagonist, prisoner status, physical limitations affecting mobility, cannot walk properly, demonstrated jumping ability (150 foot clear), grasshopper-like movement patterns

**Uncertainty Notes:** Complete lack of physical description prevents dependable image generation; manual description required for later render-facing work.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: tars_tarkas
canonical_character_id: CH004-TARS_TARKAS
aliases: vice-chieftain
is_fully_identified: true
manual_description_required: true
manual_description_reason: No specific physical or visual description of Tars Tarkas's appearance is provided in the chapter summary; only his movements and abilities are mentioned (towering fellow, great ability as statesman and warrior)
clarification_required: false
clarification_reason: 
clarification_question: 

[[SECTION markdown]]
# tars_tarkas

**Display Name:** Tars Tarkas  
**Chapter Role:** Vice-chieftain / Statesman and Warrior / Carter's guide  
**Physical Presence:** Physically present throughout chapter; explains expedition, demonstrates jumping ability ("Sak"), instructs Sola  

**Supported Physical Description:** None - no visual or physical description provided in source material. Only movement patterns described (towering fellow, jumps while repeating word).

**Costume/Silhouette/Continuity Traits:** Unknown - no costume details available in chapter summary.

**Render-Facing Noun Phrases:** vice-chieftain of Martians, statesman and warrior, great ability, towering fellow, demonstrates jumping ability (Sak), instructs young female Martian, belongs to retinue of chief

**Uncertainty Notes:** Complete lack of physical description prevents dependable image generation; manual description required for later render-facing work.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: chieftain
canonical_character_id: CH004-CHEIFAIN
aliases: chief
is_fully_identified: false
manual_description_required: true
manual_description_reason: No specific physical or visual description of the Chieftain's appearance is provided in the chapter summary; only his status and adornments are mentioned (enormous warrior, heavily loaded with metal ornaments, feathers, leather trappings with precious stones, white fur cape lined with scarlet silk)
clarification_required: false
clarification_reason: Identified by title only without personal name
clarification_question: 

[[SECTION markdown]]
# chieftain

**Display Name:** Chieftain  
**Chapter Role:** Martian leader / Addressed Carter at length / Receives formal greeting ceremony  
**Physical Presence:** Physically present in audience chamber; addresses Carter, exchanges words with Tars Tarkas  

**Supported Physical Description:** None - no visual or physical description provided in source material. Only status and adornments mentioned (enormous warrior, heavily loaded with metal ornaments, feathers, leather trappings with precious stones, white fur cape lined with scarlet silk).

**Costume/Silhouette/Continuity Traits:** Ornamented warrior - heavily loaded with metal ornaments, feathers, leather trappings with precious stones; wears white fur cape lined with scarlet silk from shoulders.

**Render-Facing Noun Phrases:** Martian leader, enormous warrior, heavily loaded with metal ornaments, feathers and leather trappings with precious stones, white fur cape lined with scarlet silk, addresses Carter at length, exchanges words with Tars Tarkas

**Uncertainty Notes:** Identified by title only without personal name; complete lack of physical description prevents dependable image generation; manual description required for later render-facing work.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: sola
canonical_character_id: CH004-SOLA
aliases: 
is_fully_identified: true
manual_description_required: false
manual_description_reason: 
clarification_required: false
clarification_reason: 
clarification_question: 

[[SECTION markdown]]
# sola

**Display Name:** Sola  
**Chapter Role:** Young female Martian / Belongs to retinue of Tars Tarkas / Conducts Carter to chamber  
**Physical Presence:** Physically present in audience chamber; makes peculiar hissing sound signaling someone in adjoining room  

**Supported Physical Description:** About 8 feet tall, light olive-green color with smooth glossy hide.

**Costume/Silhouette/Continuity Traits:** Belongs to retinue of Tars Tarkas; conducts Carter across plaza toward large building on far side.

**Render-Facing Noun Phrases:** young female Martian, about 8 feet tall, light olive-green color, smooth glossy hide, belongs to retinue of Tars Tarkas, makes peculiar hissing sound, conducts Carter to spacious chamber with silks and furs littering floor

**Uncertainty Notes:** Complete physical description available in source material; no manual description required.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: martian
canonical_character_id: CH004-MARTIAN
aliases: 
is_fully_identified: false
manual_description_required: true
manual_description_reason: Multiple unnamed Martian individuals referenced throughout chapter; no consistent physical description provided for general population beyond specific mentions (adult females 10-12 feet tall, children light in color all looking alike, naked except ornaments)
clarification_required: false
clarification_reason: General population category without individual identification
clarification_question: 

[[SECTION markdown]]
# martian

**Display Name:** Martian  
**Chapter Role:** Multiple unnamed individuals / General population of Martians  
**Physical Presence:** Physically present throughout chapter; 40-50 male Martians assembled around rostrum steps, several hundred lesser Martians witnessing demonstrations  

**Supported Physical Description:** Partial - adult females 10-12 feet tall, children light in color all looking alike, naked except ornaments. General population traits noted but no consistent individual description provided.

**Costume/Silhouette/Continuity Traits:** Naked except ornaments; women have larger tusks curving to high-set ears; green Martians exchange names or ornaments depending on mission type; customarily greet with name exchanges.

**Render-Facing Noun Phrases:** adult females 10-12 feet tall, children light in color all looking alike, naked except ornaments, women have larger tusks curving to high-set ears, no extreme age visible among population, green Martians exchange names or ornaments depending on mission type, customarily greet with name exchanges

**Uncertainty Notes:** Multiple unnamed individuals referenced; general population category without individual identification; partial physical description available but not consistent across all references.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_PACKET]]
````
