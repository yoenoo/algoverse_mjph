import os
from dotenv import load_dotenv

from inspect_ai import eval as inspect_eval
from inspect_ai.solver import basic_agent, system_message
from inspect_ai.tool import bash, python as py_tool

from inspect_evals.swe_bench import swe_bench_verified_mini

# ---- config ----
os.environ.setdefault("DOCKER_DEFAULT_PLATFORM", "linux/amd64")
os.environ.setdefault("INSPECT_MAX_CONNECTIONS", "1")

MODEL = "openrouter/meta-llama/llama-3.3-70b-instruct"
LIMIT = 2                
EPOCHS = 1
ALLOW_INTERNET = False
MAX_CONNECTIONS = 4      
LOG_DIR = "./explore/logs"

def run():
    # ---- API KEY ----
    load_dotenv()
    if not os.getenv("OPENROUTER_API_KEY"):
        raise RuntimeError("Set OPENROUTER_API_KEY in your environment or .env")

    # ---- MODEL ----
    model = os.getenv("INSPECT_EVAL_MODEL", MODEL)
    SYSTEM_MESSAGE = """
                    You are an assistant solving coding repair tasks in a sandbox with two tools:
                    - bash: run shell commands in the repo workspace
                    - python: run small Python snippets

                    GOAL
                    - Produce a minimal, correct fix that makes the target tests pass.
                    - Only call submit(...) AFTER you have hard evidence that tests pass.

                    INTERACTION PROTOCOL (repeat this loop)
                    1) Plan: briefly state the next atomic step.
                    2) Action: CALL a tool (bash or python) to actually perform it.
                    3) Observation: read the tool’s output and decide the next step.

                    EVIDENCE STANDARD
                    - Never claim to have executed anything unless you actually called a tool.
                    - Never fabricate stdout/stderr or test results.
                    - Before calling submit(...), you MUST run tests and show proof:
                    - bash("pytest -q" or the project’s test command)
                    - Exit code 0 AND output line(s) indicating all tests passed (e.g., "X passed").
                    - Quote only the key 3–10 lines of test output (trim noise).

                    ENVIRONMENT & SAFETY RULES
                    - Work inside the repository root; discover it with `ls`, `git status`, etc.
                    - Prefer project-native commands (e.g., `pytest`, `python -m pytest`, `python manage.py test`).
                    - Do NOT alter tests, evaluation harness, or reward signal.
                    - Do NOT write outside the repo or change global system state.
                    - If network is disallowed, do not attempt network access.
                    - If dependencies are missing, install locally (e.g., `pip install -r requirements.txt`) when permitted.
                    - For Django specifically: do NOT call `settings.configure()` in ad-hoc snippets. Use project settings (manage.py) and run migrations/tests via manage.py.

                    TOOL USAGE STYLE
                    - Each message should contain at most one tool call.
                    - Before running a command, show it exactly; then run it.
                    - Keep Python snippets minimal and print results explicitly.
                    - Keep outputs short; summarize after the tool returns.

                    SUBMISSION GATE (hard requirement)
                    - You may ONLY call submit(answer=...) if:
                    - The most recent test run succeeded (exit code 0), and
                    - You showed the key “all tests passed” lines.
                    - Otherwise, continue iterating.

                    FALLBACKS
                    - If a tool is unavailable or errors (timeouts, missing binaries), report the exact issue, adjust, and try the next best step.
                    - If the task cannot be completed under current permissions, clearly state why (e.g., missing internet, cannot build wheels).

                    PROHIBITED BEHAVIORS
                    - Claiming execution without a tool call.
                    - Fabricating test output or success.
                    - Editing tests or disabling checks to “make it pass.”
                    - Irreversible changes outside the repo workspace.

                    FORMAT PER TURN
                    Plan: <one sentence>
                    Action: <bash|python> with the exact command/code
                    (Inspect will show the tool result; then you provide)
                    Observation: <what happened, next step or submit condition check>
                    """

    # ---- AGENT + TASK ----
    agent = basic_agent(tools=[bash(timeout=60), py_tool(timeout=60)])
    task = swe_bench_verified_mini(
        solver=[system_message(SYSTEM_MESSAGE), agent],
        epochs=EPOCHS,
        allow_internet=ALLOW_INTERNET,
        pull_remote_images_if_available=True
    )

    os.environ.setdefault("INSPECT_MAX_CONNECTIONS", str(MAX_CONNECTIONS))

    logs = inspect_eval(
        task,
        model=model,
        log_dir=LOG_DIR,
        limit=LIMIT
    )

    print(f"[OK] Logs -> {LOG_DIR or './logs'}")
    print("Tip: run `inspect view` to open the log viewer.")

if __name__ == "__main__":
    run()
