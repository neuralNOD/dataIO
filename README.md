<div align = "justify">

1. Any additional code(s) that can be used by more than one *module* are to be included in [**`utilities`**](./utilities),
and the same is added in `PYTHONPATH` and not to be imported using `__init__.py` convention.
2. Each [**`module`**](./modules) have their own *environment* setup - named as per the module name `"^[a-zA-Z0-9]*$"`
(i.e. no special letters, example `market-data` module environment is named `marketdata`) and the environment is ignored.
   - `.gitignore` file per module ignores the environment name, however the global [`.gitignore`](./.gitignore) file ignores
   the general virtual environment names like `venv` etc. as per PEP8 standards.
   - each submodule has its own `requirements.txt` for setting up the python environment.
3. Disclaimers about each module is available in `DISCLAIMER.md` file with additional legal information(s).
4. A `VERSION` file is available under each module which keeps track of the module version.
5. `secrets.yaml` is a file available under each module which contains module level secrets and is ignored from commits.
6. Each module has the following general named directories:
   - `data` : a directory to store data files (generally raw files, which are processed),

</div>
