SHELL := /bin/bash

init:
	@pip install -r requirements.txt

lint:
	flake8 project_content/ aozora.py
	black --line-length 79 --check project_content/ aozora.py

