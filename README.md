# <PROJECT>

Code for the analysis of <...>.

## Acknowledgement
The code is <...>.

## Installation

```
pip install -e <path_to_repo>
```

After installation with the above command, the python scripts in the folder `scripts` will be available to be called in `bash` and accessible via auto-completion.

## Development

#### Testing

Testing can be automatically performed by executing `pytest` in the repo. All modules and functions that start with `test_` will be executed as test functions.

Automatic testing of test code together with packaging is setup via `tox`. Executing `tox` in the repo will first install the package (relying on `setup.py`, not `requirements.txt` (!)), and then execute the defined test commands:
 - `tox -e pytest` for running the tests with `pytest`,
 - `tox -e code_check` for running the style and type checks of the code with `flake8` and `mypy`. `flake8` is useful to check code style. `mypy` performs type checking (only where implemented).

#### Pre-commit hooks

There is a setup for `pre-commit` hooks. These are scripts that are executed before each commit.

The settings here include
- `black` which automatically applies code style standards which minimises the diff lines per commit (useful for smaller PRs and faster code review) and ensures a uniform code style,
- `flake8` which gives additional hints for code style conventions.

**After cloning** a repo locally, execute `pre-commit install` in the repo. After that, the hooks will be automatically called at each commit.

**NOTE** `pre-commit` is part of `requirements-dev.txt` and must be installed first.
