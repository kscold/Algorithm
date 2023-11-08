# 이 문제의 경우 중복을 허용하기 때문에 visited로 방문처리할 필요가 없음
n, m = map(int, input().split())
s = []


def dfs(start):
    if len(s) == m:
        print(" ".join(map(str, s)))
        return

    for i in range(start, n + 1):
        s.append(i)
        dfs(i)
        s.pop()


dfs(1)
