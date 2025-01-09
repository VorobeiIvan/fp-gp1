import re
from datetime import datetime
from colorama import Fore, Style, init

# Initialize colorama
init()

def colorama_decorator(message_type):
    """
    A decorator to style messages with colorama based on their type.

    Args:
        message_type (str): Type of the message (e.g., 'error', 'success', 'warning', 'hint', 'default').

    Returns:
        Function: The wrapped function with colored output.
    """
    def decorator(func):
        def wrapper(*args, **kwargs):
            color = {
                'error': Fore.RED,          # Red for errors
                'success': Fore.GREEN,      # Green for success
                'warning': Fore.YELLOW,     # Yellow for warnings
                'hint': Fore.MAGENTA,       # Magenta for hints
                'default': Fore.WHITE       # White for default text
            }.get(message_type, Fore.WHITE)

            # Apply color and execute the function
            print(color + Style.BRIGHT, end="")
            result = func(*args, **kwargs)
            print(Style.RESET_ALL, end="")  # Reset style after the message
            return result

        return wrapper

    return decorator


@colorama_decorator('error')
def print_error(message):
    print(message)


@colorama_decorator('warning')
def print_warning(message):
    print(message)


@colorama_decorator('hint')
def print_hint(message):
    print(message)


@colorama_decorator('success')
def print_success(message):
    print(message)


@colorama_decorator('default')
def print_default(message):
    print(message)



