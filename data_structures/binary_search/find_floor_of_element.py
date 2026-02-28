"""
Find Floor / Predecessor in Sorted Array (largest element strictly smaller than target)


Problem:
--------
Sorted array and target. Return the largest element in the array that is strictly
smaller than target. If none exists, return -1.

Approach: How I solved it
-------------------------
- Binary search: if nums[mid] == target, search left only (end = mid - 1), don't store target.
- If nums[mid] > target, search left (end = mid - 1).
- If nums[mid] < target, it's a candidate floor; store it and search right (start = mid + 1) for a larger floor.
- Return stored result (or -1 if never updated).

Time Complexity: O(log n)
    - Binary search.

Space Complexity: O(1)
    - Only a few variables.
"""

from data_structures.utils.test_utils import run_test


class Solution(object):
    def findFloorementinArray(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        start = 0
        end = len(nums) - 1
        result = -1

        while start <= end:
            mid = (start + end) // 2 

            if nums[mid] == target:
                end = mid - 1
            elif nums[mid] > target:
                end = mid - 1
            else:
                result = nums[mid]
                start = mid + 1

        return result


if __name__ == "__main__":
    s = Solution()
    run_test(s.findFloorementinArray([1, 2, 3, 4, 5], 3), 2, "[1,2,3,4,5], target=3")
    run_test(s.findFloorementinArray([1, 2, 3, 4, 5], 6), 5, "[1,2,3,4,5], target=6")
    run_test(s.findFloorementinArray([1, 2, 4, 5], 3), 2, "[1,2,4,5], target=3")
    run_test(s.findFloorementinArray([5, 10, 15], 2), -1, "[5,10,15], target=2")
    run_test(s.findFloorementinArray([7], 7), -1, "[7], target=7")
    run_test(s.findFloorementinArray([7], 5), -1, "[7], target=5")