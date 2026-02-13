"""
Next Smaller Element

Difficulty: Medium
Topics: Array, Stack, Monotonic Stack

Problem:
--------
Given an array, for each element find the next smaller element to its right.
The next smaller element of x is the first element smaller than x when
traversing right. If no such element exists, return -1.

Examples:
---------
Example 1:
    Input: arr = [4, 2, 1, 5, 3]
    Output: [2, 1, -1, 3, -1]
    Explanation: 4→2, 2→1, 1→none, 5→3, 3→none

Example 2:
    Input: arr = [2, 1, 4, 3]
    Output: [1, -1, 3, -1]
    Explanation: 2→1, 1→none, 4→3, 3→none

Constraints:
------------
- 1 <= arr.length <= 10^4
- -10^9 <= arr[i] <= 10^9

Approach: Monotonic Stack (Reversed Traversal)
----------------------------------------------
- Traverse array in reversed order (right to left)
- Stack stores elements seen so far (to the right of current)
- For each element: pop larger/equal values until we find a smaller one
  or stack is empty → result is -1
- At end: reverse result to match original order

Time Complexity: O(n)
    - Single pass, each element pushed and popped at most once

Space Complexity: O(n)
    - Stack + result list

Approach Diagram (Mermaid):
--------------------------
```mermaid
flowchart TD
    A[Traverse right to left] --> B{Stack empty?}
    B -->|Yes| C[result = -1]
    B -->|No| D{Stack top < current?}
    D -->|Yes| E[result = stack top]
    D -->|No| F[Pop until smaller or empty]
    F --> B
    C --> G[Push current]
    E --> G
```
"""

from data_structures.utils.test_utils import run_test


class Solution():
    def nextSmallerElement(self, arr):
        """
        For each element, return next smaller to the right; -1 if none.

        Code: Traverse right-to-left. Stack holds values seen. Pop while
        stack top >= current; result is stack top or -1; push current.

        Time: O(n). Space: O(n).
        :type arr: List[int]
        :rtype: List[int]
        """
        stack = []
        result = []

        for element in reversed(arr):
            if not stack:
                result.append(-1)

            if stack and stack[-1] < element:
                result.append(stack[-1])

            if stack and stack[-1] >= element:
                while stack and stack[-1] >= element:
                    stack.pop()
                if not stack:
                    result.append(-1)
                else:
                    result.append(stack[-1])

            stack.append(element)

        return result[::-1]


if __name__ == "__main__":
    s = Solution()
    run_test(s.nextSmallerElement([4, 2, 1, 5, 3]), [2, 1, -1, 3, -1], "[4,2,1,5,3]")
    run_test(s.nextSmallerElement([2, 1, 4, 3]), [1, -1, 3, -1], "[2,1,4,3]")
