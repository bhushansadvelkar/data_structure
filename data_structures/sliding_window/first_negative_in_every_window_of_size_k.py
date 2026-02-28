"""
First Negative Number in Every Window of Size K

Difficulty: Medium
Topics: Array, Sliding Window, Queue


Problem:
--------
Given an array of integers and an integer k, for each window of size k find
the first negative number in that window (from left to right). If there is no
negative number in the window, return 0 (or use 0 as the result for that window).

Examples:
---------
Example 1:
    Input: arr = [12, -1, -7, 8, -15, 30, 16, 28], k = 3
    Output: [-1, -1, -7, -15, -15, 0]
    Explanation:
    Window [12, -1, -7]         → first negative: -1
    Window [-1, -7, 8]         → first negative: -1
    Window [-7, 8, -15]        → first negative: -7
    Window [8, -15, 30]        → first negative: -15
    Window [-15, 30, 16]       → first negative: -15
    Window [30, 16, 28]        → no negative → 0

Example 2:
    Input: arr = [-8, 2, 3, -6, 10], k = 2
    Output: [-8, 0, -6, -6]

Constraints:
------------
- 1 <= k <= len(arr) <= 10^5
- -10^5 <= arr[i] <= 10^5

Approach:
---------
Sliding window + deque: store indices of negative numbers in the current
window. Front of deque is the first negative's index. When sliding, remove
indices that fall outside the window; if current element is negative, append
its index. Append front's value (or 0) to result for each window.

Time Complexity: O(n)
Space Complexity: O(k)
"""

import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from collections import deque
from data_structures.utils.test_utils import run_test


class Solution(object):
    def firstNegativeInWindow(self, arr, k):
        """
        Return list: for each window of size k, the first negative number (0 if none).

        Code: Deque stores indices of negatives in current window. Front = first
        negative. When sliding, pop front if index is outside window; if arr[i]<0
        append i. For each window append arr[front] or 0.

        Time: O(n). Space: O(k).
        :type arr: List[int]
        :type k: int
        :rtype: List[int]
        """
        result = []
        temp_result = deque()

        for i in range(len(arr)):
            if arr[i] < 0:
                temp_result.append(i)
            
            if temp_result and temp_result[0] <= i - k:
                temp_result.popleft()

            if i >= k - 1:
                if temp_result:
                    result.append(arr[temp_result[0]])
                else:
                    result.append(0)

        return result


if __name__ == "__main__":
    sol = Solution()
    run_test(
        sol.firstNegativeInWindow([12, -1, -7, 8, -15, 30, 16, 28], 3),
        [-1, -1, -7, -15, -15, 0],
        "arr=[12,-1,-7,8,-15,30,16,28], k=3",
    )
    run_test(
        sol.firstNegativeInWindow([-8, 2, 3, -6, 10], 2),
        [-8, 0, -6, -6],
        "arr=[-8,2,3,-6,10], k=2",
    )
