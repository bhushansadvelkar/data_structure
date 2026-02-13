"""
49. Group Anagrams
https://leetcode.com/problems/group-anagrams/

Difficulty: Medium
Topics: Array, String, Hash Table, Sorting

Problem:
--------
Given an array of strings strs, group the anagrams together. You can return
the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a
different word or phrase, typically using all the original letters exactly once.

Examples:
---------
Example 1:
    Input: strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    Output: [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]
    Explanation: Groups are by anagram; order of groups and strings can vary.

Example 2:
    Input: strs = [""]
    Output: [[""]]

Example 3:
    Input: strs = ["a"]
    Output: [["a"]]

Constraints:
------------
- 1 <= strs.length <= 10^4
- 0 <= strs[i].length <= 100
- strs[i] consists of lowercase English letters.

Approach:
---------
Use a key for each string that is the same for all anagrams (e.g. sorted
string, or tuple of character counts). Group strings by key in a dict;
return list of groups.

Time Complexity: O(n * k log k) with sort key; O(n * k) with count-tuple key.
Space Complexity: O(n * k) for output.
"""

import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from data_structures.utils.test_utils import run_test


def normalize(result):
    """Sort groups and strings within groups for order-independent comparison."""
    if result is None:
        return None
    return tuple(tuple(sorted(g)) for g in sorted(result, key=lambda g: tuple(sorted(g))))


class Solution(object):
    def groupAnagrams(self, strs):
        """
        Group anagrams together. Return list of groups (any order).

        Code: Use a key that is the same for all anagrams (sorted string).
        Group strings by key in a dict; return list of values.

        Time: O(n * k log k). Space: O(n * k).
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        groups = {}
        for s in strs:
            key = tuple(sorted(s))
            if key not in groups:
                groups[key] = []
            groups[key].append(s)
        return list(groups.values())

if __name__ == "__main__":
    sol = Solution()
    run_test(
        sol.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]),
        [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]],
        'strs=["eat","tea","tan","ate","nat","bat"]',
        normalize=normalize,
    )
    run_test(sol.groupAnagrams([""]), [[""]], 'strs=[""]', normalize=normalize)
    run_test(sol.groupAnagrams(["a"]), [["a"]], 'strs=["a"]', normalize=normalize)
