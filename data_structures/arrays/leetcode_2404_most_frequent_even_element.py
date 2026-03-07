"""
2404. Most Frequent Even Element
https://leetcode.com/problems/most-frequent-even-element/

Return the most frequent even element. If there is a tie, return the smallest one.
If no even element exists, return -1.
"""

from collections import Counter


class Solution(object):
    def mostFrequentEven(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counter = Counter(i for i in nums if i % 2 == 0)

        if not counter:
            return -1

        max_count = max(counter.values())
        result = {x for x, count in counter.items() if count == max_count}

        return min(result)

    def mostFrequentEven_optimized(self, nums):
        """
        One pass over counter: track max count and smallest element with that count.
        No extra set, single loop. O(n) time, O(k) space (k = distinct evens).
        """
        counter = Counter(i for i in nums if i % 2 == 0)

        if not counter:
            return -1

        max_count = -1
        best = None

        for x, count in counter.items():
            if count > max_count or (count == max_count and (best is None or x < best)):
                max_count = count
                best = x

        return best


if __name__ == "__main__":
    sol = Solution()
    for name in ("mostFrequentEven", "mostFrequentEven_optimized"):
        fn = getattr(sol, name)
        print(name, fn([0, 1, 2, 2, 4, 4, 1]), fn([4, 4, 4, 9, 2, 4]), fn([29, 47, 21, 41]))
