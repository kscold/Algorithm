# 5 6
# 101010
# 111111
# 000001
# 111111
# 111111

# bfs 풀이(미로이기 때문에 bfs는 자동적으로 최단경로를 찾는다)
from collections import deque

n, m = map(int, input().split())

gragh = []
for i in range(n):
    gragh.append(list(map(int, input())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
# 상, 하, 좌, 우


def bfs(x, y):
    queue = deque()
    queue.append((x, y)) # 시작 좌표를 큐에 넣고 시작
    # 큐가 빌 때까지 반복
    while queue:
        x, y = queue.popleft()
        # 현재 위치에서 네 방향으로의 위치 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 미로 찾기 공간을 벗어날 경우 무시
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            # 벽(괴물)인 경우 무시
            if gragh[nx][ny] == 0:
                continue
            # 해당 노드를 처음 방문하는 경우에만 최단 거리 기록
            if gragh[nx][ny] == 1:
                gragh[nx][ny] = gragh[x][y] + 1 # 그 좌표에 현재까지의 거리를 저장, 방문을 저장하는 것이 아니라 값을 저장하는 것임
                queue.append((nx, ny))
    # 가장 오른쪽 아래까지의 최단 거리 반환
    return gragh[n - 1][m - 1] # 가장 마지막칸에 최단경로의 횟수가 저장되어 있음


# BFS를 수행한 결과 출력
print(bfs(0, 0))
