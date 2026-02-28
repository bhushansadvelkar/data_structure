"""
560. Subarray Sum Equals K
https://leetcode.com/problems/subarray-sum-equals-k/

Difficulty: Medium
Topics: Array, Hash Table, Prefix Sum, Sliding Window


Problem:
--------
Given an integer array nums and an integer k, return the total number of
subarrays whose sum equals k.

A subarray is a contiguous non-empty sequence of elements within an array.

Examples:
---------
Example 1:
    Input: nums = [1, 1, 1], k = 2
    Output: 2
    Explanation: The subarrays [1, 1] and [1, 1] (at indices 0–1 and 1–2).

Example 2:
    Input: nums = [1, 2, 3], k = 3
    Output: 2
    Explanation: The subarrays [1, 2] and [3].

Example 3:
    Input: nums = [1, 2, 1, 2, 1], k = 3
    Output: 4
    Explanation: The subarrays [1, 2], [2, 1], [1, 2], [2, 1] (at indices 0–1,
    1–2, 2–3, 3–4).

Example 4:
    Input: nums = [1], k = 0
    Output: 0
    Explanation: The only subarray is [1] with sum 1; no subarray has sum 0.

Constraints:
------------
- 1 <= nums.length <= 2 * 10^4
- -1000 <= nums[i] <= 1000
- -10^7 <= k <= 10^7

How I solved it:
----------------
Use prefix sum and a frequency map. The sum of subarray from j+1 to i is
prefix_sum[i] - prefix_sum[j]. We want that equal to k, so we need
prefix_sum[j] = prefix_sum[i] - k. For each index i, I add to the answer the
number of previous indices j whose prefix sum was (current_prefix - k). I keep
a map: prefix_sum -> count of times seen. I start with {0: 1} so that when
the whole prefix equals k, we count one (subarray from 0 to i). I update the
map after counting so we only use prefix sums from strictly earlier indices.
This works with negative numbers (unlike shrinking a sliding window).

Time Complexity: O(n)
    One pass over the array; each map lookup and update is O(1).

Space Complexity: O(n)
    The map can hold up to n distinct prefix sums in the worst case.
"""

import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from data_structures.utils.test_utils import run_test


class Solution(object):
    def subarraySum(self, nums, k):
        """
        Return the total number of subarrays whose sum equals k.

        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count = 0
        prefix_sum = 0
        freq = {0: 1}
        for x in nums:
            prefix_sum += x
            count += freq.get(prefix_sum - k, 0)
            freq[prefix_sum] = freq.get(prefix_sum, 0) + 1
        return count

if __name__ == "__main__":
    s = Solution()
    run_test(s.subarraySum([1, 1, 1], 2), 2, "nums=[1,1,1], k=2")
    run_test(s.subarraySum([1, 2, 3], 3), 2, "nums=[1,2,3], k=3")
    run_test(s.subarraySum([1, 2, 1, 2, 1], 3), 4, "nums=[1,2,1,2,1], k=3")
    run_test(s.subarraySum([1], 0), 0, "nums=[1], k=0")
