"""
NumPy examples - array creation, indexing, operations, broadcasting

Requires: pip install numpy  (or: pip install -r requirements.txt)
"""

import numpy as np


if __name__ == "__main__":
    # Create arrays
    a = np.array([1, 2, 3, 4, 5])
    b = np.zeros((2, 3))
    c = np.ones((2, 2))
    d = np.arange(0, 10, 2)
    e = np.linspace(0, 1, 5)

    print("arange:", d)
    print("linspace:", e)

    # Indexing and slicing
    arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    print("arr[1, 2]:", arr[1, 2])
    print("arr[:, 1]:", arr[:, 1])
    print("arr[1:, :2]:\n", arr[1:, :2])

    # Element-wise ops and broadcasting
    x = np.array([1, 2, 3])
    print("x * 2:", x * 2)
    print("x + np.array([10, 10, 10]):", x + np.array([10, 10, 10]))
