"""
20. Valid Parentheses
https://leetcode.com/problems/valid-parentheses/

Difficulty: Easy
Topics: String, Stack


Problem:
--------
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid.

An input string is valid if:
- Open brackets must be closed by the same type of brackets.
- Open brackets must be closed in the correct order.
- Every close bracket has a corresponding open bracket of the same type.

Examples:
---------
Example 1:
    Input: s = "()"
    Output: True

Example 2:
    Input: s = "()[]{}"
    Output: True

Example 3:
    Input: s = "(]"
    Output: False

Example 4:
    Input: s = "([)]"
    Output: False

Constraints:
------------
- 1 <= s.length <= 10^4
- s consists of parentheses only '()[]{}'.

Approach:
---------
Use a stack: for each character, if it's an opening bracket push it; if it's a
closing bracket, check that the stack is non-empty and the top matches the
closing type, then pop. Valid iff we finish with an empty stack.

Time Complexity: O(n)
    - Single pass; each character pushed or popped at most once.

Space Complexity: O(n)
    - Stack can hold up to n/2 opening brackets in the worst case.
"""

import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from data_structures.utils.test_utils import run_test


class Solution(object):
    def isValid(self, s):
        """
        Return True if s has valid matching parentheses, else False.

        :type s: str
        :rtype: bool
        """
        mapping = {')': '(', '}': '{', ']': '['}
        stack = []

        for char in s:
            if char in mapping.values():
                stack.append(char)
            elif char in mapping:
                if not stack or mapping[char] != stack.pop():
                    return False
        return not stack


if __name__ == "__main__":
    sol = Solution()
    run_test(sol.isValid("()"), True, 's="()"')
    run_test(sol.isValid("()[]{}"), True, 's="()[]{}"')
    run_test(sol.isValid("(]"), False, 's="(]"')
    run_test(sol.isValid("([)]"), False, 's="([)]"')
