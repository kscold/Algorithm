N = int(input())  # 사람 수
A = list(map(int, input().split()))  # 자릿수 별로 구분해 저장한 리스트
S = [0] * N  # [0,0,0] N이 3일 때

# 삽입정렬

for i in range(1, N):  # 1부터 N-1까지 반복, 삽입정렬은 1부터 index로 선택할 수 있기 떄문
    insert_point = i  # 정렬대상 인덱스 초기화
    insert_value = A[i]  # 정렬대상 값 초기화
    for j in range(i - 1, -1, -1):  # i가 1부터 시작하므로 왼쪽으로 탐색 삽일할 위치를 탐색
        if A[j] < A[i]:  # 정렬대상 값(A[i])보다 왼쪽에 있는 값보다 크면
            insert_point = j + 1  # 삽일할 위치를 들어갈 자리보다 한칸 오른쪽에 설정
            break
        if j == 0:  # 예외처리를 해야됨 j가 0까지 갔을 때(왜냐하면 거기까지 갈 필요가 없기 때문에)
            insert_point = 0

    for j in range(i, insert_point, -1):
        A[j] = A[j - 1]  # 삽입할 위치를 만들어야되기 때문에 삽입할 위치로부터 하나씩 왼쪽에서 오른쪽으로 배열을 땡김

    A[insert_point] = insert_value

# 합배열 선언
S[0] = A[0]  # 합배열과 원본배열의 첫번째 요소는 항상 같음

for i in range(1, N):
    S[i] = S[i - 1] + A[i]

sum = 0 # 합배열을 모두 더할 변수를 선언
for i in range(0, N):
    sum += S[i]

print(sum)
