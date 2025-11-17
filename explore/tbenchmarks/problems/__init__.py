"""
Problem definitions (reusable across benchmarks).
"""

from .fibonacci import create_fibonacci_problem
from .prime import create_prime_problem

# APPS problems
try:
    from .apps.apps_0000 import create_apps_0000
    from .apps.apps_0001 import create_apps_0001
    from .apps.apps_0002 import create_apps_0002
    from .apps.apps_0003 import create_apps_0003
    from .apps.apps_0004 import create_apps_0004
    
    __all__ = [
        "create_fibonacci_problem",
        "create_prime_problem",
        "create_apps_0000",
        "create_apps_0001",
        "create_apps_0002",
        "create_apps_0003",
        "create_apps_0004",
    ]
except ImportError:
    __all__ = ["create_fibonacci_problem", "create_prime_problem"]

