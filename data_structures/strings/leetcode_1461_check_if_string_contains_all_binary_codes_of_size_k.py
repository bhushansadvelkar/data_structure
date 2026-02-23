"""
1461. Check If a String Contains All Binary Codes of Size K
https://leetcode.com/problems/check-if-a-string-contains-all-binary-codes-of-size-k/

Difficulty: Medium
Topics: String, Hash Table, Bit Manipulation, Rolling Hash

Problem:
--------
Given a binary string s and an integer k, return true if every binary code of
length k is a substring of s. Otherwise, return false.

Examples:
---------
Example 1:
    Input: s = "00110110", k = 2
    Output: true
    Explanation: The binary codes of length 2 are "00", "01", "10", and "11".
    They can all be found as substrings at indices 0, 1, 3 and 2 respectively.

Example 2:
    Input: s = "0110", k = 1
    Output: true
    Explanation: The binary codes of length 1 are "0" and "1", they are both
    present in the string.

Example 3:
    Input: s = "0110", k = 2
    Output: false
    Explanation: The binary code "00" is of length 2 and does not appear in
    the string.

Constraints:
------------
- 1 <= k <= 20
- 1 <= s.length <= 5 * 10^5
- s[i] is either '0' or '1'

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
    def hasAllCodes(self, s, k):
        """
        Return True if every binary code of length k is a substring of s.

        :type s: str
        :type k: int
        :rtype: bool
        """
        n = len(s)
        candiadates = set()

        for i in range(n - k + 1):
            sub = s[i: i + k]
        
            if sub not in candiadates:
                candiadates.add(sub)

        length = len(candiadates)

        return 2 ** k == length


if __name__ == "__main__":
    sol = Solution()
    run_test(sol.hasAllCodes("00110110", 2), True, 's="00110110", k=2')
    run_test(sol.hasAllCodes("0110", 1), True, 's="0110", k=1')
    run_test(sol.hasAllCodes("0110", 2), False, 's="0110", k=2')
