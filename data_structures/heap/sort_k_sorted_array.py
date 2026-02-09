"""
Sort a K Sorted Array

Difficulty: Medium
Topics: Array, Heap, Sorting

Problem:
--------
Given an array that is k-sorted (each element is at most k positions away
from its sorted position), sort the array efficiently.

Examples:
---------
Example 1:
    Input: arr = [6, 5, 3, 2, 8, 10, 9], k = 3
    Output: [2, 3, 5, 6, 8, 9, 10]

Example 2:
    Input: arr = [10, 9, 8, 7, 4, 70, 60, 50], k = 4
    Output: [4, 7, 8, 9, 10, 50, 60, 70]

Constraints:
------------
- 1 <= k <= n <= 10^5
- -10^4 <= arr[i] <= 10^4
"""

import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from data_structures.utils.test_utils import run_test


import heapq

class Solution(object):
    def sortKSorted(self, arr, k):
        """
        Return the sorted array (input is k-sorted).

        :type arr: List[int]
        :type k: int
        :rtype: List[int]
        """
        heap = arr[:k+1]
        heapq.heapify(heap)
        
        index = 0

        for i in range(k+1, len(arr)):
            arr[index] = heapq.heappop(heap)
            heapq.heappush(heap, arr[i])
            index += 1

        while heap:
            arr[index] = heapq.heappop(heap)
            index += 1

        return arr


if __name__ == "__main__":
    s = Solution()
    run_test(
        s.sortKSorted([6, 5, 3, 2, 8, 10, 9], 3),
        [2, 3, 5, 6, 8, 9, 10],
        "arr=[6,5,3,2,8,10,9], k=3",
    )
    run_test(
        s.sortKSorted([10, 9, 8, 7, 4, 70, 60, 50], 4),
        [4, 7, 8, 9, 10, 50, 60, 70],
        "arr=[10,9,8,7,4,70,60,50], k=4",
    )
