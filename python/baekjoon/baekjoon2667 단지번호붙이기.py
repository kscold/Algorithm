import sys

input = sys.stdin.readline


def dfs(y, x):
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    global count

    if x < 0 or x >= n or y < 0 or y >= n:
        return

    if graph[y][x] == 1:
        count += 1
        graph[y][x] = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            dfs(ny, nx)


n = int(input())

graph = []
result = []
count = 0

for _ in range(n):
    graph.append(list(map(int, input().rstrip())))

for y in range(n):
    for x in range(n):
        if graph[y][x] == 1:
            dfs(y, x)
            result.append(count)
            count = 0

result.sort()

print(len(result))
for k in result:
    print(k)
