"""
1. Write a decorator to measure execution time of a function

"""

from functools import wraps
import time


def measure_execution_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} took {end_time - start_time:.4f}s")
        return result

    return wrapper


@measure_execution_time
def slow_function():
    time.sleep(0.10)
    return "done"


if __name__ == "__main__":
    import os
    import sys

    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))
    from data_structures.utils.test_utils import run_test

    run_test(slow_function(), "done", "slow_function returns 'done'")
