"""
3. Longest Substring Without Repeating Characters
https://leetcode.com/problems/longest-substring-without-repeating-characters/

Difficulty: Medium
Topics: String, Hash Table, Sliding Window

Problem:
--------
Given a string s, find the length of the longest substring without repeating
characters. A substring is a contiguous non-empty sequence of characters
within a string.

Examples:
---------
Example 1:
    Input: s = "abcabcbb"
    Output: 3
    Explanation: The answer is "abc", with the length of 3.

Example 2:
    Input: s = "bbbbb"
    Output: 1
    Explanation: The answer is "b", with the length of 1.

Example 3:
    Input: s = "pwwkew"
    Output: 3
    Explanation: The answer is "wke" (or "kew"). Notice that the answer must
    be a substring, i.e. a contiguous sequence of characters.

Constraints:
------------
- 0 <= s.length <= 5 * 10^4
- s consists of English letters, digits, symbols and spaces.

How I solved it:
----------------
(TODO: describe your approach)

Time Complexity: O(?)
Space Complexity: O(?)
"""

import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from data_structures.utils.test_utils import run_test


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        Return the length of the longest substring without repeating characters.

        :type s: str
        :rtype: int
        """
        char_set = set()
        left = 0 
        max_length = 0

        for right in range(len(s)):
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
            char_set.add(s[right])
            max_length = max(max_length, right - left + 1)
        return max_length


if __name__ == "__main__":
    sol = Solution()
    run_test(sol.lengthOfLongestSubstring("abcabcbb"), 3, 's="abcabcbb"')
    run_test(sol.lengthOfLongestSubstring("bbbbb"), 1, 's="bbbbb"')
    run_test(sol.lengthOfLongestSubstring("pwwkew"), 3, 's="pwwkew"')
    run_test(sol.lengthOfLongestSubstring(""), 0, 's=""')
    run_test(sol.lengthOfLongestSubstring("a"), 1, 's="a"')
    run_test(sol.lengthOfLongestSubstring("aa"), 1, 's="aa"')
    run_test(sol.lengthOfLongestSubstring("ab"), 2, 's="ab"')
    run_test(sol.lengthOfLongestSubstring("abcdef"), 6, 's="abcdef"')
    run_test(sol.lengthOfLongestSubstring("aab"), 2, 's="aab"')
    run_test(sol.lengthOfLongestSubstring("abb"), 2, 's="abb"')
    run_test(sol.lengthOfLongestSubstring("dvdf"), 3, 's="dvdf"')
    run_test(sol.lengthOfLongestSubstring("anviaj"), 5, 's="anviaj"')
    run_test(sol.lengthOfLongestSubstring("tmmzuxt"), 5, 's="tmmzuxt"')
