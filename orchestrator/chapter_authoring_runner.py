from __future__ import annotations

import json

from .story_authoring import author_chapter, build_chapter_continuity


def run_full_chapter_authoring(*, project_slug: str, chapter: str) -> dict[str, object]:
    summary = author_chapter(project_slug=project_slug, chapter=chapter)
    continuity = build_chapter_continuity(project_slug=project_slug, analysis=summary.analysis)
    return {
        "analysis": summary.analysis.to_dict(),
        "continuity": continuity.to_dict(),
        "scene_runs": [scene_run.to_dict() for scene_run in summary.scene_runs],
        "shared_prompts": summary.shared_prompts.to_dict(),
    }


if __name__ == "__main__":
    payload = run_full_chapter_authoring(
        project_slug="princess_of_mars_test",
        chapter="CH008_a_princess_of_mars_ch08.md",
    )
    print(json.dumps(payload, indent=2))
