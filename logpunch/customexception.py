import inspect
import os


class TrackedException(Exception):
    """
    Custom exception that captures the filename, function name, and line number
    where the exception was raised.
    """

    def __init__(self, message: str):
        """
        Initialize the TrackedException with a message and capture contextual information.

        Args:
            message (str): The error message describing the exception.
        """
        super().__init__(message)
        # Extract the current stack frame
        current_frame = inspect.currentframe()
        # Get the caller's frame (i.e., the frame that raised the exception)
        caller_frame = current_frame.f_back if current_frame else None
        if caller_frame:
            # Get the absolute path of the file
            file_path = caller_frame.f_code.co_filename
            # Extract the base filename
            self.filename = os.path.basename(file_path)
            self.function_name = caller_frame.f_code.co_name
            self.line_number = caller_frame.f_lineno
        else:
            self.filename = "<unknown>"
            self.function_name = "<unknown>"
            self.line_number = 0

    def __str__(self):
        """
        Return a formatted string representation of the exception, including contextual information.

        Returns:
            str: Formatted error message with context.
        """
        return (
            f"{super().__str__()} (Occurred in {self.filename}, "
            f"function {self.function_name}, line {self.line_number})"
        )