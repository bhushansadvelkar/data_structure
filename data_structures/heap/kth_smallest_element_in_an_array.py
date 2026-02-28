"""
Kth Smallest Element in an Array

Difficulty: Medium
Topics: Array, Divide and Conquer, Sorting, Heap, Quickselect


Problem:
--------
Given an integer array nums and an integer k, return the kth smallest element
in the array.

Note that it is the kth smallest element in the sorted order, not the kth
distinct element.

Can you solve it without sorting?

Examples:
---------
Example 1:
    Input: nums = [3, 2, 1, 5, 6, 4], k = 2
    Output: 2
    Explanation: Sorted ascending [1, 2, 3, 4, 5, 6]; 2nd smallest is 2.

Example 2:
    Input: nums = [3, 2, 3, 1, 2, 4, 5, 5, 6], k = 4
    Output: 3
    Explanation: Sorted ascending [1, 2, 2, 3, 3, 4, 5, 5, 6]; 4th smallest is 3.

Constraints:
------------
- 1 <= k <= nums.length <= 10^5
- -10^4 <= nums[i] <= 10^4

Approach 1: Sort
----------------
Sort the array and return the element at index k - 1 (kth smallest, 1-indexed).

Time Complexity: O(n log n)
    - Sorting n elements.

Space Complexity: O(1) or O(n)
    - O(1) if sort is in-place; O(n) for merge sort / language sort internals.

Approach 2: Max-heap of size k (simulated with negated min-heap)
---------------------------------------------------------------
Maintain a max-heap of size k (store -num in Python's min-heap). Push each
element; when size > k, pop the largest (root of max-heap). After processing
all, the root is the kth smallest.

Time Complexity: O(n log k)
    - n elements, each push/pop is O(log k); heap never exceeds size k.

Space Complexity: O(k)
    - Heap holds at most k elements.
"""

import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from data_structures.utils.test_utils import run_test

import heapq


class Solution(object):
    """Approach 1: Sort. Time O(n log n), Space O(1) or O(n)."""

    def findKthSmallest(self, nums, k):
        """
        Return the kth smallest element in the array.

        :type nums: List[int]
        :type k: int
        :rtype: int
        Time: O(n log n). Space: O(1) or O(n).
        """
        nums = sorted(nums)
        return nums[k - 1]


class Solution1(object):
    """Approach 2: Max-heap of size k (negated min-heap). Time O(n log k), Space O(k)."""

    def findKthSmallest(self, nums, k):
        """
        Return the kth smallest element in the array.

        :type nums: List[int]
        :type k: int
        :rtype: int
        Time: O(n log k). Space: O(k).
        """
        heap = []  # max-heap via -num (min-heap of negatives)

        for num in nums:
            heapq.heappush(heap, -num)
            if len(heap) > k:
                heapq.heappop(heap)

        return -heap[0]


if __name__ == "__main__":
    s = Solution()
    run_test(s.findKthSmallest([3, 2, 1, 5, 6, 4], 2), 2, "nums=[3,2,1,5,6,4], k=2")
    run_test(s.findKthSmallest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4), 3, "nums=[3,2,3,1,2,4,5,5,6], k=4")
    s1 = Solution1()
    run_test(s1.findKthSmallest([3, 2, 1, 5, 6, 4], 2), 2, "nums=[3,2,1,5,6,4], k=2")
    run_test(s1.findKthSmallest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4), 3, "nums=[3,2,3,1,2,4,5,5,6], k=4")
