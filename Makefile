SHELL := /bin/bash

init:
	@pip install -r requirements.txt

lint:
	flake8 app/ tests/ aozora.py
	black --line-length 79 --check app/ tests/ aozora.py

unit:
	pytest --disable-pytest-warnings tests/unit/
