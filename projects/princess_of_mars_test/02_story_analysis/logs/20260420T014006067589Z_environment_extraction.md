# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-20T01:40:06.067589+00:00
- task: environment_extraction

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

Chapter id: CH025

Task: extract environment families into an environment index plus one Markdown file per environment family.

Return exactly one Markdown packet using this outer envelope:
[[FILMCREATOR_PACKET]]
task: environment_extraction
version: 1

[[SECTION environment_index_markdown]]
...environment_index_markdown content...
[[/SECTION]]

Repeat one FILMCREATOR_RECORD block for every extracted item of that type.

[[FILMCREATOR_RECORD]]
type: environment
asset_id: <value>

[[SECTION markdown]]
...markdown content...
[[/SECTION]]
[[/FILMCREATOR_RECORD]]
[[/FILMCREATOR_PACKET]]



Asset id rules:

- lowercase snake_case

- stable across later reruns

- include stable environment families rather than every one-off mention

- prefer visible geography and atmosphere over literary abstraction



Each environment Markdown file should include:

- environment role such as primary, secondary, or transit setting

- architecture or geography

- lighting and atmosphere cues

- scale cues and recurring environmental anchors

- useful descriptive noun phrases for later render-facing prompt writing



Chapter summary:

# Chapter XXV: The Looting of Zodanga

## Broad Story Summary
John Carter leads fifty Thark warriors into the Zodanga palace to rescue Dejah Thoris from forced marriage to Sab Than. During a ceremonial presentation, Carter interrupts the proceedings by shattering the palace window and attacking the golden chain meant to bind Dejah Thoris. A fierce battle ensues in the throne room where Carter kills both Than Kosis (father) and Sab Than (son), ultimately winning Dejah Thoris' hand in marriage despite the chaos of war surrounding them.

## Visual Continuity Facts
### Opening Sequence
- **Location**: Great gate/palace entrance
- **Characters Present**: John Carter, fifty Tharks led by Tars Tarkas
- **Key Objects**: Massive golden gates, huge hinges, palace windows
- **Visual Markers**: Fifty Tharks on mighty thoats, scarlet silk garments

### Throne Room Ceremony
- **Setting**: Audience chamber with brilliantly illuminated audience chamber
- **Characters**: Than Kosis and consort on massive golden thrones encrusted with diamonds
- **Procession Elements**: Four officers bearing huge salver with golden chain, ornaments of prince/princess
- **Key Figures**: Sab Than (muffled in scarlet silk), Dejah Thoris (princess figure)

### Combat Sequence
- **Action Points**: Window shattering, sword strikes on golden chain
- **Antagonists**: Thousand drawn swords menacing from every quarter
- **Weapons**: Long-swords, jeweled dagger (Sab Than's nuptial ornament)
- **Casualties**: Than Kosis and Sab Than both killed

### Resolution Scene
- **Location**: Throne room platform with narrow doorway behind throne
- **Characters**: John Carter, Dejah Thoris, Tars Tarkas, Kantos Kan
- **Key Objects**: Golden thrones, scarlet silks removed from figures
- **Visual Markers**: Corpses of Zodangan nobility covering floor

### Dungeon Rescue
- **Location**: Dungeons beneath palace, labyrinthine prison
- **Characters**: John Carter, dozen warriors, Kantos Kan
- **Action**: Searching for keys to open padlocks of cell and chains
````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
task: environment_extraction
version: 1

[[SECTION environment_index_markdown]]
# Environment Index - Chapter XXV

## great_gate_palace_entrance
- Role: Primary entrance setting
- Architecture: Massive golden gates with huge hinges, palace windows
- Lighting: Bright ceremonial illumination
- Atmosphere: Grandiose Zodangan palace exterior
- Scale: Fifty Tharks on mighty thoats approaching the gate
- Anchors: Golden gates, palace windows, massive hinges

## throne_room_audience_chamber
- Role: Primary ceremony setting
- Architecture: Audience chamber with golden thrones encrusted with diamonds
- Lighting: Brilliantly illuminated audience chamber
- Atmosphere: Ceremonial presentation space with ceremonial elements
- Scale: Four officers bearing huge salver, massive golden thrones
- Anchors: Golden chain, ornate diamond-encrusted thrones, scarlet silks

## dungeons_beneath_palace
- Role: Secondary rescue setting
- Architecture: Labyrinthine prison beneath palace
- Lighting: Dim dungeon lighting
- Atmosphere: Dark, confined prison environment
- Scale: Dozen warriors searching for keys to open padlocks of cell and chains
- Anchors: Cell doors, padlocks, chains, narrow passages

[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: great_gate_palace_entrance

[[SECTION markdown]]
# Great Gate Palace Entrance

## Environment Role
Primary entrance setting for the opening sequence of the chapter.

## Architecture and Geography
Massive golden gates with huge hinges dominate the palace entrance. The structure features large palace windows that frame the ceremonial space beyond. The gate serves as the threshold between the outer world and the Zodangan palace interior.

## Lighting and Atmosphere Cues
Bright ceremonial illumination bathes the entrance area, emphasizing the grandeur of the Zodangan architecture. The lighting creates a sense of importance and ceremony appropriate for the arrival of John Carter and fifty Thark warriors.

## Scale Cues and Environmental Anchors
- Fifty Tharks on mighty thoats approaching the gate
- Massive golden gates with huge hinges
- Palace windows framing the ceremonial space beyond
- Scarlet silk garments visible in the procession

## Descriptive Noun Phrases for Render-Facing Prompts
- "massive golden palace entrance gates"
- "huge ornate hinges on ceremonial doors"
- "brightly lit Zodangan palace exterior"
- "fifty scarlet-clad warriors on mighty beasts"
- "grandiose palace windows framing ceremony space"

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: throne_room_audience_chamber

[[SECTION markdown]]
# Throne Room Audience Chamber

## Environment Role
Primary ceremony setting where the forced marriage presentation takes place.

## Architecture and Geography
The audience chamber features massive golden thrones encrusted with diamonds. The space is designed for ceremonial presentations and includes a narrow doorway behind the throne platform. Four officers bear huge salvers with golden chains and ornaments of prince/princess.

## Lighting and Atmosphere Cues
Brilliantly illuminated audience chamber creates a ceremonial atmosphere appropriate for the presentation. The lighting emphasizes the opulence of the golden thrones and diamond encrustations.

## Scale Cues and Environmental Anchors
- Massive golden thrones encrusted with diamonds
- Four officers bearing huge salver with golden chain
- Scarlet silk garments on figures (Than Kosis, consort, Sab Than)
- Golden chain meant to bind Dejah Thoris
- Jeweled dagger as nuptial ornament

## Descriptive Noun Phrases for Render-Facing Prompts
- "massive diamond-encrusted golden throne"
- "brilliantly lit ceremonial audience chamber"
- "huge ornate salver with golden chain"
- "scarlet silk ceremonial garments"
- "jeweled nuptial dagger ornament"

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: dungeons_beneath_palace

[[SECTION markdown]]
# Dungeons Beneath Palace

## Environment Role
Secondary rescue setting for the dungeon escape sequence.

## Architecture and Geography
Labyrinthine prison structure beneath the palace features cell doors with padlocks and chains. The space consists of narrow passages and confined cells designed for imprisonment.

## Lighting and Atmosphere Cues
Dim dungeon lighting creates a dark, confined atmosphere appropriate for a prison environment. The low light emphasizes the dangerous nature of the rescue mission.

## Scale Cues and Environmental Anchors
- Dozen warriors searching for keys to open padlocks of cell and chains
- Cell doors with heavy padlocks
- Chains securing prisoners
- Narrow passages through labyrinthine structure
- Corpses of Zodangan nobility covering floor (from combat sequence)

## Descriptive Noun Phrases for Render-Facing Prompts
- "labyrinthine prison beneath palace"
- "dimly lit dungeon cell corridors"
- "heavy padlocked cell doors"
- "chains securing prisoner cells"
- "narrow prison passages"

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
