
def sequential_search(arr, target):
    n = len(arr)
    for i in range(0, n):
        if arr[i] == target:
            return i
    return -1

A = list(map(int, input().split()))
findA = (int(input()))
print(sequential_search(A, findA))