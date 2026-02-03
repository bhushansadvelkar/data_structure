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
    print(Solution().searchInReverseSorted([5, 4, 3, 2, 1], 3))  # Expected: True
    print(Solution().searchInReverseSorted([5, 4, 3, 2, 1], 6))  # Expected: False
    print(Solution().searchInReverseSorted([7], 7))  # Expected: True
    print(Solution().searchInReverseSorted([7], 5))  # Expected: False
    print(Solution().searchInReverseSorted([10, 5, 1], 10))  # Expected: True
    print(Solution().searchInReverseSorted([10, 5, 1], 1))   # Expected: True