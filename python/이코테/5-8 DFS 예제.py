# DFS 메서드 정의
def dfs(graph, v, visited):
    # 현재 노드를 방문 처리
    visited[v] = True
    print(v, end=' ')
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:  # 핵심 코드로 연결된 노드를 방문
        if not visited[i]:
            dfs(graph, i, visited)


# 각 노드가 연결된 정보를 인접 리스트 자료형으로 표현(2차원 리스트)
graph = [
    [],  # 인덱스를 1부터 시작하기 때문에 0은 무시
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]
# 각 노드가 방문된 정보를 리스트 자료형으로 표현(1차원 리스트)
visited = [False] * 9  # 0번째 인덱스까지 생각해서 9개 방문 리스트를 생성

# 정의된 DFS 함수 호출
dfs(graph, 1, visited)  # 첫번째 노드 인접 리스트 데이터에 접근
