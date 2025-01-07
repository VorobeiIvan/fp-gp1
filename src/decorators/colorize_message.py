from colorama import Fore, Style, init

from constants import messages, messages_error

init(autoreset=True)


def colorize_message(func):
    """Декоратор для додавання кольорового оформлення та стилів."""

    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)

        if isinstance(result, str):
            if any(msg in result for msg in messages.values()):
                return f"{Fore.GREEN}{Style.BRIGHT}{result}"
            elif any(msg in result for msg in messages_error.values()):
                return f"{Fore.RED}{Style.BRIGHT}{result}"
            else:
                return f"{Fore.BLUE}{Style.BRIGHT}{result}"
        return result

    return wrapper
