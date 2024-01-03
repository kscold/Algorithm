# numbers 리스트가 주어지면 더하기 빼기를 하여 target을 만드는 방법의 수를 카운팅
# DFS를 이용한 풀이
def solution(numbers, target):
    answer = 0
    n = len(numbers)

    def dfs(idx, result):
        if n == idx:
            if result == target:
                nonlocal answer
                answer += 1
        else:
            dfs(idx + 1, result + numbers[idx])
            dfs(idx + 1, result - numbers[idx])

    dfs(0, 0)

    return answer


# BFS를 이용한 풀이
from collections import deque


def solution(numbers, target):
    answer = 0
    queue = deque()
    n = len(numbers)
    queue.append([numbers[0], 0])  # 큐에 numbers의 값이랑, idx를 같이 저장
    queue.append([-1 * numbers[0], 0])  # 마이너스 연산을 하기 위한 저장
    while queue:
        temp, idx = queue.popleft()
        idx += 1
        if idx < n:  # n이 idx 길이보다 작을 때 반복
            queue.append([temp + numbers[idx], idx])
            queue.append([temp - numbers[idx], idx])
        else:
            if temp == target:
                answer += 1
    return answer


target = int(input())
numbers = list(map(int, input().split()))
result = solution(numbers, target)
print(result)
