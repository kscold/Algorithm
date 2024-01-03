import sys
from collections import deque

input = sys.stdin.readline

N, L = map(int, input().split()) # 요소의 총 개수 N, 슬라이드 윈도우 L 설정
mydeque = deque() # 데큐 선언 후 mydeque에 넣음
now = list(map(int, input().split())) # 탐색할 N개의 요소를 설정

for i in range(N): # 0부터 N-1까지 즉, N 만큼 반복, i가 인덱스가 됨
    # 아이디어1 나보다 큰 데이터 삭제
    while mydeque and mydeque[-1][0] > now[i]: # 데큐가 존재하고 mydeque[-1][0](데큐의 마지막 요소의 첫번째 값)이 now[i](현재 인덱스 값)보다 작으면 브레이크
        # 따라서 mydeque[-1]는 항상 마지막 요소를 가르키고  [(1(인덱스), 3(값)), (인덱스 생략)6(실제 값),  8]이면 (3, 8)을 가르키고 mydeque[-1][0]은 3을 가리킴 첫번째 값은 걸리지 않음
        mydeque.pop()
    # 슬라이딩 윈도우 벗어난 데이터를 삭제 2번째 아이디어
    mydeque.append((now[i], i)) # (현재 값, 햔재 인덱스)의 튜플 형식으로 오른쪽 큐에 추가
    if mydeque[0][1] <= i - L: # mydeque[0][1](가장 오래전에 추가 된 요소의 인덱스 제일 왼쪽 큐) 첫번째 요소의 두번째 값(즉, 현재 인덱스)이 윈도우 범위를 벗어나면(현재 인덱스와 윈도우 크기를 뺀 값이 햔재 인덱스 보다 작으면)
        mydeque.popleft() # 윈쪽 큐부터 삭제 1==1, 2==2, 3==3 이런식으로 만족하여 삭제됨 즉 인덱스 삭제
    print(mydeque[0][0], end=' ') # 공백으로 구분하여 출력
