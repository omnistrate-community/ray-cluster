#!/bin/bash
set -e

# Source directory is mounted at src
cd src

# Install requirements if requirements.txt exists
if [ -f "requirements.txt" ]; then
    echo "Installing dependencies from requirements.txt..."
    pip install -r requirements.txt
fi

# Install any Ray extras specified in RAY_EXTRAS env var
if [ -n "$RAY_EXTRAS" ]; then
    echo "Installing Ray extras: $RAY_EXTRAS..."
    pip install -U "ray[$RAY_EXTRAS]"
fi

# Find and run the main Python script
# If SCRIPT_PATH is provided, use that, otherwise look for main.py
if [ -n "$SCRIPT_PATH" ]; then
    SCRIPT_TO_RUN="$SCRIPT_PATH"
elif [ -f "main.py" ]; then
    SCRIPT_TO_RUN="main.py"
else
    # Find the first Python file if main.py doesn't exist
    SCRIPT_TO_RUN=$(find . -maxdepth 1 -name "*.py" | head -n 1)
    if [ -z "$SCRIPT_TO_RUN" ]; then
        echo "Error: No Python script found to execute."
        exit 1
    fi
fi

echo "Running script: $SCRIPT_TO_RUN"
python "$SCRIPT_TO_RUN" "$@"
