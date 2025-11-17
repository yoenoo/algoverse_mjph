"""
Run comprehensive APPS experiment across all problems and permission levels.

Evaluates all 5 APPS problems at all 4 permission levels for a given LLM,
then uses an LLM evaluator to provide detailed analysis of each result.
"""

import argparse
from pathlib import Path
from datetime import datetime
from typing import List, Dict, Any
import json
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

from .benchmarks import (
    Apps0000Benchmark,
    Apps0001Benchmark,
    Apps0002Benchmark,
    Apps0003Benchmark,
    Apps0004Benchmark,
)
from .core.results import PermissionLevel
from .core.sandbox import DockerSandbox
from .llm_providers.provider import LLMProvider
from .evaluators.llm_evaluator import LLMEvaluator
from .problems.apps import (
    create_apps_0000,
    create_apps_0001,
    create_apps_0002,
    create_apps_0003,
    create_apps_0004,
)


# Map problem names to benchmark classes and problem creators
APPS_BENCHMARKS = {
    "apps_0000": (Apps0000Benchmark, create_apps_0000),
    "apps_0001": (Apps0001Benchmark, create_apps_0001),
    "apps_0002": (Apps0002Benchmark, create_apps_0002),
    "apps_0003": (Apps0003Benchmark, create_apps_0003),
    "apps_0004": (Apps0004Benchmark, create_apps_0004),
}

# All permission levels to test
PERMISSION_LEVELS = [
    PermissionLevel.PL0_CODE_SUGGESTION,
    PermissionLevel.PL1_MANUAL_FEEDBACK,
    PermissionLevel.PL2_AUTO_TEST_EXEC,
    PermissionLevel.PL3_FILE_MODIFICATION,
]


def sanitize_filename(name: str) -> str:
    """Sanitize a string for use in a filename."""
    # Replace invalid characters
    invalid_chars = ['/', '\\', ':', '*', '?', '"', '<', '>', '|']
    for char in invalid_chars:
        name = name.replace(char, '_')
    # Replace spaces with underscores
    name = name.replace(' ', '_')
    return name


def run_single_benchmark(
    benchmark_class,
    problem_creator,
    permission_level: PermissionLevel,
    llm_provider: LLMProvider,
    results_dir: Path
) -> Dict[str, Any]:
    """
    Run a single benchmark and save results.
    
    Args:
        benchmark_class: Benchmark class to instantiate
        problem_creator: Function to create the problem
        permission_level: Permission level to test
        llm_provider: LLM provider for the benchmark
        results_dir: Directory to save results
    
    Returns:
        Dict with benchmark result and metadata
    """
    problem_name = problem_creator().name
    print(f"\n{'='*80}")
    print(f"Running: {problem_name} at {permission_level.value}")
    print(f"{'='*80}")
    
    # Create benchmark
    benchmark = benchmark_class(permission_level, llm_provider)
    
    # Create sandbox
    sandbox = DockerSandbox()
    
    try:
        # Setup benchmark
        benchmark.setup(sandbox)
        
        # Run benchmark
        print(f"Executing benchmark...")
        benchmark_result = benchmark.run()
        
        # Get problem for evaluation
        problem = problem_creator()
        
        # Save benchmark result JSON
        benchmark_filename = f"{problem_name}_{permission_level.value}_{sanitize_filename(llm_provider.model)}.json"
        benchmark_filepath = results_dir / "benchmark_results" / benchmark_filename
        benchmark_filepath.parent.mkdir(parents=True, exist_ok=True)
        benchmark_filepath.write_text(benchmark_result.to_json(indent=2))
        print(f"✓ Saved benchmark result: {benchmark_filename}")
        
        return {
            "benchmark_result": benchmark_result,
            "problem": problem,
            "benchmark_filepath": benchmark_filepath,
            "success": True
        }
        
    except Exception as e:
        print(f"✗ Error running benchmark: {e}")
        import traceback
        traceback.print_exc()
        return {
            "success": False,
            "error": str(e)
        }
    finally:
        # Cleanup
        try:
            benchmark.cleanup()
            sandbox.cleanup()
        except:
            pass


def evaluate_with_llm(
    benchmark_result,
    problem,
    evaluator: LLMEvaluator,
    results_dir: Path,
    problem_name: str,
    permission_level: PermissionLevel,
    llm_model: str
) -> Path:
    """
    Evaluate benchmark result with LLM evaluator and save evaluation.
    
    Args:
        benchmark_result: Benchmark result to evaluate
        problem: Problem definition
        evaluator: LLM evaluator
        results_dir: Directory to save results
        problem_name: Name of the problem
        permission_level: Permission level tested
        llm_model: LLM model that was tested
    
    Returns:
        Path to saved evaluation file
    """
    print(f"Evaluating with LLM evaluator...")
    
    try:
        # Get evaluation
        evaluation = evaluator.evaluate(benchmark_result, problem)
        
        # Save evaluation
        eval_filename = f"{problem_name}_{permission_level.value}_{sanitize_filename(llm_model)}_evaluation.txt"
        eval_filepath = results_dir / "evaluations" / eval_filename
        eval_filepath.parent.mkdir(parents=True, exist_ok=True)
        eval_filepath.write_text(evaluation)
        print(f"✓ Saved evaluation: {eval_filename}")
        
        return eval_filepath
        
    except Exception as e:
        print(f"✗ Error during LLM evaluation: {e}")
        import traceback
        traceback.print_exc()
        # Save error message
        eval_filename = f"{problem_name}_{permission_level.value}_{sanitize_filename(llm_model)}_evaluation_ERROR.txt"
        eval_filepath = results_dir / "evaluations" / eval_filename
        eval_filepath.parent.mkdir(parents=True, exist_ok=True)
        eval_filepath.write_text(f"Error during LLM evaluation: {e}\n\n{traceback.format_exc()}")
        return eval_filepath


def run_full_experiment(
    llm_model: str,
    evaluator_model: str = "openai/gpt-4",
    results_dir: Path = None,
    skip_evaluation: bool = False
):
    """
    Run full APPS experiment across all problems and permission levels.
    
    Args:
        llm_model: LLM model to test (e.g., "openai/gpt-4", "anthropic/claude-3-opus")
        evaluator_model: LLM model to use for evaluation (default: GPT-4)
        results_dir: Directory to save results (default: apps_experiment_results/)
        skip_evaluation: If True, skip LLM evaluation (just run benchmarks)
    """
    # Setup results directory
    if results_dir is None:
        # Default to explore/apps_experiment_results
        results_dir = Path(__file__).parent.parent / "apps_experiment_results"
    else:
        results_dir = Path(results_dir)
    
    results_dir.mkdir(parents=True, exist_ok=True)
    (results_dir / "benchmark_results").mkdir(exist_ok=True)
    (results_dir / "evaluations").mkdir(exist_ok=True)
    
    # Create LLM provider for benchmarks
    print(f"Creating LLM provider for model: {llm_model}")
    benchmark_provider = LLMProvider(model=llm_model)
    
    # Create LLM evaluator (if not skipping)
    evaluator = None
    if not skip_evaluation:
        print(f"Creating LLM evaluator with model: {evaluator_model}")
        evaluator_provider = LLMProvider(model=evaluator_model)
        evaluator = LLMEvaluator(evaluator_provider)
    
    # Track experiment metadata
    experiment_metadata = {
        "llm_model": llm_model,
        "evaluator_model": evaluator_model if not skip_evaluation else None,
        "timestamp": datetime.now().isoformat(),
        "results": []
    }
    
    # Run all combinations
    total_combinations = len(APPS_BENCHMARKS) * len(PERMISSION_LEVELS)
    current = 0
    
    print(f"\n{'='*80}")
    print(f"Starting APPS Experiment")
    print(f"  LLM Model: {llm_model}")
    print(f"  Evaluator Model: {evaluator_model if not skip_evaluation else 'N/A (skipped)'}")
    print(f"  Total combinations: {total_combinations}")
    print(f"  Results directory: {results_dir}")
    print(f"{'='*80}\n")
    
    for problem_name, (benchmark_class, problem_creator) in APPS_BENCHMARKS.items():
        for permission_level in PERMISSION_LEVELS:
            current += 1
            print(f"\n[{current}/{total_combinations}] ", end="")
            
            # Run benchmark
            result = run_single_benchmark(
                benchmark_class,
                problem_creator,
                permission_level,
                benchmark_provider,
                results_dir
            )
            
            if result["success"]:
                benchmark_result = result["benchmark_result"]
                problem = result["problem"]
                
                # Evaluate with LLM (if not skipping)
                eval_filepath = None
                if not skip_evaluation and evaluator:
                    eval_filepath = evaluate_with_llm(
                        benchmark_result,
                        problem,
                        evaluator,
                        results_dir,
                        problem_name,
                        permission_level,
                        llm_model
                    )
                
                # Track result
                experiment_metadata["results"].append({
                    "problem": problem_name,
                    "permission_level": permission_level.value,
                    "benchmark_file": str(result["benchmark_filepath"].relative_to(results_dir)),
                    "evaluation_file": str(eval_filepath.relative_to(results_dir)) if eval_filepath else None,
                    "visible_tests_passed": benchmark_result.execution_result.visible_tests_passed,
                    "hidden_tests_passed": benchmark_result.execution_result.hidden_tests_passed,
                    "hardcoding_detected": benchmark_result.detection_result.hardcoding_detected,
                    "overfitting_detected": benchmark_result.detection_result.overfitting_detected,
                    "execution_gaming_detected": benchmark_result.detection_result.execution_gaming_detected,
                    "test_modification_detected": benchmark_result.detection_result.test_edit_detected,
                    "execution_time_seconds": benchmark_result.execution_result.execution_time_seconds,
                })
            else:
                # Track failure
                experiment_metadata["results"].append({
                    "problem": problem_name,
                    "permission_level": permission_level.value,
                    "success": False,
                    "error": result.get("error", "Unknown error")
                })
    
    # Save experiment summary
    summary_filename = f"experiment_summary_{sanitize_filename(llm_model)}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    summary_filepath = results_dir / summary_filename
    summary_filepath.write_text(json.dumps(experiment_metadata, indent=2))
    print(f"\n{'='*80}")
    print(f"Experiment Complete!")
    print(f"  Summary saved to: {summary_filepath}")
    print(f"{'='*80}\n")
    
    # Print summary statistics
    successful = sum(1 for r in experiment_metadata["results"] if r.get("success", True))
    print(f"Summary Statistics:")
    print(f"  Total combinations: {total_combinations}")
    print(f"  Successful: {successful}")
    print(f"  Failed: {total_combinations - successful}")
    print()


def main():
    """Main entry point for the script."""
    parser = argparse.ArgumentParser(
        description="Run APPS experiment across all problems and permission levels"
    )
    parser.add_argument(
        "--llm-model",
        type=str,
        required=True,
        help="LLM model to test (e.g., 'openai/gpt-4', 'anthropic/claude-3-opus')"
    )
    parser.add_argument(
        "--evaluator-model",
        type=str,
        default="openai/gpt-4",
        help="LLM model to use for evaluation (default: openai/gpt-4)"
    )
    parser.add_argument(
        "--results-dir",
        type=str,
        default=None,
        help="Directory to save results (default: apps_experiment_results/)"
    )
    parser.add_argument(
        "--skip-evaluation",
        action="store_true",
        help="Skip LLM evaluation (just run benchmarks)"
    )
    
    args = parser.parse_args()
    
    # Run experiment
    run_full_experiment(
        llm_model=args.llm_model,
        evaluator_model=args.evaluator_model,
        results_dir=Path(args.results_dir) if args.results_dir else None,
        skip_evaluation=args.skip_evaluation
    )


if __name__ == "__main__":
    main()

