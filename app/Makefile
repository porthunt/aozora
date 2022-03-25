SHELL := /bin/bash

init:
	@pip install -r requirements.txt

lint:
	flake8 app/ tests/
	black --line-length 79 --check app/ tests/

unit:
	pytest --disable-pytest-warnings tests/unit/
