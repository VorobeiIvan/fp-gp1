from decorators.input_error import input_error


@input_error
def parse_input(user_input):
    """Парсер для введеного рядка. Повертає команду та аргументи."""
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, args
