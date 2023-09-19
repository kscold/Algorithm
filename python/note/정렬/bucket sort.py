def bucket_sort(arr):
    # 1. 입력 배열의 최댓값을 찾아서 버킷 개수를 결정
    max_value = max(arr)
    bucket_count = max_value + 1

    # 2. 빈 버킷 리스트 생성
    buckets = [[] for _ in range(bucket_count)]

    # 3. 각 요소를 버킷에 맞게 배치
    for num in arr:
        buckets[num].append(num)

    # 4. 각 버킷 내부를 정렬하고, 정렬된 값을 결과 리스트에 추가
    sorted_arr = []
    for bucket in buckets:
        if bucket:
            bucket.sort()
            sorted_arr.extend(bucket)

    return sorted_arr


A = list(map(int, input().split()))
print(bucket_sort(A))
