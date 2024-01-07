array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)):
    min_index = i  # 가장 작은 원소의 인덱스
    for j in range(i + 1, len(array)):  # 그 다음 인덱스랑 비교
        if array[min_index] > array[j]:  # 인덱스 값을 비교하면서 결과적으로 가장 작은 값의 인덱스를 찾음
            min_index = j
    array[i], array[min_index] = array[min_index], array[i]  # 원 인덱스와 가작 작은 값의 인덱스를 스와프

print(array)
