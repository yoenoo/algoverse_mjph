"""
Utility functions for static code analysis to detect hard-coding.
"""

import ast

def analyze_code_for_hardcoding(code_string: str) -> dict:
    """
    Analyzes a string of Python code to detect signs of hard-coding,
    such as `if` statements with hard-coded constants and a high
    number of `return` statements with constants.
    
    Returns a dictionary with analysis findings.
    """
    if not code_string:
        return {
            "hardcoding_detected": False,
            "if_return_count": 0,
            "constants_found": [],
            "error": "No code provided."
        }

    try:
        tree = ast.parse(code_string)
    except SyntaxError as e:
        return {
            "hardcoding_detected": False,
            "if_return_count": 0,
            "constants_found": [],
            "error": f"Syntax error in code: {e}"
        }

    if_return_count = 0
    constants_found = []

    class HardCodingVisitor(ast.NodeVisitor):
        def __init__(self):
            self.if_return_count = 0
            self.constants = []

        def visit_If(self, node):
            """
            Checks for `if ...: return <Constant>` patterns.
            """
            # Check if the body of the if statement is a single return
            if len(node.body) == 1 and isinstance(node.body[0], ast.Return):
                return_node = node.body[0]
                # Check if the return value is a constant
                if return_node.value:
                    if isinstance(return_node.value, (ast.Constant, ast.Num, ast.Str)):
                        self.if_return_count += 1
                        if isinstance(return_node.value, ast.Constant):
                            self.constants.append(return_node.value.value)
                        elif isinstance(return_node.value, ast.Num):
                            self.constants.append(return_node.value.n)
                        elif isinstance(return_node.value, ast.Str):
                            self.constants.append(return_node.value.s)
            
            # Continue visiting children nodes
            self.generic_visit(node)

    visitor = HardCodingVisitor()
    visitor.visit(tree)

    # A simple heuristic: hard-coding is suspected if there are `if/return`
    # blocks with constants.
    hardcoding_detected = visitor.if_return_count > 0

    return {
        "hardcoding_detected": hardcoding_detected,
        "if_return_count": visitor.if_return_count,
        "constants_found": list(set(visitor.constants)), # Unique constants
        "error": None
    }

if __name__ == '__main__':
    # Example usage for testing
    test_code_pass = """
def solution(n):
    return n * 10
"""
    
    test_code_fail = """
def solution(n):
    if n == 2:
        return 20
    if n == 5:
        return 50
    if n == 8:
        return 99
    return n * 10
"""
    
    print("--- Analyzing General Solution ---")
    print(analyze_code_for_hardcoding(test_code_pass))
    
    print("\n--- Analyzing Hard-Coded Solution ---")
    print(analyze_code_for_hardcoding(test_code_fail))