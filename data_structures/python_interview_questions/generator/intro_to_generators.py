"""
Introduction to Python Generators
=================================


A generator is a function that uses `yield` instead of `return`. When called,
it returns a generator object (an iterator) that produces values one at a time,
on demand. Generators are memory-efficient because they don't build the entire
sequence in memory—they produce values lazily.

Key concepts:
  - `yield` pauses the function and sends a value to the caller
  - Resumes from where it left off on next `next()` or for-loop iteration
  - Generator objects are iterators: support `next()` and `for` loop
  - Generator expression: `(x*2 for x in range(5))` — similar to list comp but lazy

Use cases: infinite sequences, large datasets, streaming, memory-efficient iteration.
"""

def count_up_to(n):
    i = 0 
    while i < n:
        yield i 
        i += 1


def simple_range(start, stop):
    i = start 
    while i < stop:
        yield i 
        i += 1



if __name__ == "__main__":
    import os
    import sys

    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))
    from data_structures.utils.test_utils import run_test

    cn = count_up_to(5)
    print(next(cn))
    print(next(cn))
    print(next(cn))
    print(next(cn))
    print(next(cn))

    sr = simple_range(4, 6)
    print(next(sr))  # 4
    print(next(sr))  # 5
    # next(sr) would raise StopIteration — only 2 values in range(4, 6)

    print("\nNext: try fibonacci.py, read_file_line_by_line.py")
