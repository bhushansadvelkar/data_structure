"""
5. Write a decorator with arguments (repeat function N times)

"""

from functools import wraps


def repeat(times):

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = None 
            for _ in range(times):
                result = func(*args, **kwargs)

            return result
        return wrapper
    
    return decorator


@repeat(3)
def say_hi():
    print("Hi!")


@repeat(2)
def add(a, b):
    return a + b


if __name__ == "__main__":
    import os
    import sys

    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))
    from data_structures.utils.test_utils import run_test

    print("say_hi() output:")
    say_hi()
    run_test(add(2, 3), 5, "add(2, 3) runs twice, returns last result")
