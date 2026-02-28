"""
Number of Rotations in a Sorted Array


Problem:
--------
Given an array of distinct integers `nums` sorted in ascending order and then
rotated at an unknown pivot, determine how many times the array has been
rotated. The number of rotations is equal to the index of the minimum element.

Example:
--------
nums = [15, 16, 17, 18, 9, 10, 11] -> Rotated 4 times.

Approach: How I solved it
-------------------------
Use binary search to find the index of the minimum element:
- If the leftmost element is less than or equal to the rightmost element,
  the array is already sorted: return the left index (rotation count).
- Otherwise, compute the mid index.
- If nums[mid] is greater than or equal to nums[left], then the minimum lies
  to the right of mid; move the left pointer to mid + 1.
- Otherwise, the minimum lies to the left or at mid; move the right pointer to mid.

Time Complexity: O(log n)
    - Binary search narrows down the search space exponentially.

Space Complexity: O(1)
    - Uses only constant auxiliary space.
"""

from data_structures.utils.test_utils import run_test


class Solution(object):
    def countArrayRotation(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        right = len(nums) - 1

        while left < right:
            if nums[left] <= nums[right]:
                return left

            mid = left + (right - left) // 2

            if nums[mid] >= nums[left]:
                left = mid + 1
            else:
                right = mid

        return left


if __name__ == "__main__":
    s = Solution()
    run_test(s.countArrayRotation([15, 16, 17, 18, 9, 10, 11]), 4, "[15,16,17,18,9,10,11]")
    run_test(s.countArrayRotation([3, 4, 5, 1, 2]), 3, "[3,4,5,1,2]")
    run_test(s.countArrayRotation([1, 2, 3, 4, 5]), 0, "[1,2,3,4,5]")
    run_test(s.countArrayRotation([2, 3, 4, 5, 1]), 4, "[2,3,4,5,1]")
    run_test(s.countArrayRotation([7]), 0, "[7]")