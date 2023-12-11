import sys

input = sys.stdin.readline

n, m = list(map(int, input().split()))  # 행 열 입력
board = [list(map(int, input().split())) for _ in range(n)]


def solve(x, y, c):
    flag = False
    for i in range(x, n):
        for j in range(y, m):
            if board[i][j] == 1:
                board[i][j] = 0
                c = c + 1 + solve(i, j, c)  # 1인 것을 몇개를 검출 했는지 카운트
                flag = True
            if flag:
                break
        if flag:
            break
    return c


v = 1
for i in range(n + 2):
    if v == 0:  # v가 0 일때
        print(i - 1)  # 몇번째에서 검출되었는지 이때 전부 0인 경우 1을 빼주어야됨
        break
    v = solve(i, 0, 0)  # 다 검출했으면 0을 반환할 것임
