"""
169. Majority Element
https://leetcode.com/problems/majority-element/

Difficulty: Easy

Topics: Array, Hash Table, Divide and Conquer, Sorting, Counting

Problem:
--------
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times.
You may assume that the majority element always exists in the array.

Examples:
---------
Example 1:
    Input: nums = [3, 2, 3]
    Output: 3

Example 2:
    Input: nums = [2, 2, 1, 1, 1, 2, 2]
    Output: 2

Constraints:
------------
- n == nums.length
- 1 <= n <= 5 * 10^4
- -10^9 <= nums[i] <= 10^9

Follow-up:
----------
Could you solve the problem in linear time and in O(1) space?

Approach:
---------
Count element frequencies with Counter, then return the one whose count is
greater than floor(n / 2).

Time Complexity: O(n)
Space Complexity: O(u)
    - u = number of distinct values, O(n) in the worst case.
"""

import os
import sys

from collections import Counter 
import math 

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from data_structures.utils.test_utils import run_test


class Solution(object):
    def majorityElement(self, nums):
        """
        Return the majority element (appears more than ⌊n/2⌋ times).

        :type nums: List[int]
        :rtype: int
        """
        element_frequencies = Counter(nums) 
        for key, value in element_frequencies.items():
            if value > math.floor(len(nums) / 2):
                return key

        return None


if __name__ == "__main__":
    sol = Solution()
    run_test(sol.majorityElement([3, 2, 3]), 3, "nums=[3,2,3]")
    run_test(sol.majorityElement([2, 2, 1, 1, 1, 2, 2]), 2, "nums=[2,2,1,1,1,2,2]")
