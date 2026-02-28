"""
0/1 Knapsack Problem

Difficulty: Medium
Topics: Dynamic Programming

Problem:
--------
Given n items with weights and values, and a knapsack of capacity W, choose
items to include so that total weight <= W and total value is maximized.
Each item can be used at most once (0 or 1).

Formally: Given weights[0..n-1], values[0..n-1], capacity W, return the
maximum value achievable.

Examples:
---------
Example 1:
    weights = [10, 20, 30], values = [60, 100, 120], W = 50
    Output: 220
    Explanation: Take items 1 and 2 (weight 20+30=50, value 100+120=220)

Example 2:
    weights = [1, 2, 3], values = [10, 15, 40], W = 6
    Output: 65
    Explanation: Take all items (1+2+3=6, value 10+15+40=65)

Example 3:
    weights = [5, 4, 3, 2], values = [10, 40, 50, 20], W = 9
    Output: 110
    Explanation: Take items 1,2,3 (weight 4+3+2=9, value 40+50+20=110)

Constraints:
------------
- 1 <= n <= 100
- 1 <= W <= 1000
- 1 <= weights[i], values[i] <= 1000

How I solved it:
----------------
I used plain recursion on index n and remaining capacity cap. For each item,
if it fits, I branch into include vs exclude and take max value. If it does
not fit, I skip it. Base case is n == 0 or cap == 0.

Time Complexity: O(n * W)
Space Complexity: O(n * W) or O(W) with 1D DP
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
        return max(val[n - 1] + kp(wt, val, cap - wt[n - 1], n - 1), kp(wt, val, cap, n - 1))
    else:
        return kp(wt, val, cap, n-1)

def knapsack_01(weights, values, capacity):
    """
    Return maximum value achievable with 0/1 knapsack.

    :type weights: List[int]
    :type values: List[int]
    :type capacity: int
    :rtype: int
    """
    n = len(weights)
    return kp(weights, values, capacity, n)


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
