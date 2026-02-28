"""
340. Longest Substring with At Most K Distinct Characters
https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/

Difficulty: Medium
Topics: String, Hash Table, Sliding Window


Problem:
--------
Given a string s and an integer k, return the length of the longest substring
of s that contains at most k distinct characters.

A substring is a contiguous non-empty sequence of characters within a string.

Examples:
---------
Example 1:
    Input: s = "eceba", k = 2
    Output: 3
    Explanation: The substring is "ece" with length 3.

Example 2:
    Input: s = "aa", k = 1
    Output: 2
    Explanation: The substring is "aa" with length 2.

Constraints:
------------
- 1 <= s.length <= 5 * 10^4
- 0 <= k <= 50

How I solved it:
----------------
Sliding window with a character frequency map. I use two pointers (left, right)
and maintain a window s[left..right]. For each right, I add s[right] to the
frequency map. If the number of distinct characters in the map exceeds k, I
shrink from the left: decrement freq_map[s[left]], remove the key if count
drops to 0, then move left forward. After the while loop, the window has at
most k distinct characters, so I update max_length with the current window
size (right - left + 1). I do this for every valid window, not only when
distinct count equals k, because "at most k" includes 1, 2, ..., k distinct.

Time Complexity: O(n)
    Each character is added to the window at most once and removed at most once.

Space Complexity: O(k) or O(min(k, |charset|))
    The frequency map holds at most k + 1 keys while shrinking (we shrink until
    distinct <= k). For a fixed alphabet, this is O(1); otherwise O(min(k, 128))
    for ASCII.
"""

import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from data_structures.utils.test_utils import run_test


class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        Return the length of the longest substring with at most k distinct chars.

        :type s: str
        :type k: int
        :rtype: int
        """
        left = 0 
        freq_map = {}
        max_length = 0 

        for right in range(len(s)):
            char = s[right]
            freq_map[char] = freq_map.get(char, 0) + 1

            while len(freq_map) > k:
                freq_map[s[left]] -= 1
                if freq_map[s[left]] == 0:
                    del freq_map[s[left]]
                left += 1

            max_length = max(max_length, right - left + 1)

        return max_length


if __name__ == "__main__":
    sol = Solution()
    run_test(sol.lengthOfLongestSubstringKDistinct("eceba", 2), 3, 's="eceba", k=2')
    run_test(sol.lengthOfLongestSubstringKDistinct("aa", 1), 2, 's="aa", k=1')
    run_test(sol.lengthOfLongestSubstringKDistinct("a", 1), 1, 's="a", k=1')
    run_test(sol.lengthOfLongestSubstringKDistinct("a", 2), 1, 's="a", k=2')
    run_test(sol.lengthOfLongestSubstringKDistinct("a", 0), 0, 's="a", k=0')
    run_test(sol.lengthOfLongestSubstringKDistinct("abaccc", 2), 4, 's="abaccc", k=2')
    run_test(sol.lengthOfLongestSubstringKDistinct("abc", 2), 2, 's="abc", k=2')
    run_test(sol.lengthOfLongestSubstringKDistinct("aabbcc", 1), 2, 's="aabbcc", k=1')
    run_test(sol.lengthOfLongestSubstringKDistinct("aabbcc", 2), 4, 's="aabbcc", k=2')
    run_test(sol.lengthOfLongestSubstringKDistinct("aabbcc", 3), 6, 's="aabbcc", k=3')
