"""
2. Write a decorator to log function name and arguments
"""

from functools import wraps


def log_args(func):
    """Decorator that logs function name, args, and kwargs before calling."""

    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"{func.__name__}(args={args}, kwargs={kwargs})")
        return func(*args, **kwargs)

    return wrapper


@log_args
def add(a, b):
    return a + b


if __name__ == "__main__":
    import os
    import sys

    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))
    from data_structures.utils.test_utils import run_test

    run_test(add(2, 3), 5, "add(2, 3)")
    run_test(add(a=1, b=2), 3, "add(a=1, b=2) kwargs")
