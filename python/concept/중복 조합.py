def dfs(index, count):
    if count == k: # 증가시킨 count가 뽑을 갯수랑 같으면
        print(*v) # 모든 데이터를 프린트
        return

    for i in range(index, n):
        v.append(data[i]) # 조합을 스택에 넣음
        dfs(i, count + 1)
        v.pop() # dfs 실행이후 마지막 값을 pop하고 for문을 증가시킴


data = [4, 2, 1, 3, 5]
n = 5
k = 3
v = []

index = 0  # 화살표가 우측으로 가야하기 때문에 필요함
count = 0

dfs(index, count)
