V, E = map(int, input().split()) # 정점의 갯수와 간선의 갯수를 입력받음

edge = list(map(int, input().split())) # 간선의 정보를 입력받음

adj = [[] * (V + 1) for _ in range(V + 1)] # 첫번쨰 인덱스 0을 무시하기 위해 정점 + 1 x 정점 + 1 갯수만큼 이차원 리스트를 초기화

for i in range(E):
    n1 = edge[i * 2] # 첫번째 인덱스 0를 건너뛰고 받기 위해서 edge[0] edge[2] edge[4] edge[6] edge[8]
    n2 = edge[i * 2 + 1] # 첫번째 인덱스 0를 건너뛰고 두번째 인덱스를 받기 위해서 edge[1] edge[3] edge[5] edge[7]
    adj[n1].append(n2) # adk[edge[0]].append(edge[1]) 예시) 1 2 1 3 2 4 3 5 4 6 일때 두번쨰 리스트(1)에 2값을 넣음.
    adj[n2].append(n1)

print(adj)



