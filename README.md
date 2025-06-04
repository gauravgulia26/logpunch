# Toolkit

A lightweight Python package for **Data Science** and **Machine Learning** projects, offering a customizable colored logger and an advanced exception tracking system.

[![PyPI version](https://img.shields.io/pypi/v/toolkit.svg)](https://pypi.org/project/toolkit/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/python-3.7%2B-blue)](https://www.python.org/)

## Overview

**Toolkit** is designed to streamline debugging and logging in data science and machine learning workflows. It provides:

- A **customizable logger** with colored terminal output and file-based logging, configurable for different log levels (DEBUG, INFO, WARNING, ERROR, CRITICAL).
- A **tracked exception** class that automatically captures the file name, function name, and line number of errors, simplifying debugging.

Whether you're building ML pipelines or analyzing data, Toolkit enhances traceability and monitoring with minimal setup.

## Features

- **Flexible Logging**: Log to both terminal and files with customizable formats and colors.
- **Automatic Error Tracking**: Capture detailed context (file, function, line number) for exceptions.
- **Lightweight**: Minimal dependencies for easy integration into any Python project.
- **Configurable**: Adjust log levels and directories to suit your needs.

## Requirements

- Python 3.7 or higher
- Pydantic
- Colorama

## Installation

Install Toolkit via PyPI:

```bash
pip install toolkit
```

## Usage

### Setting Up the Logger

Configure and initialize the logger with a few lines of code:

```python
from toolkit.customlogger import CustomLogger, LoggerConfig

# Define logger configuration
config = LoggerConfig(
    log_dir="logs",         # Directory for log files
    log_level="INFO"        # Options: DEBUG, INFO, WARNING, ERROR, CRITICAL
)

# Initialize logger
logger = CustomLogger(config).get_logger()

# Log messages
logger.debug("Debug message: useful for development.")
logger.info("Info message: pipeline started successfully.")
logger.warning("Warning message: disk space low.")
logger.error("Error message: file not found.")
logger.critical("Critical message: system crash!")
```

Log files are saved in the specified `log_dir` (e.g., `logs/`) with timestamps for easy tracking.

### Using the Custom Exception

The `TrackedException` class enhances error handling by automatically capturing the context of where the error occurred:

```python
from toolkit.customlogger import CustomLogger, LoggerConfig
from toolkit.customexception import TrackedException

# Logger setup
config = LoggerConfig(log_dir="logs", log_level="ERROR")
logger = CustomLogger(config).get_logger()

# Function with intentional error
def divide(a, b):
    if b == 0:
        raise TrackedException("Division by zero is not allowed.")
    return a / b

# Handle the exception
try:
    result = divide(10, 0)
except TrackedException as e:
    logger.error(str(e))
```

The logged error will include details like the file name, function name, and line number, e.g.:

```
ERROR: Division by zero is not allowed. (File: example.py, Function: divide, Line: 10)
```

## Why Use Toolkit?

- **Enhanced Debugging**: Pinpoint errors quickly with detailed exception context.
- **Clear Logging**: Colored logs improve readability during development and debugging.
- **Lightweight and Simple**: Integrate into any project without heavy dependencies.
- **Customizable**: Tailor logging behavior to your project’s needs.

## Contributing

We welcome contributions! To get started:

1. Fork the repository on [GitHub](https://github.com/your-repo/toolkit).
2. Clone your fork and create a new branch: `git checkout -b feature-name`.
3. Make your changes and commit them: `git commit -m "Add feature-name"`.
4. Push to your fork: `git push origin feature-name`.
5. Open a pull request with a clear description of your changes.

Please ensure your code follows PEP 8 guidelines and includes tests where applicable.

## License

Toolkit is licensed under the [MIT License](LICENSE).

## Contact

For questions or support, open an issue on [GitHub](https://github.com/your-repo/toolkit) or contact the maintainers at [grvgulia007@gmail.com](mailto:grvgulia007@gmail.com).