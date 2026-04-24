from __future__ import annotations

from .models import CliSummary
from .stages import STAGES, BY_KEY


def plan_rerun(project_slug: str, start_from: str) -> CliSummary:
    started = False
    steps = []
    for stage in STAGES:
        if stage.key == start_from:
            started = True
        if started:
            steps.append({
                'phase': stage.phase,
                'key': stage.key,
                'command': stage.command,
                'implemented': stage.implemented,
            })
    return CliSummary(command='rerun', project_slug=project_slug, data={'steps': steps})
