# 내가 푼 답
# import sys
#
# N, M = map(int, sys.stdin.readline().split())
#
# data = [[0] * N] * M
#
# small = [0] * M
#
# for i in range(N):
#     data[i] = list(map(int, sys.stdin.readline().split()))
#     data[i].sort()
#     small[i] = data[i][0]
#     small.sort()
#
# print(small[M - 1])


# 이 문제의 핵심 아이디어
# 그리디 알고리즘으로 여러개의 카드 중에서 가장 높은 숫자가 쓰인 카드 한장을 뽑는 경우는
# 각 행의 최소값을 전부 비교하여 그 중에서 가장 큰 수가

# 모범 답안
# min()을 사용한 예시

n, m = map(int, input().split())

result = 0

# 한 줄씩 입력받아 확인
for i in range(n):
    data = list(map(int, input().split()))
    # 현재 줄에서 '가장 작은 수' 찾기
    min_value = min(data)
    # '가장 작은 수'들 중에서 가장 큰 수 찾기
    result = max(result, min_value)  # 두 변 수 중에서 큰 수를 result에 저장

print(result)  # 최종 답안 출력

# 2 중 반복문 구조를 이용하는 예시
n, m = map(int, input().split())

result = 0
for i in range(n):
    data = list(map(int, input().split()))
    min_value = 10001
    for a in data:
        min_value = min(min_value, a)

    result = max(result, min_value)

print(result)
