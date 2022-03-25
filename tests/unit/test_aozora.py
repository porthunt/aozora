import os
import shutil
import pytest
import aozora
from argparse import ArgumentTypeError


def test_create_project_content():
    name = "lambda-api"
    assert not os.path.exists(name)
    aozora.create_project_content(name, ".")
    shutil.rmtree(name)


def test_edit_file():
    directory = "test-file"
    file_name = "random-file"
    os.mkdir(directory)
    with open(f"{directory}/{file_name}", "w") as w:
        w.write("{{TEST}}")

    aozora.edit_file(f"{directory}/{file_name}", ".", "{{TEST}}", "FOOBAR")

    with open(f"{directory}/{file_name}", "r") as r:
        lines = r.readlines()
        assert lines[0] == "FOOBAR"

    shutil.rmtree(directory)


def test_edit_file_invalid_file():
    with pytest.raises(FileNotFoundError):
        aozora.edit_file(f"foobar", ".", "{{TEST}}", "FOOBAR")


def test_edit_file_no_changes():
    directory = "test-file"
    file_name = "random-file"
    os.mkdir(directory)
    with open(f"{directory}/{file_name}", "w") as w:
        w.write("{{TEST}}")

    aozora.edit_file(f"{directory}/{file_name}", ".", "{{FOOBAR}}", "FOOBAR")

    with open(f"{directory}/{file_name}", "r") as r:
        lines = r.readlines()
        assert lines[0] == "{{TEST}}"

    shutil.rmtree(directory)


def test_project_name():
    api = "lambda-api"
    assert aozora.project_name(api) == api


def test_project_name_invalid():
    with pytest.raises(ArgumentTypeError):
        aozora.project_name("lambda api")
    with pytest.raises(ArgumentTypeError):
        aozora.project_name("lambda#api")
    with pytest.raises(ArgumentTypeError):
        aozora.project_name("lambda/api")
    with pytest.raises(ArgumentTypeError):
        aozora.project_name("lambda\\api")
