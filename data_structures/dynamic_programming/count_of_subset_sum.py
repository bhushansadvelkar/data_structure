"""
Count of Subset Sum Problem

Given an array of non-negative integers and a target sum, count how many
subsets have sum exactly equal to target.

Problem:
--------
Given nums and target, return the number of subsets whose sum is target.

Examples:
---------
Example 1:
    Input: nums = [2, 3, 5, 6, 8, 10], target = 10
    Output: 3
    Explanation: Subsets are [10], [2, 8], [2, 3, 5].

Example 2:
    Input: nums = [1, 1, 1, 1], target = 2
    Output: 6
    Explanation: Any two 1s can be chosen, so C(4,2) = 6.

Constraints:
------------
- 0 <= len(nums) <= 200
- 0 <= nums[i]
- 0 <= target

How I solved it:
----------------
(TODO)

Time Complexity: O(?)
Space Complexity: O(?)
"""

import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from data_structures.utils.test_utils import run_test


def count_of_subset_sum(nums, target):
    """
    Return the count of subsets of nums whose sum equals target.

    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    n = len(nums)
    t = [[False for _ in range(target + 1)] for _ in range(n + 1)]

    for i in range(n + 1):
        t[i][0] = True

    for i in range(1, n + 1):
        for j in range(1, target + 1):
            if nums[i - 1] <= j:
                t[i][j] = t[i - 1][j] + t[i - 1][j - nums[i - 1]]
            else:
                t[i][j] = t[i - 1][j]

    return t[n][target]


if __name__ == "__main__":
    run_test(
        count_of_subset_sum([2, 3, 5, 6, 8, 10], 10),
        3,
        "Example 1: three subsets sum to 10",
    )
    run_test(
        count_of_subset_sum([1, 1, 1, 1], 2),
        6,
        "Example 2: choose any two ones",
    )
    run_test(count_of_subset_sum([], 0), 1, "empty set has one subset with sum 0")
    run_test(count_of_subset_sum([1, 2, 3], 7), 0, "no subset sums to 7")
