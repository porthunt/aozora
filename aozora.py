#!/usr/bin/env python3
import os
import re
import argparse
import logging
from distutils.dir_util import copy_tree

DEFAULT_PROJECT_CONTENT = "project_content/"


def create_project_content(name: str, location: str):
    location = os.path.join(location, name)
    os.mkdir(location)
    copy_tree(DEFAULT_PROJECT_CONTENT, location)


def edit_file(name: str, location: str, _from: str, _to: str):
    file_name = os.path.join(location, name)
    fake_file = file_name + "_"

    with open(file_name, "r") as fr:
        lines = fr.readlines()
        with open(fake_file, "w") as fw:
            for line in lines:
                if _from in line:
                    line = line.replace(_from, _to)
                fw.write(line)

    os.remove(file_name)
    os.rename(fake_file, file_name)


def customize_project_content(name: str, location: str):
    edit_file(f"{name}/app/settings.py", location, r"{{SERVICE_NAME}}", name)
    edit_file(f"{name}/serverless.yml", location, r"{{SERVICE_NAME}}", name)


def project_name(name):
    if re.search(r"[^\w\-_\. ]", name):
        logging.error(
            "Invalid project name. Use only letters, numbers and dashes."
        )
        raise argparse.ArgumentTypeError
    return name


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Aozora - Serverless Framework API Skeleton"
    )
    parser.add_argument(
        "--name", required=True, type=project_name, help="API project name"
    )
    parser.add_argument(
        "--location",
        required=False,
        type=str,
        default=".",
        help="Path where you want your project to be created. Default is '.'",
    )

    args = parser.parse_args()
    create_project_content(args.name, args.location)
    customize_project_content(args.name, args.location)
