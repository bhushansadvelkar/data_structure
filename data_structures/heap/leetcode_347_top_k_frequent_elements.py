"""
347. Top K Frequent Elements
https://leetcode.com/problems/top-k-frequent-elements/

Difficulty: Medium
Topics: Array, Hash Table, Heap, Counting, Sorting

Problem:
--------
Given an integer array nums and an integer k, return the k most frequent
elements. You may return the answer in any order.

Examples:
---------
Example 1:
    Input: nums = [1, 1, 1, 2, 2, 3], k = 2
    Output: [1, 2]
    Explanation: 1 appears 3 times, 2 appears 2 times. So [1, 2] or [2, 1].

Example 2:
    Input: nums = [1], k = 1
    Output: [1]

Constraints:
------------
- 1 <= nums.length <= 10^5
- -10^4 <= nums[i] <= 10^4
- k is in the range [1, number of unique elements in the array].
- It is guaranteed that the answer is unique.

Approach:
---------
Count frequency of each element, then use a max-heap (negated counts in a
min-heap). Build heap from unique elements keyed by negative frequency;
pop k times to get the k most frequent elements.

Time Complexity: O(n + u log u)
    - n = len(nums), u = number of unique elements. Counting: O(n). Building
      heap from u entries: O(u). k pops: O(k log u); typically k ≤ u, so O(u log u).

Space Complexity: O(u)
    - Storing unique keys and heap of size u. In worst case u = O(n).

Approach Diagram (Mermaid):
--------------------------
```mermaid
flowchart TD
    A[Count frequency of each element] --> B[Build min-heap keyed by -count]
    B --> C[Pop k times]
    C --> D[Return k most frequent]
```
"""

import os
import sys

from collections import Counter 
import heapq
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from data_structures.utils.test_utils import run_test


def _normalize(lst):
    """Sort result for comparison (order can be any)."""
    if lst is None:
        return None
    return tuple(sorted(lst))


class Solution(object):
    def topKFrequent(self, nums, k):
        """
        Return the k most frequent elements (any order).

        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        keys_list = list(set(nums))
        heap = [(-nums.count(i), i) for i in keys_list]
        heapq.heapify(heap)
        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        res.sort()
        return res


if __name__ == "__main__":
    sol = Solution()
    run_test(
        sol.topKFrequent([1, 1, 1, 2, 2, 3, 7, 7, 7, 7, 7, 8, 8, 8], 2),
        [1, 7],
        "nums=[1,1,1,2,2,3,7,7,7,7,7,8,8,8], k=2",
        normalize=_normalize,
    )
    run_test(
        sol.topKFrequent([1], 1),
        [1],
        "nums=[1], k=1",
        normalize=_normalize,
    )
