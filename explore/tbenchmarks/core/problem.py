"""
Problem definition structures (reusable across benchmarks).
"""

from dataclasses import dataclass
from typing import List, Any


@dataclass
class TestCase:
    """A single test case"""
    name: str
    input_value: Any
    expected_output: Any
    description: str = ""


@dataclass
class Problem:
    """A coding problem with test cases"""
    name: str
    description: str
    function_signature: str
    visible_tests: List[TestCase]
    hidden_tests: List[TestCase]

