#!/usr/bin/env python3
"""
Run comprehensive APPS experiment across all problems and permission levels.

Evaluates all 5 APPS problems at all 4 permission levels for a given LLM,
then uses an LLM evaluator to provide detailed analysis of each result.

Usage:
    python explore/run_apps_experiment.py --llm-model "openai/gpt-4"
"""

import sys
from pathlib import Path

# Add explore directory to path
sys.path.insert(0, str(Path(__file__).parent))

from tbenchmarks.run_apps_experiment import run_full_experiment, main

if __name__ == "__main__":
    main()

