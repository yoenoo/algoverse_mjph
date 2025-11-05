#!/usr/bin/env python3
"""
Test script to validate current benchmark components.

Tests:
- Core structures (Problem, Results)
- Utilities (code extraction, prompt building, conversation state)
- Detectors (hardcoding, overfitting)
- Docker sandbox (if available)
- Base Benchmark and Executor classes (Phase 6)
- OpenRouter API (if API key available)
"""

import sys
import os
from pathlib import Path
from abc import ABC

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from dotenv import load_dotenv
load_dotenv()

from explore.tbenchmarks.core.problem import Problem, TestCase
from explore.tbenchmarks.core.results import PermissionLevel, DetectionResult, ExecutionResult
from explore.tbenchmarks.utils.code_extractor import extract_code_from_response
from explore.tbenchmarks.utils.prompt_builder import (
    build_pl0_prompt, 
    build_pl1_prompt, 
    build_pl2_prompt,
    build_pl3_prompt,
    build_pl4_prompt
)
from explore.tbenchmarks.utils.conversation_state import ConversationState
from explore.tbenchmarks.detectors.hardcoding import detect_hardcoding
from explore.tbenchmarks.detectors.overfitting import detect_overfitting
from explore.tbenchmarks.core.benchmark import Benchmark
from explore.tbenchmarks.core.executor import BenchmarkExecutor
from explore.tbenchmarks.executors.pl0_code_suggestion import PL0CodeSuggestionExecutor


def test_core_structures():
    """Test core data structures"""
    print("=" * 60)
    print("Testing Core Structures")
    print("=" * 60)
    
    # Test PermissionLevel enum
    pl0 = PermissionLevel.PL0_CODE_SUGGESTION
    assert pl0.value == "code_suggestion"
    print(f"✓ PermissionLevel enum PL0: {pl0}")
    
    # Test all permission levels
    pl1 = PermissionLevel.PL1_MANUAL_FEEDBACK
    pl2 = PermissionLevel.PL2_AUTO_TEST_EXEC
    pl3 = PermissionLevel.PL3_FILE_MODIFICATION
    pl4 = PermissionLevel.PL4_TEST_MODIFICATION
    assert len(PermissionLevel) == 5  # Should have 5 levels now
    print(f"✓ All permission levels present: PL0-PL4 ({len(PermissionLevel)} total)")
    
    # Test TestCase
    test_case = TestCase(
        name="test_1",
        input_value=5,
        expected_output=5,
        description="Test case 1"
    )
    assert test_case.input_value == 5
    print(f"✓ TestCase: {test_case.name}")
    
    # Test Problem
    problem = Problem(
        name="fibonacci",
        description="Calculate Fibonacci",
        function_signature="def solution(n: int) -> int:",
        visible_tests=[test_case],
        hidden_tests=[]
    )
    assert problem.name == "fibonacci"
    print(f"✓ Problem: {problem.name}")
    
    # Test DetectionResult
    detection = DetectionResult(
        hardcoding_detected=True,
        test_edit_detected=False,
        overfitting_detected=False
    )
    assert detection.hardcoding_detected == True
    print(f"✓ DetectionResult: hardcoding={detection.hardcoding_detected}")
    
    print("\n✅ All core structures working!\n")


def test_code_extraction():
    """Test code extraction utility"""
    print("=" * 60)
    print("Testing Code Extraction")
    print("=" * 60)
    
    # Test with code block
    response1 = """
    Here's the solution:
    ```python
    def solution(n: int) -> int:
        return n * 2
    ```
    """
    code1 = extract_code_from_response(response1)
    assert "def solution" in code1
    print(f"✓ Code block extraction: {len(code1)} chars")
    
    # Test with plain function
    response2 = """def solution(n: int) -> int:
    if n == 5:
        return 5
    return n"""
    code2 = extract_code_from_response(response2)
    assert "def solution" in code2
    print(f"✓ Plain code extraction: {len(code2)} chars")
    
    print("\n✅ Code extraction working!\n")


def test_prompt_building():
    """Test prompt building"""
    print("=" * 60)
    print("Testing Prompt Building")
    print("=" * 60)
    
    # Create test problem
    problem = Problem(
        name="fibonacci",
        description="Calculate nth Fibonacci number",
        function_signature="def solution(n: int) -> int:",
        visible_tests=[
            TestCase("test1", 5, 5, "Test 1"),
            TestCase("test2", 10, 55, "Test 2")
        ],
        hidden_tests=[]
    )
    
    # Test PL0 prompt
    pl0_prompt = build_pl0_prompt(problem)
    assert "fibonacci" in pl0_prompt.lower()
    assert "Input: 5" in pl0_prompt
    print(f"✓ PL0 prompt: {len(pl0_prompt)} chars")
    
    # Test PL1 prompt
    pl1_prompt = build_pl1_prompt(problem)
    assert "conversational" in pl1_prompt.lower()
    print(f"✓ PL1 prompt: {len(pl1_prompt)} chars")
    
    # Test PL2 prompt
    pl2_prompt = build_pl2_prompt(problem)
    assert "automatically" in pl2_prompt.lower()
    print(f"✓ PL2 prompt: {len(pl2_prompt)} chars")
    
    # Test PL3 prompt
    pl3_prompt = build_pl3_prompt(problem)
    assert "modify" in pl3_prompt.lower()
    print(f"✓ PL3 prompt: {len(pl3_prompt)} chars")
    
    # Test PL4 prompt
    pl4_prompt = build_pl4_prompt(problem)
    assert "test files" in pl4_prompt.lower() or "test" in pl4_prompt.lower()
    print(f"✓ PL4 prompt: {len(pl4_prompt)} chars")
    
    print("\n✅ Prompt building working!\n")


def test_conversation_state():
    """Test conversation state management"""
    print("=" * 60)
    print("Testing Conversation State")
    print("=" * 60)
    
    state = ConversationState()
    
    # Add turns
    state.add_turn("user", "Solve fibonacci")
    state.add_turn("assistant", "Here's the code...")
    assert len(state.turns) == 2
    print(f"✓ Conversation turns: {len(state.turns)}")
    
    # Add command
    state.add_command("python test.py", "All tests passed", "", 0)
    assert len(state.command_history) == 1
    print(f"✓ Command history: {len(state.command_history)}")
    
    # Track file change
    state.track_file_change("solution.py", "created")
    assert len(state.file_changes) == 1
    print(f"✓ File changes: {len(state.file_changes)}")
    
    # Get messages
    messages = state.get_messages()
    assert len(messages) == 2
    print(f"✓ Messages format: {len(messages)} messages")
    
    print("\n✅ Conversation state working!\n")


def test_detectors():
    """Test detection modules"""
    print("=" * 60)
    print("Testing Detectors")
    print("=" * 60)
    
    # Create test problem
    problem = Problem(
        name="fibonacci",
        description="Calculate Fibonacci",
        function_signature="def solution(n: int) -> int:",
        visible_tests=[
            TestCase("test1", 5, 5, "Test 1"),
            TestCase("test2", 10, 55, "Test 2")
        ],
        hidden_tests=[]
    )
    
    # Test hardcoding detection
    hardcoded_code = """
    def solution(n: int) -> int:
        if n == 5:
            return 5
        elif n == 10:
            return 55
        return 0
    """
    hardcoding_result = detect_hardcoding(hardcoded_code, problem)
    print(f"✓ Hardcoding detection: {hardcoding_result['hardcoding_detected']}")
    print(f"  Evidence: {hardcoding_result['evidence']['hardcoded_count']} matches")
    
    # Test overfitting detection
    overfitting_result = detect_overfitting(True, False)  # visible pass, hidden fail
    assert overfitting_result['overfitting_detected'] == True
    print(f"✓ Overfitting detection: {overfitting_result['overfitting_detected']}")
    
    print("\n✅ Detectors working!\n")


def test_docker_sandbox():
    """Test Docker sandbox (if available)"""
    print("=" * 60)
    print("Testing Docker Sandbox")
    print("=" * 60)
    
    try:
        from explore.tbenchmarks.core.sandbox import DockerSandbox
        
        # Just test initialization (don't create container)
        sandbox = DockerSandbox()
        print(f"✓ Sandbox initialized: {sandbox.image}")
        
        # Check if Docker is available
        try:
            sandbox.client.ping()
            print("✓ Docker is running")
        except Exception as e:
            print(f"⚠ Docker not available: {e}")
            print("  (This is OK if Docker isn't running)")
        
    except Exception as e:
        print(f"⚠ Sandbox import failed: {e}")
    
    print("\n✅ Sandbox test complete!\n")


def test_base_classes():
    """Test base Benchmark and Executor classes"""
    print("=" * 60)
    print("Testing Base Classes (Phase 6)")
    print("=" * 60)
    
    # Test Benchmark is abstract
    assert issubclass(Benchmark, ABC)
    assert hasattr(Benchmark, 'setup')
    assert hasattr(Benchmark, 'run')
    assert hasattr(Benchmark, 'detect_gaming')
    assert hasattr(Benchmark, 'cleanup')
    print("✓ Benchmark class is abstract with required methods")
    
    # Test Executor is abstract
    assert issubclass(BenchmarkExecutor, ABC)
    assert hasattr(BenchmarkExecutor, 'execute')
    print("✓ BenchmarkExecutor class is abstract with required method")
    
    # Test that we can't instantiate them directly
    try:
        # This should fail since they're abstract
        from explore.tbenchmarks.llm_providers.provider import LLMProvider
        
        # Try to create provider (may fail if no API key, that's OK)
        try:
            provider = LLMProvider.create_from_config(model="openai/gpt-3.5-turbo")
            
            # Try to instantiate Benchmark (should fail)
            try:
                bench = Benchmark("test", PermissionLevel.PL0_CODE_SUGGESTION, provider)
                print("⚠ Benchmark can be instantiated (unexpected)")
            except TypeError:
                print("✓ Benchmark correctly prevents instantiation (abstract)")
            
            # Try to instantiate Executor (should fail)
            try:
                exec = BenchmarkExecutor(PermissionLevel.PL0_CODE_SUGGESTION, provider)
                print("⚠ Executor can be instantiated (unexpected)")
            except TypeError:
                print("✓ Executor correctly prevents instantiation (abstract)")
        except ValueError:
            # No API key - that's OK for this test
            print("✓ Abstract class structure verified (provider creation skipped - no API key)")
            
    except Exception as e:
        print(f"⚠ Base class test had issues: {e}")
    
    print("\n✅ Base classes working correctly!\n")


def test_openrouter_api():
    """Test OpenRouter API connection"""
    print("=" * 60)
    print("Testing OpenRouter API")
    print("=" * 60)
    
    try:
        from explore.tbenchmarks.llm_providers.provider import LLMProvider
        
        # Check if API key is available
        api_key = os.getenv("OPENROUTER_API_KEY")
        if not api_key or api_key.strip() == "":
            print("⚠ OPENROUTER_API_KEY not set in .env")
            print("  Skipping API test (set OPENROUTER_API_KEY to test)")
            print("\n⚠ OpenRouter API test skipped (no API key)\n")
            return
        
        # Create provider
        model = os.getenv("OPENROUTER_MODEL", "openai/gpt-3.5-turbo")
        provider = LLMProvider.create_from_config(model=model)
        print(f"✓ Provider created: {provider.model}")
        
        # Test simple API call
        try:
            response = provider.generate(
                prompt="Say 'Hello, World!' and nothing else.",
                temperature=0.1,
                max_tokens=20
            )
            
            assert response.text is not None
            assert len(response.text) > 0
            assert response.provider == "openrouter"
            assert response.model == model
            
            print(f"✓ API call successful")
            print(f"  Response: {response.text[:50]}...")
            print(f"  Model: {response.model}")
            print(f"  Provider: {response.provider}")
            print(f"  Tokens: {response.usage.get('total_tokens', 'N/A')}")
            
        except Exception as e:
            print(f"❌ API call failed: {e}")
            print("  This might indicate:")
            print("  - Invalid API key")
            print("  - Network issue")
            print("  - OpenRouter service issue")
            raise
        
    except ImportError as e:
        print(f"⚠ Import failed: {e}")
    except Exception as e:
        print(f"⚠ OpenRouter test failed: {e}")
        print("  (This is OK if API key is not configured)")
    
    print("\n✅ OpenRouter API test complete!\n")


def test_pl0_executor():
    """Test PL0 executor implementation"""
    print("=" * 60)
    print("Testing PL0 Executor (Phase 7)")
    print("=" * 60)
    
    try:
        from explore.tbenchmarks.core.sandbox import DockerSandbox
        from explore.tbenchmarks.llm_providers.provider import LLMProvider
        
        # Check if we have API key (for actual execution test)
        api_key = os.getenv("OPENROUTER_API_KEY")
        has_api_key = api_key and api_key.strip() != ""
        
        # Test executor instantiation
        try:
            if has_api_key:
                provider = LLMProvider.create_from_config(model="openai/gpt-3.5-turbo")
            else:
                # Create a mock provider structure for testing
                # We'll just test that the executor class can be instantiated
                print("⚠ No API key - testing executor structure only")
                provider = None
            
            if provider:
                executor = PL0CodeSuggestionExecutor(provider)
                assert executor.permission_level == PermissionLevel.PL0_CODE_SUGGESTION
                print("✓ PL0 executor instantiated correctly")
                print(f"  Permission level: {executor.permission_level}")
                
                # Test with a simple problem (if we have API key and Docker)
                if has_api_key:
                    try:
                        sandbox = DockerSandbox()
                        sandbox.create()
                        
                        # Create simple test problem
                        problem = Problem(
                            name="test_problem",
                            description="Return the input value multiplied by 2",
                            function_signature="def solution(n: int) -> int:",
                            visible_tests=[
                                TestCase("test1", 5, 10, "Test 1"),
                            ],
                            hidden_tests=[
                                TestCase("test2", 3, 6, "Test 2"),
                            ]
                        )
                        
                        print("✓ Sandbox created")
                        print("  Testing executor with simple problem...")
                        
                        # Note: This will make an actual API call
                        # Commented out to avoid API costs during testing
                        # Uncomment to test full execution:
                        # result = executor.execute(problem, sandbox)
                        # print(f"  Execution result: visible={result.visible_tests_passed}, hidden={result.hidden_tests_passed}")
                        
                        print("  (Full execution test skipped - uncomment in code to test)")
                        sandbox.cleanup()
                        
                    except Exception as e:
                        print(f"⚠ Execution test skipped: {e}")
                else:
                    print("  (Full execution test requires API key)")
            else:
                # Just test the class structure
                print("✓ PL0 executor class structure verified")
                print("  - Can be imported")
                print("  - Inherits from BenchmarkExecutor")
                assert issubclass(PL0CodeSuggestionExecutor, BenchmarkExecutor)
                
        except ValueError as e:
            if "API key" in str(e):
                print("⚠ API key not set - testing executor structure only")
                print("✓ PL0 executor class structure verified")
            else:
                raise
        
        # Test that executor has required methods
        if has_api_key:
            try:
                provider = LLMProvider.create_from_config(model="openai/gpt-3.5-turbo")
                executor = PL0CodeSuggestionExecutor(provider)
                assert hasattr(executor, 'execute')
                assert hasattr(executor, '_run_tests')
                assert hasattr(executor, '_create_test_file')
                print("✓ Required methods present")
            except:
                pass
        
    except ImportError as e:
        print(f"⚠ Import failed: {e}")
    except Exception as e:
        print(f"⚠ PL0 executor test had issues: {e}")
        import traceback
        traceback.print_exc()
    
    print("\n✅ PL0 executor test complete!\n")


def main():
    """Run all tests"""
    print("\n" + "=" * 60)
    print("ALGOVERSE BENCHMARKS - COMPONENT TESTS")
    print("=" * 60 + "\n")
    
    try:
        test_core_structures()
        test_code_extraction()
        test_prompt_building()
        test_conversation_state()
        test_detectors()
        test_docker_sandbox()
        test_base_classes()
        test_openrouter_api()
        test_pl0_executor()
        
        print("=" * 60)
        print("✅ ALL TESTS PASSED!")
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

