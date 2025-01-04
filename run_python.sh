#!/bin/bash

VENV_DIR="venv"

# Check if the virtual environment exists
if [ ! -d "$VENV_DIR" ]; then
    echo "Virtual environment not found. Creating one..."
    python3 -m venv $VENV_DIR
fi

echo "Activating virtual environment..."
source $VENV_DIR/bin/activate

# Install dependencies if requirements.txt exists
if [ -f "requirements.txt" ]; then
    echo "Installing dependencies from requirements.txt..."
    pip install -r requirements.txt
fi

# Run the Python script
if [ $# -eq 0 ]; then
    echo "No Python script specified. Exiting."
else
    echo "Running Python script: $1"
    python "$@"
fi

# Deactivate the virtual environment
echo "Deactivating virtual environment..."
deactivate
