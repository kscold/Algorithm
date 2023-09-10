import sys

N, M, K = map(int,sys.stdin.readline().split()) # N M K 입력 예시) 5 8 3 # N은 배열 크기, M은 더할 홧수, K은 큰 수 반복 횟수

data = [0] * N # 배열로 선언 초기화

data = list(map(int, sys.stdin.readline().split())) # 공백으로 배열 입력 [] 예시) 2 4 5 4 6

data.sort() # 오름차순으로 데이터를 정렬
first = data[N - 1]
second = data[N - 2]

result = 0

while True:
    for i in range(K): # 0부터 K-1까지 K번 반복
        if M == 0: # 더할 횟수가 0이면 break
            break
        result = result + first
        M = M - 1

    if M == 0:
        break
    result = result + second
    M = M - 1

print(result)


