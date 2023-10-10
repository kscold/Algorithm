# 계단으로 오를 때 최댓값을 구한다.
# 10 20 15 25 10 20

#DP 탑다운을 이용한 방식
n = int(input())
stair = [0] * (n + 1)
for i in range(1, n + 1):
    stair[i] = int(input())

memo = [-1] * (n + 1)  # 메모이제이션을 위한 배열, -1로 초기화

def dp(st_count):
    if st_count <= 0:
        return 0

    if memo[st_count] != -1:
        return memo[st_count]

    # st_count 계단에 도달할 때의 최대 점수를 구하는 부분
    memo[st_count] = max(dp(st_count - 2) + stair[st_count], dp(st_count - 3) + stair[st_count - 1] + stair[st_count])
    return memo[st_count]


result = dp(n)
print(result)



#DP 바텀 업을 이용한 방식
n = int(input())
stair = [0] * (n+1)
for i in range(1, n+1):
    stair[i] = int(input())

dp = [0] * (n + 1)
dp[1] = stair[1]
dp[2] = stair[1] + stair[2]
dp[3] = max(stair[1] + stair[3], stair[2] + stair[3])

for i in range(4, n+1):
    dp[i] = max(dp[i - 2] + stair[i], dp[i - 3] + stair[i - 1] + stair[i])

print(dp[n])
