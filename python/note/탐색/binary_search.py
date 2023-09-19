def binary_search(arr, target):
    start = 0
    end = len(arr) - 1 # start가 0부터 이므로

    while start <= end: # start가 end보다 커질 때까지 반복
        mid = (start + end) // 2 # 중간값을 mid로 잡음

        if arr[mid] == target: # 리스트 요소가 target을 찾으면
            return mid # 바로 mid 인덱스를 반환
        elif arr[mid] < target: # 리스트 요소가 target보다 작으면
            start = mid + 1 # 리스트 index를 오른쪽으로 한칸 이동
        else:
            end = mid - 1 # 리스트 index를 왼쪽으로 한칸 이동
    return -1

A = list(map(int, input().split()))
findA = (int(input()))
print(binary_search(A, findA))


# 재귀적으로 구현
def binary_search_recursion(arr, target, start, end):
    if start > end:
        return -1

    mid = (start+end) // 2

    if arr[mid] == target:
        return mid
    elif arr[mid] == target:
        end = mid - 1
    else:
        start = mid + 1

    return binary_search_recursion(arr, target, start, end)


B = list(map(int, input().split()))
start = 0
end = len(B) - 1
findB = (int(input()))
print(binary_search_recursion(B, findB, start, end))
