"""
First and Last Occurrence of Element in Sorted Array

Difficulty: Medium
Topics: Array, Binary Search


Problem:
--------
Given a sorted array `nums` and a `target`, return the first and last indices of
`target` in the array. If the target is not present, return [-1, -1].

Examples:
---------
Example 1:
    Input: nums = [5, 7, 7, 8, 8, 10], target = 8
    Output: [3, 4]

Example 2:
    Input: nums = [1, 2, 3, 4, 5], target = 4
    Output: [3, 3]

Example 3:
    Input: nums = [1, 2, 3], target = 6
    Output: [-1, -1]

Constraints:
------------
- 1 <= nums.length <= 10^4
- -10^4 <= nums[i], target <= 10^4
- nums is sorted in non-decreasing order

Approach: Two Binary Searches
-----------------------------
1. Use binary search to find the first occurrence by moving `end` left when a
   match is found.
2. Use binary search again to find the last occurrence by moving `start` right
   when a match is found.
3. If no occurrence found, return [-1, -1].

Time Complexity: O(log n)
    - Two binary searches.

Space Complexity: O(1)
    - Constant extra memory.
"""

from data_structures.utils.test_utils import run_test


class Solution(object):
    def firstandLastOccuranceofNumber(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        start = 0 
        end = len(nums) - 1
        first = -1 

        while start <= end:
            mid = (start + end ) // 2

            if nums[mid] == target:
                first = mid
                end = mid - 1 

            elif nums[mid] > target:
                end = mid - 1
            else:
                start = mid + 1


        start = 0 
        end = len(nums) - 1
        last = -1 

        while start <= end:
            mid = (start + end ) // 2

            if nums[mid] == target:
                last = mid
                start = mid + 1 

            elif nums[mid] > target:
                end = mid - 1
            else:
                start = mid + 1

        if first == -1:
            return [-1, -1]

        return [first, last]


if __name__ == "__main__":
    s = Solution()
    run_test(s.firstandLastOccuranceofNumber([5, 7, 7, 8, 8, 10], 8), [3, 4], "nums=[5,7,7,8,8,10], target=8")
    run_test(s.firstandLastOccuranceofNumber([1, 2, 3, 4, 5], 4), [3, 3], "nums=[1,2,3,4,5], target=4")
    run_test(s.firstandLastOccuranceofNumber([1, 2, 3, 4, 5], 6), [-1, -1], "nums=[1,2,3,4,5], target=6")
    run_test(s.firstandLastOccuranceofNumber([2, 2, 2, 2], 2), [0, 3], "nums=[2,2,2,2], target=2")
    run_test(s.firstandLastOccuranceofNumber([9], 9), [0, 0], "nums=[9], target=9")