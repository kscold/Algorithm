# 최악의 경우 O(n^2), 입력 배열이 차이하는 메모리만 사용하는 in-place sorting 방식으로 구현할 경우 O(log(n))

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]  # 리스트의 가운데 있는 값을 pivot으로 선택, pivor 값보다 작은 값, 동일한 값 그리고 큰 값을 담아둘 3개의 리스트를 생성

    lesser_arr, equal_arr, greater_arr = [], [], []

    for num in arr:
        if num < pivot:
            lesser_arr.append(num)

        elif num > pivot:
            greater_arr.append(num)

        else:
            equal_arr.append(num)
    return quick_sort(lesser_arr) + equal_arr + quick_sort(greater_arr)

A = list(map(int, input().split()))
print(quick_sort(A))

# 최적화된 코드

def quick_sort2(arr):
    def sort(low, high):
        if high <= low:
            return

        mid = partition(low, high)
        sort(low, mid - 1)
        sort(mid, high)

    def partition(low, high):
        pivot = arr[(low + high) // 2]
        while low <= high:
            while arr[low] < pivot:
                low += 1
            while arr[high] > pivot:
                high -= 1
            if low <= high: # 피벗을 기준으로 작은 값은 왼쪽으로, 큰 값은 오른쪽으로 이동하는 과정을 제어
                arr[low], arr[high] = arr[high], arr[low]
                low, high = low + 1, high - 1 # 피벗을 기준으로 작은 값과 큰 값의 위치를 찾아가는 과정 -> 범위를 줄여감
        return low

    return sort(0, len(arr) - 1)

B = list(map(int, input().split()))
quick_sort(B)
print(B)