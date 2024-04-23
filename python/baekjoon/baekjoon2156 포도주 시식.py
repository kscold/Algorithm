# 탑다운 방식
import sys

sys.setrecursionlimit(100000)
input = sys.stdin.readline


def dp(n):
    if memo[n] != 0:
        return memo[n]

    if n == 0:
        return data[0]
    elif n == 1:
        return data[0] + data[1]
    elif n == 2:
        return max(dp(1), max(data[0], data[1]) + data[2])

    memo[n] = max(dp(n - 1), dp(n - 2) + data[n], dp(n - 3) + data[n - 1] + data[n])

    return memo[n]


n = int(input())

data = []
for _ in range(n):
    data.append(int(input()))

memo = [0] * n

print(dp(n - 1))

# 바텀업 방식
n = int(input())

data = []
for _ in range(n):
    data.append(int(input()))

memo = [0] * n
memo[0] = data[0]

if 1 < n:
    memo[1] = data[0] + data[1]
if 2 < n:
    memo[2] = max(memo[1], max(data[0], data[1]) + data[2])

for i in range(3, n):
    memo[i] = max(memo[i - 1], memo[i - 2] + data[i], memo[i - 3] + data[i - 1] + data[i])

print(memo[n - 1])
