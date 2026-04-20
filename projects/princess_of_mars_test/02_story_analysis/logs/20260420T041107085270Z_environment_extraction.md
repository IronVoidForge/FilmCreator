# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-20T04:11:07.085270+00:00
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

Chapter id: CH024

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

# Chapter CH024: Tars Tarkas Finds a Friend

## Narrative Summary

### Scene 1: Crash and Rescue
John Carter flies over a dead city and crashes into a battle between green warriors and Warhoons. He lands in the center of combat, drawing his long-sword to defend himself. He falls beside Tars Tarkas, who is fighting three antagonists (Warhoons). Tars Tarkas is knocked down by a dead body behind him. Carter springs before Tars Tarkas' prostrate form and engages the adversaries. After accounting for one, Carter helps Tars Tarkas settle the other.

### Scene 2: The Friendship Acknowledgement
Tars Tarkas gives Carter a look and a slight smile, touching his shoulder. He says he would scarcely recognize John Carter but notes there is no other mortal on Barsoom who would have done what Carter did for him. He states he has learned that there is such a thing as friendship. The Warhoons close in, and they fight shoulder to shoulder until the tide turns and the Warhoon horde flees into darkness. Ten thousand men were engaged; three thousand dead lie on the field.

### Scene 3: Return to Thark and Departure
On return to the city, Carter waits in Tars Tarkas' quarters while the chieftain attends council. A huge creature (Woola) rushes upon Carter in an adjoining apartment. Woola had found his way back to Thark and taken up watch for Carter's return at his former quarters. Tars Tarkas returns from the jeddak's quarters, informing Carter that Tal Hajus has ordered him brought before him tonight. Tars Tarkas offers ten thoats and will accompany Carter to the nearest waterway leading to Helium.

### Scene 4: Confrontation with Sarkoja
Carter asks about Tars Tarkas' return; he replies "the wild calots, possibly, or worse," unless he battles Tal Hajus. Carter insists on staying to see Tal Hajus tonight. They eat while Carter repeats the story Sola told him on the sea bottom. Tars Tarkas works in passion and agony at recollection of horrors heaped upon Woola. He agrees to go before Tal Hajus but wants to speak to Sarkoja first. Carter accompanies him; Sarkoja casts a look of venomous hatred. Tars Tarkas warns her about Gozava's lover seeking revenge, suggesting she might be tied to a wild thoat for survival test. The next morning Sarkoja is gone and never seen again.

### Scene 5: Palace Confrontation
They hasten to the jeddak's palace; Tal Hajus stands erect on his platform glowering at the entrance. He shrieks to strap Carter to a pillar, heat irons, and burn eyes from his head. Carter turns to the assembled council, ignoring Tal Hajus, claiming he has been a chief among them and fought for Thark. He accuses Tal Hajus of cowardice (didn't fight in battle) and asks how sounds "Jeddak of Thark?" A roar of applause greets this suggestion. Lorquas Ptomel asks if the jeddak must prove fitness to rule; twenty chieftains flash swords in assent.

### Scene 6: Victory and New Plan
Tal Hajus draws his long-sword and advances to meet Tars Tarkas. The combat is soon over; Tars Tarkas stands with foot upon neck of dead monster, becoming jeddak among the Tharks. His first act is making Carter a full-fledged chieftain. Carter enlists them in his cause against Zodanga, telling Tars Tarkas the story of adventures and explaining the thought. Tars Tarkas addresses the council: Dejah Thoris is held by Zodanga; rescue her and return to Helium. Loot of Zodanga would be magnificent; alliance with Helium could increase hatchings and make them supreme among green men. They rise to the bait as a speckled trout to a fly. Twenty mounted messengers speed across dead sea bottoms to call hordes together.

### Scene 7: March to Zodanga
In three days they are on march toward Zodanga, one hundred thousand strong (enlisted services of three smaller hordes). At head of column Carter rides beside great Thark; Woola trots at heels. They travel entirely by night, camping during day at deserted cities where beasts kept indoors. Tars Tarkas enlists fifty thousand more warriors from various hordes. Ten days after setting out they halt at midnight outside Zodanga, one hundred and fifty thousand strong. Fighting strength equivalent to ten times their number of red men. Task of obtaining entry devolves upon Carter; he directs Tars Tarkas to hold forces in two divisions opposite large gateways.

### Scene 8: Wall Climb Entry
Carter takes twenty dismounted warriors and approaches one of small gates piercing walls at short intervals. Walls are seventy-five feet high, fifty feet thick, built of enormous blocks of carborundum. Placing three warriors with faces to wall arms locked, Carter commands two more to mount shoulders; sixth climbs upon shoulders of upper two. Head of topmost warrior towers over forty feet from ground. In this way, with ten warriors, he builds series of three steps from ground to shoulders of topmost man. Starting from short distance behind them, he runs swiftly up from one tier to next, final bound from broad shoulders of highest he clutches top of great wall and draws himself to broad expanse. After him he drags six lengths of leather from equal number of warriors; previously fastened together. Passing one end to topmost warrior, he lowers other end cautiously over opposite side toward avenue below. Lowering himself to end of leather strap, he drops remaining thirty feet to pavement below.

### Scene 9: Palace Grounds Entry
Carter learned secret of opening gates from Kantos Kan; in another moment twenty great fighting men stand within doomed city of Zodanga. He finds delight that entered at lower boundary of enormous palace grounds. Building itself shows blaze of glorious light in distance. He determines to lead detachment directly within palace itself while balance of horde attacks barracks of soldiery. Dispatching one man to Tars Tarkas for detail of fifty Tharks, he orders ten warriors to capture and open one of great gates while nine remaining take the other. Plans work to perfection; sentries dispatched to fathers upon banks of lost sea of Korus; guards at both gates follow in silence.
````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
task: environment_extraction
version: 1

[[SECTION environment_index_markdown]]
# Environment Index - Chapter CH024

## dead_city
**Role:** Primary setting  
**Architecture/Geography:** Dead city with battle field, green warriors and Warhoons combat zone  
**Lighting/Atmosphere:** Combat scene lighting, battlefield atmosphere  
**Scale:** Ten thousand men engaged, three thousand dead on field  
**Anchors:** Battle field center, dead body pile

## thark_quarters
**Role:** Secondary setting  
**Architecture/Geography:** Chieftain quarters with adjoining apartments, jeddak's quarters entrance  
**Lighting/Atmosphere:** Interior apartment lighting, council chamber atmosphere  
**Scale:** Adjoining apartment space, council gathering area  
**Anchors:** Tars Tarkas quarters, Woola watch position

## jeddak_palace_platform
**Role:** Secondary setting  
**Architecture/Geography:** Palace platform with entrance gateways, assembled council area  
**Lighting/Atmosphere:** Platform glowering lighting, heated irons threat atmosphere  
**Scale:** Erect platform height, pillar binding location  
**Anchors:** Tal Hajus platform, pillar binding point

## zodanga_city
**Role:** Primary setting  
**Architecture/Geography:** City walls seventy-five feet high fifty feet thick of carborundum blocks, palace grounds with enormous building blaze of light, barracks of soldiery, large gateways  
**Lighting/Atmosphere:** Blaze of glorious light in distance, doomed city atmosphere  
**Scale:** Walls forty feet from ground to shoulders, thirty feet drop to pavement, seventy-five feet high walls  
**Anchors:** Carborundum wall blocks, palace building blaze, great gates

## lost_sea_korus_banks
**Role:** Transit setting  
**Architecture/Geography:** Banks of lost sea with sentry fathers upon banks  
**Lighting/Atmosphere:** Lost sea atmosphere, banks lighting  
**Scale:** Bank edge location, sentry father position  
**Anchors:** Lost sea banks, sentry father point

[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: dead_city

[[SECTION markdown]]
# Dead City Environment

## Role
Primary setting for crash and rescue sequence.

## Architecture/Geography
Dead city with battle field where green warriors and Warhoons combat takes place. Center of combat serves as landing zone for John Carter's crash.

## Lighting/Atmosphere
Combat scene lighting with battlefield atmosphere during engagement between opposing forces.

## Scale Cues
Ten thousand men engaged in battle, three thousand dead lie on the field. Dead body pile forms anchor point near Tars Tarkas prostrate form.

## Environmental Anchors
Battle field center, dead body pile location, combat zone boundaries.

## Descriptive Noun Phrases
Dead city battle field, green warrior combat zone, Warhoon engagement area, battlefield landing zone, dead body pile anchor.

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: thark_quarters

[[SECTION markdown]]
# Thark Quarters Environment

## Role
Secondary setting for waiting and council scenes.

## Architecture/Geography
Chieftain quarters with adjoining apartments, jeddak's quarters entrance area. Interior apartment space for Carter waiting period.

## Lighting/Atmosphere
Interior apartment lighting during waiting sequence, council chamber atmosphere when Tars Tarkas returns from jeddak's quarters.

## Scale Cues
Adjoining apartment space dimensions, council gathering area capacity. Woola watch position in former quarters.

## Environmental Anchors
Tars Tarkas quarters entrance, adjoining apartment boundary, Woola watch location, jeddak's quarters doorway.

## Descriptive Noun Phrases
Chieftain quarters interior, adjoining apartment space, jeddak quarters entrance, Woola watch position, council chamber area.

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: jeddak_palace_platform

[[SECTION markdown]]
# Jeddak Palace Platform Environment

## Role
Secondary setting for confrontation and binding scene.

## Architecture/Geography
Palace platform with entrance gateways, assembled council area. Platform height with erect standing position.

## Lighting/Atmosphere
Platform glowering lighting during Tal Hajus threat display, heated irons threat atmosphere during binding sequence.

## Scale Cues
Erect platform height, pillar binding location for Carter restraint. Entrance gateway dimensions.

## Environmental Anchors
Tal Hajus platform position, pillar binding point, entrance gateways, assembled council area.

## Descriptive Noun Phrases
Palace platform height, entrance gateway structure, pillar binding location, glowering platform stance, heated irons threat zone.

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: zodanga_city

[[SECTION markdown]]
# Zodanga City Environment

## Role
Primary setting for final assault and palace entry sequence.

## Architecture/Geography
City walls seventy-five feet high fifty feet thick built of enormous blocks of carborundum. Palace grounds with enormous building showing blaze of glorious light in distance. Barracks of soldiery. Large gateways opposite main approaches.

## Lighting/Atmosphere
Blaze of glorious light in distance from palace building, doomed city atmosphere throughout assault sequence.

## Scale Cues
Walls forty feet from ground to shoulders of topmost warrior, thirty feet drop to pavement below, seventy-five feet high walls total height.

## Environmental Anchors
Carborundum wall blocks, palace building blaze location, great gates, barracks of soldiery, avenue below wall.

## Descriptive Noun Phrases
Carborundum wall blocks, palace grounds blaze, doomed city entrance, great gateways, barracks of soldiery, seventy-five foot walls.

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: lost_sea_korus_banks

[[SECTION markdown]]
# Lost Sea Korus Banks Environment

## Role
Transit setting for sentry dispatch and guard movement.

## Architecture/Geography
Banks of lost sea with sentry fathers positioned upon banks. Guard positions at both gates following in silence.

## Lighting/Atmosphere
Lost sea atmosphere along bank edges, guard position lighting during silent movement.

## Scale Cues
Bank edge location dimensions, sentry father position height relative to water level.

## Environmental Anchors
Lost sea banks edge, sentry father position point, gate entrance locations.

## Descriptive Noun Phrases
Lost sea banks edge, sentry father position, guard movement path, bank water boundary, silent guard zone.

[[/SECTION]]
[[/FILMCREATOR_RECORD]]
[[/FILMCREATOR_PACKET]]
````
