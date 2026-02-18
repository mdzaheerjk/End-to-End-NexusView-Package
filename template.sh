# 1. Set your project name variable
export PROJECT_NAME="NexusViewPro"


# 2. Create the folder structure
mkdir -p .github/workflows src/$PROJECT_NAME tests/unit tests/integration


# 3. Create the files
touch .github/workflows/.gitkeep \
      src/$PROJECT_NAME/__init__.py \
      tests/__init__.py \
      tests/unit/__init__.py \
      tests/integration/__init__.py \
      requirements.txt \
      setup.py \
      pyproject.toml \
      setup.cfg \
      tox.ini \
      