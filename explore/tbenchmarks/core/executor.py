"""
Base Executor interface for permission-level executors.

Each permission level has its own executor implementation that
handles LLM interactions and code execution at that level.
"""

from abc import ABC, abstractmethod
from typing import Dict, Any

from .sandbox import DockerSandbox
from .results import ExecutionResult, PermissionLevel
from .problem import Problem
from ..llm_providers.provider import LLMProvider


class BenchmarkExecutor(ABC):
    """
    Base class for permission-level executors.
    
    Each executor handles LLM interactions and code execution
    for a specific permission level.
    """
    
    def __init__(
        self, 
        permission_level: PermissionLevel,
        llm_provider: LLMProvider
    ):
        """
        Args:
            permission_level: Permission level this executor handles
            llm_provider: LLM provider to use
        """
        self.permission_level = permission_level
        self.llm_provider = llm_provider
    
    @abstractmethod
    def execute(
        self, 
        problem: Problem, 
        sandbox: DockerSandbox
    ) -> ExecutionResult:
        """
        Execute the benchmark with the LLM.
        
        Args:
            problem: Problem to solve
            sandbox: Sandbox environment
        
        Returns:
            ExecutionResult with test results
        """
        pass

