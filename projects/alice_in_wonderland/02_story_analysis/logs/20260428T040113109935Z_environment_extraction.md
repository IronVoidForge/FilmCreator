# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-28T04:01:13.110435+00:00
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
*   **Visual State:** Alice is giant (over nine feet tall). Her feet are distant and small from her perspective.
*   **Event:** Alice experiences a growth spurt/size shift, observing her feet as being far away. She contemplates the logistics of sending boots to her feet via carrier.
*   **Action:** Alice's head strikes the ceiling of the hall. She picks up a **small golden key**.
*   **Action:** Alice moves to the garden door. She lies on her side to peer through the keyhole into the garden, but she is too large to pass through.

**Location: The Hall (The Pool of Tears)**
*   **Visual State:** Alice begins crying profusely. A pool of salt water forms around her, approximately four inches deep, extending halfway down the hall.
*   **Character Entrance:** The **White Rabbit** enters, trotting hurriedly. He is dressed splendidly and carries **white kid gloves** and a **large fan**. He mutters about "the Duchess."
*   **Interaction:** Alice attempts to speak to the Rabbit. The Rabbit reacts violently, drops the **gloves** and the **fan**, and scurries away into the darkness.
*   **Action/Object Interaction:** Alice picks up the fan and gloves. She uses the fan to cool herself due to the heat in the hall.
*   **Character Internal State:** Alice undergoes an identity crisis, attempting to verify her identity through math (fails), geography (fails), and reciting poetry (the "Crocodile" poem). Her voice sounds hoarse/strange during recitation.
*   **Visual State/Transformation:** Alice notices she is wearing one of the Rabbit's white kid gloves. She measures herself against a table; she has shrunk to approximately two feet tall.
*   **Action/Object Interaction:** Alice realizes the **fan** is causing her to shrink. She drops it to stop the process.
*   **Event:** Alice runs to the garden door, but finds it shut. The **golden key** is back on the glass table.
*   **Visual State/Shift:** Alice slips and falls into the pool of tears. She is now submerged up to her chin in salt water.

**Location: The Pool (Submerged)**
*   **Character Entrance:** A **Mouse** enters the pool, splashing nearby.
*   **Interaction:** Alice attempts to communicate with the Mouse using formal/Latin-inspired address ("O Mouse"). 
*   **Action/Dialogue:** Alice speaks French ("Où est ma chatte?") to the Mouse. The Mouse reacts with fright and indignation.
*   **Conflict:** Alice tries to soothe the Mouse by talking about her cat, **Dinah**. This offends the Mouse, who declares a family hatred for "nasty, low, vulgar" cats.
*   **Conflict:** Alice attempts to pivot the conversation to dogs (a terrier). The Mouse becomes increasingly agitated and swims away.
*   **Resolution/Exit:** Alice calls the Mouse back. The Mouse agrees to tell its history once they reach the shore.
*   **Character Entrance (Mass):** A crowd of animals enters the pool: a **Duck**, a **Dodo**, a **Lory**, an **Eaglet**, and other creatures.
*   **Action:** Alice leads the group of animals swimming toward the shore to exit the pool.
````

## Raw Response
````text
[[FILMCREATOR_PACKET]]
[[SECTION environment_index_markdown]]
# Environment Index

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
A vast, cavernous interior hall featuring high ceilings and a glass table. Contains a specific "Garden Door" subzone with a keyhole perspective. The space is characterized by extreme scale shifts relative to the protagonist.

**Lighting and Atmosphere Cues:** 
Variable atmosphere; can feel claustrophobic when Alice is giant (head striking ceiling) or vast and empty when she is small. Heat is present, necessitating the use of a fan.

**Scale Cues and Recurring Environmental Anchors:** 
- The Glass Table (anchor for size measurement).
- The Garden Door (threshold to another zone).
- High ceilings/distant floor (when Alice is giant).
- Small keyhole view (when Alice is peering through the door).

**Descriptive Noun Phrases:** 
Cavernous hall, glass tabletop, garden door threshold, high-ceilinged corridor, heat-heavy air, oversized architecture.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: environment
asset_id: the_pool_of_tears
[[SECTION markdown]]
# The Pool of Tears

**Role:** Secondary setting / Submerged environment

**Architecture or Geography:** 
A large, shallow body of salt water formed on the floor of the hall. It extends halfway down the corridor and creates a semi-submerged aquatic zone.

**Lighting and Atmosphere Cues:** 
Liquid/aqueous atmosphere; shimmering salt water; splashing movement; sense of submersion and buoyancy.

**Scale Cues and Recurring Environmental Anchors:** 
- Four inches deep (initial state).
- Submerged chin-deep (Alice's state after shrinking).
- The Shore (the exit point for the animal procession).

**Descriptive Noun Phrases:** 
Salt water pool, shimmering liquid floor, submerged aquatic zone, rippling salt water, crowded animal swim.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]
[[/FILMCREATOR_PACKET]]
````
