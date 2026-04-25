import re

# Read the backup file
with open(r'c:\FilmCreator_MC\orchestrator\character_bible_backup.py', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update imports
content = content.replace(
    'from .character_bible_fallback import (\n    needs_visual_production_fallback,\n    deterministic_visual_fallback,\n)',
    'from .character_bible_fallback import (\n    needs_visual_production_fallback,\n    deterministic_visual_fallback,\n    visual_field_audit,\n    fallback_result_audit,\n)'
)

# 2. Add markdown writer function before _load_existing_metadata
markdown_func = '''

def _write_fallback_diagnostics_markdown(path: Path, diagnostics: list[dict[str, Any]], project_slug: str) -> None:
    lines = [
        f"# Character Bible Fallback Diagnostics",
        f"",
        f"**Project:** {project_slug}",
        f"**Total Records:** {len(diagnostics)}",
        f"**Attempted:** {sum(1 for item in diagnostics if item['fallback_attempted'])}",
        f"**Non-Empty:** {sum(1 for item in diagnostics if item['fallback_result_audit']['non_empty'])}",
        f"",
        f"| Character | Missing | Attempted | Bucket | Filled | Status | Preview |",
        f"|-----------|---------|-----------|--------|--------|--------|---------|",
    ]
    
    for item in diagnostics:
        char_id = item["character_id"]
        missing = item["pre_fallback_audit"]["missing_count"]
        total = item["pre_fallback_audit"]["total_prompt_critical_fields"]
        attempted = "yes" if item["fallback_attempted"] else "no"
        bucket = item["fallback_result_audit"].get("fallback_bucket") or "none"
        filled = item["fallback_result_audit"]["filled_count"]
        filled_total = filled + item["fallback_result_audit"]["empty_count"]
        status = item["fallback_result_audit"].get("status") or "none"
        preview = item["fallback_preview"].get("production_body_descriptor") or item["fallback_preview"].get("production_identity_descriptor") or ""
        preview = preview[:60] + "..." if len(preview) > 60 else preview
        
        lines.append(f"| {char_id} | {missing}/{total} | {attempted} | {bucket} | {filled}/{filled_total} | {status} | {preview} |")
    
    path.write_text("\\n".join(lines), encoding="utf-8")

'''

content = content.replace(
    '\ndef _load_existing_metadata(',
    markdown_func + '\ndef _load_existing_metadata('
)

# 3. Add fallback_diagnostics list
content = content.replace(
    '    bible_records: list[CharacterBible] = []\n    review_records: list[CharacterBible] = []',
    '    bible_records: list[CharacterBible] = []\n    review_records: list[CharacterBible] = []\n    fallback_diagnostics: list[dict[str, Any]] = []'
)

# 4. Add audit and diagnostics code after merged = _merge_with_existing
audit_code = '''

        # Audit visual fields before fallback
        pre_fallback_audit = visual_field_audit(merged)
        missing_fields = pre_fallback_audit["missing_fields"]

        print(
            f"[character-bible] {char_id} visual audit: "
            f"missing={pre_fallback_audit['missing_count']}/"
            f"{pre_fallback_audit['total_prompt_critical_fields']} "
            f"fields: {', '.join(missing_fields) if missing_fields else 'none'}"
        )

        fallback_attempted = False
        fallback_method = "none"
        fallback_reason = "not_needed"
        fallback = merged.get("visual_production_fallback") or {}

        if pre_fallback_audit["needs_visual_production_fallback"]:
            fallback_attempted = True
            fallback_method = "deterministic"
            fallback_reason = "missing_prompt_critical_fields"
            fallback = deterministic_visual_fallback(entry, merged, evidence_summary)
            merged["visual_production_fallback"] = fallback
        else:
            merged["visual_production_fallback"] = {}

        post_fallback_audit = fallback_result_audit(merged.get("visual_production_fallback") or {})

        print(
            f"[character-bible] {char_id} fallback: "
            f"attempted={'yes' if fallback_attempted else 'no'} "
            f"reason={fallback_reason} "
            f"bucket={post_fallback_audit.get('fallback_bucket') or 'none'} "
            f"method={fallback_method} "
            f"filled={post_fallback_audit['filled_count']}/"
            f"{post_fallback_audit['filled_count'] + post_fallback_audit['empty_count']} "
            f"status={post_fallback_audit.get('status') or 'none'}"
        )

        preview = ""
        if isinstance(fallback, dict):
            preview = str(
                fallback.get("production_body_descriptor")
                or fallback.get("production_identity_descriptor")
                or ""
            ).strip()
        if preview:
            print(f"[character-bible] {char_id} fallback preview: {preview[:180]}")

        fallback_diagnostics.append({
            "character_id": char_id,
            "display_name": merged.get("display_name"),
            "entity_kind": entry.get("entity_kind"),
            "first_seen_chapter": entry.get("first_seen_chapter"),
            "chapter_mentions": entry.get("chapter_mentions", []),
            "synthesis_mode": "reused" if existing and not force else "synthesized",
            "pre_fallback_audit": pre_fallback_audit,
            "fallback_attempted": fallback_attempted,
            "fallback_method": fallback_method,
            "fallback_reason": fallback_reason,
            "fallback_result_audit": post_fallback_audit,
            "fallback_preview": {
                "production_identity_descriptor": fallback.get("production_identity_descriptor") if isinstance(fallback, dict) else "",
                "production_body_descriptor": fallback.get("production_body_descriptor") if isinstance(fallback, dict) else "",
                "production_costume_descriptor": fallback.get("production_costume_descriptor") if isinstance(fallback, dict) else "",
                "production_silhouette": fallback.get("production_silhouette") if isinstance(fallback, dict) else "",
            },
            "evidence_summary": evidence_summary[:5],
        })
'''

content = content.replace(
    '        merged = _merge_with_existing(synthesized_payload, existing, metadata)\n\n        metadata.upstream_dependencies',
    '        merged = _merge_with_existing(synthesized_payload, existing, metadata)' + audit_code + '\n\n        metadata.upstream_dependencies'
)

# 5. Update CharacterBible construction to include visual_production_fallback
content = content.replace(
    '            evidence_refs=evidence_refs,\n            evidence_summary=evidence_summary,\n            metadata=metadata,\n        )\n        \n        # Generate visual production fallback if canon evidence is thin\n        if needs_visual_production_fallback(merged):\n            bible.visual_production_fallback = deterministic_visual_fallback(entry, merged, evidence_summary)',
    '            evidence_refs=evidence_refs,\n            evidence_summary=evidence_summary,\n            visual_production_fallback=merged.get("visual_production_fallback", {}),\n            metadata=metadata,\n        )'
)

# 6. Add diagnostics write code
diag_write = '''    
    # Write fallback diagnostics
    diagnostics_path = review_dir / "CHARACTER_BIBLE_FALLBACK_DIAGNOSTICS.json"
    write_json(diagnostics_path, {
        "project_slug": project_slug,
        "generated_at_utc": _utc_now(),
        "total_records": len(fallback_diagnostics),
        "attempted_count": sum(1 for item in fallback_diagnostics if item["fallback_attempted"]),
        "non_empty_count": sum(1 for item in fallback_diagnostics if item["fallback_result_audit"]["non_empty"]),
        "records": fallback_diagnostics,
    })
    written_files.append(str(diagnostics_path))
    
    # Write fallback diagnostics markdown
    _write_fallback_diagnostics_markdown(review_dir / "CHARACTER_BIBLE_FALLBACK_DIAGNOSTICS.md", fallback_diagnostics, project_slug)
    written_files.append(str(review_dir / "CHARACTER_BIBLE_FALLBACK_DIAGNOSTICS.md"))
    
'''

content = content.replace(
    '    write_json(review_dir / "CHARACTER_BIBLE_REVIEW_QUEUE.json", review_queue)\n    write_character_review_queue_markdown(review_dir / "CHARACTER_BIBLE_REVIEW_QUEUE.md", review_queue)\n    main_records',
    '    write_json(review_dir / "CHARACTER_BIBLE_REVIEW_QUEUE.json", review_queue)\n    write_character_review_queue_markdown(review_dir / "CHARACTER_BIBLE_REVIEW_QUEUE.md", review_queue)\n' + diag_write + '    main_records'
)

# Write the updated file
with open(r'c:\FilmCreator_MC\orchestrator\character_bible.py', 'w', encoding='utf-8') as f:
    f.write(content)

print("File updated successfully")
