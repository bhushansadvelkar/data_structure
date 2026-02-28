"""
Subset Sum Problem

Classic decision problem: given a set of non-negative integers and a target,
determine if there exists a subset that sums to exactly the target.

Problem:
--------
Given an array nums of non-negative integers and an integer target, return True
if some subset of nums sums to target, otherwise False.

Examples:
---------
Example 1:
    Input: nums = [3, 34, 4, 12, 5, 2], target = 9
    Output: True
    Explanation: Subset [4, 5] sums to 9.

Example 2:
    Input: nums = [3, 34, 4, 12, 5, 2], target = 30
    Output: False
    Explanation: No subset sums to 30.

Example 3:
    Input: nums = [], target = 0
    Output: True
    Explanation: Empty subset sums to 0.

Constraints:
------------
- 0 <= len(nums) <= 200
- 0 <= nums[i]
- 0 <= target

How I solved it:
----------------
I used classic 0/1 subset-sum DP with a boolean table t[i][j], meaning whether
sum j can be formed using the first i numbers. Transition is:
exclude current number, or include it if it does not exceed j.

Time Complexity: O(n * target)
Space Complexity: O(n * target)
"""

import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from data_structures.utils.test_utils import run_test


def subset_sum(nums, target):
    """
    Return True if some subset of nums sums to target, else False.

    :type nums: List[int]
    :type target: int
    :rtype: bool
    """
    n = len(nums)
    t = [[False for _ in range(target + 1)] for _ in range(n + 1)]

    for i in range(n + 1):
        t[i][0] = True

    for i in range(1, n + 1):
        for j in range(1, target + 1):
            if nums[i - 1] <= j:
                t[i][j] = t[i - 1][j] or t[i - 1][j - nums[i - 1]]
            else:
                t[i][j] = t[i - 1][j]

    return t[n][target]
    




if __name__ == "__main__":
    run_test(
        subset_sum([3, 34, 4, 12, 5, 2], 9),
        True,
        "Example 1: subset [4,5] sums to 9",
    )
    run_test(
        subset_sum([3, 34, 4, 12, 5, 2], 30),
        False,
        "Example 2: no subset sums to 30",
    )
    run_test(subset_sum([], 0), True, "empty array, target 0")
    run_test(subset_sum([1, 2, 3], 5), True, "[2,3] sums to 5")
    run_test(subset_sum([1, 2, 3], 7), False, "no subset sums to 7")
