"""
Previous Greater Element

Difficulty: Medium
Topics: Array, Stack, Monotonic Stack


Problem:
--------
Given an array, for each element find the previous greater element to its left.
The previous greater element of x is the first element greater than x when
traversing left. If no such element exists, return -1.

Examples:
---------
Example 1:
    Input: arr = [4, 2, 1, 5, 3]
    Output: [-1, 4, 2, -1, 5]
    Explanation: 4→none, 2→4, 1→2, 5→none, 3→5

Example 2:
    Input: arr = [5, 4, 3, 2, 1]
    Output: [-1, 5, 4, 3, 2]
    Explanation: Each element's previous greater is the one before it

Constraints:
------------
- 1 <= arr.length <= 10^4
- -10^9 <= arr[i] <= 10^9

Approach: Monotonic Stack (Left to Right Traversal)
---------------------------------------------------
- Traverse array left to right (normal order)
- Stack stores elements seen so far (to the left of current)
- For each element: pop smaller/equal values until we find a greater one
  or stack is empty → result is -1
- No need to reverse since we process in order

Time Complexity: O(n)
    - Single pass, each element pushed and popped at most once

Space Complexity: O(n)
    - Stack + result list

Running Steps (Example: arr = [4, 2, 1, 5, 3]):
-----------------------------------------------
Initial: stack=[], result=[]

Step 1: element=4
    - stack is empty → append(-1)
    - stack=[4], result=[-1]

Step 2: element=2
    - stack[-1]=4, 4>2 → append(4)
    - stack=[4,2], result=[-1,4]

Step 3: element=1
    - stack[-1]=2, 2>1 → append(2)
    - stack=[4,2,1], result=[-1,4,2]

Step 4: element=5
    - stack[-1]=1, 1<=5 → pop until greater or empty
    - pop 1, pop 2, pop 4, stack=[]
    - stack empty → append(-1)
    - stack=[5], result=[-1,4,2,-1]

Step 5: element=3
    - stack[-1]=5, 5>3 → append(5)
    - stack=[5,3], result=[-1,4,2,-1,5]

Final: return [-1, 4, 2, -1, 5]
"""

from data_structures.utils.test_utils import run_test


class Solution():
    def prevGreaterElement(self, arr):
        """
        For each element, return previous greater to the left; -1 if none.

        Code: Traverse left to right. Stack holds values seen. Pop while
        stack top <= current; result is stack top or -1; push current.

        Time: O(n). Space: O(n).
        :type arr: List[int]
        :rtype: List[int]
        """
        stack = []
        result = []

        for element in arr:
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

        return result


if __name__ == "__main__":
    s = Solution()
    run_test(s.prevGreaterElement([4, 2, 1, 5, 3]), [-1, 4, 2, -1, 5], "[4,2,1,5,3]")
    run_test(s.prevGreaterElement([5, 4, 3, 2, 1]), [-1, 5, 4, 3, 2], "[5,4,3,2,1]")
