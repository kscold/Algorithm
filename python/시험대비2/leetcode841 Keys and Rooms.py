# 진입차수와 진출차수를 이용한 풀이
class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        visited = [False] * len(rooms)  # 방문 테이블을 초기화

        def dfs(n):
            if visited[n]:  # n번째를 방문했다면 return
                return

            visited[n] = True  # n번째를 방문처리

            for room in rooms[n]:  # n번째 리스트를 언패킹
                if visited[room]:  # 언패킹 한 room이 방문처리 되어있으면 continue
                    continue
                dfs(room)

        dfs(0)  # dfs를 0부터 차례대로 순회

        if False in visited:  # 방문 테이블에 하나라도 False가 있으면 False를 반환
            return False

        return True  # 아니면 True를 반환


from collections import deque

# bfs를 이용한 풀이
class Solution:
    def canVisitAllRooms(self, rooms):
        N = len(rooms)
        is_visited = [False] * N
        is_visited[0] = True  # 0번 방은 곧 들릴 예정
        visited_left = N - 1  # 0번 방 제외 다른 방들은 들리지 않음
        q = deque([0])  # 0번 방을 가장 처음으로 들릴 queue 제작

        # 들릴 방이 남아 있을 때까지 반복, 이미 모든 방 방문했으면 break
        while len(q) and visited_left:
            now = q.popleft()
            # 현재 방에서 들릴 수 있는 다음 방들에 대해 is_visited 체크
            for key in rooms[now]:
                if not is_visited[key]:
                    is_visited[key] = True
                    visited_left -= 1
                    q.append(key)

        return False if visited_left else True

rooms = [[1, 3], [3, 0, 1], [2], [0]]
solution = Solution()
result = solution.canVisitAllRooms(rooms)
print(result)
