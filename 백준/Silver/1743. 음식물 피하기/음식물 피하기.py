from collections import deque


def bfs(y, x):
    global count
    queue = deque([(y, x)])
    count += 1
    graph[y][x] = -1

    while queue:
        y, x = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= ny < n and 0 <= nx < m and graph[ny][nx] == 1:
                queue.append((ny, nx))
                count += 1
                graph[ny][nx] = -1


n, m, k = map(int, input().split())

graph = [[0] * m for _ in range(n)]

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
count = 0

for _ in range(k):
    y, x = map(int, input().split())
    graph[y - 1][x - 1] = 1

count_list = []
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            count = 0
            bfs(i, j)
            count_list.append(count)

print(max(count_list))
