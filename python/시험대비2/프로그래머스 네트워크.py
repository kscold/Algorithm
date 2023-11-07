# 인접 행렬로 이루어진 dfs 덩어리를 전부 세는 문제
def solution(n, computers):
    def dfs(v):
        visited[v] = True

        for i in range(n):
            if not visited[i] and computers[v][i]:
                dfs(i)

    count = 0
    visited = [False] * (n)

    for node_idx in range(n):
        if not visited[node_idx]:
            dfs(node_idx)
            count += 1

    return count

n = int(input())
computers = [list(map(int, input().split())) for i in range(n)]
result = solution(n, computers)

print(result)