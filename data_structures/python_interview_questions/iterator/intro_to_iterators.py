"""
Introduction to Python Iterators
================================

An iterator is an object that implements the iterator protocol: __iter__ and __next__.
- __iter__ returns the iterator itself (or a new iterator for iterables)
- __next__ returns the next value, or raises StopIteration when done

Iterators are consumed: each next() advances the state. After exhaustion, they
don't restart—create a new iterator to iterate again.

Key concepts:
  - iter(obj) calls obj.__iter__()
  - next(obj) calls obj.__next__()
  - for x in obj: uses iter(obj) and repeatedly calls next()
  - Iterable: has __iter__ (e.g. list, dict). Iterator: has __iter__ and __next__
"""


class CountToN:

    def __init__(self, n):
        self.n = n 
        self.current = 0 

    def __iter__(self):
        return self 

    def __next__(self):
        if self.current >= self.n:
            raise StopIteration
        value = self.current
        self.current += 1
        return value



if __name__ == "__main__":
    import os
    import sys

    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))
    from data_structures.utils.test_utils import run_test

    # next() usage
    it = CountToN(3)
    run_test(next(it), 0, "next() first")
    run_test(next(it), 1, "next() second")
    run_test(next(it), 2, "next() third")

    # for loop
    run_test(list(CountToN(5)), [0, 1, 2, 3, 4], "for loop / list(CountToN(5))")

    # iter() returns self
    c = CountToN(2)
    run_test(iter(c) is c, True, "iter() returns self")

    print("\nNext: try custom_iterator_class.py, iter_and_next.py")
