# Title
Environment Prompt

# ID
ENV001_environment_prompt

# Purpose
Generate a reusable environment reference at the project scope.

# Workflow Type
still.t2i.klein.distilled

# Positive Prompt
Describe the location, geometry, materials, lighting, and framing intent.

# Negative Prompt
List environment drift and style failures to avoid.

# Inputs
- project_id: project_template
- asset_scope: project
- asset_family: environments
- asset_id: ENV001

# Continuity Notes
- Keep this location stable for downstream scene and clip work.

# Repair Notes

# Sources
- projects/project_template/02_story_analysis/environment_breakdowns/
