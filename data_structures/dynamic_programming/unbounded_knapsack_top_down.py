"""
Unbounded Knapsack Problem - Top-Down (Memoized Recursion)

Top-down = recursion with memoization. Start from full problem (capacity W,
all n items) and recurse down to base cases; cache results to avoid repeated work.

Same recurrence as plain recursion: include item (keep n to allow repeat) or
exclude. Table t[n][cap] = max value using first n item types and capacity cap.
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
                    val[i - 1] + t[i][j - wt[i-1]],
                    t[i-1][j]
                )
            else:
                t[i][j] = t[i-1][j]

    return t[n][cap]


def unbounded_knapsack(weights, values, capacity):
    """
    Return maximum value (unbounded knapsack) using top-down memoized DP.

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
        unbounded_knapsack([1, 3, 4, 5], [10, 40, 50, 70], 8),
        110,
        "weights=[1,3,4,5] values=[10,40,50,70] W=8",
    )
    run_test(
        unbounded_knapsack([2, 4, 6], [5, 11, 13], 10),
        27,
        "weights=[2,4,6] values=[5,11,13] W=10",
    )
    run_test(unbounded_knapsack([5], [10], 3), 0, "single item too heavy")
    run_test(unbounded_knapsack([3], [8], 9), 24, "single item repeatable (3+3+3=9)")
    run_test(unbounded_knapsack([1], [1], 0), 0, "capacity 0")
    run_test(unbounded_knapsack([2], [5], 10), 25, "repeat weight-2 item 5 times")
    run_test(unbounded_knapsack([1, 2, 5], [15, 20, 50], 7), 105, "coin-style")
    run_test(unbounded_knapsack([5], [25], 5), 25, "single item fits exactly once")
    run_test(unbounded_knapsack([1, 2], [1, 3], 4), 6, "two items: 2+2 best")
    run_test(unbounded_knapsack([1, 2, 3], [2, 5, 9], 6), 18, "best: 3+3=18")
