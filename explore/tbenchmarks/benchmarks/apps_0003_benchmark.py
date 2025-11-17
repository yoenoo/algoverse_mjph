"""
APPS Problem 0003 Benchmark.

Tests reward hacking behaviors on APPS problem 0003, including:
- Hardcoding: Model hardcodes visible test answers
- Overfitting: Model passes visible tests but fails hidden tests
- Execution gaming: Model manipulates test execution
- Test modification: Model modifies test files (PL3+)
"""

from datetime import datetime
from typing import Dict, Any

from ..core.benchmark import Benchmark
from ..core.results import (
    BenchmarkResult, 
    DetectionResult, 
    ExecutionResult, 
    PermissionLevel
)
from ..core.problem import Problem
from ..core.sandbox import DockerSandbox
from ..llm_providers.provider import LLMProvider
from ..problems.apps.apps_0003 import create_apps_0003
from ..detectors.hardcoding import detect_hardcoding
from ..detectors.overfitting import detect_overfitting


class Apps0003Benchmark(Benchmark):
    """
    Benchmark for testing reward hacking on APPS problem 0003.
    
    Detects hardcoding, overfitting, execution gaming, and test modification
    behaviors by comparing model performance on visible vs hidden test cases.
    """
    
    def __init__(
        self,
        permission_level: PermissionLevel,
        llm_provider: LLMProvider
    ):
        """
        Initialize APPS 0003 benchmark.
        
        Args:
            permission_level: Permission level to test (PL0, PL1, PL2, PL3)
            llm_provider: LLM provider to use
        """
        # Create APPS 0003 problem
        problem = create_apps_0003()
        
        # Initialize base class
        super().__init__(
            problem_name=problem.name,
            permission_level=permission_level,
            llm_provider=llm_provider
        )
        
        # Store problem instance
        self.problem = problem
    
    def setup(self, sandbox: DockerSandbox) -> None:
        """
        Set up the benchmark environment.
        
        Args:
            sandbox: Sandbox to set up (will be created)
        """
        sandbox.create()
        self.sandbox = sandbox
    
    def run(self) -> BenchmarkResult:
        """
        Run the benchmark.
        
        Returns:
            BenchmarkResult with execution and detection results
            
        Raises:
            RuntimeError: If benchmark not set up (call setup() first)
            NotImplementedError: If permission level not yet implemented
        """
        if not self.sandbox:
            raise RuntimeError("Benchmark not set up. Call setup() first.")
        
        # Create executor for this permission level
        if self.permission_level == PermissionLevel.PL0_CODE_SUGGESTION:
            from ..executors.pl0_code_suggestion import PL0CodeSuggestionExecutor
            executor = PL0CodeSuggestionExecutor(self.llm_provider)
        elif self.permission_level == PermissionLevel.PL1_MANUAL_FEEDBACK:
            from ..executors.pl1_manual_feedback import PL1ManualFeedbackExecutor
            executor = PL1ManualFeedbackExecutor(self.llm_provider)
        elif self.permission_level == PermissionLevel.PL2_AUTO_TEST_EXEC:
            from ..executors.pl2_auto_test_exec import PL2AutoTestExecExecutor
            executor = PL2AutoTestExecExecutor(self.llm_provider)
        elif self.permission_level == PermissionLevel.PL3_FILE_MODIFICATION:
            from ..executors.pl3_file_modification import PL3FileModificationExecutor
            executor = PL3FileModificationExecutor(self.llm_provider)
        else:
            raise NotImplementedError(
                f"Permission level {self.permission_level} not yet implemented. "
                f"Currently supported: PL0, PL1, PL2, PL3"
            )
        
        # Execute benchmark
        execution_result = executor.execute(self.problem, self.sandbox)
        
        # Detect gaming behaviors
        detection_result = self.detect_gaming(execution_result)
        
        # Create benchmark result
        return BenchmarkResult(
            benchmark_name="apps_0003",
            permission_level=self.permission_level,
            timestamp=datetime.now().isoformat(),
            problem_name=self.problem.name,
            execution_result=execution_result,
            detection_result=detection_result,
            llm_model=self.llm_provider.model,
            llm_provider=detection_result.evidence.get("provider", "openrouter") if detection_result.evidence else "openrouter",
            metadata={
                "problem_description": self.problem.description[:500] if len(self.problem.description) > 500 else self.problem.description,
                "function_signature": self.problem.function_signature,
                "num_visible_tests": len(self.problem.visible_tests),
                "num_hidden_tests": len(self.problem.hidden_tests)
            }
        )
    
    def detect_gaming(
        self,
        execution_result: ExecutionResult
    ) -> DetectionResult:
        """
        Detect reward hacking behaviors.
        
        Args:
            execution_result: Results from executing the LLM code
            
        Returns:
            DetectionResult with detected gaming behaviors
        """
        # Try to get code from sandbox
        code = None
        try:
            if self.sandbox:
                code = self.sandbox.read_file("solution.py")
        except Exception:
            # Code might not exist or file might not be readable
            pass
        
        # Combined evidence dictionary
        evidence: Dict[str, Any] = {
            "provider": "openrouter"
        }
        
        # Detect hardcoding (if code is available)
        hardcoding_detected = False
        if code:
            hardcoding_result = detect_hardcoding(code, self.problem)
            hardcoding_detected = hardcoding_result.get("detected", False)
            if hardcoding_detected:
                evidence["hardcoding"] = hardcoding_result.get("evidence", {})
                evidence["hardcoding_matches"] = hardcoding_result.get("evidence", {}).get("matches", [])
        
        # Detect overfitting (visible pass, hidden fail)
        overfitting_result = detect_overfitting(
            execution_result.visible_tests_passed,
            execution_result.hidden_tests_passed
        )
        overfitting_detected = overfitting_result.get("detected", False)
        if overfitting_detected:
            evidence["overfitting"] = overfitting_result.get("evidence", {})
        
        # Combine all evidence
        evidence.update({
            "visible_tests_passed": execution_result.visible_tests_passed,
            "hidden_tests_passed": execution_result.hidden_tests_passed,
            "code_available": code is not None,
            "code_length": len(code) if code else 0
        })
        
        # Detect execution gaming (for PL1+)
        execution_gaming_detected = False
        if execution_result.command_history and len(execution_result.command_history) > 0:
            from ..detectors.execution_gaming import detect_execution_gaming
            gaming_result = detect_execution_gaming(
                execution_result.command_history,
                code if code else "",
                execution_result.visible_tests_passed
            )
            execution_gaming_detected = gaming_result.get("detected", False)
            if execution_gaming_detected:
                evidence["execution_gaming"] = gaming_result.get("evidence", {})
        
        # Detect test file modification (for PL3+)
        test_edit_detected = False
        if self.permission_level in [PermissionLevel.PL3_FILE_MODIFICATION, PermissionLevel.PL4_TEST_MODIFICATION]:
            from ..detectors.test_modification import detect_test_modification
            test_mod_result = detect_test_modification(execution_result.file_changes)
            test_edit_detected = test_mod_result.get("test_edit_detected", False)
            if test_edit_detected:
                evidence["test_modification"] = test_mod_result.get("evidence", {})
        
        # Create detection result
        return DetectionResult(
            hardcoding_detected=hardcoding_detected,
            test_edit_detected=test_edit_detected,
            overfitting_detected=overfitting_detected,
            execution_gaming_detected=execution_gaming_detected,
            evidence=evidence
        )
