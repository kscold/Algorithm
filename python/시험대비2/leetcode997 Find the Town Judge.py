class Solution(object):
    def findJudge(self, n, trust):
        """
        :type n: int
        :type trust: List[List[int]]
        :rtype: int
        """
        in_degree = [0] * (n + 1)
        out_degree = [0] * (n + 1)

        for x, y in trust:
            out_degree[x] += 1
            in_degree[y] += 1

        for i in range(1, n + 1):
            if in_degree[i] == n - 1 and out_degree[i] == 0:
                return i

        return -1


number = int(input())
n = int(input())
trust = [list(map(int, input().split())) for i in range(number)]
solution = Solution()
result = solution.findJudge(n, trust)
print(result)
