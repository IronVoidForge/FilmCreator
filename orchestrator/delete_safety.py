from __future__ import annotations

import shutil
from pathlib import Path


def find_project_root(target: Path) -> Path | None:
    resolved = target.resolve()
    if resolved.is_dir():
        candidates = [resolved, *resolved.parents]
    else:
        candidates = [*resolved.parents]
    for candidate in candidates:
        if candidate.parent.name == "projects":
            return candidate
    return None


def validate_project_relative_path(relative_path: str) -> str:
    normalized = relative_path.replace("\\", "/").strip().strip("/")
    if not normalized:
        raise ValueError("Deletion target cannot be empty.")
    relative = Path(normalized)
    if relative.is_absolute():
        raise ValueError(f"Deletion target must be project-relative, got absolute path: {relative_path}")
    if any(part in {"", ".", ".."} for part in relative.parts):
        raise ValueError(f"Deletion target contains unsafe path traversal: {relative_path}")
    return normalized


def resolve_project_target(*, project_root: Path, relative_path: str) -> Path:
    normalized = validate_project_relative_path(relative_path)
    target = (project_root.resolve() / Path(normalized)).resolve()
    ensure_within_project(project_root, target, allow_project_root=False)
    return target


def ensure_within_project(project_root: Path, target: Path, *, allow_project_root: bool = False) -> None:
    root = project_root.resolve()
    resolved_target = target.resolve()
    if resolved_target == root:
        if allow_project_root:
            return
        raise ValueError(f"Refusing to delete project root itself: {resolved_target}")
    if root not in resolved_target.parents:
        raise ValueError(f"Deletion target escapes project root: {resolved_target}")


def remove_path_within_project(
    target: Path,
    *,
    project_root: Path,
    missing_ok: bool = False,
) -> bool:
    resolved = target.resolve()
    ensure_within_project(project_root, resolved, allow_project_root=False)
    if not resolved.exists():
        return False if missing_ok else False
    if resolved.is_dir():
        shutil.rmtree(resolved)
    else:
        resolved.unlink()
    return True
