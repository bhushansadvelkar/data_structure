"""
912. Sort an Array
https://leetcode.com/problems/sort-an-array/

Difficulty: Medium
Topics: Array, Divide and Conquer, Sorting, Heap, Merge Sort

Problem:
--------
Given an array of integers nums, sort the array in ascending order and return it.

You must solve the problem without using any built-in sort functions in
O(n log n) time complexity and with the smallest space complexity possible.

Examples:
---------
Example 1:
    Input: nums = [5, 2, 3, 1]
    Output: [1, 2, 3, 5]

Example 2:
    Input: nums = [5, 1, 1, 2, 0, 0]
    Output: [0, 0, 1, 1, 2, 5]
    Note: values are not necessarily unique.

Constraints:
------------
- 1 <= nums.length <= 5 * 10^4
- -5 * 10^4 <= nums[i] <= 5 * 10^4

Approach (Heap Sort):
---------------------
1. Build a min-heap from the array in place using heapify (O(n)).
2. Repeatedly pop the minimum from the heap and append to the result; each
   pop is O(log n). After n pops we have the sorted order.
3. The min-heap keeps the smallest remaining element at the root, so
   popping in sequence yields ascending order.

Time Complexity: O(n log n)
    - heapify: O(n).
    - n × heappop: n × O(log n) = O(n log n).
    - Dominant term is O(n log n).

Space Complexity: O(n)
    - Result list holds n elements. Heap reuses the input array (in-place
      heapify and pop), so extra space beyond the output is O(1).
"""

import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from data_structures.utils.test_utils import run_test

import heapq 


class Solution(object):
    def sortArray(self, nums):
        """
        Return the array sorted in ascending order (heap sort).

        :type nums: List[int]
        :rtype: List[int]
        Time: O(n log n). Space: O(n) for result.
        """
        heapq.heapify(nums)
        result = []

        while nums:
            result.append(heapq.heappop(nums))

        return result


if __name__ == "__main__":
    s = Solution()
    run_test(s.sortArray([5, 2, 3, 1]), [1, 2, 3, 5], "nums=[5,2,3,1]")
    run_test(s.sortArray([5, 1, 1, 2, 0, 0]), [0, 0, 1, 1, 2, 5], "nums=[5,1,1,2,0,0]")
