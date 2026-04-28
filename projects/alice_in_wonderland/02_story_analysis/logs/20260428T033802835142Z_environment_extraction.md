# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-28T03:38:02.835641+00:00
- task: environment_extraction

## System Prompt
````text
You are FilmCreator's chapter analysis engine.
Return only FilmCreator packets with the requested sections and records.
Do not wrap the packet in code fences unless explicitly requested.
Do not produce JSON-only responses.
If a packet asks for markdown sections, emit the section name on its own line and wrap the body in [[SECTION ...]] ... [[/SECTION]].
Do not put another [[SECTION ...]] tag inside a section body.
Copy every FILMCREATOR structural tag literally.
Do not rename, translate, partially rewrite, or decorate any PACKET, RECORD, or SECTION tag.
The only valid closing tags are [[/FILMCREATOR_PACKET]], [[/FILMCREATOR_RECORD]], and [[/SECTION]].
Keep the response deterministic and grounded in the supplied chapter text.
````

## User Prompt
````text
Project slug: alice_in_wonderland

Chapter id: CH006

Task: extract environment families into an environment index plus one Markdown file per environment family.

Packet contract:
- task: environment_extraction
- version: 1
- first line: [[FILMCREATOR_PACKET]]
- last line: [[/FILMCREATOR_PACKET]]
- required sections: environment_index_markdown
- record type environment: fields=asset_id sections=markdown



Literal tag rules:

- begin with [[FILMCREATOR_PACKET]] on its own line

- end with [[/FILMCREATOR_PACKET]] on its own line

- wrap each environment item in [[FILMCREATOR_RECORD]] ... [[/FILMCREATOR_RECORD]]

- use [[SECTION environment_index_markdown]] and [[SECTION markdown]] exactly as written

- do not echo this instruction block back as an example packet; return the actual packet only



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

**Location: The House Exterior / Woods**
- **Event:** A Fish-Footman (fish-like face, powdered curly hair) runs from the woods to a house and raps on the door.
- **Character Entrance:** A Frog-Footman (round face, large eyes, powdered curly hair) opens the door.
- **Interaction/Object:** The Fish-Footman presents a massive letter (size of a man) to the Frog-Footman; it is an invitation from the Queen for the Duchess to play croquet.
- **Visual Gag:** Both footmen bow low and their powdered curls become entangled.
- **Character Action:** Alice hides in the woods, laughing, then peeks out. The Fish-Footman exits; the Frog-Footman sits on the ground staring at the sky.
- **Interaction:** Alice knocks. The Frog-Footman refuses to help because he is on the same side of the door as her and the noise inside is too loud (howling, sneezing, crashing).
- **Visual/Sound Event:** A large plate skims out of the house, grazes the Frog-Footman's nose, and breaks against a tree. The Footman remains indifferent.
- **Decision:** Alice decides to enter the house despite the Footman's apathy.

**Location: The Kitchen (Interior)**
- **Environment/Atmosphere:** Thick smoke; heavy presence of pepper causing constant sneezing.
- **Character Entrances/Presence:** 
    - The Duchess: Sitting on a three-legged stool, nursing a baby.
    - The Cook: Leaning over a fire, stirring a large cauldron of soup.
    - The Cheshire Cat: Sitting on the hearth, grinning widely.
- **Interaction:** Alice asks why the cat is grinning. The Duchess identifies it as a Cheshire Cat and shouts "Pig!" at the baby.
- **Conflict/Action:** The Cook begins throwing kitchen items (fire-irons, saucepans, plates, dishes) at the Duchess and the baby. 
- **Visual Continuity:** The Duchess remains unbothered by the projectiles; the baby is constantly howling and sneezing. A large saucepan nearly hits the baby's nose.
- **Dialogue/Decision:** Alice attempts to discuss the earth's rotation; the Duchess responds by ordering "Chop off her head!" 
- **Performance/Sound:** The Duchess sings a violent lullaby, shaking the baby at the end of every line. The Cook and Baby join in a chorus of "Wow! wow! wow!"
- **Character Exit/Transition:** The Duchess flings the baby at Alice and exits to play croquet; the Cook throws a frying pan at her (misses).

**Location: Exterior / Woods (Near the House)**
- **Object Interaction:** Alice catches the "starfish-shaped" baby. She learns to nurse it by twisting it into a knot, holding its right ear and left foot.
- **Transformation Event:** As Alice carries the baby outside, the creature's nose becomes a snout and eyes shrink. The baby grunts/sobs and transforms into a pig.
- **Character Action:** Alice sets the pig down; it trots into the woods.
- **Character Entrance:** The Cheshire Cat appears on a tree bough. 
- **Interaction/Dialogue:** Alice asks for directions. The Cat explains that everyone is mad (including Alice). The Cat uses its own behavior (growling when pleased, wagging tail when angry) to prove its madness.
- **Visual Effect:** The Cat mentions the croquet game and vanishes. It reappears, asks about the baby, and then vanishes slowly—starting with the tail and ending with a lingering grin.

**Location: March Hare's House (Exterior)**
- **Environment/Setting:** A large house with chimneys shaped like ears and a roof thatched with fur.
- **Character Action/Scale Shift:** Alice nibbles on a piece of mushroom to adjust her height to approximately two feet.
- **Decision:** Alice approaches the house timidly, feeling uncertain about visiting the March Hare versus the Hatter.
````

## Raw Response
````text
[[FILMCREATOR_PACKET]]
[[SECTION environment_index_markdown]]
- [woods_and_house_exterior](woods_and_house_exterior)
- [duchess_kitchen_interior](duchess_kitchen_interior)
- [march_hare_house_exterior](march_hare_house_exterior)
[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: woods_and_house_exterior
[[SECTION markdown]]
**Role:** Primary / Transit Setting
**Architecture or Geography:** Dense, shadowy woodland bordering a residential structure; large trees providing cover for hiding.
**Lighting and Atmosphere Cues:** Dappled sunlight through thick foliage; sense of voyeurism and concealment; chaotic soundscape (howling/crashing from the house).
**Scale Cues and Recurring Environmental Anchors:** Massive letters (man-sized); large breaking plates against tree trunks; low-angle perspective from Alice's hiding spot.
**Descriptive Noun Phrases:** Shadowy forest thicket, woodland edge, domestic threshold, broken ceramic shards, oversized stationery.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: duchess_kitchen_interior
[[SECTION markdown]]
**Role:** Primary Setting
**Architecture or Geography:** A cluttered, chaotic domestic kitchen; hearth with a large fireplace.
**Lighting and Atmosphere Cues:** Thick, heavy smoke; hazy atmosphere filled with floating pepper particles; oppressive and volatile energy.
**Scale Cues and Recurring Environmental Anchors:** Large bubbling cauldron; three-legged stool; flying projectiles (saucepans, fire-irons, plates); hearth/fireplace.
**Descriptive Noun Phrases:** Smoke-filled kitchen, pepper-heavy air, chaotic culinary workspace, soot-stained hearth, projectile-strewn floor.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: march_hare_house_exterior
[[SECTION markdown]]
**Role:** Secondary Setting
**Architecture or Geography:** Surrealist domestic architecture; whimsical and organic shapes.
**Lighting and Atmosphere Cues:** Dreamlike, slightly unsettling; bright but strange textures.
**Scale Cues and Recurring Environmental Anchors:** Chimneys shaped like ears; thatched roof made of fur; Alice's scale-shifting height (approx. two feet).
**Descriptive Noun Phrases:** Ear-shaped chimneys, fur-thatched roof, surrealist cottage, anthropomorphic architecture.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]
[[/FILMCREATOR_PACKET]]
````
