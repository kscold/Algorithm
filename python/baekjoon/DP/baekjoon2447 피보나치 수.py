# 탑다운 방식
import sys

input = sys.stdin.readline
sys.setrecursionlimit(10000)


def dp(n):
    if memo[n] > 0:
        return memo[n]

    if n == 0:
        return 0

    elif n == 1:
        return 1

    else:
        memo[n] = dp(n - 1) + dp(n - 2)
        return memo[n]


n = int(input())
memo = [0] * (n + 1)

print(dp(n))

# 바텀 업 방식
n = int(input())

dp = [0] * (n + 1)
dp[0] = 0
dp[1] = 1

for i in range(2, n + 1):
    dp[i] = dp[i - 2] + dp[i - 1]

print(dp[n])
