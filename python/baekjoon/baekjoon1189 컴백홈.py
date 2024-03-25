# 한수는 캠프를 마치고 집에 돌아가려 한다. 한수는 현재 왼쪽 아래점에 있고 집은 오른쪽 위에 있다.
# 그리고 한수는 집에 돌아가는 방법이 다양하다. 단, 한수는 똑똑하여 한번 지나친 곳을 다시 방문하지는 않는다.

#       cdef  ...f  ..ef  ..gh  cdeh  cdej  ...f
#       bT..  .T.e  .Td.  .Tfe  bTfg  bTfi  .Tde
#       a...  abcd  abc.  abcd  a...  a.gh  abc.
# 거리 :  6     6     6     8     8    10    6
# 위 예제는 한수가 집에 돌아갈 수 있는 모든 경우를 나타낸 것이다.
# T로 표시된 부분은 가지 못하는 부분이다.
# 문제는 R x C 맵에 못가는 부분이 주어지고 거리 K가 주어지면 한수가 집까지도 도착하는 경우 중 거리가 K인 가짓수를 구하는 것이다.

# 입력
# 첫 줄에 정수 R(1 ≤ R ≤ 5), C(1 ≤ C ≤ 5), K(1 ≤ K ≤ R×C)가 공백으로 구분되어 주어진다.
# 두 번째부터 R+1번째 줄까지는 R×C 맵의 정보를 나타내는 '.'과 'T'로 구성된 길이가 C인 문자열이 주어진다.

# 출력
# 첫 줄에 거리가 K인 가짓수를 출력한다.

# 예제 입력 1
# 3 4 6
# ....
# .T..
# ....
# 예제 출력 1
# 4


R, C, K = list(map(int, input().split()))

data = [list(map(str, input())) for _ in range(R)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
#   하   상   우   좌

count = 0  # 가짓수를 카운트 하는 변수


def dfs(x, y, distance):
    global count

    if distance == K and y == C - 1 and x == 0:  # 목표하는 거리와 같고 집의 위치 data[0][C - 1]와 같으면
        count += 1
    else:
        data[x][y] = 'T'  # T로 방문처리
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < R and 0 <= ny < C and data[nx][ny] == ".":  # 방문하지 않은 곳으로 이동
                data[nx][ny] = 'T'  # 방문하지 않았던 곳도 방문처리
                dfs(nx, ny, distance + 1)  # 거리를 하나 증가
                data[nx][ny] = "."  # 원래 상태로 돌려 놓아 다른 방향으로 다시 탐색하도록 함(while문을 사용하지 않고 계속 반복시킬 수 있음)


dfs(R - 1, 0, 1)
print(count)
