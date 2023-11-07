from collections import deque


# BFS 메서드 정의
def bfs(graph, start, visited):
    queue = deque([start])  # 큐(Queue) 구현을 위해 deque 라이브러리 사용
    visited[start] = True  # 현재 노드를 방문 처리

    while queue:  # 큐가 빌 때까지 반복
        v = queue.popleft()  # 큐에서 하나의 원소를 뽑아 출력하기
        print(v, end=' ')
        for i in graph[v]:  # 아직 방문하지 않은 인접한 원소들을 큐에 삽입
            if not visited[i]:  # 방문하지 않은 노드만 큐에 추가
                queue.append(i)
                visited[i] = True


# 에지리스트에서 BFS를 돌리는 방법
graph = [
    [],  # 주로 노드의 번호가 1번부터 시작하기 때문에 첫 번째 인덱스를 비워 0번 노드를 없앰
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

# 각 노드가 방문된 정보를 표현
visited = [False] * 9

# 정의된 BFS 함수 호출
bfs(graph, 1, visited)
