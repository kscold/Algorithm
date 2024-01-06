# N개의 정수 A[1], A[2], …, A[N]이 주어져 있을 때, 이 안에 X라는 정수가 존재하는지 알아내는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 자연수 N(1 ≤ N ≤ 100,000)이 주어진다. 다음 줄에는 N개의 정수 A[1], A[2], …, A[N]이 주어진다.
# 다음 줄에는 M(1 ≤ M ≤ 100,000)이 주어진다. 다음 줄에는 M개의 수들이 주어지는데, 이 수들이 A안에 존재하는지 알아내면 된다.
# 모든 정수의 범위는 -231 보다 크거나 같고 231보다 작다.

# 출력
# M개의 줄에 답을 출력한다.

# 예제 입력 1
# 5
# 4 1 5 2 3
# 5
# 1 3 7 9 5

# 예제 출력 1
# 1
# 1
# 0
# 0
# 1

# 내가 짠 코드 이분 탐색에 맞는 알고리즘 코드이나 그러나 시간 초과가 난다. 따라서 list O(n)인 리스트를 사용하지 않고 set를 사용하여 O(1)로 풀 수 있다.
# import sys
#
# input = sys.stdin.readline
#
#
# def binarySearch(data, target):
#     data.sort()
#     start = 0
#     end = len(data) - 1
#
#     while (start <= end):
#         mid = (start + end) // 2
#
#         if data[mid] == target:
#             return 1
#         elif data[mid] < target:
#             start = mid + 1
#         else:
#             end = mid - 1
#     return 0
#
#
# n = int(input())
#
# data = list(map(int, input().split()))
#
# m = int(input())
# target = list(map(int, input().split()))
#
# for t in target:
#     result = binarySearch(data, t)
#     print(result)

# 정답이지만 set를 이용한 방법
# import sys
#
# input = sys.stdin.readline
#
# n = int(input())
# data = set(map(int, input().split()))
# m = int(input())
# target = list(map(int, input().split()))
#
# for t in target:
#     if t in data:
#         print(1)
#     else:
#         print(0)

# nlogn의 이진 탐색을 이용한 정답 코드
import sys

input = sys.stdin.readline


def binary_search(data, target, start=0, end=None):
    if end == None:
        end = len(data) - 1
    if start > end:
        return 0

    mid = (start + end) // 2

    if data[mid] == target:
        return 1
    elif data[mid] < target:
        start = mid + 1
    elif data[mid] > target:
        end = mid - 1

    return  binary_search(data, target, start, end)

n = int(input())
data = list(map(int, input().split()))
sorted_data = sorted(data)

m = int(input())
target = list(map(int, input().split()))

for i in range(len(target)):
    print(binary_search(sorted_data, target[i]))
