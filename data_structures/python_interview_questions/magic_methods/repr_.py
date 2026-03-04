"""
__repr__ magic method

Unambiguous representation for developers. Used by repr() and in debugger.
Ideal: eval(repr(obj)) would recreate the object.
"""


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point({self.x}, {self.y})"


if __name__ == "__main__":
    p = Point(3, 4)
    print(repr(p))   # Point(3, 4)
