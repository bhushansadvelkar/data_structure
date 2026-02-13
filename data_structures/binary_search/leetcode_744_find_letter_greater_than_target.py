"""
744. Find Smallest Letter Greater Than Target
https://leetcode.com/problems/find-smallest-letter-greater-than-target/

Problem:
--------
Sorted array of letters and a target. Return the smallest letter in the array
that is strictly greater than target. If none exists, return the first letter (wrap-around).

Approach: How I solved it
-------------------------
- Binary search: if letters[mid] > target, it's a candidate; search left for a smaller one (end = mid - 1).
- If letters[mid] <= target, search right (start = mid + 1).
- Use result to store best candidate; after loop return result or letters[0] if no candidate.

Time Complexity: O(log n)
    - Binary search halves the search space each step.

Space Complexity: O(1)
    - Only a few variables.

Approach Diagram (Mermaid):
--------------------------
```mermaid
flowchart TD
    A{letters[mid] > target?} -->|Yes| B[result = letters[mid], end = mid - 1]
    A -->|No| C[start = mid + 1]
    B --> D{start <= end?}
    C --> D
    D -->|Yes| A
    D -->|No| E{result set?}
    E -->|Yes| F[Return result]
    E -->|No| G[Return letters 0 wrap-around]
```
"""

from data_structures.utils.test_utils import run_test


class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        start = 0
        end = len(letters) - 1
        result = None

        while start <= end:
            mid = (start + end) // 2

            if letters[mid] == target:
                start = mid + 1
            elif letters[mid] > target:
                result = letters[mid]
                end = mid - 1
            else:
                start = mid + 1

        return result if result is not None else letters[0]

if __name__ == "__main__":
    s = Solution()
    run_test(s.nextGreatestLetter(["c", "f", "j"], "a"), "c", 'letters=["c","f","j"], target="a"')
    run_test(s.nextGreatestLetter(["c", "f", "j"], "c"), "f", 'letters=["c","f","j"], target="c"')
    run_test(s.nextGreatestLetter(["x", "x", "y", "y"], "z"), "x", 'letters=["x","x","y","y"], target="z"')
    run_test(s.nextGreatestLetter(["c", "f", "j"], "j"), "c", 'letters=["c","f","j"], target="j"')