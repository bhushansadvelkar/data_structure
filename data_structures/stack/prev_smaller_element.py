"""
Previous Smaller Element

Difficulty: Medium
Topics: Array, Stack, Monotonic Stack


Problem:
--------
Given an array, for each element find the previous smaller element to its left.
The previous smaller element of x is the first element smaller than x when
traversing left. If no such element exists, return -1.

Examples:
---------
Example 1:
    Input: arr = [4, 2, 1, 5, 3]
    Output: [-1, -1, -1, 1, 1]
    Explanation: 4→none, 2→none, 1→none, 5→1, 3→1

Example 2:
    Input: arr = [2, 1, 4, 3]
    Output: [-1, -1, 1, 1]
    Explanation: 2→none, 1→none, 4→1, 3→1

Constraints:
------------
- 1 <= arr.length <= 10^4
- -10^9 <= arr[i] <= 10^9

Approach: Monotonic Stack (Left to Right Traversal)
---------------------------------------------------
- Traverse array left to right (normal order)
- Stack stores elements seen so far (to the left of current)
- For each element: pop larger/equal values until we find a smaller one
  or stack is empty → result is -1
- No need to reverse since we process in order

Time Complexity: O(n)
    - Single pass, each element pushed and popped at most once

Space Complexity: O(n)
    - Stack + result list
"""

from data_structures.utils.test_utils import run_test


class Solution():
    def prevSmallerElement(self, arr):
        """
        For each element, return previous smaller to the left; -1 if none.

        Code: Traverse left to right. Stack holds values seen. Pop while
        stack top >= current; result is stack top or -1; push current.

        Time: O(n). Space: O(n).
        :type arr: List[int]
        :rtype: List[int]
        """
        stack = []
        result = []

        for element in arr:
            if not stack:
                result.append(-1)

            if stack and stack[-1] < element:
                result.append(stack[-1])

            if stack and stack[-1] >= element:
                while stack and stack[-1] >= element:
                    stack.pop()
                if not stack:
                    result.append(-1)
                else:
                    result.append(stack[-1])

            stack.append(element)

        return result


if __name__ == "__main__":
    s = Solution()
    run_test(s.prevSmallerElement([4, 2, 1, 5, 3]), [-1, -1, -1, 1, 1], "[4,2,1,5,3]")
    run_test(s.prevSmallerElement([2, 1, 4, 3]), [-1, -1, 1, 1], "[2,1,4,3]")
