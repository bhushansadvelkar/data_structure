"""
__eq__ magic method

Defines equality (==) for instances. Should return True/False.

This implementation compares another Point by reading other.x and other.y.
Comparing to a non-Point (for example a tuple) will raise AttributeError unless
you add a type check and return NotImplemented for unknown types.
"""

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y 

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


if __name__ == "__main__":
    p1 = Point(1, 2)
    p2 = Point(1, 2)
    p3 = Point(3, 4)

    print(p1 == p2)   # True
    print(p1 == p3)   # False
    # print(p1 == (1, 2))  # AttributeError: 'tuple' object has no attribute 'x'
