arr = [1, 1, 1, 2, 2, 3, 3, 3]

result = []
for index, data in enumerate(arr):
    count = 0
    left = index - 1
    while left >= 0 and arr[left] == data:
        count += 1
        left -= 1

    right = index + 1
    while right < len(arr) and arr[right] == data:
        count += 1
        right += 1

    result.append(count + 1)

print(result)

arr = [1, 1, 1, 2, 2, 3, 3, 3]

result = []
for data in arr:
    count = 0
    for element in arr:
        if element == data:
            count += 1
    result.append(count)

print(result)
