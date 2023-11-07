# 사이클이 있는 무방향그래프에서 어떤 두 노드의 간선을 자르면 트리가 되는지
class Solution(object):
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        sets = [0] * (len(edges) + 1)

        def find(x):
            if sets[x] == 0:
                return x
            return find(sets[x])

        for x, y in edges:
            u = find(x)
            v = find(y)
            if u == v: # u와 v가 같은 값이라면, 이미 같은 집합에 속해 있고 이 간선을 추가할 경우 사이클이 형성
                return [x, y] # 따라서 [x, y]이 불필요한 연결이므로 반환
            sets[u] = v # 두 노드가 다른 집합에 속해 있을 경우, 이 코드를 통해 u가 속한 집합을 v와 합침 이렇게 하면 u가 속한 모든 노드는 이제 v가 속한 집합에 포함


edges = [[1, 2], [1, 3], [2, 3]]
solution = Solution()
result = solution.findRedundantConnection(edges)
print(result)
