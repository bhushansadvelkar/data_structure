"""
779. K-th Symbol in Grammar
https://leetcode.com/problems/k-th-symbol-in-grammar/

Difficulty: Medium
Topics: Math, Bit Manipulation, Recursion


Problem:
--------
We build a table of n rows (1-indexed). We start by writing 0 in the 1st row.
In every subsequent row, we look at the previous row and replace:
  - each 0 with 01
  - each 1 with 10

Given two integers n and k, return the kth (1-indexed) symbol in the nth row.

Examples:
---------
Example 1:
    Input: n = 1, k = 1
    Output: 0
    Explanation: row 1 is "0".

Example 2:
    Input: n = 2, k = 1
    Output: 0
    Explanation: row 1: 0, row 2: 01 → 1st symbol is 0.

Example 3:
    Input: n = 2, k = 2
    Output: 1
    Explanation: row 2: 01 → 2nd symbol is 1.

Example 4:
    Input: n = 3, k = 1
    Output: 0
    Explanation: row 1: 0, row 2: 01, row 3: 0110 → 1st symbol is 0.

Constraints:
------------
- 1 <= n <= 30
- 1 <= k <= 2^(n - 1)

Approach: Parent Mapping / Recursion (matches this implementation)
--------------------------------------------------------------------
- Row n has length 2^(n-1). The code uses mid = 2^(n-1) as the split between
  the first and second half of that row (same as the row length for n >= 2).
- If k <= mid, recurse with kthGrammar(n - 1, k). Otherwise recurse with
  kthGrammar(n - 1, k - mid) and flip the bit (0↔1).
- Base cases: (n == 1, k == 1) → 0; (n == 1, k == 2) → 1 (handles the n == 2,
  k == 2 case together with the mid split above).

Time Complexity: O(n)
    - At most n recursive levels (n → n-1 → ... → 1), O(1) work per level.

Space Complexity: O(n)
    - Recursion call stack depth is n.
"""

from data_structures.utils.test_utils import run_test


class Solution(object):
    def kthGrammar(self, n, k):
        """
        Return the kth (1-indexed) symbol in the nth row.

        :type n: int
        :type k: int
        :rtype: int
        """
        if n == 1 and k == 1:
            return 0 
        
        if n == 1 and k == 2:
            return 1

        mid = 2 ** (n - 1)
        if k<= mid:
            return self.kthGrammar(n-1, k)
        else:
            return int(not(self.kthGrammar(n-1 , k - mid)))


if __name__ == "__main__":
    s = Solution()
    run_test(s.kthGrammar(1, 1), 0, "n=1, k=1")
    run_test(s.kthGrammar(2, 1), 0, "n=2, k=1")
    run_test(s.kthGrammar(2, 2), 1, "n=2, k=2")
    run_test(s.kthGrammar(3, 1), 0, "n=3, k=1")
    run_test(s.kthGrammar(3, 4), 0, "n=3, k=4")
    run_test(s.kthGrammar(4, 5), 1, "n=4, k=5")
