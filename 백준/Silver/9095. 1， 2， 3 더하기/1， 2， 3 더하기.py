memo = {1: 1, 2: 2, 3: 4}

def dp(x):
    if x in memo:
        return memo[x]
    memo[x] = dp(x- 1) + dp(x - 2) + dp(x - 3)

    return memo[x]

T = int(input())

for i in range(T):
    n = int(input())
    print(dp(n))
