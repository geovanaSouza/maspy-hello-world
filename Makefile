# VENV: virtual environment path (default: .venv)
VENV ?= .venv
# PYTHON: Python interpreter used by setup (default: $(VENV)/bin/python)
PYTHON ?= $(VENV)/bin/python

.PHONY: setup run run-initial-belief clean help

setup: ## Create the virtual environment and install project dependencies
	uv venv $(VENV) --python 3.12
	uv pip install --python $(PYTHON) -e .

run: run-initial-belief run-add-belief-after-agent-creation run-add-belief-after-start-system run-atomic-plan run-dependencies-between-plans ## Run all examples sequencially

run-initial-belief: ## Run the initial belief example
	$(PYTHON) examples/01_initial_belief.py

run-add-belief-after-agent-creation: ## Run the agent adding a belief after creation
	$(PYTHON) examples/02_add_belief_after_agent_creation.py

run-add-belief-after-start-system: ## Run the agent adding a belief after the system start
	$(PYTHON) examples/03_add_belief_after_start_system.py

run-atomic-plan: ## Run agent with atomic plan
	$(PYTHON) examples/04_atomic_plan.py

run-dependencies-between-plans: ## Run agent dependents plans
	$(PYTHON) examples/05_dependencies_between_plans.py

clean: ## Remove the virtual environment
	rm -rf $(VENV)

help: ## Show this help
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z0-9_.-]+:.*?## / {printf "  %-12s %s\n", $$1, $$2}' $(MAKEFILE_LIST)