import sys

input = sys.stdin.readline
sys.setrecursionlimit(10000)


def dfs(index, count):
    if count == m:
        print(*v)
        return

    for i in range(index, n):
        v.append(data[i])
        dfs(i, count + 1)
        v.pop()


n, m = map(int, input().split())

data = list(range(1, n + 1))

v = []

index = 0
count = 0

dfs(index, count)
