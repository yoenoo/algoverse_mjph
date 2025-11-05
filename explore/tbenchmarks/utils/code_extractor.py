"""
Extract Python code from LLM responses.

Handles various response formats that LLMs might use:
- Code blocks with language tags
- Code blocks without tags
- Function definitions
- Plain code
"""

import re
from textwrap import dedent


def extract_code_from_response(response_text: str) -> str:
    """
    Extract Python code from LLM response text.
    
    Handles various formats:
    - Code blocks (```python ... ```)
    - Code blocks (``` ... ```)
    - Function definitions
    - Plain code
    
    Args:
        response_text: Raw response from LLM
    
    Returns:
        Extracted Python code as string
    """
    if not response_text:
        return ""
    
    # Look for code blocks with language tags
    code_patterns = [
        r'```python\n(.*?)\n```',  # ```python\ncode\n```
        r'```python(.*?)```',      # ```pythoncode```
        r'```\n(.*?)\n```',        # ```\ncode\n```
        r'```(.*?)```',            # ```code```
    ]
    
    for pattern in code_patterns:
        matches = re.findall(pattern, response_text, re.DOTALL)
        if matches:
            code = matches[0].strip()
            # Ensure function exists
            if "def solution(" in code:
                return code
    
    # If no code blocks, look for function definition
    lines = response_text.split('\n')
    code_lines = []
    in_function = False
    
    for line in lines:
        if line.strip().startswith('def solution'):
            in_function = True
            code_lines.append(line)
        elif in_function:
            # Continue until we hit a non-indented line or empty line followed by non-indented
            if line.strip() == '':
                # Allow empty lines within function
                code_lines.append(line)
            elif line.startswith(' ') or line.startswith('\t'):
                code_lines.append(line)
            else:
                # Non-indented line, function probably ended
                break
    
    if code_lines:
        return '\n'.join(code_lines)
    
    # Fallback: return as-is (might be plain code)
    return response_text.strip()

