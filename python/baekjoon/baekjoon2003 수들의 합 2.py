n, m = map(int, input().split())

data = list(map(int, input().split()))

left, right = 0, 1
count = 0

while right <= n and left <= right:
    sum_data = data[left:right]
    total = sum(sum_data)

    if total == m:
        count += 1
        left = left + 1
        right = right + 1
    elif total < m:
        right += 1
    else:
        left += 1

print(count)
