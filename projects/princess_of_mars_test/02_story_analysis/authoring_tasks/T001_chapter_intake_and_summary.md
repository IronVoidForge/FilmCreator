# Task
T001 Chapter Intake And Summary

## Objective

Read the chapter source file and produce a project-level summary and a chapter-level analysis foundation for later scene extraction.

## Inputs

- `01_source/chapters/CH001_a_princess_of_mars_ch08.md`

## Output Files

- `02_story_analysis/story_summary/project_summary.md`
- `02_story_analysis/chapter_analysis/CH001_summary.md`

## Response Contract

Return valid JSON only with these keys:

- `project_summary_markdown`
- `chapter_summary_markdown`

## Required Coverage

- overall premise of the work as needed for this chapter
- chapter summary
- major visual motifs
- major recurring characters present or referenced in this chapter
- major environment families present in this chapter
- continuity-sensitive facts that later scenes must preserve

## Rules

- proper nouns are allowed
- do not write prompt-package language yet
- do not mention ComfyUI nodes, workflow JSON, or rendering settings
- separate summary facts from visual continuity facts
- preserve uncertainty where the chapter is ambiguous

## Local LLM Guidance

- use chat-completions style structured generation
- prefer low temperature for reproducible extraction
- return complete Markdown strings that can be written directly to files
