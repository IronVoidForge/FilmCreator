"""
Overnight pipeline resume validator.
Checks which stages are complete and returns the first incomplete stage.
"""
import json
import sys
from pathlib import Path
from typing import Optional


def count_source_chapters(project_root: Path) -> int:
    """Count source chapter files."""
    chapters_dir = project_root / "01_source" / "chapters"
    if not chapters_dir.exists():
        return 0
    return len(list(chapters_dir.glob("CH*.md")))


def check_story_analysis(project_root: Path) -> bool:
    """Check if story analysis is complete."""
    analysis_dir = project_root / "02_story_analysis"
    
    # Check chapter summaries
    chapter_analysis_dir = analysis_dir / "chapter_analysis"
    if not chapter_analysis_dir.exists():
        return False
    
    # Count source chapters and require matching summaries
    source_count = count_source_chapters(project_root)
    if source_count == 0:
        return False
    
    summary_files = list(chapter_analysis_dir.glob("CH*_summary.md"))
    if len(summary_files) < source_count:
        return False
    
    # Check global registries
    world_global = analysis_dir / "world" / "global"
    if not (world_global / "CHARACTER_REGISTRY_GLOBAL.json").exists():
        return False
    if not (world_global / "ENVIRONMENT_REGISTRY_GLOBAL.json").exists():
        return False
    
    return True


def check_character_taxonomy(project_root: Path) -> bool:
    """Check if character taxonomy is complete."""
    taxonomy_dir = project_root / "02_story_analysis" / "taxonomy" / "characters"
    index_file = taxonomy_dir / "CHARACTER_TAXONOMY_INDEX.json"
    
    if not index_file.exists():
        return False
    
    # Check at least one taxonomy file has required fields
    for tax_file in taxonomy_dir.glob("CHAR_*.json"):
        try:
            with open(tax_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
                if all(k in data for k in ['morphology', 'renderability', 'confidence', 'direct_evidence_records']):
                    return True
        except:
            continue
    
    return False


def check_identity_refinement(project_root: Path) -> bool:
    """Check if identity refinement is complete."""
    refinement_dir = project_root / "02_story_analysis" / "world" / "refinement"
    if not refinement_dir.exists():
        return False
    
    # Check if any refinement output exists
    return len(list(refinement_dir.glob("*.json"))) > 0


def check_character_bibles(project_root: Path) -> bool:
    """Check if character bibles are complete."""
    bibles_dir = project_root / "02_story_analysis" / "bibles" / "characters"
    index_file = bibles_dir / "CHARACTER_BIBLE_INDEX.json"
    
    if not index_file.exists():
        return False
    
    # Check at least one bible has required fields
    for bible_file in bibles_dir.glob("CHAR_*.json"):
        try:
            with open(bible_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
                if all(k in data for k in ['entity_taxonomy', 'alias_resolution', 'associated_entities', 'visual_production_fallback']):
                    return True
        except:
            continue
    
    return False


def check_environment_bibles(project_root: Path) -> bool:
    """Check if environment bibles are complete."""
    bibles_dir = project_root / "02_story_analysis" / "bibles" / "environments"
    index_file = bibles_dir / "ENVIRONMENT_BIBLE_INDEX.json"
    
    if not index_file.exists():
        return False
    
    # Check at least one environment bible exists
    return len(list(bibles_dir.glob("ENV_*.json"))) > 0


def check_visual_fallbacks(project_root: Path) -> bool:
    """Check if visual fallbacks are complete."""
    fallbacks_file = project_root / "02_story_analysis" / "world" / "global" / "VISUAL_FALLBACKS.json"
    
    if not fallbacks_file.exists():
        return False
    
    try:
        with open(fallbacks_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return all(k in data for k in ['book_visual_context', 'character_fallbacks', 'environment_fallbacks', 'negative_terms'])
    except:
        return False


def check_scene_contracts(project_root: Path, chapters: str) -> bool:
    """Check if scene contracts are complete for selected chapters."""
    contracts_dir = project_root / "02_story_analysis" / "contracts"
    
    if not chapters:
        # If no chapters specified, just check if any contracts exist
        return contracts_dir.exists() and len(list(contracts_dir.glob("CH*/scene_*.json"))) > 0
    
    # Parse chapter range
    chapter_nums = parse_chapters(chapters)
    for ch_num in chapter_nums:
        ch_dir = contracts_dir / f"CH{ch_num:03d}"
        if not ch_dir.exists() or len(list(ch_dir.glob("scene_*.json"))) == 0:
            return False
    
    return True


def check_scene_bindings(project_root: Path, chapters: str) -> bool:
    """Check if scene bindings are complete for selected chapters."""
    # Scene bindings are typically in the same contracts directory or a bindings subdirectory
    contracts_dir = project_root / "02_story_analysis" / "contracts"
    
    if not chapters:
        return contracts_dir.exists() and len(list(contracts_dir.glob("CH*/scene_*_bindings.json"))) > 0
    
    chapter_nums = parse_chapters(chapters)
    for ch_num in chapter_nums:
        ch_dir = contracts_dir / f"CH{ch_num:03d}"
        if not ch_dir.exists() or len(list(ch_dir.glob("scene_*_bindings.json"))) == 0:
            return False
    
    return True


def check_shot_packages(project_root: Path, chapters: str) -> bool:
    """Check if shot packages are complete for selected chapters."""
    contracts_dir = project_root / "02_story_analysis" / "contracts"
    
    if not chapters:
        return contracts_dir.exists() and len(list(contracts_dir.glob("CH*/scene_*_shots.json"))) > 0
    
    chapter_nums = parse_chapters(chapters)
    for ch_num in chapter_nums:
        ch_dir = contracts_dir / f"CH{ch_num:03d}"
        if not ch_dir.exists() or len(list(ch_dir.glob("scene_*_shots.json"))) == 0:
            return False
    
    return True


def check_dialogue_timeline(project_root: Path, chapters: str) -> bool:
    """Check if dialogue timeline is complete for selected chapters."""
    timelines_dir = project_root / "02_story_analysis" / "timelines" / "chapters"
    
    if not chapters:
        return timelines_dir.exists() and len(list(timelines_dir.glob("CH*/*_DIALOGUE_TIMELINE.json"))) > 0
    
    chapter_nums = parse_chapters(chapters)
    for ch_num in chapter_nums:
        timeline_file = timelines_dir / f"CH{ch_num:03d}" / f"CH{ch_num:03d}_DIALOGUE_TIMELINE.json"
        if not timeline_file.exists():
            return False
    
    return True


def check_descriptor_enrichment(project_root: Path) -> bool:
    """Check if descriptor enrichment is complete."""
    descriptors_dir = project_root / "02_story_analysis" / "descriptors"
    index_file = descriptors_dir / "DESCRIPTOR_INDEX.json"
    
    if not index_file.exists():
        return False
    
    try:
        with open(index_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return data.get('total_entries', 0) > 0 or len(data.get('records', [])) > 0
    except:
        return False


def check_prompt_preparation(project_root: Path) -> bool:
    """Check if prompt preparation is complete."""
    prompt_dir = project_root / "03_prompt_packages"
    index_file = prompt_dir / "PROMPT_PREPARATION_INDEX.json"
    
    if not index_file.exists():
        return False
    
    prepared_dir = prompt_dir / "prepared"
    return prepared_dir.exists() and len(list(prepared_dir.glob("*.md"))) > 0


def check_quality_grading(project_root: Path) -> bool:
    """Check if quality grading is complete."""
    quality_dir = project_root / "02_story_analysis" / "quality"
    grading_dir = project_root / "02_story_analysis" / "grading"
    
    # Check either location
    for check_dir in [quality_dir, grading_dir]:
        if check_dir.exists():
            json_files = list(check_dir.glob("*.json"))
            if json_files:
                try:
                    with open(json_files[0], 'r', encoding='utf-8') as f:
                        data = json.load(f)
                        if data.get('total_records', 0) > 0:
                            return True
                except:
                    continue
    
    return False


def parse_chapters(chapters: str) -> list[int]:
    """Parse chapter range like '2-3' into [2, 3]."""
    if not chapters or chapters == "":
        return []
    
    if '-' in chapters:
        start, end = chapters.split('-')
        return list(range(int(start), int(end) + 1))
    else:
        return [int(chapters)]


def find_first_incomplete_stage(project_slug: str, chapters: str = "") -> Optional[str]:
    """Find the first incomplete stage in the pipeline."""
    repo_root = Path(__file__).parent.parent
    project_root = repo_root / "projects" / project_slug
    
    if not project_root.exists():
        return "story_analysis"
    
    stages = [
        ("story_analysis", lambda: check_story_analysis(project_root)),
        ("character_taxonomy", lambda: check_character_taxonomy(project_root)),
        ("identity_refinement", lambda: check_identity_refinement(project_root)),
        ("character_bibles", lambda: check_character_bibles(project_root)),
        ("environment_bibles", lambda: check_environment_bibles(project_root)),
        ("visual_fallbacks", lambda: check_visual_fallbacks(project_root)),
        ("scene_contracts", lambda: check_scene_contracts(project_root, chapters)),
        ("scene_bindings", lambda: check_scene_bindings(project_root, chapters)),
        ("shot_packages", lambda: check_shot_packages(project_root, chapters)),
        ("dialogue_timeline", lambda: check_dialogue_timeline(project_root, chapters)),
        ("descriptor_enrichment", lambda: check_descriptor_enrichment(project_root)),
        ("prompt_preparation", lambda: check_prompt_preparation(project_root)),
        ("quality_grading", lambda: check_quality_grading(project_root)),
    ]
    
    for stage_name, check_func in stages:
        if not check_func():
            return stage_name
    
    return None  # All complete


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("story_analysis")
        sys.exit(0)
    
    project_slug = sys.argv[1]
    chapters = sys.argv[2] if len(sys.argv) > 2 else ""
    
    first_incomplete = find_first_incomplete_stage(project_slug, chapters)
    
    if first_incomplete:
        print(first_incomplete)
    else:
        print("complete")
    
    sys.exit(0)
