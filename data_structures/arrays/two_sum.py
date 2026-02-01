"""
1. Two Sum
https://leetcode.com/problems/two-sum/

Difficulty: Easy
Topics: Array, Hash Table

Problem:
--------
Given an array of integers nums and an integer target, return indices of the two
numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not
use the same element twice.

You can return the answer in any order.

Examples:
---------
Example 1:
    Input: nums = [2, 7, 11, 15], target = 9
    Output: [0, 1]
    Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
    Input: nums = [3, 2, 4], target = 6
    Output: [1, 2]

Example 3:
    Input: nums = [3, 3], target = 6
    Output: [0, 1]

Constraints:
------------
- 2 <= nums.length <= 10^4
- -10^9 <= nums[i] <= 10^9
- -10^9 <= target <= 10^9
- Only one valid answer exists.

Follow-up:
----------
Can you come up with an algorithm that is less than O(n^2) time complexity?

Approach 1: Two-Pointer with Index Preservation
-----------------------------------------------
Why we can't sort directly:
    Sorting nums in-place would destroy the original indices. We need those
    indices for the answer. Solution: store (value, original_index) pairs.

How it works:
    1. Create indexed = [(nums[i], i) for each element]
    2. Sort indexed by value → pairs are now ordered smallest to largest
    3. Two pointers: start=0 (smallest), end=len-1 (largest)
    4. Compare sum to target:
       - sum == target → return [left_idx, right_idx]
       - sum < target  → move start right (need bigger sum)
       - sum > target  → move end left (need smaller sum)

Why two-pointer works on sorted data:
    If sum is too small, the only way to increase it is to take a larger
    left value (start++). If sum is too large, take a smaller right value
    (end--). We never skip the solution.

Time Complexity: O(n log n)
    - Building indexed: O(n)
    - Sorting: O(n log n)  ← dominant
    - Two-pointer scan: O(n)

Space Complexity: O(n)
    - indexed list stores n (value, index) pairs

---
Approach 2: Hash Map
-------------------
Key insight:
    For each number x, we need to find if (target - x) exists in the array.
    Hash map gives O(1) lookup instead of O(n) linear search.

How it works (single pass):
    1. As we iterate, store each value -> index in a hash map
    2. Before adding current num, check: does (target - num) already exist?
    3. If yes → we found our pair! Return [seen_index, current_index]
    4. If no → add current num to map and continue

Why check BEFORE adding:
    Prevents using the same element twice. When at index i, the map only
    contains elements we've seen (indices < i). So complement can't be
    the current element.

Example: nums = [2, 7, 11, 15], target = 9
    i=0: num=2, complement=7, 7 not in seen → seen = {2: 0}
    i=1: num=7, complement=2, 2 in seen! → return [0, 1]

Time Complexity: O(n)
    - Single pass through the array
    - Hash map lookup and insert are O(1) average

Space Complexity: O(n)
    - Hash map stores up to n value -> index pairs

Comparison:
    Hash map: O(n) time, O(n) space  ← optimal for time
    Two-pointer: O(n log n) time, O(n) space
"""


class Solution(object):
    def twoSum(self, nums, target):
        """
        Approach 1: Two-pointer with index preservation.
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Step 1: Pair each value with its original index (we need indices for output)
        indexed = [(val, i) for i, val in enumerate(nums)]

        # Step 2: Sort by value so two-pointer works (smallest to largest)
        indexed.sort(key=lambda x: x[0])

        start = 0
        end = len(indexed) - 1

        # Step 3: Two-pointer: start from both ends, move based on sum vs target
        while start < end:
            left_val, left_idx = indexed[start]
            right_val, right_idx = indexed[end]
            total = left_val + right_val

            if total == target:
                return [left_idx, right_idx]
            elif total < target:
                start += 1  # Need bigger sum → move to larger left value
            else:
                end -= 1  # Need smaller sum → move to smaller right value

        return None 

# --- Approach 2: Hash Map ---


class SolutionHashMap:
    """
    Approach 2: Hash map (single pass).
    Optimal O(n) time.
    """

    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        seen = {}  # value -> index

        for i, num in enumerate(nums):
            complement = target - num

            # Check BEFORE adding: ensures we don't use same element twice
            if complement in seen:
                return [seen[complement], i]

            seen[num] = i

        return None


# --- Run both approaches ---
if __name__ == "__main__":
    test_cases = [([2, 7, 11, 15], 9), ([3, 2, 4], 6), ([3, 3], 6)]

    print("Approach 1 (Two-Pointer):")
    for nums, target in test_cases:
        print(f"  {nums}, target={target} -> {Solution().twoSum(nums, target)}")

    print("\nApproach 2 (Hash Map):")
    for nums, target in test_cases:
        print(f"  {nums}, target={target} -> {SolutionHashMap().twoSum(nums, target)}")  