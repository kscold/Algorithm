# import sys
#
# input = sys.stdin.readline
# sys.setrecursionlimit(10000)
#
# n = int(input())
#
#
# def permutation(arr, r):
#     arr = sorted(arr)
#     memo = [0 for _ in range(len(arr))]
#
#     def generate(chosen, memo):
#         if len(chosen) == r:
#             for i in chosen:
#                 print(i, end=" ")
#             print()
#             return
#
#         for i in range(len(arr)):
#             if memo[i] == 0:
#                 chosen.append(arr[i])
#                 memo[i] = 1
#                 generate(chosen, memo)
#                 memo[i] = 0
#                 chosen.pop()
#
#     generate([], memo)
#
#
# permutation(list(range(1, n + 1)), n)

import sys

input = sys.stdin.readline
sys.setrecursionlimit(10000)

n = int(input())
temp = []


def dfs():
    if len(temp) == n:
        print(*temp)
        return
    for i in range(1, n + 1):
        if i not in temp:
            temp.append(i)
            dfs()
            temp.pop()


dfs()
