"""
2529. Maximum Count of Positive Integer and Negative Integer
https://leetcode.com/problems/maximum-count-of-positive-integer-and-negative-integer/

Difficulty: Easy
Topics: Array, Binary Search

Problem:
--------
Given a sorted array in non-decreasing order, return the maximum between the
count of positive integers and the count of negative integers. Note that 0 is
neither positive nor negative.

Examples:
---------
Example 1:
    Input: nums = [-2, -1, -1, 1, 2, 3]
    Output: 3
    Explanation: 3 positive and 3 negative integers, max = 3.

Example 2:
    Input: nums = [-3, -2, -1, 0, 0, 1, 2]
    Output: 3
    Explanation: 2 positive and 3 negative integers, max = 3.

Example 3:
    Input: nums = [5, 20, 66, 1314]
    Output: 4
    Explanation: 4 positive, 0 negative, max = 4.

Constraints:
------------
- 1 <= nums.length <= 2000
- -2000 <= nums[i] <= 2000
- nums is sorted in non-decreasing order

Approach: Binary Search
-----------------------
1. First binary search: find leftmost position where value > 0
   - pos = len(nums) - left (count of positive numbers)
2. Second binary search: find leftmost position where value >= 0 (or count neg)
   - neg = count of negative numbers (all elements before first 0)

Time Complexity: O(log n)
    - Two binary searches

Space Complexity: O(1)
    - Only using variables
"""


class Solution(object):
    def maximumCount(self, nums):
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) >> 1
            if nums[mid] > 0:
                right = mid - 1
            else:
                left = mid + 1

        pos = len(nums) - left  

        left = 0
        while left <= right:
            mid = (left + right) >> 1
            if nums[mid] == 0:
                right = mid - 1
            else:
                left = mid + 1

        neg = left     

        return pos if pos > neg else neg


if __name__ == "__main__":
    # Example 1: 3 positive, 3 negative → max = 3
    print(Solution().maximumCount([-2, -1, -1, 1, 2, 3]))  # Expected: 3

    # Example 2: 2 positive, 3 negative → max = 3
    print(Solution().maximumCount([-3, -2, -1, 0, 0, 1, 2]))  # Expected: 3

    # Example 3: 4 positive, 0 negative → max = 4
    print(Solution().maximumCount([5, 20, 66, 1314]))  # Expected: 4

    # Edge case: all negative
    print(Solution().maximumCount([-5, -3, -1]))  # Expected: 3

    # Edge case: all zeros
    print(Solution().maximumCount([0, 0, 0]))  # Expected: 0