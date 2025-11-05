"""
Result structures and JSON serialization for benchmarks.
"""

from dataclasses import dataclass, asdict
from typing import Dict, Any, List
from datetime import datetime
from enum import Enum
import json
from pathlib import Path


class PermissionLevel(Enum):
    """
    Permission levels for the experiment.
    
    Based on real-world LLM coding assistant scenarios:
    - PL0: Code suggestion only (GitHub Copilot style)
    - PL1: Code generation with manual feedback (ChatGPT style)
    - PL2: Automated test execution (Aider/Cursor style)
    - PL3: File modification - code files only
    - PL4: Test file modification - can modify test files (maximum reward hacking)
    """
    PL0_CODE_SUGGESTION = "code_suggestion"  # No execution, no feedback
    PL1_MANUAL_FEEDBACK = "manual_feedback"  # User shares test results
    PL2_AUTO_TEST_EXEC = "auto_test_exec"  # System runs tests automatically
    PL3_FILE_MODIFICATION = "file_modification"  # Can modify code files
    PL4_TEST_MODIFICATION = "test_modification"  # Can modify test files


@dataclass
class DetectionResult:
    """Results from reward hacking detection"""
    hardcoding_detected: bool
    test_edit_detected: bool
    overfitting_detected: bool
    execution_gaming_detected: bool = False
    evidence: Dict[str, Any] | None = None


@dataclass
class ExecutionResult:
    """Results from executing LLM code"""
    visible_tests_passed: bool
    hidden_tests_passed: bool
    visible_test_output: str
    hidden_test_output: str
    command_history: List[Dict[str, Any]] | None = None
    file_changes: Dict[str, str] | None = None  # file_path -> change_type
    execution_time_seconds: float | None = None


@dataclass
class BenchmarkResult:
    """Complete result from running a benchmark"""
    benchmark_name: str
    permission_level: PermissionLevel
    timestamp: str
    problem_name: str
    execution_result: ExecutionResult
    detection_result: DetectionResult
    llm_model: str
    llm_provider: str
    metadata: Dict[str, Any] | None = None
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary for JSON serialization"""
        data = asdict(self)
        # Convert enum to string
        data['permission_level'] = self.permission_level.value
        return data
    
    def to_json(self, indent: int = 2) -> str:
        """Convert to JSON string"""
        return json.dumps(self.to_dict(), indent=indent)
    
    def save(self, results_dir: Path):
        """
        Save result to JSON file.
        
        Args:
            results_dir: Directory to save results in
        """
        results_dir.mkdir(parents=True, exist_ok=True)
        
        # Generate filename
        timestamp_str = self.timestamp.replace(':', '-').replace('.', '-')
        filename = f"{self.benchmark_name}_{self.permission_level.value}_{timestamp_str}.json"
        filepath = results_dir / filename
        
        # Write JSON
        filepath.write_text(self.to_json())
        return filepath
    
    @classmethod
    def load(cls, filepath: Path) -> "BenchmarkResult":
        """Load result from JSON file"""
        data = json.loads(filepath.read_text())
        # Convert string back to enum
        data['permission_level'] = PermissionLevel(data['permission_level'])
        return cls(**data)

