import heapq


class Solution(object):
    def swimInWater(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        visited = [[False] * len(grid) for _ in range(len(grid))]
        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]
        n = len(grid)
        res = 0

        q = []
        heapq.heappush(q, (grid[0][0], 0, 0))

        while q:
            time, x, y = heapq.heappop(q)
            visited[x][y] = True
            res = max(res, time)

            if x == n - 1 and y == n - 1:
                return res

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if nx < 0 or ny < 0 or nx >= n or ny >= n or visited[nx][ny]:
                    continue

                heapq.heappush(q, (grid[nx][ny], nx, ny))


grid = [[0, 2], [1, 3]]
solution = Solution()
result = solution.swimInWater(grid)
print(result)
