"""
438. Find All Anagrams in a String
https://leetcode.com/problems/find-all-anagrams-in-a-string/

Difficulty: Medium
Topics: String, Sliding Window, Hash Table

Problem:
--------
Given two strings s and p, return an array of all the start indices of p's
anagrams in s. You may return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a
different word or phrase, typically using all the original letters exactly once.

Examples:
---------
Example 1:
    Input: s = "cbaebabacd", p = "abc"
    Output: [0, 6]
    Explanation: The substring with start index = 0 is "cba", which is an
    anagram of "abc". The substring with start index = 6 is "bac", which is
    an anagram of "abc".

Example 2:
    Input: s = "abab", p = "ab"
    Output: [0, 1, 2]
    Explanation: The substring with start index = 0 is "ab", which is an
    anagram of "ab". The substring with start index = 1 is "ba", which is an
    anagram of "ab". The substring with start index = 2 is "ab".

Constraints:
------------
- 1 <= s.length, p.length <= 3 * 10^4
- s and p consist of lowercase English letters.

Approach:
---------
Sliding window of length len(p). Maintain frequency counts of the current
window and of p. When window frequencies match p's frequencies, the window is
an anagram — add start index to result. Slide by one: decrement count for
char leaving, increment for char entering; update match state.

Time Complexity: O(n)
Space Complexity: O(1) or O(26) for frequency arrays
"""

import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from data_structures.utils.test_utils import run_test

from collections import Counter 

class Solution(object):
    def findAnagrams(self, s, p):
        """
        Return list of start indices in s where a substring is an anagram of p.

        :type s: str
        :type p: str
        :rtype: List[int]
        """
        k = len(p)
        need = Counter(p)
        window = Counter()

        result = []
        i = 0

        for j in range(len(s)):
            window[s[j]] += 1

            if j - i + 1 > k:
                window[s[i]] -= 1
                if window[s[i]] == 0:
                    del window[s[i]]
                i += 1

            if j - i + 1 == k and window == need:
                result.append(i)

        return result


if __name__ == "__main__":
    sol = Solution()
    run_test(
        sol.findAnagrams("cbaebabacd", "abc"),
        [0, 6],
        's="cbaebabacd", p="abc"',
    )
    run_test(
        sol.findAnagrams("abab", "ab"),
        [0, 1, 2],
        's="abab", p="ab"',
    )
