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
(Backtracking: for each index, include or exclude the element. Or cascading.)

Time Complexity:
Space Complexity:
"""


class Solution(object):
    def subsets(self, nums):
        """
        Return all possible subsets (power set).

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


def run_test(s, nums, expected, name):
    got = s.subsets(nums)
    if got is None:
        print(f"FAIL: {name} | solution returned None (not implemented)")
        return
    exp_set = normalize(expected)
    got_set = normalize(got)
    status = "PASS" if exp_set == got_set else "FAIL"
    print(f"{status}: {name}" + (f" | got {len(got)} subsets, expected {len(expected)}" if status == "FAIL" else ""))


if __name__ == "__main__":
    s = Solution()
    run_test(s, [1, 2, 3], [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]], "[1,2,3]")
    run_test(s, [0], [[], [0]], "[0]")
    run_test(s, [1, 2, 2], [[], [1], [1, 2], [1, 2, 2], [2], [2, 2]], "[1,2,2]")
