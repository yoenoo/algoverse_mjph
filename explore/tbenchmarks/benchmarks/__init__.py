"""
Benchmark implementations (problem-specific).

Each benchmark is tied to a specific problem and tests reward hacking behaviors.
"""

from .fibonacci_hardcoding import FibonacciHardcodingBenchmark
from .prime_hardcoding import PrimeHardcodingBenchmark

__all__ = ["FibonacciHardcodingBenchmark", "PrimeHardcodingBenchmark"]

