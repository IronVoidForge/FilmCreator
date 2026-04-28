# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-28T03:00:58.460633+00:00
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

Chapter id: CH002

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

**Location: The Hall / The Garden Door Subzone**
*   **Event:** Alice experiences rapid growth, reaching over nine feet in height. Her head strikes the ceiling of the hall.
*   **Character State:** Alice is disoriented and struggling to speak coherent English.
*   **Object Interaction:** Alice picks up a small golden key.
*   **Action/Movement:** Alice moves toward the garden door but finds it impossible to peer through due to her size. She sits down and begins to cry.
*   **Visual Continuity/Environment Shift:** Alice's crying creates a large pool of salt water, approximately four inches deep, spreading halfway down the hall.

**Location: The Hall (Near the Pool)**
*   **Character Entrance:** The White Rabbit enters, trotting hurriedly. He is dressed splendidly and carries white kid gloves and a large fan.
*   **Dialogue/Action:** The White Rabbit mutters about "the Duchess." Alice attempts to speak to him; the Rabbit reacts violently, drops the gloves and the fan, and flees into the darkness.
*   **Object Interaction:** Alice picks up the fan and the white kid gloves.
*   **Character State/Internal Monologue:** Alice experiences an identity crisis, questioning if she has been transformed into another child (Mabel or Ada). She attempts to verify her identity through math (multiplication tables), geography (capitals of Europe), and reciting poetry ("How doth the little crocodile"), but fails all tests.
*   **Visual Continuity/Transformation:** Alice notices she is wearing one of the Rabbit's white kid gloves. She measures herself against a table and finds she has shrunk to approximately two feet tall.
*   **Action/Decision:** Alice realizes the fan causes her to shrink; she drops it to prevent shrinking away entirely.
*   **Movement/Failure:** Alice runs toward the garden door, but finds it shut. The golden key is back on the glass table.

**Location: The Pool of Tears**
*   **Event/Action:** Alice slips and falls into the pool of salt water, which now reaches up to her chin.
*   **Character State:** Alice believes she might be drowning in her own tears.
*   **Character Entrance:** A Mouse enters the pool, swimming nearby.
*   **Interaction (Alice & Mouse):** 
    *   Alice attempts to communicate with the Mouse using formal "O Mouse" address and then French ("Où est ma chatte?").
    *   The Mouse reacts with fright/agitation at the mention of cats.
    *   Alice attempts to soothe the Mouse by describing her cat, Dinah, which causes the Mouse to bristle and become offended.
    *   Alice attempts to change the subject to dogs (a terrier), which causes the Mouse to swim away in a commotion.
    *   Alice calls the Mouse back, promising not to mention cats or dogs.
*   **Dialogue/Reveal:** The Mouse agrees to return and proposes they go to the shore so he can explain his history regarding cats and dogs.
*   **Character Entrances (Crowd):** As the pool becomes crowded, several animals emerge: a Duck, a Dodo, a Lory, and an Eaglet.
*   **Movement/Exit:** Alice leads the group of animals/birds out of the water toward the shore.
````

## Raw Response
````text
[[FILMCREATOR_PACKET]]
task: environment_extraction
version: 1

[[SECTION environment_index_markdown]]
# Environment Index - Chapter CH002

- [the_hall](#the_hall)
- [the_pool_of_tears](#the_pool_of_tears)
[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: the_hall
[[SECTION markdown]]
# The Hall

**Role:** Primary setting / Transit setting

**Architecture or Geography:** 
A vast, enclosed interior space characterized by high ceilings and long corridors. Features include a glass-topped table and a garden door that serves as a threshold to another zone. The scale of the room shifts dramatically based on Alice's physical size.

**Lighting and Atmosphere Cues:** 
Varies from bright/open to pockets of deep darkness where characters (like the White Rabbit) flee. The atmosphere is one of disorientation and surreal spatial distortion.

**Scale Cues and Recurring Environmental Anchors:** 
- High ceilings (striking Alice when she is giant).
- A glass table holding a small golden key.
- A garden door acting as a focal point for movement.
- Drastic scale shifts: from nine feet tall to two feet tall.

**Descriptive Noun Phrases:** 
vast hall, high-ceilinged corridor, glass-topped table, miniature garden door, looming architecture, shifting proportions, dark recesses.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: the_pool_of_tears
[[SECTION markdown]]
# The Pool of Tears

**Role:** Secondary setting / Interaction zone

**Architecture or Geography:** 
A large, spreading expanse of salt water covering the floor of the hall. It is a shallow but wide body of liquid that creates a temporary aquatic environment within the larger structure.

**Lighting and Atmosphere Cues:** 
Reflective, shimmering surface; sense of drowning/submersion; chaotic movement from swimming animals.

**Scale Cues and Recurring Environmental Anchors:** 
- Four inches deep initially, rising to chin-height for Alice.
- Spreads halfway down the hall.
- A shoreline where land meets the salt water.

**Descriptive Noun Phrases:** 
salt water expanse, shimmering pool, shallow sea of tears, aquatic floor, rippling surface, crowded shoreline.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
