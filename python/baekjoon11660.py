import sys

input = sys.stdin.readline

n, m = map(int, input().split())  # n은 배열 행열 n*n 크기, m은 (x1, y1) (x2, y2) 질의의 크기, 예를 들어 [(x1, y1) (x2, y2)]가 3줄 있으면 m은 3개
A = [[0] * (n + 1)]  # n+1 만큼 0으로 만든 배열, n이 3이라면 [[0, 0, 0, 0]]
D = [[0] * (n + 1) for _ in
     range(n + 1)]  # 합배열을 설정, n+1행과 0요소 갯수 설정, n이 3이라면 0,1,2,3 4개 => [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]] 이차원 배열

for i in range(n):  # range의 시작점이 주어지지 않았으므로 0부터 n-1까지 돌음 지금 n이 3이므로 0, 1, 2까지 3번 돔
    A_row = [0] + [int(x) for x in input().split()]  # 1 2 3 이런식으로 입력했다면 [0, 1, 2, 3] 이런식으로 설정, 즉 인덱스를 1부터 설정함 3번 반복
    A.append(A_row) # [[0, 0, 0, 0]]가 [[0, 0, 0, 0], [0, 1, 2, 3]]가  로 추가 3번 반복 [[0,0,0,0],[0,1,2,3],[0,4,5,6],[0,7,8,9]] 이런형식이 됨

for i in range(1, n + 1):  # 행 1부터 n까지, n이 3이므로 1, 2, 3  3번 돔
    for j in range(1, n + 1):  # 열 1부터 n까지 3번 돔
        D[i][j] = D[i - 1][j] + D[i][j - 1] - D[i - 1][j - 1] + A[i][j] # D[1][1] 부터 D[1][2] 이런식으로 구함 D[3][3]까지 합행렬을 설정 [[0,0,0,0],[0,합1,합2,합3],[0,합1,합2,합3],[0,합1,합2,합3]]

for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    result = D[x2][y2] - D[x1-1][y2] - D[x2][y1-1] + D[x1-1][y1-1] # 합배열로 표현하였지만 D[x1-1][y2] D[x2][y1-1] 이 식들은 원본 배열 A의 한 줄 겹치는 요소 D[x1-1][y1-1]을 두번 빼주었으므로 1개를 다시 더함
    print(result)