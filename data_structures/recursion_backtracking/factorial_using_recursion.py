"""
Factorial Using Recursion

Practice:
---------
Compute n! (factorial of n) using recursion.
n! = n * (n-1) * (n-2) * ... * 1, with 0! = 1.

Example:
--------
factorial(5)  -> 120   (5 * 4 * 3 * 2 * 1)
factorial(0)  -> 1

Approach: How I solved it
-------------------------
- Base case: n == 0 or n == 1 → return 1 (by definition 0! = 1, 1! = 1).
- Recurrence: n! = n * (n-1)!, so return n * factorial(n - 1).
- Total n recursive calls, O(1) work per call.

Time Complexity: O(n)
    - n recursive calls.

Space Complexity: O(n)
    - Recursion call stack depth is n.
"""


def factorial(n):
    """
    Return n! using recursion.

    :type n: int
    :rtype: int
    """
    if n == 1 or n == 0:
        return 1
    
    return n * factorial(n - 1)


if __name__ == "__main__":
    print(factorial(5))   # Expected: 120
    print(factorial(0))    # Expected: 1
    print(factorial(1))    # Expected: 1
    print(factorial(4))    # Expected: 24
