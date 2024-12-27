# Python Development Skeleton Project

A GitHub template for Python development in a devcontainer.

## Overview

This repository provides a starting point for Python projects, utilizing a devcontainer setup for consistent development environments.

## Features

- **Devcontainer Configuration**: Configured for use with Visual Studio Code or other compatible IDEs.
- **Python Environment**: Assumes Python 3.13 (or adjust according to your needs).
- **Tools**: Includes [`uv`](https://docs.astral.sh/uv/), [`ruff`](https://docs.astral.sh/ruff/), and [`pytest`](https://docs.pytest.org/en/stable/) for package management, linting/formatting, and testing respectively.

## Setup

To use this template:

1. **Clone or Use as Template**:
   - Clone this repository:

     ```bash
     git clone https://github.com/nheirbaut/python-development-skeleton.git your-project-name
     ```

   - Or, use this as a template for a new repository via GitHub's "Use this template" button.

2. **Open in VS Code with Devcontainers**:
   - Open the cloned repository in Visual Studio Code.
   - When prompted, choose to "Reopen in Container" to start the devcontainer.

## Usage

- **Run Example Script**:

  ```bash
  uv run python src/main.py
  ```

- **Run Example Tests**:

   ```bash
   uv run pytest
   ```
