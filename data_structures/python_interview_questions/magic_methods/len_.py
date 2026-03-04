"""
__len__ magic method

Returns the length (non-negative int) for len(obj).
"""


class Stack:
    def __init__(self, items=None):
        self._items = list(items or [])

    def __len__(self):
        return len(self._items)


if __name__ == "__main__":
    s = Stack([1, 2, 3])
    print(len(s))   # 3
