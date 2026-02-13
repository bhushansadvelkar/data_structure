"""
1475. Final Prices With a Special Discount in a Shop
https://leetcode.com/problems/final-prices-with-a-special-discount-in-a-shop/

Difficulty: Easy
Topics: Array, Stack, Monotonic Stack

Problem:
--------
You are given an integer array prices where prices[i] is the price of the ith
item in a shop. There is a special discount for items in the shop.

If you buy the ith item, then you will receive a discount equivalent to
prices[j] where j is the minimum index such that j > i and prices[j] <= prices[i].
Otherwise, you will not receive any discount at all.

Return an integer array answer where answer[i] is the final price you will pay
for the ith item of the shop, considering the special discount.

Examples:
---------
Example 1:
    Input: prices = [8, 4, 6, 2, 3]
    Output: [4, 2, 4, 2, 3]
    Explanation:
    - Item 0: 8 - 4 = 4 (discount from prices[1]=4)
    - Item 1: 4 - 2 = 2 (discount from prices[3]=2)
    - Item 2: 6 - 2 = 4 (discount from prices[3]=2)
    - Items 3, 4: no smaller/equal price to the right

Example 2:
    Input: prices = [1, 2, 3, 4, 5]
    Output: [1, 2, 3, 4, 5]
    Explanation: All prices are increasing, no discounts.

Example 3:
    Input: prices = [10, 1, 1, 6]
    Output: [9, 0, 1, 6]

Constraints:
------------
- 1 <= prices.length <= 500
- 1 <= prices[i] <= 1000

Approach: Monotonic Stack (Reversed Traversal)
----------------------------------------------
This is essentially a "Next Smaller or Equal Element" problem.
- Traverse array in reversed order (right to left)
- Stack stores elements seen so far (potential discounts)
- For each element: pop larger values until we find a smaller/equal one
  or stack is empty → no discount
- Discount = current price - stack top (or 0 if stack empty)

Time Complexity: O(n)
    - Single pass, each element pushed and popped at most once

Space Complexity: O(n)
    - Stack + result list

Approach Diagram (Mermaid):
--------------------------
```mermaid
flowchart TD
    A[Traverse right to left] --> B{Stack empty?}
    B -->|Yes| C[discount = 0]
    B -->|No| D{Stack top <= current?}
    D -->|Yes| E[discount = current - stack top]
    D -->|No| F[Pop until smaller/equal or empty]
    F --> B
    C --> G[Push current]
    E --> G
```
"""

from data_structures.utils.test_utils import run_test


class Solution(object):
    def finalPrices(self, prices):
        """
        Return final price per item: price - next smaller-or-equal to the right.

        Code: Traverse right to left. Stack holds candidate discounts. Pop
        larger values until smaller-or-equal or empty; discount = stack top.

        Time: O(n). Space: O(n).
        :type prices: List[int]
        :rtype: List[int]
        """
        stack = []
        result = []

        for element in reversed(prices):
            if not stack:
                result.append(element)
            
            if stack and stack[-1] <= element:
                result.append(element - stack[-1])
            
            if stack and stack[-1] > element:
                while stack and stack[-1] > element:
                    stack.pop()
                if not stack:
                    result.append(element)
                else:
                    result.append(element - stack[-1])

            stack.append(element)
    
        return result[::-1]


if __name__ == "__main__":
    s = Solution()
    run_test(s.finalPrices([8, 4, 6, 2, 3]), [4, 2, 4, 2, 3], "[8,4,6,2,3]")
    run_test(s.finalPrices([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5], "[1,2,3,4,5]")
    run_test(s.finalPrices([10, 1, 1, 6]), [9, 0, 1, 6], "[10,1,1,6]")