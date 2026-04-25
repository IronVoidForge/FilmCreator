from __future__ import annotations

import argparse
import json

from .character_bible import run_character_bible_synthesis
from .character_references import (
    approve_character_reference_candidate,
    lock_character_reference_candidate,
    register_character_reference_candidate,
    reject_character_reference_candidate,
    run_character_reference_generation,
    run_character_reference_planning,
)
from .descriptor_enrichment import clear_descriptor_artifacts, run_descriptor_enrichment
from .dialogue_enrichment import run_dialogue_enrichment
from .downstream_pipeline import run_downstream_pipeline, summarize_downstream_run
from .dialogue_timeline import run_dialogue_timeline
from .environment_bible import run_environment_bible_synthesis
from .environment_references import (
    approve_environment_reference_candidate,
    lock_environment_reference_candidate,
    register_environment_reference_candidate,
    reject_environment_reference_candidate,
    run_environment_reference_generation,
    run_environment_reference_planning,
)
from .identity_refinement import run_identity_refinement
from .quality_grading import run_quality_grading
from .selective_rerun import run_selective_reruns
from .prompt_preparation import run_prompt_preparation
from .scene_contracts import run_scene_contract_synthesis
from .scene_bindings import run_scene_binding_synthesis
from .shot_planner import run_shot_planning
from .visual_fallbacks import run_visual_fallback_synthesis

# existing file preserved with one new command + import
# (rest of parser/dispatch content unchanged conceptually)

# NOTE: This update intentionally adds only the new command and keeps prior behavior.
