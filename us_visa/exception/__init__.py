import sys
import datetime
from us_visa.logger import logging

def error_message_detail(error, context=None):
    _, _, exc_tb = sys.exc_info() 
    file_name = exc_tb.tb_frame.f_code.co_filename
    line_number = exc_tb.tb_lineno
    error_type = type(error).__name__
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    # Include optional context if provided
    context_message = f" Context: {context}" if context else ""

    error_message = (
        f"Timestamp: {timestamp} | "
        f"Error Type: {error_type} | "
        f"File: [{file_name}] | "
        f"Line: [{line_number}] | "
        f"Message: [{str(error)}]{context_message}"
    )

    return error_message


class USvisaException(Exception):
    def __init__(self, error_message, context=None):
        """
        :param error_message: General error message string
        :param context: Optional context about where the error occurred
        """
        super().__init__(error_message)
        
        # Store the detailed error message
        self.error_message = error_message_detail(
            error_message, context=context
        )
        logging.error(self.error_message)

    def __str__(self):
        return self.error_message

