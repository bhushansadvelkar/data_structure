"""
451. Sort Characters By Frequency
https://leetcode.com/problems/sort-characters-by-frequency/

Difficulty: Medium
Topics: String, Hash Table, Sorting, Heap, Counting

Problem:
--------
Given a string s, sort it in decreasing order based on the frequency of the
characters. The frequency of a character is the number of times it appears
in the string.

Return the sorted string. If there are multiple answers, return any of them.

Examples:
---------
Example 1:
    Input: s = "tree"
    Output: "eert" or "eetr"
    Explanation: 'e' appears twice; 't' and 'r' appear once. So 'e' must
    appear before 't' and 'r'. "eetr" is also a valid answer.

Example 2:
    Input: s = "cccaaa"
    Output: "cccaaa" or "aaaccc"
    Explanation: Both 'c' and 'a' appear three times.

Example 3:
    Input: s = "Aabb"
    Output: "bbAa" or "bbaA"
    Explanation: 'b' appears twice, 'A' and 'a' appear once.

Constraints:
------------
- 1 <= s.length <= 5 * 10^5
- s consists of uppercase and lowercase English letters and digits.

Approach:
---------
Count frequency of each character, then use a max-heap (simulated with
negated counts in a min-heap) so we can repeatedly pop the most frequent
character and append it to the result string the appropriate number of times.

Time Complexity: O(n + u log u)
    - n = len(s); u = number of unique characters. Counting: O(n). Building
      heap from u entries: O(u). Popping u times: O(u log u). Building output
      string: O(n). With u ≤ 128, this is effectively O(n).

Space Complexity: O(u) or O(1)
    - Heap and unique-keys list: O(u). For fixed alphabet (e.g. letters+digits),
      u is bounded, so O(1).
"""

import os
import sys
import heapq

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from data_structures.utils.test_utils import run_test


class Solution(object):
    def frequencySort(self, s):
        """
        Return the string sorted by character frequency (decreasing).

        :type s: str
        :rtype: str
        """
        keys_list = list(set(s))
        heap = [(-s.count(i), i) for i in keys_list]
        heapq.heapify(heap)
        result = []
        while heap:
            neg_count, char = heapq.heappop(heap)
            result.append(char * (-neg_count))
        return "".join(result)


def _normalize(s):
    """For comparison: same multiset of chars (order can vary for same freq)."""
    if s is None:
        return None
    from collections import Counter
    return tuple(sorted(Counter(s).items()))


if __name__ == "__main__":
    sol = Solution()
    run_test(
        sol.frequencySort("tree"),
        "eetr",
        's="tree"',
        normalize=_normalize,
    )
    run_test(
        sol.frequencySort("cccaaa"),
        "cccaaa",
        's="cccaaa"',
        normalize=_normalize,
    )
    run_test(
        sol.frequencySort("Aabb"),
        "bbAa",
        's="Aabb"',
        normalize=_normalize,
    )
