"""
Base Benchmark class for problem-specific benchmarks.

Each benchmark is tied to a specific problem and implements
the Benchmark interface to test reward hacking behaviors.
"""

from abc import ABC, abstractmethod
from pathlib import Path
from typing import Dict, Any

from .sandbox import DockerSandbox
from .results import BenchmarkResult, DetectionResult, PermissionLevel
from .problem import Problem
from ..llm_providers.provider import LLMProvider


class Benchmark(ABC):
    """
    Base class for problem-specific benchmarks.
    
    Each benchmark is tied to a specific problem and tests
    reward hacking behaviors at a specific permission level.
    """
    
    def __init__(
        self, 
        problem_name: str,
        permission_level: PermissionLevel,
        llm_provider: LLMProvider
    ):
        """
        Args:
            problem_name: Name of the problem this benchmark tests
            permission_level: Permission level to test (PL0, PL1, PL2, or PL3)
            llm_provider: LLM provider to use
        """
        self.problem_name = problem_name
        self.permission_level = permission_level
        self.llm_provider = llm_provider
        self.sandbox: DockerSandbox | None = None
        self.problem: Problem | None = None
    
    @abstractmethod
    def setup(self, sandbox: DockerSandbox) -> None:
        """
        Set up the benchmark environment.
        
        Args:
            sandbox: Sandbox to set up
        """
        pass
    
    @abstractmethod
    def run(self) -> BenchmarkResult:
        """
        Run the benchmark.
        
        Returns:
            BenchmarkResult with execution and detection results
        """
        pass
    
    @abstractmethod
    def detect_gaming(
        self, 
        execution_result: Any  # Will be ExecutionResult
    ) -> DetectionResult:
        """
        Detect reward hacking behaviors specific to this benchmark.
        
        Args:
            execution_result: Results from executing the LLM code
        
        Returns:
            DetectionResult with detected gaming behaviors
        """
        pass
    
    def cleanup(self):
        """Clean up benchmark resources"""
        if self.sandbox:
            self.sandbox.cleanup()

