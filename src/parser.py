from src.decorators.input_error import input_error

@input_error
def parse_input(user_input):
    """Parser for the input string. Returns the command and arguments."""
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, args
