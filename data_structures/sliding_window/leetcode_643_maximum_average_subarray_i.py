"""
643. Maximum Average Subarray I
https://leetcode.com/problems/maximum-average-subarray-i/

Difficulty: Easy
Topics: Array, Sliding Window

Problem:
--------
You are given an integer array nums consisting of n elements, and an integer k.

Find a contiguous subarray whose length is equal to k that has the maximum
average value and return this value. Any answer with a calculation error less
than 10^-5 will be accepted.

Examples:
---------
Example 1:
    Input: nums = [1, 12, -5, -6, 50, 3], k = 4
    Output: 12.75
    Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75

Example 2:
    Input: nums = [5], k = 1
    Output: 5.0

Constraints:
------------
- n == nums.length
- 1 <= k <= n <= 10^5
- -10^4 <= nums[i] <= 10^4

Approach:
---------
Sliding window of length k: compute sum of first k elements, then slide by
one step at a time (add next element, subtract element leaving the window).
Track the maximum sum; return max_sum / k.

Time Complexity: O(n)
    - Single pass; each window update is O(1).

Space Complexity: O(1)
    - Only a few variables for current sum and max sum.
"""

import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from data_structures.utils.test_utils import run_test


class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        Return the maximum average of any contiguous subarray of length k.

        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        sum_array = []

        for i in range(len(nums)):
            if len(nums[i:i+k]) >= k:
                sum_array.append(sum(nums[i:i+k]) / float(k))

        return max(sum_array)


if __name__ == "__main__":
    sol = Solution()
    run_test(
        sol.findMaxAverage([1, 12, -5, -6, 50, 3], 4),
        12.75,
        "nums=[1,12,-5,-6,50,3], k=4",
    )
    run_test(
        sol.findMaxAverage([5], 1),
        5.0,
        "nums=[5], k=1",
    )
