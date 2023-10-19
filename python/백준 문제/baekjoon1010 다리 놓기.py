# 일반적인 재귀함수로 구현
# def factorial(N):
#     if N >1:
#         return (N* factorial(N-1))
#     else:
#         return 1
#
# T = int(input())
# for _ in range(T):
#     N, M = list(map(int, input().split()))
#     print(factorial(M) // factorial(M-N) * factorial(N))


T = int(input())
dp = [[0] * 30 for _ in range(30)]
for i in range(30):
    for j in range(30):
        if i == 1:
            dp[i][j] = j
        else:
            if i == j:
                dp[i][j] = 1
            elif i < j:
                dp[i][j] = dp[i-1][j-1] + dp[i][j-1]

for _ in range(T):
    N, M = list(map(int, input().split()))
    print (dp[N][M])
