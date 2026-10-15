# VENV: virtual environment path (default: .venv)
VENV ?= .venv
# PYTHON: Python interpreter used by setup (default: $(VENV)/bin/python)
PYTHON ?= $(VENV)/bin/python

.PHONY: setup run run-initial-belief clean help

setup: ## Create the virtual environment and install project dependencies
	uv venv $(VENV) --python 3.12
	uv pip install --python $(PYTHON) -e .

run: run-initial-belief run-add-belief-after-agent-creation run-add-belief-after-start-system ## Run all examples sequencially

run-initial-belief: ## Run the initial belief example
	$(PYTHON) examples/01_initial_belief.py

run-add-belief-after-agent-creation: ## Run the agent adding a belief after creation
	$(PYTHON) examples/02_add_belief_after_agent_creation.py

run-add-belief-after-start-system: ## Run the agent adding a belief after the system start
	$(PYTHON) examples/03_add_belief_after_start_system.py
clean: ## Remove the virtual environment
	rm -rf $(VENV)

help: ## Show this help
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z0-9_.-]+:.*?## / {printf "  %-12s %s\n", $$1, $$2}' $(MAKEFILE_LIST)