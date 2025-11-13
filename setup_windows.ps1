# Windows PowerShell setup script for AlgoVerse
# Run this from the algoverse_mjph directory

Write-Host "Setting up AlgoVerse environment for Windows..." -ForegroundColor Green

# Check if Python 3.12 is available
$pythonVersion = python --version 2>&1
if ($pythonVersion -match "Python 3\.(1[2-9]|[2-9][0-9])") {
    Write-Host "Found Python: $pythonVersion" -ForegroundColor Green
} else {
    Write-Host "Warning: Python 3.12+ recommended. Found: $pythonVersion" -ForegroundColor Yellow
}

# Create virtual environment
if (-not (Test-Path "venv")) {
    Write-Host "Creating virtual environment..." -ForegroundColor Cyan
    python -m venv venv
} else {
    Write-Host "Virtual environment already exists." -ForegroundColor Yellow
}

# Activate virtual environment
Write-Host "Activating virtual environment..." -ForegroundColor Cyan
& .\venv\Scripts\Activate.ps1

# Upgrade pip
Write-Host "Upgrading pip..." -ForegroundColor Cyan
python -m pip install --upgrade pip

# Install dependencies
Write-Host "Installing dependencies (this may take a while)..." -ForegroundColor Cyan
pip install -r requirements.txt

# Create .env file if it doesn't exist
if (-not (Test-Path ".env")) {
    Write-Host "Creating .env file from template..." -ForegroundColor Cyan
    @"
# OpenRouter API Key (required for running experiments)
OPENROUTER_API_KEY=your_openrouter_api_key_here

# Optional: Override the default model
# INSPECT_EVAL_MODEL=openrouter/meta-llama/llama-3.3-70b-instruct

# Optional: Permission level (strict, moderate, permissive)
# PERMISSION_LEVEL=moderate

# Optional: Enable dry-run mode (skip Docker/model calls)
# DRY_RUN=false

# Optional: Pull remote Docker images
# PULL_REMOTE_IMAGES=false
"@ | Out-File -FilePath ".env" -Encoding utf8
    Write-Host "Created .env file. Please edit it and add your OPENROUTER_API_KEY!" -ForegroundColor Yellow
} else {
    Write-Host ".env file already exists." -ForegroundColor Yellow
}

Write-Host "`nSetup complete!" -ForegroundColor Green
Write-Host "To activate the virtual environment in the future, run:" -ForegroundColor Cyan
Write-Host "  .\venv\Scripts\Activate.ps1" -ForegroundColor White
Write-Host "`nDon't forget to set your OPENROUTER_API_KEY in the .env file!" -ForegroundColor Yellow


