import sys
# dfs의 한번 노드와 연결되면 모두 탐색을하는 특징을 이용ㄱ

def dfs(x, y):
    # 주어진 범위를 벗어나는 경우에는 즉시 종료
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False

    # 현재 노드를 아직 방문하지 않았다면
    if graph[x][y] == 0: # 0인 부분이 아이스크림이 쏟아진 덩어리 부분이므로
        # 해당 노드 방문 처리
        graph[x][y] = 1
        # 상, 하, 좌, 우의 위치들도 모두 재귀적으로 호출
        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)
        return True
    return False  # 방문한 곳이라면 즉 1이라면 바로 dfs 종료


n, m = map(int, sys.stdin.readline().split())

graph = []

for i in range(n):
    graph.append(list(map(int, sys.stdin.readline().rstrip())))

result = 0
for i in range(n):
    for j in range(m):
        # 현재 위치에서 DFS 수행
        if dfs(i, j) == True:
            result += 1

print(result)
