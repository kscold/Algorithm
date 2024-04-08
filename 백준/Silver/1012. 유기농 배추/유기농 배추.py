import sys

sys.setrecursionlimit(2501)


def dfs(graph, x, y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if (0 <= nx < m) and (0 <= ny < n):
            if graph[ny][nx] == 1:
                graph[ny][nx] = -1
                dfs(graph, nx, ny)


t = int(input())

for i in range(t):
    m, n, k = map(int, input().split())
    graph = [[0] * m for _ in range(n)]

    result = 0

    for _ in range(k):
        x, y = map(int, input().split())
        graph[y][x] = 1

    for y in range(n):
        for x in range(m):
            if graph[y][x] == 1:
                dfs(graph, x, y)
                result += 1

    print(result)
