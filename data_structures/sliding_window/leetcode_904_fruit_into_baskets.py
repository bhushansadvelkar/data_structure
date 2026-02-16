"""
904. Fruit Into Baskets
https://leetcode.com/problems/fruit-into-baskets/

Difficulty: Medium
Topics: Array, Hash Table, Sliding Window

Problem:
--------
You are visiting a farm that has a single row of fruit trees arranged from left
to right. The trees are represented by an integer array fruits where fruits[i]
is the type of fruit the i-th tree produces.

You want to collect as much fruit as possible. However, the owner has some
strict rules that you must follow:

- You only have two baskets, and each basket can only hold a single type of
  fruit. There is no limit on the amount of fruit each basket can hold.
- Starting from any tree of your choice, you must pick exactly one fruit from
  every tree (moving right) until you cannot.
- Once you reach a tree with fruit that cannot fit in your baskets, you must stop.

Given the integer array fruits, return the maximum number of fruits you can pick.

(Equivalently: find the length of the longest contiguous subarray with at most
two distinct values.)

Examples:
---------
Example 1:
    Input: fruits = [1, 2, 1]
    Output: 3
    Explanation: We can pick from all 3 trees.

Example 2:
    Input: fruits = [0, 1, 2, 2]
    Output: 3
    Explanation: We can pick from trees [1, 2, 2]. If we started at the first
    tree, we would only pick from [0, 1].

Example 3:
    Input: fruits = [1, 2, 3, 2, 2]
    Output: 4
    Explanation: We can pick from trees [2, 3, 2, 2]. If we started at the first
    tree, we would only pick [1, 2].

Constraints:
------------
- 1 <= fruits.length <= 10^5
- 0 <= fruits[i] < fruits.length

How I solved it:
----------------
Same as longest substring with at most k distinct (here k=2). Sliding window
with a frequency map: two pointers (left, right), add fruits[right] to the
map, then while the map has more than 2 distinct fruit types, shrink from the
left (decrement count for fruits[left], remove key if 0, move left). After
shrinking, the window has at most 2 types, so update max_count with the
current window length (right - left + 1).

Time Complexity: O(n)
    Each fruit is added to the window at most once and removed at most once.

Space Complexity: O(1)
    The frequency map holds at most 3 keys (we shrink until distinct <= 2).
    So O(1) for a bounded number of fruit types.
"""

import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from data_structures.utils.test_utils import run_test


class Solution(object):
    def totalFruit(self, fruits):
        """
        Return the maximum number of fruits you can pick (at most 2 types).

        :type fruits: List[int]
        :rtype: int
        """
        left = 0 
        freq_map = {}
        max_count = 0 

        for right in range(len(fruits)):
            char = fruits[right]
            freq_map[char] = freq_map.get(char, 0) + 1

            while len(freq_map) > 2:
                freq_map[fruits[left]] -= 1
                if freq_map[fruits[left]] == 0:
                    del freq_map[fruits[left]]
                left += 1

            max_count = max(max_count, right - left + 1)

        return max_count

if __name__ == "__main__":
    sol = Solution()
    run_test(sol.totalFruit([1, 2, 1]), 3, "fruits=[1,2,1]")
    run_test(sol.totalFruit([0, 1, 2, 2]), 3, "fruits=[0,1,2,2]")
    run_test(sol.totalFruit([1, 2, 3, 2, 2]), 4, "fruits=[1,2,3,2,2]")
    run_test(sol.totalFruit([5]), 1, "fruits=[5]")
    run_test(sol.totalFruit([1, 1, 1, 1]), 4, "fruits=[1,1,1,1]")
    run_test(sol.totalFruit([1, 2, 1, 2]), 4, "fruits=[1,2,1,2]")
    run_test(sol.totalFruit([1, 1, 1, 2, 2, 2]), 6, "fruits=[1,1,1,2,2,2]")
    run_test(sol.totalFruit([3, 3, 3, 1, 2, 1, 1, 2]), 5, "fruits=[3,3,3,1,2,1,1,2]")
    run_test(sol.totalFruit([0, 0, 1, 1, 2, 2]), 4, "fruits=[0,0,1,1,2,2]")
    run_test(sol.totalFruit([1, 0, 1, 4, 1, 4, 1, 2, 3]), 5, "fruits=[1,0,1,4,1,4,1,2,3]")
