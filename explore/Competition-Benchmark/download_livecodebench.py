"""
Download and convert competitive programming problems to our Problem/TestCase format.
Currently supports APPS dataset from HuggingFace.
"""

import json
import re
import ast
from typing import List, Dict, Any, Tuple, Optional
from pathlib import Path

# Import our problem structures
import sys
sys.path.insert(0, str(Path(__file__).parent.parent / "tbenchmarks"))

from core.problem import Problem, TestCase


def extract_function_signature(code: str) -> str:
    """Extract function signature from code."""
    # Look for function definitions
    patterns = [
        r'def\s+(\w+)\s*\([^)]*\)\s*:',
        r'def\s+(\w+)\s*\([^)]*\)\s*->\s*\w+\s*:',
    ]
    
    for pattern in patterns:
        match = re.search(pattern, code)
        if match:
            func_name = match.group(1)
            # Try to get the full signature
            full_match = re.search(rf'def\s+{func_name}\s*\([^)]*\)\s*(?:->\s*\w+)?\s*:', code)
            if full_match:
                return full_match.group(0)
    
    # Default signature
    return "def solution(*args, **kwargs):"


def parse_test_cases(test_inputs: List[str], test_outputs: List[str]) -> List[TestCase]:
    """Parse test cases from APPS format."""
    test_cases = []
    
    for i, (input_val, output_val) in enumerate(zip(test_inputs, test_outputs), 1):
        # Try to parse input/output as Python literals
        input_parsed = safe_eval(input_val) if isinstance(input_val, str) else input_val
        output_parsed = safe_eval(output_val) if isinstance(output_val, str) else output_val
        
        test_cases.append(
            TestCase(
                name=f"test_case_{i}",
                input_value=input_parsed,
                expected_output=output_parsed,
                description=f"Test case {i}: input={str(input_val)[:50]}, expected={str(output_val)[:50]}"
            )
        )
    
    return test_cases


def safe_eval(value: str) -> Any:
    """Safely evaluate a string as Python literal."""
    try:
        return ast.literal_eval(value)
    except:
        return value


def convert_apps_to_problem(item: Dict[str, Any], index: int) -> Problem:
    """Convert an APPS item to our Problem format."""
    
    # Extract problem name
    problem_name = f'apps_{index:04d}'
    
    # Get description
    description = item.get('question', '')
    if not description:
        description = "Solve the following coding problem."
    
    # Get starter code to extract function signature
    starter_code = item.get('starter_code', '')
    function_signature = extract_function_signature(starter_code)
    if not function_signature or function_signature == "def solution(*args, **kwargs):":
        function_signature = "def solution(*args, **kwargs):"
    
    # Get test cases from APPS format
    # APPS has 'input_output' field with dict containing inputs/outputs lists
    visible_tests = []
    hidden_tests = []
    
    io_data = item.get('input_output', {})
    if isinstance(io_data, str):
        try:
            io_data = json.loads(io_data)
        except:
            io_data = {}
    
    inputs = io_data.get('inputs', [])
    outputs = io_data.get('outputs', [])
    
    if inputs and outputs:
        # Split into visible and hidden tests
        # Use first 3-4 as visible, rest as hidden
        num_visible = min(3, len(inputs))
        
        visible_tests = parse_test_cases(
            inputs[:num_visible],
            outputs[:num_visible]
        )
        
        if len(inputs) > num_visible:
            hidden_tests = parse_test_cases(
                inputs[num_visible:],
                outputs[num_visible:]
            )
        else:
            # If we have very few tests, use last visible as hidden
            if visible_tests:
                hidden_tests = [visible_tests[-1]]
                visible_tests = visible_tests[:-1]
    
    if not visible_tests:
        # Create a dummy test case if none found
        visible_tests = [
            TestCase(
                name="test_case_1",
                input_value=None,
                expected_output=None,
                description="Test case from APPS dataset"
            )
        ]
    
    return Problem(
        name=problem_name,
        description=description,
        function_signature=function_signature,
        visible_tests=visible_tests,
        hidden_tests=hidden_tests
    )


def save_problem_to_file(problem: Problem, output_dir: Path):
    """Save a Problem to a Python file."""
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Generate Python code
    lines = [
        '"""',
        f'{problem.name} problem from APPS dataset.',
        '"""',
        '',
        'from typing import List',
        'from ...core.problem import Problem, TestCase',
        '',
        '',
        f'def create_{problem.name}() -> Problem:',
        '    """',
        f'    Create the {problem.name} problem.',
        '    """',
        '    # Visible tests (shown to the model)',
        '    visible_tests: List[TestCase] = [',
    ]
    
    for test in problem.visible_tests:
        lines.append(f'        TestCase(')
        lines.append(f'            name="{test.name}",')
        lines.append(f'            input_value={repr(test.input_value)},')
        lines.append(f'            expected_output={repr(test.expected_output)},')
        # Escape description properly
        desc = test.description.replace('\\', '\\\\').replace('"', '\\"').replace('\n', '\\n')
        lines.append(f'            description="{desc}"')
        lines.append(f'        ),')
    
    lines.extend([
        '    ]',
        '    ',
        '    # Hidden tests (not shown to model, used for validation)',
        '    hidden_tests: List[TestCase] = [',
    ])
    
    for test in problem.hidden_tests:
        lines.append(f'        TestCase(')
        lines.append(f'            name="{test.name}",')
        lines.append(f'            input_value={repr(test.input_value)},')
        lines.append(f'            expected_output={repr(test.expected_output)},')
        # Escape description properly
        desc = test.description.replace('\\', '\\\\').replace('"', '\\"').replace('\n', '\\n')
        lines.append(f'            description="{desc}"')
        lines.append(f'        ),')
    
    lines.extend([
        '    ]',
        '    ',
        '    return Problem(',
        f'        name="{problem.name}",',
    ])
    
    # Use triple-quoted string for description to handle special characters
    lines.append('        description=r"""' + problem.description + '""",')
    
    lines.extend([
        f'        function_signature="{problem.function_signature}",',
        '        visible_tests=visible_tests,',
        '        hidden_tests=hidden_tests',
        '    )',
    ])
    
    # Write to file
    output_file = output_dir / f"{problem.name}.py"
    with open(output_file, 'w') as f:
        f.write('\n'.join(lines))
    
    print(f"Saved: {output_file}")


def load_apps_problem(problem_dir: Path) -> Dict[str, Any]:
    """Load a single APPS problem from directory."""
    problem_data = {}
    
    # Read question
    question_file = problem_dir / "question.txt"
    if question_file.exists():
        with open(question_file, 'r', encoding='utf-8') as f:
            problem_data['question'] = f.read()
    
    # Read input/output
    io_file = problem_dir / "input_output.json"
    if io_file.exists():
        with open(io_file, 'r', encoding='utf-8') as f:
            problem_data['input_output'] = json.load(f)
    
    # Read metadata
    metadata_file = problem_dir / "metadata.json"
    if metadata_file.exists():
        with open(metadata_file, 'r', encoding='utf-8') as f:
            problem_data['metadata'] = json.load(f)
    
    # Read starter code from solutions (first solution)
    solutions_file = problem_dir / "solutions.json"
    if solutions_file.exists():
        with open(solutions_file, 'r', encoding='utf-8') as f:
            solutions = json.load(f)
            if solutions:
                problem_data['starter_code'] = solutions[0] if isinstance(solutions, list) else solutions.get('solutions', [''])[0]
    
    return problem_data


def main():
    """Download and convert 5 problems from APPS dataset."""
    apps_dir = Path(__file__).parent / "APPS" / "test"
    
    if not apps_dir.exists():
        print(f"Error: APPS dataset not found at {apps_dir}")
        print("Please download it from: https://people.eecs.berkeley.edu/~hendrycks/APPS.tar.gz")
        return
    
    # Get all problem directories, sorted
    problem_dirs = sorted([d for d in apps_dir.iterdir() if d.is_dir()])
    
    if not problem_dirs:
        print("No problems found in APPS/test directory")
        return
    
    print(f"Found {len(problem_dirs)} problems in APPS dataset")
    
    # Get first 5 problems
    num_problems = 5
    selected_dirs = problem_dirs[:num_problems]
    
    # Output directory
    output_dir = Path(__file__).parent.parent / "tbenchmarks" / "problems" / "apps"
    
    print(f"\nConverting {num_problems} problems...")
    
    for i, problem_dir in enumerate(selected_dirs):
        print(f"\nProcessing problem {i+1}/{num_problems}: {problem_dir.name}")
        
        try:
            item = load_apps_problem(problem_dir)
            problem = convert_apps_to_problem(item, i)
            save_problem_to_file(problem, output_dir)
        except Exception as e:
            print(f"Error converting problem {i+1}: {e}")
            import traceback
            traceback.print_exc()
            continue
    
    print(f"\n✓ Successfully converted {num_problems} problems to {output_dir}")


if __name__ == "__main__":
    main()

