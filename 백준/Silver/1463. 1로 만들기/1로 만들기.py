N = int(input())

memo = {}


def dp(x):
    if x in memo:
        return memo[x]

    if x == 1:  # 1일 때 1이 되는데 필요한 연산 횟수가 0회그럼
        return 0

    if (x % 3 == 0) and (x % 2 == 0):
        memo[x] = min(dp(x // 3) + 1, dp(x // 2) + 1)

    elif x % 3 == 0:
        memo[x] = min(dp(x // 3) + 1, dp(x - 1) + 1)

    elif x % 2 == 0:
        memo[x] = min(dp(x // 2) + 1, dp(x - 1) + 1)

    else:
        memo[x] = dp(x - 1) + 1
    return memo[x]


print(dp(N))
