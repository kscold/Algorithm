array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]


def quick_sort(array, start, end): # 리스트, 피벗, 갯수
    if start >= end:  # 원소 1개인 경우 종료
        return
    pivot = start  # 피벗은 첫 번째 원소 인덱스
    left = start + 1 # 왼쪽 탐색 목표는 피벗 다음 인덱스
    right = end # 오른쪽 탐색 목표는 마지막 인덱스
    while left <= right: # 왼쪽 탐색 목표가 오른쪽 탐색 목표보다 작거나 같을 때까지 반복
        # 피벗보다 큰 데이터를 찾을 때까지 반복
        while left <= end and array[left] <= array[pivot]:  # 다음 인덱스 요소가 현재 피벗 인덱스 요소보다 크면 반복
            left += 1  # left 탐색 진행
        # 피벗보다 작은 데이터를 찾을 때까지 반복
        while right > start and array[right] >= array[pivot]:  # 마지막 인덱스 요소가 현재 피벗 인덱스 요소보다 크면 반복
            right -= 1  # left 탐색 진행

        if left > right:  # 엇갈렸다면 작은 데이터와 피벗을 교체
            array[right], array[pivot] = array[pivot], array[right]
        else:  # 엇갈리지 않았다면 작은 데이터와 큰 데이터 교체
            array[left], array[right] = array[right], array[left]

    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행
    quick_sort(array, start, right - 1)
    quick_sort(array, right + 1, end)


quick_sort(array, 0, len(array) - 1)
print(array)
