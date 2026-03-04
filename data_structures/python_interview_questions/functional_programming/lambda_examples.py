"""
Lambda functions - anonymous single-expression functions

Syntax: lambda args: expression
Common with sort, map, filter.
"""


if __name__ == "__main__":
    # Sort by custom key
    pairs = [(1, "one"), (3, "three"), (2, "two")]
    sorted(pairs, key=lambda x:x[1])
    print(pairs)  # by string: [(1,'one'), (3,'three'), (2,'two')]

    # Map
    nums = [1, 2, 3, 4]
    double = list(map(lambda x : x* 2, nums))
    print(double)  # [2, 4, 6, 8]

    # Filter
    evens = list(filter(lambda x: x % 2 == 0, nums))
    print(evens)  # [2, 4]

    square = lambda x: x*x 
    print(square(2))
