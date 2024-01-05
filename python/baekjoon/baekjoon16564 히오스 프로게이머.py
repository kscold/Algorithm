import sys

input = sys.stdin.readline

n, k = map(int, input().split())
levels = [int(input()) for _ in range(n)]

levels.sort()
start = levels[0]  # 시작 값은 최소값
end = start + k  # 마지막 값은 최소값에 k를 더한 값

res = 0
while (start <= end): # 15 16 17
    mid = (start + end) // 2  # 이분탐색의 중값을 지정

    diff_sum = 0 # 차이의 합을 다시 초기화
    for level in levels:
        if mid > level:  # 현재 레벨보다 mid값이 더 크면
            diff_sum += (mid - level)  # 중간 값과 level 값의 차이 15 - 10, 15 - 15, 15 - 20, 18 - 10, 18 - 15, 18 - 20

    if diff_sum <= k:  # 중간값과의 현재 레벨의 차이의 합 <= 총 올릴 수 있는 레벨 k 일때
        start = mid + 1
        res = max(mid, res) # 15
    else:  # 중간값과 현재 레벨의 차이의 합 > 총 올릴 수 있는 레벨의 k일 때 # 19 18
        end = mid - 1

print(res)
