def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except (ValueError, IndexError, KeyError, TypeError) as e:
            return str(e)

    return wrapper
