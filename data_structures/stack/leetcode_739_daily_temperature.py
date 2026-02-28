"""
739. Daily Temperatures
https://leetcode.com/problems/daily-temperatures/


Problem:
--------
Given an array of daily temperatures, return an array such that result[i] is the
number of days you have to wait after day i to get a warmer temperature. If no future day is warmer, use 0.

Approach: How I solved it
-------------------------
- Monotonic stack (process from right to left): for each index i, pop from stack while top has value <= temperatures[i]; then the next warmer day is at stack top (or 0 if stack empty); push (temperatures[i], i) onto stack.
- Each index pushed and popped at most once.

Time Complexity: O(n)
    - Each index pushed once and popped at most once.

Space Complexity: O(n)
    - Stack can hold up to n indices in the worst case.
"""

from data_structures.utils.test_utils import run_test


class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        For each day i, return how many days until a warmer day (0 if none).

        Code: Monotonic stack (reversed order). Stack holds (value, index).
        For each i: pop while top <= temperatures[i]; next warmer = stack top
        (or 0); push (temperatures[i], i). Reverse result at end.

        Time: O(n). Space: O(n).
        :type temperatures: List[int]
        :rtype: List[int]
        """
        result = []
        stack = []  # (temperature, index)

        for i in reversed(range(len(temperatures))):
            if not stack:
                result.append(0)

            if stack and stack[-1][0] > temperatures[i]:
                result.append(stack[-1][1] - i)
            
            if stack and stack[-1][0] <= temperatures[i]:
                while stack and stack[-1][0] <= temperatures[i]:
                    stack.pop()
                if not stack:
                    result.append(0)
                else:
                    result.append(stack[-1][1] - i)
                
            stack.append([temperatures[i], i])

        return result[::-1]


if __name__ == "__main__":
    s = Solution()
    run_test(s.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]), [1, 1, 4, 2, 1, 1, 0, 0], "[73,74,75,71,69,72,76,73]")
    run_test(s.dailyTemperatures([30, 40, 50, 60]), [1, 1, 1, 0], "[30,40,50,60]")
    run_test(s.dailyTemperatures([30, 60, 90]), [1, 1, 0], "[30,60,90]")
