"""
__str__ magic method

Human-readable string for print(). Falls back to __repr__ if not defined.
"""


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __repr__(self):
        return f"Point({self.x}, {self.y})"


if __name__ == "__main__":
    p = Point(3, 4)
    print(str(p))   # (3, 4)
    print(p)        # (3, 4)  - print uses __str__
