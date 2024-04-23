def dfs(index, count):
    if count == k:  # 뽑을 갯수랑 조합의 갯수랑 같으면
        for i in range(len(select)):  # 선택한 갯수만큼 반복
            if select[i] == 1:  # 방문했는지 검사
                print(data[i], end=" ")  # 방문한 인덱스의 원소를 출력
        print()
        return

    for i in range(index, n):  # 0 부터 n - 1까지 반복(모든 원소를 대상으로)
        if select[i] == 1:  # 이미 뽑은 원소라면 건너 뜀
            continue

        select[i] = 1  # 방문처리
        dfs(i, count + 1)  # 방문처리한 값은 건너 뛰므로 count + 1만 증가
        select[i] = 0  # 완전탐색을 끝내면 select를 초기화


data = [4, 2, 1, 3, 5]  # 원소 리스트
select = [0] * len(data)  # 원소들의 뽑았는지 유무를 체크하는 리스트

n = 5  # 원소의 종류
k = 3  # 뽑을 조합의 갯수

index = 0  # 뽑는 숫자의 인덱스
count = 0  # 현재까지 뽑은 숫자 갯수

dfs(index, count)
