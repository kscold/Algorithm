import heapq
import sys

graph = {
    'A': {'B': 10, 'C': 3},
    'B': {'C': 1, 'D': 2},
    'C': {'B': 4, 'D': 8, 'E': 2},
    'D': {'E': 7},
    'E': {'D': 9},
}

def shortest_path(start):
    distances = {node: sys.maxsize for node in graph}  # 초기 거리를 무한대로 설정
    distances[start] = 0  # 시작 노드의 거리는 0으로 설정
    queue = []
    heapq.heappush(queue, (distances[start], start))  # 우선순위 큐에 (거리, 노드) 쌍을 저장하며 시작노드를 큐에 넣음
    # heapq 모듈에 첫 번째 데이터를 기준으로 정렬을 진행하기 때문 (노드, 거리) 순으로 넣으면 최소 힙이 예상한대로 정렬되지 않음

    while queue:  # 우선 순위 큐에 데이터가 하나도 없을 때까지 반복
        current_distance, node = heapq.heappop(queue)  # 가장 낮은 거리를 가진 거리와 노드를 추출
        # 파이썬 heapq에 (거리, 노드) 순으로 넣다 보니까 동일한 노드라도 큐에 저장이 된다 예시: queue[(7, 'B'), (10, 'B')]

        if distances[node] < current_distance: # 저장한 거리와 추출된 거리와 비교하여 저장된 거리가 더 작다면 비교하지 않고 큐의 다음 데이터로 넘어간다.
            continue


        for adjacency_node, distance in graph[node].items():  # 대상인 노드에서 인접한 노드와 거리를 순회 adjacency_node = key, distance = value
            weighted_distance = current_distance + distance # 현재 노드에서 인접한 노드를 지나갈 때까지의 거리를 더함 -> 가중치 거리

            if weighted_distance < distances[adjacency_node]: # 가중치 거리 < 배열의 저장된 거리이면 해당 노드의 거리 변경
                distances[adjacency_node] = weighted_distance # 배열에 저장된 거리보다 가중치가 더 작으므로 변경
                heapq.heappush(queue, (weighted_distance, adjacency_node)) # 다음 인접 거리를 계산 하기 위해 우선 순위 큐에 삽입 (노드가 동일해도 일단 다 저장함)

    return distances


result = shortest_path('A')
print(result)
