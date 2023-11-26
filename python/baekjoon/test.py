# 5 // 점의 갯수
# 55 // 퍼센티지
# 0 0
# 10 10
# 10 0
# 0 10
# 3 3


# (y2 - y1) / (x2 - x2)

# n = int(input())
# p = int(input())
# point = []
# for i in range(n):
#     point = tuple(map(int, input().split()))
#
# x = 0
# y = 0
# tmpx = 0
# tmpy = 0
# firstx, firsty = map(int, point[0])
# for tmpx, tmpy in point[1:]:
#     (tmpx - firstx) / (tmpy - firsty)x +


import random
import time

n = int(input())
per = int(input())
want = n * per // 100 + (1 if n * per % 100 != 0 else 0)
v = [tuple(map(int, input().split())) for _ in range(n)]


def cnt(x, y, points):
    return sum((y[1] - x[1]) * (i[0] - x[0]) == (i[1] - x[1]) * (y[0] - x[0]) for i in points)


rd = random.Random()
rd.seed((int((time.time() * 1000000) % 1000000007)))

for _ in range(150):
    a = rd.randint(0, n - 1)
    b = rd.randint(0, n - 1)
    while a == b:
        b = rd.randint(0, n - 1)

    if cnt(v[a], v[b], v) >= want:
        print("possible")
        break
else:
    print("impossible")


