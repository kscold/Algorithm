# 이 문제의 아이디어를 모든 경우를 살펴보는 dp에 점화식 f(n)=f(n-1)+f(n-2)+f(n-3) (n>=4)를 생각하는 것이다.
# 따라서 제일 작은 수 4를 대입해보았을 때 f(4) =

T = int(input())

memo = {1: 1, 2: 2, 3: 4}

def dp(x):
    if x in memo:
        return memo[x]
    memo[x] = dp(x- 1) + dp(x - 2) + dp(x - 3)

    return memo[x]

for i in range(T):
    n = int(input())
    print(dp(n))
