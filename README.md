# AlgoVerse Unit-Test Overfitting Experiment

A research project investigating how LLM permission levels affect reward hacking behaviors in coding tasks.

## Project Structure

- `explore/` - Experimental/PoC code (your active workspace)
- `src/` - Future production code (empty for now)
- `tests/` - Test suite for explore/ code
- `docs/` - Documentation and experiment design

## Quick Start

### WSL (Windows Subsystem for Linux) - **Recommended**

1. **Setup environment:**
   ```bash
   cd algoverse_mjph
   chmod +x setup_wsl.sh
   ./setup_wsl.sh
   ```
   
   Or manually:
   ```bash
   python3.12 -m venv wsl_venv_lite
   source wsl_venv_lite/bin/activate
   pip install -r requirements.txt
   ```

2. **Configure API keys:**
   - Edit the `.env` file (created by setup script) and add your `OPENROUTER_API_KEY`

3. **Run SWE-bench experiment:**
   ```bash
   # Make sure venv is activated
   source wsl_venv_lite/bin/activate
   
   # Run the experiment
   python explore/swe_bench_inspect_eval.py
   ```

### Windows (PowerShell)

1. **Setup environment:**
   ```powershell
   cd algoverse_mjph
   .\setup_windows.ps1
   ```
   
   Or manually:
   ```powershell
   python -m venv venv
   .\venv\Scripts\Activate.ps1
   pip install -r requirements.txt
   ```

2. **Configure API keys:**
   - Edit the `.env` file (created by setup script) and add your `OPENROUTER_API_KEY`

3. **Run SWE-bench experiment:**
   ```powershell
   # Make sure venv is activated
   .\venv\Scripts\Activate.ps1
   
   # Run the experiment
   python explore\swe_bench_inspect_eval.py
   ```

### Linux/macOS

1. **Setup environment:**
   ```bash
   python3.12 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

2. **Configure API keys:**
   ```bash
   cp .env.example .env
   # Edit .env with your API keys
   ```

3. **Run SWE-bench experiment:**
   ```bash
   python explore/swe_bench_inspect_eval.py
   ```

## Prerequisites

- **Python 3.12+** (3.12 recommended per project standards)
- **Docker Desktop** (must be running for SWE-bench experiments)
- **OpenRouter API Key** (set in `.env` file)
- **Git** (for installing `inspect-evals` from GitHub)

## Experiment Design

This project tests whether LLMs exhibit reward hacking behaviors when given different permission levels:

- **PL0 (Text-only)**: Model returns code as text, no execution
- **PL1 (Execute)**: Model can request test execution  
- **PL2 (Write)**: Model can modify test files

We measure gaming behaviors like hardcoding answers, test modification, and overfitting to visible test cases.

## Development Status

✅ **Phase 0 Complete**: Environment setup and project scaffolding
🚧 **Phase 1**: Running initial experiments and collecting data

## Project Files

- `explore/swe_bench_inspect_eval.py` - Main experiment script
- `explore/analysis/parse_grades.py` - Utility to parse and aggregate grades from logs
- `explore/code_analysis_utils.py` - Code analysis for detecting hardcoding
- `scripts/run_experiments.sh` - Batch experiment runner for multiple permission levels

## Logs and Results

Evaluation logs are saved to `explore/logs/`. View them with:
```bash
inspect view explore/logs/<log-file>.eval
```

## Contributing

This is a research project investigating reward hacking behaviors in LLMs on coding tasks.
