import sys

sys.setrecursionlimit(10000)


def dfs(y, x, count, color):
    graph[y][x] = 0
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < m:
            if graph[ny][nx] == color:
                count = dfs(ny, nx, count + 1, color)
    return count


n, m = map(int, input().split())

graph = []
for _ in range(m):
    graph.append(list(map(str, input())))

white = 0
blue = 0
for y in range(m):
    for x in range(n):
        if graph[y][x] == "W":
            white += (dfs(y, x, 1, "W")) ** 2
        elif graph[y][x] == "B":
            blue += (dfs(y, x, 1, "B")) ** 2

print(white, blue)
