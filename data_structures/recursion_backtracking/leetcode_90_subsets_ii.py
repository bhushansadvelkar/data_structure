"""
90. Subsets II
https://leetcode.com/problems/subsets-ii/

Difficulty: Medium
Topics: Array, Backtracking

Problem:
--------
Given an integer array nums that may contain duplicates, return all possible
subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in
any order.

Examples:
---------
Example 1:
    Input: nums = [1, 2, 2]
    Output: [[], [1], [1, 2], [1, 2, 2], [2], [2, 2]]

Example 2:
    Input: nums = [0]
    Output: [[], [0]]

Constraints:
------------
- 1 <= nums.length <= 10
- -10 <= nums[i] <= 10

Approach: How I solved it
-------------------------
- Include/exclude recursion: for each element, either include it (op2 = output_arr + [input_arr[0]]) or exclude it (op1 = output_arr). Recurse on input_arr[1:].
- Base case: when input_arr is empty, append current output_arr to result.
- Deduplication: at the end, convert each subset to tuple(sorted(sub)), put in set to remove duplicates, then back to list of lists. This merges [4,4,1] and [1,4,4] into one.

Time Complexity: O(2^n * n log n)
    - 2^n recursive paths (each element: include or exclude).
    - Final deduplication: O(result_size * n log n) for sorting each subset.

Space Complexity: O(n)
    - Recursion stack depth is n. Result list holds up to 2^n subsets.

Approach Diagram (Mermaid):
--------------------------
```mermaid
flowchart TD
    A[Include or exclude each element] --> B[Recurse on rest]
    B --> C{input empty?}
    C -->|Yes| D[Add subset to result]
    C -->|No| A
    D --> E[Deduplicate via set of sorted tuples]
```
"""

from data_structures.utils.test_utils import run_test


class Solution(object):
    def subsetsWithDup(self, nums):
        """
        Return all possible subsets (power set) without duplicates.

        :type nums: List[int]
        :rtype: List[List[int]]
        """
        input_arr = nums
        output_arr = []
        result = []
        self.solve(input_arr, output_arr, result)
        return list(map(list, set(tuple(sorted(sub)) for sub in result)))

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
    return set(tuple(sorted(sub)) for sub in result)


if __name__ == "__main__":
    s = Solution()
    run_test(s.subsetsWithDup([1, 2, 2]), [[], [1], [1, 2], [1, 2, 2], [2], [2, 2]], "[1,2,2]", normalize=normalize)
    run_test(s.subsetsWithDup([0]), [[], [0]], "[0]", normalize=normalize)
    run_test(
        s.subsetsWithDup([1, 2, 3]),
        [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]],
        "[1,2,3]",
        normalize=normalize,
    )
    run_test(
        s.subsetsWithDup([4, 4, 4, 1, 4]),
        [[], [1], [1, 4], [1, 4, 4], [1, 4, 4, 4], [1, 4, 4, 4, 4], [4], [4, 4], [4, 4, 4], [4, 4, 4, 4]],
        "[4,4,4,1,4]",
        normalize=normalize,
    )
