"""
Context manager class

Implement __enter__ and __exit__ to support `with` statement.
__enter__ runs before the block, __exit__ runs after (or on exception).
"""


class Timer:
    def __enter__(self):
        import time
        self.start = time.perf_counter()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        import time
        self.elapsed = time.perf_counter() - self.start
        return False  # don't suppress exceptions


if __name__ == "__main__":
    with Timer() as t:
        pass  # do work
    print(f"Elapsed: {t.elapsed:.6f}s")
