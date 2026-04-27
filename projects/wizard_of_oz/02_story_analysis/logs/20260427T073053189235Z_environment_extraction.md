# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-27T07:30:53.189235+00:00
- task: environment_extraction

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
Project slug: wizard_of_oz

Chapter id: CH021

Task: extract environment families into an environment index plus one Markdown file per environment family.

Packet contract:
- task: environment_extraction
- version: 1
- first line: [[FILMCREATOR_PACKET]]
- last line: [[/FILMCREATOR_PACKET]]
- required sections: environment_index_markdown
- record type environment: fields=asset_id sections=markdown



Output format:

[[FILMCREATOR_PACKET]]

task: environment_extraction

version: 1

environment_index_markdown:

[[SECTION environment_index_markdown]]

...index markdown...

[[/SECTION]]



[[FILMCREATOR_RECORD]]

type: environment

asset_id: arizona_quartz_vein_location



[[SECTION markdown]]

# Arizona Quartz Vein Location

Short, grounded environment markdown.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]



Asset id rules:

- lowercase snake_case

- stable across later reruns

- emit one explicit environment record per meaningful location or setting family

- every environment record must have a FILMCREATOR_RECORD wrapper with type environment

- include stable environment families rather than every one-off mention

- prefer visible geography and atmosphere over literary abstraction



Each environment Markdown file should include:

- environment role such as primary, secondary, or transit setting

- architecture or geography

- lighting and atmosphere cues

- scale cues and recurring environmental anchors

- useful descriptive noun phrases for later render-facing prompt writing



Chapter summary:

**Setting:** A disagreeable country of bogs and marshes, leading into a vast, ancient forest filled with massive trees and thick moss.

**Characters:** Dorothy, Toto, the Scarecrow, the Tin Woodman, the Lion, various forest beasts (tigers, elephants, bears, wolves, foxes), and the Great Spider monster.

**Events:**
- The travelers navigate through difficult marshlands and enter a deep, ancient forest.
- The group discovers a massive gathering of wild animals in a forest clearing.
- A tiger informs the Lion that the animals are being terrorized by a giant spider-like monster with elephant-sized body and tree-trunk legs.
- The Lion strikes a deal: if he kills the monster, the animals will crown him King of the Forest.
- The Lion tracks the monster to an oak grove while it is sleeping.
- Utilizing the creature's anatomy (a slender neck), the Lion leaps onto its back and decapitates it with a single heavy paw strike.
- The Lion returns to the clearing, announces his victory, and is officially recognized as the King of Beasts. He promises to return to rule once Dorothy has reached Kansas.
````

## Raw Response
````text
[[FILMCREATOR_PACKET]]

task: environment_extraction

version: 1

environment_index_markdown:

[[SECTION environment_index_markdown]]

# Environment Index - Chapter CH021

## Marshlands and Bogs
- [marshland_bog_complex](#marshland_bog_complex)

## Ancient Forest
- [ancient_forest_interior](#ancient_forest_interior)
- [oak_grove_monstrous_lair](#oak_grove_monstrous_lair)

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: marshland_bog_complex

[[SECTION markdown]]

# Marshland Bog Complex

**Role:** Transit setting.

**Architecture or Geography:** A disagreeable, low-lying landscape dominated by waterlogged terrain, thick bogs, and treacherous marshes. The ground is uneven and unstable.

**Lighting and Atmosphere Cues:** Damp, heavy atmosphere; muted colors; low visibility due to mist or humidity; oppressive and difficult to traverse.

**Scale Cues and Recurring Environmental Anchors:** Wide expanses of stagnant water; patches of reeds and marsh grass; sinking mud pits.

**Descriptive Noun Phrases:** Sinking peat bogs, murky marshland, treacherous wetlands, damp mire, fog-shrouded swamps.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: ancient_forest_interior

[[SECTION markdown]]

# Ancient Forest Interior

**Role:** Primary setting.

**Architecture or Geography:** A vast, primordial woodland characterized by massive, towering trees and a dense floor covered in thick moss. Includes large clearings where animals gather.

**Lighting and Atmosphere Cues:** Dappled sunlight filtering through high canopies; deep shadows; lush, verdant tones; sense of ancient scale and wildness.

**Scale Cues and Recurring Environmental Anchors:** Colossal tree trunks; expansive forest floor; wide animal clearings; dense undergrowth.

**Descriptive Noun Phrases:** Primordial woodland, massive ancient trees, moss-covered forest floor, sun-dappled canopy, sprawling forest clearing.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: oak_grove_monstrous_lair

[[SECTION markdown]]

# Oak Grove Monstrous Lair

**Role:** Secondary setting (location of climax).

**Architecture or Geography:** A specific grove within the ancient forest, dominated by large oak trees providing cover and shade.

**Lighting and Atmosphere Cues:** Deeply shadowed; quiet but tense atmosphere; pockets of darkness beneath heavy branches.

**Scale Cues and Recurring Environmental Anchors:** Large oak trunks; thick roots; sheltered hollows suitable for a massive creature to sleep.

**Descriptive Noun Phrases:** Shadowed oak grove, gnarled tree roots, dense woodland shelter, dark canopy recesses.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
