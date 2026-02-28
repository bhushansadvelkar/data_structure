"""
242. Valid Anagram
https://leetcode.com/problems/valid-anagram/

Difficulty: Easy
Topics: String, Hash Table, Sorting


Problem:
--------
Given two strings s and t, return true if t is an anagram of s, and false
otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a
different word or phrase, typically using all the original letters exactly once.

Examples:
---------
Example 1:
    Input: s = "anagram", t = "nagaram"
    Output: true

Example 2:
    Input: s = "rat", t = "car"
    Output: false

Constraints:
------------
- 1 <= s.length, t.length <= 5 * 10^4
- s and t consist of lowercase English letters.

Follow-up:
----------
What if the inputs contain Unicode characters? How would you adapt your solution?

Approach:
---------
Option 1: Count frequency of each character in s; traverse t and decrement
counts. If lengths differ, false. If any count goes negative, false. Else true.
Option 2: Sort both strings and compare (O(n log n) time).

Time Complexity: O(n)
Space Complexity: O(1) or O(26) for count array
"""

import os
import sys
from collections import Counter

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from data_structures.utils.test_utils import run_test


class Solution(object):
    def isAnagram(self, s, t):
        """
        Return True if t is an anagram of s, else False.

        :type s: str
        :type t: str
        :rtype: bool
        """
        return Counter(s) == Counter(t)


if __name__ == "__main__":
    sol = Solution()
    run_test(sol.isAnagram("anagram", "nagaram"), True, 's="anagram", t="nagaram"')
    run_test(sol.isAnagram("rat", "car"), False, 's="rat", t="car"')
