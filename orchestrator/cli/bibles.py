from __future__ import annotations

from ..character_bible import run_character_bible_synthesis
from ..environment_bible import run_environment_bible_synthesis
from .models import CliSummary


def refresh_bibles(project_slug: str, *, character_limit: int | None = None, environment_limit: int | None = None, use_llm: bool = True, force: bool = False) -> CliSummary:
    characters = run_character_bible_synthesis(project_slug, use_llm=use_llm, force=force, limit=character_limit)
    environments = run_environment_bible_synthesis(project_slug, use_llm=use_llm, force=force, limit=environment_limit)
    return CliSummary(
        command="refresh-bibles",
        project_slug=project_slug,
        message="Bible refresh complete.",
        data={
            "characters": characters.to_dict(),
            "environments": environments.to_dict(),
        },
    )
