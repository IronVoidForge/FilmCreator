from __future__ import annotations

from .models import CliSummary


def run_quick_test(project_slug: str) -> CliSummary:
    steps = [
        'clear downstream artifacts',
        'optional bible refresh',
        'scene contracts',
        'scene bindings',
        'shot packages',
        'dialogue timeline',
        'descriptor enrichment',
        'prompt preparation',
        'quality grading',
    ]
    return CliSummary(command='test-pipeline', project_slug=project_slug, message='Quick-test plan prepared', data={'steps': steps})
