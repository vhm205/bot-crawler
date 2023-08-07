# Variables
files := requirements.txt Pipfile
PYTHON := python3
PIPENV := pipenv

# Targets
.PHONY: install run clean

init:
	pip install pipenv

# Target: install
install:
    @echo "Installing dependencies..."
    $(PIPENV) install --dev

# Target: test
test:
    $(PIPENV) run pytest

# Target: lint
lint:
    $(PIPENV) run flake8

# Target: format
format:
    $(PIPENV) run black .

# Target: run
run:
    @echo "Running script..."
    $(PIPENV) run $(PYTHON) main.py

# Target: clean
clean:
    $(PIPENV) --rm
    rm -rf __pycache__

# Target: help
help:
	@echo "Available targets:"
	@echo "  install   - Install project dependencies."
	@echo "  test      - Run tests."
	@echo "  lint      - Lint code."
	@echo "  format    - Format code using black."
	@echo "  run       - Run your script (replace 'your_script.py' with the actual script name)."
	@echo "  clean     - Remove virtual environment and clean cache files."
	@echo "  help      - Show this help message."

# Default target
.DEFAULT_GOAL := help

