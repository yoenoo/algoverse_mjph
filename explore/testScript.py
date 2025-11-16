import os
import sys
from pathlib import Path

from explore.scicode_script import ALLOW_INTERNET, MAX_CONNECTIONS, LOG_DIR

# Windows compatibility: create stub for 'resource' module if it doesn't exist
if sys.platform == "win32":
    try:
        import resource
    except ImportError:
        import types
        resouce = types.ModuleType("resource")

        # Common resource module attributes with dummy values
        resource.RLIMIT_CPU = 0
        resource.RLIMIT_AS = 2
        resource.RLIMIT_DATA = 2
        resource.RLIMIT_STACK = 3
        resource.RLIMIT_NOFILE = 7
        resource.RLIMIT_NPROC = 6
        resource.RLIM_INFINITY = -1
        resource.RLIMIT_INFINITY = -1

        def getrlimit(resource_type):
            return (resource.RLIM_INFINITY, resource.RLIM_INFINITY)

        def setrlimit(resource_type, limits):
            pass

        resource.getrlimit = getrlimit
        resource.setrlimit = setrlimit
        sys.modules["resource"] = resouce

from dotenv import load_dotenv
import re

from inspect_ai import eval as inspect_eval
from inspect_ai.solver import basic_agent, system_message
from inspect_ai.tool import bash, python as py_tool
from inspect_ai.scorer import model_graded_qa

from inspect_evals.scicode import scicode

# Config
os.environ.setDefault("DOCKER_DEFAULT_PLATFORM", "linux/amd64")
os.environ.setdefault("DOCKER_DEFAULT_PLATFORM", "1")

MODEL = "openrouter/gpt-5-mini"
LIMIT = 2
EPOCHS = 1
ALLOW_INTERNET = False
MAX_CONNECTIONS = 4
LOG_DIR = ".\explore\logs\scicode"
SPLIT = "test"
WITH_BACKGROUND = False

