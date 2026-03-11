"""
Pass by value vs pass by reference (Python: pass by object reference)

Python passes references to objects. Reassigning the parameter doesn't affect the caller.
Mutating a mutable object (list, dict) is visible to the caller.
"""


def modify_immutable(x):
    x = x + 10
    print(f"Inside (immutable): x = {x}")


def modify_mutable(lst):
    lst.append(4)
    print(f"Inside (mutable): lst = {lst}")


def reassign_mutable(lst):
    lst = [10, 20]
    print(f"Inside (reassign): lst = {lst}")


if __name__ == "__main__":
    # Immutable (int): rebinding the local parameter does not affect the caller.
    n = 5
    modify_immutable(n)
    print(f"After (immutable): n = {n}")  # still 5

    # Mutable (list): in-place mutation is visible to the caller because both
    # names refer to the same underlying object.
    arr = [1, 2, 3]
    modify_mutable(arr)
    print(f"After (mutable): arr = {arr}")  # [1, 2, 3, 4]

    # Reassigning the param doesn't affect caller - only rebinds local name
    arr2 = [1, 2]
    reassign_mutable(arr2)
    print(f"After (reassign): arr2 = {arr2}")  # still [1, 2]
