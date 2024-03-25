def dfs(list, v, visited):
    visited[v] = True

    for i in list[v]:
        if not visited[i]: # false라면 (not False) == True
            dfs(list, i, visited)


t = int(input())

for i in range(t):
    n = int(input())
    datas = list(map(int, input().split()))

    visited = [False] * (n + 1)

    Alist = [[] for i in range(n + 1)]
    for i, data in enumerate(datas):
        Alist[i + 1].append(data)

    count = 0
    for i in range(1, n + 1):
        if not visited[i]: # global이 아니여도 매개변수로 넘겨주었으므로 결과가 유지
            dfs(Alist, i, visited)
            count += 1
    print(count)
