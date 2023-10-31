class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        # prerequisites를 그래프로 변환
        graph = {}
        for course, prereq in prerequisites:
            if course not in graph:
                graph[course] = []
            if prereq not in graph:
                graph[prereq] = []
            graph[course].append(prereq)

        # 방문 상태를 나타내는 visited 배열
        visited = [0] * (numCourses)

        # 사이클 검사를 위한 DFS 함수
        def dfs(course):
            # 이미 방문한 과목이면 사이클이 존재
            if visited[course] == -1:
                return True

            # 이번 DFS 탐색에서 방문한 과목을 -1로 표시, 방문 확인
            visited[course] = -1

            # 이웃한 과목들을 재귀적으로 탐색
            if course in graph:
                for prereq in graph[course]:
                    if visited[prereq] == -1 or (visited[prereq] == 0 and dfs(prereq)):
                        return True

            # 탐색이 끝났으면 해당 과목을 1로 표시
            visited[course] = 1
            return False

        # 모든 과목에 대해 위상 정렬 및 사이클 검사
        for course in range(numCourses):
            if visited[course] == 0: # 처음 방문하는 것으로 처리(탐색 시작)
                if dfs(course): # dfs가 True면(사이클이 존재하면)
                    return False # False를 반환

        # 모든 과목을 수강할 수 있으면 True 반환(dfs가 False이면)
        return True

solution = Solution()

print(solution.canFinish(2, [[1,0],[0,1]]))