# Title
city_plaza_exterior Environment Reference Prompt

# ID
city_plaza_exterior_ref_prompt

# Purpose
Shared reference prompt for generating consistent city plaza exterior scenes across the project. Defines architectural scale, lighting conditions, atmospheric states, and environmental anchors to maintain visual continuity during regeneration cycles. Supports both bustling procession and post-battle deserted states while preserving structural integrity of multi-story buildings and paved surfaces.

# Workflow Type
still.t2i.klein.distilled

# Positive Prompt
Multi-story urban buildings with doorways and windows. Paved plaza ground surface with street pathways. Bright sunlight illumination casting distinct shadows on building facades. Dim interior spaces visible through window openings. Towering architectural structures above plaza level. Building portals at ground floor entrances. Smoke rising from distant burning ship location. Urban geography with vertical scale emphasis. Recurring environmental anchors at doorways and upper windows.

# Negative Prompt
Blurry or indistinct building details. Dark interior spaces without window visibility. Overexposed sunlight losing shadow definition. Missing paved plaza surface texture. Inconsistent architectural scale between buildings. Absent structural doorways or windows. Floating smoke without ground connection. Improper urban geography alignment. Missing environmental anchor points at portals and upper floors.

# Inputs
- Project path: projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/city_plaza_exterior.md
- Asset identifier: city_plaza_exterior
- Environment breakdown location: 02_story_analysis folder structure
- Regeneration context: Shared environment-reference prompt draft for stable local generation

# Continuity Notes
- Maintain multi-story building architecture consistency across all regeneration cycles. Preserve paved plaza surface texture and lighting shadow patterns. Keep environmental anchors at doorways and upper windows visible in every generated scene. Match atmospheric states between bustling procession and post-battle deserted conditions while preserving structural integrity. Ensure smoke from burning ship remains distant anchor point without dominating foreground composition.

# Repair Notes
- If regeneration produces inconsistent building scale, adjust architectural height parameters to match multi-story urban structures. When shadow definition is lost in bright sunlight, recalibrate lighting intensity to preserve distinct shadow patterns on building facades. If environmental anchors become obscured, increase visibility of doorways and upper windows through window openings. For atmospheric state transitions between bustling and deserted conditions, maintain structural continuity while adjusting smoke density and crowd presence levels.

# Sources
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/city_plaza_exterior.md
