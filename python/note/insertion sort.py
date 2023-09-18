def insertion_sort(arr):
    for end in range(1, len(arr)):  # 1부터 arr길이 -1 까지
        for i in range(end, 0, -1):  #
            if arr[i - 1] > arr[i]:  # 만약 이전 값이 현재값보다 크면
                arr[i - 1], arr[i] = arr[i], arr[i - 1]  # swap

    return arr


a = list(map(int, input().split()))
print(a)
print(insertion_sort(a))


# 최적화된 코드

def insertion_sort2(arr2):
    for end in range(1, len(arr2)):  # 1부터 arr 길이 - 1 까지
        i = end
        while i > 0 and arr2[i - 1] > arr2[i]:
            arr2[i - 1], arr2[i] = arr2[i], arr2[i - 1]  # swap
            i -= 1

    return arr2

b = list(map(int, input().split()))
print(b)
print(insertion_sort2(b))


