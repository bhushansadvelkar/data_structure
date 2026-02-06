"""
Binary Search in Reverse (Descending) Sorted Array

Difficulty: Easy
Topics: Array, Binary Search

Problem:
--------
Given an array sorted in descending order and a target, return True if target
exists in the array, False otherwise. Uses binary search with reversed logic
since elements decrease left to right.

Examples:
---------
Example 1:
    Input: nums = [5, 4, 3, 2, 1], target = 3
    Output: True
    Explanation: 3 exists at index 2.

Example 2:
    Input: nums = [5, 4, 3, 2, 1], target = 6
    Output: False
    Explanation: 6 does not exist.

Example 3:
    Input: nums = [10, 5, 1], target = 1
    Output: True

Constraints:
------------
- 1 <= nums.length <= 10^4
- -10^4 <= nums[i], target <= 10^4
- nums is sorted in descending order (no duplicates)

Approach: Binary Search (Reversed Comparison)
---------------------------------------------
Same structure as standard binary search, but direction is flipped:
- nums[mid] > target → target is smaller → search RIGHT (start = mid + 1)
- nums[mid] < target → target is larger → search LEFT (end = mid - 1)

Time Complexity: O(log n)
    - Each iteration halves the search space

Space Complexity: O(1)
"""

from data_structures.utils.test_utils import run_test


class Solution(object):
    def searchInReverseSorted(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        start = 0
        end = len(nums) - 1

        while start <= end:
            mid = (start + end) // 2

            if nums[mid] == target:
                return True 

            if nums[mid] < target:
                end = mid - 1 
            else:
                start = mid + 1

        return False


if __name__ == "__main__":
    s = Solution()
    run_test(s.searchInReverseSorted([5, 4, 3, 2, 1], 3), True, "[5,4,3,2,1], target=3")
    run_test(s.searchInReverseSorted([5, 4, 3, 2, 1], 6), False, "[5,4,3,2,1], target=6")
    run_test(s.searchInReverseSorted([7], 7), True, "[7], target=7")
    run_test(s.searchInReverseSorted([7], 5), False, "[7], target=5")
    run_test(s.searchInReverseSorted([10, 5, 1], 10), True, "[10,5,1], target=10")
    run_test(s.searchInReverseSorted([10, 5, 1], 1), True, "[10,5,1], target=1")