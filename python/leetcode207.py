import sys


def dfs(graph, vistited, i):
    if vistited[i] == 1:  #
        return True
    elif vistited[i] == - 1:
        return False

    vistited[i] = -1

    for j in graph:
        if not dfs(graph, vistited, j):
            return False

    vistited[i] = 1
    return True


n = int(sys.stdin.readline())

p = []

vistied = [0] * n

for i in range(n):
    p.append(list(map(int, sys.stdin.readline().rstrip())))

for i in range(n):
    if not dfs(p, vistied, i):  # 사이클생성
        return False
