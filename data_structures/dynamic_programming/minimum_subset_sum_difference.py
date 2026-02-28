"""
Minimum Subset Sum Difference

Partition an array into two subsets such that the absolute difference of their
sums is minimized, and return that minimum difference.

Problem:
--------
Given an array nums of non-negative integers, divide it into two subsets S1
and S2 such that |sum(S1) - sum(S2)| is minimum. Return the minimum value.

Examples:
---------
Example 1:
    Input: nums = [1, 6, 11, 5]
    Output: 1
    Explanation: Subsets [1, 5, 6] and [11] have sums 12 and 11.

Example 2:
    Input: nums = [1, 2, 7]
    Output: 4
    Explanation: Subsets [1, 2] and [7] have sums 3 and 7.

Example 3:
    Input: nums = [1, 2, 3, 9]
    Output: 3
    Explanation: Subsets [1, 2, 3] and [9] have sums 6 and 9.

Constraints:
------------
- 0 <= len(nums) <= 200
- 0 <= nums[i]

How I solved it:
----------------
I converted the problem into a subset-sum reachability DP. If total sum is S,
the best split is achieved by finding a reachable subset sum s1 closest to S/2.
I build a boolean table t[i][j] (using first i items to make sum j), then scan
from S/2 downward to get the first reachable s1 and compute S - 2*s1.

Time Complexity: O(n * S)
Space Complexity: O(n * S)
"""

import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from data_structures.utils.test_utils import run_test


def minimum_subset_sum_difference(nums):
    """
    Return the minimum absolute difference between sums of two subsets.

    :type nums: List[int]
    :rtype: int
    """
    n = len(nums)
    total = sum(nums)
    target = total // 2

    t = [[False for _ in range(target + 1)] for _ in range(n + 1)]

    for i in range(n + 1):
        t[i][0] = True

    for i in range(1, n + 1):
        for j in range(1, target + 1):
            if nums[i - 1] <= j:
                t[i][j] = t[i - 1][j] or t[i - 1][j - nums[i - 1]]
            else:
                t[i][j] = t[i - 1][j]

    for s1 in range(target, -1, -1):
        if t[n][s1]:
            return total - (2 * s1)

    return 0


if __name__ == "__main__":
    run_test(
        minimum_subset_sum_difference([1, 6, 11, 5]),
        1,
        "Example 1: minimum difference is 1",
    )
    run_test(
        minimum_subset_sum_difference([1, 2, 7]),
        4,
        "Example 2: minimum difference is 4",
    )
    run_test(
        minimum_subset_sum_difference([1, 2, 3, 9]),
        3,
        "Example 3: minimum difference is 3",
    )
    run_test(minimum_subset_sum_difference([]), 0, "empty array")
