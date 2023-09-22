V, E = map(int, input().split())  # 정점의 개수와 간선의 갯수를 입력받음
edge = list(map(int, input().split()))  # 간선의 정보를 입력받음
adj = [[0] * (V + 1) for _ in range(V + 1)]  # 첫번째 인덱스 0를 1부터 받기 위해서 V x V가 아니라 V + 1 x v + 1 을 행렬을 초기화

for i in range(E):  # 간선의 갯수 만큼 반복
    n1 = edge[i * 2]  # 첫번째 인덱스 0를 건너뛰고 받기 위해서 edge[0] edge[2] edge[4] edge[6] edge[8]
    n2 = edge[i * 2 + 1]  # 첫번째 인덱스 0를 건너뛰고 두번째 인덱스를 받기 위해서 edge[1] edge[3] edge[5] edge[7]
    adj[n1][n2] = 1  # 위에서 받은 정보를 토대로 값이 있는 위치에 1로 표기
    adj[n2][n1] = 1  # 무향 그래프인 경우 대칭

print(adj)  # 이 위치로 이동하여 한 번만 출력되도록 수정
