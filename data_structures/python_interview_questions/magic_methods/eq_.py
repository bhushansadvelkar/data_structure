"""
__eq__ magic method

Defines equality (==) for instances. Should return True/False.
Use NotImplemented when comparing to unknown types so Python can try the other object's __eq__.
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
    print(p1 == (1, 2))  # False (NotImplemented delegates, tuple has no Point handling)
