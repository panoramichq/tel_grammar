install:
	pip install .[dev]

pre-commit-install:
	python -m pre_commit install

lint:
	pre-commit run --all-files

tests:
	python -m pytest tests

black:
	pre-commit run black

flake8:
	pre-commit run flake8

isort:
	pre-commit run isort

.PHONY: install pre-commit-install lint tests black flake8 isort
