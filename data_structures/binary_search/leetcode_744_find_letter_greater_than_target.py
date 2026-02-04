class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        start = 0
        end = len(letters) - 1
        result = None

        while start <= end:
            mid = (start + end) // 2

            if letters[mid] == target:
                start = mid + 1
            elif letters[mid] > target:
                result = letters[mid]
                end = mid - 1
            else:
                start = mid + 1

        return result if result is not None else letters[0]



if __name__ == "__main__":
    s = Solution()
    print(s.nextGreatestLetter(["c", "f", "j"], "a"))   # Expected: "c"
    print(s.nextGreatestLetter(["c", "f", "j"], "c"))   # Expected: "f"
    print(s.nextGreatestLetter(["x", "x", "y", "y"], "z"))  # Expected: "x"
    print(s.nextGreatestLetter(["c", "f", "j"], "j"))   # Expected: "c"