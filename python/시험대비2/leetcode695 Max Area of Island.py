# 1로 이루어진 섬 중 가장 큰 면적을 반환
class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return 0

        result = 0

        def dfs(i, j):
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == 0:
                # 그리드의 행이 0보다 작거나 길이를 초과하거나 그리드의 열이 0 보다 작거나 길이를 초과하면
                return 0

            grid[i][j] = 0  # 위의 조건에 만족하는 좌표는 방문처리 함
            count = 1  # 카운트를 1로 초기화

            # 카운트에 4방향의 dfs 값을 대입(면적을 구함)
            count += dfs(i + 1, j)
            count += dfs(i - 1, j)
            count += dfs(i, j + 1)
            count += dfs(i, j - 1)

            return count

        for i in range(len(grid)):  # 행
            for j in range(len(grid[0])):  # 열
                if grid[i][j] == 1:  # 섬만 dfs 돌리기
                    current_count = dfs(i, j)
                    result = max(result, current_count)  # result 값에 대입해서 결과적으로 가장 큰 값(최대 값)을 찾음

        return result


grid = [[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
        [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]
solution = Solution()
result = solution.maxAreaOfIsland(grid)
print(result)
