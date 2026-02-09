"""
378. Kth Smallest Element in a Sorted Matrix
https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/

Difficulty: Medium
Topics: Array, Binary Search, Sorting, Heap, Matrix

Problem:
--------
Given an n x n matrix where each of the rows and columns is sorted in
ascending order, return the kth smallest element in the matrix.

Note that it is the kth smallest element in the sorted order, not the kth
distinct element.

You must find a solution with a memory complexity better than O(n^2).

Examples:
---------
Example 1:
    Input: matrix = [[1, 5, 9], [10, 11, 13], [12, 13, 15]], k = 8
    Output: 13
    Explanation: The elements in the matrix are [1, 5, 9, 10, 11, 12, 13, 13, 15],
    and the 8th smallest number is 13.

Example 2:
    Input: matrix = [[-5]], k = 1
    Output: -5

Constraints:
------------
- n == matrix.length == matrix[i].length
- 1 <= n <= 300
- -10^9 <= matrix[i][j] <= 10^9
- All rows and columns of matrix are guaranteed to be sorted in non-decreasing order.
- 1 <= k <= n^2

Follow-up:
----------
- Could you solve the problem with O(1) memory complexity?
- Could you solve the problem in O(n) time? (Advanced; see paper on selection in X+Y.)
"""

import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from data_structures.utils.test_utils import run_test

import heapq

class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        Return the kth smallest element in the sorted matrix.

        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        arr = [item for sublist in matrix for item in sublist]
        heap = []
        for num in arr:
            heapq.heappush(heap, -num)
            if len(heap) > k:
                heapq.heappop(heap)

        return -heap[0]

if __name__ == "__main__":
    s = Solution()
    run_test(
        s.kthSmallest([[1, 5, 9], [10, 11, 13], [12, 13, 15]], 8),
        13,
        "matrix=[[1,5,9],[10,11,13],[12,13,15]], k=8",
    )
    run_test(s.kthSmallest([[-5]], 1), -5, "matrix=[[-5]], k=1")
