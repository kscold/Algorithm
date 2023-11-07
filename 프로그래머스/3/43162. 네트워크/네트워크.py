def solution(n, computers):
    def dfs(v):
        visited[v] = True
        
        for i in range(n):
            if not visited[i] and computers[v][i]:
                dfs(i)
                
    count = 0
    visited = [False] *(n)
    
    for node_idx in range(n):
        if not visited[node_idx]:
            dfs(node_idx)
            count += 1
    
    return count