"""
215. Kth Largest Element in an Array
https://leetcode.com/problems/kth-largest-element-in-an-array/

Difficulty: Medium
Topics: Array, Divide and Conquer, Sorting, Heap, Quickselect

Problem:
--------
Given an integer array nums and an integer k, return the kth largest element
in the array.

Note that it is the kth largest element in the sorted order, not the kth
distinct element.

Can you solve it without sorting?

Examples:
---------
Example 1:
    Input: nums = [3, 2, 1, 5, 6, 4], k = 2
    Output: 5
    Explanation: Sorted descending [6, 5, 4, 3, 2, 1]; 2nd largest is 5.

Example 2:
    Input: nums = [3, 2, 3, 1, 2, 4, 5, 5, 6], k = 4
    Output: 4
    Explanation: Sorted descending [6, 5, 5, 4, 3, 3, 2, 2, 1]; 4th largest is 4.

Constraints:
------------
- 1 <= k <= nums.length <= 10^5
- -10^4 <= nums[i] <= 10^4

Approach 1: Sort
----------------
Sort the array and return the element at index len(nums) - k (kth largest).

Time Complexity: O(n log n)
    - Sorting n elements.

Space Complexity: O(1) or O(n)
    - O(1) if sort is in-place; O(n) for merge sort / language sort internals.

Approach 2: Min-heap of size k
------------------------------
Maintain a min-heap of size k. Push each element; when size > k, pop the
smallest. After processing all, the root is the kth largest.

Time Complexity: O(n log k)
    - n elements, each push/pop is O(log k); heap never exceeds size k.

Space Complexity: O(k)
    - Heap holds at most k elements.

Approach Diagram - Min-heap (Mermaid):
--------------------------------------
```mermaid
flowchart TD
    A[Push num to min-heap] --> B{heap size > k?}
    B -->|Yes| C[Pop smallest]
    B -->|No| D[Continue]
    C --> D
    D --> E{More elements?}
    E -->|Yes| A
    E -->|No| F[Return heap[0]]
```
"""

import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from data_structures.utils.test_utils import run_test

import heapq


class Solution(object):
    """Approach 1: Sort. Time O(n log n), Space O(1) or O(n)."""

    def findKthLargest(self, nums, k):
        """
        Return the kth largest element in the array.

        :type nums: List[int]
        :type k: int
        :rtype: int
        Time: O(n log n). Space: O(1) or O(n).
        """
        nums.sort()
        return nums[-k]


class Solution1(object):
    """Approach 2: Min-heap of size k. Time O(n log k), Space O(k)."""

    def findKthLargest(self, nums, k):
        """
        Return the kth largest element in the array.

        :type nums: List[int]
        :type k: int
        :rtype: int
        Time: O(n log k). Space: O(k).
        """
        heap = []

        for num in nums:
            heapq.heappush(heap, num)
            if len(heap) > k:
                heapq.heappop(heap)

        return heap[0]


if __name__ == "__main__":
    s = Solution()
    run_test(s.findKthLargest([3, 2, 1, 5, 6, 4], 2), 5, "nums=[3,2,1,5,6,4], k=2")
    run_test(s.findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4), 4, "nums=[3,2,3,1,2,4,5,5,6], k=4")
    s = Solution1()
    run_test(s.findKthLargest([3, 2, 1, 5, 6, 4], 2), 5, "nums=[3,2,1,5,6,4], k=2")
    run_test(s.findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4), 4, "nums=[3,2,3,1,2,4,5,5,6], k=4")