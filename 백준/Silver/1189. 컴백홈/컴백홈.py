R, C, K = list(map(int, input().split()))

data = [list(map(str, input())) for _ in range(R)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

count = 0


def dfs(x, y, distance):
    global count

    if distance == K and y == C - 1 and x == 0:
        count += 1
    else:
        data[x][y] = 'T'
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < R and 0 <= ny < C and data[nx][ny] == ".": 
                data[nx][ny] = 'T'
                dfs(nx, ny, distance + 1)
                data[nx][ny] = "."


dfs(R - 1, 0, 1)
print(count)