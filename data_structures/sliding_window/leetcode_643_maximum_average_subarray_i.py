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

Approach: How I solved it
-------------------------
Approach 1: Loop over each window, sum window, take max average.
Approach 2 (preferred): Sliding window of length k: compute sum of first k
elements, then slide by one step (add next element, subtract element leaving
the window). Track the maximum sum; return max_sum / float(k).

Time Complexity: O(n)
    - Sliding window (Approach 2): single pass; O(n*k) for Approach 1.
Space Complexity: O(1)
    - Sliding window uses only a few variables; O(n) for Approach 1.

Approach Diagram (Mermaid):
--------------------------
```mermaid
flowchart TD
    A[Compute sum of first k elements] --> B[Track as max_sum]
    B --> C[i = k to n-1]
    C --> D[window_sum += nums[i] - nums[i-k]]
    D --> E{window_sum > max_sum?}
    E -->|Yes| F[max_sum = window_sum]
    E -->|No| G[Continue]
    F --> G
    G --> H{More elements?}
    H -->|Yes| C
    H -->|No| I[Return max_sum / k]
```
"""

import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from data_structures.utils.test_utils import run_test


class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        Return the maximum average of any contiguous subarray of length k.

        Code: For each start i, window nums[i:i+k]; compute sum and average;
        take max over all windows.

        Time: O(n*k). Space: O(n) for list of averages.
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        sum_array = []

        for i in range(len(nums)):
            if len(nums[i:i+k]) >= k:
                sum_array.append(sum(nums[i:i+k]) / float(k))

        return max(sum_array)

    def findMaxAverage2(self, nums, k):
        """
        Approach 2: Sliding window. Return the maximum average of length k.

        Code: First window sum = sum(nums[:k]). Slide: add nums[i], subtract
        nums[i-k]; update max_avg. Return max_avg.

        Time: O(n). Space: O(1).
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        if not nums or k <= 0 or k > len(nums):
            return 0.0
        window_sum = sum(nums[:k])
        max_avg = window_sum / float(k)

        for i in range(k, len(nums)):
            window_sum = window_sum + nums[i] - nums[i - k]
            max_avg = max(max_avg, window_sum / float(k))

        return max_avg


if __name__ == "__main__":
    sol = Solution()
    # Approach 1 tests
    run_test(
        sol.findMaxAverage([1, 12, -5, -6, 50, 3], 4),
        12.75,
        "Approach 1: nums=[1,12,-5,-6,50,3], k=4",
    )
    run_test(
        sol.findMaxAverage([5], 1),
        5.0,
        "Approach 1: nums=[5], k=1",
    )
    # Approach 2 tests
    run_test(
        sol.findMaxAverage2([1, 12, -5, -6, 50, 3], 4),
        12.75,
        "Approach 2: nums=[1,12,-5,-6,50,3], k=4",
    )
    run_test(
        sol.findMaxAverage2([5], 1),
        5.0,
        "Approach 2: nums=[5], k=1",
    )
    run_test(
        sol.findMaxAverage2([0, 1, 1, 3, 3], 4),
        2.0,
        "Approach 2: nums=[0,1,1,3,3], k=4",
    )
    run_test(
        sol.findMaxAverage2([-1, -2, -3, -4, -5], 3),
        -2.0,
        "Approach 2: nums=[-1,-2,-3,-4,-5], k=3",
    )
