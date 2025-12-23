import sys
from typing import Optional
from networksecurity.logging import logger


class NetworkSecurityException(Exception):
    """Custom exception class for Network Security application"""

    def __init__(self, error_message: str, error_details: sys = sys):
        """
        Initialize NetworkSecurityException

        Args:
            error_message: The error message or exception object
            error_details: The sys module to extract traceback info (default: sys)
        """
        super().__init__(error_message)

        # Extract traceback information
        _, _, exc_tb = error_details.exc_info()

        if exc_tb is not None:
            self.lineno: Optional[int] = exc_tb.tb_lineno
            self.file_name: Optional[str] = exc_tb.tb_frame.f_code.co_filename
        else:
            self.lineno: Optional[int] = None
            self.file_name: Optional[str] = None

        self.error_message: str = str(error_message)

    def __str__(self) -> str:
        """Return formatted error message"""
        return (
            f"Error occurred in python script name [{self.file_name}] "
            f"line number [{self.lineno}] "
            f"error message [{self.error_message}]"
        )


if __name__ == "__main__":
    try:
        logger.info("Enter the try block")
        a = 1 / 0
        logger.info("This line won't execute")
    except Exception as e:
        logger.error("Exception occurred", exc_info=True)
        raise NetworkSecurityException(e, sys) from e
