"""
4. Write a decorator for memoization (cache results)
"""

from functools import wraps


def memoize(func):

    cache = {}

    @wraps(func)
    def wrapper(*args, **kwargs):
        key = (args, tuple(sorted(kwargs.items)))
        if key not in cache:
            cache[key] = func(*args, **kwargs)
        return cache[key]

    return wrapper

@memoize
def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)


if __name__ == "__main__":
    import os
    import sys

    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))
    from data_structures.utils.test_utils import run_test

    run_test(fib(0), 0, "fib(0)")
    run_test(fib(1), 1, "fib(1)")
    run_test(fib(10), 55, "fib(10)")
