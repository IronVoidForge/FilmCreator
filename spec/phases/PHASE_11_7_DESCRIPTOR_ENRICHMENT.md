# Phase 11.7 - Descriptor Enrichment and Reference Coverage

## Goal

Turn canonical entities into structured, evidence-grounded descriptor profiles so later prompt preparation can reuse stable visual and scene detail without repeatedly asking the LLM to rediscover it.

---

## Why This Phase Exists

The project already has:

- chapter extraction
- character and environment bibles
- scene contracts
- shot packages
- prompt-preparation bundles
- dialogue timelines
- key-item planning

What is still missing is a structured enrichment layer that captures:

- what the book explicitly states
- what the evidence strongly implies
- what remains unknown
- where each fact was seen
- how confident the system is in each field

This phase is the place to fill in the fields that should not be repeatedly requested earlier, while keeping earlier phases narrow and low-friction.

---

## Design Principle

Earlier phases should not ask for every final visual detail.

Instead:

- extraction should capture explicit mentions, chapter references, and minimum usable visible facts
- synthesis should build canonical bibles from those facts
- this phase should enrich those bibles with structured descriptors and confidence
- prompt preparation should consume the structured descriptors rather than re-parsing prose summaries

This keeps the pipeline from asking the LLM the same thing multiple times.

---

## Inputs

- chapter extraction outputs
- book index and paragraph windows
- character bibles
- environment bibles
- scene contracts
- shot packages
- key-item registry entries when available
- continuity notes and review queues
- librarian retrieval helpers

---

## Outputs

- structured character descriptor profiles
- structured environment descriptor profiles
- structured scene descriptor profiles
- structured key-item descriptor profiles
- reference coverage maps
- field-level confidence and provenance records
- review queues for thin or uncertain fields

---

## Descriptor Coverage Rules

Every enriched record should separate:

- explicit facts from the source
- strong inferences from context
- unresolved gaps

Every enriched record should carry:

- where the fact came from
- which chapter or scene mentioned it
- whether the field is explicit or inferred
- confidence or review state

---

## Image Generation Descriptor Schema

This is the shared schema family the later prompt-prep and reference-sheet phases should consume.

The goal is not to hardcode one giant prompt string. The goal is to capture the stable visual facts a model needs so prompts can be assembled from structured parts.

### Shared Descriptor Primitives

Every entity type can use these primitives where relevant:

- identity
- scale
- shape
- materials
- surface finish
- color palette
- texture
- lighting response
- spatial context
- motion or pose state
- camera relationship
- continuity locks
- symbolic or functional role
- provenance
- confidence
- review state

### ComfyUI-Oriented Prompt Assembly Rules

- keep the descriptor output structured
- keep the final prompt compact
- let prompt enhancers expand the compact prompt later
- avoid repeating the same fact in multiple prompt fields
- avoid proper nouns in the prompt body unless text must appear on screen
- keep camera, composition, and continuity separate from identity traits
- keep negative constraints separate from positive descriptors
- keep source metadata separate from render-facing prompt text

### What Should Be Asked Earlier Versus Later

Earlier phases should ask for:

- explicit names
- chapter mentions
- basic presence vs reference status
- obvious visible facts
- unresolved ambiguity notes

This phase should ask for or infer:

- normalized sex
- age range
- height
- body type
- skin tone
- hair and eye details
- face shape
- costume structure
- environment layout and anchors
- item construction and visual identity
- scene-level action and camera intent

This phase should not re-ask:

- whether the thing exists
- which chapter it was in
- which alias was mentioned
- whether the entity is canonical or provisional
- whether the source is uncertain

---

## Descriptor Record Contract

Every descriptor record should follow the same high-level shape:

- canonical_id
- display_name
- entity_type
- status
- field_values
- field_sources
- field_confidence
- field_origin
- review_flags
- chapter_mentions
- scene_mentions
- shot_mentions
- evidence_refs
- inferred_fields

### Field Value Style

Each field should be stored as one of:

- a short scalar string
- a short controlled list of strings
- a structured object when subfields matter

Avoid large prose blobs inside the descriptor itself.

### Field State

Every field should be marked as one of:

- explicit
- inferred
- review_needed
- unknown

### Confidence Style

Use a simple confidence scale:

- high
- medium
- low

If a field is unknown, do not invent it just to complete the record.

---

## Character Descriptor Fields

The character layer should be structured enough that later prompt generation can reuse it directly.

### Core Identity

- canonical_id
- display_name
- aliases
- sex
- age_range
- role
- entity_kind

### Visual Structure

- height
- build
- skin_tone
- hair_color
- hair_style
- eye_color
- face_shape
- facial_hair
- distinctive_features

### Character Field Contract

- sex: explicit biological or textual sex when supported, otherwise unknown
- age_range: broad visual age band, not exact age unless clearly stated
- height: relative height class or approximate height if the source supports it
- build: body type and mass distribution
- skin_tone: visible or inferred skin tone only when supportable
- hair_color: visible hair color or canonical equivalent
- hair_style: shape, length, arrangement, or grooming
- eye_color: visible eye color when known
- face_shape: overall facial geometry
- facial_hair: beard, mustache, stubble, or none
- distinctive_features: scars, markings, missing parts, unusual anatomy, or iconic identifiers
- costume_layers: visible clothing or armor layers in canonical order
- costume_materials: cloth, leather, metal, fur, hide, scale, or other materials
- costume_signature: the short stable costume phrase that should survive across prompts
- silhouette_notes: shape language useful for rendering and angle consistency
- recurring_accessories: weapons, jewelry, bags, masks, wraps, tools, or other repeatable accessories
- posture: default posture or stance
- expression_tendency: most common readable expression or emotional posture
- physical_presence_notes: how the character reads physically in a frame
- voice_or_presence_notes: if the source gives a stable conversational or presence cue

### Character Prompt-Use Notes

- Use sex, age_range, height, build, skin_tone, hair_color, hair_style, and eye_color when known.
- Use costume_signature, silhouette_notes, and recurring_accessories to stabilize recurring generation.
- If the character lacks physical detail, the descriptor should clearly show the gap instead of inventing a full body description.

### Costume and Silhouette

- costume_layers
- costume_materials
- costume_signature
- silhouette_notes
- recurring_accessories

### Behavioral / Readable Cues

- posture
- expression_tendency
- physical_presence_notes
- voice_or_presence_notes

### Optional Character Image-Gen Detail Fields

These fields are especially useful for consistent image generation and should be added when evidence supports them:

- gender presentation only if clearly needed for the visual concept
- age band
- body fat / muscularity / frame
- limb proportions
- hand shape
- gait or stance
- facial symmetry
- brow shape
- nose shape
- lip shape
- jaw shape
- beard or facial marking details
- scars or tattoos
- jewelry or adornment
- weapon or tool carry style
- cloth drape behavior
- dominant pose tendencies
- expression range
- texture notes for skin, hair, armor, cloth, fur, scale, or feathers

### Provenance

- chapter_mentions
- scene_mentions
- shot_mentions
- evidence_refs
- source_confidence
- inferred_fields

### Review Flags

- unresolved_visual_gaps
- low_confidence_fields
- manual_followup_required

Note:

- use `sex` as the structural field here
- do not force `presentation` as a separate default field unless later evidence explicitly warrants it

---

## Environment Descriptor Fields

### Core Identity

- canonical_id
- display_name
- environment_type
- entity_kind

### Spatial Structure

- layout
- scale
- geography
- architecture
- pathways
- camera_friendly_landmarks

### Visual Atmosphere

- materials
- lighting
- mood
- weather_or_atmosphere
- recurring_anchors

### Environment Field Contract

- environment_type: canonical setting class such as interior, exterior, transit, chamber, city, wilderness, or another stable class
- layout: the practical spatial arrangement of the place
- scale: relative size and spatial scale
- geography: terrain, structure, or physical setting type
- architecture: built form, if any
- pathways: routes, corridors, openings, stairways, passages, or movement channels
- camera_friendly_landmarks: strong framing anchors the camera can repeatedly find
- materials: stone, metal, wood, fabric, sand, dust, water, or other recurring materials
- lighting: stable lighting language or most common illumination state
- mood: emotional or atmospheric feel
- weather_or_atmosphere: mist, heat, dust, wind, humidity, dry air, etc.
- recurring_anchors: recurring visual anchors that keep the environment canonical

### Environment Prompt-Use Notes

- Use layout, scale, geography, architecture, and landmarks to preserve consistent camera placement.
- Use materials and recurring anchors to keep the environment visually distinct.
- If the source only gives atmosphere, the descriptor should mark layout as thin rather than inventing a floor plan.

### Optional Environment Image-Gen Detail Fields

- architecture style
- structural geometry
- room shape or terrain shape
- floor, wall, and ceiling surfaces
- doorway, arch, stair, path, or corridor layout
- foreground / midground / background anchors
- scale cues
- depth cues
- reflective or matte behavior
- dust, haze, mist, smoke, rain, or wind
- flora or fauna if recurring
- signs, banners, carvings, or props if recurring
- daylight, torchlight, ambient glow, or shadow logic

### Provenance

- chapter_mentions
- scene_mentions
- evidence_refs
- source_confidence
- inferred_fields

### Review Flags

- unresolved_layout_gaps
- low_confidence_fields
- manual_followup_required

---

## Scene Descriptor Fields

Scene descriptors should support shot planning and prompt bundling without re-reading the whole scene contract every time.

### Core Identity

- canonical_id
- chapter_id
- scene_id
- scene_title

### Action Structure

- action_summary
- emotional_beat
- participants
- key_items
- location_requirements
- camera_intent

### Continuity / Sequencing

- start_state
- end_state
- movement_notes
- transition_notes
- dialogue_relevance

### Scene Field Contract

- action_summary: what physically happens in the scene
- emotional_beat: the emotional movement of the scene
- participants: characters who matter in the scene
- key_items: items that need continuity or visual emphasis
- location_requirements: what the scene requires from the environment
- camera_intent: broad framing or coverage intent
- start_state: state at scene entry
- end_state: state at scene exit
- movement_notes: motion, blocking, or repositioning that matters visually
- transition_notes: what changes between scenes
- dialogue_relevance: whether the scene carries dialogue that must bind to later clips

### Scene Prompt-Use Notes

- Use action_summary and emotional_beat to drive shot intent.
- Use location_requirements and camera_intent to help prompt preparation build shot variants.
- Keep participants and key_items tied to canonical asset ids when available.

---

## Shot Descriptor Fields

Shot descriptors should capture the exact framing and movement facts that matter for reference-sheet generation, keyframe generation, and later image-to-video work.

### Core Identity

- canonical_id
- chapter_id
- scene_id
- shot_id
- shot_title
- shot_type

### Camera Structure

- angle
- framing
- lens_family
- distance
- camera_height
- camera_motion
- zoom_behavior
- focus_target
- perspective_notes

### Subject Structure

- characters_in_frame
- primary_subject
- secondary_subjects
- subject_positions
- pose_notes
- gaze_direction
- interaction_notes

### Environment Structure

- environment_id
- environment_label
- spatial_continuity
- background_layers
- foreground_elements
- midground_elements
- depth_cues

### Continuity / Motion

- start_state
- end_state
- movement_notes
- continuity_constraints
- keyframe_intent
- image_to_image_intent

### Provenance

- scene_mentions
- chapter_mentions
- evidence_refs
- source_confidence
- inferred_fields

### Shot Prompt-Use Notes

- use shot_type, angle, framing, and motion to seed the prompt family
- keep the prompt compact, but do not omit the camera facts that define the shot
- keep character and environment descriptors tied to their canonical ids
- if a shot is missing a solid environment or subject descriptor, flag it for review instead of inventing a complete scene

### Optional Scene Image-Gen Detail Fields

- visual beat
- frame priority
- center of attention
- dominant motion
- offscreen pressure
- crowd density
- environmental change during the scene
- camera emphasis
- blocking cues
- prop handoff or reveal

### Provenance

- chapter_mentions
- shot_mentions
- evidence_refs
- source_confidence
- inferred_fields

---

## Key Item Descriptor Fields

Key items should become structured canonical assets, not just named props.

### Core Identity

- canonical_id
- display_name
- aliases
- item_kind

### Key Item Field Contract

- item_kind: sword, ring, armor set, emblem, relic, tool, device, weapon, or another stable canonical class
- shape: overall form and silhouette
- scale: size relative to a hand, body, room, or other known reference
- materials: visible construction materials
- color_palette: stable colors that matter for rendering
- ornamentation: decorative details, engravings, inlay, filigree, or iconic finishing
- condition_or_wear: pristine, used, damaged, aged, sacred, repaired, etc.
- holder_or_user_notes: who carries or uses it
- iconic_features: the few visual features that should survive all prompts
- symbolic_role: story meaning or canonical function

### Key Item Prompt-Use Notes

- If the item is story-significant, it should be treated like a real canonical visual asset.
- Keep the descriptor focused on the few features that must survive across angles and shots.
- If the item is too incidental, keep it out of the main index rather than forcing a full descriptor.

### Visual Structure

- shape
- scale
- materials
- color_palette
- ornamentation
- condition_or_wear

### Optional Key Item Image-Gen Detail Fields

- silhouette
- grip or wear pattern
- edge profile
- wear marks
- inscriptions or symbols
- gem, metal, stone, or cloth behavior
- mounted versus handheld behavior
- storage or presentation style
- whether it should read as ceremonial, practical, dangerous, sacred, or mundane

### Continuity

- chapter_mentions
- scene_mentions
- holder_or_user_notes
- iconic_features
- symbolic_role

### Provenance

- evidence_refs
- source_confidence
- inferred_fields

---

## Book Index and Reference Coverage

This phase should use the indexed book more aggressively than earlier synthesis phases.

It should:

- search the book index for the best matching chapters
- pull paragraph windows around each relevant mention
- attach those windows as evidence snippets
- record which chapters have already been used for each entity
- mark under-covered entities for review instead of silently repeating the same summary text

The goal is not to pass huge book context to the LLM.

The goal is to pass small, tagged, high-signal evidence slices and keep a reference coverage map so we know where the LLM has already been fed context.

Recommended evidence slice strategy:

- one chapter summary anchor
- one or two paragraph windows for the strongest mentions
- one compact canonical summary from the current bible
- one concise note for anything still unresolved

This is usually enough to improve the descriptor without bloating the prompt.

---

## What Should Be Deferred Until This Phase

These details should not be repeatedly demanded in extraction or first-pass synthesis when they are not clearly supported yet:

- full character trait expansion
- inferred sex when the text is ambiguous and the book does not state it plainly
- height and body type normalization
- hair and eye color normalization
- facial structure refinement
- costume material and layering synthesis
- environment layout normalization
- recurring anchor consolidation
- scene camera intent refinement
- item material and iconography consolidation

Earlier phases should log the mentions and gaps.

This phase should decide what can be inferred safely and what must remain unresolved.

---

## Artifact Locations

Likely locations:

- `02_story_analysis/descriptors/characters/<asset_id>.json`
- `02_story_analysis/descriptors/characters/<asset_id>.md`
- `02_story_analysis/descriptors/environments/<asset_id>.json`
- `02_story_analysis/descriptors/environments/<asset_id>.md`
- `02_story_analysis/descriptors/scenes/<scene_id>.json`
- `02_story_analysis/descriptors/scenes/<scene_id>.md`
- `02_story_analysis/descriptors/key_items/<item_id>.json`
- `02_story_analysis/descriptors/key_items/<item_id>.md`
- `02_story_analysis/descriptors/review/`

The prompt-preparation layer should consume these descriptors when available, but still fall back to the current bible fields so the pipeline stays additive.

---

## Implementation Files

Likely new orchestration layer:

- `orchestrator/descriptor_enrichment.py`
- `orchestrator/cli.py`

Potential supporting helpers:

- `orchestrator/book_librarian.py`
- `orchestrator/character_bible.py`
- `orchestrator/environment_bible.py`
- `orchestrator/prompt_preparation.py`
- `orchestrator/scene_contracts.py`
- `orchestrator/key_item_index.py`

Potential launcher:

- `launchers/authoring/run_phase11_7_descriptor_enrichment.bat`

---

## Acceptance Criteria

- canonical entities can be enriched with structured descriptor fields
- book index references and paragraph windows are attached as evidence
- low-confidence fields are routed to review instead of silently guessed
- prompt preparation can consume the enriched descriptors without bloating prompt text
- earlier extraction phases do not need to be rewritten to carry every final detail
- the system avoids repeated LLM rereview of the same entity facts

---

## Status

- `planned`
- evidence: the pipeline already has canonical bibles, scene contracts, shot packages, prompt preparation, and book-index retrieval, so this is the right place to add structured descriptor enrichment without restarting the whole architecture
