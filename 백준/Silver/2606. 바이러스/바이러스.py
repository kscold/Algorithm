import sys

sys.setrecursionlimit(10000)

input = sys.stdin.readline


def dfs(graph, v, visited):
    global count
    visited[v] = True
    count += 1

    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)


v = int(input())
e = int(input())

graph = [[] for _ in range(v + 1)]
for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for low in graph:
    low.sort()

visited = [False] * (v + 1)

count = 0
dfs(graph, 1, visited)
print(count - 1)
