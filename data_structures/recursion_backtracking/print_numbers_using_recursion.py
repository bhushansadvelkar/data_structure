"""
Print Numbers Using Recursion


Practice:
---------
1. Print numbers from 1 to n (ascending)
2. Print numbers from n to 1 (descending)

Example:
--------
print_1_to_n(5)  -> 1 2 3 4 5
print_n_to_1(5)  -> 5 4 3 2 1

Approach: How I solved it
-------------------------
- print_1_to_n: Base case n==1 → print 1. Else recurse on n-1 first, then print n so numbers print in ascending order as the stack unwinds.
- print_n_to_1: Base case n==1 → print 1. Else print n first, then recurse on n-1 so numbers print in descending order on the way down.
- Each call does O(1) work; total n calls.

Time Complexity: O(n)
    - n recursive calls, O(1) work per call.

Space Complexity: O(n)
    - Recursion call stack depth is n (worst case).
"""

from data_structures.utils.test_utils import run_test


def print_1_to_n(n):
    """
    Print numbers from 1 to n (ascending) using recursion.

    :type n: int
    :rtype: None
    """
    if n == 1:
        print(1)
        return
    
    print_1_to_n(n - 1)
    print(n)
    


def print_n_to_1(n):
    """
    Print numbers from n to 1 (descending) using recursion.

    :type n: int
    :rtype: None
    """
    if n == 1:
        print(1)
        return 
    
    print(n)
    print_n_to_1(n-1)


if __name__ == "__main__":
    print("print_1_to_n(5):")
    print_1_to_n(5)
    run_test(None, None, "print_1_to_n(5)", compare=False)
    print("\nprint_1_to_n(1):")
    print_1_to_n(1)
    run_test(None, None, "print_1_to_n(1)", compare=False)
    print("\nprint_n_to_1(5):")
    print_n_to_1(5)
    run_test(None, None, "print_n_to_1(5)", compare=False)
    print("\nprint_n_to_1(1):")
    print_n_to_1(1)
    run_test(None, None, "print_n_to_1(1)", compare=False)
