"""
2176. Count Equal and Divisible Pairs in an Array
https://leetcode.com/problems/count-equal-and-divisible-pairs-in-an-array/

Difficulty: Easy

Topics: Array

Problem:
--------
Given a 0-indexed integer array nums of length n and an integer k, return the
number of pairs (i, j) where 0 <= i < j < n such that:
  - nums[i] == nums[j]
  - (i * j) is divisible by k

Examples:
---------
Example 1:
    Input: nums = [3, 1, 2, 2, 2, 1, 3], k = 2
    Output: 4
    Explanation: (0,6), (2,3), (2,4), (3,4)

Example 2:
    Input: nums = [1, 2, 3, 4], k = 1
    Output: 0

Constraints:
------------
- 1 <= nums.length <= 100
- 1 <= nums[i], k <= 100

How I solved it:
---------------
1. Brute force: Iterate over all pairs (i, j) with i < j. For each pair, check
   if nums[i] == nums[j] and (i * j) % k == 0. Count valid pairs.

2. Optimized: Group indices by value using a dict. For each value, we only need
   to check pairs among indices that share that value (since nums[i] must equal
   nums[j]). Within each group, iterate over all pairs and check (i * j) % k == 0.
   This skips many pairs when there are many distinct values.

Time Complexity:
---------------
- Brute force: O(n²) — nested loops over all pairs.
- Optimized: O(n) to build groups + O(sum of group_size²). Worst case O(n²)
  when all elements are equal; best case O(n) when all distinct.

Space Complexity:
-----------------
- Brute force: O(1) — only a counter.
- Optimized: O(n) — dict storing indices per value.
"""

import os
import sys
from collections import defaultdict

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from data_structures.utils.test_utils import run_test


class Solution(object):
    def countPairs(self, nums, k):
        """
        Brute force: O(n^2) time, O(1) space.
        """
        counter = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j] and (i * j) % k == 0:
                    counter += 1
        return counter

    def countPairsOptimized(self, nums, k):
        """
        Group by value: only check pairs (i,j) where nums[i]==nums[j].
        When many distinct values, we skip most pairs.

        Time Complexity: O(n) build groups + O(sum over groups of size^2). Worst O(n^2).
        Space Complexity: O(n) for the groups dict.
        """
        groups = defaultdict(list)
        for i, v in enumerate(nums):
            groups[v].append(i)

        count = 0
        for indices in groups.values():
            for p in range(len(indices)):
                for q in range(p + 1, len(indices)):
                    i, j = indices[p], indices[q]
                    if (i * j) % k == 0:
                        count += 1
        return count


if __name__ == "__main__":
    sol = Solution()
    run_test(sol.countPairs([3, 1, 2, 2, 2, 1, 3], 2), 4, "Example 1")
    run_test(sol.countPairs([1, 2, 3, 4], 1), 0, "Example 2")
    run_test(sol.countPairsOptimized([3, 1, 2, 2, 2, 1, 3], 2), 4, "Optimized Example 1")
