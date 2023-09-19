# 위상 정렬 사용 -> 사이클이 없는 코드에서만 작동
from collections import deque

# 그래프 정의
v = 7  # 노드의 개수
graph = [[] for _ in range(v + 1)]  # 그래프 초기화

# 간선 정보 입력
edges = [(1, 2), (1, 3), (2, 4), (3, 5), (4, 6), (5, 7), (6, 5)]

# 그래프 구성
for a, b in edges:
    graph[a].append(b)

# 진입 차수 리스트 초기화
indegree = [0] * (v + 1)

# 진입 차수 계산
for i in range(1, v + 1):
    for node in graph[i]:
        indegree[node] += 1

def topology_sort():
    result = [] # 알고리즘 수행 결과를 담을 리스트
    q = deque() # 큐 기능을 위한 deque 라이브러리 사용
    for i in range(1, v+1): # 처음 시작할 때는 진입차수가 0인 노드를 큐에 삽입
        if indegree[i] == 0:
            q.append(i) # 큐가 빌 때까지 반복
    while q:
        now = q.popleft() # 큐에서 원소 꺼내기
        result.append(now) # 해당 원소와 연결된 노드들의 진입차수에서 1빼기
        for i in graph[now]:
            indegree[i] -= 1 # 새롭게 진입차수가 0이 되는 노드를 큐에 삽입
            if indegree[i] == 0:
                q.append(i) # 위상 정렬을 수행한 결과 출력

    for i in result:
        print(i, end=" ")

topology_sort()