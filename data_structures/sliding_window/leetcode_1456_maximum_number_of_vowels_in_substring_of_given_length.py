"""
1456. Maximum Number of Vowels in a Substring of Given Length
https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/

Difficulty: Medium
Topics: String, Sliding Window

Problem:
--------
Given a string s and an integer k, return the maximum number of vowel letters
in any substring of s with length k.

Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.

Examples:
---------
Example 1:
    Input: s = "abciiidef", k = 3
    Output: 3
    Explanation: The substring "iii" contains 3 vowel letters.

Example 2:
    Input: s = "aeiou", k = 2
    Output: 2
    Explanation: Any substring of length 2 contains 2 vowels.

Example 3:
    Input: s = "leetcode", k = 3
    Output: 2
    Explanation: "lee", "eet", "ode" contain 2 vowels.

Constraints:
------------
- 1 <= s.length <= 10^5
- s consists of lowercase English letters.
- 1 <= k <= s.length

Approach:
---------
Sliding window of length k:
1. Count vowels in the first window s[0:k].
2. For each step, slide by one: the new character entering is s[i], the one
   leaving is s[i - k]. Add 1 to count if s[i] is a vowel, subtract 1 if
   s[i - k] is a vowel.
3. Track the maximum vowel count over all windows; return it.

Time Complexity: O(n)
    - One pass over s: O(k) for the first window, then (n - k) steps, each O(1).
    - Total O(n).

Space Complexity: O(1)
    - Only a fixed-size set for vowels and a few variables (count, max_count).

Approach Diagram (Mermaid):
--------------------------
```mermaid
flowchart TD
    A[Count vowels in first window s[0:k]] --> B[max_count = count]
    B --> C[For i=k to n-1]
    C --> D[s[i] vowel? add 1 to count]
    D --> E[s[i-k] vowel? subtract 1]
    E --> F[max_count = max(max_count, count)]
    F --> G{More?}
    G -->|Yes| C
    G -->|No| H[Return max_count]
```
"""

import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from data_structures.utils.test_utils import run_test


class Solution(object):
    def maxVowels(self, s, k):
        """
        Return the maximum number of vowels in any substring of s with length k.

        Code: vowels = set('aeiou'). Count vowels in first window s[:k]. Slide:
        if s[i] is vowel add 1; if s[i-k] is vowel subtract 1. Track max_count.

        Time: O(n). Space: O(1).
        :type s: str
        :type k: int
        :rtype: int
        """
        vowels = set("aeiou")
        if not s or k <= 0 or k > len(s):
            return 0
        count = sum(1 for c in s[:k] if c in vowels)  # first window
        max_count = count
        for i in range(k, len(s)):
            if s[i] in vowels:
                count += 1
            if s[i - k] in vowels:
                count -= 1
            max_count = max(max_count, count)
        return max_count


if __name__ == "__main__":
    sol = Solution()
    run_test(
        sol.maxVowels("abciiidef", 3),
        3,
        's="abciiidef", k=3',
    )
    run_test(
        sol.maxVowels("aeiou", 2),
        2,
        's="aeiou", k=2',
    )
    run_test(
        sol.maxVowels("leetcode", 3),
        2,
        's="leetcode", k=3',
    )
