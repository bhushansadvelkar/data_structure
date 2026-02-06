"""
35. Search Insert Position
https://leetcode.com/problems/search-insert-position/

Difficulty: Easy
Topics: Array, Binary Search

Problem:
--------
Given a sorted array of distinct integers and a target value, return the index
if the target is found. If not, return the index where it would be if it were
inserted in order.

You must write an algorithm with O(log n) runtime complexity.

Examples:
---------
Example 1:
    Input: nums = [1, 3, 5, 6], target = 5
    Output: 2
    Explanation: 5 is at index 2.

Example 2:
    Input: nums = [1, 3, 5, 6], target = 2
    Output: 1
    Explanation: 2 would be inserted at index 1 (between 1 and 3).

Example 3:
    Input: nums = [1, 3, 5, 6], target = 7
    Output: 4
    Explanation: 7 would be inserted at the end, index 4.

Constraints:
------------
- 1 <= nums.length <= 10^4
- -10^4 <= nums[i], target <= 10^4
- nums contains distinct values sorted in ascending order.

Approach: Binary Search
-----------------------
- Same as classic binary search; if target found, return mid.
- If not found, after the loop the left pointer `l` is exactly the index where
  target would be inserted (all elements before `l` are < target, all from `l`
  onward are >= target).

Time Complexity: O(log n)
    - Each iteration halves the search space.

Space Complexity: O(1)
    - Only a few variables (l, r, mid).
"""

from data_structures.utils.test_utils import run_test


class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = l + (r - l) // 2

            if nums[mid] == target:
                return mid

            if nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1

        return l
if __name__ == "__main__":
    s = Solution()
    run_test(s.searchInsert([1, 3, 5, 6], 5), 2, "[1,3,5,6], target=5")
    run_test(s.searchInsert([1, 3, 5, 6], 2), 1, "[1,3,5,6], target=2")
    run_test(s.searchInsert([1, 3, 5, 6], 7), 4, "[1,3,5,6], target=7")
    run_test(s.searchInsert([1, 3, 5, 6], 0), 0, "[1,3,5,6], target=0")
    run_test(s.searchInsert([1], 1), 0, "[1], target=1")
    run_test(s.searchInsert([2], 1), 0, "[2], target=1")
    run_test(s.searchInsert([2], 3), 1, "[2], target=3")