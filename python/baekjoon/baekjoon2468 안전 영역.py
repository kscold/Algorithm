import sys

sys.setrecursionlimit(100000)


def dfs(x, y, height):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0:
            if graph[nx][ny] > height:
                visited[nx][ny] = 1
                dfs(nx, ny, height)


n = int(input())

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

graph = []
max_height = 0

for i in range(n):
    lows = list(map(int, input().split()))
    graph.append(lows)

    for low in lows:
        if low > max_height:
            max_height = low

result = 1
for height in range(max_height):
    visited = [[0] * n for _ in range(n)]
    count = 0

    for y in range(n):
        for x in range(n):
            if graph[y][x] > height and visited[y][x] == 0:
                visited[y][x] = 1
                count += 1
                dfs(y, x, height)
    result = max(result, count)

print(result)
