# 퀸은 같은 행 같은 형 같은 대각선으로 움직인다.

# 기본 가정: 같은 행에는 퀸을 놓지 않는다.
# 유망 함수 구현: 같은 열이나 같은 대각선에 놓는지를 확인
# 파이썬이 너무 느려 통과가 안되므로 pypy로 통과해야함

import sys

input = sys.stdin.readline


def promising(i):
    for k in range(i):
        if row[i] == row[k] or abs(row[i] - row[k]) == i - k:
            return False
    return True


def backtracking(i):
    global result
    if i == N:
        result += 1
        return
    for j in range(N):
        if check[j]:
            continue
        row[i] = j
        if promising(i):
            check[j] = True
            backtracking(i + 1)
            check[j] = False


N = int(input())
row = [0] * N
check = [False] * N
result = 0

backtracking(0)

print(result)
