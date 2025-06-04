import logging
import os
from datetime import datetime
from typing import Optional
from pathlib import Path
from colorama import Fore, Style, init as colorama_init
from pydantic import BaseModel, Field, ValidationError

# Initialize colorama
colorama_init(autoreset=True)


class LoggerConfig(BaseModel):
    """
    Configuration model for the custom logger.

    Attributes:
        log_dir (DirectoryPath): Path to the directory where log files will be stored.
        log_level (str): Logging level (e.g., 'DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL').
    """

    log_dir: Path = Field(..., description="POSIX Path for the Directory to store log files.")
    log_level: str = Field(description="Logging level.",default='INFO')

    class Config:
        validate_assignment = True


class ColoredFormatter(logging.Formatter):
    """
    Custom formatter to add colors to log messages based on their severity level.
    """

    # Mapping of log levels to their corresponding colors
    LOG_COLORS = {
        logging.DEBUG: Fore.CYAN,
        logging.INFO: Fore.GREEN,
        logging.WARNING: Fore.YELLOW,
        logging.ERROR: Fore.RED,
        logging.CRITICAL: Fore.MAGENTA + Style.BRIGHT,
    }

    def format(self, record: logging.LogRecord) -> str:
        """
        Format the log record with appropriate color.

        Args:
            record (logging.LogRecord): The log record to format.

        Returns:
            str: The formatted log message with color.
        """
        log_color = self.LOG_COLORS.get(record.levelno, "")
        formatted_message = super().format(record)
        return f"{log_color}{formatted_message}{Style.RESET_ALL}"


class CustomLogger:
    """
    Custom logger that outputs colored logs to the terminal and writes logs to a file.

    Attributes:
        logger (logging.Logger): The configured logger instance.
    """

    def __init__(self, config: LoggerConfig, logger_name: Optional[str] = None):
        """
        Initialize the custom logger.

        Args:
            config (LoggerConfig): Configuration for the logger.
            logger_name (Optional[str]): Name of the logger. Defaults to the module name.
        """
        self.logger = logging.getLogger(logger_name or __name__)
        self.logger.setLevel(getattr(logging, config.log_level.upper(), logging.INFO))
        self.logger.propagate = False  # Prevent duplicate logs

        # Formatter for log messages
        formatter = logging.Formatter(
            fmt="%(asctime)s | %(levelname)s | %(message)s", datefmt="%Y-%m-%d-%H:%M:%S"
        )

        # Colored formatter for console output
        colored_formatter = ColoredFormatter(
            fmt="%(asctime)s | %(levelname)s | %(message)s", datefmt="%Y-%m-%d-%H:%M:%S"
        )

        # Console handler with colored output
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(colored_formatter)
        self.logger.addHandler(console_handler)

        # Ensure log directory exists
        os.makedirs(config.log_dir, exist_ok=True)

        # File handler
        timestamp = datetime.now().strftime("%Y:%m:%d-%H:%M:%S")
        log_file_path = os.path.join(config.log_dir, f"{timestamp}.log")
        file_handler = logging.FileHandler(log_file_path)
        file_handler.setFormatter(formatter)
        self.logger.addHandler(file_handler)

    def get_logger(self) -> logging.Logger:
        """
        Retrieve the configured logger instance.

        Returns:
            logging.Logger: The logger instance.
        """
        return self.logger