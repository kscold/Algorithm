import sys

sys.setrecursionlimit(10000)
input = sys.stdin.readline


def dfs(graph, v, visited, count):
    visited[v] = True

    count += 1

    if v == target2:
        result.append(count)

    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited, count)


n = int(input())
target1, target2 = map(int, input().split())
m = int(input())

visited = [False] * (n + 1)
graph = [[] for _ in range(n + 1)]
result = []

count = 0

for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

dfs(graph, target1, visited, count)

if len(result) == 0:
    print(-1)
else:
    print(result[0] - 1)
