class Solution(object):
    def validPath(self, n, edges, source, destination):
        graph = {}

        for edge in edges:
            u, v = edge
            if u not in graph:
                graph[u] = []
            if v not in graph:
                graph[v] = []

            graph[u].append(v)
            graph[v].append(u)

        visited = [False] * (n + 1)

        def dfs(node):
            visited[node] = True

            if node == destination:
                return True

            for neighbor in graph.get(node, []):
                if not visited[neighbor]:
                    if dfs(neighbor):
                        return True

            return False

        return dfs(source)

# n = 3
# edges = [[0,1],[1,2],[2,0]]
# source = 0
# destination = 2

n = 6
edges = [[0,1],[0,2],[3,5],[5,4],[4,3]]
source = 0
destination = 5

solution = Solution()
result = solution.validPath(n, edges, source, destination)
print(result)