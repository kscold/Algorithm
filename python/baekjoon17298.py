import sys

n = int(sys.stdin.readline()) # 수열 갯수 입력
ans = [0] * n # 정답 리스트 초기화
A = list(map(int, sys.stdin.readline().split())) # 수열 리스트 채우기
myStack = [] # 스택을 선언

for i in range(n): # 수열 갯수만큼 반복 인덱스 i에 저장(0부터 n+1까지)
    while myStack and A[myStack[-1]] < A[i]: # 스텍이 존재하고 수열 리스트 스택의 top[-1]이 이번에 들어온 A[i] 보다 크면 브레이크(오큰수가 들어오기 전까지 반복)
        ans[myStack.pop()] = A[i] # 스택에서 pop한 값을 index으로 하는 정답 리스트 부분(즉, myStack.pop()은 마지막 요소 myStack[-1]을 반환하고 삭제)을 수열 리스트의 현재 값(A[i])으로 저장 정답 리스트에 오큰 수 저장
    myStack.append(i) # 오큰수가 들어오면 스택에 추가(위의 조건에 만족하지 않으면)

while myStack: # 스택이 존재하면(즉, 스택이 존재하지 않으면 브레이크)
    ans[myStack.pop()] = -1 # 정답 리스트의 마지막 인덱스(top, 즉 마지막 인덱스)를 -1로 설정

print(' '.join(map(str, ans)))