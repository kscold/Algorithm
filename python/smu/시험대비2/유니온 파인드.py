class Solution:
    def find_parent(self, parent, i):
        if parent[i] == -1:
            return i
        if parent[i] != -1:
            return self.find_parent(parent, parent[i])

    def union(self, parent, x, y):
        x_set = self.find_parent(parent, x)
        y_set = self.find_parent(parent, y)
        parent[x_set] = y_set

    def isCyclic(self, edges):
        V = max(max(edges, key=lambda x: max(x))) + 1  # 정점의 개수 계산
        parent = [-1] * V

        for x, y in edges:
            x_set = self.find_parent(parent, x)
            y_set = self.find_parent(parent, y)

            if x_set == y_set:
                return True  # 사이클이 존재함

            self.union(parent, x, y)

        return False  # 사이클이 존재하지 않음

edges = [(0, 1), (0, 2), (1, 2)]
solution = Solution()
result = solution.isCyclic(edges)
print(result)  # 출력: True (사이클 존재)
