import sys


def solution(A, n, m):
    left, right = 0, 0 
    answer = 2000000000
    while right < n:
        diff = A[right] - A[left]
        if diff < m:  
            right += 1
        elif diff > m:
            answer = min(diff, answer) 
            left += 1 
        else: 
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