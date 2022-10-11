#!/usr/bin/env python
import os
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
        # with open(dotenv_example, "w") as file_:
        # call([f"(Get-Content {dotenv}) -replace('=.*', '=')"], stdout=file_)
        pass

    else:
        with open(dotenv_example, "w") as file_:
            # sed 's/=.*/=/' .env > .env.example
            call(["sed", "'s/=.*/=/'", f"{dotenv}"], stdout=file_)

    call(f"git add {dotenv_example}")  # nosec


if __name__ == "__main__":
    exit(main())
