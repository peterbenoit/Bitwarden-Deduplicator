#!/bin/bash

# Set the virtual environment directory
VENV_DIR="venv"

# Check if the virtual environment exists
if [ ! -d "$VENV_DIR" ]; then
    echo "Virtual environment not found. Creating one..."
    python3 -m venv $VENV_DIR
fi

# Activate the virtual environment
echo "Activating virtual environment..."
source $VENV_DIR/bin/activate

# Install dependencies if requirements.txt exists
if [ -f "requirements.txt" ]; then
    echo "Installing dependencies from requirements.txt..."
    pip install -r requirements.txt
fi

# Default script to run
SCRIPT="deduplicate.py"

# Prompt for configuration if no arguments are passed
if [ $# -eq 0 ]; then
    echo "No arguments provided. Let's configure the script."

    # Input file
    read -p "Enter the path to the Bitwarden JSON file (default: bitwarden-export.json): " INPUT_FILE
    INPUT_FILE=${INPUT_FILE:-bitwarden-export.json}

    # Filter by type
    echo "Select the type to process:"
    echo "1. Login"
    echo "2. Secure Note"
    echo "3. Card"
    echo "4. Identity"
    echo "5. All (default)"
    read -p "Enter your choice: " TYPE
    case $TYPE in
        1) TYPE_FLAG="--type 1" ;;
        2) TYPE_FLAG="--type 2" ;;
        3) TYPE_FLAG="--type 3" ;;
        4) TYPE_FLAG="--type 4" ;;
        *) TYPE_FLAG="" ;;
    esac

    # Output options
    echo "Select the output option:"
    echo "1. Save only unique items"
    echo "2. Save only duplicate items"
    echo "3. Save both (default)"
    read -p "Enter your choice: " OUTPUT
    case $OUTPUT in
        1) OUTPUT_FLAG="--output-unique" ;;
        2) OUTPUT_FLAG="--output-duplicates" ;;
        *) OUTPUT_FLAG="--output-both" ;;
    esac

    # Run the Python script with the configured options
    echo "Running Python script with selected options..."
    python $SCRIPT $INPUT_FILE $TYPE_FLAG $OUTPUT_FLAG
else
    # Run the Python script with the provided arguments
    echo "Running Python script with provided arguments: $@"
    python $SCRIPT "$@"
fi

# Deactivate the virtual environment
echo "Deactivating virtual environment..."
deactivate
