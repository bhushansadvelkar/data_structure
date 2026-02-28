"""
Maximum Sum Subarray of Size K

Difficulty: Easy
Topics: Array, Sliding Window


Problem:
--------
Given an array of integers and an integer k, find the maximum sum of any
contiguous subarray of size k.

Examples:
---------
Example 1:
    Input: nums = [2, 1, 5, 1, 3, 2], k = 3
    Output: 9
    Explanation: Subarrays of size 3: [2,1,5]=8, [1,5,1]=7, [5,1,3]=9, [1,3,2]=6.
    Maximum sum is 9.

Example 2:
    Input: nums = [2, 3, 4, 1, 5], k = 2
    Output: 7
    Explanation: [3, 4] has the maximum sum 7.

Constraints:
------------
- 1 <= k <= len(nums) <= 10^5
- -10^4 <= nums[i] <= 10^4

Approach:
---------
Sliding window of length k: compute sum of first k elements, then slide by
one step (add next element, subtract element leaving the window). Track the
maximum sum.

Time Complexity: O(n)
Space Complexity: O(1)
"""

import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from data_structures.utils.test_utils import run_test


class Solution(object):
    def maxSumSubarray(self, nums, k):
        """
        Return the maximum sum of any contiguous subarray of size k.

        Code: Sliding window. First window sum = sum(nums[:k]). Slide: add
        nums[i], subtract nums[i-k]; track max_sum.

        Time: O(n). Space: O(1).
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if not nums or k <= 0 or k > len(nums):
            return 0
        max_sum = sum(nums[:k])
        window_sum = max_sum

        for i in range(k, len(nums)):
            window_sum = window_sum + nums[i] - nums[i - k]
            max_sum = max(max_sum, window_sum)

        return max_sum


if __name__ == "__main__":
    sol = Solution()
    run_test(
        sol.maxSumSubarray([2, 1, 5, 1, 3, 2], 3),
        9,
        "nums=[2,1,5,1,3,2], k=3",
    )
    run_test(
        sol.maxSumSubarray([2, 3, 4, 1, 5], 2),
        7,
        "nums=[2,3,4,1,5], k=2",
    )
