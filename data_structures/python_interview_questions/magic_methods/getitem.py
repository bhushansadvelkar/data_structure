"""
__getitem__ magic method

Enables subscript access (obj[key]) and iteration. Accepts int index or slice.
"""


class MyList:
    def __init__(self, data):
        self._data = list(data)

    def __getitem__(self, key):
        if isinstance(key, slice):
            return MyList(self._data[key])
        return self._data[key]

    def __repr__(self):
        return f"MyList({self._data})"


if __name__ == "__main__":
    arr = MyList([10, 20, 30, 40, 50])

    print(arr[0])     # 10
    print(arr[-1])    # 50
    print(arr[1:4])   # MyList([20, 30, 40])
