"""
Example usage of LLM-based evaluator.

This shows how to use the LLM evaluator to evaluate benchmark results.
"""

from ..evaluators.llm_evaluator import LLMEvaluator
from ..llm_providers.provider import LLMProvider
from ..core.results import BenchmarkResult
from ..core.problem import Problem


def evaluate_benchmark_result(
    benchmark_result: BenchmarkResult,
    problem: Problem,
    evaluator_model: str = "openai/gpt-4"
) -> str:
    """
    Evaluate a benchmark result using an LLM evaluator.
    
    Args:
        benchmark_result: Benchmark result to evaluate
        problem: Problem definition
        evaluator_model: Model to use for evaluation (default: GPT-4)
    
    Returns:
        Detailed evaluation text
    """
    # Create evaluator LLM provider
    evaluator_provider = LLMProvider(model=evaluator_model)
    
    # Create evaluator
    evaluator = LLMEvaluator(evaluator_provider)
    
    # Evaluate
    evaluation = evaluator.evaluate(benchmark_result, problem)
    
    return evaluation


# Example usage:
if __name__ == "__main__":
    # After running a benchmark:
    # benchmark_result = benchmark.run()
    # problem = benchmark.problem
    
    # Evaluate the result
    # evaluation = evaluate_benchmark_result(benchmark_result, problem)
    # print(evaluation)
    pass

