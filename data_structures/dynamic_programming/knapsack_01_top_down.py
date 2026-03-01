"""
0/1 Knapsack Problem - Top-Down Approach

Top-down = recursion with memoization. Start from the full problem (n items,
capacity W) and recurse down to base cases; cache results in a table to avoid
repeated work.

Same recurrence as recursive solution: either include item n-1 or exclude it.
Table t[n][cap] = max value using first n items and capacity cap.

"""

import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from data_structures.utils.test_utils import run_test


def _kp(wt, val, cap, n, t):

    for i in range(1, n + 1):
        for j in range(1, cap + 1):
            if wt[i - 1] <= j:
                t[i][j] = max(
                    val[i - 1] + t[i-1][j - wt[i-1]],
                    t[i-1][j]
                )
            else:
                t[i][j] = t[i-1][j]

    return t[n][cap]


def knapsack_01(weights, values, capacity):
    """
    Return maximum value (0/1 knapsack) using top-down DP.

    :type weights: List[int]
    :type values: List[int]
    :type capacity: int
    :rtype: int
    """
    n = len(weights)
    t = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]
    return _kp(weights, values, capacity, n, t)


if __name__ == "__main__":
    run_test(
        knapsack_01([10, 20, 30], [60, 100, 120], 50),
        220,
        "weights=[10,20,30] values=[60,100,120] W=50",
    )
    run_test(
        knapsack_01([1, 2, 3], [10, 15, 40], 6),
        65,
        "weights=[1,2,3] values=[10,15,40] W=6",
    )
    run_test(
        knapsack_01([5, 4, 3, 2], [10, 40, 50, 20], 9),
        110,
        "weights=[5,4,3,2] values=[10,40,50,20] W=9",
    )
    run_test(knapsack_01([1], [10], 1), 10, "single item")
    run_test(knapsack_01([2], [10], 1), 0, "single item too heavy")
