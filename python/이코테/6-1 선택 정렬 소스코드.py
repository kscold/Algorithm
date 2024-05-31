# 선택 정령 가장 작은 데이터를 선택해 맨 앞에 있는 데이터와 바꾸고 그 다음 작은 데이터를 선택해

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)):
    min_index = i  # 현재의 인덱스를 변수에 저장
    for j in range(i + 1, len(array)):  # 그 다음 인덱스랑 비교하면서 가장 작은 인덱스를 찾음
        if array[min_index] > array[j]:  # 현재 값이 다음 인덱스 값보다 크면
            min_index = j # 현재 인덱스에 가장 작은 인덱스를 넣음
    array[i], array[min_index] = array[min_index], array[i]  # 원 인덱스와 가작 작은 값의 인덱스를 스와프

print(array)
