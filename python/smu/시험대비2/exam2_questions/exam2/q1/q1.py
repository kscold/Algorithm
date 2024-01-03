import time


def q1(coinmap):
    # your code is here
    # ----------------------------------------------

    R = len(coinmap)
    C = len(coinmap[0])
    cnt = 0
    visited = [[0] * C for _ in range(R)]
    visited[0][0] = 1

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    def isValid(x, y):  # 맵 영역을 벗어나는지 체크
        return (x >= 0 and x < R and y >= 0 and y < C)

    def dfs(x, y):  # 코인맵과 좌표, 초기 카운트를 대입
        # nonlocal result
        if (isValid(x, y) == False or coinmap[x][y] == 'X'):  # 맵에 벗어나면 0 반환
            return 0

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]  # 4방향 이동

            if coinmap[nx-1][ny-1] == 'O':
                if visited[nx][ny] == 0 or visited[nx][ny] > visited[x][y] + 1:
                    visited[nx][ny] = visited[x][y] + 1
                    if nx == n - 1 and ny == m - 1:
                        return
                    dfs(nx, ny)

    dfs(0, 0)
    return visited[n - 1][m - 1]


# ----------------------------------------------


def compare_output(file1, file2):
    f1 = open(file1, "r")
    f2 = open(file2, "r")

    lines1 = f1.readlines()
    lines2 = f2.readlines()

    success = True
    i = 0
    for _ in lines2:
        if lines1[i].strip() != lines2[i].strip():
            print("[%i] Wrong answer: Yours=\'%s\', Expected=\'%s\'\n" % (i + 1, lines1[i].strip(), lines2[i].strip()))
            success = False
            break
        i = i + 1

    if success:
        print("Success!")
    f1.close()
    f2.close()


# main code
input = open("input.txt", "r")  # input data
output = open("output.txt", "w")  # your answer

start_time = time.time()
line = input.readline().split()
K = int(line[0])
for _ in range(K):
    line = input.readline().split()
    n = int(line[0])
    m = int(line[1])
    coinmap = []
    for y in range(n):
        row = list(input.readline().strip())
        coinmap.append(row)
    result = q1(coinmap)
    print(result)
    output.write('{}\n'.format(result))

end_time = time.time()
## -----------------------------------------------

# DO NOT EDIT. Checking answers
input.close()
output.close()
compare_output("output.txt", "expected.txt")
print('Elapsed time: {:.2f} seconds. '.format(end_time - start_time), end='')
