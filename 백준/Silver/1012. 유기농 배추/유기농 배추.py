import sys
sys.setrecursionlimit(10000)

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

for _ in range(t):
    m, n, k = map(int, input().split())
    data = [[0] * m for _ in range(n)]
    result = 0

    for _ in range(k):
        x, y = map(int, input().split())
        data[y][x] = 1


    for i in range(m):
        for j in range(n):
            if data[j][i] == 1: 
                dfs(data, i, j)
                result += 1
    print(result)