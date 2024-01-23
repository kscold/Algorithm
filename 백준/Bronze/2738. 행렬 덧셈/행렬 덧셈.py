n, m = map(int, input().split())

A = []
B = []
sum = [[0] * m for i in range(n)]

for i in range(n):
    A.append(list(map(int, input().split())))

for i in range(n):
    B.append(list(map(int, input().split())))

for i in range(n):
    for j in range(m):
        sum[i][j] = A[i][j] + B[i][j]


for i in sum:
    print(*i)