"""
0/1 Knapsack Problem (Memoized)

Same problem as knapsack_01.py, solved with memoization using the decorator
from data_structures/python_interview_questions/decorator/memoization.py.
"""

import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from data_structures.utils.test_utils import run_test

def kp(wt, val , cap , n, t):
    #base condition 
    if n == 0 or cap == 0:
        return 0 

    if t[n][cap] != -1:
        return t[n][cap] 

    # choice: include item n-1 or exclude it
    if wt[n - 1] <= cap:
        t[n][cap] = max(val[n - 1] + kp(wt, val, cap - wt[n - 1], n - 1, t), kp(wt, val, cap, n - 1, t))
        return t[n][cap]
    else:
        t[n][cap] = kp(wt, val, cap, n - 1, t)
        return t[n][cap]

def knapsack_01(weights, values, capacity):
    """
    Return maximum value achievable with 0/1 knapsack (memoized recursion).
    """
    n = len(weights)
    t = [[-1 for _ in range(capacity + 1)] for _ in range(n + 1)]

    return kp(weights, values, capacity, n, t)

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
