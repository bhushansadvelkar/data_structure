"""
10. Write decorator that works with *args and **kwargs

"""

from functools import wraps


def accepts_any_args(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)

    return wrapper


@accepts_any_args
def add(a, b):
    return a + b


@accepts_any_args
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"


if __name__ == "__main__":
    import os
    import sys

    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))
    from data_structures.utils.test_utils import run_test

    run_test(add(2, 3), 5, "add(2, 3)")
    run_test(add(a=1, b=2), 3, "add(a=1, b=2) kwargs")
    run_test(greet("World"), "Hello, World!", "greet('World')")
    run_test(greet("Alice", greeting="Hi"), "Hi, Alice!", "greet with kwargs")

