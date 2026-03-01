"""
Rod Cutting Problem (Unbounded Knapsack Variant)

Difficulty: Medium
Topics: Dynamic Programming

Problem:
--------
Given a rod of length n and an array prices where prices[i] is the value for a
piece of length (i+1), find the maximum total value obtainable by cutting the
rod and selling the pieces. You can cut a rod of length L into pieces of lengths
that sum to L; each length can be used any number of times (unbounded).

Formally: prices[0]=value of length 1, prices[1]=value of length 2, ... 
Return maximum value for rod length n.

Examples:
---------
Example 1:
    prices = [1, 5, 8, 9, 10, 17, 17, 20], n = 8
    Output: 22
    Explanation: Cut into lengths 2 and 6: 5 + 17 = 22.

Example 2:
    prices = [2, 5, 9, 10], n = 4
    Output: 11
    Explanation: Cut into lengths 1 and 3: 2 + 9 = 11.

Constraints:
------------
- 1 <= n <= 100
- 1 <= prices[i] <= 1000
- len(prices) >= n (prices for lengths 1..n)

How I solved it:
----------------
Model as unbounded knapsack: lengths 1..n = weights, prices = values, capacity = n.
DP[i][j] = max value using lengths 1..i to fill capacity j. Include length i: val[i-1] + dp[i][j-wt];
exclude: dp[i-1][j]. Use t[i][j-wt] (not t[i-1]) since same length can be used again.

Time Complexity: O(n^2)
Space Complexity: O(n^2)
"""

import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from data_structures.utils.test_utils import run_test

def _solve(wt, val, n, cap, t):
    """Unbounded knapsack: include item -> t[i][j-wt] (can repeat), exclude -> t[i-1][j]."""
    for i in range(1, n + 1):
        for j in range(1, cap + 1):
            if wt[i - 1] <= j:
                t[i][j] = max(
                    val[i - 1] + t[i][j - wt[i - 1]],
                    t[i - 1][j],
                )
            else:
                t[i][j] = t[i - 1][j]
    return t[n][cap]


def rod_cutting(prices, n):
    """
    Return maximum value obtainable by cutting rod of length n.

    :type prices: List[int]  # prices[i] = value for piece of length (i+1)
    :type n: int
    :rtype: int
    """
    # lengths 1..n as weights, prices as values, capacity = n
    wt = list(range(1, n + 1))
    val = prices[:n]
    t = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
    return _solve(wt, val, n, n, t)


if __name__ == "__main__":
    run_test(
        rod_cutting([1, 5, 8, 9, 10, 17, 17, 20], 8),
        22,
        "n=8, cut 2+6 -> 5+17=22",
    )
    run_test(
        rod_cutting([2, 5, 9, 10], 4),
        11,
        "n=4, cut 1+3 -> 2+9=11",
    )
    run_test(rod_cutting([1], 1), 1, "n=1, single piece")
