class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        result = []
        stack = []

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
    print(Solution().dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))  # Expected: [1, 1, 4, 2, 1, 1, 0, 0]
    print(Solution().dailyTemperatures([30, 40, 50, 60]))  # Expected: [1, 1, 1, 0]
    print(Solution().dailyTemperatures([30, 60, 90]))  # Expected: [1, 1, 0]
