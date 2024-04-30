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