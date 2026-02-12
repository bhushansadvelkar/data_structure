"""
704. Binary Search
https://leetcode.com/problems/binary-search/

Difficulty: Easy
Topics: Array, Binary Search

Problem:
--------
Given an array of integers nums which is sorted in ascending order, and an integer
target, write a function to search target in nums. If target exists, then return
its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.

Examples:
---------
Example 1:
    Input: nums = [-1, 0, 3, 5, 9, 12], target = 9
    Output: 4
    Explanation: 9 exists in nums and its index is 4.

Example 2:
    Input: nums = [-1, 0, 3, 5, 9, 12], target = 2
    Output: -1
    Explanation: 2 does not exist in nums so return -1.

Constraints:
------------
- 1 <= nums.length <= 10^4
- -10^4 < nums[i], target < 10^4
- All the integers in nums are unique.
- nums is sorted in ascending order.

Approach: Classic Binary Search
-------------------------------
- Initialize start = 0, end = len(nums) - 1
- While start <= end:
  - Calculate mid = (start + end) // 2
  - If nums[mid] == target → return mid
  - If nums[mid] > target → search left (end = mid - 1)
  - Else → search right (start = mid + 1)
- If loop ends, target not found → return -1

Time Complexity: O(log n)
    - Each iteration eliminates half of the search space

Space Complexity: O(1)
    - Only using a few variables
"""

from data_structures.utils.test_utils import run_test


class Solution(object):
    def search(self, nums, target):
        """
        Return index of target in sorted nums, or -1 if not found.

        Code: Classic binary search: mid = (lo+hi)//2; if nums[mid]==target
        return mid; else narrow to left or right half.

        Time: O(log n). Space: O(1).
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        start = 0
        end = len(nums) - 1

        while start <= end: 
            mid = (start + end) // 2
            if  nums[mid] == target:
                return mid 
            
            if nums[mid] > target:
                end = mid - 1
            else:
                start = mid + 1

        return -1
if __name__ == "__main__":
    s = Solution()
    run_test(s.search([-1, 0, 3, 5, 9, 12], 9), 4, "nums=[-1,0,3,5,9,12], target=9")
    run_test(s.search([-1, 0, 3, 5, 9, 12], 2), -1, "nums=[-1,0,3,5,9,12], target=2")
    run_test(s.search([5], 5), 0, "nums=[5], target=5")
    run_test(s.search([5], 3), -1, "nums=[5], target=3")