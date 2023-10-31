# 이중 반복문 구조를 이용하는 답안 예시
n, m = map(int, input().split())

result = 0
# 한 줄씩 입력받아 확인
for i in range(n):
    data = list(map(int, input().split()))
    # 현재 줄에서 '가장 작은 수' 찾기
    min_value = 10001
    for a in data: # for문을 이용하여 min 값을 탐색
        min_value = min(min_value, a) # 처음에는 10000 이하의 수만 허용하므로 10001과 비교 그 이후에는 처음 값과 다음값 비교 식으로 최솟값을 찾음
    # '가장 작은 수'들 중에서 가장 큰 수 찾기
    result = max(result, min_value) # n 행번 만큼 반복하여 최종 정답값을 찾음

print(result)