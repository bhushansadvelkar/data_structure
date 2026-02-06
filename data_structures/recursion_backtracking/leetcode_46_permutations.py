"""
46. Permutations
https://leetcode.com/problems/permutations/

Difficulty: Medium
Topics: Array, Backtracking

Problem:
--------
Given an array nums of distinct integers, return all the possible permutations.
You can return the answer in any order.

Examples:
---------
Example 1:
    Input: nums = [1, 2, 3]
    Output: [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]

Example 2:
    Input: nums = [0, 1]
    Output: [[0, 1], [1, 0]]

Example 3:
    Input: nums = [1]
    Output: [[1]]

Constraints:
------------
- 1 <= nums.length <= 6
- -10 <= nums[i] <= 10
- All the integers of nums are unique.
"""

from data_structures.utils.test_utils import run_test


class Solution(object):
    def permute(self, nums):
        """
        Return all possible permutations of nums.

        :type nums: List[int]
        :rtype: List[List[int]]
        """
        pass


def normalize(result):
    """Convert result to comparable form (set of tuples for order-independent comparison)."""
    if result is None:
        return None
    return set(tuple(p) for p in result)


if __name__ == "__main__":
    s = Solution()
    run_test(
        s.permute([1, 2, 3]),
        [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]],
        "[1,2,3]",
        normalize=normalize,
    )
    run_test(s.permute([0, 1]), [[0, 1], [1, 0]], "[0,1]", normalize=normalize)
    run_test(s.permute([1]), [[1]], "[1]", normalize=normalize)
