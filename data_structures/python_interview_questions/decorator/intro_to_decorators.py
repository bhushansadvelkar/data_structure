"""
Introduction to Python Decorators
=================================


A decorator is a function that wraps another function to extend its behavior
without modifying the original function's source code. Python supports
decorators using the @decorator_name syntax. Internally, decorators use
closures, where the outer function takes the original function as an argument
and returns a wrapper function.

Decorators are useful for cross-cutting concerns like:
  - Logging
  - Authorization
  - Caching
  - Timing execution

Example: Logging Decorator
-------------------------
Below is a decorator that logs function calls without modifying the function
itself. Read through it, run this file, then try implementing the exercises
in measure_execution_time, log_function_args, memoization, repeat_n_times, and args_kwargs_decorator.
"""

from functools import wraps


def log_decorator(func):
    """Decorator that logs function name, args, kwargs, and return value."""

    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Function Name: ", func.__name__)
        print("Args: ", args)
        print("Kwargs: ", kwargs)

        result = func(*args, **kwargs)

        print("Function executed")

        return result

    return wrapper

# --- Usage with @ syntax ---

@log_decorator
def add_values(a, b):
    return a + b


if __name__ == "__main__":
    import os
    import sys

    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))
    from data_structures.utils.test_utils import run_test

    run_test(add_values(2, 3), 5, "add_values(2, 3)")
    run_test(add_values(a=2, b=3), 5, "add_values(a=2, b=3) kwargs")
    run_test(add_values.__name__, "add_values", "add_values.__name__ preserved")
