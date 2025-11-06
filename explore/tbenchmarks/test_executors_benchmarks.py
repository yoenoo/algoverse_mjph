#!/usr/bin/env python3
"""
Test script for executors and benchmarks.

Tests:
- PL0 executor
- PL1 executor
- Benchmark execution with all executors
- Outputs LLM responses for debugging
"""

import sys
import os
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from dotenv import load_dotenv
load_dotenv()

from explore.tbenchmarks.core.problem import Problem, TestCase
from explore.tbenchmarks.core.results import PermissionLevel
from explore.tbenchmarks.core.sandbox import DockerSandbox
from explore.tbenchmarks.executors.pl0_code_suggestion import PL0CodeSuggestionExecutor
from explore.tbenchmarks.executors.pl1_manual_feedback import PL1ManualFeedbackExecutor
from explore.tbenchmarks.llm_providers.provider import LLMProvider
from explore.tbenchmarks.benchmarks import FibonacciHardcodingBenchmark, PrimeHardcodingBenchmark
from explore.tbenchmarks.problems.fibonacci import create_fibonacci_problem
from explore.tbenchmarks.problems.prime import create_prime_problem


def test_pl0_executor_full():
    """Test PL0 executor with full execution"""
    print("=" * 60)
    print("Testing PL0 Executor (Full Execution)")
    print("=" * 60)
    
    try:
        # Check API key
        api_key = os.getenv("OPENROUTER_API_KEY")
        if not api_key or api_key.strip() == "":
            print("⚠ OPENROUTER_API_KEY not set")
            print("  Skipping PL0 executor test (set OPENROUTER_API_KEY to test)")
            return
        
        # Create provider
        model = os.getenv("OPENROUTER_MODEL", "openai/gpt-3.5-turbo")
        provider = LLMProvider.create_from_config(model=model)
        print(f"✓ Provider created: {provider.model}")
        
        # Create executor
        executor = PL0CodeSuggestionExecutor(provider)
        print(f"✓ Executor created: {executor.permission_level}")
        
        # Create problem
        problem = create_fibonacci_problem()
        print(f"✓ Problem created: {problem.name}")
        
        # Create sandbox
        sandbox = DockerSandbox()
        sandbox.create()
        print(f"✓ Sandbox created")
        
        # Execute
        print(f"\n  Executing PL0 benchmark (this will make an API call)...")
        print(f"  ⚠ WARNING: This will use API credits!\n")
        
        # Capture LLM response by patching the provider
        llm_responses = []
        original_generate = provider.generate
        
        def logged_generate(*args, **kwargs):
            response = original_generate(*args, **kwargs)
            llm_responses.append({
                "prompt": args[0] if args else kwargs.get("prompt", ""),
                "response": response.text,
                "model": response.model,
                "tokens": response.usage.get("total_tokens", 0) if response.usage else 0
            })
            return response
        
        provider.generate = logged_generate
        
        execution_result = executor.execute(problem, sandbox)
        
        print(f"\n✓ Execution completed")
        print(f"  Visible tests: {'PASSED ✓' if execution_result.visible_tests_passed else 'FAILED ✗'}")
        print(f"  Hidden tests: {'PASSED ✓' if execution_result.hidden_tests_passed else 'FAILED ✗'}")
        print(f"  Execution time: {execution_result.execution_time_seconds:.2f}s")
        
        # Show LLM responses
        if llm_responses:
            print(f"\n  LLM Response(s):")
            for i, resp in enumerate(llm_responses, 1):
                print(f"    Response {i}:")
                print(f"      Model: {resp['model']}")
                print(f"      Tokens: {resp['tokens']}")
                print(f"      Response preview: {resp['response'][:200]}...")
                if len(resp['response']) > 200:
                    print(f"      (Full response: {len(resp['response'])} chars)")
        
        # Show output if failed
        if not execution_result.visible_tests_passed:
            print(f"\n  Visible test output:")
            print(f"  {execution_result.visible_test_output[:200]}...")
        
        if not execution_result.hidden_tests_passed:
            print(f"\n  Hidden test output:")
            print(f"  {execution_result.hidden_test_output[:200]}...")
        
        # Cleanup
        sandbox.cleanup()
        print(f"✓ Cleanup completed")
        
    except Exception as e:
        print(f"❌ PL0 executor test failed: {e}")
        import traceback
        traceback.print_exc()
    
    print("\n✅ PL0 executor test complete!\n")


def test_pl1_executor_full():
    """Test PL1 executor with full execution"""
    print("=" * 60)
    print("Testing PL1 Executor (Full Execution)")
    print("=" * 60)
    
    try:
        # Check API key
        api_key = os.getenv("OPENROUTER_API_KEY")
        if not api_key or api_key.strip() == "":
            print("⚠ OPENROUTER_API_KEY not set")
            print("  Skipping PL1 executor test (set OPENROUTER_API_KEY to test)")
            return
        
        # Create provider
        model = os.getenv("OPENROUTER_MODEL", "openai/gpt-3.5-turbo")
        provider = LLMProvider.create_from_config(model=model)
        print(f"✓ Provider created: {provider.model}")
        
        # Create executor
        executor = PL1ManualFeedbackExecutor(provider, max_iterations=3)  # Limit iterations for testing
        print(f"✓ Executor created: {executor.permission_level}")
        print(f"✓ Max iterations: {executor.max_iterations}")
        
        # Create problem
        problem = create_fibonacci_problem()
        print(f"✓ Problem created: {problem.name}")
        
        # Create sandbox
        sandbox = DockerSandbox()
        sandbox.create()
        print(f"✓ Sandbox created")
        
        # Execute
        print(f"\n  Executing PL1 benchmark (this will make multiple API calls)...")
        print(f"  ⚠ WARNING: This will use API credits!")
        print(f"  ⚠ Multi-turn conversation may take several API calls\n")
        
        # Capture LLM responses by patching the provider
        llm_responses = []
        original_chat = provider.chat
        
        def logged_chat(*args, **kwargs):
            messages = args[0] if args else kwargs.get("messages", [])
            response = original_chat(*args, **kwargs)
            llm_responses.append({
                "turn": len(llm_responses) + 1,
                "messages": messages[-1] if messages else {},  # Last message
                "response": response.text,
                "model": response.model,
                "tokens": response.usage.get("total_tokens", 0) if response.usage else 0
            })
            return response
        
        provider.chat = logged_chat
        
        execution_result = executor.execute(problem, sandbox)
        
        print(f"\n✓ Execution completed")
        print(f"  Visible tests: {'PASSED ✓' if execution_result.visible_tests_passed else 'FAILED ✗'}")
        print(f"  Hidden tests: {'PASSED ✓' if execution_result.hidden_tests_passed else 'FAILED ✗'}")
        print(f"  Execution time: {execution_result.execution_time_seconds:.2f}s")
        print(f"  Commands executed: {len(execution_result.command_history) if execution_result.command_history else 0}")
        print(f"  LLM turns: {len(llm_responses)}")
        
        # Show LLM conversation
        if llm_responses:
            print(f"\n  LLM Conversation:")
            for resp in llm_responses:
                print(f"\n    Turn {resp['turn']}:")
                print(f"      Model: {resp['model']}")
                print(f"      Tokens: {resp['tokens']}")
                if resp.get('messages'):
                    msg = resp['messages']
                    print(f"      User message: {msg.get('content', '')[:100]}...")
                print(f"      Assistant response preview: {resp['response'][:200]}...")
                if len(resp['response']) > 200:
                    print(f"      (Full response: {len(resp['response'])} chars)")
        
        # Show command history
        if execution_result.command_history:
            print(f"\n  Command history:")
            for i, cmd in enumerate(execution_result.command_history[:5], 1):  # Show first 5
                print(f"    {i}. {cmd.get('command', 'N/A')[:50]}...")
            if len(execution_result.command_history) > 5:
                print(f"    ... and {len(execution_result.command_history) - 5} more")
        
        # Show output if failed
        if not execution_result.visible_tests_passed:
            print(f"\n  Visible test output:")
            print(f"  {execution_result.visible_test_output[:200]}...")
        
        if not execution_result.hidden_tests_passed:
            print(f"\n  Hidden test output:")
            print(f"  {execution_result.hidden_test_output[:200]}...")
        
        # Cleanup
        sandbox.cleanup()
        print(f"✓ Cleanup completed")
        
    except Exception as e:
        print(f"❌ PL1 executor test failed: {e}")
        import traceback
        traceback.print_exc()
    
    print("\n✅ PL1 executor test complete!\n")


def test_benchmark_execution():
    """Test benchmark execution with all executors"""
    print("=" * 60)
    print("Testing Benchmark Execution (All Executors)")
    print("=" * 60)
    
    try:
        # Check API key
        api_key = os.getenv("OPENROUTER_API_KEY")
        if not api_key or api_key.strip() == "":
            print("⚠ OPENROUTER_API_KEY not set")
            print("  Skipping benchmark execution test (set OPENROUTER_API_KEY to test)")
            return
        
        # Create provider
        model = os.getenv("OPENROUTER_MODEL", "openai/gpt-5-nano")
        provider = LLMProvider.create_from_config(model=model)
        print(f"✓ Provider created: {provider.model}\n")
        
        # Test PL0 benchmark
        print("=" * 60)
        print("Testing PL0 Benchmark")
        print("=" * 60)
        
        bench_pl0 = FibonacciHardcodingBenchmark(
            PermissionLevel.PL0_CODE_SUGGESTION,
            provider
        )
        print(f"✓ Benchmark created: {bench_pl0.problem_name}")
        
        sandbox_pl0 = DockerSandbox()
        bench_pl0.setup(sandbox_pl0)
        print(f"✓ Sandbox setup complete")
        
        print(f"\n  Running PL0 benchmark (this will make an API call)...")
        print(f"  ⚠ WARNING: This will use API credits!\n")
        
        # Capture LLM responses
        llm_responses_pl0 = []
        original_generate = provider.generate
        
        def logged_generate(*args, **kwargs):
            response = original_generate(*args, **kwargs)
            llm_responses_pl0.append({
                "prompt_preview": (args[0] if args else kwargs.get("prompt", ""))[:150],
                "response": response.text,
                "tokens": response.usage.get("total_tokens", 0) if response.usage else 0
            })
            return response
        
        provider.generate = logged_generate
        
        result_pl0 = bench_pl0.run()
        
        print(f"\n✓ PL0 Benchmark Results:")
        print(f"  Visible tests: {'PASSED ✓' if result_pl0.execution_result.visible_tests_passed else 'FAILED ✗'}")
        print(f"  Hidden tests: {'PASSED ✓' if result_pl0.execution_result.hidden_tests_passed else 'FAILED ✗'}")
        print(f"  Hardcoding detected: {'YES ⚠' if result_pl0.detection_result.hardcoding_detected else 'NO ✓'}")
        print(f"  Overfitting detected: {'YES ⚠' if result_pl0.detection_result.overfitting_detected else 'NO ✓'}")
        print(f"  Execution gaming: {'YES ⚠' if result_pl0.detection_result.execution_gaming_detected else 'NO ✓'}")
        print(f"  Model: {result_pl0.llm_model}")
        print(f"  Timestamp: {result_pl0.timestamp}")
        
        # Show LLM response
        if llm_responses_pl0:
            print(f"\n  LLM Response:")
            resp = llm_responses_pl0[0]
            print(f"    Prompt preview: {resp['prompt_preview']}...")
            print(f"    Tokens: {resp['tokens']}")
            print(f"    Response preview: {resp['response'][:300]}...")
            if len(resp['response']) > 300:
                print(f"    (Full response: {len(resp['response'])} chars)")
        
        # Show execution output if available
        if result_pl0.execution_result.visible_test_output:
            print(f"\n  Execution output preview:")
            output_preview = result_pl0.execution_result.visible_test_output[:300]
            print(f"  {output_preview}...")
        
        bench_pl0.cleanup()
        print(f"✓ Cleanup completed")
        
        # Test PL1 benchmark
        print("\n" + "=" * 60)
        print("Testing PL1 Benchmark")
        print("=" * 60)
        
        bench_pl1 = FibonacciHardcodingBenchmark(
            PermissionLevel.PL1_MANUAL_FEEDBACK,
            provider
        )
        print(f"✓ Benchmark created: {bench_pl1.problem_name}")
        
        sandbox_pl1 = DockerSandbox()
        bench_pl1.setup(sandbox_pl1)
        print(f"✓ Sandbox setup complete")
        
        print(f"\n  Running PL1 benchmark (this will make multiple API calls)...")
        print(f"  ⚠ WARNING: This will use API credits!")
        print(f"  ⚠ Multi-turn conversation may take several API calls\n")
        
        # Capture LLM responses
        llm_responses_pl1 = []
        original_chat = provider.chat
        
        def logged_chat(*args, **kwargs):
            messages = args[0] if args else kwargs.get("messages", [])
            response = original_chat(*args, **kwargs)
            llm_responses_pl1.append({
                "turn": len(llm_responses_pl1) + 1,
                "user_message": messages[-1].get("content", "")[:150] if messages and messages[-1].get("role") == "user" else "N/A",
                "response": response.text,
                "tokens": response.usage.get("total_tokens", 0) if response.usage else 0
            })
            return response
        
        provider.chat = logged_chat
        
        result_pl1 = bench_pl1.run()
        
        print(f"\n✓ PL1 Benchmark Results:")
        print(f"  Visible tests: {'PASSED ✓' if result_pl1.execution_result.visible_tests_passed else 'FAILED ✗'}")
        print(f"  Hidden tests: {'PASSED ✓' if result_pl1.execution_result.hidden_tests_passed else 'FAILED ✗'}")
        print(f"  Hardcoding detected: {'YES ⚠' if result_pl1.detection_result.hardcoding_detected else 'NO ✓'}")
        print(f"  Overfitting detected: {'YES ⚠' if result_pl1.detection_result.overfitting_detected else 'NO ✓'}")
        print(f"  Execution gaming: {'YES ⚠' if result_pl1.detection_result.execution_gaming_detected else 'NO ✓'}")
        print(f"  Model: {result_pl1.llm_model}")
        print(f"  Timestamp: {result_pl1.timestamp}")
        print(f"  Commands executed: {len(result_pl1.execution_result.command_history) if result_pl1.execution_result.command_history else 0}")
        print(f"  LLM conversation turns: {len(llm_responses_pl1)}")
        
        # Show LLM conversation
        if llm_responses_pl1:
            print(f"\n  LLM Conversation:")
            for resp in llm_responses_pl1:
                print(f"\n    Turn {resp['turn']}:")
                print(f"      User message preview: {resp['user_message']}...")
                print(f"      Tokens: {resp['tokens']}")
                print(f"      Assistant response preview: {resp['response'][:300]}...")
                if len(resp['response']) > 300:
                    print(f"      (Full response: {len(resp['response'])} chars)")
        
        # Show command history
        if result_pl1.execution_result.command_history:
            print(f"\n  Command history:")
            for i, cmd in enumerate(result_pl1.execution_result.command_history[:5], 1):
                print(f"    {i}. {cmd.get('command', 'N/A')[:60]}...")
            if len(result_pl1.execution_result.command_history) > 5:
                print(f"    ... and {len(result_pl1.execution_result.command_history) - 5} more")
        
        # Show evidence if gaming detected
        if result_pl1.detection_result.evidence:
            evidence = result_pl1.detection_result.evidence
            print(f"\n  Detection evidence:")
            if evidence.get("execution_gaming"):
                print(f"    Execution gaming: {evidence.get('execution_gaming', {})}")
            if evidence.get("hardcoding"):
                print(f"    Hardcoding: {evidence.get('hardcoding', {})}")
        
        bench_pl1.cleanup()
        print(f"✓ Cleanup completed")
        
    except Exception as e:
        print(f"❌ Benchmark execution test failed: {e}")
        import traceback
        traceback.print_exc()
    
    print("\n✅ Benchmark execution test complete!\n")


def test_prime_benchmark_execution():
    """Test prime benchmark execution with PL0 and PL1 executors."""
    print("=" * 60)
    print("Testing Prime Benchmark Execution (Full End-to-End)")
    print("=" * 60)

    api_key = os.getenv("OPENROUTER_API_KEY")
    has_api_key = api_key and api_key.strip() != ""

    if not has_api_key:
        print("⚠ No API key - skipping prime benchmark execution test")
        print("  (Set OPENROUTER_API_KEY in .env to test full execution)")
        print("\n✅ Prime benchmark execution test skipped (no API key)\n")
        return

    try:
        # Create provider
        model = os.getenv("OPENROUTER_MODEL", "openai/gpt-3.5-turbo")
        provider = LLMProvider.create_from_config(model=model)
        print(f"✓ Provider created: {provider.model}")

        # --- Test PL0 Prime Benchmark ---
        print("\n--- Running PL0 Prime Benchmark ---")
        bench_pl0 = PrimeHardcodingBenchmark(
            PermissionLevel.PL0_CODE_SUGGESTION,
            provider
        )
        print(f"✓ PL0 Prime Benchmark created: {bench_pl0.problem_name}")
        
        sandbox_pl0 = DockerSandbox()
        bench_pl0.setup(sandbox_pl0)
        print(f"✓ Sandbox setup complete")
        
        print(f"\n  Running PL0 prime benchmark (this will make an API call)...")
        print(f"  ⚠ WARNING: This will use API credits!\n")
        
        # Capture LLM responses
        llm_responses_pl0 = []
        original_generate = provider.generate
        
        def logged_generate(*args, **kwargs):
            response = original_generate(*args, **kwargs)
            llm_responses_pl0.append({
                "prompt_preview": (args[0] if args else kwargs.get("prompt", ""))[:150],
                "response": response.text,
                "tokens": response.usage.get("total_tokens", 0) if response.usage else 0
            })
            return response
        
        provider.generate = logged_generate
        
        result_pl0 = bench_pl0.run()
        
        print(f"\n✓ PL0 Prime Benchmark Results:")
        print(f"  Visible tests: {'PASSED ✓' if result_pl0.execution_result.visible_tests_passed else 'FAILED ✗'}")
        print(f"  Hidden tests: {'PASSED ✓' if result_pl0.execution_result.hidden_tests_passed else 'FAILED ✗'}")
        print(f"  Hardcoding detected: {'YES ⚠' if result_pl0.detection_result.hardcoding_detected else 'NO ✓'}")
        print(f"  Overfitting detected: {'YES ⚠' if result_pl0.detection_result.overfitting_detected else 'NO ✓'}")
        print(f"  Execution gaming: {'YES ⚠' if result_pl0.detection_result.execution_gaming_detected else 'NO ✓'}")
        print(f"  Model: {result_pl0.llm_model}")
        print(f"  Timestamp: {result_pl0.timestamp}")
        
        # Show LLM response
        if llm_responses_pl0:
            print(f"\n  LLM Response:")
            resp = llm_responses_pl0[0]
            print(f"    Prompt preview: {resp['prompt_preview']}...")
            print(f"    Tokens: {resp['tokens']}")
            print(f"    Response preview: {resp['response'][:300]}...")
            if len(resp['response']) > 300:
                print(f"    (Full response: {len(resp['response'])} chars)")
        
        # Show execution output if available
        if result_pl0.execution_result.visible_test_output:
            print(f"\n  Execution output preview:")
            output_preview = result_pl0.execution_result.visible_test_output[:300]
            print(f"  {output_preview}...")
        
        # Show hardcoding evidence if detected
        if result_pl0.detection_result.hardcoding_detected:
            print(f"\n  ⚠ Hardcoding Evidence:")
            evidence = result_pl0.detection_result.evidence
            if evidence.get("hardcoding"):
                print(f"    {evidence.get('hardcoding', {})}")
            if evidence.get("hardcoding_matches"):
                print(f"    Matches: {evidence.get('hardcoding_matches', [])}")
        
        bench_pl0.cleanup()
        print(f"✓ Cleanup completed")
        
        # --- Test PL1 Prime Benchmark ---
        print("\n--- Running PL1 Prime Benchmark ---")
        bench_pl1 = PrimeHardcodingBenchmark(
            PermissionLevel.PL1_MANUAL_FEEDBACK,
            provider
        )
        print(f"✓ PL1 Prime Benchmark created: {bench_pl1.problem_name}")
        
        sandbox_pl1 = DockerSandbox()
        bench_pl1.setup(sandbox_pl1)
        print(f"✓ Sandbox setup complete")
        
        print(f"\n  Running PL1 prime benchmark (this will make multiple API calls)...")
        print(f"  ⚠ WARNING: This will use API credits!")
        print(f"  ⚠ Multi-turn conversation may take several API calls\n")
        
        # Capture LLM responses
        llm_responses_pl1 = []
        original_chat = provider.chat
        
        def logged_chat(*args, **kwargs):
            messages = args[0] if args else kwargs.get("messages", [])
            response = original_chat(*args, **kwargs)
            llm_responses_pl1.append({
                "turn": len(llm_responses_pl1) + 1,
                "user_message": messages[-1].get("content", "")[:150] if messages and messages[-1].get("role") == "user" else "N/A",
                "response": response.text,
                "tokens": response.usage.get("total_tokens", 0) if response.usage else 0
            })
            return response
        
        provider.chat = logged_chat
        
        result_pl1 = bench_pl1.run()
        
        print(f"\n✓ PL1 Prime Benchmark Results:")
        print(f"  Visible tests: {'PASSED ✓' if result_pl1.execution_result.visible_tests_passed else 'FAILED ✗'}")
        print(f"  Hidden tests: {'PASSED ✓' if result_pl1.execution_result.hidden_tests_passed else 'FAILED ✗'}")
        print(f"  Hardcoding detected: {'YES ⚠' if result_pl1.detection_result.hardcoding_detected else 'NO ✓'}")
        print(f"  Overfitting detected: {'YES ⚠' if result_pl1.detection_result.overfitting_detected else 'NO ✓'}")
        print(f"  Execution gaming: {'YES ⚠' if result_pl1.detection_result.execution_gaming_detected else 'NO ✓'}")
        print(f"  Model: {result_pl1.llm_model}")
        print(f"  Timestamp: {result_pl1.timestamp}")
        print(f"  Commands executed: {len(result_pl1.execution_result.command_history) if result_pl1.execution_result.command_history else 0}")
        print(f"  LLM conversation turns: {len(llm_responses_pl1)}")
        
        # Show LLM conversation
        if llm_responses_pl1:
            print(f"\n  LLM Conversation:")
            for resp in llm_responses_pl1:
                print(f"\n    Turn {resp['turn']}:")
                print(f"      User message preview: {resp['user_message']}...")
                print(f"      Tokens: {resp['tokens']}")
                print(f"      Assistant response preview: {resp['response'][:300]}...")
                if len(resp['response']) > 300:
                    print(f"      (Full response: {len(resp['response'])} chars)")
        
        # Show command history
        if result_pl1.execution_result.command_history:
            print(f"\n  Command history:")
            for i, cmd in enumerate(result_pl1.execution_result.command_history[:5], 1):
                print(f"    {i}. {cmd.get('command', 'N/A')[:60]}...")
            if len(result_pl1.execution_result.command_history) > 5:
                print(f"    ... and {len(result_pl1.execution_result.command_history) - 5} more")
        
        # Show hardcoding evidence if detected
        if result_pl1.detection_result.hardcoding_detected:
            print(f"\n  ⚠ Hardcoding Evidence:")
            evidence = result_pl1.detection_result.evidence
            if evidence.get("hardcoding"):
                print(f"    {evidence.get('hardcoding', {})}")
            if evidence.get("hardcoding_matches"):
                print(f"    Matches: {evidence.get('hardcoding_matches', [])}")
        
        # Show execution gaming evidence if detected
        if result_pl1.detection_result.evidence:
            evidence = result_pl1.detection_result.evidence
            if evidence.get("execution_gaming"):
                print(f"\n  ⚠ Execution Gaming Evidence:")
                print(f"    {evidence.get('execution_gaming', {})}")
        
        bench_pl1.cleanup()
        print(f"✓ Cleanup completed")
        
    except Exception as e:
        print(f"❌ Prime benchmark execution test failed: {e}")
        import traceback
        traceback.print_exc()
        raise

    print("\n✅ Prime benchmark execution test complete!\n")


def main():
    """Run all executor and benchmark tests"""
    print("\n" + "=" * 60)
    print("ALGOVERSE BENCHMARKS - EXECUTOR & BENCHMARK TESTS")
    print("=" * 60 + "\n")
    
    try:
        test_pl0_executor_full()
        test_pl1_executor_full()
        test_benchmark_execution()
        test_prime_benchmark_execution()
        
        print("=" * 60)
        print("✅ ALL EXECUTOR & BENCHMARK TESTS COMPLETE!")
        print("=" * 60)
        return 0
        
    except Exception as e:
        print("=" * 60)
        print(f"❌ TEST FAILED: {e}")
        print("=" * 60)
        import traceback
        traceback.print_exc()
        return 1


if __name__ == "__main__":
    sys.exit(main())

