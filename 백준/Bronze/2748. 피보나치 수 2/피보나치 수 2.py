n = int(input())

memo = {}

def dp(n):
    if n in memo:
        return memo[n]

    if n == 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 1

    for i in range(3, n + 1):
        memo[i] = dp(i - 1) + dp(i - 2)

    return memo[n]

result = dp(n)
print(result)