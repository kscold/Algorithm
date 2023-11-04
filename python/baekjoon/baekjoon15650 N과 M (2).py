n, m = map(int, input().split())
s = []
visited = [False] * (n + 1)


def dfs(start): # 이 문제의 키 포인트는 일전 15649의 문제에 일전에 계산한 값은 가지치기를 하기 위해 start 파라미터를 받아 처리를 함
    if len(s) == m:
        print(" ".join(map(str, s)))
        return
    for i in range(start, n + 1):
        if visited[i]:
            continue
        visited[i] = True
        s.append(i)
        dfs(i)
        s.pop()
        visited[i] = False


dfs(1)
