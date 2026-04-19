# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-19T20:09:16.973876+00:00
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

Chapter id: CH008

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

# Chapter Summary: The Fair Captive from the Sky

**Narrative Arc:**
The third day after the incubator ceremony, the procession sets out toward home but is ordered to return immediately upon entering the open ground. The green Martians melt into nearby buildings like mist. The narrator enters a building on the city front (where he previously encountered apes) and climbs to an upper floor to observe the valley.

**Visual Continuity & Battle Sequence:**
*   **Arrival of Fleet:** Twenty gray-painted, long, low airships swing over the crest of the nearest hill. Each carries a strange banner and a painted device on the prow that gleams in sunlight. Figures crowd forward decks.
*   **First Volley:** Green Martian warriors fire a terrific volley from building windows facing the valley. The scene changes by magic; the foremost vessel swings broadside, bringing guns into play.
*   **Fire Exchange:** Our own fire never diminishes (approx 75% accuracy). A little figure drops on one craft at each explosion; banners and upper works dissolve in spurts of flame. Enemy fire is ineffectual due to suddenness of first volley catching crews unprepared.
*   **Tactics:** Green warriors have objective points for fire: wireless finding/sighting apparatus, smaller guns, gunners, officers, crew members, upper works, steering gear/propellers.
*   **Retreat & Damage:** Twenty minutes after the first volley, the fleet swings trailing off. Several craft limp perceptibly. Fire ceases; energies focus on escape. Warriors rush to roofs and follow retreating armada with continuous fusillade.
*   **The Disabled Ship:** One barely moving craft is in sight, entirely unmanned, drifting slowly. Warriors cease firing as it appears helpless. As she neared the city (50 feet above ground), warriors swarmed upon her from windows using great spears to ease collision shock. Grappling hooks were thrown; big boat hauled to ground.
*   **Search & Loot:** Warriors search vessel stem to stern. Dead sailors examined for signs of life. A party drags a little figure (less than half as tall, walks erect). Loot requisitioned: arms, ammunition, silks, furs, jewels, carved stone vessels, solid foods/liquids (casks of water).
*   **Destruction:** Last load removed; craft towed far out into valley. Warriors empty contents of carboys over dead sailors/decks. Last warrior throws missile back upon vessel; faint spurt of flame rises. Guy ropes released; warship soars majestically into air, decks/upper works mass of roaring flames.
*   **Aftermath:** Ship drifts to southeast, rising higher as flames eat wooden parts. Narrator watches for hours from roof until lost in distance. Warriors follow with possibility of reinforcement return.

**Character Interaction & Resolution:**
*   **Narrator's Emotion:** Depressed by defeat of kindred people (humans) rather than routing unfriendly creatures. Feels hallucination; yearning toward unknown foemen; hope fleet returns for reckoning.
*   **Street Scene:** Woola follows at heel. Sola rushes up as though searching. Cavalcade returning to plaza; homeward march given up for week due to fear of air craft return attack. Lorquas Ptomel remains at deserted city until danger passed.
*   **The Prisoner:** As Sola and narrator enter plaza, glimpse of prisoner from battle craft being roughly dragged into nearby building by green Martian females.
*   **Visual Description of Captive:** Slender, girlish figure similar to earthly women. Oval face, beautiful features, finely chiseled. Large lustrous eyes. Mass of coal black, waving hair caught loosely into strange coiffure. Skin light reddish copper color; crimson glow of cheeks and ruby lips. Destitute of clothes save for highly wrought ornaments; entirely naked.
*   **Interaction:** Captive does not see narrator at first. Just as she disappears through portal, eyes meet mine. She makes little sign with free hand (ununderstood). Look of hope fades into dejection, loathing, contempt. Narrator realizes he did not answer signal; feels appeal for succor prevented by ignorance. Dragged out of sight into depths of deserted edifice.
````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
task: character_extraction
version: 1

[[SECTION character_index_markdown]]
# Character Index - Chapter CH008

| Character | Role | Identification Status | Description Status |
| :--- | :--- | :--- | :--- |
| Narrator | Observer/Protagonist | Weak (No Name) | Missing Visuals |
| Woola | Companion/Follower | Identified by Name | Missing Visuals |
| Sola | Follower/Searcher | Identified by Name | Missing Visuals |
| Lorquas Ptomel | City Guardian | Identified by Name | Missing Visuals |
| Captive | Prisoner/Subject | Weak (No Name) | Detailed Visuals |

[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: narrator
canonical_character_id: narrator
aliases: none
is_fully_identified: false
manual_description_required: true
manual_description_reason: No physical description provided in the chapter summary.
clarification_required: true
clarification_reason: Unknown identity or name.
clarification_question: Does this character have a specific name or identity beyond 'narrator' in the source material?

[[SECTION markdown]]
# Narrator - Chapter CH008

**Display Name:** The Narrator  
**Chapter Role:** Observer / Protagonist  
**Physical Presence:** Referenced (First-person perspective)  
**Visual Description:** None provided in source text.  
**Continuity Notes:** No physical traits, costume, or silhouette details available for image generation.  
**Uncertainty:** Identity is strictly defined by narrative function ("I", "our own fire") rather than a proper name. Visual appearance is unknown and requires manual description for consistent rendering.

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: woola
canonical_character_id: woola
aliases: none
is_fully_identified: true
manual_description_required: true
manual_description_reason: No physical description provided in the chapter summary.
clarification_required: false
clarification_reason: 
clarification_question: 

[[SECTION markdown]]
# Woola - Chapter CH008

**Display Name:** Woola  
**Chapter Role:** Companion / Follower  
**Physical Presence:** Present (Follows at heel)  
**Visual Description:** None provided in source text.  
**Continuity Notes:** No physical traits, costume, or silhouette details available for image generation.  
**Uncertainty:** While identified by name, visual characteristics are missing from the chapter summary and require manual description for consistent rendering.

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: sola
canonical_character_id: sola
aliases: none
is_fully_identified: true
manual_description_required: true
manual_description_reason: No physical description provided in the chapter summary.
clarification_required: false
clarification_reason: 
clarification_question: 

[[SECTION markdown]]
# Sola - Chapter CH008

**Display Name:** Sola  
**Chapter Role:** Follower / Searcher  
**Physical Presence:** Present (Rushes up)  
**Visual Description:** None provided in source text.  
**Continuity Notes:** No physical traits, costume, or silhouette details available for image generation.  
**Uncertainty:** While identified by name, visual characteristics are missing from the chapter summary and require manual description for consistent rendering.

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: lorquas_ptomel
canonical_character_id: lorquas_ptomel
aliases: none
is_fully_identified: true
manual_description_required: true
manual_description_reason: No physical description provided in the chapter summary.
clarification_required: false
clarification_reason: 
clarification_question: 

[[SECTION markdown]]
# Lorquas Ptomel - Chapter CH008

**Display Name:** Lorquas Ptomel  
**Chapter Role:** City Guardian / Observer  
**Physical Presence:** Present (Remains at deserted city)  
**Visual Description:** None provided in source text.  
**Continuity Notes:** No physical traits, costume, or silhouette details available for image generation.  
**Uncertainty:** While identified by name, visual characteristics are missing from the chapter summary and require manual description for consistent rendering.

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: captive
canonical_character_id: captive
aliases: prisoner
is_fully_identified: false
manual_description_required: false
manual_description_reason: Detailed physical description provided (slender, coal black hair, light reddish copper skin).
clarification_required: false
clarification_reason: 
clarification_question: 

[[SECTION markdown]]
# The Captive - Chapter CH008

**Display Name:** The Captive  
**Chapter Role:** Prisoner / Subject of Battle  
**Physical Presence:** Referenced (Dragged into building)  
**Visual Description:** Slender, girlish figure similar to earthly women. Oval face, beautiful features, finely chiseled. Large lustrous eyes. Mass of coal black, waving hair caught loosely into strange coiffure. Skin light reddish copper color; crimson glow of cheeks and ruby lips. Destitute of clothes save for highly wrought ornaments; entirely naked.  
**Continuity Notes:** Distinct visual traits available for image generation. No name provided in chapter summary.  
**Uncertainty:** Identity is strictly defined by narrative function ("captive", "prisoner") rather than a proper name. Visual appearance is fully described but lacks stable identification by name.

[[/SECTION]]
[[/FILMCREATOR_RECORD]]
[[/FILMCREATOR_PACKET]]
````
