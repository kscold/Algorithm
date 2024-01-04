# N개의 정수로 이루어진 수열 A[1], A[2], …, A[N]이 있다. 이 수열에서 두 수를 골랐을 때(같은 수일 수도 있다), 그 차이가 M 이상이면서 제일 작은 경우를 구하는 프로그램을 작성하시오.

# 예를 들어 수열이 {1, 2, 3, 4, 5}라고 하자. 만약 M = 3일 경우, 1 4, 1 5, 2 5를 골랐을 때 그 차이가 M 이상이 된다. 이 중에서 차이가 가장 작은 경우는 1 4나 2 5를 골랐을 때의 3이 된다.

# 입력
# 첫째 줄에 두 정수 N, M이 주어진다. 다음 N개의 줄에는 차례로 A[1], A[2], …, A[N]이 주어진다.

# 출력
# 첫째 줄에 M 이상이면서 가장 작은 차이를 출력한다. 항상 차이가 M이상인 두 수를 고를 수 있다.

# 제한
# 1 ≤ N ≤ 100,000
# 0 ≤ M ≤ 2,000,000,000
# 0 ≤ |A[i]| ≤ 1,000,000,000

# 내 풀이 정답은 맞으니 백준 시간 초과 오류가 난다. 2중 for 문을 돌아 시간 복잡도가 높아져서 그런 것 같음
# import sys
#
# input = sys.stdin.readline
#
# n, m = map(int, input().split())
#
# A = []
# for _ in range(n):
#     A.append(int(input()))
#
# A.sort()
# B = A[1:]
#
# min_value = 2000000000
# pre = []
# for i in A:
#     for j in B:
#         if j - i >= m:
#             min_value = min(j - i, min_value)
# print(min_value)

# 최솟값을 사용하는 풀이
import sys


def solution(A, n, m):
    left, right = 0, 0  # 원래 수, 다음 수 인덱스 초기화
    answer = 2000000000
    while right < n:
        diff = A[right] - A[left]  # A 배열의 다음 수에서 원래 수 차이 계산
        if diff < m:  # 목표차이 m보다 작으면
            right += 1  # 다음 수 인덱스 증가
        elif diff > m: # 목표차이 m보다 크면
            answer = min(diff, answer) # 최솟값 갱신
            left += 1 # 원래 수 인덱스 증가
        else: # 만족하지 못해도 무조건 m 이상 차이는 있으므로 m를 반환
            return m
    return answer


input = sys.stdin.readline

n, m = map(int, input().split())

A = []
for _ in range(n):
    A.append(int(input()))

A.sort()

answer = solution(A, n, m)
print(answer)
