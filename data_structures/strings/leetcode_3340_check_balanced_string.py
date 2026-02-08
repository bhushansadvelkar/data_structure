"""
Check Balanced String
https://leetcode.com/problems/check-balanced-string/

Difficulty: Easy
Topics: String

Problem:
--------
You are given a string num consisting of only digits. A string of digits is
called balanced if the sum of the digits at even indices is equal to the sum
of digits at odd indices.

Return true if num is balanced, otherwise return false.

Examples:
---------
Example 1:
    Input: num = "1234"
    Output: false
    Explanation:
    Even indices sum = 1 + 3 = 4
    Odd indices sum = 2 + 4 = 6
    4 != 6 so not balanced

Example 2:
    Input: num = "24123"
    Output: true
    Explanation:
    Even indices sum = 2 + 1 + 3 = 6
    Odd indices sum = 4 + 2 = 6
    6 == 6 so balanced

Constraints:
------------
- 2 <= num.length <= 100
- num consists of digits only

Approach:
---------
Single pass with two running sums: iterate over indices 0, 2, 4, ... for
even_sum and 1, 3, 5, ... for odd_sum (or one loop with even_counter and
odd_counter stepping by 2). Compare the two sums at the end.

Time Complexity: O(n)
    - One pass over the string; each character visited at most once.

Space Complexity: O(1)
    - Only a few variables (even_sum, odd_sum, counters).
"""

import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from data_structures.utils.test_utils import run_test


class Solution(object):
    def isBalanced(self, num):
        """
        Return True if num is balanced, else False.

        :type num: str
        :rtype: bool
        """
        odd_sum, even_sum = 0, 0
        even_counter, odd_counter = 0, 1

        for _ in range((len(num) + 1) // 2):
            if even_counter < len(num):
                even_sum += int(num[even_counter])
            if odd_counter < len(num):
                odd_sum += int(num[odd_counter])
            even_counter += 2
            odd_counter += 2

        return even_sum == odd_sum


if __name__ == "__main__":
    s = Solution()
    run_test(s.isBalanced("1234"), False, 'num="1234"')
    run_test(s.isBalanced("24123"), True, 'num="24123"')
