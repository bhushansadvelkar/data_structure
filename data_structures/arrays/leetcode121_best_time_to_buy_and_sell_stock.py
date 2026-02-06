"""
121. Best Time to Buy and Sell Stock
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

Difficulty: Easy
Topics: Array, Dynamic Programming

Problem:
--------
You are given an array prices where prices[i] is the price of a given stock on
the ith day. You want to maximize your profit by choosing a single day to buy
one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot
achieve any profit, return 0.

Examples:
---------
Example 1:
    Input: prices = [7, 1, 5, 3, 6, 4]
    Output: 5
    Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6),
    profit = 6 - 1 = 5. Note that buying on day 2 and selling on day 1 is not
    allowed because you must buy before you sell.

Example 2:
    Input: prices = [7, 6, 4, 3, 1]
    Output: 0
    Explanation: In this case, no transactions are done and the max profit = 0.

Constraints:
------------
- 1 <= prices.length <= 10^5
- 0 <= prices[i] <= 10^4

Approach: Single Pass (Track Minimum)
-------------------------------------
For each day, we can sell at prices[i] if we bought at the minimum price seen
so far. Track the minimum price (best_buy) and max profit in one pass.

Time Complexity: O(n)
    - Single pass through the array
    - Each iteration does O(1) work

Space Complexity: O(1)
    - Only two variables: max_profit and best_buy
"""

from data_structures.utils.test_utils import run_test


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0

        max_profit = 0
        best_buy = prices[0]

        for i in range(1, len(prices)):
            max_profit = max(max_profit, prices[i] - best_buy)
            best_buy = min(best_buy, prices[i])

        return max_profit


if __name__ == "__main__":
    s = Solution()
    run_test(s.maxProfit([7, 1, 5, 3, 6, 4]), 5, "[7,1,5,3,6,4]")
    run_test(s.maxProfit([7, 6, 4, 3, 1]), 0, "[7,6,4,3,1]") 