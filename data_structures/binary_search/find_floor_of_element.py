class Solution(object):
    def findFloorementinArray(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        start = 0
        end = len(nums) - 1
        result = -1

        while start <= end:
            mid = (start + end) // 2 

            if nums[mid] == target:
                end = mid - 1
            elif nums[mid] > target:
                end = mid - 1
            else:
                result = nums[mid]
                start = mid + 1

        return result

if __name__ == "__main__":
    s = Solution()
    # Largest element strictly smaller than target (predecessor)
    print(s.findFloorementinArray([1, 2, 3, 4, 5], 3))   # Expected: 2 (largest < 3)
    print(s.findFloorementinArray([1, 2, 3, 4, 5], 6))   # Expected: 5 (largest < 6)
    print(s.findFloorementinArray([1, 2, 4, 5], 3))      # Expected: 2 (largest < 3)
    print(s.findFloorementinArray([5, 10, 15], 2))       # Expected: -1 (no elem < 2)
    print(s.findFloorementinArray([7], 7))               # Expected: -1 (no elem < 7)
    print(s.findFloorementinArray([7], 5))               # Expected: -1 (no elem < 5)