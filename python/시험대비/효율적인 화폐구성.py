n, m = map(int, input().split())  # 정수 N, M을 입력받기

# N개의 화폐 단위 정보를 입력받기
array = []
for i in range(n):
    array.append(int(input()))

# 다이나믹 프로그래밍 진행(바텀업)
dp = [10001] * (m + 1)  # 0부터 n까지 만들기 위해 +1을 함

dp[0] = 0  # dp[0]에는 0을 대입
for i in range(n):  # 0부터 moeny 종류 배열의 길이 만큼 반복
    for j in range(array[i], m + 1):
        if dp[j - array[i]] != 10001:
            dp[j] = min(dp[j], dp[j - array[i]] + 1)

if dp[m] == 10001:
    print(-1)
else:
    print(dp[m])
