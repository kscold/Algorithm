import sys

input = sys.stdin.readline

n, m = map(int, input().split()) # n은 배열 행열 n*n 크기
A = [[0] * (n + 1)]  # n+1 만큼 0으로 만든 배열 n이 3이라면 [[0, 0, 0, 0]]
D = [[0]*(n+1) for _ in range(n+1)] # n+1행과 0요소 갯수 설정, n이 3이라면 [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]] 이차원 배열

for i in range(n): # range의 시작점이 주어지지 않았으므로 0부터 n-1까지 돌음
    A_row = [0] + [int(x) for x in input().split()]
    A.append(A_row)

for i in range(1, n+1):
    for j in range(1, n+1):