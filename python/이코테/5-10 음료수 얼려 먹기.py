# 예시
# 4 5
# 00110
# 00011
# 11111
# 00000
# DFS 풀이
n, m = map(int, input().split())
graph = []

for i in range(n):
    graph.append(list(map(int, input())))

count = 0


def dfs(x, y):
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False

    if graph[x][y] == 0:
        graph[x][y] = 1  # 해당 노드 방문 처리

        # 상, 하, 좌, 우의 위치도 모두 재귀적으로 호출
        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)
        return True

    return False


# 모든 노드(위치)에 대하여 음료수 채우

# 카운트를 세기 위한 코드
result = 0
for i in range(n):
    for j in range(m):
        # 현재 위치에서 DFS 수행
        if dfs(i, j) == True:
            result += 1

print(result)

# BFS 풀이
# 음료수 얼려먹기 - BFS - 타인 코드
from collections import deque

n, m = map(int, input().split())

# 그래프 생성
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

# 상하좌우 탐색
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

# BFS
def bfs(x, y):
    # 현재 위치를 큐에 집어넣음
    q = deque()
    q.append((x,y))

    # 만약 현재 위치가 1이라면 아이스크림을 만들 수 없는 공간이거나 이미 탐색한 곳이므로 False 반환
    if graph[x][y] == 1:
        return False

    # 현재 위치를 기준으로 BFS 탐색
    while q:
        x, y = q.popleft()
        # 현재 위치 값을 0에서 1로 변경
        graph[x][y] = 1
        # 상하좌우 탐색
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 얼음 틀 범위에서 벗어나지 않으면서 그 위치의 값이 0인 경우에만 큐에 집어넣음
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0:
                q.append((nx,ny))
    # 하나의 아이스크림이 만들어지는 공간을 모두 탐색한 경우 True
    return True

cnt = 0

for i in range(n):
    for j in range(m):
        # 현재 위치에서 BFS 수행
        if bfs(i, j) == True:
            cnt += 1

print(cnt)
