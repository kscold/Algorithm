import random

testcase = int(input()) # 테스트 케이스의 수를 저장
answer = 0
A = [0]*(100001) # 배열 크기를 100001인 리스트 A를 생성하고 모든 원소를 0으로 초기화

for i in range(0, 100001): # 범위를 잘못지정할 수 있기 때문에
    A[i] = random.randrange(1, 101) # 각 배열에 1부터 101사이의 랜덤한 정수 값을 할당

for t in range(1, testcase+1):
    start, end = map(int, input().split())  # 시작과 끝 인덱스를 입력받아 해당 범위 내의 배열 원소들을 모두 합산

    for i in range(start, end +1):
        answer = answer + A[i]

    print(str(testcase) + " " +str(answer/2))