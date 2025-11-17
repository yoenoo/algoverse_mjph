"""
Benchmark implementations (problem-specific).

Each benchmark is tied to a specific problem and tests reward hacking behaviors.
"""

from .fibonacci_hardcoding import FibonacciHardcodingBenchmark
from .prime_hardcoding import PrimeHardcodingBenchmark

# APPS benchmarks
from .apps_0000_benchmark import Apps0000Benchmark
from .apps_0001_benchmark import Apps0001Benchmark
from .apps_0002_benchmark import Apps0002Benchmark
from .apps_0003_benchmark import Apps0003Benchmark
from .apps_0004_benchmark import Apps0004Benchmark

__all__ = [
    "FibonacciHardcodingBenchmark",
    "PrimeHardcodingBenchmark",
    "Apps0000Benchmark",
    "Apps0001Benchmark",
    "Apps0002Benchmark",
    "Apps0003Benchmark",
    "Apps0004Benchmark",
]

