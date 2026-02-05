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
    # Largest element strictly smaller than target (predecessor)
    print(s.findFloorementinArray([1, 2, 3, 4, 5], 3))   # Expected: 2 (largest < 3)
    print(s.findFloorementinArray([1, 2, 3, 4, 5], 6))   # Expected: 5 (largest < 6)
    print(s.findFloorementinArray([1, 2, 4, 5], 3))      # Expected: 2 (largest < 3)
    print(s.findFloorementinArray([5, 10, 15], 2))       # Expected: -1 (no elem < 2)
    print(s.findFloorementinArray([7], 7))               # Expected: -1 (no elem < 7)
    print(s.findFloorementinArray([7], 5))               # Expected: -1 (no elem < 5)