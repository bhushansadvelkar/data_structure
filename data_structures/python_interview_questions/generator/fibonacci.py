"""
16. Write generator for Fibonacci sequence

"""
def generate_fibonacci(n):
    """Yield the first n Fibonacci numbers: 0, 1, 1, 2, 3, 5, ..."""
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


if __name__ == "__main__":
    import os
    import sys

    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))
    from data_structures.utils.test_utils import run_test

    run_test(list(generate_fibonacci(5)), [0, 1, 1, 2, 3], "first 5 Fibonacci")
    run_test(list(generate_fibonacci(1)), [0], "first 1 Fibonacci")
