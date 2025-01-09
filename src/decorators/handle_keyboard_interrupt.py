def handle_keyboard_interrupt(func):
    """Decorator to handle KeyboardInterrupt in functions."""
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyboardInterrupt:
            print("\n Operation cancelled. Returning to main menu.")
    return wrapper
