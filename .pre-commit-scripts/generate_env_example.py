#!/usr/bin/env python
import os
import re
from subprocess import call  # nosec
from sys import platform


def main():

    dotenv = "./.env"
    dotenv_example = "./.env.example"

    if not os.path.exists(dotenv):
        print(f"there is no {dotenv}")
        exit()

    if platform == "win32":
        # (Get-Content .\.env) -replace('=.*', '=') | Set-Content .env.example
        with open(dotenv, "r") as file_:
            lines = file_.readlines()
            with open(dotenv_example, "w") as file__:
                for line in lines:
                    file__.write(re.sub("=.*", "=", line))

    else:
        with open(dotenv_example, "w") as file_:
            # sed 's/=.*/=/' .env > .env.example
            call(["sed", "'s/=.*/=/'", f"{dotenv}"], stdout=file_)

    call(f"git add {dotenv_example}")  # nosec


if __name__ == "__main__":
    exit(main())
