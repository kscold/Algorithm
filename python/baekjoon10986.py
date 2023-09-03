import sys

input = sys.stdin.readline
n, m = map(int, input().split())  # n 배열의 갯수 n을 입력, 배열을 나룰 수 m을 설정
A = list(map(int, input().split()))  # n개의 원본 배열을 공백을 기준으로 입력받음
S = [0] * n  # n번만큼 리스트의 원소를 0으로 설정, 합배열로 만드는 순간 0 또는 1밖에 안나옴
C = [0] * m  # m번만큼 리스트의 원소를 0으로 설정, 나머지가 0인지 아닌지 결과를 저장하는 배열 C
answer = 0 # 나머지가 0으로 떨어질 때 증가시킬 카운트를 설정

S[0] = A[0]  # 매우 중요! 합배열과 원본배열의 첫번째 인덱스 A[0]를 기준으로 문제에서 A[0]은 1 S[0] 1로 설정 맞춰줌
for i in range(1, n):  # i는 1부터 n-1번째까지 반복
    S[i] = S[i - 1] + A[i]  # 합 배열 저장

for i in range(n):
    remainder = S[i] % m # 나머지 m으로 합배열을 나눔
    if remainder == 0: # 나머지가 0 이면
        answer += 1 # 정답 카운트를 증가
    C[remainder] += 1 # m개의 나머지 배열 즉 m=3일때는 [나머지 0,나머지 1,나머지 2]의 갯수를 카운트

for i in range(m):
    if C[i] > 1:
        answer += (C[i] * (C[i] - 1) // 2) # Conbination의 공식

print(answer)