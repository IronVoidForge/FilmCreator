from __future__ import annotations

from pathlib import Path
from .models import ArtifactStatus, CliSummary
from .stages import STAGES


def run_status(project_slug: str) -> CliSummary:
    root = Path('projects') / project_slug
    rows = []
    for stage in STAGES:
        probe = root / '03_prompt_packages' if stage.key == 'prompt_preparation' else root
        state = 'generated' if probe.exists() else 'missing'
        rows.append(ArtifactStatus(stage.phase, stage.artifact_family, state, str(probe)).to_dict())
    return CliSummary(command='status', project_slug=project_slug, data={'artifacts': rows})
