#!/bin/bash
# WSL setup script for AlgoVerse
# Run this from the algoverse_mjph directory in WSL

set -e

echo "Setting up AlgoVerse environment for WSL..."

# Check if Python 3.12 is available
if command -v python3.12 &> /dev/null; then
    PYTHON_CMD=python3.12
    echo "Found Python 3.12"
elif command -v python3 &> /dev/null; then
    PYTHON_CMD=python3
    PYTHON_VERSION=$(python3 --version | cut -d' ' -f2)
    echo "Found Python: $PYTHON_VERSION (3.12+ recommended)"
else
    echo "Error: Python 3 not found. Please install Python 3.12+"
    exit 1
fi

# Create virtual environment if it doesn't exist
if [ ! -d "wsl_venv_lite" ]; then
    echo "Creating virtual environment..."
    $PYTHON_CMD -m venv wsl_venv_lite
else
    echo "Virtual environment already exists."
fi

# Activate virtual environment
echo "Activating virtual environment..."
source wsl_venv_lite/bin/activate

# Upgrade pip
echo "Upgrading pip..."
python -m pip install --upgrade pip

# Install dependencies
echo "Installing dependencies (this may take a while)..."
pip install -r requirements.txt

# Create .env file if it doesn't exist
if [ ! -f ".env" ]; then
    echo "Creating .env file from template..."
    cat > .env << 'EOF'
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
EOF
    echo "Created .env file. Please edit it and add your OPENROUTER_API_KEY!"
else
    echo ".env file already exists."
fi

echo ""
echo "Setup complete!"
echo "To activate the virtual environment in the future, run:"
echo "  source wsl_venv_lite/bin/activate"
echo ""
echo "Don't forget to set your OPENROUTER_API_KEY in the .env file!"


