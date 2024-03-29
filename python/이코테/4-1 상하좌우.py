# 입력
# 5
# R R R U D D

# 출력
# 3 4

n = int(input()) # 이동하는 방향의 갯수를 n에 저장

x, y = 1, 1
plans = input().split()  # 이동하는 방향 문자를 입력 받음

# L, R, U, D에 따른 이동 방향
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

# 'L'인 경우, dx[0]은 0이며, dy[0]은 -1이다. 이는 현재 위치에서 좌측으로 한 칸 이동하는 것을 나타낸다.
# 'R'인 경우, dx[1]은 0이며, dy[1]은 1이다. 이는 현재 위치에서 우측으로 한 칸 이동하는 것을 나타낸다.
# 'U'인 경우, dx[2]은 -1이며, dy[2]은 0이다. 이는 현재 위치에서 위쪽으로 한 칸 이동하는 것을 나타낸다.
# 'D'인 경우, dx[3]은 1이며, dy[3]은 0이다. 이는 현재 위치에서 아래쪽으로 한 칸 이동하는 것을 나타낸다.

# 이동 계획을 하나씩 확인
for plan in plans:
    # 이동 후 좌표 구하기
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]

    # 공간을 벗어나는 경우 무시
    if nx < 1 or ny < 1 or nx > n or ny > n: # 이동을 해야하므로 n보다는 nx와 ny가 작아야한다.
        continue
    # 이동 수헹
    x, y = nx, ny

print(x, y)
