# -*- encoding: utf-8 -*-

"""
Initialize an Empty ETL Module as per General Conventions

A set of rules are defined to maintain any module, as defined in
`README.md` (root) file. The code initializes an empty module with
all the necessary files and subdirectories.

The command is kept simple, and should work simply from the command
line using:

```shell
$ python create-module.py "module-name"
```
"""

import os
import sys
import string

if __name__ == "__main__":
    module_name = sys.argv[1]

    # by convention, the virtual environment is to be created
    # with the same name as that of the module but should follow
    # the `regex: "^[a-zA-Z]*$"` thus, using the string search
    # to get the environment name, and ignore the same using
    # the `.gitignore` file
    env_name = "".join([i for i in module_name if i in list(string.ascii_letters)])
    print(f"Creating Module: `{module_name}`", end = " | ")
    print(f"Environment Name Convention: `{env_name}`")

    # create directories and structures using the `os` module
    ROOT = os.path.join(os.getcwd(), module_name) # ? can use `.`
    os.makedirs(os.path.join(ROOT, "data"))

    # add additional files as per requirements
    open(os.path.join(ROOT, "VERSION"), "w").close()
    open(os.path.join(ROOT, "secrets.yaml"), "w").close()

    # contents of `.gitignore`
    gitignore_ = [
        "# ignore python environment",
        f"{env_name}/",
        "",             # keep a blank line, forcefully
        "data/*",       # ignore all contents of data directory
        "secrets.yaml", # ? keep the secrets, may use env vars
        ""              # add a blank line at EOF
    ]

    with open(os.path.join(ROOT, ".gitignore"), "w") as f:
        f.write("\n".join(gitignore_))
