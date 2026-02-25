"""
416. Partition Equal Subset Sum
https://leetcode.com/problems/partition-equal-subset-sum/

Difficulty: Medium
Topics: Array, Dynamic Programming

Problem:
--------
Given an integer array nums, return true if you can partition the array into
two subsets such that the sum of the elements in both subsets is equal, or
false otherwise.

Examples:
---------
Example 1:
    Input: nums = [1, 5, 11, 5]
    Output: true
    Explanation: The array can be partitioned as [1, 5, 5] and [11].

Example 2:
    Input: nums = [1, 2, 3, 5]
    Output: false
    Explanation: The array cannot be partitioned into equal sum subsets.

Constraints:
------------
- 1 <= nums.length <= 200
- 1 <= nums[i] <= 100

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


class Solution(object):
    def canPartition(self, nums):
        """
        Return true if nums can be partitioned into two subsets with equal sum.

        :type nums: List[int]
        :rtype: bool
        """
        sum_of_nums = sum(nums)
        if sum_of_nums % 2 != 0:
            return False
        
        target = sum_of_nums // 2
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
    sol = Solution()

    run_test(sol.canPartition([1, 5, 11, 5]), True, "Example 1: [1,5,11,5]")
    run_test(sol.canPartition([1, 2, 3, 5]), False, "Example 2: [1,2,3,5]")
    run_test(sol.canPartition([1, 1]), True, "two same: [1,1]")
    run_test(sol.canPartition([1, 2, 5]), False, "odd total: [1,2,5]")
