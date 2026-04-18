# Title
open_plaza Environment Reference Prompt

# ID
open_plaza_ref_prompt

# Purpose
Secondary transit destination environment for prisoner movement and fleet arrival context. Open plaza space at valley floor level serving as transition zone between exterior ground and city interior. Ground space positioned in front of building structures with clear daylight visibility conditions. Entrance point functions as architectural anchor for dragging action sequences and character observation from elevated positions.

# Workflow Type
still.t2i.klein.distilled

# Positive Prompt
Open ground plaza at valley floor, building entrance with prisoner being dragged, open daylight on plaza surface, transition space between fleet and city interior, ground level space allowing dragging action, clear visibility conditions, ambient lighting without weather effects, exterior ground positioned in front of city buildings, architectural transition point to interior spaces.

# Negative Prompt
character names, proper nouns, specific weather conditions, rain or snow effects, night time, indoor scenes, close-up character faces, dialogue bubbles, text overlays, branded logos, fictional location names, mountain peaks, water features, vegetation growth, ornate decorations, dramatic shadows.

# Inputs
- Project: princess_of_mars_test
- Asset: open_plaza
- Environment Role: Secondary / Retreat Destination (Transit Setting)
- Architecture or Geography: Open ground/plaza at valley floor level. Ground space in front of city buildings. Entrance to building where prisoner is dragged.
- Lighting and Atmosphere Cues: Open daylight conditions. Clear visibility for Carter's observation from window/balcony. No specific weather effects noted, standard ambient lighting.
- Scale Cues and Recurring Environmental Anchors: Ground level space allowing dragging action. Building entrance serves as transition point to interior. Open space allows fleet arrival context.
- Descriptive Noun Phrases for Render-Facing Prompts: Open ground plaza at valley floor, building entrance with prisoner being dragged, open daylight on plaza surface, transition space between fleet and city interior.

# Continuity Notes
- Maintain consistent valley floor elevation across all plaza scenes. Keep daylight conditions uniform without introducing weather variations. Preserve architectural relationship between plaza ground and building entrances. Ensure dragging action sequences occur at same ground level height. Building entrance transition points must remain visible as anchor for character movement between exterior and interior spaces. Fleet arrival context should utilize open space without obstructing plaza visibility.

# Repair Notes
- Review prompt bodies to ensure no proper nouns slipped into positive_prompt section. Verify negative_prompt includes all mentioned weather effects that are not part of standard ambient lighting. Check that continuity notes reference specific architectural anchors consistently across scene variations. Confirm asset_id open_plaza is only used in inputs_markdown and not embedded in render-facing prompt text. Ensure scale cues maintain ground level consistency without introducing elevation changes that contradict valley floor positioning.

# Sources
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/open_plaza.md
