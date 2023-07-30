files := requirements.txt Pipfile

# Variables
PYTHON = pipenv run python

# Targets
.PHONY: install run clean

init:
	pip install pipenv

install:
    @echo "Installing dependencies..."
    pipenv install --dev

run:
    @echo "Running script..."
    $(PYTHON) main.py

clean:
    @echo "Cleaning up..."
    pipenv --rm
