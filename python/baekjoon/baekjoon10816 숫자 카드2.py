# 시간 초과 답안 일반 이분 탐색 구현 후 리스트에 같은 데이터가 있는지 확인
# def binarySearch(datas, target):
#     start = 0
#     end = m - 1
#
#     while start <= end:
#         mid = (start + end) // 2
#
#         if datas[mid] == target:
#             return mid
#         elif datas[mid] < target:
#             start = mid + 1
#         elif datas[mid] > target:
#             end = mid - 1
#     return -1
#
#
# n = int(input())
# inits = list(map(int, input().split()))
# inits.sort()
#
# m = int(input())
# datas = list(map(int, input().split()))
#
# result = []
# for data in datas:
#     count = 0
#     index = binarySearch(inits, data)
#
#     # 리스트에 겹치는 데이터가 있는지 확인하는 구현을 사용
#     if index != -1:
#         count = 1
#         left = index - 1
#         while left >= 0 and inits[left] == data:
#             count += 1
#             left -= 1
#
#         right = index + 1
#         while right < n and inits[right] == data:
#             count += 1
#             right += 1
#
#     result.append(count)
#
# print(' '.join(map(str, result)))

# 딕셔너리 이분 탐색 응용
n = int(input())
cards = list(map(int, input().split()))
cards.sort()

m = int(input())
targets = list(map(int, input().split()))

count = {}
for card in cards:
    if card in count:
        count[card] += 1
    else:
        count[card] = 1


def binarySearch(arr, target, start, end):
    if start > end:
        return 0

    mid = (start + end) // 2
    if arr[mid] == target:
        return count.get(target)
    elif arr[mid] < target:
        return binarySearch(arr, target, mid + 1, end)
    elif arr[mid] > target:
        return binarySearch(arr, target, start, end - 1)


for target in targets:
    print(binarySearch(cards, target, 0, n - 1), end=" ")

# 딕셔너리 응용
n = int(input())
cards = list(map(int, input().split()))
m = int(input())
targets = list(map(int, input().split()))

count = {}
for card in cards:
    if card in count:
        count[card] += 1
    else:
        count[card] = 1

for target in targets:
    result = count.get(target)  # target(key)로 하는 value를 가져옴
    if result == None:
        print(0, end=" ")
    else:
        print(result, end=" ")
