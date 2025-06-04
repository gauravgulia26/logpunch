import os


def create_file(path, content=""):
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)


def create_pypi_project_structure(lib_name="your_library"):
    os.makedirs(f"{lib_name}/{lib_name}", exist_ok=True)
    os.makedirs(f"{lib_name}/tests", exist_ok=True)

    # __init__.py and a placeholder module
    create_file(f"{lib_name}/{lib_name}/__init__.py", "")
    create_file(f"{lib_name}/{lib_name}/{lib_name}_module.py", "# Example module")

    # Test file
    create_file(
        f"{lib_name}/tests/test_something.py",
        f"""\
def test_example():
    assert 1 + 1 == 2
""",
    )

    # README.md
    create_file(f"{lib_name}/README.md", f"# {lib_name}\n\nDescribe your package here.")

    # LICENSE (MIT by default)
    create_file(
        f"{lib_name}/LICENSE",
        """\
MIT License

Copyright (c) 2025

Permission is hereby granted, free of charge, to any person obtaining a copy...
""",
    )

    # pyproject.toml
    create_file(
        f"{lib_name}/pyproject.toml",
        f"""\
[project]
name = "{lib_name}"
version = "0.1.0"
description = "A short description of your library"
readme = "README.md"
requires-python = ">=3.7"
license = {{text = "MIT"}}
authors = [
  {{ name = "Your Name", email = "you@example.com" }}
]
dependencies = []

[build-system]
requires = ["setuptools", "wheel"]
build-backend = "setuptools.build_meta"
""",
    )

    # MANIFEST.in
    create_file(f"{lib_name}/MANIFEST.in", "include README.md\ninclude LICENSE")

    # setup.cfg (optional)
    create_file(
        f"{lib_name}/setup.cfg",
        f"""\
[metadata]
name = {lib_name}
version = 0.1.0
description = A short description
long_description = file: README.md
long_description_content_type = text/markdown
author = Your Name
author_email = you@example.com
license = MIT

[options]
packages = find:
python_requires = >=3.7
""",
    )

    print(f"✅ Project '{lib_name}' structure created successfully.")


# Run the function
if __name__ == "__main__":
    create_pypi_project_structure("toolkit")
