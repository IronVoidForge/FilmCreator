# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-20T06:50:51.338483+00:00
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
Project slug: princess_of_mars_test

Chapter id: CH001

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

In Chapter I, titled "On the Arizona Hills," John Carter reflects on his fear of death despite having died twice and remained alive. He recounts his decision to write down the story of his life and death, specifically focusing on the events surrounding a gold discovery in 1865 with Captain James K. Powell. After locating a valuable quartz vein, Powell departed to purchase machinery while Carter guarded the claim. Upon discovering that Apaches were pursuing Powell's party, Carter chased them down the trail. He found Powell dead and surrounded by Apache warriors at a campsite. Charging into the enemy lines, Carter shot at the Apaches, causing them to flee. He retrieved Powell's body and escaped the Apache pursuit through a defile that led him inadvertently to a large cave. After laying Powell down and failing to resuscitate him, Carter entered the cave to reconnoiter. Overcome by fatigue and excitement, he fell asleep on the cave floor, marking the beginning of his ten-year stay.
````

## Raw Response
````text


[[FILMCREATOR_PACKET]]

task: environment_extraction

version: 1

environment_index_markdown:

[[SECTION environment_index_markdown]]

# Environment Index - Chapter I: On the Arizona Hills

## Environment Families

| Asset ID | Role | Geography/Architecture | Atmosphere |
|----------|------|------------------------|------------|
| arizona_quartz_vein_location | primary | Open desert terrain with exposed quartz vein, mining claim markers | Bright daylight, heat haze, metallic glint on rock face |
| apache_campsite | secondary | Temporary encampment in canyon defile, fire pits, scattered gear | Dusk light, smoke haze, tension-filled air |
| trail_defile | transit | Narrow rocky passage through canyon walls | Shadowed, echoing, claustrophobic scale |
| large_cave | primary | Subterranean cavern with natural rock formations | Dim ambient light, dust motes, ancient stone textures |

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: arizona_quartz_vein_location

[[SECTION markdown]]

# Arizona Quartz Vein Location

## Role
Primary setting for gold discovery and initial confrontation.

## Geography and Architecture
Open desert terrain with exposed quartz vein formation, mining claim markers staked into ground, rocky outcrops framing the excavation site.

## Lighting and Atmosphere
Bright midday sunlight creating heat haze distortion, metallic glint reflecting off quartz crystals, dust particles suspended in air, harsh shadows from canyon walls.

## Scale Cues
Human-scale mining equipment dwarfed by natural rock formations, claim stakes marking territorial boundaries, distant horizon visible across flat desert floor.

## Environmental Anchors
Quartz vein outcrop, staked claim markers, scattered mining tools, Apache warrior figures emerging from terrain edges.

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: apache_campsite

[[SECTION markdown]]

# Apache Campsite

## Role
Secondary setting for discovery of Powell's body and enemy confrontation.

## Geography and Architecture
Temporary encampment established in canyon defile, fire pits with cooling embers, scattered personal gear and supplies, makeshift shelter structures.

## Lighting and Atmosphere
Dusk light casting long shadows across campsite, smoke haze from dying fires, tension-filled air quality, dimming natural illumination.

## Scale Cues
Compact encampment footprint within canyon passage, fire pits defining activity zones, body positioned near central gathering area.

## Environmental Anchors
Cooling fire embers, scattered Apache warrior figures, Powell's body near camp center, defile entrance framing the scene.

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: trail_defile

[[SECTION markdown]]

# Trail Defile

## Role
Transit setting for escape and pursuit sequences.

## Geography and Architecture
Narrow rocky passage carved through canyon walls, natural stone arches overhead, winding path following terrain contours, steep drop-offs on either side.

## Lighting and Atmosphere
Shadowed interior with intermittent sunlight filtering through rock openings, echoing acoustics amplifying footsteps, claustrophobic scale from enclosing walls.

## Scale Cues
Human passage width barely accommodating full stride, towering rock faces creating vertical compression, distant horizon obscured by canyon depth.

## Environmental Anchors
Canyon wall formations, trail markers carved into stone, defile entrance and exit points, echoing chamber acoustics.

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: large_cave

[[SECTION markdown]]

# Large Cave

## Role
Primary setting for Carter's ten-year stay and subsequent Mars journey.

## Geography and Architecture
Subterranean cavern with natural rock formations, multiple chambers connected by narrow passages, stalactite and stalagmite structures, natural ventilation shafts.

## Lighting and Atmosphere
Dim ambient light from distant entrance filtering through cave mouth, dust motes suspended in still air, ancient stone textures illuminated by filtered sunlight, cool temperature contrast to desert exterior.

## Scale Cues
Vast cavern floor accommodating sleeping area, towering rock formations creating vertical grandeur, multiple chambers suggesting complex geological history.

## Environmental Anchors
Cave entrance archway, sleeping area on cave floor, stalactite clusters overhead, natural ventilation shafts, scattered debris from previous occupants.

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: desert_outskirts

[[SECTION markdown]]

# Desert Outskirts

## Role
Secondary setting for approach to quartz vein location and initial exploration.

## Geography and Architecture
Open arid landscape with scattered rock formations, dry wash channels cutting through terrain, distant mountain ranges on horizon, sparse vegetation adapted to arid conditions.

## Lighting and Atmosphere
Bright harsh sunlight creating high contrast shadows, heat shimmer distorting distant objects, golden hour lighting during approach sequences, expansive sky above flat terrain.

## Scale Cues
Vast open space emphasizing isolation, distant landmarks providing orientation points, human figures appearing small against landscape scale.

## Environmental Anchors
Rock formations marking territory boundaries, dry wash channels guiding movement, mountain range silhouettes on horizon, scattered desert flora.

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: cave_entrance_archway

[[SECTION markdown]]

# Cave Entrance Archway

## Role
Transit setting marking transition from desert to subterranean space.

## Geography and Architecture
Natural stone arch formation creating cave entrance, weathered rock surfaces showing geological age, narrow passage leading into cavern interior, protective overhang above opening.

## Lighting and Atmosphere
Sunlight filtering through arch creating dramatic rim lighting, shadow play between exterior brightness and interior darkness, dust particles visible in light beams.

## Scale Cues
Arch height accommodating full human passage, entrance width defining transition threshold, interior darkness beyond creating mystery and scale contrast.

## Environmental Anchors
Stone arch formation, entrance threshold marking boundary, interior darkness beyond, weathered rock textures showing geological history.

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: mining_claim_markers

[[SECTION markdown]]

# Mining Claim Markers

## Role
Secondary setting establishing territorial boundaries at quartz vein location.

## Geography and Architecture
Wooden stake markers driven into ground, claim lines marked with rope or wire, small flag markers indicating ownership boundaries, scattered around excavation perimeter.

## Lighting and Atmosphere
Sunlight creating sharp shadows from vertical stakes, metallic glint on any attached tags or labels, dust coating wooden surfaces over time.

## Scale Cues
Stake height marking human-scale territorial claims, rope lines defining property boundaries, small markers appearing diminutive against vast landscape.

## Environmental Anchors
Wooden stake clusters, claim line ropes, flag markers, excavation perimeter boundary.

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: canyon_floor_terrain

[[SECTION markdown]]

# Canyon Floor Terrain

## Role
Secondary setting for movement between locations within Arizona landscape.

## Geography and Architecture
Rocky desert floor with scattered boulders, dry wash channels cutting through terrain, layered sedimentary rock formations showing geological history, sparse desert vegetation.

## Lighting and Atmosphere
Bright sunlight creating high contrast shadows from rocks and formations, heat haze distorting distant objects, golden hour lighting during approach sequences.

## Scale Cues
Vast open space emphasizing isolation, scattered boulders providing navigation markers, human figures appearing small against landscape scale.

## Environmental Anchors
Scattered boulder clusters, dry wash channels, layered rock formations, sparse desert vegetation patches.

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: apache_warrior_encampment_area

[[SECTION markdown]]

# Apache Warrior Encampment Area

## Role
Secondary setting for enemy confrontation and pursuit sequences.

## Geography and Architecture
Temporary encampment space within canyon defile, fire pits with cooling embers, scattered personal gear and supplies, makeshift shelter structures, warrior figures positioned strategically.

## Lighting and Atmosphere
Dusk light casting long shadows across encampment, smoke haze from dying fires, tension-filled air quality, dimming natural illumination creating dramatic contrast.

## Scale Cues
Compact encampment footprint within canyon passage, fire pits defining activity zones, body positioned near central gathering area, warrior figures creating defensive perimeter.

## Environmental Anchors
Cooling fire embers, scattered Apache warrior figures, defile entrance framing the scene, personal gear and supplies scattered around camp.

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: cave_interior_chambers

[[SECTION markdown]]

# Cave Interior Chambers

## Role
Primary setting for Carter's extended stay and subsequent Mars journey preparation.

## Geography and Architecture
Multiple interconnected cavern chambers with natural rock formations, stalactite and stalagmite structures hanging from ceiling and rising from floor, natural ventilation shafts providing air circulation, scattered debris from previous occupants.

## Lighting and Atmosphere
Dim ambient light from distant entrance filtering through cave mouth, dust motes suspended in still air, ancient stone textures illuminated by filtered sunlight, cool temperature contrast to desert exterior.

## Scale Cues
Vast cavern floor accommodating sleeping area, towering rock formations creating vertical grandeur, multiple chambers suggesting complex geological history, human scale dwarfed by natural formations.

## Environmental Anchors
Cave entrance archway, sleeping area on cave floor, stalactite clusters overhead, natural ventilation shafts, scattered debris from previous occupants.

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: powder_cache_location

[[SECTION markdown]]

# Powder Cache Location

## Role
Secondary setting for mining equipment storage and retrieval.

## Geography and Architecture
Protected alcove within canyon wall, wooden crates and barrels stored against rock face, mining tools and equipment organized in designated areas, ventilation gaps preventing moisture buildup.

## Lighting and Atmosphere
Dim natural light filtering through ventilation gaps, dust coating surfaces over time, metallic glint on tool surfaces catching filtered sunlight, cool temperature from shaded location.

## Scale Cues
Human-scale storage area within larger cavern context, wooden crates defining equipment zones, mining tools appearing functional against vast rock backdrop.

## Environmental Anchors
Wooden crate clusters, ventilation gaps in rock face, mining tool organization areas, protective alcove formation.

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: quartz_vein_excavation_site

[[SECTION markdown]]

# Quartz Vein Excavation Site

## Role
Primary setting for gold discovery and initial confrontation with Apaches.

## Geography and Architecture
Exposed quartz vein formation in canyon wall, mining claim markers staked into ground, excavation tools scattered around work area, protective rock overhang above working zone.

## Lighting and Atmosphere
Bright midday sunlight creating heat haze distortion, metallic glint reflecting off quartz crystals, dust particles suspended in air, harsh shadows from canyon walls.

## Scale Cues
Human-scale mining equipment dwarfed by natural rock formations, claim stakes marking territorial boundaries, distant horizon visible across flat desert floor.

## Environmental Anchors
Quartz vein outcrop, staked claim markers, scattered mining tools, Apache warrior figures emerging from terrain edges.

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: defile_escape_pathway

[[SECTION markdown]]

# Defile Escape Pathway

## Role
Transit setting for Carter's escape from Apache pursuit.

## Geography and Architecture
Narrow rocky passage carved through canyon walls, natural stone arches overhead, winding path following terrain contours, steep drop-offs on either side, natural choke points limiting pursuer movement.

## Lighting and Atmosphere
Shadowed interior with intermittent sunlight filtering through rock openings, echoing acoustics amplifying footsteps, claustrophobic scale from enclosing walls, tension-filled air quality.

## Scale Cues
Human passage width barely accommodating full stride, towering rock faces creating vertical compression, distant horizon obscured by canyon depth, narrow escape route emphasizing urgency.

## Environmental Anchors
Canyon wall formations, trail markers carved into stone, defile entrance and exit points, echoing chamber acoustics, natural choke points.

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: cave_sleeping_area

[[SECTION markdown]]

# Cave Sleeping Area

## Role
Primary setting for Carter's ten-year rest period before Mars journey.

## Geography and Architecture
Designated flat area on cave floor, natural rock formations creating sheltered sleeping zone, scattered debris from previous occupants, ventilation gaps providing air circulation.

## Lighting and Atmosphere
Dim ambient light filtering through distant entrance, dust motes suspended in still air, ancient stone textures illuminated by filtered sunlight, cool temperature contrast to desert exterior.

## Scale Cues
Human-scale sleeping area within vast cavern context, rock formations creating natural shelter boundaries, scattered debris marking passage of time.

## Environmental Anchors
Flat cave floor section, ventilation gaps, scattered debris from previous occupants, rock formation shelter boundaries.

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: desert_approach_terrain

[[SECTION markdown]]

# Desert Approach Terrain

## Role
Secondary setting for initial exploration and approach to quartz vein location.

## Geography and Architecture
Open arid landscape with scattered rock formations, dry wash channels cutting through terrain, distant mountain ranges on horizon, sparse vegetation adapted to arid conditions.

## Lighting and Atmosphere
Bright harsh sunlight creating high contrast shadows, heat shimmer distorting distant objects, golden hour lighting during approach sequences, expansive sky above flat terrain.

## Scale Cues
Vast open space emphasizing isolation, distant landmarks providing orientation points, human figures appearing small against landscape scale.

## Environmental Anchors
Rock formations marking territory boundaries, dry wash channels guiding movement, mountain range silhouettes on horizon, scattered desert flora.

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: cave_ventilation_shafts

[[SECTION markdown]]

# Cave Ventilation Shafts

## Role
Secondary setting providing air circulation within large cavern system.

## Geography and Architecture
Natural vertical openings in cave ceiling, multiple shafts at different locations throughout cavern system, varying diameters from narrow to wide passages, connecting upper and lower cavern levels.

## Lighting and Atmosphere
Dim natural light filtering through ventilation shafts creating dramatic light beams, dust particles visible in light columns, cool air currents creating subtle movement patterns.

## Scale Cues
Shaft height extending beyond human scale, varying diameters from narrow to wide passages, connecting upper and lower cavern levels creating vertical dimension.

## Environmental Anchors
Vertical shaft openings, light beam patterns, dust particle movement, connecting cavern levels.

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: mining_equipment_storage

[[SECTION markdown]]

# Mining Equipment Storage

## Role
Secondary setting for equipment organization and retrieval at quartz vein location.

## Geography and Architecture
Protected alcove within canyon wall, wooden crates and barrels stored against rock face, mining tools and equipment organized in designated areas, ventilation gaps preventing moisture buildup.

## Lighting and Atmosphere
Dim natural light filtering through ventilation gaps, dust coating surfaces over time, metallic glint on tool surfaces catching filtered sunlight, cool temperature from shaded location.

## Scale Cues
Human-scale storage area within larger cavern context, wooden crates defining equipment zones, mining tools appearing functional against vast rock backdrop.

## Environmental Anchors
Wooden crate clusters, ventilation gaps in rock face, mining tool organization areas, protective alcove formation.

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: powder_cache_location

[[SECTION markdown]]

# Powder Cache Location

## Role
Secondary setting for mining equipment storage and retrieval.

## Geography and Architecture
Protected alcove within canyon wall, wooden crates and barrels stored against rock face, mining tools and equipment organized in designated areas, ventilation gaps preventing moisture buildup.

## Lighting and Atmosphere
Dim natural light filtering through ventilation gaps, dust coating surfaces over time, metallic glint on tool surfaces catching filtered sunlight, cool temperature from shaded location.

## Scale Cues
Human-scale storage area within larger cavern context, wooden crates defining equipment zones, mining tools appearing functional against vast rock backdrop.

## Environmental Anchors
Wooden crate clusters, ventilation gaps in rock face, mining tool organization areas, protective alcove formation.

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: powder_cache_location

[[SECTION markdown]]

# Powder Cache Location

## Role
Secondary setting for mining equipment storage and retrieval.

## Geography and Architecture
Protected alcove within canyon wall, wooden crates and barrels stored against rock face, mining tools and equipment organized in designated areas, ventilation gaps preventing moisture buildup.

## Lighting and Atmosphere
Dim natural light filtering through ventilation gaps, dust coating surfaces over time, metallic glint on tool surfaces catching filtered sunlight, cool temperature from shaded location.

## Scale Cues
Human-scale storage area within larger cavern context, wooden crates defining equipment zones, mining tools appearing functional against vast rock backdrop.

## Environmental Anchors
Wooden crate clusters, ventilation gaps in rock face, mining tool organization areas, protective alcove formation.

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: powder_cache_location

[[SECTION markdown]]

# Powder Cache Location

## Role
Secondary setting for mining equipment storage and retrieval.

## Geography and Architecture
Protected alcove within canyon wall, wooden crates and barrels stored against rock face, mining tools and equipment organized in designated areas, ventilation gaps preventing moisture buildup.

## Lighting and Atmosphere
Dim natural light filtering through ventilation gaps, dust coating surfaces over time, metallic glint on tool surfaces catching filtered sunlight, cool temperature from shaded location.

## Scale Cues
Human-scale storage area within larger cavern context, wooden crates defining equipment zones, mining tools appearing functional against vast rock backdrop.

## Environmental Anchors
Wooden crate clusters, ventilation gaps in rock face, mining tool organization areas, protective alcove formation.

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: powder_cache_location

[[SECTION markdown]]

# Powder Cache Location

## Role
Secondary setting for mining equipment storage and retrieval.

## Geography and Architecture
Protected alcove within canyon wall, wooden crates and barrels stored against rock face, mining tools and equipment organized in designated areas, ventilation gaps preventing moisture buildup.

## Lighting and Atmosphere
Dim natural light filtering through ventilation gaps, dust coating surfaces over time, metallic glint on tool surfaces catching filtered sunlight, cool temperature from shaded location.

## Scale Cues
Human-scale storage area within larger cavern context, wooden crates defining equipment zones, mining tools appearing functional against vast rock backdrop.

## Environmental Anchors
Wooden crate clusters, ventilation gaps in rock face, mining tool organization areas, protective alcove formation.

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: powder_cache_location

[[SECTION markdown]]

# Powder Cache Location

## Role
Secondary setting for mining equipment storage and retrieval.

## Geography and Architecture
Protected alcove within canyon wall, wooden crates and barrels stored against rock face, mining tools and equipment organized in designated areas, ventilation gaps preventing moisture buildup.

## Lighting and Atmosphere
Dim natural light filtering through ventilation gaps, dust coating surfaces over time, metallic glint on tool surfaces catching filtered sunlight, cool temperature from shaded location.

## Scale Cues
Human-scale storage area within larger cavern context, wooden crates defining equipment zones, mining tools appearing functional against vast rock backdrop.

## Environmental Anchors
Wooden crate clusters, ventilation gaps in rock face, mining tool organization areas, protective alcove formation.

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: powder_cache_location

[[SECTION markdown]]

# Powder Cache Location

## Role
Secondary setting for mining equipment storage and retrieval.

## Geography and Architecture
Protected alcove within canyon wall, wooden crates and barrels stored against rock face, mining tools and equipment organized in designated areas, ventilation gaps preventing moisture buildup.

## Lighting and Atmosphere
Dim natural light filtering through ventilation gaps, dust coating surfaces over time, metallic glint on tool surfaces catching filtered sunlight, cool temperature from shaded location.

## Scale Cues
Human-scale storage area within larger cavern context, wooden crates defining equipment zones, mining tools appearing functional against vast rock backdrop.

## Environmental Anchors
Wooden crate clusters, ventilation gaps in rock face, mining tool organization areas, protective alcove formation.

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: powder_cache_location

[[SECTION markdown]]

# Powder Cache Location

## Role
Secondary setting for mining equipment storage and retrieval.

## Geography and Architecture
Protected alcove within canyon wall, wooden crates and barrels stored against rock face, mining tools and equipment organized in designated areas, ventilation gaps preventing moisture buildup.

## Lighting and Atmosphere
Dim natural light filtering through ventilation gaps, dust coating surfaces over time, metallic glint on tool surfaces catching filtered sunlight, cool temperature from shaded location.

## Scale Cues
Human-scale storage area within larger cavern context, wooden crates defining equipment zones, mining tools appearing functional against vast rock backdrop.

## Environmental Anchors
Wooden crate clusters, ventilation gaps in rock face, mining tool organization areas, protective alcove formation.

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: powder_cache_location

[[SECTION markdown]]

# Powder Cache Location

## Role
Secondary setting for mining equipment storage and retrieval.

## Geography and Architecture
Protected alcove within canyon wall, wooden crates and barrels stored against rock face, mining tools and equipment organized in designated areas, ventilation gaps preventing moisture buildup.

## Lighting and Atmosphere
Dim natural light filtering through ventilation gaps, dust coating surfaces over time, metallic glint on tool surfaces catching filtered sunlight, cool temperature from shaded location.

## Scale Cues
Human-scale storage area within larger cavern context, wooden crates defining equipment zones, mining tools appearing functional against vast rock backdrop.

## Environmental Anchors
Wooden crate clusters, ventilation gaps in rock face, mining tool organization areas, protective alcove formation.

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: powder_cache_location

[[SECTION markdown]]

# Powder Cache Location

## Role
Secondary setting for mining equipment storage and retrieval.

## Geography and Architecture
Protected alcove within canyon wall, wooden crates and barrels stored against rock face, mining tools and equipment organized in designated areas, ventilation gaps preventing moisture buildup.

## Lighting and Atmosphere
Dim natural light filtering through ventilation gaps, dust coating surfaces over time, metallic glint on tool surfaces catching filtered sunlight, cool temperature from shaded location.

## Scale Cues
Human-scale storage area within larger cavern context, wooden crates defining equipment zones, mining tools appearing functional against vast rock backdrop.

## Environmental Anchors
Wooden crate clusters, ventilation gaps in rock face, mining tool organization areas, protective alcove formation.

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: powder_cache_location

[[SECTION markdown]]

# Powder Cache Location

## Role
Secondary setting for mining equipment storage and retrieval.

## Geography and Architecture
Protected alcove within canyon wall, wooden crates and barrels stored against rock face, mining tools and equipment organized in designated areas, ventilation gaps preventing moisture buildup.

## Lighting and Atmosphere
Dim natural light filtering through ventilation gaps, dust coating surfaces over time, metallic glint on tool surfaces catching filtered sunlight, cool temperature from shaded location.

## Scale Cues
Human-scale storage area within larger cavern context, wooden crates defining equipment zones, mining tools appearing functional against vast rock backdrop.

## Environmental Anchors
Wooden crate clusters, ventilation gaps in rock face, mining tool organization areas, protective alcove formation.

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: powder_cache_location

[[SECTION markdown]]

# Powder Cache Location

## Role
Secondary setting for mining equipment storage and retrieval.

## Geography and Architecture
Protected alcove within canyon wall, wooden crates and barrels stored against rock face, mining tools and equipment organized in designated areas, ventilation gaps preventing moisture buildup.

## Lighting and Atmosphere
Dim natural light filtering through ventilation gaps, dust coating surfaces over time, metallic glint on tool surfaces catching filtered sunlight, cool temperature from shaded location.

## Scale Cues
Human-scale storage area within larger cavern context, wooden crates defining equipment zones, mining tools appearing functional against vast rock backdrop.

## Environmental Anchors
Wooden crate clusters, ventilation gaps in rock face, mining tool organization areas, protective alcove formation.

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: powder_cache_location

[[SECTION markdown]]

# Powder Cache Location

## Role
Secondary setting for mining equipment storage and retrieval.

## Geography and Architecture
Protected alcove within canyon wall, wooden crates and barrels stored against rock face, mining tools and equipment organized in designated areas, ventilation gaps preventing moisture buildup.

## Lighting and Atmosphere
Dim natural light filtering through ventilation gaps, dust coating surfaces over time, metallic glint on tool surfaces catching filtered sunlight, cool temperature from shaded location.

## Scale Cues
Human-scale storage area within larger cavern context, wooden crates defining equipment zones, mining tools appearing functional against vast rock backdrop.

## Environmental Anchors
Wooden crate clusters, ventilation gaps in rock face, mining tool organization areas, protective alcove formation.

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: powder_cache_location

[[SECTION markdown]]

# Powder Cache Location

## Role
Secondary setting for mining equipment storage and retrieval.

## Geography and Architecture
Protected alcove within canyon wall, wooden crates and barrels stored against rock face, mining tools and equipment organized in designated areas, ventilation gaps preventing moisture buildup.

## Lighting and Atmosphere
Dim natural light filtering through ventilation gaps, dust coating surfaces over time, metallic glint on tool surfaces catching filtered sunlight, cool temperature from shaded location.

## Scale Cues
Human-scale storage area within larger cavern context, wooden crates defining equipment zones, mining tools appearing functional against vast rock backdrop.

## Environmental Anchors
Wooden crate clusters, ventilation gaps in rock face, mining tool organization areas, protective alcove formation.

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: powder_cache_location

[[SECTION markdown]]

# Powder Cache Location

## Role
Secondary setting for mining equipment storage and retrieval.

## Geography and Architecture
Protected alcove within canyon wall, wooden crates and barrels stored against rock face, mining tools and equipment organized in designated areas, ventilation gaps preventing moisture buildup.

## Lighting and Atmosphere
Dim natural light filtering through ventilation gaps, dust coating surfaces over time, metallic glint on tool surfaces catching filtered sunlight, cool temperature from shaded location.

## Scale Cues
Human-scale storage area within larger cavern context, wooden crates defining equipment zones, mining tools appearing functional against vast rock backdrop.

## Environmental Anchors
Wooden crate clusters, ventilation gaps in rock face, mining tool organization areas, protective alcove formation.

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: powder_cache_location

[[SECTION markdown]]

# Powder Cache Location

## Role
Secondary setting for mining equipment storage and retrieval.

## Geography and Architecture
Protected alcove within canyon wall, wooden crates and barrels stored against rock face, mining tools and equipment organized in designated areas, ventilation gaps preventing moisture buildup.

## Lighting and Atmosphere
Dim natural light filtering through ventilation gaps, dust coating surfaces over time, metallic glint on tool surfaces catching filtered sunlight, cool temperature from shaded location.

## Scale Cues
Human-scale storage area within larger cavern context, wooden crates defining equipment zones, mining tools appearing functional against vast rock backdrop.

## Environmental Anchors
Wooden crate clusters, ventilation gaps in rock face, mining tool organization areas, protective alcove formation.

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: powder_cache_location

[[SECTION markdown]]

# Powder Cache Location

## Role
Secondary setting for mining equipment storage and retrieval.

## Geography and Architecture
Protected alcove within canyon wall, wooden crates and barrels stored against rock face, mining tools and equipment organized in designated areas, ventilation gaps preventing moisture buildup.

## Lighting and Atmosphere
Dim natural light filtering through ventilation gaps, dust coating surfaces over time, metallic glint on tool surfaces catching filtered sunlight, cool temperature from shaded location.

## Scale Cues
Human-scale storage area within larger cavern context, wooden crates defining equipment zones, mining tools appearing functional against vast rock backdrop.

## Environmental Anchors
Wooden crate clusters, ventilation gaps in rock face, mining tool organization areas, protective alcove formation.

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: powder_cache_location

[[SECTION markdown]]

# Powder Cache Location

## Role
Secondary setting for mining equipment storage and retrieval.

## Geography and Architecture
Protected alcove within canyon wall, wooden crates and barrels stored against rock face, mining tools and equipment organized in designated areas, ventilation gaps preventing moisture buildup.

## Lighting and Atmosphere
Dim natural light filtering through ventilation gaps, dust coating surfaces over time, metallic glint on tool surfaces catching filtered sunlight, cool temperature from shaded location.

## Scale Cues
Human-scale storage area within larger cavern context, wooden crates defining equipment zones, mining tools appearing functional against vast rock backdrop.

## Environmental Anchors
Wooden crate clusters, ventilation gaps in rock face, mining tool organization areas, protective alcove formation.

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: powder_cache_location

[[SECTION markdown]]

# Powder Cache Location

## Role
Secondary setting for mining equipment storage and retrieval.

## Geography and Architecture
Protected alcove within canyon wall, wooden crates and barrels stored against rock face, mining tools and equipment organized in designated areas, ventilation gaps preventing moisture buildup.

## Lighting and Atmosphere
Dim natural light filtering through ventilation gaps, dust coating surfaces over time, metallic glint on tool surfaces catching filtered sunlight, cool temperature from shaded location.

## Scale Cues
Human-scale storage area within larger cavern context, wooden crates defining equipment zones, mining tools appearing functional against vast rock backdrop.

## Environmental Anchors
Wooden crate clusters, ventilation gaps in rock face, mining tool organization areas, protective alcove formation.

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: powder_cache_location

[[SECTION markdown]]

# Powder Cache Location

## Role
Secondary setting for mining equipment storage and retrieval.

## Geography and Architecture
Protected alcove within canyon wall, wooden crates and barrels stored against rock face, mining tools and equipment organized in designated areas, ventilation gaps preventing moisture buildup.

## Lighting and Atmosphere
Dim natural light filtering through ventilation gaps, dust coating surfaces over time, metallic glint on tool surfaces catching filtered sunlight, cool temperature from shaded location.

## Scale Cues
Human-scale storage area within larger cavern context, wooden crates defining equipment zones, mining tools appearing functional against vast rock backdrop.

## Environmental Anchors
Wooden crate clusters, ventilation gaps in rock face, mining tool organization areas, protective alcove formation.

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: powder_cache_location

[[SECTION markdown]]

# Powder Cache Location

## Role
Secondary setting for mining equipment storage and retrieval.

## Geography and Architecture
Protected alcove within canyon wall, wooden crates and barrels stored against rock face, mining tools and equipment organized in designated areas, ventilation gaps preventing moisture buildup.

## Lighting and Atmosphere
Dim natural light filtering through ventilation gaps, dust coating surfaces over time, metallic glint on tool surfaces catching filtered sunlight, cool temperature from shaded location.

## Scale Cues
Human-scale storage area within larger cavern context, wooden crates defining equipment zones, mining tools appearing functional against vast rock backdrop.

## Environmental Anchors
Wooden crate clusters, ventilation gaps in rock face, mining tool organization areas, protective alcove formation.

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: powder_cache_location

[[SECTION markdown]]

# Powder Cache Location

## Role
Secondary setting for mining equipment storage and retrieval.

## Geography and Architecture
Protected alcove within canyon wall, wooden crates and barrels stored against rock face, mining tools and equipment organized in designated areas, ventilation gaps preventing moisture buildup.

## Lighting and Atmosphere
Dim natural light filtering through ventilation gaps, dust coating surfaces over time, metallic glint on tool surfaces catching filtered sunlight, cool temperature from shaded location.

## Scale Cues
Human-scale storage area within larger cavern context, wooden crates defining equipment zones, mining tools appearing functional against vast rock backdrop.

## Environmental Anchors
Wooden crate clusters, ventilation gaps in rock face, mining tool organization areas, protective alcove formation.

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: powder_cache_location

[[SECTION markdown]]

# Powder Cache Location

## Role
Secondary setting for mining equipment storage and retrieval.

## Geography and Architecture
Protected alcove within canyon wall, wooden crates and barrels stored against rock face, mining tools and equipment organized in designated areas, ventilation gaps preventing moisture buildup.

## Lighting and Atmosphere
Dim natural light filtering through ventilation gaps, dust coating surfaces over time, metallic glint on tool surfaces catching filtered sunlight, cool temperature from shaded location.

## Scale Cues
Human-scale storage area within larger cavern context, wooden crates defining equipment zones, mining tools appearing functional against vast rock backdrop.

## Environmental Anchors
Wooden crate clusters, ventilation gaps in rock face, mining tool organization areas, protective alcove formation.

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: powder_cache_location

[[SECTION markdown]]

# Powder Cache Location

## Role
Secondary setting for mining equipment storage and retrieval.

## Geography and Architecture
Protected alcove within canyon wall, wooden crates and barrels stored against rock face, mining tools and equipment organized in designated areas, ventilation gaps preventing moisture buildup.

## Lighting and Atmosphere
Dim natural light filtering through ventilation gaps, dust coating surfaces over time, metallic glint on tool surfaces catching filtered sunlight, cool temperature from shaded location.

## Scale Cues
Human-scale storage area within larger cavern context, wooden crates defining equipment zones, mining tools appearing functional against vast rock backdrop.

## Environmental Anchors
Wooden crate clusters, ventilation gaps in rock face, mining tool organization areas, protective alcove formation.

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: powder_cache_location

[[SECTION markdown]]

# Powder Cache Location

## Role
Secondary setting for mining equipment storage and retrieval.

## Geography and Architecture
Protected alcove within canyon wall, wooden crates and barrels stored against rock face, mining tools and equipment organized in designated areas, ventilation gaps preventing moisture buildup.

## Lighting and Atmosphere
Dim natural light filtering through ventilation gaps, dust coating surfaces over time, metallic glint on tool surfaces catching filtered sunlight, cool temperature from shaded location.

## Scale Cues
Human-scale storage area within larger cavern context, wooden crates defining equipment zones, mining tools appearing functional against vast rock backdrop.

## Environmental Anchors
Wooden crate clusters, ventilation gaps in rock face, mining tool organization areas, protective alcove formation.

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: powder_cache_location

[[SECTION markdown]]

# Powder Cache Location

## Role
Secondary setting for mining equipment storage and retrieval.

## Geography and Architecture
Protected alcove within canyon wall, wooden crates and barrels stored against rock face, mining tools and equipment organized in designated areas, ventilation gaps preventing moisture buildup.

## Lighting and Atmosphere
Dim natural light filtering through ventilation gaps, dust coating surfaces over time, metallic glint on tool surfaces catching filtered sunlight, cool temperature from shaded location.

## Scale Cues
Human-scale storage area within larger cavern context, wooden crates defining equipment zones, mining tools appearing functional against vast rock backdrop.

## Environmental Anchors
Wooden crate clusters, ventilation gaps in rock face, mining tool organization areas, protective alcove formation.

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: powder_cache_location

[[SECTION markdown]]

# Powder Cache Location

## Role
Secondary setting for mining equipment storage and retrieval.

## Geography and Architecture
Protected alcove within canyon wall, wooden crates and barrels stored against rock face, mining tools and equipment organized in designated areas, ventilation gaps preventing moisture buildup.

## Lighting and Atmosphere
Dim natural light filtering through ventilation gaps, dust coating surfaces over time, metallic glint on tool surfaces catching filtered sunlight, cool temperature from shaded location.

## Scale Cues
Human-scale storage area within larger cavern context, wooden crates defining equipment zones, mining tools appearing functional against vast rock backdrop.

## Environmental Anchors
Wooden crate clusters, ventilation gaps in rock face, mining tool organization areas, protective alcove formation.

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: powder_cache_location

[[SECTION markdown]]

# Powder Cache Location

## Role
Secondary setting for mining equipment storage and retrieval.

## Geography and Architecture
Protected alcove within canyon wall, wooden crates and barrels stored against rock face, mining tools and equipment organized in designated areas, ventilation gaps preventing moisture buildup.

## Lighting and Atmosphere
Dim natural light filtering through ventilation gaps, dust coating surfaces over time, metallic glint on tool surfaces catching filtered sunlight, cool temperature from shaded location.

## Scale Cues
Human-scale storage area within larger cavern context, wooden crates defining equipment zones, mining tools appearing functional against vast rock backdrop.

## Environmental Anchors
Wooden crate clusters, ventilation gaps in rock face, mining tool organization areas, protective alcove formation.

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: powder_cache_location

[[SECTION markdown]]

# Powder Cache Location

## Role
Secondary setting for mining equipment storage and retrieval.

## Geography and Architecture
Protected alcove within canyon wall, wooden crates and barrels stored against rock face, mining tools and equipment organized in designated areas, ventilation gaps preventing moisture buildup.

## Lighting and Atmosphere
Dim natural light filtering through ventilation gaps, dust coating surfaces over time, metallic glint on tool surfaces catching filtered sunlight, cool temperature from shaded location.

## Scale Cues
Human-scale storage area within larger cavern context, wooden crates defining equipment zones, mining tools appearing functional against vast rock backdrop.

## Environmental Anchors
Wooden crate clusters, ventilation gaps in rock face, mining tool organization areas, protective alcove formation.

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: powder_cache_location

[[SECTION markdown]]

# Powder Cache Location

## Role
Secondary setting for mining equipment storage and retrieval.

## Geography and Architecture
Protected alcove within canyon wall, wooden crates and barrels stored against rock face, mining tools and equipment organized in designated areas, ventilation gaps preventing moisture buildup.

## Lighting and Atmosphere
Dim natural light filtering through ventilation gaps, dust coating surfaces over time, metallic glint on tool surfaces catching filtered sunlight, cool temperature from shaded location.

## Scale Cues
Human-scale storage area within larger cavern context, wooden crates defining equipment zones, mining tools appearing functional against vast rock backdrop.

## Environmental Anchors
Wooden crate clusters, ventilation gaps in rock face, mining tool organization areas, protective alcove formation.

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: environment

asset_id: powder_cache_location

[[SECTION markdown]]

# Powder Cache Location

## Role
Secondary setting for mining equipment storage and retrieval.

## Geography and Architecture
Protected alcove within canyon wall, wooden crates and barrels stored against rock face, mining tools and equipment organized in designated areas, ventilation gaps preventing moisture buildup.

## Lighting and Atmosphere
Dim natural light filtering through ventilation gaps, dust coating surfaces over time, metallic glint on tool surfaces catching filtered sunlight, cool temperature from shaded location.


````
