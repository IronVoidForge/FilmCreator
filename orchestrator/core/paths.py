from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
PROJECTS_ROOT = ROOT / "projects"
REGISTRY_PATH = ROOT / "orchestrator" / "registry" / "workflow_registry.json"
TEMPLATES_ROOT = ROOT / "orchestrator" / "templates"


def ensure_dir(path: Path) -> Path:
    path.mkdir(parents=True, exist_ok=True)
    return path


def repo_relative(path: Path) -> str:
    try:
        from .. import common as common_module
    except Exception:  # pragma: no cover - fallback for import bootstrap
        common_module = None

    root = getattr(common_module, "ROOT", ROOT) if common_module is not None else ROOT
    return path.resolve().relative_to(root).as_posix()


def character_taxonomy_dir(project_dir: Path) -> Path:
    """Return the character taxonomy directory path."""
    return project_dir / "02_story_analysis" / "taxonomy" / "characters"


def character_taxonomy_path(project_dir: Path, character_id: str) -> Path:
    """Return the taxonomy file path for a specific character."""
    return character_taxonomy_dir(project_dir) / f"CHAR_{character_id}_TAXONOMY.json"


def character_taxonomy_index_path(project_dir: Path) -> Path:
    """Return the character taxonomy index file path."""
    return character_taxonomy_dir(project_dir) / "CHARACTER_TAXONOMY_INDEX.json"


def character_taxonomy_review_dir(project_dir: Path) -> Path:
    """Return the character taxonomy review directory path."""
    return project_dir / "02_story_analysis" / "taxonomy" / "review"
