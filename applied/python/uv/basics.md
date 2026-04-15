## UV Introduction
UV is a python tool that manages the environment creation, package management for modern python projects and is very fast.

## Main commands
- uv init project_name: initializes a python project with basic structure
- uv python list: show availble python versions
- uv python install version: installs the python
- uv venv: create a virtual environment
- uv add package_name: install a package in the env
    - add --dev for adding to dev dependecies
- uv remove package_name
- uv sync: adds the dependecies to the venv which are in the lock file
    - use --no-dev for adding only production dependencies
- uv run module or filename

## UV environment setup
- use UV_INDEX_URL=https://your-mirror/simple env variable for custom pypi mirror

## Best practices for project structure
- pyproject.toml file : contains the metadata about the python project it's authors etc, it's dependencies and tooling. It is useful for standardizing the distribution of the source code, it defines how projects are built, configured and packaged but it does not have exact dependencies(that's the usecase for lock files). It also has build backend configuration how the project is built. It is recommended to use toml file rather than setup.py if possible. 
- src folder for keeping the source code
- tests folder for keeping the unit tests
