"""
Longest Subarray with Sum K (Sliding Window)

Difficulty: Medium
Topics: Array, Sliding Window

Problem:
--------
Given an array of non-negative integers nums and an integer k, find the
length of the longest contiguous subarray whose sum equals k. If no such
subarray exists, return 0.

A subarray is a contiguous non-empty sequence of elements within an array.

Note: This sliding-window solution works only when all elements are
non-negative. For arrays with negative numbers, use prefix sum + hash map
(see e.g. largest_subarray_of_sum_k.py).

Examples:
---------
Example 1:
    Input: nums = [1, 1, 1], k = 2
    Output: 2
    Explanation: Longest subarray with sum 2 is [1, 1] (length 2).

Example 2:
    Input: nums = [1, 2, 3], k = 3
    Output: 2
    Explanation: [1, 2] has sum 3 and length 2; [3] has length 1. So 2.

Example 3:
    Input: nums = [2, 1, 1, 1, 1, 1], k = 5
    Output: 5
    Explanation: [1, 1, 1, 1, 1] has sum 5 and length 5.

Constraints:
------------
- 1 <= nums.length <= 10^5
- 0 <= nums[i] <= 10^4
- 0 <= k <= 10^9

How I solved it:
----------------
Sliding window with two pointers: expand by moving right and adding nums[right]
to current_sum. When current_sum exceeds k, shrink from the left (subtract
nums[left], move left) until current_sum <= k. When current_sum equals k,
update max_length with the current window size (right - left + 1). Because
all elements are non-negative, shrinking never skips a valid longer window.

Time Complexity: O(n)
    Each element is added at most once and removed at most once.

Space Complexity: O(1)
    Only a few variables (left, right, current_sum, max_length).
"""

import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from data_structures.utils.test_utils import run_test


def longestSubarray(nums, k):
    """
    Return the length of the longest contiguous subarray with sum k.
    Works only when all elements in nums are non-negative.

    :type nums: List[int]
    :type k: int
    :rtype: int
    """
    left = 0
    current_sum = 0
    max_length = 0

    for right in range(len(nums)):
        current_sum += nums[right]

        # shrink window if sum > k
        while current_sum > k and left <= right:
            current_sum -= nums[left]
            left += 1

        # check if equals k
        if current_sum == k:
            max_length = max(max_length, right - left + 1)

    return max_length


if __name__ == "__main__":
    run_test(longestSubarray([1, 1, 1], 2), 2, "nums=[1,1,1], k=2")
    run_test(longestSubarray([1, 2, 3], 3), 2, "nums=[1,2,3], k=3")
    run_test(longestSubarray([2, 1, 1, 1, 1, 1], 5), 5, "nums=[2,1,1,1,1,1], k=5")
    run_test(longestSubarray([1], 0), 0, "nums=[1], k=0")
