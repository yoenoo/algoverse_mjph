"""
PL0 Executor: Code Suggestion Only (GitHub Copilot style).

Model receives problem description and visible tests, but cannot
execute code or see results. Single attempt, no feedback loop.
"""

import time
from typing import Dict, Any

from ..core.executor import BenchmarkExecutor
from ..core.results import ExecutionResult, PermissionLevel
from ..core.problem import Problem
from ..core.sandbox import DockerSandbox
from ..llm_providers.provider import LLMProvider
from ..utils.prompt_builder import build_pl0_prompt
from ..utils.code_extractor import extract_code_from_response


class PL0CodeSuggestionExecutor(BenchmarkExecutor):
    """
    PL0: Code suggestion only (GitHub Copilot style).
    
    Model receives problem description and visible tests, returns code.
    No execution visibility, no feedback loop, single attempt.
    """
    
    def __init__(self, llm_provider: LLMProvider):
        super().__init__(PermissionLevel.PL0_CODE_SUGGESTION, llm_provider)
    
    def execute(
        self,
        problem: Problem,
        sandbox: DockerSandbox
    ) -> ExecutionResult:
        """
        Execute PL0 benchmark: get code from LLM, run tests.
        
        Args:
            problem: Problem to solve
            sandbox: Sandbox environment
        
        Returns:
            ExecutionResult with test results
        """
        start_time = time.time()
        
        # Build prompt
        prompt = build_pl0_prompt(problem)
        
        # Get code from LLM (single call, no feedback)
        try:
            response = self.llm_provider.generate(
                prompt=prompt,
                temperature=0.7,
                max_tokens=2000
            )
            
            # Extract code from response
            code = extract_code_from_response(response.text)
            
            # Ensure code has solution function
            if "def solution(" not in code:
                # Add function signature if missing
                code = f"{problem.function_signature}\n    {code}"
            
        except Exception as e:
            # If LLM call fails, return failure result
            return ExecutionResult(
                visible_tests_passed=False,
                hidden_tests_passed=False,
                visible_test_output=f"LLM call failed: {e}",
                hidden_test_output=f"LLM call failed: {e}",
                command_history=None,
                file_changes=None,
                execution_time_seconds=time.time() - start_time
            )
        
        # Run tests in sandbox
        visible_result = self._run_tests(code, problem.visible_tests, sandbox)
        hidden_result = self._run_tests(code, problem.hidden_tests, sandbox)
        
        execution_time = time.time() - start_time
        
        return ExecutionResult(
            visible_tests_passed=visible_result["passed"],
            hidden_tests_passed=hidden_result["passed"],
            visible_test_output=visible_result["output"],
            hidden_test_output=hidden_result["output"],
            command_history=None,  # No commands for PL0
            file_changes=None,  # No file changes for PL0
            execution_time_seconds=execution_time
        )
    
    def _run_tests(
        self,
        code: str,
        test_cases: list,
        sandbox: DockerSandbox
    ) -> Dict[str, Any]:
        """
        Run tests in sandbox.
        
        Args:
            code: Generated code
            test_cases: List of test cases to run
            sandbox: Sandbox environment
        
        Returns:
            Dict with 'passed' (bool) and 'output' (str)
        """
        # Write code to sandbox
        sandbox.write_file("solution.py", code)
        
        # Create test file
        test_content = self._create_test_file(test_cases)
        sandbox.write_file("test_solution.py", test_content)
        
        # Run tests
        result = sandbox.execute_command(
            "python test_solution.py",
            timeout=10
        )
        
        return {
            "passed": result["returncode"] == 0,
            "output": result["stdout"] + result["stderr"]
        }
    
    def _create_test_file(self, test_cases: list) -> str:
        """
        Create test file from test cases.
        
        Args:
            test_cases: List of TestCase objects
        
        Returns:
            Test file content as string
        """
        lines = [
            "from solution import solution",
            "",
            "def test_solution():",
        ]
        
        for test_case in test_cases:
            lines.append(
                f'    assert solution({test_case.input_value}) == {test_case.expected_output}, '
                f'"{test_case.description}"'
            )
        
        lines.append("")
        lines.append('if __name__ == "__main__":')
        lines.append("    test_solution()")
        lines.append('    print("All tests passed!")')
        
        return "\n".join(lines)

