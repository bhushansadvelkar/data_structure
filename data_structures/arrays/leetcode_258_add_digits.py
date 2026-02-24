"""
258. Add Digits
https://leetcode.com/problems/add-digits/

Difficulty: Easy
Topics: Math, Simulation, Number Theory

Problem:
--------
Given an integer num, repeatedly add all its digits until the result has only
one digit, and return it.

Examples:
---------
Example 1:
    Input: num = 38
    Output: 2
    Explanation: 38 → 3 + 8 = 11 → 1 + 1 = 2

Example 2:
    Input: num = 0
    Output: 0

Constraints:
------------
- 0 <= num <= 2^31 - 1

Follow-up: Could you solve it without any loop/recursion in O(1) runtime?

How I solved it:
----------------
(TODO)

Time Complexity: O(?)
Space Complexity: O(?)
"""

import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from data_structures.utils.test_utils import run_test


class Solution(object):
    def addDigits(self, num):
        """
        Repeatedly add digits until a single digit remains.

        :type num: int
        :rtype: int
        """
        pass


if __name__ == "__main__":
    sol = Solution()

    run_test(sol.addDigits(38), 2, "num=38")
    run_test(sol.addDigits(0), 0, "num=0")
    run_test(sol.addDigits(10), 1, "num=10")
    run_test(sol.addDigits(99), 9, "num=99")
