"""
1343. Number of Sub-arrays of Size K and Average Greater than or Equal to Threshold
https://leetcode.com/problems/number-of-sub-arrays-of-size-k-and-average-greater-than-or-equal-to-threshold/

Difficulty: Medium
Topics: Array, Sliding Window


Problem:
--------
Given an array of integers arr and two integers k and threshold, return the
number of sub-arrays of size k and average greater than or equal to threshold.

Examples:
---------
Example 1:
    Input: arr = [2, 2, 2, 2, 5, 5, 5, 8], k = 3, threshold = 4
    Output: 3
    Explanation: Sub-arrays [2,5,5], [5,5,5] and [5,5,8] have averages 4, 5
    and 6. Others have avg < 4.

Example 2:
    Input: arr = [11, 13, 17, 23, 29, 31, 7, 5, 2, 3], k = 3, threshold = 5
    Output: 6

Constraints:
------------
- 1 <= arr.length <= 10^5
- 1 <= arr[i] <= 10^4
- 1 <= k <= arr.length
- 0 <= threshold <= 10^4

Approach:
---------
Sliding window of size k. Average >= threshold is equivalent to
sum >= k * threshold. Maintain window sum; for each window, if sum >= k * threshold
increment count.

Time Complexity: O(n)
Space Complexity: O(1)
"""

import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from data_structures.utils.test_utils import run_test


class Solution(object):
    def numOfSubarrays(self, arr, k, threshold):
        """
        Return the number of sub-arrays of size k with average >= threshold.

        Code: average >= threshold iff sum >= k*threshold. Sliding window:
        maintain window_sum; first window sum(arr[:k]); then add arr[i],
        subtract arr[i-k]. Count windows where window_sum >= target.

        Time: O(n). Space: O(1).
        :type arr: List[int]
        :type k: int
        :type threshold: int
        :rtype: int
        """
        target = k * threshold  # average >= threshold  <=>  sum >= k * threshold
        window_sum = sum(arr[:k])
        count = 1 if window_sum >= target else 0
        for i in range(k, len(arr)):
            window_sum = window_sum + arr[i] - arr[i - k]
            count = count + 1 if window_sum >= target else count

        return count



if __name__ == "__main__":
    sol = Solution()
    run_test(
        sol.numOfSubarrays([2, 2, 2, 2, 5, 5, 5, 8], 3, 4),
        3,
        "arr=[2,2,2,2,5,5,5,8], k=3, threshold=4",
    )
    run_test(
        sol.numOfSubarrays([11, 13, 17, 23, 29, 31, 7, 5, 2, 3], 3, 5),
        6,
        "arr=[11,13,17,23,29,31,7,5,2,3], k=3, threshold=5",
    )
