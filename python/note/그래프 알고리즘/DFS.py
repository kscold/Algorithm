# DFS
def dfs(graph, v, vistied):  # (그래프, 노드(정점), 방문처리 정보 리스트)
    vistied[v] = True  # 현재 노드를 방문 처리
    print(v, end=' ')

    for i in graph[v]:  # 그래프를 탐색
        if not vistied[i]:  # 방문처리가 안된 곳을 만나면
            dfs(graph, i, vistied)  # dfs를 재귀적으로 실행


graph = [
    [],  # 주로 노드의 번호가 1번부터 시작하기 때문에 첫번째 인덱스를 비워 0번 노드를 없앰
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

# 각 노드가 방문된 정보를 표현 (1차원 리스트)
visited = [False] * 9

# 정의된 DFS 함수 호출
dfs(graph, 1, visited)
