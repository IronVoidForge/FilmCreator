param(
    [string]$ProjectSlug = "princess_of_mars_test",
    [string]$Arg2 = "",
    [string]$Arg3 = ""
)

$ErrorActionPreference = "Stop"
$RunnerVersion = "PS_WRAPPER_QUIET_V3_2026-04-26"

$Chapters = $Arg2
$Mode = $Arg3

if ($Chapters -ieq "PLAN_ONLY") {
    $Mode = "PLAN_ONLY"
    $Chapters = ""
}

if ($Chapters -ieq "VALIDATE_ONLY") {
    $Mode = "VALIDATE_ONLY"
    $Chapters = ""
}

$ChaptersDisplay = if ([string]::IsNullOrWhiteSpace($Chapters)) { "ALL" } else { $Chapters }

$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$RepoRoot = (Resolve-Path (Join-Path $ScriptDir "..")).Path
Set-Location $RepoRoot

$LogDir = Join-Path $RepoRoot "logs\overnight"
New-Item -ItemType Directory -Force -Path $LogDir | Out-Null

$Stamp = Get-Date -Format "yyyyMMdd_HHmmss"
$LogFile = Join-Path $LogDir "${ProjectSlug}_overnight_resume_${Stamp}.log"
$LatestLog = Join-Path $LogDir "${ProjectSlug}_overnight_resume_latest.log"
$TempLog = Join-Path $LogDir "${ProjectSlug}_overnight_resume_step.tmp"
$StepListPath = Join-Path $LogDir "${ProjectSlug}_overnight_resume_steps_${Stamp}.tsv"

Remove-Item $LatestLog, $TempLog, $StepListPath -Force -ErrorAction SilentlyContinue

function Write-Both {
    param([string]$Text = "")
    Write-Host $Text
    Add-Content -Path $LogFile -Value $Text
    Add-Content -Path $LatestLog -Value $Text
}

function Add-Log {
    param([string]$Text = "")
    Add-Content -Path $LogFile -Value $Text
    Add-Content -Path $LatestLog -Value $Text
}

function Invoke-PythonCaptured {
    param(
        [string[]]$Args,
        [string]$OutPath
    )

    Remove-Item $OutPath -Force -ErrorAction SilentlyContinue

    $oldPreference = $global:ErrorActionPreference
    $global:ErrorActionPreference = "Continue"

    try {
        $output = & python @Args 2>&1
        $exitCode = $LASTEXITCODE
    } finally {
        $global:ErrorActionPreference = $oldPreference
    }

    if ($null -eq $output) {
        "" | Set-Content -Path $OutPath
    } else {
        $output | ForEach-Object { $_.ToString() } | Set-Content -Path $OutPath
    }

    return $exitCode
}

function Invoke-AnalysisCaptured {
    param(
        [string]$OutPath
    )

    $py = "from orchestrator.book_authoring import analyze_book; import json; summary = analyze_book(project_slug='$ProjectSlug'); print(json.dumps(summary.to_dict(), indent=2))"
    return Invoke-PythonCaptured -Args @("-c", $py) -OutPath $OutPath
}

Write-Both "============================================================"
Write-Both "FilmCreator Overnight Resume Pipeline"
Write-Both "RUNNER_VERSION: $RunnerVersion"
Write-Both "Project:        $ProjectSlug"
Write-Both "Chapters:       $ChaptersDisplay"
Write-Both "Repo root:      $RepoRoot"
Write-Both "Log:            $LogFile"
Write-Both "Latest:         $LatestLog"
Write-Both "============================================================"
Write-Both ""

if ($Mode -ieq "VALIDATE_ONLY") {
    Write-Both "VALIDATE_ONLY"
    $args = @("-m", "orchestrator.overnight_pipeline_resume_check", $ProjectSlug)
    if (-not [string]::IsNullOrWhiteSpace($Chapters)) { $args += $Chapters }
    $args += "--report"

    $exit = Invoke-PythonCaptured -Args $args -OutPath $TempLog
    Get-Content $TempLog | ForEach-Object {
        Write-Host $_
        Add-Log $_
    }
    exit $exit
}

Write-Both "Detecting resume stage..."
$detectArgs = @("-m", "orchestrator.overnight_pipeline_resume_check", $ProjectSlug)
if (-not [string]::IsNullOrWhiteSpace($Chapters)) { $detectArgs += $Chapters }

$detectExit = Invoke-PythonCaptured -Args $detectArgs -OutPath $TempLog
Get-Content $TempLog | ForEach-Object { Add-Log $_ }

if ($detectExit -ne 0) {
    Write-Both "ERROR: Resume detection failed. exit=$detectExit"
    Write-Both "Detection output:"
    Get-Content $TempLog -Tail 40 | ForEach-Object { Write-Both $_ }
    exit $detectExit
}

$ResumeStage = (Get-Content $TempLog | Where-Object { $_ -and $_.ToString().Trim() } | Select-Object -First 1).ToString().Trim()

if ([string]::IsNullOrWhiteSpace($ResumeStage)) {
    Write-Both "ERROR: Resume detection produced no stage."
    Write-Both "Detection output:"
    Get-Content $TempLog -Tail 40 | ForEach-Object { Write-Both $_ }
    exit 1
}

Write-Both "Detected: $ResumeStage"
Write-Both ""

if ($ResumeStage -eq "complete") {
    Write-Both "Already complete."
    exit 0
}

$StageLevels = @{
    "story_analysis"        = 1
    "character_taxonomy"    = 3
    "identity_refinement"   = 4
    "character_bibles"      = 6
    "environment_bibles"    = 7
    "visual_fallbacks"      = 8
    "scene_contracts"       = 9
    "scene_bindings"        = 10
    "shot_packages"         = 11
    "dialogue_timeline"     = 12
    "descriptor_enrichment" = 13
    "prompt_preparation"    = 14
    "quality_grading"       = 15
}

if (-not $StageLevels.ContainsKey($ResumeStage)) {
    Write-Both "ERROR: Unknown resume stage: $ResumeStage"
    exit 1
}

$StartLevel = $StageLevels[$ResumeStage]
$Steps = New-Object System.Collections.Generic.List[object]

function Add-Step {
    param(
        [string]$Name,
        [string[]]$Args,
        [switch]$Analysis
    )

    $Steps.Add([pscustomobject]@{
        Name = $Name
        Args = $Args
        Analysis = [bool]$Analysis
    })
}

if ($StartLevel -le 1) {
    Add-Step "01 LM Studio check" @("-m", "orchestrator", "diagnostics-lmstudio")
}

if ($StartLevel -le 2) {
    Add-Step "02 Story analysis" @() -Analysis
}

if ($StartLevel -le 3) {
    Add-Step "03 Character taxonomy" @("-m", "orchestrator", "synthesize-character-taxonomy", $ProjectSlug, "--force")
}

if ($StartLevel -le 4) {
    Add-Step "04 Identity refinement plan" @("-m", "orchestrator", "refine-identities", $ProjectSlug)
}

if ($StartLevel -le 5) {
    Add-Step "05 Identity refinement apply" @("-m", "orchestrator", "refine-identities", $ProjectSlug, "--apply")
}

if ($StartLevel -le 6) {
    Add-Step "06 Character bibles" @("-m", "orchestrator", "synthesize-character-bibles", $ProjectSlug, "--force")
}

if ($StartLevel -le 7) {
    Add-Step "07 Environment bibles" @("-m", "orchestrator", "synthesize-environment-bibles", $ProjectSlug, "--force")
}

if ($StartLevel -le 8) {
    Add-Step "08 Visual fallbacks" @("-m", "orchestrator", "synthesize-visual-fallbacks", $ProjectSlug, "--force")
}

if ($StartLevel -le 9) {
    $args = @("-m", "orchestrator", "synthesize-scene-contracts", $ProjectSlug, "--force")
    if (-not [string]::IsNullOrWhiteSpace($Chapters)) { $args += @("--chapters", $Chapters) }
    Add-Step "09 Scene contracts" $args
}

if ($StartLevel -le 10) {
    $args = @("-m", "orchestrator", "synthesize-scene-bindings", $ProjectSlug, "--force")
    if (-not [string]::IsNullOrWhiteSpace($Chapters)) { $args += @("--chapters", $Chapters) }
    Add-Step "10 Scene bindings" $args
}

if ($StartLevel -le 11) {
    $args = @("-m", "orchestrator", "synthesize-shot-packages", $ProjectSlug, "--force")
    if (-not [string]::IsNullOrWhiteSpace($Chapters)) { $args += @("--chapters", $Chapters) }
    Add-Step "11 Shot packages" $args
}

if ($StartLevel -le 12) {
    $args = @("-m", "orchestrator", "synthesize-dialogue-timeline", $ProjectSlug, "--force")
    if (-not [string]::IsNullOrWhiteSpace($Chapters)) { $args += @("--chapters", $Chapters) }
    Add-Step "12 Dialogue timeline" $args
}

if ($StartLevel -le 13) {
    $args = @("-m", "orchestrator", "synthesize-descriptor-enrichment", $ProjectSlug, "--force")
    if (-not [string]::IsNullOrWhiteSpace($Chapters)) { $args += @("--chapters", $Chapters) }
    Add-Step "13 Descriptor enrichment" $args
}

if ($StartLevel -le 14) {
    $args = @("-m", "orchestrator", "synthesize-prompt-preparation", $ProjectSlug, "--force")
    if (-not [string]::IsNullOrWhiteSpace($Chapters)) { $args += @("--chapters", $Chapters) }
    Add-Step "14 Prompt preparation" $args
}

if ($StartLevel -le 15) {
    Add-Step "15 Quality grading" @("-m", "orchestrator", "grade-artifacts", $ProjectSlug)
}

$stepNames = $Steps | ForEach-Object { $_.Name }

if (($stepNames -contains "12 Dialogue timeline") -and $StartLevel -le 11) {
    foreach ($required in @("09 Scene contracts", "10 Scene bindings", "11 Shot packages")) {
        if ($stepNames -notcontains $required) {
            Write-Both "ERROR: Invalid step list. Dialogue timeline missing upstream step: $required"
            $stepNames | ForEach-Object { Write-Both "  $_" }
            exit 1
        }
    }
}

$Steps | ForEach-Object {
    $cmdText = if ($_.Analysis) {
        "__ANALYZE_BOOK__"
    } else {
        "python " + ($_.Args -join " ")
    }
    Add-Content -Path $StepListPath -Value "$($_.Name)`t$cmdText"
}

if ($Mode -ieq "PLAN_ONLY") {
    Write-Both "PLAN_ONLY | RUNNER_VERSION=$RunnerVersion"
    Write-Both "resume=$ResumeStage | start_level=$StartLevel | project=$ProjectSlug | chapters=$ChaptersDisplay"
    Write-Both "Step list:"
    $Steps | ForEach-Object { Write-Both "  $($_.Name)" }
    Write-Both "Step list file: $StepListPath"
    Write-Both "Log: $LogFile"
    exit 0
}

Write-Both "Resume stage: $ResumeStage"
Write-Both "Start level:  $StartLevel"
Write-Both "Step list:"
$Steps | ForEach-Object { Write-Both "  $($_.Name)" }
Write-Both ""

function Get-JsonSummary {
    param([string]$Path)

    if (-not (Test-Path $Path)) { return "" }

    $raw = Get-Content $Path -Raw
    $idx = $raw.IndexOf("{")
    if ($idx -lt 0) { return "" }

    $jsonText = $raw.Substring($idx).Trim()
    try {
        $obj = $jsonText | ConvertFrom-Json -ErrorAction Stop
    } catch {
        return ""
    }

    $parts = New-Object System.Collections.Generic.List[string]

    foreach ($key in @(
        "status",
        "total_registry_entries",
        "candidate_count",
        "comparison_count",
        "decision_count",
        "applied_count",
        "human_review_count",
        "total_entries",
        "total_chapters",
        "total_events",
        "total_scene_entries",
        "total_shot_entries",
        "total_scene_bindings",
        "total_shot_bindings",
        "synthesized_count",
        "reused_count",
        "stale_locked_count",
        "review_queue_count",
        "needs_review_count",
        "unknown_count",
        "total_records"
    )) {
        if ($obj.PSObject.Properties.Name -contains $key) {
            $parts.Add("$key=$($obj.$key)")
        }
    }

    if ($obj.PSObject.Properties.Name -contains "written_files") {
        $parts.Add("files=$(@($obj.written_files).Count)")
    }

    if ($obj.PSObject.Properties.Name -contains "warnings") {
        $parts.Add("warnings=$(@($obj.warnings).Count)")
    }

    if ($obj.PSObject.Properties.Name -contains "family_summaries") {
        $families = @($obj.family_summaries) |
            Where-Object { $_.count -gt 0 } |
            ForEach-Object { "$($_.family)=$($_.count)/rerun=$($_.rerun_count)" }

        if ($families.Count -gt 0) {
            $parts.Add("families=" + ($families -join ", "))
        }
    }

    if ($parts.Count -eq 0) { return "" }
    return "SUMMARY: " + ($parts -join " | ")
}

function Get-ProgressLines {
    param([string]$Path)

    if (-not (Test-Path $Path)) { return @() }

    $lines = Get-Content $Path

    $progress = $lines | Where-Object {
        ($_ -match '^\[[A-Za-z0-9_-]+\]') -and
        ($_ -match 'starting|finished|synthesized|reused|failed|error|warning')
    }

    return @($progress | Select-Object -Last 120)
}

function Invoke-Step {
    param($Step)

    Write-Both ""
    Write-Both "----------------------------------------"
    Write-Both "START: $($Step.Name)"
    Write-Both "----------------------------------------"

    if ($Step.Analysis) {
        $exitCode = Invoke-AnalysisCaptured -OutPath $TempLog
    } else {
        $exitCode = Invoke-PythonCaptured -Args $Step.Args -OutPath $TempLog
    }

    Add-Log ""
    Add-Log "----------------------------------------"
    Add-Log "START: $($Step.Name)"
    Add-Log ("COMMAND: " + $(if ($Step.Analysis) { "__ANALYZE_BOOK__" } else { "python " + ($Step.Args -join " ") }))
    Add-Log "----------------------------------------"

    if (Test-Path $TempLog) {
        Get-Content $TempLog | ForEach-Object { Add-Log $_ }
    }

    if ($exitCode -ne 0) {
        Write-Both "FAILED: $($Step.Name) exit code $exitCode"
        Write-Both "Last 40 log lines:"
        Get-Content $TempLog -Tail 40 | ForEach-Object { Write-Both $_ }
        exit $exitCode
    }

    $progress = Get-ProgressLines $TempLog
    foreach ($line in $progress) {
        Write-Both $line
    }

    $summary = Get-JsonSummary $TempLog
    if (-not [string]::IsNullOrWhiteSpace($summary)) {
        Write-Both $summary
    }

    Write-Both "DONE: $($Step.Name) exit code 0"
}

foreach ($step in $Steps) {
    Invoke-Step $step
}

Write-Both ""
Write-Both "============================================================"
Write-Both "COMPLETE"
Write-Both "Log:    $LogFile"
Write-Both "Latest: $LatestLog"
Write-Both "============================================================"

exit 0