"""
78. Subsets
https://leetcode.com/problems/subsets/

Difficulty: Medium
Topics: Array, Backtracking, Bit Manipulation

Problem:
--------
Given an integer array nums of unique elements, return all possible subsets
(the power set).

The solution set must not contain duplicate subsets. Return the solution in
any order.

Examples:
---------
Example 1:
    Input: nums = [1, 2, 3]
    Output: [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]

Example 2:
    Input: nums = [0]
    Output: [[], [0]]

Constraints:
------------
- 1 <= nums.length <= 10
- -10 <= nums[i] <= 10
- All the numbers of nums are unique.

Approach:
---------
Backtracking: for each element, two choices — include or exclude. Recurse on
rest; when input is empty, add current subset to result.

Time Complexity: O(n * 2^n)
    - 2^n subsets, each of size up to n to copy.

Space Complexity: O(n)
    - Recursion depth and current path O(n). Output is O(2^n * n) excluded.
"""

from data_structures.utils.test_utils import run_test


class Solution(object):
    def subsets(self, nums):
        """
        Return all possible subsets (power set).

        Code: Backtrack: include or exclude first element; recurse on rest;
        base case: add current subset to result.

        Time: O(n * 2^n). Space: O(n) recursion.
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        input_arr = nums
        output_arr = []
        result = []
        self.solve(input_arr, output_arr, result)
        return list(map(list, set(map(tuple, result))))

    def solve(self, input_arr, output_arr, result):
        if len(input_arr) == 0:
            result.append(output_arr)
            return

        op1 = output_arr
        op2 = output_arr + [input_arr[0]]

        self.solve(input_arr[1:], op1, result)
        self.solve(input_arr[1:], op2, result)


def normalize(result):
    """Convert result to comparable form (order of subsets and elements can vary)."""
    if result is None:
        return None
    return set(tuple(sorted(sub)) for sub in result)


if __name__ == "__main__":
    s = Solution()
    run_test(
        s.subsets([1, 2, 3]),
        [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]],
        "[1,2,3]",
        normalize=normalize,
    )
    run_test(s.subsets([0]), [[], [0]], "[0]", normalize=normalize)
    run_test(s.subsets([1, 2, 2]), [[], [1], [1, 2], [1, 2, 2], [2], [2, 2]], "[1,2,2]", normalize=normalize)
