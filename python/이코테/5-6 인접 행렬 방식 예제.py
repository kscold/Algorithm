INF = 999999999  # 무한의 비용 선언

# 2차원 리스트를 이용해 인접 행렬 표현
graph = [
    [0, 7, 5],  # weight, left, right , 인덱스 0 이 data
    [7, 0, INF],  # 인덱스 1이 data
    [5, INF, 0]  # 인덱스 2이 data
]
