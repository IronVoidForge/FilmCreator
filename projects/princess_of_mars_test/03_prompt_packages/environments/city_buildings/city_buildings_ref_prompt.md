# Title
city_buildings Environment Reference Prompt

# ID
city_buildings_ref_prompt

# Purpose
This environment prompt defines the urban building structures used in observation and action sequences, establishing vertical scale and atmospheric conditions for the plaza setting. The architecture supports multiple vertical levels with consistent daylight illumination and fire damage effects that maintain visibility of foreground-background relationships.

# Workflow Type
still.t2i.klein.distilled

# Positive Prompt
upper floor windows with daylight illumination, building facades facing open plaza area, interior spaces accessible from exterior levels, rooftop positions with firing stances, missile impact flames spurt from building surfaces, smoke accumulation from fire damage, valley visibility from upper levels indicating regional geography, vertical scale established through window-to-ground distances

# Negative Prompt
proper nouns, character names, specific brand identifiers, indoor lighting without daylight, dark interiors, closed windows, empty rooftops, no smoke or fire effects, flat perspective, lack of vertical scale, artificial lighting sources, obscured plaza visibility

# Inputs
- asset_id: city_buildings
- project_slug: princess_of_mars_test
- environment_role: Primary setting for observation and action sequences. Multiple vertical levels utilized throughout chapter.
- architecture_geography: Urban structures with upper floors, windows, and roofs; Building facades facing open plaza area; Interior spaces accessible from exterior levels; Rooftop positions for firing stances; Window openings serving as vantage points.
- lighting_atmosphere: Daylight conditions throughout primary sequences; Smoke accumulation from fire damage; Missile impact flames spurt from building surfaces; Fire-induced atmospheric disturbance visible from plaza.
- scale_anchors: Building height establishes vertical scale for air craft approach; Window-to-ground distance defines observation perspective; Rooftop elevation provides firing platform context; Plaza proximity creates foreground-background relationship; Valley visibility from upper levels indicates regional geography.

# Continuity Notes
- The building structures maintain consistent daylight illumination across all sequences without introducing artificial lighting sources. Smoke and fire effects are present but do not obscure the plaza area or valley visibility. Vertical scale is established through window-to-ground distances and rooftop elevations that remain constant throughout shots. The foreground-background relationship between plaza proximity and upper levels is preserved in every frame.

# Repair Notes
- Ensure proper nouns like "Green Martian" are replaced with descriptive terms such as "firing stances". Maintain daylight conditions without introducing artificial lighting sources. Keep smoke accumulation visible but not overwhelming to the plaza area. Preserve the plaza foreground-background relationship throughout all shots and ensure valley visibility remains constant as a regional anchor.

# Sources
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/city_buildings.md
