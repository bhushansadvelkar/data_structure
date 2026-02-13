"""
503. Next Greater Element II
https://leetcode.com/problems/next-greater-element-ii/

Difficulty: Medium
Topics: Array, Stack, Monotonic Stack

Problem:
--------
Given a circular integer array nums (i.e., the next element of nums[n-1] is
nums[0]), return the next greater number for every element in nums.

The next greater number of a number x is the first greater number to its
traversing-order next in the array, which means you could search circularly to
find its next greater number. If it doesn't exist, return -1 for this number.

Examples:
---------
Example 1:
    Input: nums = [1, 2, 1]
    Output: [2, -1, 2]
    Explanation: The first 1's next greater is 2; the number 2 can't find next
    greater; the second 1's next greater needs to search circularly, which is 2.

Example 2:
    Input: nums = [1, 2, 3, 4, 3]
    Output: [2, 3, 4, -1, 4]

Constraints:
------------
- 1 <= nums.length <= 10^4
- -10^9 <= nums[i] <= 10^9

Approach: Stack (Reversed Traversal)
------------------------------------
- Double the array (arr+arr) to handle circular wrap-around
- Traverse in reversed order: process from end to beginning (twice)
- Stack stores values (not indices) of elements seen so far
- For each element: pop smaller values from stack until we find a greater one,
  or stack is empty (result = -1)
- At end: reverse result and take first n elements (one per original element)

Time Complexity: O(n)
    - 2n iterations, each element pushed/popped O(1) times amortized

Space Complexity: O(n)
    - Stack + result list

Approach Diagram (Mermaid):
--------------------------
```mermaid
flowchart TD
    A[Double array for circular] --> B[Traverse reversed arr+arr]
    B --> C{Stack empty?}
    C -->|Yes| D[result = -1]
    C -->|No| E{Stack top > current?}
    E -->|Yes| F[result = stack top]
    E -->|No| G[Pop until greater or empty]
    G --> C
    D --> H[Push current]
    F --> H
```
"""

from data_structures.utils.test_utils import run_test


class Solution():
    def nextGreaterElements(self, arr):
        """
        For each element, return next greater (circular). -1 if none.

        Code: Double array for circular; traverse reversed. Stack holds values.
        Pop smaller until greater found or empty; push current.

        Time: O(n). Space: O(n).
        :type arr: List[int]
        :rtype: List[int]
        """
        stack = []
        result = []

        for element in reversed(arr+arr):
            if not stack:
                result.append(-1)

            if stack and stack[-1] > element:
                result.append(stack[-1])

            if stack and stack[-1] <= element:
                while stack and stack[-1] <= element:
                    stack.pop()
                if not stack:
                    result.append(-1)
                else:
                    result.append(stack[-1])

            stack.append(element)

        return result[::-1][:len(arr)]


if __name__ == "__main__":
    s = Solution()
    run_test(s.nextGreaterElements([1, 2, 1]), [2, -1, 2], "[1,2,1]")
    run_test(s.nextGreaterElements([1, 2, 3, 4, 3]), [2, 3, 4, -1, 4], "[1,2,3,4,3]")
