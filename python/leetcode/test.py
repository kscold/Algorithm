class Solution(object):
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        set_edges = set(edges)
        v = list(set_edges).sort

        visited = [0] * (len(v) + 1)

        def dfs(i, v):
            if i in v:
                visited[i] = i
            else:
                visited[i] = -1

            node = i

            if not node in visited:
                dfs(node, v)
            elif node in visited:
                return -1

            return

        result =

        for i in range(1, len(v + 1):
            if
        visited[i] = > 0:
        if dfs(i, v):
            result =




