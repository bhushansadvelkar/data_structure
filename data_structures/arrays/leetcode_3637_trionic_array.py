"""
3637. Trionic Array I
https://leetcode.com/problems/trionic-array-i/

Difficulty: Easy
Topics: Array, Simulation

Problem:
--------
A trionic array is an array that has three distinct phases in order:
1. Increasing (slot1): nums[i] < nums[i+1]
2. Decreasing (slot2): nums[i] > nums[i+1] (must occur after slot1)
3. Increasing again (slot3): nums[i] < nums[i+1] (must occur after slot2)

Return true if the array is trionic, false otherwise.
- No adjacent elements can be equal
- All three phases must be present

Examples:
---------
Example 1:
    Input: nums = [1, 4, 2, 3]
    Output: True
    Explanation: 1<4 (slot1), 4>2 (slot2), 2<3 (slot3)

Example 2:
    Input: nums = [1, 3, 5, 4, 2, 6, 8]
    Output: True
    Explanation: Up to 5, down to 2, up to 8

Example 3:
    Input: nums = [1, 2, 3]
    Output: False
    Explanation: Only increasing, missing slot2 and slot3

Constraints:
------------
- 2 <= nums.length <= 100
- 1 <= nums[i] <= 100

Approach: Single Pass State Machine
-----------------------------------
Track three boolean flags (slot1, slot2, slot3) as we traverse.
- slot1: seen increasing pair
- slot2: seen decreasing pair (only if slot1 done)
- slot3: seen increasing pair after slot2
Return False if adjacent equal, or if we hit an invalid transition.

Time Complexity: O(n)
    - Single pass through the array

Space Complexity: O(1)
    - Only three boolean variables
"""


class Solution(object):
    def isTrionic(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        slot1 = False 
        slot2 = False 
        slot3 = False 
        
        for i in range(len(nums) - 1):
            if nums[i] == nums[i+1]:
                return False 
            if nums[i] < nums[i+1] and not slot2 and not slot3:
                slot1 = True 
            elif nums[i] > nums[i+1] and slot1 and not slot3:    
                slot2 = True
            elif nums[i]<nums[i+1] and slot2:
                slot3=True
            else:
                return False
            
        return slot1 and slot2 and slot3


if __name__ == "__main__":
    # Valid: up -> down -> up
    print(Solution().isTrionic([1, 4, 2, 3]))  # Expected: True

    # Valid: longer trionic
    print(Solution().isTrionic([1, 3, 5, 4, 2, 6, 8]))  # Expected: True

    # Invalid: only increasing (no decrease then increase)
    print(Solution().isTrionic([1, 2, 3]))  # Expected: False

    # Invalid: only decreasing
    print(Solution().isTrionic([3, 2, 1]))  # Expected: False

    # Invalid: adjacent equal elements
    print(Solution().isTrionic([1, 2, 2, 3]))  # Expected: False

    # Invalid: up then down but no second up
    print(Solution().isTrionic([1, 3, 2]))  # Expected: False (need slot3)