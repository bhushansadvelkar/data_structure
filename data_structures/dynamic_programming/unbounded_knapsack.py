"""
Unbounded Knapsack Problem

Difficulty: Medium
Topics: Dynamic Programming

Problem:
--------
Given n item types with weights and values, and a knapsack capacity W, find the
maximum total value you can achieve. You can use each item type any number of
times (unbounded choice), as long as total weight does not exceed W.

Formally: Given weights[0..n-1], values[0..n-1], and capacity W, return the
maximum value achievable.

Examples:
---------
Example 1:
    weights = [1, 3, 4, 5], values = [10, 40, 50, 70], W = 8
    Output: 110
    Explanation: Pick weight 3 once (value 40) and weight 5 once (value 70).

Example 2:
    weights = [2, 4, 6], values = [5, 11, 13], W = 10
    Output: 27
    Explanation: Pick weight 4 once and weight 6 once (11 + 13 = 24) or
                 weight 2 five times (25); best is 27 from 4 + 2 + 2 + 2.

Constraints:
------------
- 1 <= n <= 100
- 1 <= W <= 1000
- 1 <= weights[i], values[i] <= 1000

How I solved it:
----------------
I used bottom-up DP with a 1D array where dp[c] stores the maximum value for
capacity c. For each capacity, try every item type that fits and update:
dp[c] = max(dp[c], values[i] + dp[c - weights[i]]).
Because this references dp in the same row/capacity pass, the same item can be
chosen multiple times, which is exactly the unbounded behavior.

Time Complexity: O(n * W)
Space Complexity: O(W)
"""

import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from data_structures.utils.test_utils import run_test


def kp(wt, val , cap , n):
    #base condition 
    if n == 0 or cap == 0:
        return 0 

    # choice: include item n-1 or exclude it
    if wt[n - 1] <= cap:
        return max(val[n - 1] + kp(wt, val, cap - wt[n - 1], n), kp(wt, val, cap, n - 1))
    else:
        return kp(wt, val, cap, n-1)

def unbounded_knapsack(weights, values, capacity):
    """
    Return maximum value achievable with unbounded knapsack.

    :type weights: List[int]
    :type values: List[int]
    :type capacity: int
    :rtype: int
    """
    n = len(weights)
    return kp(weights, values, capacity, n)


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
    run_test(unbounded_knapsack([1, 2, 5], [15, 20, 50], 7), 105, "coin-style: best 7x item1")
    run_test(unbounded_knapsack([5], [25], 5), 25, "single item fits exactly once")
    run_test(unbounded_knapsack([1, 2], [1, 3], 4), 6, "two items: 2+2 best")
    run_test(unbounded_knapsack([1, 2, 3], [2, 5, 9], 6), 18, "best: 3+3=18")
