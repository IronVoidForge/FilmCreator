from __future__ import annotations


def extract_manifest_candidate_paths(manifest: dict[str, object]) -> list[str]:
    batch = manifest.get("batch", {})
    if isinstance(batch, dict):
        candidate_entries = batch.get("candidates", [])
        if isinstance(candidate_entries, list):
            paths: list[str] = []
            for entry in candidate_entries:
                if not isinstance(entry, dict):
                    continue
                output_files = entry.get("output_files", [])
                if isinstance(output_files, list):
                    for path in output_files:
                        if isinstance(path, str) and path:
                            paths.append(path)
            if paths:
                return paths

    output_files = manifest.get("output_files", [])
    if isinstance(output_files, list):
        return [path for path in output_files if isinstance(path, str) and path]
    return []
