class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        dp = [[0] * (rowIndex + 1) for _ in range(rowIndex + 1)]

        dp[0][0] = 1
        for i in range(rowIndex + 1):
            for j in range(i + 1):
                if j == 0 or i == j:
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]

        return dp[rowIndex]

n = int(input())
solution = Solution()
result = solution.getRow(n)
print(result)