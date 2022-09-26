#!/usr/bin/env python

from subprocess import call  # nosec
from sys import platform


def main():
    file_name = "./requirements.txt"

    if platform == "win32":
        with open(file_name, "w") as file_:
            call(["./venv/Scripts/pip3", "freeze"], stdout=file_)
    else:
        with open(file_name, "w") as file_:
            call(["./venv/bin/pip3", "freeze"], stdout=file_)
    call(f"git add {file_name}")  # nosec


if __name__ == "__main__":
    exit(main())
