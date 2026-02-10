"""
973. K Closest Points to Origin
https://leetcode.com/problems/k-closest-points-to-origin/

Difficulty: Medium
Topics: Array, Math, Divide and Conquer, Geometry, Sorting, Heap, Quickselect

Problem:
--------
Given an array of points where points[i] = [xi, yi] represents a point on the
X-Y plane and an integer k, return the k closest points to the origin (0, 0).

The distance between two points on the X-Y plane is the Euclidean distance
(i.e., sqrt((x1 - x2)^2 + (y1 - y2)^2)).

You may return the answer in any order. The answer is guaranteed to be unique
(except for the order that it is in).

Examples:
---------
Example 1:
    Input: points = [[1, 3], [-2, 2]], k = 1
    Output: [[-2, 2]]
    Explanation: Distance from (1, 3) to origin = sqrt(10).
    Distance from (-2, 2) to origin = sqrt(8). sqrt(8) < sqrt(10), so
    (-2, 2) is closer. Answer is [[-2, 2]].

Example 2:
    Input: points = [[3, 3], [5, -1], [-2, 4]], k = 2
    Output: [[3, 3], [-2, 4]] (or [[-2, 4], [3, 3]])

Constraints:
------------
- 1 <= k <= points.length <= 10^4
- -10^4 <= xi, yi <= 10^4

Approach:
---------
Use a min-heap keyed by squared distance to origin (avoids sqrt). Push all
points; pop k times to get the k closest. Squared distance is x^2 + y^2.

Time Complexity: O(n log k) with heap of size k; or O(n log n) if building
    heap from all n points then popping k times.
Space Complexity: O(k) or O(n) depending on whether you maintain a size-k
    heap or heapify the full list.
"""

import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from data_structures.utils.test_utils import run_test


def _normalize(result):
    """Sort list of points for order-independent comparison."""
    if result is None:
        return None
    return tuple(tuple(p) for p in sorted(result, key=lambda p: (p[0], p[1])))


class Solution(object):
    def kClosest(self, points, k):
        """
        Return the k closest points to the origin (0, 0).

        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        pass


if __name__ == "__main__":
    sol = Solution()
    run_test(
        sol.kClosest([[1, 3], [-2, 2]], 1),
        [[-2, 2]],
        "points=[[1,3],[-2,2]], k=1",
        normalize=_normalize,
    )
    run_test(
        sol.kClosest([[3, 3], [5, -1], [-2, 4]], 2),
        [[3, 3], [-2, 4]],
        "points=[[3,3],[5,-1],[-2,4]], k=2",
        normalize=_normalize,
    )
