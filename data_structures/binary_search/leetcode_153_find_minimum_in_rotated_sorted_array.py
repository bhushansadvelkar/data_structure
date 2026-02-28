"""
153. Find Minimum in Rotated Sorted Array
https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

Difficulty: Medium
Topics: Array, Binary Search


Problem:
--------
Given an array of unique integers `nums` sorted in ascending order, rotated at
an unknown pivot, return the minimum element of the array.

Examples:
---------
Example 1:
    Input: nums = [3, 4, 5, 1, 2]
    Output: 1
    Explanation: The original array [1, 2, 3, 4, 5] was rotated 3 times.

Example 2:
    Input: nums = [4, 5, 6, 7, 0, 1, 2]
    Output: 0
    Explanation: Rotation pivot is between 7 and 0.

Example 3:
    Input: nums = [11, 13, 15, 17]
    Output: 11
    Explanation: Not rotated, so the first element is the minimum.

Constraints:
------------
- 1 <= nums.length <= 5000
- -5000 <= nums[i] <= 5000
- All integers are unique.
- nums was originally sorted in strictly increasing order, then rotated.

Approach: Binary Search for Rotation Pivot
------------------------------------------
- Maintain pointers `l` and `r`. The minimum element lies in the unsorted
  portion relative to `nums[r]`.
- Compute `mid = l + (r - l) // 2`.
- If `nums[mid] > nums[r]`, the minimum lies to the right, so set `l = mid + 1`.
- Otherwise, the minimum lies at `mid` or to the left, so set `r = mid`.
- Loop stops when `l == r`, which points to the minimum element.

Time Complexity: O(log n)
    - Binary search halves the search space each iteration.

Space Complexity: O(1)
    - Uses only a constant amount of extra memory.
"""

from data_structures.utils.test_utils import run_test


class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = 0
        r = len(nums) - 1

        while l < r:
            mid = l + (r - l) // 2

            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid

        return nums[l]


if __name__ == "__main__":
    s = Solution()
    run_test(s.findMin([3, 4, 5, 1, 2]), 1, "[3,4,5,1,2]")
    run_test(s.findMin([4, 5, 6, 7, 0, 1, 2]), 0, "[4,5,6,7,0,1,2]")
    run_test(s.findMin([11, 13, 15, 17]), 11, "[11,13,15,17]")
    run_test(s.findMin([1]), 1, "[1]")
    run_test(s.findMin([2, 1]), 1, "[2,1]")
