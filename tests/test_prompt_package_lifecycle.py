from pathlib import Path

from orchestrator.artifact_lifecycle import metadata_sidecar_path, read_artifact_sidecar, write_artifact_with_metadata
from orchestrator.prompt_package import PromptPackage, parse_prompt_package, write_prompt_package
from orchestrator.prompt_preparation import _write_prompt_package_if_changed_with_metadata


def _make_package(path: Path, *, positive_prompt: str, prompt_id: str = "hero_prompt") -> PromptPackage:
    return PromptPackage(
        path=path,
        title="Hero Prompt",
        prompt_id=prompt_id,
        purpose="Prompt lifecycle validation",
        workflow_type="still.t2i.klein.distilled",
        positive_prompt=positive_prompt,
        negative_prompt="blurry",
        inputs_markdown="\n".join(
            [
                "- subject_kind: character",
                "- subject_id: hero",
                "- source_artifact_ids: source_a",
                "- reference_mode: canonical_reference_generation",
                "- variant_name: bust_portrait",
                "- reuse_policy: reuse canonical visual canon",
            ]
        ),
        continuity_notes_markdown="- preserve continuity",
        sources_markdown="- source_a.json",
    )


def test_prompt_package_write_creates_metadata_sidecar(tmp_path: Path) -> None:
    path = tmp_path / "hero_prompt.md"
    package = _make_package(path, positive_prompt="cinematic portrait reference")

    wrote = _write_prompt_package_if_changed_with_metadata(path, package, force=False, source_fingerprint="fp1")

    assert wrote is True
    sidecar = read_artifact_sidecar(path)
    assert sidecar is not None
    assert metadata_sidecar_path(path).exists()
    assert sidecar["artifact_type"] == "prompt_package"
    assert sidecar["metadata"]["status"] == "generated"
    assert sidecar["metadata"]["source_fingerprint"] == "fp1"


def test_locked_prompt_package_survives_normal_rerun(tmp_path: Path) -> None:
    path = tmp_path / "hero_prompt.md"
    original = _make_package(path, positive_prompt="cinematic portrait reference")
    write_prompt_package(path, original)
    write_artifact_with_metadata(
        metadata_sidecar_path(path),
        {
            "artifact_id": original.prompt_id,
            "path": str(path),
            "prompt_id": original.prompt_id,
            "title": original.title,
            "workflow_type": original.workflow_type,
        },
        artifact_type="prompt_package",
        status="locked",
        source_fingerprint="fp_locked",
        locked_fields={"__artifact__": True},
    )

    changed = _make_package(path, positive_prompt="new rewritten prompt that should not replace the locked one")
    wrote = _write_prompt_package_if_changed_with_metadata(path, changed, force=False, source_fingerprint="fp_new")

    assert wrote is False
    parsed = parse_prompt_package(path)
    assert parsed.positive_prompt == "cinematic portrait reference"
    sidecar = read_artifact_sidecar(path)
    assert sidecar is not None
    assert sidecar["metadata"]["status"] == "stale"
