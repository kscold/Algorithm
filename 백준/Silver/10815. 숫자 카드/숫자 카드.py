import sys

input = sys.stdin.readline


def binarySearch(target):
    l, r = 0, n - 1

    while l <= r:
        mid = (l + r) // 2
        if dataList[mid] == target:
            return True
        elif dataList[mid] < target:
            l = mid + 1
        elif dataList[mid] > target:
            r = mid - 1
    return False


n = int(input())
dataList = list(map(int, input().split()))
dataList.sort()

m = int(input())
targetList = list(map(int, input().split()))

for target in targetList:
    if binarySearch(target) == True:
        print(1, end=" ")
    else:
        print(0, end=" ")
