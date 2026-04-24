from __future__ import annotations

from .models import CliSummary
from ..character_references import run_character_reference_planning, run_character_reference_generation
from ..environment_references import run_environment_reference_planning, run_environment_reference_generation


def plan_all_references(project_slug: str) -> CliSummary:
    characters = run_character_reference_planning(project_slug)
    environments = run_environment_reference_planning(project_slug)
    return CliSummary(command="plan-references", project_slug=project_slug, message="Reference planning complete.", data={"characters": characters.to_dict(), "environments": environments.to_dict()})


def generate_master_references(project_slug: str) -> CliSummary:
    characters = run_character_reference_generation(project_slug, variants=["full_body_neutral"])
    environments = run_environment_reference_generation(project_slug, variants=["establishing_wide"])
    return CliSummary(command="generate-master-references", project_slug=project_slug, message="Prepared master reference generation.", data={"characters": characters.to_dict(), "environments": environments.to_dict()})
