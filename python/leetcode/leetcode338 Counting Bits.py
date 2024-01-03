# Input: n = 5
# Output: [0,1,1,2,1,2]
# Explanation:
# 0 --> 0 = 0
# 1 --> 1 = 1
# 2 --> 10 = 1
# 3 --> 11 = 2
# 4 --> 100 = 1
# 5 --> 101 = 2
# 예시를 보면 1과 0을 왼쪽에서 오른쪽으로 밀어서 합치면 됨

# Input: n = 2
# Output: [0,1,1]
# Explanation:
# 0 --> 0
# 1 --> 1
# 2 --> 10
class Solution(object):
    def countBits(self, n):

        dp = [0] * (n + 1) # [0,0,0,0,0,0]
        count = 1

        for i in range(1, n + 1):
            if count * 2 == i: # 2 == 2
                count = i #count = 2
            dp[i] = 1 + dp[i - count] # dp[2] = 1 + dp[2 -2 ], d[2] = 1 ,d[1] = 1 , d[0] = 0

        return dp

n = int(input())
solution = Solution()
result = solution.countBits(n)
print(result)