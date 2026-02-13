"""
658. Find K Closest Elements
https://leetcode.com/problems/find-k-closest-elements/

Difficulty: Medium
Topics: Array, Two Pointers, Binary Search, Sliding Window, Sorting, Heap

Problem:
--------
Given a sorted integer array arr, two integers k and x, return the k closest
integers to x in the array. The result should also be sorted in ascending order.

An integer a is closer to x than an integer b if:
- |a - x| < |b - x|, or
- |a - x| == |b - x| and a < b (ties broken by smaller value)

Examples:
---------
Example 1:
    Input: arr = [1, 2, 3, 4, 5], k = 4, x = 3
    Output: [1, 2, 3, 4]
    Explanation: The 4 closest to 3 are [1, 2, 3, 4]; sorted ascending.

Example 2:
    Input: arr = [1, 1, 2, 3, 4, 5], k = 4, x = -1
    Output: [1, 1, 2, 3]
    Explanation: The 4 closest to -1 are [1, 1, 2, 3].

Constraints:
------------
- 1 <= k <= arr.length <= 10^4
- -10^4 <= arr[i], x <= 10^4
- arr is sorted in ascending order

Approach:
---------
Use a min-heap keyed by (distance to x, value). Push all elements, then pop
k times to get the k closest. Sort the result for ascending order as required.

Time Complexity: O(n log n)
    - n = len(arr). Building heap from n elements: O(n). k pops: O(k log n).
      Final sort of k elements: O(k log k). Dominant term O(n log n) for heap build.

Space Complexity: O(n)
    - Heap stores n (distance, value) pairs.

Approach Diagram (Mermaid):
--------------------------
```mermaid
flowchart TD
    A[Build heap: abs(x - num), num for each] --> B[Heapify]
    B --> C[Pop k times]
    C --> D[Sort result ascending]
    D --> E[Return k closest]
```
"""

import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from data_structures.utils.test_utils import run_test

import heapq

class Solution:
    def findClosestElements(self, arr, k, x):
        """
        Return k closest integers to x, sorted ascending.

        Code: Min-heap keyed by (distance to x, value). Heapify all, pop k
        times, sort result for ascending order.

        Time: O(n log n). Space: O(n).
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        heap = [(abs(x - i), i) for i in arr]
        heapq.heapify(heap)
        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        res.sort()
        return res


if __name__ == "__main__":
    s = Solution()
    run_test(
        s.findClosestElements([1, 2, 3, 4, 5], 4, 3),
        [1, 2, 3, 4],
        "arr=[1,2,3,4,5], k=4, x=3",
    )
    run_test(
        s.findClosestElements([1, 1, 2, 3, 4, 5], 4, -1),
        [1, 1, 2, 3],
        "arr=[1,1,2,3,4,5], k=4, x=-1",
    )
