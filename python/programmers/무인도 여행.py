# from collections import deque
#
#
# def solution(maps):
#     answer = []
#     graph = []
#     for row in maps:
#         row = row.replace("X", "0")
#         graph.append(list(map(int, row)))
#
#     def bfs(y, x):
#         dx = [0, 0, -1, 1]
#         dy = [-1, 1, 0, 0]
#
#         queue = deque([(y, x)])
#         visited.add((y, x))
#         total_food = graph[y][x]
#
#         while queue:
#             cy, cx = queue.popleft()
#
#             for i in range(4):
#                 nx = cx + dx[i]
#                 ny = cy + dy[i]
#
#                 if 0 <= nx < len(graph[0]) and 0 <= ny < len(graph):
#                     if (ny, nx) not in visited and graph[ny][nx] != 0:
#                         visited.add((ny, nx))
#                         queue.append((ny, nx))
#                         total_food += graph[ny][nx]
#
#         return total_food
#
#     visited = set()
#     for y in range(len(graph)):
#         for x in range(len(graph[0])):
#             if graph[y][x] != 0 and (y, x) not in visited:
#                 island_food = bfs(y, x)
#                 answer.append(island_food)
#
#     if not answer:
#         return [-1]
#
#     answer.sort()
#     return answer
#
#
# print(solution(["X591X", "X1X5X", "X231X", "1XXX1"]))
# print(solution(["XXX", "XXX", "XXX"]))

def solution(array):
    array.sort()
    answer = len(array) // 2 + 1
    return answer
print(solution([9, -1, 0]))