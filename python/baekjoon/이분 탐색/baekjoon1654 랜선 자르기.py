n, k = map(int, input().split())

result = 0
datas = []
for _ in range(n):
    datas.append(int(input()))
# [802, 743, 457, 539]

start = 1
# 가장 큰 값을 end로 설정
end = max(datas)  # 802

while start <= end:
    mid = (start + end) // 2  # 401
    target = 0

    # 이 문제의 핵심, 데이터 자체를 순회함
    for data in datas:  # [802, 743, 457, 539]
        target += data // mid  # mid 값으로 나누어 현재 목표(target) 갯수를 구함

    if k <= target:  # 실제 목표 k 보다 현재 목표(target)가 크면
        start = mid + 1

    elif k >= target:  # 실제 목표 k보다 현재 목표(target)가 작으면
        end = mid - 1

print(end)