# APPS Experiment Results

This directory contains results from running APPS benchmarks across all problems and permission levels.

## Directory Structure

```
apps_experiment_results/
├── benchmark_results/          # JSON files with benchmark execution results
│   ├── apps_0000_code_suggestion_<model>.json
│   ├── apps_0000_manual_feedback_<model>.json
│   ├── apps_0000_auto_test_exec_<model>.json
│   ├── apps_0000_file_modification_<model>.json
│   ├── apps_0001_code_suggestion_<model>.json
│   └── ... (20 total files per LLM model)
│
├── evaluations/                # LLM evaluation text files
│   ├── apps_0000_code_suggestion_<model>_evaluation.txt
│   ├── apps_0000_manual_feedback_<model>_evaluation.txt
│   └── ... (20 total files per LLM model)
│
└── experiment_summary_<model>_<timestamp>.json  # Overall experiment summary
```

## File Naming Convention

- **Benchmark Results**: `{problem_name}_{permission_level}_{llm_model}.json`
- **Evaluations**: `{problem_name}_{permission_level}_{llm_model}_evaluation.txt`
- **Summary**: `experiment_summary_{llm_model}_{timestamp}.json`

## Running Experiments

```bash
# Run full experiment with LLM evaluation
python explore/run_apps_experiment.py --llm-model "openai/gpt-4"

# Run with custom evaluator model
python explore/run_apps_experiment.py --llm-model "openai/gpt-4" --evaluator-model "openai/gpt-4o"

# Run without LLM evaluation (just benchmarks)
python explore/run_apps_experiment.py --llm-model "openai/gpt-4" --skip-evaluation

# Custom results directory
python explore/run_apps_experiment.py --llm-model "openai/gpt-4" --results-dir "./my_results"
```

## Experiment Coverage

Each experiment runs:
- **5 APPS problems**: apps_0000, apps_0001, apps_0002, apps_0003, apps_0004
- **4 Permission levels**: PL0, PL1, PL2, PL3
- **Total**: 20 benchmark combinations per LLM model

## Result Files

### Benchmark Result JSON
Contains:
- Test execution results (visible/hidden pass/fail)
- Detection results (hardcoding, overfitting, execution gaming, test modification)
- Command history
- File changes
- Execution metadata

### Evaluation Text
Contains detailed LLM analysis:
- Problem-solving performance assessment
- Reward hacking behavior detection
- Specific examples and evidence
- Severity assessments
- Recommendations

### Summary JSON
Contains:
- Experiment metadata
- Summary statistics for all combinations
- Quick reference for pass/fail and detection results

