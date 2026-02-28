"""
48. Rotate Image
https://leetcode.com/problems/rotate-image/

Difficulty: Medium

Topics: Array, Math, Matrix

Problem:
--------
You are given an n x n 2D matrix representing an image. Rotate the image by
90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the
input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

Examples:
---------
Example 1:
    Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
    Output: [[7,4,1],[8,5,2],[9,6,3]]

Example 2:
    Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
    Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]

Constraints:
------------
- n == matrix.length == matrix[i].length
- 1 <= n <= 20
- -1000 <= matrix[i][j] <= 1000

Approach:
---------
Transpose + reverse rows: Rotating 90° clockwise is equivalent to (1) transposing
the matrix (swap matrix[row][col] with matrix[col][row] for row <= col to avoid
double-swapping), then (2) reversing each row in-place. Both steps modify the
matrix in-place.

Time Complexity: O(n²)
    - Transpose: visit each cell above/below diagonal once O(n²).
    - Reverse rows: each of n rows reversed O(n * n) = O(n²).

Space Complexity: O(1)
    - In-place; only a few loop variables.
"""

import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from data_structures.utils.test_utils import run_test


class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        
        n = len(matrix)
        
        for row in range(n):
            for col in range(row, n):
                matrix[row][col], matrix[col][row] = matrix[col][row],matrix[row][col]
                
        for i in range(n):
            matrix[i].reverse()


if __name__ == "__main__":
    s = Solution()

    m1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    s.rotate(m1)
    run_test(m1, [[7, 4, 1], [8, 5, 2], [9, 6, 3]], "Example 1: 3x3")

    m2 = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
    s.rotate(m2)
    run_test(m2, [[15, 13, 2, 5], [14, 3, 4, 1], [12, 6, 8, 9], [16, 7, 10, 11]], "Example 2: 4x4")
