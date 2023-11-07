# 예시 1:

# 입력: numCourses = 2, prerequisites = [[1,0]]
#  출력: true
#  설명: 총 2개 과정을 수강해야 합니다.
# 1과정을 수강하려면 0과정을 이수해야 하므로 가능합니다.

# 예 2:

# 입력: numCourses = 2, prerequisites = [[1,0],[0,1]]
#  출력: false
#  설명: 총 2개 과정을 수강해야 합니다.
# 1과목을 수강하려면 0과목을 이수해야 하고, 0과목을 수강하려면 1과목도 이수해야 하기 때문에 불가능합니다.
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """

        # 인접 리스트로 바꿈
        graph = {}
        for course, prereq in prerequisites:  # course는 1, prereq는 0으로 언패킹
            if course not in graph:  # 인접 리스트안에 course가 없으면
                graph[course] = []  # {course(1): 값들} 인접리스트를 생성
            if prereq not in graph:  # prereq도 똑같음
                graph[prereq] = []
            graph[course].append(prereq)  # 그래프에 course에 대한 값이 있다면, prereq에 대한 값만 추가

        visited = [0] * (numCourses)  # 방문 테이블을 과목 수만큼 초기화

        def dfs(course):
            if visited[course] == -1:  # 일전에 방문 중인 코스가 -1 이면 사이클이 있다는 것임으로 True 반환
                return True

            visited[course] = -1  # 방문 중임을 표시

            if course in graph:  # 그래프 안에 course가 있으면
                for prereq in graph[course]:  # 그래프 코스의 key에 대한 value를 순회
                    if visited[prereq] == -1 or (visited[prereq] == 0 and dfs(
                            prereq)):  # 전제조건을 방문했거나 아직 방문하지 않았으면서 전제조건을 dfs 돌 숭 있으면, 사이클이 존재하면 True
                        return True

            visited[course] = 1  # 방문함을 표시
            return False  # 사이클이 존재하지 않으면 False를 표현

        for course in range(numCourses):  # 방문테이블을 순회
            if visited[course] == 0:  # 방문테이블이 0이면
                if dfs(course):  # dfs가 true이면, 사이클이 존재하면, False를 반환
                    return False

        return True  # 사이클이 존재하지 않으면 True를 반환


n = int(input())  # 반복 횟수
numCourses = int(input())
prerequisites = [list(map(int, input().split())) for i in range(n)]
solution = Solution()
result = solution.canFinish(numCourses, prerequisites)
print(result)
