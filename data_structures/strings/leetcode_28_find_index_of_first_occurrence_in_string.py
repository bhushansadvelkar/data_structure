"""
28. Find the Index of the First Occurrence in a String
https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/

Difficulty: Easy
Topics: Two Pointers, String, String Matching


Problem:
--------
Given two strings needle and haystack, return the index of the first occurrence
of needle in haystack, or -1 if needle is not part of haystack.

Examples:
---------
Example 1:
    Input: haystack = "sadbutsad", needle = "sad"
    Output: 0
    Explanation: "sad" occurs at index 0 and 6. The first occurrence is at index 0.

Example 2:
    Input: haystack = "leetcode", needle = "leeto"
    Output: -1
    Explanation: "leeto" did not occur in "leetcode".

Constraints:
------------
- 1 <= haystack.length, needle.length <= 10^4
- haystack and needle consist of only lowercase English letters.

Approach: How I solved it
-------------------------
Sliding window: try every possible starting index i in haystack. For each i,
check if the substring haystack[i : i + len(needle)] equals needle. Return i
as soon as we find a match; if no match after all indices, return -1.

Time Complexity: O(n * m)
    - n = len(haystack), m = len(needle). We try at most (n - m + 1) starting
      indices; each comparison checks up to m characters. Worst case O(n * m).

Space Complexity: O(1)
    - Only a few variables (index i, no extra data structures). Using a slice
      for comparison uses O(m) temporary space per check; still O(1) extra
      in the usual analysis.
"""

import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from data_structures.utils.test_utils import run_test


class Solution(object):
    def strStr(self, haystack, needle):
        """
        Return the index of the first occurrence of needle in haystack, or -1 if not found.

        :type haystack: str
        :type needle: str
        :rtype: int
        """
        for i in range(len(haystack)):
            if needle == haystack[i:i + len(needle)]:
                return i 

        return -1


if __name__ == "__main__":
    sol = Solution()
    run_test(sol.strStr("sadbutsad", "sad"), 0, 'haystack="sadbutsad", needle="sad"')
    run_test(sol.strStr("leetcode", "leeto"), -1, 'haystack="leetcode", needle="leeto"')
