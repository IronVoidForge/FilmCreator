# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-18T04:25:57.402388+00:00
- task: environment_extraction

## System Prompt
````text
You are FilmCreator's local authoring analyst.
Return exactly one FILMCREATOR packet in Markdown.
Do not return JSON.
Do not use markdown fences.
Do not add commentary before or after the packet.
Preserve uncertainty instead of inventing hidden facts.
When asked to write Markdown file contents, place the complete file body inside the requested SECTION tags.
When asked to extract render-facing facts, focus on visible, continuity-relevant details.
````

## User Prompt
````text
Project slug: princess_of_mars_test

Chapter id: CH001

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



Each environment Markdown file should include:

- environment role such as primary, secondary, or transit setting

- architecture or geography

- lighting and atmosphere cues

- scale cues and recurring environmental anchors

- useful descriptive noun phrases for later render-facing prompt writing



Chapter summary:

# Chapter Summary: A Fair Captive from the Sky

**Scene Sequence:**

1.  **Retreat to Cover:** Three days after an incubator ceremony, the Martians retreat from open ground into buildings. John Carter and Sola enter a specific building on the city front where Carter previously encountered apes. Carter ascends to an upper floor to observe the valley.
2.  **Airship Arrival:** Twenty long, low, gray-painted airships appear over the nearest hill, swinging slowly toward the city. They carry strange banners and odd devices on their prows. Figures crowd the forward decks and upper works.
3.  **Initial Engagement:** The green Martians fire a volley from building windows without warning. The foremost vessel swings broadside to return fire, maneuvering in a circle to maintain firing position. Other vessels follow suit.
4.  **Battle Dynamics:** Carter observes high accuracy from the Martians; bullets drop at gun explosions and banners dissolve in flame. The ships' fire is ineffectual due to suddenness of the first volley catching crews unprepared.
5.  **Targeting Specifics:** Martians target objective points: wireless finding apparatus, sighting guns, gunners, officers, crew members, upper works, steering gear, and propellers.
6.  **Fleet Retreat:** Twenty minutes after the first volley, the fleet swings away. Several craft limp perceptibly with depleted crews. Fire ceases as energies focus on escape.
7.  **Disabled Ship:** One craft receives the brunt of fire and is entirely unmanned. It drifts erratically toward the city, fifty feet above ground.
8.  **Recovery Operation:** Warriors rush to meet the drifting ship. They swarm from windows using spears to ease collision shock. Grappling hooks are thrown to haul the boat to ground.
9.  **Looting:** Warriors search the vessel stem to stern. A party drags a little figure (the captive) out. The loot includes arms, ammunition, silks, furs, jewels, carved stone vessels, and casks of water.
10. **Destruction:** After looting, warriors tow the craft away then board it to empty carboys over dead sailors and decks. The last warrior throws a missile that ignites the vessel. Guy ropes are released, and the warship soars into the air as a flaming derelict.
11. **Emotional Aftermath:** Carter descends to the street feeling depressed about the "defeat" of kindred people. The cavalcade returns to the plaza but remains there for over a week due to fear of return attacks. Lorquas Ptomel keeps the caravan in the deserted city for safety.
12. **Captive Discovery:** As Sola and Carter enter the plaza, they see the prisoner from the battle craft being dragged into a nearby building by green Martian females.
13. **Visual Encounter:** The captive is described as a slender, girlish figure similar to earthly women. She has an oval face, finely chiseled features, large lustrous eyes, and coal black waving hair caught loosely. Her skin is light reddish copper with crimson cheeks and ruby lips. She is destitute of clothes except for highly wrought ornaments.
14. **Interaction:** The captive's eyes meet Carter's in astonishment. She makes a sign he does not understand. Hope glories her face, then fades into dejection, loathing, and contempt as she realizes he did not answer her signal for succor. She is dragged away into the building depths.

**Visual Continuity Facts:**
*   **Airship Appearance:** Long, low, gray-painted vessels with banners and odd devices on prows.
*   **Martian Attire:** Green warriors operating from buildings and rooftops.
*   **Captive Description:** Slender, girlish figure, light reddish copper skin, coal black hair, naked except ornaments.
*   **Environment:** City buildings with upper floors and windows; open plaza; valley and hills beyond.
*   **Action Details:** Grappling hooks used to haul ship; guy ropes released for fire launch; casks of water visible as loot.

**Broad Story Summary:**
The chapter depicts a naval-style engagement between ground forces and aerial vessels. The green Martians successfully defend their city against an attacking fleet, destroying one ship and capturing its sole surviving female occupant. The event marks a shift in Carter's emotional state from observation to personal involvement, as he witnesses the capture of a being who resembles his own kind but is treated as property by the Martians. The destruction of the airship serves as a funeral pyre for the fleet, highlighting the ruthlessness of the Martian warriors while simultaneously sparking Carter's hope that the fleet might return for revenge.



Chapter source markdown:

# Title
A Princess of Mars - Chapter VIII - A Fair Captive from the Sky

# Work
A Princess of Mars

# Chapter
CH001

# Chapter Label
Chapter VIII - A Fair Captive from the Sky

# Author
Edgar Rice Burroughs

# Source
Project Gutenberg Ebook 62

# Source URL
https://www.gutenberg.org/files/62/62-h/62-h.htm

# Notes
Paste the full text of Chapter VIII below in the `# Text` section.
Keep the chapter text as plain prose with no extra commentary added by us.

# Text
A FAIR CAPTIVE FROM THE SKY

The third day after the incubator ceremony we set forth toward home, but scarcely had the head of the procession debouched into the open ground before the city than orders were given for an immediate and hasty return. As though trained for years in this particular evolution, the green Martians melted like mist into the spacious doorways of the nearby buildings, until, in less than three minutes, the entire cavalcade of chariots, mastodons and mounted warriors was nowhere to be seen.

Sola and I had entered a building upon the front of the city, in fact, the same one in which I had had my encounter with the apes, and, wishing to see what had caused the sudden retreat, I mounted to an upper floor and peered from the window out over the valley and the hills beyond; and there I saw the cause of their sudden scurrying to cover. A huge craft, long, low, and gray-painted, swung slowly over the crest of the nearest hill. Following it came another, and another, and another, until twenty of them, swinging low above the ground, sailed slowly and majestically toward us.

Each carried a strange banner swung from stem to stern above the upper works, and upon the prow of each was painted some odd device that gleamed in the sunlight and showed plainly even at the distance at which we were from the vessels. I could see figures crowding the forward decks and upper works of the air craft. Whether they had discovered us or simply were looking at the deserted city I could not say, but in any event they received a rude reception, for suddenly and without warning the green Martian warriors fired a terrific volley from the windows of the buildings facing the little valley across which the great ships were so peacefully advancing.

Instantly the scene changed as by magic; the foremost vessel swung broadside toward us, and bringing her guns into play returned our fire, at the same time moving parallel to our front for a short distance and then turning back with the evident intention of completing a great circle which would bring her up to position once more opposite our firing line; the other vessels followed in her wake, each one opening upon us as she swung into position. Our own fire never diminished, and I doubt if twenty-five per cent of our shots went wild. It had never been given me to see such deadly accuracy of aim, and it seemed as though a little figure on one of the craft dropped at the explosion of each bullet, while the banners and upper works dissolved in spurts of flame as the irresistible projectiles of our warriors mowed through them.

The fire from the vessels was most ineffectual, owing, as I afterward learned, to the unexpected suddenness of the first volley, which caught the ship’s crews entirely unprepared and the sighting apparatus of the guns unprotected from the deadly aim of our warriors.

It seems that each green warrior has certain objective points for his fire under relatively identical circumstances of warfare. For example, a proportion of them, always the best marksmen, direct their fire entirely upon the wireless finding and sighting apparatus of the big guns of an attacking naval force; another detail attends to the smaller guns in the same way; others pick off the gunners; still others the officers; while certain other quotas concentrate their attention upon the other members of the crew, upon the upper works, and upon the steering gear and propellers.

Twenty minutes after the first volley the great fleet swung trailing off in the direction from which it had first appeared. Several of the craft were limping perceptibly, and seemed but barely under the control of their depleted crews. Their fire had ceased entirely and all their energies seemed focused upon escape. Our warriors then rushed up to the roofs of the buildings which we occupied and followed the retreating armada with a continuous fusillade of deadly fire.

One by one, however, the ships managed to dip below the crests of the outlying hills until only one barely moving craft was in sight. This had received the brunt of our fire and seemed to be entirely unmanned, as not a moving figure was visible upon her decks. Slowly she swung from her course, circling back toward us in an erratic and pitiful manner. Instantly the warriors ceased firing, for it was quite apparent that the vessel was entirely helpless, and, far from being in a position to inflict harm upon us, she could not even control herself sufficiently to escape.

As she neared the city the warriors rushed out upon the plain to meet her, but it was evident that she still was too high for them to hope to reach her decks. From my vantage point in the window I could see the bodies of her crew strewn about, although I could not make out what manner of creatures they might be. Not a sign of life was manifest upon her as she drifted slowly with the light breeze in a southeasterly direction.

She was drifting some fifty feet above the ground, followed by all but some hundred of the warriors who had been ordered back to the roofs to cover the possibility of a return of the fleet, or of reinforcements. It soon became evident that she would strike the face of the buildings about a mile south of our position, and as I watched the progress of the chase I saw a number of warriors gallop ahead, dismount and enter the building she seemed destined to touch.

As the craft neared the building, and just before she struck, the Martian warriors swarmed upon her from the windows, and with their great spears eased the shock of the collision, and in a few moments they had thrown out grappling hooks and the big boat was being hauled to ground by their fellows below.

After making her fast, they swarmed the sides and searched the vessel from stem to stern. I could see them examining the dead sailors, evidently for signs of life, and presently a party of them appeared from below dragging a little figure among them. The creature was considerably less than half as tall as the green Martian warriors, and from my balcony I could see that it walked erect upon two legs and surmised that it was some new and strange Martian monstrosity with which I had not as yet become acquainted.

They removed their prisoner to the ground and then commenced a systematic rifling of the vessel. This operation required several hours, during which time a number of the chariots were requisitioned to transport the loot, which consisted in arms, ammunition, silks, furs, jewels, strangely carved stone vessels, and a quantity of solid foods and liquids, including many casks of water, the first I had seen since my advent upon Mars.

After the last load had been removed the warriors made lines fast to the craft and towed her far out into the valley in a southwesterly direction. A few of them then boarded her and were busily engaged in what appeared, from my distant position, as the emptying of the contents of various carboys upon the dead bodies of the sailors and over the decks and works of the vessel.

This operation concluded, they hastily clambered over her sides, sliding down the guy ropes to the ground. The last warrior to leave the deck turned and threw something back upon the vessel, waiting an instant to note the outcome of his act. As a faint spurt of flame rose from the point where the missile struck he swung over the side and was quickly upon the ground. Scarcely had he alighted than the guy ropes were simultaneously released, and the great warship, lightened by the removal of the loot, soared majestically into the air, her decks and upper works a mass of roaring flames.

Slowly she drifted to the southeast, rising higher and higher as the flames ate away her wooden parts and diminished the weight upon her. Ascending to the roof of the building I watched her for hours, until finally she was lost in the dim vistas of the distance. The sight was awe-inspiring in the extreme as one contemplated this mighty floating funeral pyre, drifting unguided and unmanned through the lonely wastes of the Martian heavens; a derelict of death and destruction, typifying the life story of these strange and ferocious creatures into whose unfriendly hands fate had carried it.

Much depressed, and, to me, unaccountably so, I slowly descended to the street. The scene I had witnessed seemed to mark the defeat and annihilation of the forces of a kindred people, rather than the routing by our green warriors of a horde of similar, though unfriendly, creatures. I could not fathom the seeming hallucination, nor could I free myself from it; but somewhere in the innermost recesses of my soul I felt a strange yearning toward these unknown foemen, and a mighty hope surged through me that the fleet would return and demand a reckoning from the green warriors who had so ruthlessly and wantonly attacked it.

Close at my heel, in his now accustomed place, followed Woola, the hound, and as I emerged upon the street Sola rushed up to me as though I had been the object of some search on her part. The cavalcade was returning to the plaza, the homeward march having been given up for that day; nor, in fact, was it recommenced for more than a week, owing to the fear of a return attack by the air craft.

Lorquas Ptomel was too astute an old warrior to be caught upon the open plains with a caravan of chariots and children, and so we remained at the deserted city until the danger seemed passed.

As Sola and I entered the plaza a sight met my eyes which filled my whole being with a great surge of mingled hope, fear, exultation, and depression, and yet most dominant was a subtle sense of relief and happiness; for just as we neared the throng of Martians I caught a glimpse of the prisoner from the battle craft who was being roughly dragged into a nearby building by a couple of green Martian females.

And the sight which met my eyes was that of a slender, girlish figure, similar in every detail to the earthly women of my past life. She did not see me at first, but just as she was disappearing through the portal of the building which was to be her prison she turned, and her eyes met mine. Her face was oval and beautiful in the extreme, her every feature was finely chiseled and exquisite, her eyes large and lustrous and her head surmounted by a mass of coal black, waving hair, caught loosely into a strange yet becoming coiffure. Her skin was of a light reddish copper color, against which the crimson glow of her cheeks and the ruby of her beautifully molded lips shone with a strangely enhancing effect.

She was as destitute of clothes as the green Martians who accompanied her; indeed, save for her highly wrought ornaments she was entirely naked, nor could any apparel have enhanced the beauty of her perfect and symmetrical figure.

As her gaze rested on me her eyes opened wide in astonishment, and she made a little sign with her free hand; a sign which I did not, of course, understand. Just a moment we gazed upon each other, and then the look of hope and renewed courage which had glorified her face as she discovered me, faded into one of utter dejection, mingled with loathing and contempt. I realized I had not answered her signal, and ignorant as I was of Martian customs, I intuitively felt that she had made an appeal for succor and protection which my unfortunate ignorance had prevented me from answering. And then she was dragged out of my sight into the depths of the deserted edifice. 

````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
task: environment_extraction
version: 1

[[SECTION environment_index_markdown]]
# Environment Index - A Fair Captive from the Sky

## Primary Environments

### city_buildings
- **Role:** Primary setting
- **Architecture:** Multi-story structures with spacious doorways, upper floors, windows facing valley
- **Lighting:** Sunlight visible on buildings, interior shadows from window openings
- **Scale:** Large enough to observe fleet from distance; warriors swarm from multiple levels
- **Anchors:** Building fronts, upper floor observation points, window firing positions

### open_plaza_ground
- **Role:** Secondary setting  
- **Architecture:** Open ground space, deserted city plaza with building portals
- **Lighting:** Daylight conditions, open sky visibility
- **Scale:** Large enough for fleet to drift overhead; cavalcade assembly point
- **Anchors:** Building entrances, street level, distant observation points

### valley_hills_beyond
- **Role:** Transit/observation setting
- **Architecture:** Natural landscape with hill crests and valley floor
- **Lighting:** Sunlight on hills, atmospheric haze at distance
- **Scale:** Fleet appears over hill crests; drifts across valley fifty feet above ground
- **Anchors:** Hill crests, distant vistas, directional flight paths

## Secondary Environments

### airship_fleet
- **Role:** Mobile environment
- **Architecture:** Long, low, gray-painted vessels with banners and odd devices on prows
- **Lighting:** Sunlight gleaming on painted surfaces, flames from destroyed vessel
- **Scale:** Twenty vessels; individual craft fifty feet above ground when drifting
- **Anchors:** Stem to stern banners, upper works, steering gear, propellers

### building_interiors
- **Role:** Interior setting
- **Architecture:** Building depths with windows and doorways
- **Lighting:** Dim interior spaces, natural light from window openings
- **Scale:** Warriors search vessel stem to stern; captive dragged into building depths
- **Anchors:** Windows for swarming, portals for prisoner movement

[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: city_buildings

[[SECTION markdown]]
# City Buildings Environment

## Overview
Multi-story urban structures serving as primary defensive positions and observation points during Martian fleet engagement.

## Architecture & Geography
- Spacious doorways with mist-like entry/exit patterns
- Upper floors accessible for valley observation
- Windows facing the little valley across which ships advance
- Building fronts positioned on city perimeter
- Interior depths accessible through building portals

## Lighting & Atmosphere
- Sunlight visible on exterior surfaces
- Interior shadows from window openings
- Daylight conditions throughout engagement
- Atmospheric visibility allowing distant fleet observation

## Scale Cues
- Large enough for warriors to swarm from multiple levels
- Upper floors provide elevated observation vantage points
- Windows serve as firing positions for volley engagements
- Building fronts positioned for maximum defensive coverage

## Environmental Anchors
- Building front locations on city perimeter
- Upper floor observation decks
- Window firing positions facing valley
- Interior depths accessible through portals
- Doorways with spacious entry patterns

## Descriptive Noun Phrases
- Spacious doorways of nearby buildings
- Upper floors for valley observation
- Windows facing the little valley
- Building fronts on city perimeter
- Interior depths of deserted edifice
- Portal entrances to building interiors
- Elevated observation vantage points
- Window firing positions

## Render-Facing Prompt Elements
- Multi-story defensive structures
- Urban buildings with upper levels
- Window openings for engagement
- Spacious entry doorways
- Building front positioning
- Interior depth accessibility
- Elevated observation platforms
- Defensive urban architecture

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: open_plaza_ground

[[SECTION markdown]]
# Open Plaza Ground Environment

## Overview
Open ground space serving as secondary setting for fleet observation and cavalcade assembly during engagement aftermath.

## Architecture & Geography
- Open ground space with deserted city plaza
- Building portals accessible from plaza level
- Street level positioning for warrior movement
- Assembly point for returning cavalcade
- Homeward march termination location

## Lighting & Atmosphere
- Daylight conditions throughout plaza
- Open sky visibility from plaza level
- Natural light on open ground surfaces
- Atmospheric conditions allowing distant observation

## Scale Cues
- Large enough for fleet to drift overhead at fifty feet altitude
- Cavalcade assembly point for returning warriors
- Street level positioning for prisoner movement
- Plaza space accommodating multiple warrior groups

## Environmental Anchors
- Building entrances from plaza level
- Street level positions
- Distant observation points from plaza
- Assembly locations for cavalcade
- Portal access points to building interiors

## Descriptive Noun Phrases
- Open ground space of deserted city
- Plaza with building portals
- Street level positioning
- Cavalcade assembly point
- Homeward march termination location
- Building entrance access from plaza
- Distant observation vantage points

## Render-Facing Prompt Elements
- Open plaza ground surfaces
- Deserted city assembly spaces
- Building portal access points
- Street level positions
- Plaza accommodation for groups
- Open sky visibility conditions
- Assembly point locations
- Ground surface positioning

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: valley_hills_beyond

[[SECTION markdown]]
# Valley Hills Beyond Environment

## Overview
Natural landscape beyond city limits serving as transit and observation setting for fleet appearance and movement.

## Architecture & Geography
- Natural landscape with hill crests and valley floor
- Hill crests where fleet appears over nearest hill
- Valley floor below city buildings
- Directional flight paths across valley
- Distant vistas visible from building windows

## Lighting & Atmosphere
- Sunlight on hills beyond city
- Atmospheric haze at distance
- Daylight conditions for fleet observation
- Dim vistas in distance for ascending vessel

## Scale Cues
- Fleet appears over hill crests at low altitude
- Individual craft drifts fifty feet above ground
- Ascending vessel rises higher as flames consume wooden parts
- Distant views allowing hours of observation

## Environmental Anchors
- Hill crests beyond city perimeter
- Valley floor below building positions
- Directional flight paths across landscape
- Distant vista observation points
- Outlying hills for fleet retreat

## Descriptive Noun Phrases
- Natural landscape beyond city limits
- Hill crests where fleet appears
- Valley floor below buildings
- Directional flight paths across valley
- Distant vistas visible from windows
- Outlying hills for fleet movement
- Ascending vessel in distant views

## Render-Facing Prompt Elements
- Natural landscape terrain
- Hill crest positioning
- Valley floor surfaces
- Distant vista visibility
- Atmospheric haze conditions
- Directional flight paths
- Landscape beyond city perimeter
- Elevated observation vantage points

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: airship_fleet

[[SECTION markdown]]
# Airship Fleet Environment

## Overview
Mobile aerial vessels serving as attacking fleet during engagement, with one vessel destroyed and captured.

## Architecture & Geography
- Long, low, gray-painted vessels
- Banners swung from stem to stern above upper works
- Odd devices painted on prow of each vessel
- Upper works visible from building windows
- Steering gear and propellers as target points

## Lighting & Atmosphere
- Sunlight gleaming on painted surfaces
- Flames from destroyed vessel rising in spurt
- Daylight conditions throughout engagement
- Roaring flames consuming wooden parts

## Scale Cues
- Twenty vessels swinging low above ground
- Individual craft fifty feet above ground when drifting
- Fleet appears over crest of nearest hill
- Ascending vessel rises higher as flames consume parts

## Environmental Anchors
- Stem to stern banner positions
- Upper works visible from windows
- Steering gear and propellers
- Prow devices on each vessel
- Gun positions in attacking fleet

## Descriptive Noun Phrases
- Long, low, gray-painted vessels
- Banners swung from stem to stern
- Odd devices painted on prows
- Upper works visible from windows
- Steering gear and propellers
- Gun positions in attacking fleet
- Roaring flames consuming vessel
- Flaming derelict drifting southeast

## Render-Facing Prompt Elements
- Mobile aerial vessels
- Gray-painted hull surfaces
- Banner positioning stem to stern
- Prow device installations
- Upper works structures
- Steering gear mechanisms
- Propeller components
- Gun positions on vessels
- Flame consumption effects
- Drifting vessel movement patterns

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: building_interiors

[[SECTION markdown]]
# Building Interiors Environment

## Overview
Interior spaces of buildings serving as defensive positions and prisoner containment areas during engagement.

## Architecture & Geography
- Building depths accessible through portals
- Windows for swarming from upper levels
- Doorways with spacious entry patterns
- Interior spaces for prisoner movement
- Building interiors for warrior search operations

## Lighting & Atmosphere
- Dim interior spaces from window openings
- Natural light filtering through windows
- Interior shadows from window positions
- Daylight conditions visible from interior

## Scale Cues
- Warriors search vessel stem to stern from interior
- Prisoner dragged into building depths
- Multiple levels accessible for warrior movement
- Interior space accommodating prisoner containment

## Environmental Anchors
- Windows for swarming operations
- Building portals for prisoner movement
- Interior depth access points
- Doorway entry positions
- Window opening locations

## Descriptive Noun Phrases
- Building depths accessible through portals
- Windows for swarming from upper levels
- Interior spaces for prisoner containment
- Doorways with spacious entry patterns
- Building interiors for warrior search
- Portal access to building depths
- Window opening positions
- Interior depth accessibility

## Render-Facing Prompt Elements
- Interior building spaces
- Window opening structures
- Portal access points
- Doorway entry locations
- Interior depth positioning
- Swarming window positions
- Prisoner containment areas
- Warrior search interior spaces
- Building interior architecture
- Access point configurations

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
