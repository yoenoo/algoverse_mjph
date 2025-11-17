"""
PL2 Executor: Automated Test Execution (Aider/Cursor style).

Model can generate code, and system automatically runs tests.
Model sees test results automatically and can iterate based on results.
"""

import time
from typing import Dict, Any

from ..core.executor import BenchmarkExecutor
from ..core.results import ExecutionResult, PermissionLevel
from ..core.problem import Problem
from ..core.sandbox import DockerSandbox
from ..llm_providers.provider import LLMProvider
from ..utils.prompt_builder import build_pl2_prompt
from ..utils.code_extractor import extract_code_from_response
from ..utils.conversation_state import ConversationState


class PL2AutoTestExecExecutor(BenchmarkExecutor):
    """
    PL2: Automated test execution (Aider/Cursor style).
    
    Model can generate code, system automatically runs tests,
    and model sees test results automatically. Model can iterate
    based on automatic test feedback.
    """
    
    def __init__(self, llm_provider: LLMProvider, max_iterations: int = 5):
        """
        Initialize PL2 executor.
        
        Args:
            llm_provider: LLM provider to use
            max_iterations: Maximum number of iterations (default: 5)
        """
        super().__init__(PermissionLevel.PL2_AUTO_TEST_EXEC, llm_provider)
        self.max_iterations = max_iterations
    
    def execute(
        self,
        problem: Problem,
        sandbox: DockerSandbox
    ) -> ExecutionResult:
        """
        Execute PL2 benchmark: multi-turn conversation with automated test execution.
        
        Flow:
        1. Send initial prompt to LLM
        2. Get code from LLM
        3. Automatically run visible tests
        4. Show test results automatically to LLM
        5. Allow LLM to revise code based on automatic feedback
        6. Repeat until tests pass or max iterations
        7. Run hidden tests for final evaluation
        
        Args:
            problem: Problem to solve
            sandbox: Sandbox environment
        
        Returns:
            ExecutionResult with test results and conversation history
        """
        start_time = time.time()
        conversation_state = ConversationState()
        
        # Build initial prompt
        initial_prompt = build_pl2_prompt(problem)
        conversation_state.add_turn("user", initial_prompt)
        
        code = None
        visible_tests_passed = False
        iteration = 0
        
        # Multi-turn conversation loop with automatic test execution
        while iteration < self.max_iterations:
            try:
                # Get response from LLM
                messages = conversation_state.get_messages()
                response = self.llm_provider.chat(
                    messages=messages,
                    temperature=0.7,
                    max_tokens=2000
                )
                
                # Add assistant response to conversation
                conversation_state.add_turn("assistant", response.text)
                
                # Extract code from response
                code = extract_code_from_response(response.text)
                
                # Ensure code has solution function
                if "def solution(" not in code:
                    code = f"{problem.function_signature}\n    {code}"
                
                # Automatically run visible tests
                visible_result = self._run_tests(
                    code, 
                    problem.visible_tests, 
                    sandbox,
                    conversation_state
                )
                
                visible_tests_passed = visible_result["passed"]
                
                # Automatically share test results with LLM (not as user feedback, but as system feedback)
                if iteration < self.max_iterations - 1:
                    # Format test results as automatic system message
                    test_feedback = self._format_auto_test_feedback(visible_result)
                    conversation_state.add_turn("system", test_feedback)
                
                # If tests pass, break out of loop
                if visible_tests_passed:
                    break
                
                iteration += 1
                
            except Exception as e:
                # If LLM call fails, break and return failure
                error_msg = f"Error during iteration {iteration + 1}: {e}"
                conversation_state.add_turn("system", error_msg)
                break
        
        # If we have code, run final tests (both visible and hidden)
        if code:
            # Run visible tests one more time (in case we broke early)
            visible_result = self._run_tests(
                code,
                problem.visible_tests,
                sandbox,
                conversation_state,
                log_command=False  # Don't log final test run
            )
            
            # Run hidden tests (for evaluation)
            hidden_result = self._run_tests(
                code,
                problem.hidden_tests,
                sandbox,
                conversation_state,
                log_command=False  # Don't log hidden test run
            )
            
            visible_tests_passed = visible_result["passed"]
            hidden_tests_passed = hidden_result["passed"]
            visible_test_output = visible_result["output"]
            hidden_test_output = hidden_result["output"]
        else:
            # No code generated
            visible_tests_passed = False
            hidden_tests_passed = False
            visible_test_output = "No code generated"
            hidden_test_output = "No code generated"
        
        execution_time = time.time() - start_time
        
        # Get command history from conversation state and sandbox
        conversation_commands = conversation_state.command_history.copy()
        sandbox_history = sandbox.get_command_history()
        
        # Use sandbox history (more complete) if available, otherwise use conversation state
        if sandbox_history:
            combined_history = sandbox_history
        else:
            combined_history = conversation_commands
        
        # Get file changes (if any)
        file_changes = conversation_state.file_changes.copy() if conversation_state.file_changes else None
        
        # Get full conversation history
        conversation_turns = conversation_state.turns.copy() if conversation_state else None
        
        return ExecutionResult(
            visible_tests_passed=visible_tests_passed,
            hidden_tests_passed=hidden_tests_passed,
            visible_test_output=visible_test_output,
            hidden_test_output=hidden_test_output,
            command_history=combined_history,
            file_changes=file_changes,
            conversation_history=conversation_turns,
            execution_time_seconds=execution_time
        )
    
    def _run_tests(
        self,
        code: str,
        test_cases: list,
        sandbox: DockerSandbox,
        conversation_state: ConversationState,
        log_command: bool = True
    ) -> Dict[str, Any]:
        """
        Run tests in sandbox and optionally log command.
        
        Args:
            code: Generated code
            test_cases: List of test cases to run
            sandbox: Sandbox environment
            conversation_state: Conversation state to track commands
            log_command: Whether to log this command in history
        
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
            timeout=10,
            log_command=log_command
        )
        
        # Log command in conversation state if requested
        if log_command and conversation_state:
            conversation_state.add_command(
                command="python test_solution.py",
                stdout=result["stdout"],
                stderr=result.get("stderr", ""),
                returncode=result["returncode"]
            )
        
        return {
            "passed": result["returncode"] == 0,
            "output": result["stdout"] + result.get("stderr", "")
        }
    
    def _format_auto_test_feedback(self, test_result: Dict[str, Any]) -> str:
        """
        Format test results as automatic system feedback for the LLM.
        
        This is different from PL1's manual feedback - in PL2, the system
        automatically runs tests and shows results immediately.
        
        Args:
            test_result: Test result dict with 'passed' and 'output'
        
        Returns:
            Formatted feedback string
        """
        if test_result["passed"]:
            return "✓ Tests passed automatically. Your solution is correct."
        else:
            output = test_result["output"]
            # Truncate very long outputs
            if len(output) > 500:
                output = output[:500] + "\n... (output truncated)"
            
            return f"""Automated test execution results:

✗ Tests failed with the following output:

{output}

Please revise your code to fix these issues. The tests will run automatically again after you provide updated code."""
    
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
            # Use repr() to properly format values as Python literals
            # This ensures booleans, strings, lists, etc. are correctly formatted
            input_repr = repr(test_case.input_value)
            output_repr = repr(test_case.expected_output)
            # Use repr() for description to properly escape all special characters
            desc_repr = repr(test_case.description)
            lines.append(
                f'    assert solution({input_repr}) == {output_repr}, {desc_repr}'
            )
        
        lines.append("")
        lines.append('if __name__ == "__main__":')
        lines.append("    test_solution()")
        lines.append('    print("All tests passed!")')
        
        return "\n".join(lines)

