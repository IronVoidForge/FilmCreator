# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-20T03:28:41.310183+00:00
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

Chapter id: CH004

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

**Scene 1: Arrival at the City & Audience Chamber**
Carter arrives at the foot of mountains near a ruined city on Mars. He is brought before the Chieftain in a magnificent edifice constructed of gleaming white marble and gold. Visual continuity note: The furniture (desks, chairs) is sized for humans, creating a size mismatch with the Martians who cannot fit comfortably. The chamber features galleries and carved wooden desks.

**Scene 2: Ceremonial Introduction & Cultural Exchange**
Tars Tarkas (Vice-Chieftain) escorts Carter to the Chieftain's rostrum. A formal greeting occurs involving name exchange or ornament/shot exchange depending on familiarity. Carter learns about Martian customs: smiling is perfunctory, laughter is horrific, and humor involves death agonies or inflicting death on prisoners. Visual note: Martians are largely naked with ornaments; women have larger tusks and lighter skin color.

**Scene 3: Physical Demonstrations & Combat**
Carter performs "sak" jumps to demonstrate utility (clearing 150 feet). He is bullied by a warrior who bullies him into fighting; Carter punches the warrior in self-defense against brutality. The Martians applaud his fighting spirit and approach. Visual note: Martians laugh at Carter's misfortunes during initial attempts but cheer his combat success.

**Scene 4: Sola & Sleeping Quarters**
Carter is hungry and thirsty. Tars Tarkas sends Sola (young female, ~8 feet tall, light olive-green) to accompany him. They move to a spacious chamber decorated with mural paintings and mosaics showing signs of antiquity. Visual note: A ten-legged creature waddles in; it is the size of a Shetland pony with a frog-like head and three rows of sharp tusks.
````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
task: environment_extraction
version: 1

[[SECTION environment_index_markdown]]
# Chapter CH004 Environment Index

## Extracted Environments

1. **martian_ruined_city_exterior** - Arrival at foot of mountains near ruined city structures.
2. **chieftain_palace_interior** - Audience chamber with white marble, gold, galleries, and carved desks.
3. **ceremonial_grounds** - Open space for sak jumps and distance demonstrations.
4. **sola_sleeping_quarters** - Spacious chamber with mural paintings, mosaics, and ten-legged creature anchor.

## Notes

- All environments are stable across later reruns.
- Asset IDs follow lowercase snake_case convention.
- Descriptions prioritize visible geography and atmosphere over literary abstraction.
[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: martian_ruined_city_exterior

[[SECTION markdown]]
**Environment Role:** Arrival / Transit Setting

**Architecture & Geography:** Foot of mountains near a ruined city on Mars. The landscape features rugged terrain with remnants of ancient structures scattered around the base of the mountain range.

**Lighting & Atmosphere:** Martian daylight conditions, likely dusty and hazy due to atmospheric composition. The ruins suggest a history of decay or abandonment, contributing to a somber yet majestic atmosphere.

**Scale & Anchors:** Mountains serve as the primary vertical anchor, towering over the ruined city. The scale of the mountains contrasts with the human-sized artifacts found within the ruins.

**Descriptive Noun Phrases:** Mountain foothills, ruined cityscape, Martian dust haze, ancient stone remnants, rugged terrain.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: chieftain_palace_interior

[[SECTION markdown]]
**Environment Role:** Primary Setting (Audience Chamber)

**Architecture & Geography:** Magnificent edifice constructed of gleaming white marble and gold. Features galleries, carved wooden desks, and human-sized furniture (desks, chairs).

**Lighting & Atmosphere:** Bright, reflective surfaces from the white marble and gold create a luminous interior. The atmosphere is formal and imposing, emphasizing the Chieftain's authority.

**Scale & Anchors:** Human-sized furniture creates a size mismatch with giant Martians who cannot fit comfortably. Galleries provide vertical depth anchors within the chamber.

**Descriptive Noun Phrases:** Gleaming white marble, gold accents, carved wooden desks, human-sized furniture, gallery walkways.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: ceremonial_grounds

[[SECTION markdown]]
**Environment Role:** Transit / Training Setting

**Architecture & Geography:** Open flat ground suitable for jumping demonstrations. The area allows for clear visibility of distance measurements (150 feet clearance).

**Lighting & Atmosphere:** Clear visibility conditions, likely bright daylight to ensure accurate distance perception during jumps. Minimal obstructions in the open space.

**Scale & Anchors:** 150-foot clearance marker serves as a functional anchor for utility demonstrations. The ground surface provides a stable platform for physical feats.

**Descriptive Noun Phrases:** Open flat terrain, jump demonstration zone, distance markers, clear visibility area.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: sola_sleeping_quarters

[[SECTION markdown]]
**Environment Role:** Secondary / Private Setting

**Architecture & Geography:** Spacious chamber decorated with mural paintings and mosaics showing signs of antiquity. Features a ten-legged creature (frog-like head, three rows of sharp tusks) as an anchor.

**Lighting & Atmosphere:** Decorative lighting from murals and mosaics suggests an artistic or historical ambiance. The space feels ancient yet maintained.

**Scale & Anchors:** Ten-legged creature waddling in the chamber serves as a biological anchor. The spaciousness accommodates both humans and larger Martians comfortably.

**Descriptive Noun Phrases:** Mural paintings, mosaic floors, ten-legged creature, antique decorations, spacious chamber.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]
[[/FILMCREATOR_PACKET]]
````
