class Solution(object):
    def getMaximumGenerated(self, n):
        """
        :type n: int
        :rtype: int
        """
        memo = {}

        def dp(i):
            if i in memo:
                return memo[i]

            if i == 0:
                return 0

            if i == 1:
                return 1

            if i % 2 == 0:
                memo[i] = dp(i // 2)
            else:
                memo[i] = dp(i // 2) + dp(i // 2 + 1)

            return memo[i]

        max_int = 0
        for i in range(0, n + 1):
            max_int = max(max_int, dp(i))

        return max_int


n = int(input())
solution = Solution()
maxgenerated = solution.getMaximumGenerated(n)
print(maxgenerated)
