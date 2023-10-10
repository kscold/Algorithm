class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """

        if n <= 2: # 초기값을 설정하기 위한 설정 없으면 1, 2 입력시 오류
            return n

        dp = [0] * (n + 1)
        dp[1] = 1
        dp[2] = 2

        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[n]

n = int(input())
solution = Solution()
result = solution.climbStairs(n)
print(result)