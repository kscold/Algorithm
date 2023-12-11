import sys

input = sys.stdin.readline

n, m = list(map(int, input().split()))
board = [list(map(int, input().split())) for _ in range(n)]

def solve(x, y, c):
    flag = False
    for i in range(x, n):
        for j in range(y, m):
            if board[i][j] == 1:
                board[i][j] = 0
                c = c + 1 + solve(i, j, c)
                flag = True
            if flag:
                break
        if flag:
            break
    return c


v = 1
for i in range(n + 2):
    if v == 0:
        print(i - 1)
        break
    v = solve(i, 0, 0)
